import csv
import re
import os

# Raw data from user
raw_data = """Business	Category	Email	Phone	Priority
Property Boss LLC	Property Management	Staff@propertybossllc.com	(772) 621-2273	High
Coastal Management Professionals	Property Management	Accounting@cpmfl.com	561-310-9672	High
South Florida Realty Management	Property Management	info@floridapm.net ✓	—	Medium
Maaco Auto Body & Painting Stuart	Auto Body Shop	stuartflmaaco@bellsouth.net	1204650995	High
Signature Property Management	hoa	Ira@signaturepropertymgmt.com	772) 219-4474	High
Martin, FL Property Management Companies	hoa	info@pamartinfl.gov	(772) 631-6450	High
Professional HOA & COA Services in Martin County	hoa	esposito@macombgov.org	1016146955	High
Coastal Property Management – Stuart & Jupiter – Condominium ...	hoa	susan.palmieri@cpmfl.com	772-600-8900	High
Palm Beach and Martin Counties Property Management	hoa	info@pa.martin.fl.us	(772) 288-5608	High
Martin Property Management, Martin Property ...	hoa	info@pa.martin.fl.us	781.532.8250	High
Properties & Communities	hoa	kevin@stewartteam.com	(248) 759-5474	High
St. Lucie and Martin County Property Management Agency	hoa	info@mgtspec.com	(877) 665-5505	High
Trusted Cleaning Company in Stuart FL	cleaning	ncsnatyka@gmail.com	772-220-7915	High
Commercial Cleaning Services in Stuart, Florida	cleaning	office@customcleaningtc.com	561-935-8549	High
Stuart, FL Commercial Cleaning and Janitorial Services	cleaning	info@stuartmartinchamber.org	772-220-7915	High
Cleaning Services Stuart, Jensen Beach FL 772-205-3994	cleaning	info@dustintimecleaning.com	772-205-3994	High
Fresh and Clean Cleaning Service, Stuart, FL 34997, US	cleaning	info@cleanandfreshcleaning.com	786-920-2105	High
Commercial Cleaning Services in Stuart, FL	cleaning	office@customcleaningtc.com	772-287-1088	High
Florida Investment Properties	real_estate	nabertke@gmail.com	(772) 763-8506	High
Treasure Coast Real Estate	real_estate	John@tccommercialre.com	(772) 288-0632	High
Treasure Coast Realty Group	real_estate	Meluke@treasurecoastrg.com	(772) 288-0632	High
Excellent Investment	real_estate	sales@stewartsresort.com	1514742893	High
RE/MAX Gold	real_estate	Meconnormckinney.re@gmail.com	973-508-9425	High
Estate Listings on	real_estate	spiersrealestate@gmail.com	(868) 622-2685	High
Luxury Homes of the Treasure Coast	real_estate	Kevin@TradewindRe.com	800-274-6637	High
Treasure Coast Fl. Real Estate Articles	real_estate	John@tccommericalre.com	(772) 288-0632	High
Treasure Coast Real Estate: Treasure Coast Homes for Sale	real_estate	info@treasurecoastmlssearch.com	1000570592	High
Top Rated Car Dealerships near Stuart, FL	auto_shop	—	772-872-0501	High
New & Used Cars For Sale	auto_shop	info@wallaceautogroup.com ✓	772.218.7007	High
Wallace Chevrolet	auto_shop	ewallace@wallacechev.com	772-286-0155	High
All Dealers in Stuart, FL 34997	auto_shop	sales@jldauto.net	(772) 288-2099	High
Starling Buick GMC Dealership in Stuart, FL	auto_shop	info@starlingbuickgmcstuart.com	(772) 210-0299	High
Honda Dealership Stuart FL	auto_shop	events@hohmartin.org	(772) 286-4673	High
Treasure Coast Toyota Of Stuart	auto_shop	info@treasurecoasttoyotaofstuart.com	(772) 283-8300	High
Wallace Chrysler, Jeep, Dodge, Ram & Wagoneer Dealership In ...	auto_shop	users@wallaceautogroup.net	772-291-5172	High
Martin County Condo & Homeowners Association Attorneys	apartment_complex	jeanette.m.lugo@gmail.com	(772) 293-0352	High
Martin Downs Property Owners Association: Home	apartment_complex	reception@mdpoa.org	(772) 283-4746	High
Beau Rivage Estates HOA	apartment_complex	fenglund@bellsouth.net	1313679510	High
Martin Meadows | Home Owners Association – MMHOA	apartment_complex	admin@martinmeadows.com ✓	—	High
Circle Bay Yacht Club	apartment_complex	—	772.287.0990	High
The Landings of Martin County | HOA in Stuart, FL	apartment_complex	tkryzda@martin.fl.us	(772) 288-5939	High
Master Association - Welcome to Hammock Creek	apartment_complex	Master.HammockCreek@gmail.com	772-334-8900	High
Community Association - Reblawpa	apartment_complex	jee@reblawpa.com	(772) 287-8045	High
Treasure Coast, FL - TourSeniorLiving.org	healthcare	—	(772) 732-1223	High
The Best Assisted Living Facilities in Port St. Lucie, FL	healthcare	info@brightenalf.comALF	772-237-5165	High
Treasure Coast Senior Living Communities	healthcare	faithmarie@tc-seniorliving.com	(954) 549-7566	High
JD Treasure Coast ALF in Florida - Oasis Senior Advisors	healthcare	jlibratore@youroasisadvisor.com	(772) 214-0806	High
The Gardens of Port St. Lucie Senior Living	healthcare	info@sinceriseniorliving.com	—	High
Castlewood Assisted Living Residence	healthcare	brittanyf.cal@outlook.com	(605) 793-2234	High
jd treasure coast assisted living facility, llc - Florida Health Finder	healthcare	info@quality.healthfinder.fl.gov	(646) 823-7554	High
Treasure Coast ALF | Port St. Lucie, Florida Senior Living Community	healthcare	info@seniorplacementgroup.com	(561) 510-8367	High
10 Best Assisted Living Facilities in St Lucie County, FL	healthcare	info@aplaceformom.com ✓	(772) 207-7622	High
Independent Living - CarePatrol of The Treasure Coast	healthcare	lvelez@carepatrol.com	(321) 273-2424	High
THE 10 BEST Restaurants in Stuart (Updated February 2026)	restaurant	sales@tripadvisor.com ✓	—	High
Dining - Historic Downtown Stuart	restaurant	info@downtownstuartflorida.com ✓	—	High
The 10 Best Restaurants Near Me in Stuart, FL | OpenTable	restaurant	info@opentable.com	—	High
Home - BOATHOUSE - Fish restaurant in Stuart, FL	restaurant	info@stuartboathouse.com	—	High
The Sailor's Return Restaurant in Stuart Florida (772) 872-7250	restaurant	info@thesailorsreturn.com	—	High
Stuart Fish Grill - Stuart, FL	restaurant	info@stuartfishgrill.com ✓	—	High
The Black Marlin | Bar & Restaurant in Historic Stuart, Florida	restaurant	contact@theblackmarlin.net ✓	—	High
Hudson's On The River | Waterfront Dining | Best restaurants in ...	restaurant	info@hudsonontheriver.com	—	High
Martin North Hospital | Cleveland Clinic	healthcare	roiwestonfl@ccf.org	(772) 287-5200	High
Hospitals near Stuart, FL - Healthgrades	healthcare	admin@healthgrades.com ✓	—	High
Martin North Hospital | Cleveland Clinic Florida	healthcare	PHPPRcontactus@providence.org	(772) 287-5200	High
HCA Florida Stuart Emergency	healthcare	info@stuartmartinchamber.org	(772) 203-8015	High
HOSPITALS/EMERGENCY ROOM Category | Stuart Martin County ...	healthcare	info@business.stuartmartinchamber.org	—	High
Cleveland Clinic Martin Health-Stuart in Stuart, FL - Health US News	healthcare	singhr@ccf.org	(772) 223-2300	High
Martin Memorial Hospital South, Stuart, FL - WellMed	healthcare	info@doctors.wellmedhealthcare.com	—	High
Cleveland Clinic Martin North Hospital - Medicare	healthcare	PHPPRcontactus@providence.org	772.287.5200	High
Treasure Coast Auto Spa: Treasure Coast Auto Detailing	detailing	ceramicprotcas@treasurecoastautospa.com	(772) 204-1286	High
MDS Auto Detailing	detailing	info@mdsautodetailing.com	—	High
Doctor Detail of the Treasure Coast: Auto Detailing	detailing	info@ddoftc.com	—	High
Lio's Quality detailing	detailing	liosqdllc@gmail.com	(772) 348-9559	High
Florida Finest Detailing: Home	detailing	ffdetailing77@gmail.com	772-377-0077	High
Ceramic Coating Experts | Best Auto Detailing in Port St Lucie, Fort ...	detailing	showtimedetailing28@gmail.com	2006217259	High
Lion Heartz Detailing: Mobile Auto Detailing Services	detailing	—	(772)-480-4133	High
Booking - Showtime Detailing	detailing	info@showtimedetailing.org	—	High
HOME - DA Detailing - PSL	detailing	info@dadetailingpsl.com	—	High
Full Service Catering | Treasure Coast | Home	restaurant	info@snlevents.com	—	High
Catering services along the Treasure Coast, FL - Corporate Caterers	restaurant	info@corporatecaterers.com	—	High
True Roots Catering | Vero Beach | Stuart | Palm Beach	restaurant	info@truerootscatering.com ✓	—	High
Catering Revolution: Catering Services in Stuart, FL	restaurant	info@cateringrevolution.com	—	High
Premier Catering Services in Fort Pierce | Shelly's Bistro	restaurant	info@shellyzbistro.com	—	High
CT Catering	restaurant	info@cheftablecatering.com	—	High
Caterer Service in Treasure Coast, FL | Corporate Caterers - Menu	restaurant	joe.stellato@gmail.com	772 286-0877	High
Purple Olive: Catering Service | Saint Augustine, FL	restaurant	purpleolive2004@gmail.com	(904) 461-1250	High
Investment properties Martin County FL - Landmark Realty	real_estate	info@landmarkinvestmentsflorida.com	—	High
CRA Investment Program | Martin County Florida	real_estate	info@martin.fl.us	—	High
Martin County, FL commercial real estate for sale - Realmo	real_estate	info@realmo.com	—	High
Martin County Existing Condo Sales Climb - MIAMI REALTORS®	real_estate	info@miamirealtors.com	—	High
Martin County, FL Homes for Sale - The Zecca Group	real_estate	info@thezeccagroup.com	—	High
Martin County Real Estate Market Update – September 2025	real_estate	info@echofineproperties.com	—	High
Office Cleaning in Stuart FL | Serving Treasure Coast	cleaning	info@customcleaningtc.com	—	High
Snap Clean: Cleaning Services in Treasure Coast, FL	cleaning	hello@snapcleanservices.com ✓	—	High
Commercial Cleaning Services in Palm Beach and Treasure Coast	cleaning	info@vanguardcleaning.com	—	High
Janitorial Services - FREEDOM COAST CLEANING SERVICES ...	cleaning	info@freedomcoastcleaningservices.com	—	High
Treasure Coast Commercial Cleaning and Janitorial Services	cleaning	info@cleanproservicesllc.com	—	High
Office Cleaning Services in South Florida	cleaning	info@akbuildingservices.com ✓	—	High
Top Treasure Coast Cleaning Company 360 Cleaning Solutions LLC	cleaning	info@treasurecoastcleaningsolutions.com	—	High
Reliable Cleaning Services Of Treasure Coast LLC - Home	cleaning	info@rcsoftreasurecoast.com	—	High
Commercial Cleaning - Eastside Chem-Dry	cleaning	contact@eastsidechemdry.com ✓	—	High
General Cleaning and Janitorial Services - Servpro	cleaning	info@servpro.com	—	High
B & S Auto Detailing LLC: Superior Auto Detailing Services in Stuart ...	detailing	info@bnsautodetailing.com	—	High
Mobile Car Detailing in Stuart, FL | AIRLITE	detailing	info@airliteautodetailing.com	—	High
Cameruski's Auto Detailing: Ceramic Coating & Detailing in Stuart, FL	detailing	info@camskisdetailing.com	—	High
B&B Mobile Detailing - Stuart - Book Online - Prices, Reviews, Photos	detailing	info@booksy.com ✓	—	High
Stuart mobile detailing - JonathanDetail	detailing	info@jonathandetailstuartflorida.com	—	High
Service Areas | Mobile Detailing in Martin County & Surrounding ...	detailing	info@harvsdetails.com	—	High
MonkMobileDetailing: HOME	detailing	monkmobiledetailing@gmail.com	(772) 202-8871	High
Tony's Showroom Finish Detailing: Top Car Detailing Services in ...	detailing	Stuart@auto-genie.co.uk	(772) 882-5877	High
Top Stuart, Florida Property Management Companies | APM	property_mgmt	info@allpropertymanagement.com ✓	—	High
24 Best Property Manager Companies in Stuart, FL - KeyCrew	property_mgmt	contact@keycrew.co ✓	—	High
Real Property Management Sailfish Coast - Stuart FL Property ...	property_mgmt	info@rpmsailfishcoast.com ✓	—	High
Top Property Management Companies in Stuart, FL | Birdeye	property_mgmt	info@reviews.birdeye.com	—	High
Vacation Rental & Airbnb Management in Stuart, FL	property_mgmt	info@hometeamluxuryrentals.com ✓	—	High
Warehouses for Lease in Stuart, FL | Crexi	warehouse	info@crexi.com ✓	—	High
Stuart Industrial and Warehouse Space For Rent & Lease - Showcase	warehouse	info@showcase.com ✓	—	High
Stuart, FL Industrial & Warehouse Spaces for Rent - PropertyShark	warehouse	info@propertyshark.com	—	High
Stuart, FL Industrial & Warehouse Space for Rent - CommercialSearch	warehouse	info@commercialsearch.com	—	High
Martin County, FL Warehouses for Rent & Lease | Realmo	warehouse	info@realmo.com	—	High
Stuart, FL Industrial & Warehouse Spaces for Rent - Commercial Cafe	warehouse	info@commercialcafe.com	—	High
Commercial Industrial Space	warehouse	info@treasurecoastcommercialrealestate.com	—	High
Stuart, FL Industrial Space For Lease - CityFeet	warehouse	info@cityfeet.com ✓	—	High
House Cleaning Services in Stuart , FL 34997	cleaning	info@cleaningsvcstuartfl.com	—	High
Home Cleaning Services	cleaning	info@keimys.com	—	High
Olaf's Window Cleaning: Stuart, FL Window Cleaning Services	cleaning	info@olafswindowcleaning.com ✓	—	High
Treasure Coast Life Real Estate Professionals	real_estate	info@treasurecoastlife.net ✓	—	High
Treasure Coast Realtors | Homes & Real Estate in Florida	real_estate	themazurssell@aol.com	(772) 286-1900	High
Investment Properties for Sale in Port St Lucie, Florida | 476+ Listings	real_estate	info@houzeo.com ✓	—	High
Bathroom Remodeling | Stuart, FL	bathroom	isaac@tileanddecorusa.com	(772)-946-1986	High
Home | Kitchen and Bath Remodel from Stuart KBF	bathroom	info@stuartkitchenbathandflooring.com ✓	—	High
Kitchen Bath & Home Design | Remodel: Stuart, Florida	bathroom	info@kitchenbathandhomedesign.com ✓	—	High
Bathroom Remodeling in Stuart, FL from Agler Kitchen, Bath & Floors	bathroom	info@aglerinteriors.com ✓	—	High
East Coast Kitchen & Bath | Remodeling Services | Stuart, FL	bathroom	info@eastcoastkitchenandbath.com	—	High
Bathroom Remodeling Services | Stuart & Port St. Lucie, FL	bathroom	isaac@tileanddecorusa.com	(772) 453-0909	High
Bathroom Remodeling - Retrofits And Renovations	bathroom	info@retrofitsandrenovations.com	—	High
Home Remodeler | DreamMaker Bath & Kitchen of SE Florida | Stuart	bathroom	info@dreammaker-stuart.com	—	High
Apartments for Rent in Stuart, FL - Homes.com	apartments	info@homes.com ✓	—	High
Stuart, FL Apartments for Rent - 579 Rentals - HotPads	apartments	info@hotpads.com ✓	—	High
Apartments for Rent in Stuart, FL - New Listings Daily - RentCafe	apartments	info@rentcafe.com	—	High
RESTAURANTS Category | Stuart Martin County Chamber of ...	restaurant	info@business.stuartmartinchamber.org	—	High
23 Fun Family Restaurants in Stuart + Martin County	restaurant	info@treasurecoastmom.com	—	High
69 Best Casual Restaurants in Stuart | OpenTable	restaurant	info@opentable.com	—	High
Stuart Apartments - PMC Property Group	property_mgmt	info@pmcpropertygroup.com ✓	—	High
New & Used Cars For Sale | Wallace Auto Group | Stuart & Ft. Pierce	auto	info@wallaceautogroup.com ✓	—	High
Victory Auto Store: Used Car Dealership in Stuart, FL	auto	info@victoryautostore.com ✓	—	High
Car Dealerships in Stuart, FL 34997 - Kelley Blue Book	auto	sales@jldauto.net	772-283-6000	High
Starling Buick GMC Stuart Named Best Car Dealer in Stuart for 2025	auto	info@starlingbuickgmcstuart.com	—	High
Wallace Chevrolet - Chevrolet Dealership In Stuart, FL	auto	info@wallacechevrolet.com	—	High
Encompass Health Rehabilitation Hospital, an affiliate of Martin Health	healthcare	info@encompasshealth.com	—	High
Cleveland Clinic Martin North Hospital (100044) - Free Profile	healthcare	sales@ahd.com ✓	—	High
Cleveland Clinic Martin North Hospital - Stuart, FL - Castle Connolly	healthcare	info@castleconnolly.com ✓	—	High
Luxury Estate and Home Property Management | South Florida ...	hoa	info@ihemfl.com	—	High
Evergreen Property Owners Association: Home	hoa	info@evergreenpoa.com	—	High
Jupiter Stuart Port St. Lucie Custom Cabinets, Refacing & Remodeling	kitchen	info@kitchentuneup.com	—	High
RDI Kitchens - Home Remodeling | Stuart FL	kitchen	info@rdikitchens.com	—	High
Kitchen Remodeling in Stuart FL - Home & Beyond Services	kitchen	info@homeandbeyondfl.com ✓	—	High
Outdoor Kitchen Design Services In Stuart, Fl - Island Living & Patio	kitchen	info@islandlivingpatio.com ✓	—	High
Stuart Kitchen Remodeling: Expert Kitchen Remodeling in Stuart	kitchen	info@stuartkitchenremodeling.com	—	High
The Estates at Stuart in Stuart, FL | PMC Property Group Apartments	apartments	info@pmcpropertygroup.com ✓	—	High
Mobile Car Detailing in Stuart, FL | AIRLITE	detailing	info@airliteautodetailing.com	—	High
RV detail stuart florida - JonathanDetail - Stuart car detailing	detailing	info@jonathandetailstuartflorida.com	—	High
Car Detailing in Stuart FL | Mobile Car Detailing - National Detail Pros	detailing	info@nationaldetailpros.com	—	High
St. Lucie/Treasure Coast Chapter - Florida Assisted Living Association	apartments	info@fala.org	—	High
REAL ESTATE/PROPERTY MANAGEMENT Category | Stuart Martin ...	property_mgmt	info@business.stuartmartinchamber.org	—	High
MEYERS GROUP – Meyers Group, founded by respected real ...	property_mgmt	info@meyersgroup.net ✓	—	High
Best assisted living communities in Treasure Coast | SENIORS.FYI	apartments	info@seniors.fyi	—	High
Senior Living options in Treasure Coast | Oasis Senior Advisors	apartments	info@oasissenioradvisors.com	—	High
Assisted Living - CarePatrol of The Treasure Coast	apartments	info@carepatrol.com ✓	—	High
14 Assisted Living Facilities in Vero Beach, FL (with Reviews)	apartments	info@seniorhomes.com	—	High
Agler Kitchen, Bath & Floors: Flooring store in Stuart, FL	kitchen	info@aglerinteriors.com ✓	—	High
Best Restaurants in Stuart Florida	restaurant	info@stuartfishgrill.com ✓	—	High
La Grande Martier | Low-Country Cuisine in Stuart, FL	restaurant	info@grandemartier.com ✓	—	High
Mobile Car Detailing in Stuart, FL | AIRLITE	detailing	info@airliteautodetailing.com	—	High
The 10 Best Mobile Auto Detailing in Stuart, FL - PreferredMechanic	detailing	info@preferredmechanic.com	—	High
Best Auto Body Shops near Stuart, FL - Carwise.com	auto	admin@carwise.com ✓	—	High
Collision Body Shop | Wallace Auto Group In Stuart	auto	info@wallaceautogroup.com ✓	—	High
Auto Repair in Stuart | Caliber Collision	auto	admin@caliber.com ✓	—	High
The 10 Best Auto Body Repair in Stuart, FL - PreferredMechanic	auto	info@preferredmechanic.com	—	High
Kia Collision Body Shop In Stuart, FL - Wallace Kia	auto	info@wallacekiaofstuart.com ✓	—	High
Certified Collision Experts in Stuart, FL, 34994 | Auto Body Shops	auto	admin@carwise.com ✓	—	High
Featured Treasure Coast Realty Group Property Listings | Crexi.com	real_estate	info@crexi.com ✓	—	High
Treasure Island Beachfront Investment Properties	real_estate	info@mygulfcoastproperty.com ✓	—	High
New & Used Cars For Sale | Wallace Auto Group | Stuart & Ft. Pierce	auto	info@wallaceautogroup.com ✓	—	High
Wallace Chevrolet - Chevrolet Dealership In Stuart, FL	auto	info@wallacechevrolet.com ✓	—	High
Wallace Chrysler, Jeep, Dodge, Ram & Wagoneer Dealership In ...	auto	info@wallacecjd.com	—	High
CFREIA	real_estate	info@cfreia.com ✓	—	High
Best Realtor & Brokerage for Real Estate Investors on the Treasure ...	real_estate	info@echofineproperties.com	—	High
Treasure Coast Real Estate Investors Association - Meetup	real_estate	sales@meetup.com ✓	—	High
Treasure Coast Investor - BiggerPockets	real_estate	info@biggerpockets.com ✓	—	High
Our Agents | The Brokerage Treasure Coast	real_estate	info@thebrokeragetc.com	—	High
Real Treasure Coast Real Estate Blog	real_estate	info@realtreasurecoast.com ✓	—	High
Florida's Treasure Coast Offers Natural Allure for Investors in ...	real_estate	info@circlesquaredalts.com ✓	—	High
10 Amazing Bars and Restaurants in Martin County You Have to Try	restaurant	info@emilyluxton.co.uk	—	High
Waterfront Stuart	restaurant	waterfront@sandcrg.com	(772) 288-1881	High
Floridian Management Group: Florida Property Management	hoa	info@floridianmanagement.com	—	High
Mobile Car Detailing in Stuart, FL | AIRLITE	detailing	info@airliteautodetailing.com	—	High
Apartments For Rent in Stuart, FL	apartments	info@rent.com ✓	—	High
55+ Active Adult Communities in Treasure Coast - Del Webb	apartments	info@delwebb.com	—	High
Custom Kitchen Design Experts - Stuart Kitchen Remodeling	kitchen	info@stuartkitchenremodeling.com	—	High
The Real Estate Leaders of the Treasure Coast of FL	real_estate	info@stuartmartinchamber.org	772-288-1111	High
Investment Property for Sale in Port St. Lucie, FL - Mashvisor	real_estate	info@mashvisor.com ✓	—	High
Collision Body Shop | Wallace Auto Group In Stuart	auto	info@wallaceautogroup.com ✓	—	High
Kia Collision Body Shop In Stuart, FL - Wallace Kia	auto	info@wallacekiaofstuart.com ✓	—	High
Extreme Performace | Stuart, FL Automotive Customization Shop	auto	info@extremeperformance.biz	—	High
Collision Body Shop | Wallace Auto Group In Stuart	auto	info@wallaceautogroup.com ✓	—	High
Kia Collision Body Shop In Stuart, FL - Wallace Kia	auto	info@wallacekiaofstuart.com ✓	—	High
Commercial Cleaning Jobs, Employment in Stuart, FL - Indeed	cleaning	—	321-306-0622	High
Wallace Chevrolet - Chevrolet Dealership In Stuart, FL	auto	info@wallacechevrolet.com ✓	—	High
New & Used Cars For Sale | Wallace Auto Group | Stuart & Ft. Pierce	auto	info@wallaceautogroup.com ✓	—	High
Wallace Chrysler, Jeep, Dodge, Ram & Wagoneer Dealership In ...	auto	info@wallacecjd.com ✓	—	High
Mobile Car Detailing in Stuart, FL | AIRLITE	detailing	info@airliteautodetailing.com	—	High
Treasure Property Group. Real Estate Services in Florida	real_estate	info@treasurepropertygroup.com	—	High
The Brennity at Tradition Senior Living | Retirement Community	apartments	—	—	High
3 Best Assisted Living Communities in Fort Pierce South, Florida	apartments	—	—	High
The Brennity at Vero Beach Senior Living | Retirement Community	apartments	—	(772) 299-7900	High
Mobile Car Detailing in Stuart, FL | AIRLITE	detailing	info@airliteautodetailing.com	—	High
Property Management Jobs, Employment in Stuart, FL | Indeed	property_mgmt	—	6880420380	High
Home - Whitemarsh Reserve HOA	hoa	info@whitemarshreserve.com	—	High
Kitchen Remodeling Services in Stuart, FL	kitchen	info@garciaandsonsconstruct.com	772.283.8912	High
Kitchen remodeling services in Stuart - Local General Contractor	kitchen	info@garciaandsonsconstruct.com	—	High
Grand Oaks of Jensen Beach, Florida | Assisted Living and Memory ...	apartments	info@grandoaksjensenbeach.com	—	High
Collision Body Shop | Wallace Auto Group In Stuart	auto	info@wallaceautogroup.com ✓	—	High
Classic Collision Treasure Coast	auto	contact@classiccollision.com ✓	—	High
3776 SE Dixie Hwy Stuart, FL 34997	auto	info@autodentrepair.co	—	High
Kia Collision Body Shop In Stuart, FL - Wallace Kia	auto	info@wallacekiaofstuart.com ✓	—	High
Industrial Warehouse Space	warehouse	info@treasurecoastcommercialrealestate.com	—	High
Mobile Car Detailing in Stuart, FL | AIRLITE	detailing	info@airliteautodetailing.com	—	High
Wallace Chevrolet - Chevrolet Dealership In Stuart, FL	auto	info@wallacechevrolet.com	—	High
New & Used Cars For Sale | Wallace Auto Group | Stuart & Ft. Pierce	auto	info@wallaceautogroup.com ✓	—	High
Wallace Chrysler, Jeep, Dodge, Ram & Wagoneer Dealership In ...	auto	info@wallacecjd.com	—	High
REAL ESTATE/PROPERTY MANAGEMENT Category	hoa	info@business.stuartmartinchamber.org	—	High
Ecosystem Restoration and Management	hoa	info@martin.fl.us	—	High
Commercial Cleaning	cleaning	contact@eastsidechemdry.com ✓	—	High
Treasure Coast Real Estate Investors Association	real_estate	sales@meetup.com ✓	—	High
Treasure Coast Investor	real_estate	info@biggerpockets.com ✓	—	High
Port Saint Lucie Real Estate Investment Club	real_estate	info@freedommentor.com ✓	—	High
INFINITI Stuart: Infiniti Dealership in Stuart, FL	auto_shop	info@infinitistuart.com	—	High
New & Used Cars For Sale | Wallace Auto Group | Stuart & Ft. Pierce	auto	info@wallaceautogroup.com ✓	—	High
Palm Tree Auto Sales: Used Car Dealer in Stuart, Florida	auto	—	(772) 288-2099	High
Wallace Chrysler, Jeep, Dodge, Ram & Wagoneer Dealership In ...	auto	info@wallacecjd.com ✓	—	High
Car Team USA: Used Car Dealer in Stuart, FL	auto	info@carteamusa.com	—	High
Collision Body Shop | Wallace Auto Group In Stuart	auto	info@wallaceautogroup.com ✓	—	High
Kia Collision Body Shop In Stuart, FL - Wallace Kia	auto	info@wallacekiaofstuart.com ✓	—	High
Investment Property for Sale in Port St. Lucie, FL - Mashvisor	real_estate	info@mashvisor.com ✓	—	High
Mobile Car Detailing in Stuart, FL | AIRLITE	detailing	info@airliteautodetailing.com	—	High
Car Detailing in Stuart FL | Mobile Car Detailing - National Detail Pros	detailing	info@nationaldetailpros.com	—	High
Wallace Chevrolet - Chevrolet Dealership In Stuart, FL	auto	info@wallacechevrolet.com	—	High
New & Used Cars For Sale | Wallace Auto Group | Stuart & Ft. Pierce	auto	info@wallaceautogroup.com ✓	—	High
Wallace Chrysler, Jeep, Dodge, Ram & Wagoneer Dealership In ...	auto	info@wallacecjd.com	—	High
Collision Body Shop | Wallace Auto Group In Stuart	auto	info@wallaceautogroup.com ✓	—	High
Kia Collision Body Shop In Stuart, FL - Wallace Kia	auto	info@wallacekiaofstuart.com ✓	—	High
Bathroom Remodeling in Stuart FL - Home & Beyond Services	bathroom	info@homeandbeyondfl.com ✓	—	High
Bathroom Remodeling Contractor | Stuart, FL | Bobby & Brothers ...	bathroom	—	(772) 453-0909	High
Stuart Bathroom Contractors - DreamMaker Bath & Kitchen	bathroom	info@dreammaker-stuart.com	(561) 459-1004	High
Bathroom Remodelers​ Stuart, FL | Adamo Painting	bathroom	davidadamo779@gmail.com	(862) 344-4286	High
New & Used Cars For Sale | Wallace Auto Group | Stuart & Ft. Pierce	auto	info@wallaceautogroup.com ✓	—	High
Wallace Chevrolet - Chevrolet Dealership In Stuart, FL	auto	info@wallacechevrolet.com	—	High
Palm Tree Auto Sales: Used Car Dealer in Stuart, Florida	auto	—	(772) 288-2099	High
Collision Body Shop | Wallace Auto Group In Stuart	auto	info@wallaceautogroup.com ✓	—	High
Kia Collision Body Shop In Stuart, FL - Wallace Kia	auto	info@wallacekiaofstuart.com ✓	—	High
Mobile Car Detailing in Stuart, FL | AIRLITE	detailing	info@airliteautodetailing.com	—	High
NAI Southcoast | Commercial Real Estate Services	property_mgmt	info@naisouthcoast.com ✓	—	High
New & Used Cars For Sale | Wallace Auto Group | Stuart & Ft. Pierce	auto	info@wallaceautogroup.com ✓	—	High
Collision Body Shop | Wallace Auto Group In Stuart	auto	info@wallaceautogroup.com ✓	—	High
Kia Collision Body Shop In Stuart, FL - Wallace Kia	auto	info@wallacekiaofstuart.com ✓	—	High
Mobile Car Detailing in Stuart, FL | AIRLITE	detailing	info@airliteautodetailing.com	—	High
Stuart's Top Car Detailing | Get Your Price Instantly - Panda Hub	detailing	info@pandahub.com ✓	—	High
14 Assisted Living Facilities in Martin County, FL (with Reviews)	apartments	info@seniorhomes.com	—	High
4 Best Assisted Living Communities in Jensen Beach, Florida - Health	apartments	—	3493467007	High
Treasure Coast - 2025 Pricing, Photos, Reviews in Port St. Lucie, FL	apartments	info@assistedlivingcenter.com ✓	—	High
Collision Body Shop | Wallace Auto Group In Stuart	auto	info@wallaceautogroup.com ✓	—	High
Custom Auto Center in Stuart, FL, 34994 | Auto Body Shops	auto	admin@carwise.com ✓	—	High
Mobile Car Detailing in Stuart, FL | AIRLITE	detailing	info@airliteautodetailing.com	—	High
Car Detailing in Stuart FL | Mobile Car Detailing - National Detail Pros	detailing	info@nationaldetailpros.com	—	High
Stuart Industrial Space For Rent | Commercial Leasing | Crexi.com	warehouse	info@crexi.com ✓	—	High
New & Used Cars For Sale | Wallace Auto Group | Stuart & Ft. Pierce	auto	info@wallaceautogroup.com ✓	—	High
Wallace Chevrolet - Chevrolet Dealership In Stuart, FL	auto	info@wallacechevrolet.com ✓	—	High
Collision Body Shop | Wallace Auto Group In Stuart	auto	info@wallaceautogroup.com ✓	—	High
Kia Collision Body Shop In Stuart, FL - Wallace Kia	auto	info@wallacekiaofstuart.com ✓	—	High
Mobile Car Detailing in Stuart, FL | AIRLITE	detailing	info@airliteautodetailing.com	—	High
New & Used Cars For Sale | Wallace Auto Group | Stuart & Ft. Pierce	auto	info@wallaceautogroup.com ✓	—	High
Expert Kitchen Remodeling in Stuart	restaurant	info@stuartkitchenremodeling.com	—	High
Home	restaurant	info@stuartkitchenbathandflooring.com ✓	—	High
Stuart, Florida	restaurant	info@kitchenbathandhomedesign.com ✓	—	High
Kitchen Renovation Company	restaurant	info@islandhomesfl.com ✓	—	High
Transitional Kitchens Gallery	restaurant	—	—	High
Flooring store in Stuart, FL	restaurant	info@aglerinteriors.com ✓	—	High
Kitchen Remodeling in Stuart, FL from Agler Kitchen, Bath & Floors	restaurant	info@aglerinteriors.com ✓	—	High
Stuart Kitchen Contractors	restaurant	—
"""

output_file = '/home/chris/.openclaw/workspace/clean_leads.csv'

# Generic email patterns to exclude
generic_patterns = [
    r'^info@', r'^sales@', r'^admin@', r'^support@', r'^office@', r'^hello@',
    r'^contact@', r'^reception@', r'^users@', r'^events@', r'^booking@',
    r'^reservations@', r'^customerservice@', r'^webmaster@', r'^postmaster@',
    r'^jobs@', r'^careers@', r'^hr@', r'^team@', r'^staff@', r'^email@',
    r'^inquiries@', r'^mail@', r'^media@', r'^press@', r'^marketing@',
    r'^feedback@', r'^help@', r'^billing@', r'^accounting@'
]

cleaned_leads = []
headers = ['Business', 'Category', 'Email', 'Phone', 'Priority']

try:
    lines = raw_data.split('\n')
    print(f'Processing {len(lines)} lines of raw data.')

    for line in lines:
        if not line.strip(): continue
        # Detect header row
        if 'Business' in line and 'Category' in line: continue
        
        parts = line.strip().split('\t')
        
        # Helper to find email - simple logic based on @ symbol
        email = ''
        phone = ''
        business = parts[0] if len(parts) > 0 else ''
        category = parts[1] if len(parts) > 1 else ''
        
        # Try to find email in parts
        for p in parts:
            if '@' in p:
                email = p.replace(' ✓', '').strip()
                break
        
        if not email or email == '—':
            continue 

        is_generic = False
        for pattern in generic_patterns:
            if re.match(pattern, email, re.IGNORECASE):
                is_generic = True
                break
        
        if not is_generic:
            # Construct row
            row = [business, category, email, '', 'High'] 
            # Try to find phone
            for p in parts:
                if re.search(r'\d{3}[-.)]', p) or re.search(r'\d{10}', p):
                    row[3] = p
                    break
            
            cleaned_leads.append(row)

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(cleaned_leads)

    print(f'Successfully saved {len(cleaned_leads)} quality leads to {output_file}')

except Exception as e:
    print(f'Error: {e}')
