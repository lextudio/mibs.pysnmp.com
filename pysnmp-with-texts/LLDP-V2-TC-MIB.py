#
# PySNMP MIB module LLDP-V2-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LLDP-V2-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:17:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Integer32, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Unsigned32, org, ObjectIdentity, Bits, Counter32, ModuleIdentity, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Unsigned32", "org", "ObjectIdentity", "Bits", "Counter32", "ModuleIdentity", "Gauge32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lldpV2TcMIB = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 12))
lldpV2TcMIB.setRevisions(('2009-06-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: lldpV2TcMIB.setRevisionsDescriptions(('Published as part of IEEE Std 802.1AB-2009 revision.',))
if mibBuilder.loadTexts: lldpV2TcMIB.setLastUpdated('200906080000Z')
if mibBuilder.loadTexts: lldpV2TcMIB.setOrganization('IEEE 802.1 Working Group')
if mibBuilder.loadTexts: lldpV2TcMIB.setContactInfo('WG-URL: http://grouper.ieee.org/groups/802/1/index.html WG-EMail: STDS-802-1-L@LISTSERV.IEEE.ORG Contact: Tony Jeffree Postal: 11a Poplar Grove Sale Cheshire M33 3AX UK Tel: +44-161-973-4278 E-mail: tony@jeffree.co.uk')
if mibBuilder.loadTexts: lldpV2TcMIB.setDescription('Textual conventions used throughout the IEEE Std 802.1AB version 2 and later MIB modules. Unless otherwise indicated, the references in this MIB module are to IEEE 802.1AB-2009. The TCs in this MIB are taken from the original LLDP-MIB, LLDP-EXT-DOT1-MIB, and LLDP-EXT-DOT3-MIB published in IEEE Std 802-1D-2005, with the addition of TCs to support the management address table. They have been made available as a separate TC MIB module to facilitate referencing from other MIB modules. Copyright (C) IEEE (2009). This version of this MIB module is published as subclause 11.5.1 of IEEE Std 802.1AB-2009; see the standard itself for full legal notices.')
ieee802dot1mibs = MibIdentifier((1, 3, 111, 2, 802, 1, 1))
class LldpV2ChassisIdSubtype(TextualConvention, Integer32):
    description = "This TC describes the source of a chassis identifier. The enumeration 'chassisComponent(1)' represents a chassis identifier based on the value of entPhysicalAlias object (defined in IETF RFC 4133) for a chassis component (i.e., an entPhysicalClass value of 'chassis(3)'). The enumeration 'interfaceAlias(2)' represents a chassis identifier based on the value of ifAlias object (defined in IETF RFC 2863) for an interface on the containing chassis. The enumeration 'portComponent(3)' represents a chassis identifier based on the value of entPhysicalAlias object (defined in IETF RFC 4133) for a port or backplane component (i.e., entPhysicalClass value of 'port(10)' or 'backplane(4)'), within the containing chassis. The enumeration 'macAddress(4)' represents a chassis identifier based on the value of a unicast source address (encoded in network byte order and IEEE 802.3 canonical bit order), of a port on the containing chassis as defined in IEEE Std 802. The enumeration 'networkAddress(5)' represents a chassis identifier based on a network address, associated with a particular chassis. The encoded address is actually composed of two fields. The first field is a single octet, representing the IANA AddressFamilyNumbers value for the specific address type, and the second field is the network address value. The enumeration 'interfaceName(6)' represents a chassis identifier based on the value of ifName object (defined in IETF RFC 2863) for an interface on the containing chassis. The enumeration 'local(7)' represents a chassis identifier based on a locally defined value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("chassisComponent", 1), ("interfaceAlias", 2), ("portComponent", 3), ("macAddress", 4), ("networkAddress", 5), ("interfaceName", 6), ("local", 7))

class LldpV2ChassisId(TextualConvention, OctetString):
    description = "This TC describes the format of a chassis identifier string. Objects of this type are always used with an associated LldpChassisIdSubtype object, which identifies the format of the particular LldpChassisId object instance. If the associated LldpChassisIdSubtype object has a value of 'chassisComponent(1)', then the octet string identifies a particular instance of the entPhysicalAlias object (defined in IETF RFC 4133) for a chassis component (i.e., an entPhysicalClass value of 'chassis(3)'). If the associated LldpChassisIdSubtype object has a value of 'interfaceAlias(2)', then the octet string identifies a particular instance of the ifAlias object (defined in IETF RFC 2863) for an interface on the containing chassis. If the particular ifAlias object does not contain any values, another chassis identifier type should be used. If the associated LldpChassisIdSubtype object has a value of 'portComponent(3)', then the octet string identifies a particular instance of the entPhysicalAlias object (defined in IETF RFC 4133) for a port or backplane component within the containing chassis. If the associated LldpChassisIdSubtype object has a value of 'macAddress(4)', then this string identifies a particular unicast source address (encoded in network byte order and IEEE 802.3 canonical bit order), of a port on the containing chassis as defined in IEEE Std 802. If the associated LldpChassisIdSubtype object has a value of 'networkAddress(5)', then this string identifies a particular network address, encoded in network byte order, associated with one or more ports on the containing chassis. The first octet contains the IANA Address Family Numbers enumeration value for the specific address type, and octets 2 through N contain the network address value in network byte order. If the associated LldpChassisIdSubtype object has a value of 'interfaceName(6)', then the octet string identifies a particular instance of the ifName object (defined in IETF RFC 2863) for an interface on the containing chassis. If the particular ifName object does not contain any values, another chassis identifier type should be used. If the associated LldpChassisIdSubtype object has a value of 'local(7)', then this string identifies a locally assigned Chassis ID."
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class LldpV2PortIdSubtype(TextualConvention, Integer32):
    description = "This TC describes the source of a particular type of port identifier used in the LLDP MIB. The enumeration 'interfaceAlias(1)' represents a port identifier based on the ifAlias MIB object, defined in IETF RFC 2863. The enumeration 'portComponent(2)' represents a port identifier based on the value of entPhysicalAlias (defined in IETF RFC 4133) for a port component (i.e., entPhysicalClass value of 'port(10)'), within the containing chassis. The enumeration 'macAddress(3)' represents a port identifier based on a unicast source address (encoded in network byte order and IEEE 802.3 canonical bit order), which has been detected by the agent and associated with a particular port (IEEE Std 802). The enumeration 'networkAddress(4)' represents a port identifier based on a network address, detected by the agent and associated with a particular port. The enumeration 'interfaceName(5)' represents a port identifier based on the ifName MIB object, defined in IETF RFC 2863. The enumeration 'agentCircuitId(6)' represents a port identifier based on the agent-local identifier of the circuit (defined in RFC 3046), detected by the agent and associated with a particular port. The enumeration 'local(7)' represents a port identifier based on a value locally assigned."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("interfaceAlias", 1), ("portComponent", 2), ("macAddress", 3), ("networkAddress", 4), ("interfaceName", 5), ("agentCircuitId", 6), ("local", 7))

class LldpV2PortId(TextualConvention, OctetString):
    description = "This TC describes the format of a port identifier string. Objects of this type are always used with an associated LldpPortIdSubtype object, which identifies the format of the particular LldpPortId object instance. If the associated LldpPortIdSubtype object has a value of 'interfaceAlias(1)', then the octet string identifies a particular instance of the ifAlias object (defined in IETF RFC 2863). If the particular ifAlias object does not contain any values, another port identifier type should be used. If the associated LldpPortIdSubtype object has a value of 'portComponent(2)', then the octet string identifies a particular instance of the entPhysicalAlias object (defined in IETF RFC 4133) for a port or backplane component. If the associated LldpPortIdSubtype object has a value of 'macAddress(3)', then this string identifies a particular unicast source address (encoded in network byte order and IEEE 802.3 canonical bit order) associated with the port (IEEE Std 802). If the associated LldpPortIdSubtype object has a value of 'networkAddress(4)', then this string identifies a network address associated with the port. The first octet contains the IANA AddressFamilyNumbers enumeration value for the specific address type, and octets 2 through N contain the networkAddress address value in network byte order. If the associated LldpPortIdSubtype object has a value of 'interfaceName(5)', then the octet string identifies a particular instance of the ifName object (defined in IETF RFC 2863). If the particular ifName object does not contain any values, another port identifier type should be used. If the associated LldpPortIdSubtype object has a value of 'agentCircuitId(6)', then this string identifies a agent-local identifier of the circuit (defined in RFC 3046). If the associated LldpPortIdSubtype object has a value of 'local(7)', then this string identifies a locally assigned port ID."
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class LldpV2ManAddrIfSubtype(TextualConvention, Integer32):
    reference = '8.5.9.5'
    description = "This TC defines an enumeration value that identifies the interface numbering method used for defining the interface number associated with a management address. An object with this syntax defines the format of an interface number object. The enumeration 'unknown(1)' represents the case where the interface is not known. In this case, the corresponding interface number is of zero length. The enumeration 'ifIndex(2)' represents interface identifier based on the ifIndex MIB object. The enumeration 'systemPortNumber(3)' represents interface identifier based on the system port numbering convention."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("ifIndex", 2), ("systemPortNumber", 3))

class LldpV2ManAddress(TextualConvention, OctetString):
    description = 'The value of a management address associated with the LLDP agent that may be used to reach higher layer entities to assist discovery by network management. It should be noted that appropriate security credentials, such as SNMP engineId, may be required to access the LLDP agent using a management address. These necessary credentials should be known by the network management and the objects associated with the credentials are not included in the LLDP agent.'
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 31)

class LldpV2SystemCapabilitiesMap(TextualConvention, Bits):
    description = "This TC describes the system capabilities. The bit 'other(0)' indicates that the system has capabilities other than those listed below. The bit 'repeater(1)' indicates that the system has repeater capability. The bit 'bridge(2)' indicates that the system has bridge capability. The bit 'wlanAccessPoint(3)' indicates that the system has WLAN access point capability. The bit 'router(4)' indicates that the system has router capability. The bit 'telephone(5)' indicates that the system has telephone capability. The bit 'docsisCableDevice(6)' indicates that the system has DOCSIS Cable Device capability (IETF RFC 4639 & 2670). The bit 'stationOnly(7)' indicates that the system has only station capability and nothing else. The bit 'cVLANComponent(8)' indicates that the system has C-VLAN component functionality. The bit 'sVLANComponent(8)' indicates that the system has S-VLAN component functionality. The bit 'twoPortMACRelay(10)' indicates that the system has Two-port MAC Relay (TPMR) functionality."
    status = 'current'
    namedValues = NamedValues(("other", 0), ("repeater", 1), ("bridge", 2), ("wlanAccessPoint", 3), ("router", 4), ("telephone", 5), ("docsisCableDevice", 6), ("stationOnly", 7), ("cVLANComponent", 8), ("sVLANComponent", 9), ("twoPortMACRelay", 10))

class LldpV2DestAddressTableIndex(TextualConvention, Unsigned32):
    description = 'An index value, used as the index to the table of destination MAC addresses used both as the destination addresses on transmitted LLDPDUs and on received LLDPDUs. This index value is also used as a secondary index value in tables indexed by fields of type ifIndex, in order to associate a destination address with each row of the table.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4096)

class LldpV2LinkAggStatusMap(TextualConvention, Bits):
    description = "This TC describes the link aggregation status. The bit 'aggCapable(0)' indicates the link is capable of being aggregated. The bit 'aggEnabled(1)' indicates the link is currently in aggregation."
    status = 'current'
    namedValues = NamedValues(("aggCapable", 0), ("aggEnabled", 1))

class LldpV2PowerPortClass(TextualConvention, Integer32):
    description = 'This TC describes the Power over Ethernet (PoE) port class.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("pClassPSE", 1), ("pClassPD", 2))

mibBuilder.exportSymbols("LLDP-V2-TC-MIB", LldpV2ManAddress=LldpV2ManAddress, LldpV2DestAddressTableIndex=LldpV2DestAddressTableIndex, PYSNMP_MODULE_ID=lldpV2TcMIB, lldpV2TcMIB=lldpV2TcMIB, LldpV2ChassisId=LldpV2ChassisId, LldpV2SystemCapabilitiesMap=LldpV2SystemCapabilitiesMap, LldpV2PortIdSubtype=LldpV2PortIdSubtype, LldpV2ManAddrIfSubtype=LldpV2ManAddrIfSubtype, LldpV2ChassisIdSubtype=LldpV2ChassisIdSubtype, LldpV2PortId=LldpV2PortId, LldpV2PowerPortClass=LldpV2PowerPortClass, ieee802dot1mibs=ieee802dot1mibs, LldpV2LinkAggStatusMap=LldpV2LinkAggStatusMap)
