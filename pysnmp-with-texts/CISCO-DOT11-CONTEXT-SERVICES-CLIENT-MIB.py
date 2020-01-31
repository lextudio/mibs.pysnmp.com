#
# PySNMP MIB module CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:55:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, Bits, ObjectIdentity, NotificationType, Unsigned32, IpAddress, Counter32, TimeTicks, iso, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "ObjectIdentity", "NotificationType", "Unsigned32", "IpAddress", "Counter32", "TimeTicks", "iso", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32")
TextualConvention, DisplayString, TimeInterval = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TimeInterval")
ciscoDot11CscMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 109))
ciscoDot11CscMIB.setRevisions(('2004-06-02 00:00', '2003-05-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDot11CscMIB.setRevisionsDescriptions(('The definition of the object cDot11CscParentWdsAddress has been modified to return a specific error value on certain conditions. ', 'Initial version of this MIB module. ',))
if mibBuilder.loadTexts: ciscoDot11CscMIB.setLastUpdated('200406020000Z')
if mibBuilder.loadTexts: ciscoDot11CscMIB.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoDot11CscMIB.setContactInfo(' Cisco Systems, Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-dot11@cisco.com')
if mibBuilder.loadTexts: ciscoDot11CscMIB.setDescription("This MIB is intended to be implemented on all 802.11 Access Points and Wireless Bridges that need to participate in the context management process and make use of the services provided by the entities offering WDS and WNS. The term '802.11 station' refers to one of the Access Point / Wireless Bridge throughout the MIB unless stated otherwise. The hierarchy of the devices offering the wireless domain and network services looks like the following. += = = = + | | | WNS | (Campus level) | | += = = = + / \\ / \\ / \\ / \\ \\/ \\/ += = =+ += = =+ | | | | | WNS | | WNS | | | | | += = =+ += = =+ / \\ \\ / \\ \\ / \\ \\ / \\ \\ \\/ \\/ \\/ +=====+ +=====+ +=====+ | | | | | | | WDS | | WDS | | WDS | ( Subnet | | | | | | level- +=====+ +=====+ +=====+ Single / \\ \\ \\ broadcast / \\ \\ \\ domain ) / \\ \\ \\ / \\ \\ \\ / \\ \\ \\ \\/ \\/ \\/ \\/ +~-~-~+ +~-~-~+ +~-~-~+ +~-~-~+ + + + + + + + + + AP + + AP + + AP + + AP + + + + + + + + + +~-~-~+ +~-~-~+ +~-~-~+ +~-~-~+ .. . . . . . . . . . . . . . . . . . . . . . . . \\/ \\/ \\/ \\/ \\/ +.....+ +.....+ +-.-.-.+ +~-~-~+ +......+ + + + + + + + + + + + MN + + MN + + WGB + + AP + + MN + + + + + + + + + + + +.....+ +.....+ +-.-.-.+ +~-~-~+ +......+ . . . . . . . . . . . . \\/ \\/ \\/ ++++++++ +......+ +......+ + + + + + + + EN + + MN + + MN + + + + + + + ++++++++ +......+ +......+ The diagram above depicts the overall campus network hierarchy and the services being offered at various levels in the hierarchy. Here, authentication services for infrastructure nodes are offered by the root node, the node providing WNS at the topmost (Campus) level. This node spans an enterprise campus that resides in a geographic location. In this case, an 802.11 station performs initial authentication with the topmost WNS entity. It also gets the keys needed for secure context transfer by communication with that entity. WNS are offered at various levels as shown in the hierarchy to achieve scalability. WNS at the subsequent levels other than the root level include authentication services for MNs and are typically confined to a single building. At the broadcast domain level, the WDS includes authentication and registration services for the APs. An AP provides proxy authentication and registration services for the MNs. The APs that connect to parent APs through the wireless interface ( as shown by the dotted lines ) are Repeater-APs. The WGBs are managed in the same manner as the MNs. However, the Ethernet Nodes ( EN ) that are connected to the WGB won't be served as part of the WDS. GLOSSARY Access Point ( AP ) Any entity that contains an 802.11 medium access control ( MAC ) and physical layer ( PHY ) interface and provides access to the distribution services via the wireless medium for associated clients. Wireless Bridge An 802.11 entity that provides wireless connectivity between two wired LAN segments and is used in point- to-point or point-to-multipoint configurations. Mobile Node ( MN ) A roaming 802.11 wireless device in a wireless network associated with an access point. WorkGroup Bridge ( WGB ) A work-group bridge is a non-STP AP with an 802.11 primary port and a secondary Ethernet port that provides access to a non-STP secondary Ethernet LAN segment. STP refers to the IEEE 802.1D Spanning Tree Protocol. An 'STP AP' executes the 802.1D STP and the 802.1D STP is operated on an 'STP link'. A 'non-STP AP' does not execute the 802.1D STP. Repeater-AP A repeater is a 'wireless AP' that is attached to a parent AP on an 802.11 primary port. The Ethernet port is disabled in a Repeater-AP. Infrastructure Node ( IN ) This term refers to Access Points, Wireless Bridges and those devices that implement and offer WNS and WDS as shown in the network hierarchy. Ethernet Node ( EN ) The node that gets the uplink to the Wireless AP via the WGB. This node connects to the WGB through its primary Ethernet port. Context The mobility context for an MN includes its current mobility bindings with the APs, IP/802 address bindings, cached configuration parameters, QoS state, IP group membership, authentication state, accounting statistics, and other dynamically derived protocol state information. Wireless Domain Services The set of services being offered at a particular broadcast domain that may be an IP subnet or a particular VLAN. The services include the following. 1. MN security credential caching to provide seamless, secure intra-subnet roaming. 2. Authenticated context transfer for roaming client within the subnet. Since, by definition, the WDS are bound to one subnet ( broadcast domain ), if implemented in a device spanning multiple subnets, the implementation should take care to provide separate set of services for each of the subnets. Wireless Network Services The set of services that can be visualized as being offered at various levels other than the lowest (subnet) level of a hierarchical campus network. At the topmost level, infrastructure authentication services for all the devices in the network that provide WNS and WDS are offered. In case if WNS are not distributed at several levels as shown in the hierarchy above and is confined to be offered only at a single topmost level, the services offered also include authentication services for the MNs. WNS Entity The logical entity that resides in an infrastructure node and offers WNS to the descendants of that infrastructure node in the wireless services hierarchy. WDS Entity The logical entity that resides in an infrastructure node and offers WDS to the descendants of that infrastructure node in the wireless services hierarchy. WS Entity Refers to one of WNS / WDS Entities. Parent Node The entity that immediately precedes an infrastructure node in the hierarchy. For mobile nodes, the parent APs provide proxy wireless services by talking to their immediate parent entities providing WDS. Root Node The entity that is at the highest level in the network hierarchy. The root node acts as the IN Authenticator for the infrastructure nodes. In case if WNS are not distributed, the root node also acts as the Mobile Node Authenticator ( See description below ). Descendant A node that is in the sub-tree of the campus hierarchy tree rooted at the node providing WNS at the campus level. Infrastructure Node ( IN ) Authenticator The logical entity that communicates with the AAA server and provides authentication services for the infrastructure nodes. Details of the IN Authenticator has to be configured in the device providing WDS manually. The AP learns about the IN Authenticator automatically upon registering with its immediate parent. The WDS also includes MN authentication services if the entity providing WDS is at the topmost level in the hierarchy. Mobile Node ( MN ) Authenticator The logical entity that communicates with the AAA server and provides authentication services for mobile nodes. An infrastructure node learns the whereabouts of the MN Authenticator from the root node. Wireless Network Manager ( WNM ) The network management system that manages the entire hierarchy of devices providing WNS and WDS. Advertisement The process by which the Access Points identify their parent entities providing WDS. APs listen to the advertisements of the WDS entities and gets registered with one of those entities to facilitate secured context transfer. WLCCP Wireless LAN Context Control Protocol. Used to establish and manage the network topology and securely manage the 'operational context' for mobile stations in a campus network. AAA Authentication, Authorization, Accounting The method by which users are authenticated, authorized and tracked to gain access and move about inside a network. A node will request network access through an appropriate protocol to an authentication server that provides protocols and services for providing authentication, authorization and session accounting. Service Set Identifier ( SSID ) 802.11 Service Set Identifier. An SSID identifies a set of mobile nodes grouped into a logical 'service set' and the APs that provide access for the service set. Wireless services at subnet level ================================= +========+ | | | WDS | ( Subnet level - Broadcast | | domain ) +========+ / \\ / \\ / \\ / \\ / \\ \\/ \\/ +~-~-~+ +~-~-~+ + + + + + AP + + AP + + + + + +~-~-~+ +~-~-~+ . . . . . . . . . . . . . . . . . . \\/ \\/ \\/ +......+ +-.-.-.+ +~-~-~-+ + + + + + + + MN + + WGB + + AP + + + + + + + +......+ +-.-.-.+ +~-~-~-+ The above diagram depicts how wireless services are being offered in a network rooted at the device implementing WDS. In such a network, the WDS entity provides authentication services to both the infrastructure and mobile nodes. An 802.11 station in this hierarchy mentioned above performs the following. 1) Provides proxy authentication and registration services to the MNs, WGBs and repeater-APs. The station forwards all the authentication and registration requests of its clients to its parent node offering WDS and acting as the IN Authenticator to enable the authentication and registration of its clients. 2) Participates in the election process to elect the node that will provide WDS for a particular broadcast domain. ")
ciscoDot11CscMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 109, 1))
ciscoDot11CscMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 109, 2))
ciscoDot11CscConfigGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1))
cDot11CscAddressType = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CscAddressType.setStatus('current')
if mibBuilder.loadTexts: cDot11CscAddressType.setDescription('Represents the type of addresses stored in the objects cDot11CscParentWdsAddress, cDot11CscRootNodeAddress and cDot11CscMnAuthenticatorAddress. ')
cDot11CscParentWdsAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CscParentWdsAddress.setStatus('current')
if mibBuilder.loadTexts: cDot11CscParentWdsAddress.setDescription("The address of the parent WDS entity this 802.11 station is currently registered with. The type of InetAddress supported by this object is determined by the cDot11CscAddressType object. If cDot11CscOperMode equals 'distributed' and the user credentials are not configured in this 802.11 station, a noSuchInstance error is returned. On all other occasions, when cDot11CscOperMode equals 'distributed', the value returned is 0.0.0.0 to indicate that either this node is not registered with a WDS entity or that no parent WDS entity existed when the query was made. ")
cDot11CscRootNodeAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CscRootNodeAddress.setStatus('current')
if mibBuilder.loadTexts: cDot11CscRootNodeAddress.setDescription('The address of the root node this 802.11 station gets authenticated with. The type of InetAddress supported by this object is determined by the cDot11CscAddressType object. If the parent WDS entity acts as the root node, this object returns the address of the parent WDS entity. If the hierarchy contains a campus level WNS entity, this object returns the address of that WNS entity. ')
cDot11CscMnAuthenticatorAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CscMnAuthenticatorAddress.setStatus('current')
if mibBuilder.loadTexts: cDot11CscMnAuthenticatorAddress.setDescription('The address of the Mobile Node Authenticator to which this 802.11 station forwards authentication requests of the mobile nodes attempting to associate with this station. The type of InetAddress supported by this object is determined by the cDot11CscAddressType object. If the parent WDS entity acts as the root node, so that no WNS entity is present in the network hierarchy, this object returns the address of the parent WDS entity. If the parent WDS entity has the root WNS entity as its immediate parent, this object returns the address of the root WNS entity. If the WDS entity has a WNS entity, that is not the root node, as its immediate parent, this object returns the address of that WNS entity. ')
cDot11CscOperMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("infrastructure", 1), ("distributed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CscOperMode.setStatus('current')
if mibBuilder.loadTexts: cDot11CscOperMode.setDescription("The current mode of operation of this 802.11 station. The semantics for this object are as follows. infrastructure - An 802.11 station operates in the 'infrastructure' mode if it discovers a WDS entity through advertisement messages and registers with it. distributed - If the 802.11 station couldn't discover a WDS entity or has lost contact with the its parent WDS entity, then the station operates in the 'distributed' mode. However, the station listens for the advertisement messages from the WDS entity in the background to get back to the 'infrastructure' mode. ")
cDot11CscMnInactivityTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 6), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CscMnInactivityTime.setStatus('current')
if mibBuilder.loadTexts: cDot11CscMnInactivityTime.setDescription('The maximum time a mobile node can remain associated with this 802.11 station without sending a frame. ')
cDot11CscRegistrationLifeTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 7), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CscRegistrationLifeTime.setStatus('current')
if mibBuilder.loadTexts: cDot11CscRegistrationLifeTime.setDescription('The maximum time after which the registration of this 802.11 station with its parent WDS entity expires. ')
cDot11CscStateTransitions = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CscStateTransitions.setStatus('current')
if mibBuilder.loadTexts: cDot11CscStateTransitions.setDescription('This object counts the number of times this 802.11 station has transitioned between the infrastructure and distributed modes since the last reboot. ')
ciscoDot11CscMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 109, 2, 1))
ciscoDot11CscMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 109, 2, 2))
ciscoDot11CscMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 109, 2, 1, 1)).setObjects(("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "ciscoDot11CscConfigGlobalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CscMIBCompliance = ciscoDot11CscMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoDot11CscMIBCompliance.setDescription('The compliance statement for the SNMP entities that implement the ciscoDot11CscMIB module. ')
ciscoDot11CscConfigGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 109, 2, 2, 1)).setObjects(("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscAddressType"), ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscParentWdsAddress"), ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscRootNodeAddress"), ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscMnAuthenticatorAddress"), ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscOperMode"), ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscMnInactivityTime"), ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscRegistrationLifeTime"), ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscStateTransitions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CscConfigGlobalGroup = ciscoDot11CscConfigGlobalGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoDot11CscConfigGlobalGroup.setDescription("This collection of objects provide information about this 802.11 station's parent WDS, its mode of operation, the address of the IN/MN authenticators, its registration life time and the number of times the station has switched between the two modes. ")
mibBuilder.exportSymbols("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", cDot11CscMnInactivityTime=cDot11CscMnInactivityTime, ciscoDot11CscMIBGroups=ciscoDot11CscMIBGroups, cDot11CscMnAuthenticatorAddress=cDot11CscMnAuthenticatorAddress, ciscoDot11CscMIBObjects=ciscoDot11CscMIBObjects, ciscoDot11CscMIBConformance=ciscoDot11CscMIBConformance, cDot11CscOperMode=cDot11CscOperMode, cDot11CscStateTransitions=cDot11CscStateTransitions, PYSNMP_MODULE_ID=ciscoDot11CscMIB, ciscoDot11CscMIB=ciscoDot11CscMIB, cDot11CscRootNodeAddress=cDot11CscRootNodeAddress, ciscoDot11CscMIBCompliance=ciscoDot11CscMIBCompliance, cDot11CscRegistrationLifeTime=cDot11CscRegistrationLifeTime, ciscoDot11CscConfigGlobalGroup=ciscoDot11CscConfigGlobalGroup, ciscoDot11CscMIBCompliances=ciscoDot11CscMIBCompliances, ciscoDot11CscConfigGlobal=ciscoDot11CscConfigGlobal, cDot11CscParentWdsAddress=cDot11CscParentWdsAddress, cDot11CscAddressType=cDot11CscAddressType)