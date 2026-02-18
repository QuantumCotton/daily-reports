// ESH Operations Hub - Main Application JavaScript
// Handles API calls, state management, view switching, and real-time updates

// Global Configuration
const API_BASE_URL = 'http://107.172.20.181:8002';
const REALTIME_INTERVAL = 5000; // 5 seconds
const TOKEN_KEY = 'esh_auth_token';
const USER_KEY = 'esh_current_user';

// Application State
let appState = {
    currentUser: null,
    currentProject: null,
    projects: [],
    users: [],
    tasks: [],
    messages: [],
    notifications: [],
    isLoading: false,
    activeView: 'kanban',
    authToken: null,
    wsConnection: null,
    lastUpdate: null
};

// Initialize Application
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

async function initializeApp() {
    try {
        showLoading(true);
        
        // Load authentication state
        await loadAuthState();
        
        // Initialize UI components
        initializeUI();
        
        // Load initial data
        await loadInitialData();
        
        // Start real-time updates
        startRealTimeUpdates();
        
        // Setup global event listeners
        setupEventListeners();
        
        console.log('ESH Operations Hub initialized successfully');
        
    } catch (error) {
        console.error('Failed to initialize app:', error);
        showError('Failed to initialize application');
    } finally {
        showLoading(false);
    }
}

// Authentication Functions
async function loadAuthState() {
    const token = localStorage.getItem(TOKEN_KEY);
    const userData = localStorage.getItem(USER_KEY);
    
    if (token && userData) {
        appState.authToken = token;
        appState.currentUser = JSON.parse(userData);
        
        // Verify token with server
        try {
            const response = await apiCall('/api/auth/verify', {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            });
            
            if (!response.valid) {
                clearAuthState();
                return false;
            }
            
            appState.currentUser = response.user;
            return true;
            
        } catch (error) {
            clearAuthState();
            return false;
        }
    }
    
    // For demo purposes, auto-login with mock user
    return await autoLogin();
}

async function autoLogin() {
    // Mock authentication for development
    const mockUser = {
        id: 1,
        telegram_id: 7881105163,
        email: 'chris@esh.com',
        username: 'chris',
        full_name: 'Chris Johnson',
        role: 'admin',
        market_id: 1,
        phone: '+1234567890',
        avatar_url: 'https://picsum.photos/seed/chris/100/100',
        is_active: true
    };
    
    const mockToken = 'mock_token_' + Date.now();
    
    appState.currentUser = mockUser;
    appState.authToken = mockToken;
    
    localStorage.setItem(TOKEN_KEY, mockToken);
    localStorage.setItem(USER_KEY, JSON.stringify(mockUser));
    
    return true;
}

function clearAuthState() {
    appState.currentUser = null;
    appState.authToken = null;
    localStorage.removeItem(TOKEN_KEY);
    localStorage.removeItem(USER_KEY);
}

function getAuthToken() {
    return appState.authToken;
}

// UI Initialization
function initializeUI() {
    // Initialize view tabs
    const tabButtons = document.querySelectorAll('.tab-btn');
    tabButtons.forEach(button => {
        button.addEventListener('click', function() {
            switchView(this.dataset.view);
        });
    });
    
    // Initialize project selector
    const projectSelect = document.getElementById('projectSelect');
    if (projectSelect) {
        projectSelect.addEventListener('change', function() {
            const projectId = parseInt(this.value);
            selectProject(projectId);
        });
    }
    
    // Initialize task form
    const taskForm = document.getElementById('taskForm');
    if (taskForm) {
        taskForm.addEventListener('submit', handleTaskSubmit);
    }
    
    // Initialize message input
    const messageInput = document.getElementById('messageInput');
    const sendButton = document.getElementById('sendMessage');
    
    if (messageInput && sendButton) {
        sendButton.addEventListener('click', sendMessage);
        messageInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
            }
        });
    }
    
    // Initialize chat toggle
    const chatToggle = document.querySelector('.chat-toggle-btn');
    if (chatToggle) {
        chatToggle.addEventListener('click', toggleChat);
    }
    
    // Update user profile display
    updateUserProfileDisplay();
}

function setupEventListeners() {
    // Listen for messages from iframes
    window.addEventListener('message', handleIframeMessage);
    
    // Handle window resize
    window.addEventListener('resize', debounce(() => {
        // Resize handlers
    }, 250));
    
    // Handle keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        // Ctrl/Cmd + K for quick search
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            // Focus project selector or search
        }
        
        // Escape to close modals
        if (e.key === 'Escape') {
            closeAllModals();
        }
    });
    
    // Handle beforeunload
    window.addEventListener('beforeunload', function(e) {
        if (hasUnsavedChanges()) {
            e.preventDefault();
            e.returnValue = 'You have unsaved changes. Are you sure you want to leave?';
        }
    });
}

function handleIframeMessage(event) {
    const { type, data } = event.data;
    
    switch (type) {
        case 'taskUpdated':
            handleTaskUpdate(data);
            break;
        case 'editTask':
            openTaskModal(data.task);
            break;
        case 'quickAddTask':
            openTaskModal(null, data.date);
            break;
        case 'projectChanged':
            // Handle project change from iframe
            break;
        default:
            console.log('Unknown message type:', type);
    }
}

// Data Loading Functions
async function loadInitialData() {
    try {
        // Load projects
        await loadProjects();
        
        // Load users
        await loadUsers();
        
        // Load messages
        await loadMessages();
        
        // Load notifications
        await loadNotifications();
        
        // Select first project if none selected
        if (appState.projects.length > 0 && !appState.currentProject) {
            selectProject(appState.projects[0].id);
        }
        
    } catch (error) {
        console.error('Failed to load initial data:', error);
        throw error;
    }
}

async function loadProjects() {
    const response = await apiCall('/api/projects', {
        headers: {
            'Authorization': `Bearer ${appState.authToken}`
        }
    });
    
    appState.projects = response.projects || [];
    updateProjectSelector();
}

async function loadUsers() {
    const response = await apiCall('/api/users', {
        headers: {
            'Authorization': `Bearer ${appState.authToken}`
        }
    });
    
    appState.users = response.users || [];
    updateUserSelectOptions();
}

async function loadMessages() {
    if (!appState.currentProject) return;
    
    const response = await apiCall(`/api/projects/${appState.currentProject.id}/messages`, {
        headers: {
            'Authorization': `Bearer ${appState.authToken}`
        }
    });
    
    appState.messages = response.messages || [];
    renderMessages();
}

async function loadNotifications() {
    const response = await apiCall('/api/notifications', {
        headers: {
            'Authorization': `Bearer ${appState.authToken}`
        }
    });
    
    appState.notifications = response.notifications || [];
    updateNotificationBadge();
}

// UI Update Functions
function updateProjectSelector() {
    const selector = document.getElementById('projectSelect');
    if (!selector) return;
    
    selector.innerHTML = '<option value="">Select Project...</option>';
    
    appState.projects.forEach(project => {
        const option = document.createElement('option');
        option.value = project.id;
        option.textContent = project.name;
        selector.appendChild(option);
    });
    
    if (appState.currentProject) {
        selector.value = appState.currentProject.id;
    }
}

function updateUserSelectOptions() {
    const select = document.getElementById('taskAssignee');
    if (!select) return;
    
    select.innerHTML = '<option value="">Unassigned</option>';
    
    appState.users.forEach(user => {
        const option = document.createElement('option');
        option.value = user.id;
        option.textContent = user.full_name;
        select.appendChild(option);
    });
}

function updateUserProfileDisplay() {
    const userAvatar = document.querySelector('.user-avatar');
    const userName = document.querySelector('.user-name');
    
    if (appState.currentUser) {
        if (userAvatar) {
            userAvatar.src = appState.currentUser.avatar_url || `https://picsum.photos/seed/${appState.currentUser.username}/40/40`;
            userAvatar.alt = appState.currentUser.full_name;
        }
        
        if (userName) {
            userName.textContent = appState.currentUser.full_name;
        }
    }
}

function updateNotificationBadge() {
    const badge = document.querySelector('.notification-badge');
    if (!badge) return;
    
    const unreadCount = appState.notifications.filter(n => !n.is_read).length;
    
    if (unreadCount > 0) {
        badge.textContent = unreadCount > 9 ? '9+' : unreadCount;
        badge.style.display = 'flex';
    } else {
        badge.style.display = 'none';
    }
}

// View Management
function switchView(viewName) {
    if (appState.activeView === viewName) return;
    
    // Update tab buttons
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    document.querySelector(`[data-view="${viewName}"]`).classList.add('active');
    
    // Update tab content
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.remove('active');
    });
    document.getElementById(viewName).classList.add('active');
    
    // Update active view
    appState.activeView = viewName;
    
    // Notify iframes of view change
    notifyIframesOfProjectChange();
}

function selectProject(projectId) {
    const project = appState.projects.find(p => p.id === projectId);
    
    if (project) {
        appState.currentProject = project;
        
        // Update selector
        const selector = document.getElementById('projectSelect');
        if (selector) {
            selector.value = projectId;
        }
        
        // Reload data for new project
        loadMessages();
        
        // Notify iframes
        notifyIframesOfProjectChange();
    }
}

function notifyIframesOfProjectChange() {
    const iframes = document.querySelectorAll('.view-frame');
    
    iframes.forEach(iframe => {
        if (iframe.contentWindow) {
            iframe.contentWindow.postMessage({
                type: 'projectChanged',
                project: appState.currentProject
            }, '*');
        }
    });
}

// Task Management
function openTaskModal(task = null, defaultDueDate = null) {
    const modal = document.getElementById('taskModal');
    const form = document.getElementById('taskForm');
    const title = document.getElementById('modalTitle');
    
    if (!modal || !form) return;
    
    // Reset form
    form.reset();
    form.dataset.taskId = '';
    
    if (task) {
        // Edit mode
        title.textContent = 'Edit Task';
        form.dataset.taskId = task.id;
        
        // Populate form
        document.getElementById('taskTitle').value = task.title || '';
        document.getElementById('taskDescription').value = task.description || '';
        document.getElementById('taskAssignee').value = task.assignee_id || '';
        document.getElementById('taskPriority').value = task.priority || 'medium';
        document.getElementById('taskStage').value = task.stage || 'backlog';
        
        if (task.due_date) {
            const date = new Date(task.due_date);
            document.getElementById('taskDueDate').value = date.toISOString().slice(0, 16);
        }
        
        document.getElementById('taskEstimatedHours').value = task.estimated_hours || '';
        
    } else {
        // Create mode
        title.textContent = 'Create New Task';
        
        if (defaultDueDate) {
            document.getElementById('taskDueDate').value = defaultDueDate;
        }
        
        if (appState.currentProject) {
            // Set default assignee to current user
            document.getElementById('taskAssignee').value = appState.currentUser.id;
        }
    }
    
    // Show modal
    modal.classList.add('show');
}

function closeTaskModal() {
    const modal = document.getElementById('taskModal');
    if (modal) {
        modal.classList.remove('show');
    }
}

async function handleTaskSubmit(event) {
    event.preventDefault();
    
    const form = event.target;
    const taskId = form.dataset.taskId;
    const isEdit = !!taskId;
    
    const formData = new FormData(form);
    const taskData = {
        title: formData.get('title'),
        description: formData.get('description'),
        assignee_id: formData.get('assignee_id') ? parseInt(formData.get('assignee_id')) : null,
        priority: formData.get('priority'),
        stage: formData.get('stage'),
        due_date: formData.get('due_date') || null,
        estimated_hours: formData.get('estimated_hours') ? parseFloat(formData.get('estimated_hours')) : null
    };
    
    if (appState.currentProject) {
        taskData.project_id = appState.currentProject.id;
    }
    
    try {
        showLoading(true);
        
        let response;
        if (isEdit) {
            response = await apiCall(`/api/tasks/${taskId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${appState.authToken}`
                },
                body: JSON.stringify(taskData)
            });
        } else {
            response = await apiCall('/api/tasks', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${appState.authToken}`
                },
                body: JSON.stringify(taskData)
            });
        }
        
        // Add message to chat
        if (response.task) {
            const message = isEdit 
                ? `Task "${response.task.title}" was updated`
                : `New task "${response.task.title}" was created`;
            
            await addSystemMessage(message);
        }
        
        closeTaskModal();
        
        // Refresh iframes
        refreshIframes();
        
    } catch (error) {
        console.error('Failed to save task:', error);
        showError('Failed to save task');
    } finally {
        showLoading(false);
    }
}

// Chat Functions
async function sendMessage() {
    const input = document.getElementById('messageInput');
    const content = input.value.trim();
    
    if (!content || !appState.currentProject) return;
    
    try {
        const response = await apiCall(`/api/projects/${appState.currentProject.id}/messages`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${appState.authToken}`
            },
            body: JSON.stringify({
                content: content,
                message_type: 'text'
            })
        });
        
        if (response.message) {
            appState.messages.push(response.message);
            renderMessages();
            input.value = '';
        }
        
    } catch (error) {
        console.error('Failed to send message:', error);
        showError('Failed to send message');
    }
}

function renderMessages() {
    const container = document.getElementById('messagesContainer');
    if (!container) return;
    
    container.innerHTML = '';
    
    appState.messages.forEach(message => {
        const messageEl = createMessageElement(message);
        container.appendChild(messageEl);
    });
    
    // Scroll to bottom
    container.scrollTop = container.scrollHeight;
}

function createMessageElement(message) {
    const div = document.createElement('div');
    div.className = `message ${message.message_type || 'text'}`;
    
    const time = new Date(message.created_at).toLocaleTimeString('en-US', {
        hour: '2-digit',
        minute: '2-digit'
    });
    
    if (message.message_type === 'system') {
        div.innerHTML = `
            <div class="message-content">
                ${message.content}
            </div>
            <div class="message-time">${time}</div>
        `;
    } else {
        const sender = message.sender_name || 'Unknown';
        div.innerHTML = `
            <div class="message-header">
                <strong>${sender}</strong>
                <span class="message-time">${time}</span>
            </div>
            <div class="message-content">
                ${message.content}
            </div>
        `;
    }
    
    return div;
}

async function addSystemMessage(content) {
    if (!appState.currentProject) return;
    
    try {
        const response = await apiCall(`/api/projects/${appState.currentProject.id}/messages`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${appState.authToken}`
            },
            body: JSON.stringify({
                content: content,
                message_type: 'system'
            })
        });
        
        if (response.message) {
            appState.messages.push(response.message);
            renderMessages();
        }
        
    } catch (error) {
        console.error('Failed to add system message:', error);
    }
}

function toggleChat() {
    const sidebar = document.querySelector('.chat-sidebar');
    if (sidebar) {
        sidebar.classList.toggle('collapsed');
    }
}

// Real-time Updates
function startRealTimeUpdates() {
    // Load initial data
    performRealTimeUpdate();
    
    // Set up interval
    setInterval(performRealTimeUpdate, REALTIME_INTERVAL);
    
    // Set up WebSocket if available
    setupWebSocket();
}

async function performRealTimeUpdate() {
    if (!appState.currentProject) return;
    
    try {
        // Update messages
        const messagesResponse = await apiCall(`/api/projects/${appState.currentProject.id}/messages`, {
            headers: {
                'Authorization': `Bearer ${appState.authToken}`
            }
        });
        
        if (messagesResponse.messages && messagesResponse.messages.length !== appState.messages.length) {
            appState.messages = messagesResponse.messages;
            renderMessages();
        }
        
        // Update notifications
        const notificationsResponse = await apiCall('/api/notifications?unread_only=true', {
            headers: {
                'Authorization': `Bearer ${appState.authToken}`
            }
        });
        
        if (notificationsResponse.notifications) {
            const unreadCount = notificationsResponse.notifications.length;
            const currentUnreadCount = appState.notifications.filter(n => !n.is_read).length;
            
            if (unreadCount !== currentUnreadCount) {
                appState.notifications = [...appState.notifications.filter(n => n.is_read), ...notificationsResponse.notifications];
                updateNotificationBadge();
            }
        }
        
        appState.lastUpdate = new Date();
        
    } catch (error) {
        console.error('Real-time update failed:', error);
    }
}

function setupWebSocket() {
    try {
        const wsUrl = API_BASE_URL.replace('http', 'ws') + '/ws/notifications';
        appState.wsConnection = new WebSocket(wsUrl);
        
        appState.wsConnection.onopen = function() {
            console.log('WebSocket connected');
            
            // Send authentication
            this.send(JSON.stringify({
                type: 'auth',
                token: appState.authToken
            }));
        };
        
        appState.wsConnection.onmessage = function(event) {
            const data = JSON.parse(event.data);
            handleWebSocketMessage(data);
        };
        
        appState.wsConnection.onclose = function() {
            console.log('WebSocket disconnected');
            // Attempt to reconnect after 5 seconds
            setTimeout(setupWebSocket, 5000);
        };
        
        appState.wsConnection.onerror = function(error) {
            console.error('WebSocket error:', error);
        };
        
    } catch (error) {
        console.error('Failed to setup WebSocket:', error);
    }
}

function handleWebSocketMessage(data) {
    switch (data.type) {
        case 'new_notification':
            appState.notifications.unshift(data.data);
            updateNotificationBadge();
            showNotification(data.data);
            break;
        case 'task_updated':
            handleTaskUpdate(data.data);
            break;
        case 'new_message':
            appState.messages.push(data.data);
            renderMessages();
            break;
        default:
            console.log('Unknown WebSocket message:', data);
    }
}

function handleTaskUpdate(task) {
    // Update task in local state
    const index = appState.tasks.findIndex(t => t.id === task.id);
    if (index !== -1) {
        appState.tasks[index] = task;
    } else {
        appState.tasks.push(task);
    }
    
    // Show notification
    showNotification({
        title: 'Task Updated',
        message: `Task "${task.title}" was updated`,
        type: 'task_updated'
    });
}

// Utility Functions
function showLoading(show) {
    const overlay = document.getElementById('loadingOverlay');
    if (overlay) {
        overlay.style.display = show ? 'flex' : 'none';
    }
}

function showError(message) {
    showNotification({
        title: 'Error',
        message: message,
        type: 'error'
    });
}

function showNotification(notification) {
    // Create toast notification
    const toast = document.createElement('div');
    toast.className = 'toast notification';
    toast.innerHTML = `
        <div class="toast-header">
            <strong>${notification.title}</strong>
            <button class="toast-close" onclick="this.parentElement.parentElement.remove()">&times;</button>
        </div>
        <div class="toast-body">
            ${notification.message}
        </div>
    `;
    
    // Add to page
    document.body.appendChild(toast);
    
    // Position toast
    toast.style.position = 'fixed';
    toast.style.top = '20px';
    toast.style.right = '20px';
    toast.style.zIndex = '9999';
    toast.style.background = 'var(--bg-secondary)';
    toast.style.border = '1px solid var(--bg-tertiary)';
    toast.style.borderRadius = 'var(--radius-md)';
    toast.style.padding = 'var(--spacing-md)';
    toast.style.boxShadow = 'var(--shadow-lg)';
    toast.style.maxWidth = '400px';
    toast.style.animation = 'slideInRight 0.3s ease';
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        if (toast.parentElement) {
            toast.remove();
        }
    }, 5000);
}

function closeAllModals() {
    document.querySelectorAll('.modal').forEach(modal => {
        modal.classList.remove('show');
    });
}

function hasUnsavedChanges() {
    // Check if any forms have unsaved changes
    const forms = document.querySelectorAll('form');
    
    for (const form of forms) {
        const formData = new FormData(form);
        const initialData = form.dataset.initialData;
        
        if (initialData) {
            // Compare current form data with initial data
            const currentData = JSON.stringify(Object.fromEntries(formData));
            if (currentData !== initialData) {
                return true;
            }
        }
    }
    
    return false;
}

function refreshIframes() {
    const iframes = document.querySelectorAll('.view-frame');
    
    iframes.forEach(iframe => {
        if (iframe.contentWindow && iframe.contentWindow.refreshKanban) {
            iframe.contentWindow.refreshKanban();
        }
        if (iframe.contentWindow && iframe.contentWindow.refreshCalendar) {
            iframe.contentWindow.refreshCalendar();
        }
        if (iframe.contentWindow && iframe.contentWindow.refreshTimeline) {
            iframe.contentWindow.refreshTimeline();
        }
    });
}

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// API Helper Function
async function apiCall(url, options = {}) {
    const defaultOptions = {
        headers: {
            'Content-Type': 'application/json'
        }
    };
    
    const finalOptions = {
        ...defaultOptions,
        ...options,
        headers: {
            ...defaultOptions.headers,
            ...options.headers
        }
    };
    
    const fullUrl = url.startsWith('http') ? url : `${API_BASE_URL}${url}`;
    
    try {
        const response = await fetch(fullUrl, finalOptions);
        
        if (!response.ok) {
            if (response.status === 401) {
                clearAuthState();
                window.location.reload();
                return;
            }
            
            const errorText = await response.text();
            throw new Error(`API Error: ${response.status} - ${errorText}`);
        }
        
        const contentType = response.headers.get('content-type');
        if (contentType && contentType.includes('application/json')) {
            return await response.json();
        }
        
        return await response.text();
        
    } catch (error) {
        console.error('API call failed:', error);
        throw error;
    }
}

// Export functions for global access
window.eshApp = {
    // State
    getState: () => appState,
    getCurrentUser: () => appState.currentUser,
    getCurrentProject: () => appState.currentProject,
    
    // Authentication
    getAuthToken,
    clearAuthState,
    
    // UI Functions
    openTaskModal,
    closeTaskModal,
    showLoading,
    showError,
    showNotification,
    
    // API Functions
    apiCall,
    
    // View Management
    switchView,
    selectProject
};

// Make functions available for iframes
window.openTaskModal = openTaskModal;
window.closeTaskModal = closeTaskModal;
window.showLoading = showLoading;
window.showError = showError;
window.getAuthToken = getAuthToken;
window.API_BASE_URL = API_BASE_URL;

// Add CSS animation for toasts
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    .toast {
        font-family: inherit;
    }
    
    .toast-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 8px;
    }
    
    .toast-header strong {
        color: var(--text-primary);
    }
    
    .toast-close {
        background: none;
        border: none;
        color: var(--text-muted);
        font-size: 18px;
        cursor: pointer;
        padding: 0;
        line-height: 1;
    }
    
    .toast-close:hover {
        color: var(--text-primary);
    }
    
    .toast-body {
        color: var(--text-secondary);
    }
`;
document.head.appendChild(style);

console.log('ESH Operations Hub app.js loaded');