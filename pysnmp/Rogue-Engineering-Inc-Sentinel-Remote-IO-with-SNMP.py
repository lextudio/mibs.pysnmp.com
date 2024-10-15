# SNMP MIB module (Rogue-Engineering-Inc-Sentinel-Remote-IO-with-SNMP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Rogue-Engineering-Inc-Sentinel-Remote-IO-with-SNMP
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:58 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

rogueSentinelv2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2)
)
rogueSentinelv2.setRevisions(
        ("2008-06-04 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RogueEngr_ObjectIdentity = ObjectIdentity
rogueEngr = _RogueEngr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28459)
)
_RogueRIOS_ObjectIdentity = ObjectIdentity
rogueRIOS = _RogueRIOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28459, 228)
)
_RegMap_ObjectIdentity = ObjectIdentity
regMap = _RegMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1)
)
_RegFirmwareVersion_Type = Integer32
_RegFirmwareVersion_Object = MibScalar
regFirmwareVersion = _RegFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 3),
    _RegFirmwareVersion_Type()
)
regFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regFirmwareVersion.setStatus("current")
_RegFirmwareRevision_Type = Integer32
_RegFirmwareRevision_Object = MibScalar
regFirmwareRevision = _RegFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 4),
    _RegFirmwareRevision_Type()
)
regFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regFirmwareRevision.setStatus("current")
_RegSerialBaud_Type = Integer32
_RegSerialBaud_Object = MibScalar
regSerialBaud = _RegSerialBaud_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 99),
    _RegSerialBaud_Type()
)
regSerialBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regSerialBaud.setStatus("current")
_RegSNMPManagerIP1_Type = Integer32
_RegSNMPManagerIP1_Object = MibScalar
regSNMPManagerIP1 = _RegSNMPManagerIP1_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 100),
    _RegSNMPManagerIP1_Type()
)
regSNMPManagerIP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regSNMPManagerIP1.setStatus("current")
_RegSNMPManagerIP2_Type = Integer32
_RegSNMPManagerIP2_Object = MibScalar
regSNMPManagerIP2 = _RegSNMPManagerIP2_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 101),
    _RegSNMPManagerIP2_Type()
)
regSNMPManagerIP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regSNMPManagerIP2.setStatus("current")
_RegSNMPManagerIP3_Type = Integer32
_RegSNMPManagerIP3_Object = MibScalar
regSNMPManagerIP3 = _RegSNMPManagerIP3_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 102),
    _RegSNMPManagerIP3_Type()
)
regSNMPManagerIP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regSNMPManagerIP3.setStatus("current")
_RegSNMPManagerIP4_Type = Integer32
_RegSNMPManagerIP4_Object = MibScalar
regSNMPManagerIP4 = _RegSNMPManagerIP4_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 103),
    _RegSNMPManagerIP4_Type()
)
regSNMPManagerIP4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regSNMPManagerIP4.setStatus("current")
_RegMODBUSAddress_Type = Integer32
_RegMODBUSAddress_Object = MibScalar
regMODBUSAddress = _RegMODBUSAddress_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 104),
    _RegMODBUSAddress_Type()
)
regMODBUSAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regMODBUSAddress.setStatus("current")
_RegMACAddress1_Type = Integer32
_RegMACAddress1_Object = MibScalar
regMACAddress1 = _RegMACAddress1_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 105),
    _RegMACAddress1_Type()
)
regMACAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regMACAddress1.setStatus("current")
_RegMACAddress2_Type = Integer32
_RegMACAddress2_Object = MibScalar
regMACAddress2 = _RegMACAddress2_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 106),
    _RegMACAddress2_Type()
)
regMACAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regMACAddress2.setStatus("current")
_RegMACAddress3_Type = Integer32
_RegMACAddress3_Object = MibScalar
regMACAddress3 = _RegMACAddress3_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 107),
    _RegMACAddress3_Type()
)
regMACAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regMACAddress3.setStatus("current")
_RegMACAddress4_Type = Integer32
_RegMACAddress4_Object = MibScalar
regMACAddress4 = _RegMACAddress4_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 108),
    _RegMACAddress4_Type()
)
regMACAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regMACAddress4.setStatus("current")
_RegMACAddress5_Type = Integer32
_RegMACAddress5_Object = MibScalar
regMACAddress5 = _RegMACAddress5_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 109),
    _RegMACAddress5_Type()
)
regMACAddress5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regMACAddress5.setStatus("current")
_RegMACAddress6_Type = Integer32
_RegMACAddress6_Object = MibScalar
regMACAddress6 = _RegMACAddress6_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 110),
    _RegMACAddress6_Type()
)
regMACAddress6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regMACAddress6.setStatus("current")
_RegIPAddress1_Type = Integer32
_RegIPAddress1_Object = MibScalar
regIPAddress1 = _RegIPAddress1_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 111),
    _RegIPAddress1_Type()
)
regIPAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regIPAddress1.setStatus("current")
_RegIPAddress2_Type = Integer32
_RegIPAddress2_Object = MibScalar
regIPAddress2 = _RegIPAddress2_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 112),
    _RegIPAddress2_Type()
)
regIPAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regIPAddress2.setStatus("current")
_RegIPAddress3_Type = Integer32
_RegIPAddress3_Object = MibScalar
regIPAddress3 = _RegIPAddress3_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 113),
    _RegIPAddress3_Type()
)
regIPAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regIPAddress3.setStatus("current")
_RegIPAddress4_Type = Integer32
_RegIPAddress4_Object = MibScalar
regIPAddress4 = _RegIPAddress4_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 114),
    _RegIPAddress4_Type()
)
regIPAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regIPAddress4.setStatus("current")
_RegGatewayIPAddress1_Type = Integer32
_RegGatewayIPAddress1_Object = MibScalar
regGatewayIPAddress1 = _RegGatewayIPAddress1_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 115),
    _RegGatewayIPAddress1_Type()
)
regGatewayIPAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regGatewayIPAddress1.setStatus("current")
_RegGatewayIPAddress2_Type = Integer32
_RegGatewayIPAddress2_Object = MibScalar
regGatewayIPAddress2 = _RegGatewayIPAddress2_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 116),
    _RegGatewayIPAddress2_Type()
)
regGatewayIPAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regGatewayIPAddress2.setStatus("current")
_RegGatewayIPAddress3_Type = Integer32
_RegGatewayIPAddress3_Object = MibScalar
regGatewayIPAddress3 = _RegGatewayIPAddress3_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 117),
    _RegGatewayIPAddress3_Type()
)
regGatewayIPAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regGatewayIPAddress3.setStatus("current")
_RegGatewayIPAddress4_Type = Integer32
_RegGatewayIPAddress4_Object = MibScalar
regGatewayIPAddress4 = _RegGatewayIPAddress4_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 118),
    _RegGatewayIPAddress4_Type()
)
regGatewayIPAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regGatewayIPAddress4.setStatus("current")
_RegSubnetMask1_Type = Integer32
_RegSubnetMask1_Object = MibScalar
regSubnetMask1 = _RegSubnetMask1_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 119),
    _RegSubnetMask1_Type()
)
regSubnetMask1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regSubnetMask1.setStatus("current")
_RegSubnetMask2_Type = Integer32
_RegSubnetMask2_Object = MibScalar
regSubnetMask2 = _RegSubnetMask2_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 120),
    _RegSubnetMask2_Type()
)
regSubnetMask2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regSubnetMask2.setStatus("current")
_RegSubnetMask3_Type = Integer32
_RegSubnetMask3_Object = MibScalar
regSubnetMask3 = _RegSubnetMask3_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 121),
    _RegSubnetMask3_Type()
)
regSubnetMask3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regSubnetMask3.setStatus("current")
_RegSubnetMask4_Type = Integer32
_RegSubnetMask4_Object = MibScalar
regSubnetMask4 = _RegSubnetMask4_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 122),
    _RegSubnetMask4_Type()
)
regSubnetMask4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regSubnetMask4.setStatus("current")
_RegControllerName1_Type = Integer32
_RegControllerName1_Object = MibScalar
regControllerName1 = _RegControllerName1_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 208),
    _RegControllerName1_Type()
)
regControllerName1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName1.setStatus("current")
_RegControllerName2_Type = Integer32
_RegControllerName2_Object = MibScalar
regControllerName2 = _RegControllerName2_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 209),
    _RegControllerName2_Type()
)
regControllerName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName2.setStatus("current")
_RegControllerName3_Type = Integer32
_RegControllerName3_Object = MibScalar
regControllerName3 = _RegControllerName3_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 210),
    _RegControllerName3_Type()
)
regControllerName3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName3.setStatus("current")
_RegControllerName4_Type = Integer32
_RegControllerName4_Object = MibScalar
regControllerName4 = _RegControllerName4_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 211),
    _RegControllerName4_Type()
)
regControllerName4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName4.setStatus("current")
_RegControllerName5_Type = Integer32
_RegControllerName5_Object = MibScalar
regControllerName5 = _RegControllerName5_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 212),
    _RegControllerName5_Type()
)
regControllerName5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName5.setStatus("current")
_RegControllerName6_Type = Integer32
_RegControllerName6_Object = MibScalar
regControllerName6 = _RegControllerName6_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 213),
    _RegControllerName6_Type()
)
regControllerName6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName6.setStatus("current")
_RegControllerName7_Type = Integer32
_RegControllerName7_Object = MibScalar
regControllerName7 = _RegControllerName7_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 214),
    _RegControllerName7_Type()
)
regControllerName7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName7.setStatus("current")
_RegControllerName8_Type = Integer32
_RegControllerName8_Object = MibScalar
regControllerName8 = _RegControllerName8_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 215),
    _RegControllerName8_Type()
)
regControllerName8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName8.setStatus("current")
_RegControllerName9_Type = Integer32
_RegControllerName9_Object = MibScalar
regControllerName9 = _RegControllerName9_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 216),
    _RegControllerName9_Type()
)
regControllerName9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName9.setStatus("current")
_RegControllerName10_Type = Integer32
_RegControllerName10_Object = MibScalar
regControllerName10 = _RegControllerName10_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 217),
    _RegControllerName10_Type()
)
regControllerName10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName10.setStatus("current")
_RegControllerName11_Type = Integer32
_RegControllerName11_Object = MibScalar
regControllerName11 = _RegControllerName11_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 218),
    _RegControllerName11_Type()
)
regControllerName11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName11.setStatus("current")
_RegControllerName12_Type = Integer32
_RegControllerName12_Object = MibScalar
regControllerName12 = _RegControllerName12_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 219),
    _RegControllerName12_Type()
)
regControllerName12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName12.setStatus("current")
_RegControllerName13_Type = Integer32
_RegControllerName13_Object = MibScalar
regControllerName13 = _RegControllerName13_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 220),
    _RegControllerName13_Type()
)
regControllerName13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName13.setStatus("current")
_RegControllerName14_Type = Integer32
_RegControllerName14_Object = MibScalar
regControllerName14 = _RegControllerName14_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 221),
    _RegControllerName14_Type()
)
regControllerName14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName14.setStatus("current")
_RegControllerName15_Type = Integer32
_RegControllerName15_Object = MibScalar
regControllerName15 = _RegControllerName15_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 222),
    _RegControllerName15_Type()
)
regControllerName15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName15.setStatus("current")
_RegControllerName16_Type = Integer32
_RegControllerName16_Object = MibScalar
regControllerName16 = _RegControllerName16_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 223),
    _RegControllerName16_Type()
)
regControllerName16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName16.setStatus("current")
_RegControllerName17_Type = Integer32
_RegControllerName17_Object = MibScalar
regControllerName17 = _RegControllerName17_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 224),
    _RegControllerName17_Type()
)
regControllerName17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName17.setStatus("current")
_RegControllerName18_Type = Integer32
_RegControllerName18_Object = MibScalar
regControllerName18 = _RegControllerName18_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 225),
    _RegControllerName18_Type()
)
regControllerName18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName18.setStatus("current")
_RegControllerName19_Type = Integer32
_RegControllerName19_Object = MibScalar
regControllerName19 = _RegControllerName19_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 226),
    _RegControllerName19_Type()
)
regControllerName19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName19.setStatus("current")
_RegControllerName20_Type = Integer32
_RegControllerName20_Object = MibScalar
regControllerName20 = _RegControllerName20_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 227),
    _RegControllerName20_Type()
)
regControllerName20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName20.setStatus("current")
_RegControllerName21_Type = Integer32
_RegControllerName21_Object = MibScalar
regControllerName21 = _RegControllerName21_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 228),
    _RegControllerName21_Type()
)
regControllerName21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName21.setStatus("current")
_RegControllerName22_Type = Integer32
_RegControllerName22_Object = MibScalar
regControllerName22 = _RegControllerName22_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 229),
    _RegControllerName22_Type()
)
regControllerName22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName22.setStatus("current")
_RegControllerName23_Type = Integer32
_RegControllerName23_Object = MibScalar
regControllerName23 = _RegControllerName23_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 230),
    _RegControllerName23_Type()
)
regControllerName23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName23.setStatus("current")
_RegControllerName24_Type = Integer32
_RegControllerName24_Object = MibScalar
regControllerName24 = _RegControllerName24_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 231),
    _RegControllerName24_Type()
)
regControllerName24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName24.setStatus("current")
_RegControllerName25_Type = Integer32
_RegControllerName25_Object = MibScalar
regControllerName25 = _RegControllerName25_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 232),
    _RegControllerName25_Type()
)
regControllerName25.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName25.setStatus("current")
_RegControllerName26_Type = Integer32
_RegControllerName26_Object = MibScalar
regControllerName26 = _RegControllerName26_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 233),
    _RegControllerName26_Type()
)
regControllerName26.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName26.setStatus("current")
_RegControllerName27_Type = Integer32
_RegControllerName27_Object = MibScalar
regControllerName27 = _RegControllerName27_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 234),
    _RegControllerName27_Type()
)
regControllerName27.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName27.setStatus("current")
_RegControllerName28_Type = Integer32
_RegControllerName28_Object = MibScalar
regControllerName28 = _RegControllerName28_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 235),
    _RegControllerName28_Type()
)
regControllerName28.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName28.setStatus("current")
_RegControllerName29_Type = Integer32
_RegControllerName29_Object = MibScalar
regControllerName29 = _RegControllerName29_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 236),
    _RegControllerName29_Type()
)
regControllerName29.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName29.setStatus("current")
_RegControllerName30_Type = Integer32
_RegControllerName30_Object = MibScalar
regControllerName30 = _RegControllerName30_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 237),
    _RegControllerName30_Type()
)
regControllerName30.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName30.setStatus("current")
_RegControllerName31_Type = Integer32
_RegControllerName31_Object = MibScalar
regControllerName31 = _RegControllerName31_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 238),
    _RegControllerName31_Type()
)
regControllerName31.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName31.setStatus("current")
_RegControllerName32_Type = Integer32
_RegControllerName32_Object = MibScalar
regControllerName32 = _RegControllerName32_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 239),
    _RegControllerName32_Type()
)
regControllerName32.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName32.setStatus("current")
_RegControllerName33_Type = Integer32
_RegControllerName33_Object = MibScalar
regControllerName33 = _RegControllerName33_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 240),
    _RegControllerName33_Type()
)
regControllerName33.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName33.setStatus("current")
_RegControllerName34_Type = Integer32
_RegControllerName34_Object = MibScalar
regControllerName34 = _RegControllerName34_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 241),
    _RegControllerName34_Type()
)
regControllerName34.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName34.setStatus("current")
_RegControllerName35_Type = Integer32
_RegControllerName35_Object = MibScalar
regControllerName35 = _RegControllerName35_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 242),
    _RegControllerName35_Type()
)
regControllerName35.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName35.setStatus("current")
_RegControllerName36_Type = Integer32
_RegControllerName36_Object = MibScalar
regControllerName36 = _RegControllerName36_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 243),
    _RegControllerName36_Type()
)
regControllerName36.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName36.setStatus("current")
_RegControllerName37_Type = Integer32
_RegControllerName37_Object = MibScalar
regControllerName37 = _RegControllerName37_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 244),
    _RegControllerName37_Type()
)
regControllerName37.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName37.setStatus("current")
_RegControllerName38_Type = Integer32
_RegControllerName38_Object = MibScalar
regControllerName38 = _RegControllerName38_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 245),
    _RegControllerName38_Type()
)
regControllerName38.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName38.setStatus("current")
_RegControllerName39_Type = Integer32
_RegControllerName39_Object = MibScalar
regControllerName39 = _RegControllerName39_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 246),
    _RegControllerName39_Type()
)
regControllerName39.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName39.setStatus("current")
_RegControllerName40_Type = Integer32
_RegControllerName40_Object = MibScalar
regControllerName40 = _RegControllerName40_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 247),
    _RegControllerName40_Type()
)
regControllerName40.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName40.setStatus("current")
_RegControllerName41_Type = Integer32
_RegControllerName41_Object = MibScalar
regControllerName41 = _RegControllerName41_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 248),
    _RegControllerName41_Type()
)
regControllerName41.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName41.setStatus("current")
_RegControllerName42_Type = Integer32
_RegControllerName42_Object = MibScalar
regControllerName42 = _RegControllerName42_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 249),
    _RegControllerName42_Type()
)
regControllerName42.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName42.setStatus("current")
_RegControllerName43_Type = Integer32
_RegControllerName43_Object = MibScalar
regControllerName43 = _RegControllerName43_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 250),
    _RegControllerName43_Type()
)
regControllerName43.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName43.setStatus("current")
_RegControllerName44_Type = Integer32
_RegControllerName44_Object = MibScalar
regControllerName44 = _RegControllerName44_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 251),
    _RegControllerName44_Type()
)
regControllerName44.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName44.setStatus("current")
_RegControllerName45_Type = Integer32
_RegControllerName45_Object = MibScalar
regControllerName45 = _RegControllerName45_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 252),
    _RegControllerName45_Type()
)
regControllerName45.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName45.setStatus("current")
_RegControllerName46_Type = Integer32
_RegControllerName46_Object = MibScalar
regControllerName46 = _RegControllerName46_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 253),
    _RegControllerName46_Type()
)
regControllerName46.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName46.setStatus("current")
_RegControllerName47_Type = Integer32
_RegControllerName47_Object = MibScalar
regControllerName47 = _RegControllerName47_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 254),
    _RegControllerName47_Type()
)
regControllerName47.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName47.setStatus("current")
_RegControllerName48_Type = Integer32
_RegControllerName48_Object = MibScalar
regControllerName48 = _RegControllerName48_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 255),
    _RegControllerName48_Type()
)
regControllerName48.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName48.setStatus("current")
_RegControllerName49_Type = Integer32
_RegControllerName49_Object = MibScalar
regControllerName49 = _RegControllerName49_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 256),
    _RegControllerName49_Type()
)
regControllerName49.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName49.setStatus("current")
_RegControllerName50_Type = Integer32
_RegControllerName50_Object = MibScalar
regControllerName50 = _RegControllerName50_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 257),
    _RegControllerName50_Type()
)
regControllerName50.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName50.setStatus("current")
_RegControllerName51_Type = Integer32
_RegControllerName51_Object = MibScalar
regControllerName51 = _RegControllerName51_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 258),
    _RegControllerName51_Type()
)
regControllerName51.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName51.setStatus("current")
_RegControllerName52_Type = Integer32
_RegControllerName52_Object = MibScalar
regControllerName52 = _RegControllerName52_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 259),
    _RegControllerName52_Type()
)
regControllerName52.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName52.setStatus("current")
_RegControllerName53_Type = Integer32
_RegControllerName53_Object = MibScalar
regControllerName53 = _RegControllerName53_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 260),
    _RegControllerName53_Type()
)
regControllerName53.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName53.setStatus("current")
_RegControllerName54_Type = Integer32
_RegControllerName54_Object = MibScalar
regControllerName54 = _RegControllerName54_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 261),
    _RegControllerName54_Type()
)
regControllerName54.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName54.setStatus("current")
_RegControllerName55_Type = Integer32
_RegControllerName55_Object = MibScalar
regControllerName55 = _RegControllerName55_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 262),
    _RegControllerName55_Type()
)
regControllerName55.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regControllerName55.setStatus("current")
_RegClockYear_Type = Integer32
_RegClockYear_Object = MibScalar
regClockYear = _RegClockYear_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 263),
    _RegClockYear_Type()
)
regClockYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regClockYear.setStatus("current")
_RegClockMonth_Type = Integer32
_RegClockMonth_Object = MibScalar
regClockMonth = _RegClockMonth_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 264),
    _RegClockMonth_Type()
)
regClockMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regClockMonth.setStatus("current")
_RegClockDay_Type = Integer32
_RegClockDay_Object = MibScalar
regClockDay = _RegClockDay_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 265),
    _RegClockDay_Type()
)
regClockDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regClockDay.setStatus("current")
_RegClockHour_Type = Integer32
_RegClockHour_Object = MibScalar
regClockHour = _RegClockHour_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 266),
    _RegClockHour_Type()
)
regClockHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regClockHour.setStatus("current")
_RegClockMinute_Type = Integer32
_RegClockMinute_Object = MibScalar
regClockMinute = _RegClockMinute_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 267),
    _RegClockMinute_Type()
)
regClockMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regClockMinute.setStatus("current")
_RegClockSecond_Type = Integer32
_RegClockSecond_Object = MibScalar
regClockSecond = _RegClockSecond_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 268),
    _RegClockSecond_Type()
)
regClockSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regClockSecond.setStatus("current")
_RegDataLoggingInterval_Type = Integer32
_RegDataLoggingInterval_Object = MibScalar
regDataLoggingInterval = _RegDataLoggingInterval_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 269),
    _RegDataLoggingInterval_Type()
)
regDataLoggingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regDataLoggingInterval.setStatus("current")
_RegRelay1_Type = Integer32
_RegRelay1_Object = MibScalar
regRelay1 = _RegRelay1_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 280),
    _RegRelay1_Type()
)
regRelay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regRelay1.setStatus("current")
_RegRelay2_Type = Integer32
_RegRelay2_Object = MibScalar
regRelay2 = _RegRelay2_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 281),
    _RegRelay2_Type()
)
regRelay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regRelay2.setStatus("current")
_RegBatteryLowAlarmEnable_Type = Integer32
_RegBatteryLowAlarmEnable_Object = MibScalar
regBatteryLowAlarmEnable = _RegBatteryLowAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 290),
    _RegBatteryLowAlarmEnable_Type()
)
regBatteryLowAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regBatteryLowAlarmEnable.setStatus("current")
_RegBatteryLowTriggerVoltage_Type = Integer32
_RegBatteryLowTriggerVoltage_Object = MibScalar
regBatteryLowTriggerVoltage = _RegBatteryLowTriggerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 291),
    _RegBatteryLowTriggerVoltage_Type()
)
regBatteryLowTriggerVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regBatteryLowTriggerVoltage.setStatus("current")
_RegBatteryLowResetVoltage_Type = Integer32
_RegBatteryLowResetVoltage_Object = MibScalar
regBatteryLowResetVoltage = _RegBatteryLowResetVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 292),
    _RegBatteryLowResetVoltage_Type()
)
regBatteryLowResetVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regBatteryLowResetVoltage.setStatus("current")
_RegBatteryHighAlarmEnable_Type = Integer32
_RegBatteryHighAlarmEnable_Object = MibScalar
regBatteryHighAlarmEnable = _RegBatteryHighAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 293),
    _RegBatteryHighAlarmEnable_Type()
)
regBatteryHighAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regBatteryHighAlarmEnable.setStatus("current")
_RegBatteryHighTriggerVoltage_Type = Integer32
_RegBatteryHighTriggerVoltage_Object = MibScalar
regBatteryHighTriggerVoltage = _RegBatteryHighTriggerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 294),
    _RegBatteryHighTriggerVoltage_Type()
)
regBatteryHighTriggerVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regBatteryHighTriggerVoltage.setStatus("current")
_RegBatteryHighResetVoltage_Type = Integer32
_RegBatteryHighResetVoltage_Object = MibScalar
regBatteryHighResetVoltage = _RegBatteryHighResetVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 295),
    _RegBatteryHighResetVoltage_Type()
)
regBatteryHighResetVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regBatteryHighResetVoltage.setStatus("current")
_RegTemperatureLowAlarmEnable_Type = Integer32
_RegTemperatureLowAlarmEnable_Object = MibScalar
regTemperatureLowAlarmEnable = _RegTemperatureLowAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 296),
    _RegTemperatureLowAlarmEnable_Type()
)
regTemperatureLowAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regTemperatureLowAlarmEnable.setStatus("current")
_RegTemperatureLowTrigger_Type = Integer32
_RegTemperatureLowTrigger_Object = MibScalar
regTemperatureLowTrigger = _RegTemperatureLowTrigger_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 297),
    _RegTemperatureLowTrigger_Type()
)
regTemperatureLowTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regTemperatureLowTrigger.setStatus("current")
_RegTemperatureLowReset_Type = Integer32
_RegTemperatureLowReset_Object = MibScalar
regTemperatureLowReset = _RegTemperatureLowReset_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 298),
    _RegTemperatureLowReset_Type()
)
regTemperatureLowReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regTemperatureLowReset.setStatus("current")
_RegTemperatureHighAlarmEnable_Type = Integer32
_RegTemperatureHighAlarmEnable_Object = MibScalar
regTemperatureHighAlarmEnable = _RegTemperatureHighAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 299),
    _RegTemperatureHighAlarmEnable_Type()
)
regTemperatureHighAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regTemperatureHighAlarmEnable.setStatus("current")
_RegTemperatureHighTrigger_Type = Integer32
_RegTemperatureHighTrigger_Object = MibScalar
regTemperatureHighTrigger = _RegTemperatureHighTrigger_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 300),
    _RegTemperatureHighTrigger_Type()
)
regTemperatureHighTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regTemperatureHighTrigger.setStatus("current")
_RegTemperatureHighReset_Type = Integer32
_RegTemperatureHighReset_Object = MibScalar
regTemperatureHighReset = _RegTemperatureHighReset_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 301),
    _RegTemperatureHighReset_Type()
)
regTemperatureHighReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regTemperatureHighReset.setStatus("current")
_RegAnalog1LowAlarmEnable_Type = Integer32
_RegAnalog1LowAlarmEnable_Object = MibScalar
regAnalog1LowAlarmEnable = _RegAnalog1LowAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 302),
    _RegAnalog1LowAlarmEnable_Type()
)
regAnalog1LowAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAnalog1LowAlarmEnable.setStatus("current")
_RegAnalog1LowTriggerVoltage_Type = Integer32
_RegAnalog1LowTriggerVoltage_Object = MibScalar
regAnalog1LowTriggerVoltage = _RegAnalog1LowTriggerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 303),
    _RegAnalog1LowTriggerVoltage_Type()
)
regAnalog1LowTriggerVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAnalog1LowTriggerVoltage.setStatus("current")
_RegAnalog1LowResetVoltage_Type = Integer32
_RegAnalog1LowResetVoltage_Object = MibScalar
regAnalog1LowResetVoltage = _RegAnalog1LowResetVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 304),
    _RegAnalog1LowResetVoltage_Type()
)
regAnalog1LowResetVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAnalog1LowResetVoltage.setStatus("current")
_RegAnalog1HighAlarmEnable_Type = Integer32
_RegAnalog1HighAlarmEnable_Object = MibScalar
regAnalog1HighAlarmEnable = _RegAnalog1HighAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 305),
    _RegAnalog1HighAlarmEnable_Type()
)
regAnalog1HighAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAnalog1HighAlarmEnable.setStatus("current")
_RegAnalog1HighTriggerVoltage_Type = Integer32
_RegAnalog1HighTriggerVoltage_Object = MibScalar
regAnalog1HighTriggerVoltage = _RegAnalog1HighTriggerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 306),
    _RegAnalog1HighTriggerVoltage_Type()
)
regAnalog1HighTriggerVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAnalog1HighTriggerVoltage.setStatus("current")
_RegAnalog1HighResetVoltage_Type = Integer32
_RegAnalog1HighResetVoltage_Object = MibScalar
regAnalog1HighResetVoltage = _RegAnalog1HighResetVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 307),
    _RegAnalog1HighResetVoltage_Type()
)
regAnalog1HighResetVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAnalog1HighResetVoltage.setStatus("current")
_RegAnalog2LowAlarmEnable_Type = Integer32
_RegAnalog2LowAlarmEnable_Object = MibScalar
regAnalog2LowAlarmEnable = _RegAnalog2LowAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 308),
    _RegAnalog2LowAlarmEnable_Type()
)
regAnalog2LowAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAnalog2LowAlarmEnable.setStatus("current")
_RegAnalog2LowTriggerVoltage_Type = Integer32
_RegAnalog2LowTriggerVoltage_Object = MibScalar
regAnalog2LowTriggerVoltage = _RegAnalog2LowTriggerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 309),
    _RegAnalog2LowTriggerVoltage_Type()
)
regAnalog2LowTriggerVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAnalog2LowTriggerVoltage.setStatus("current")
_RegAnalog2LowResetVoltage_Type = Integer32
_RegAnalog2LowResetVoltage_Object = MibScalar
regAnalog2LowResetVoltage = _RegAnalog2LowResetVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 310),
    _RegAnalog2LowResetVoltage_Type()
)
regAnalog2LowResetVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAnalog2LowResetVoltage.setStatus("current")
_RegAnalog2HighAlarmEnable_Type = Integer32
_RegAnalog2HighAlarmEnable_Object = MibScalar
regAnalog2HighAlarmEnable = _RegAnalog2HighAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 311),
    _RegAnalog2HighAlarmEnable_Type()
)
regAnalog2HighAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAnalog2HighAlarmEnable.setStatus("current")
_RegAnalog2HighTriggerVoltage_Type = Integer32
_RegAnalog2HighTriggerVoltage_Object = MibScalar
regAnalog2HighTriggerVoltage = _RegAnalog2HighTriggerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 312),
    _RegAnalog2HighTriggerVoltage_Type()
)
regAnalog2HighTriggerVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAnalog2HighTriggerVoltage.setStatus("current")
_RegAnalog2HighResetVoltage_Type = Integer32
_RegAnalog2HighResetVoltage_Object = MibScalar
regAnalog2HighResetVoltage = _RegAnalog2HighResetVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 313),
    _RegAnalog2HighResetVoltage_Type()
)
regAnalog2HighResetVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAnalog2HighResetVoltage.setStatus("current")
_RegDigital1TriggeredAlarmEnable_Type = Integer32
_RegDigital1TriggeredAlarmEnable_Object = MibScalar
regDigital1TriggeredAlarmEnable = _RegDigital1TriggeredAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 362),
    _RegDigital1TriggeredAlarmEnable_Type()
)
regDigital1TriggeredAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regDigital1TriggeredAlarmEnable.setStatus("current")
_RegDigital1TriggeredCycle_Type = Integer32
_RegDigital1TriggeredCycle_Object = MibScalar
regDigital1TriggeredCycle = _RegDigital1TriggeredCycle_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 363),
    _RegDigital1TriggeredCycle_Type()
)
regDigital1TriggeredCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regDigital1TriggeredCycle.setStatus("current")
_RegDigital1OpenAlarmEnable_Type = Integer32
_RegDigital1OpenAlarmEnable_Object = MibScalar
regDigital1OpenAlarmEnable = _RegDigital1OpenAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 364),
    _RegDigital1OpenAlarmEnable_Type()
)
regDigital1OpenAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regDigital1OpenAlarmEnable.setStatus("current")
_RegDigital1OpenCycle_Type = Integer32
_RegDigital1OpenCycle_Object = MibScalar
regDigital1OpenCycle = _RegDigital1OpenCycle_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 365),
    _RegDigital1OpenCycle_Type()
)
regDigital1OpenCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regDigital1OpenCycle.setStatus("current")
_RegDigital2TriggeredAlarmEnable_Type = Integer32
_RegDigital2TriggeredAlarmEnable_Object = MibScalar
regDigital2TriggeredAlarmEnable = _RegDigital2TriggeredAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 366),
    _RegDigital2TriggeredAlarmEnable_Type()
)
regDigital2TriggeredAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regDigital2TriggeredAlarmEnable.setStatus("current")
_RegDigital2TriggeredCycle_Type = Integer32
_RegDigital2TriggeredCycle_Object = MibScalar
regDigital2TriggeredCycle = _RegDigital2TriggeredCycle_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 367),
    _RegDigital2TriggeredCycle_Type()
)
regDigital2TriggeredCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regDigital2TriggeredCycle.setStatus("current")
_RegDigital2OpenAlarmEnable_Type = Integer32
_RegDigital2OpenAlarmEnable_Object = MibScalar
regDigital2OpenAlarmEnable = _RegDigital2OpenAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 368),
    _RegDigital2OpenAlarmEnable_Type()
)
regDigital2OpenAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regDigital2OpenAlarmEnable.setStatus("current")
_RegDigital2OpenCycle_Type = Integer32
_RegDigital2OpenCycle_Object = MibScalar
regDigital2OpenCycle = _RegDigital2OpenCycle_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 369),
    _RegDigital2OpenCycle_Type()
)
regDigital2OpenCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regDigital2OpenCycle.setStatus("current")
_RegHardwareAlarmEnable_Type = Integer32
_RegHardwareAlarmEnable_Object = MibScalar
regHardwareAlarmEnable = _RegHardwareAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 402),
    _RegHardwareAlarmEnable_Type()
)
regHardwareAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regHardwareAlarmEnable.setStatus("current")
_RegHardwareAlarmCycle_Type = Integer32
_RegHardwareAlarmCycle_Object = MibScalar
regHardwareAlarmCycle = _RegHardwareAlarmCycle_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 403),
    _RegHardwareAlarmCycle_Type()
)
regHardwareAlarmCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regHardwareAlarmCycle.setStatus("current")
_RegBatteryZeroPoint_Type = Integer32
_RegBatteryZeroPoint_Object = MibScalar
regBatteryZeroPoint = _RegBatteryZeroPoint_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 410),
    _RegBatteryZeroPoint_Type()
)
regBatteryZeroPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regBatteryZeroPoint.setStatus("current")
_RegBatteryMidPoint_Type = Integer32
_RegBatteryMidPoint_Object = MibScalar
regBatteryMidPoint = _RegBatteryMidPoint_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 411),
    _RegBatteryMidPoint_Type()
)
regBatteryMidPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regBatteryMidPoint.setStatus("current")
_RegBatteryMidPointVoltage_Type = Integer32
_RegBatteryMidPointVoltage_Object = MibScalar
regBatteryMidPointVoltage = _RegBatteryMidPointVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 412),
    _RegBatteryMidPointVoltage_Type()
)
regBatteryMidPointVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regBatteryMidPointVoltage.setStatus("current")
_RegAnalog1ZeroPoint32V_Type = Integer32
_RegAnalog1ZeroPoint32V_Object = MibScalar
regAnalog1ZeroPoint32V = _RegAnalog1ZeroPoint32V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 413),
    _RegAnalog1ZeroPoint32V_Type()
)
regAnalog1ZeroPoint32V.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAnalog1ZeroPoint32V.setStatus("current")
_RegAnalog1MidPoint32V_Type = Integer32
_RegAnalog1MidPoint32V_Object = MibScalar
regAnalog1MidPoint32V = _RegAnalog1MidPoint32V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 414),
    _RegAnalog1MidPoint32V_Type()
)
regAnalog1MidPoint32V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regAnalog1MidPoint32V.setStatus("current")
_RegAnalog1MidPointVoltage32V_Type = Integer32
_RegAnalog1MidPointVoltage32V_Object = MibScalar
regAnalog1MidPointVoltage32V = _RegAnalog1MidPointVoltage32V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 415),
    _RegAnalog1MidPointVoltage32V_Type()
)
regAnalog1MidPointVoltage32V.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAnalog1MidPointVoltage32V.setStatus("current")
_RegAnalog1ZeroPoint5V_Type = Integer32
_RegAnalog1ZeroPoint5V_Object = MibScalar
regAnalog1ZeroPoint5V = _RegAnalog1ZeroPoint5V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 416),
    _RegAnalog1ZeroPoint5V_Type()
)
regAnalog1ZeroPoint5V.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAnalog1ZeroPoint5V.setStatus("current")
_RegAnalog1MidPoint5V_Type = Integer32
_RegAnalog1MidPoint5V_Object = MibScalar
regAnalog1MidPoint5V = _RegAnalog1MidPoint5V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 417),
    _RegAnalog1MidPoint5V_Type()
)
regAnalog1MidPoint5V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regAnalog1MidPoint5V.setStatus("current")
_RegAnalog1MidPointVoltage5V_Type = Integer32
_RegAnalog1MidPointVoltage5V_Object = MibScalar
regAnalog1MidPointVoltage5V = _RegAnalog1MidPointVoltage5V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 418),
    _RegAnalog1MidPointVoltage5V_Type()
)
regAnalog1MidPointVoltage5V.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAnalog1MidPointVoltage5V.setStatus("current")
_RegAnalog1ZeroPoint420mA_Type = Integer32
_RegAnalog1ZeroPoint420mA_Object = MibScalar
regAnalog1ZeroPoint420mA = _RegAnalog1ZeroPoint420mA_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 419),
    _RegAnalog1ZeroPoint420mA_Type()
)
regAnalog1ZeroPoint420mA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAnalog1ZeroPoint420mA.setStatus("current")
_RegAnalog1MidPoint420mA_Type = Integer32
_RegAnalog1MidPoint420mA_Object = MibScalar
regAnalog1MidPoint420mA = _RegAnalog1MidPoint420mA_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 420),
    _RegAnalog1MidPoint420mA_Type()
)
regAnalog1MidPoint420mA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regAnalog1MidPoint420mA.setStatus("current")
_RegAnalog1MidPointCurrent420mA_Type = Integer32
_RegAnalog1MidPointCurrent420mA_Object = MibScalar
regAnalog1MidPointCurrent420mA = _RegAnalog1MidPointCurrent420mA_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 421),
    _RegAnalog1MidPointCurrent420mA_Type()
)
regAnalog1MidPointCurrent420mA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAnalog1MidPointCurrent420mA.setStatus("current")
_RegAnalog2ZeroPoint32V_Type = Integer32
_RegAnalog2ZeroPoint32V_Object = MibScalar
regAnalog2ZeroPoint32V = _RegAnalog2ZeroPoint32V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 422),
    _RegAnalog2ZeroPoint32V_Type()
)
regAnalog2ZeroPoint32V.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAnalog2ZeroPoint32V.setStatus("current")
_RegAnalog2MidPoint32V_Type = Integer32
_RegAnalog2MidPoint32V_Object = MibScalar
regAnalog2MidPoint32V = _RegAnalog2MidPoint32V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 423),
    _RegAnalog2MidPoint32V_Type()
)
regAnalog2MidPoint32V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regAnalog2MidPoint32V.setStatus("current")
_RegAnalog2MidPointVoltage32V_Type = Integer32
_RegAnalog2MidPointVoltage32V_Object = MibScalar
regAnalog2MidPointVoltage32V = _RegAnalog2MidPointVoltage32V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 424),
    _RegAnalog2MidPointVoltage32V_Type()
)
regAnalog2MidPointVoltage32V.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAnalog2MidPointVoltage32V.setStatus("current")
_RegAnalog2ZeroPoint5V_Type = Integer32
_RegAnalog2ZeroPoint5V_Object = MibScalar
regAnalog2ZeroPoint5V = _RegAnalog2ZeroPoint5V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 425),
    _RegAnalog2ZeroPoint5V_Type()
)
regAnalog2ZeroPoint5V.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAnalog2ZeroPoint5V.setStatus("current")
_RegAnalog2MidPoint5V_Type = Integer32
_RegAnalog2MidPoint5V_Object = MibScalar
regAnalog2MidPoint5V = _RegAnalog2MidPoint5V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 426),
    _RegAnalog2MidPoint5V_Type()
)
regAnalog2MidPoint5V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regAnalog2MidPoint5V.setStatus("current")
_RegAnalog2MidPointVoltage5V_Type = Integer32
_RegAnalog2MidPointVoltage5V_Object = MibScalar
regAnalog2MidPointVoltage5V = _RegAnalog2MidPointVoltage5V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 427),
    _RegAnalog2MidPointVoltage5V_Type()
)
regAnalog2MidPointVoltage5V.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAnalog2MidPointVoltage5V.setStatus("current")
_RegAnalog2ZeroPoint420mA_Type = Integer32
_RegAnalog2ZeroPoint420mA_Object = MibScalar
regAnalog2ZeroPoint420mA = _RegAnalog2ZeroPoint420mA_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 428),
    _RegAnalog2ZeroPoint420mA_Type()
)
regAnalog2ZeroPoint420mA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAnalog2ZeroPoint420mA.setStatus("current")
_RegAnalog2MidPoint420mA_Type = Integer32
_RegAnalog2MidPoint420mA_Object = MibScalar
regAnalog2MidPoint420mA = _RegAnalog2MidPoint420mA_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 429),
    _RegAnalog2MidPoint420mA_Type()
)
regAnalog2MidPoint420mA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regAnalog2MidPoint420mA.setStatus("current")
_RegAnalog2MidPointCurrent420mA_Type = Integer32
_RegAnalog2MidPointCurrent420mA_Object = MibScalar
regAnalog2MidPointCurrent420mA = _RegAnalog2MidPointCurrent420mA_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 430),
    _RegAnalog2MidPointCurrent420mA_Type()
)
regAnalog2MidPointCurrent420mA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAnalog2MidPointCurrent420mA.setStatus("current")
_RegForceBuffers_Type = Integer32
_RegForceBuffers_Object = MibScalar
regForceBuffers = _RegForceBuffers_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 500),
    _RegForceBuffers_Type()
)
regForceBuffers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regForceBuffers.setStatus("current")
_RegAlarmActionBatLowTrigger_Type = Integer32
_RegAlarmActionBatLowTrigger_Object = MibScalar
regAlarmActionBatLowTrigger = _RegAlarmActionBatLowTrigger_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 600),
    _RegAlarmActionBatLowTrigger_Type()
)
regAlarmActionBatLowTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAlarmActionBatLowTrigger.setStatus("current")
_RegAlarmActionBatLowReset_Type = Integer32
_RegAlarmActionBatLowReset_Object = MibScalar
regAlarmActionBatLowReset = _RegAlarmActionBatLowReset_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 601),
    _RegAlarmActionBatLowReset_Type()
)
regAlarmActionBatLowReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAlarmActionBatLowReset.setStatus("current")
_RegAlarmActionBatHighTrigger_Type = Integer32
_RegAlarmActionBatHighTrigger_Object = MibScalar
regAlarmActionBatHighTrigger = _RegAlarmActionBatHighTrigger_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 602),
    _RegAlarmActionBatHighTrigger_Type()
)
regAlarmActionBatHighTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAlarmActionBatHighTrigger.setStatus("current")
_RegAlarmActionBatHighReset_Type = Integer32
_RegAlarmActionBatHighReset_Object = MibScalar
regAlarmActionBatHighReset = _RegAlarmActionBatHighReset_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 603),
    _RegAlarmActionBatHighReset_Type()
)
regAlarmActionBatHighReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAlarmActionBatHighReset.setStatus("current")
_RegAlarmActionTempLowTrigger_Type = Integer32
_RegAlarmActionTempLowTrigger_Object = MibScalar
regAlarmActionTempLowTrigger = _RegAlarmActionTempLowTrigger_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 604),
    _RegAlarmActionTempLowTrigger_Type()
)
regAlarmActionTempLowTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAlarmActionTempLowTrigger.setStatus("current")
_RegAlarmActionTempLowReset_Type = Integer32
_RegAlarmActionTempLowReset_Object = MibScalar
regAlarmActionTempLowReset = _RegAlarmActionTempLowReset_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 605),
    _RegAlarmActionTempLowReset_Type()
)
regAlarmActionTempLowReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAlarmActionTempLowReset.setStatus("current")
_RegAlarmActionTempHighTrigger_Type = Integer32
_RegAlarmActionTempHighTrigger_Object = MibScalar
regAlarmActionTempHighTrigger = _RegAlarmActionTempHighTrigger_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 606),
    _RegAlarmActionTempHighTrigger_Type()
)
regAlarmActionTempHighTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAlarmActionTempHighTrigger.setStatus("current")
_RegAlarmActionTempHighReset_Type = Integer32
_RegAlarmActionTempHighReset_Object = MibScalar
regAlarmActionTempHighReset = _RegAlarmActionTempHighReset_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 607),
    _RegAlarmActionTempHighReset_Type()
)
regAlarmActionTempHighReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAlarmActionTempHighReset.setStatus("current")
_RegAlarmActionAIN1LowTrigger_Type = Integer32
_RegAlarmActionAIN1LowTrigger_Object = MibScalar
regAlarmActionAIN1LowTrigger = _RegAlarmActionAIN1LowTrigger_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 608),
    _RegAlarmActionAIN1LowTrigger_Type()
)
regAlarmActionAIN1LowTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAlarmActionAIN1LowTrigger.setStatus("current")
_RegAlarmActionAIN1LowReset_Type = Integer32
_RegAlarmActionAIN1LowReset_Object = MibScalar
regAlarmActionAIN1LowReset = _RegAlarmActionAIN1LowReset_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 609),
    _RegAlarmActionAIN1LowReset_Type()
)
regAlarmActionAIN1LowReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAlarmActionAIN1LowReset.setStatus("current")
_RegAlarmActionAIN1HighTrigger_Type = Integer32
_RegAlarmActionAIN1HighTrigger_Object = MibScalar
regAlarmActionAIN1HighTrigger = _RegAlarmActionAIN1HighTrigger_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 610),
    _RegAlarmActionAIN1HighTrigger_Type()
)
regAlarmActionAIN1HighTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAlarmActionAIN1HighTrigger.setStatus("current")
_RegAlarmActionAIN1HighReset_Type = Integer32
_RegAlarmActionAIN1HighReset_Object = MibScalar
regAlarmActionAIN1HighReset = _RegAlarmActionAIN1HighReset_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 611),
    _RegAlarmActionAIN1HighReset_Type()
)
regAlarmActionAIN1HighReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAlarmActionAIN1HighReset.setStatus("current")
_RegAlarmActionAIN2LowTrigger_Type = Integer32
_RegAlarmActionAIN2LowTrigger_Object = MibScalar
regAlarmActionAIN2LowTrigger = _RegAlarmActionAIN2LowTrigger_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 612),
    _RegAlarmActionAIN2LowTrigger_Type()
)
regAlarmActionAIN2LowTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAlarmActionAIN2LowTrigger.setStatus("current")
_RegAlarmActionAIN2LowReset_Type = Integer32
_RegAlarmActionAIN2LowReset_Object = MibScalar
regAlarmActionAIN2LowReset = _RegAlarmActionAIN2LowReset_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 613),
    _RegAlarmActionAIN2LowReset_Type()
)
regAlarmActionAIN2LowReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAlarmActionAIN2LowReset.setStatus("current")
_RegAlarmActionAIN2HighTrigger_Type = Integer32
_RegAlarmActionAIN2HighTrigger_Object = MibScalar
regAlarmActionAIN2HighTrigger = _RegAlarmActionAIN2HighTrigger_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 614),
    _RegAlarmActionAIN2HighTrigger_Type()
)
regAlarmActionAIN2HighTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAlarmActionAIN2HighTrigger.setStatus("current")
_RegAlarmActionAIN2HighReset_Type = Integer32
_RegAlarmActionAIN2HighReset_Object = MibScalar
regAlarmActionAIN2HighReset = _RegAlarmActionAIN2HighReset_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 615),
    _RegAlarmActionAIN2HighReset_Type()
)
regAlarmActionAIN2HighReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAlarmActionAIN2HighReset.setStatus("current")
_RegAlarmActionDIN1Trigger_Type = Integer32
_RegAlarmActionDIN1Trigger_Object = MibScalar
regAlarmActionDIN1Trigger = _RegAlarmActionDIN1Trigger_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 648),
    _RegAlarmActionDIN1Trigger_Type()
)
regAlarmActionDIN1Trigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAlarmActionDIN1Trigger.setStatus("current")
_RegAlarmActionDIN1Reset_Type = Integer32
_RegAlarmActionDIN1Reset_Object = MibScalar
regAlarmActionDIN1Reset = _RegAlarmActionDIN1Reset_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 649),
    _RegAlarmActionDIN1Reset_Type()
)
regAlarmActionDIN1Reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAlarmActionDIN1Reset.setStatus("current")
_RegAlarmActionDIN2Trigger_Type = Integer32
_RegAlarmActionDIN2Trigger_Object = MibScalar
regAlarmActionDIN2Trigger = _RegAlarmActionDIN2Trigger_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 650),
    _RegAlarmActionDIN2Trigger_Type()
)
regAlarmActionDIN2Trigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAlarmActionDIN2Trigger.setStatus("current")
_RegAlarmActionDIN2Reset_Type = Integer32
_RegAlarmActionDIN2Reset_Object = MibScalar
regAlarmActionDIN2Reset = _RegAlarmActionDIN2Reset_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 651),
    _RegAlarmActionDIN2Reset_Type()
)
regAlarmActionDIN2Reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regAlarmActionDIN2Reset.setStatus("current")
_RegBatteryVoltage_Type = Integer32
_RegBatteryVoltage_Object = MibScalar
regBatteryVoltage = _RegBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1000),
    _RegBatteryVoltage_Type()
)
regBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regBatteryVoltage.setStatus("current")
_RegTemperature_Type = Integer32
_RegTemperature_Object = MibScalar
regTemperature = _RegTemperature_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1001),
    _RegTemperature_Type()
)
regTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regTemperature.setStatus("current")
_RegAnalog132V_Type = Integer32
_RegAnalog132V_Object = MibScalar
regAnalog132V = _RegAnalog132V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1002),
    _RegAnalog132V_Type()
)
regAnalog132V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regAnalog132V.setStatus("current")
_RegAnalog15V_Type = Integer32
_RegAnalog15V_Object = MibScalar
regAnalog15V = _RegAnalog15V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1003),
    _RegAnalog15V_Type()
)
regAnalog15V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regAnalog15V.setStatus("current")
_RegAnalog1420mA_Type = Integer32
_RegAnalog1420mA_Object = MibScalar
regAnalog1420mA = _RegAnalog1420mA_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1004),
    _RegAnalog1420mA_Type()
)
regAnalog1420mA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regAnalog1420mA.setStatus("current")
_RegAnalog232V_Type = Integer32
_RegAnalog232V_Object = MibScalar
regAnalog232V = _RegAnalog232V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1005),
    _RegAnalog232V_Type()
)
regAnalog232V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regAnalog232V.setStatus("current")
_RegAnalog25V_Type = Integer32
_RegAnalog25V_Object = MibScalar
regAnalog25V = _RegAnalog25V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1006),
    _RegAnalog25V_Type()
)
regAnalog25V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regAnalog25V.setStatus("current")
_RegAnalog2420mA_Type = Integer32
_RegAnalog2420mA_Object = MibScalar
regAnalog2420mA = _RegAnalog2420mA_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1007),
    _RegAnalog2420mA_Type()
)
regAnalog2420mA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regAnalog2420mA.setStatus("current")
_RegDigital1_Type = Integer32
_RegDigital1_Object = MibScalar
regDigital1 = _RegDigital1_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1100),
    _RegDigital1_Type()
)
regDigital1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regDigital1.setStatus("current")
_RegDigital2_Type = Integer32
_RegDigital2_Object = MibScalar
regDigital2 = _RegDigital2_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1101),
    _RegDigital2_Type()
)
regDigital2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regDigital2.setStatus("current")
_RegLogPointCountHigh_Type = Integer32
_RegLogPointCountHigh_Object = MibScalar
regLogPointCountHigh = _RegLogPointCountHigh_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1200),
    _RegLogPointCountHigh_Type()
)
regLogPointCountHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLogPointCountHigh.setStatus("current")
_RegLogPointCountLow_Type = Integer32
_RegLogPointCountLow_Object = MibScalar
regLogPointCountLow = _RegLogPointCountLow_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1201),
    _RegLogPointCountLow_Type()
)
regLogPointCountLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLogPointCountLow.setStatus("current")
_RegAlarmPointCount_Type = Integer32
_RegAlarmPointCount_Object = MibScalar
regAlarmPointCount = _RegAlarmPointCount_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1204),
    _RegAlarmPointCount_Type()
)
regAlarmPointCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regAlarmPointCount.setStatus("current")
_RegRelayPointCount_Type = Integer32
_RegRelayPointCount_Object = MibScalar
regRelayPointCount = _RegRelayPointCount_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1205),
    _RegRelayPointCount_Type()
)
regRelayPointCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regRelayPointCount.setStatus("current")
_RegCurrentLogPointHigh_Type = Integer32
_RegCurrentLogPointHigh_Object = MibScalar
regCurrentLogPointHigh = _RegCurrentLogPointHigh_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1300),
    _RegCurrentLogPointHigh_Type()
)
regCurrentLogPointHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regCurrentLogPointHigh.setStatus("current")
_RegCurrentLogPointLow_Type = Integer32
_RegCurrentLogPointLow_Object = MibScalar
regCurrentLogPointLow = _RegCurrentLogPointLow_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1301),
    _RegCurrentLogPointLow_Type()
)
regCurrentLogPointLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regCurrentLogPointLow.setStatus("current")
_RegCurrentAlarmPoint_Type = Integer32
_RegCurrentAlarmPoint_Object = MibScalar
regCurrentAlarmPoint = _RegCurrentAlarmPoint_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1304),
    _RegCurrentAlarmPoint_Type()
)
regCurrentAlarmPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regCurrentAlarmPoint.setStatus("current")
_RegCurrentRelayPoint_Type = Integer32
_RegCurrentRelayPoint_Object = MibScalar
regCurrentRelayPoint = _RegCurrentRelayPoint_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1305),
    _RegCurrentRelayPoint_Type()
)
regCurrentRelayPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regCurrentRelayPoint.setStatus("current")
_RegEraseLogData_Type = Integer32
_RegEraseLogData_Object = MibScalar
regEraseLogData = _RegEraseLogData_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1350),
    _RegEraseLogData_Type()
)
regEraseLogData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regEraseLogData.setStatus("current")
_RegEraseAlarmData_Type = Integer32
_RegEraseAlarmData_Object = MibScalar
regEraseAlarmData = _RegEraseAlarmData_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1351),
    _RegEraseAlarmData_Type()
)
regEraseAlarmData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regEraseAlarmData.setStatus("current")
_RegEraseRelayData_Type = Integer32
_RegEraseRelayData_Object = MibScalar
regEraseRelayData = _RegEraseRelayData_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1352),
    _RegEraseRelayData_Type()
)
regEraseRelayData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regEraseRelayData.setStatus("current")
_RegLogDateYear_Type = Integer32
_RegLogDateYear_Object = MibScalar
regLogDateYear = _RegLogDateYear_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1400),
    _RegLogDateYear_Type()
)
regLogDateYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLogDateYear.setStatus("current")
_RegLogDateMonth_Type = Integer32
_RegLogDateMonth_Object = MibScalar
regLogDateMonth = _RegLogDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1401),
    _RegLogDateMonth_Type()
)
regLogDateMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLogDateMonth.setStatus("current")
_RegLogDateDay_Type = Integer32
_RegLogDateDay_Object = MibScalar
regLogDateDay = _RegLogDateDay_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1402),
    _RegLogDateDay_Type()
)
regLogDateDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLogDateDay.setStatus("current")
_RegLogDateHour_Type = Integer32
_RegLogDateHour_Object = MibScalar
regLogDateHour = _RegLogDateHour_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1403),
    _RegLogDateHour_Type()
)
regLogDateHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLogDateHour.setStatus("current")
_RegLogDateMinute_Type = Integer32
_RegLogDateMinute_Object = MibScalar
regLogDateMinute = _RegLogDateMinute_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1404),
    _RegLogDateMinute_Type()
)
regLogDateMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLogDateMinute.setStatus("current")
_RegLogDateSecond_Type = Integer32
_RegLogDateSecond_Object = MibScalar
regLogDateSecond = _RegLogDateSecond_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1405),
    _RegLogDateSecond_Type()
)
regLogDateSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLogDateSecond.setStatus("current")
_RegLogBatteryVoltage_Type = Integer32
_RegLogBatteryVoltage_Object = MibScalar
regLogBatteryVoltage = _RegLogBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1406),
    _RegLogBatteryVoltage_Type()
)
regLogBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLogBatteryVoltage.setStatus("current")
_RegLogTemperature_Type = Integer32
_RegLogTemperature_Object = MibScalar
regLogTemperature = _RegLogTemperature_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1407),
    _RegLogTemperature_Type()
)
regLogTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLogTemperature.setStatus("current")
_RegLogAnalog132V_Type = Integer32
_RegLogAnalog132V_Object = MibScalar
regLogAnalog132V = _RegLogAnalog132V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1408),
    _RegLogAnalog132V_Type()
)
regLogAnalog132V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLogAnalog132V.setStatus("current")
_RegLogAnalog15V_Type = Integer32
_RegLogAnalog15V_Object = MibScalar
regLogAnalog15V = _RegLogAnalog15V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1409),
    _RegLogAnalog15V_Type()
)
regLogAnalog15V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLogAnalog15V.setStatus("current")
_RegLogAnalog1420mA_Type = Integer32
_RegLogAnalog1420mA_Object = MibScalar
regLogAnalog1420mA = _RegLogAnalog1420mA_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1410),
    _RegLogAnalog1420mA_Type()
)
regLogAnalog1420mA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLogAnalog1420mA.setStatus("current")
_RegLogAnalog232V_Type = Integer32
_RegLogAnalog232V_Object = MibScalar
regLogAnalog232V = _RegLogAnalog232V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1411),
    _RegLogAnalog232V_Type()
)
regLogAnalog232V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLogAnalog232V.setStatus("current")
_RegLogAnalog25V_Type = Integer32
_RegLogAnalog25V_Object = MibScalar
regLogAnalog25V = _RegLogAnalog25V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1412),
    _RegLogAnalog25V_Type()
)
regLogAnalog25V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLogAnalog25V.setStatus("current")
_RegLogAnalog2420mA_Type = Integer32
_RegLogAnalog2420mA_Object = MibScalar
regLogAnalog2420mA = _RegLogAnalog2420mA_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1413),
    _RegLogAnalog2420mA_Type()
)
regLogAnalog2420mA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLogAnalog2420mA.setStatus("current")
_RegLogDigital1_Type = Integer32
_RegLogDigital1_Object = MibScalar
regLogDigital1 = _RegLogDigital1_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1414),
    _RegLogDigital1_Type()
)
regLogDigital1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLogDigital1.setStatus("current")
_RegLogDigital2_Type = Integer32
_RegLogDigital2_Object = MibScalar
regLogDigital2 = _RegLogDigital2_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1415),
    _RegLogDigital2_Type()
)
regLogDigital2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLogDigital2.setStatus("current")
_RegAdvanceLog_Type = Integer32
_RegAdvanceLog_Object = MibScalar
regAdvanceLog = _RegAdvanceLog_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1416),
    _RegAdvanceLog_Type()
)
regAdvanceLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regAdvanceLog.setStatus("current")
_RegDecrementLog_Type = Integer32
_RegDecrementLog_Object = MibScalar
regDecrementLog = _RegDecrementLog_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1417),
    _RegDecrementLog_Type()
)
regDecrementLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regDecrementLog.setStatus("current")
_RegAlarmDateYear_Type = Integer32
_RegAlarmDateYear_Object = MibScalar
regAlarmDateYear = _RegAlarmDateYear_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1500),
    _RegAlarmDateYear_Type()
)
regAlarmDateYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regAlarmDateYear.setStatus("current")
_RegAlarmDateMonth_Type = Integer32
_RegAlarmDateMonth_Object = MibScalar
regAlarmDateMonth = _RegAlarmDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1501),
    _RegAlarmDateMonth_Type()
)
regAlarmDateMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regAlarmDateMonth.setStatus("current")
_RegAlarmDateDay_Type = Integer32
_RegAlarmDateDay_Object = MibScalar
regAlarmDateDay = _RegAlarmDateDay_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1502),
    _RegAlarmDateDay_Type()
)
regAlarmDateDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regAlarmDateDay.setStatus("current")
_RegAlarmDateHour_Type = Integer32
_RegAlarmDateHour_Object = MibScalar
regAlarmDateHour = _RegAlarmDateHour_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1503),
    _RegAlarmDateHour_Type()
)
regAlarmDateHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regAlarmDateHour.setStatus("current")
_RegAlarmDateMinute_Type = Integer32
_RegAlarmDateMinute_Object = MibScalar
regAlarmDateMinute = _RegAlarmDateMinute_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1504),
    _RegAlarmDateMinute_Type()
)
regAlarmDateMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regAlarmDateMinute.setStatus("current")
_RegAlarmDateSecond_Type = Integer32
_RegAlarmDateSecond_Object = MibScalar
regAlarmDateSecond = _RegAlarmDateSecond_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1505),
    _RegAlarmDateSecond_Type()
)
regAlarmDateSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regAlarmDateSecond.setStatus("current")
_RegAlarmID_Type = Integer32
_RegAlarmID_Object = MibScalar
regAlarmID = _RegAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1506),
    _RegAlarmID_Type()
)
regAlarmID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regAlarmID.setStatus("current")
_RegAdvanceAlarm_Type = Integer32
_RegAdvanceAlarm_Object = MibScalar
regAdvanceAlarm = _RegAdvanceAlarm_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1507),
    _RegAdvanceAlarm_Type()
)
regAdvanceAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regAdvanceAlarm.setStatus("current")
_RegDecrementAlarm_Type = Integer32
_RegDecrementAlarm_Object = MibScalar
regDecrementAlarm = _RegDecrementAlarm_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1508),
    _RegDecrementAlarm_Type()
)
regDecrementAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regDecrementAlarm.setStatus("current")
_RegRelayDateYear_Type = Integer32
_RegRelayDateYear_Object = MibScalar
regRelayDateYear = _RegRelayDateYear_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1600),
    _RegRelayDateYear_Type()
)
regRelayDateYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regRelayDateYear.setStatus("current")
_RegRelayDateMonth_Type = Integer32
_RegRelayDateMonth_Object = MibScalar
regRelayDateMonth = _RegRelayDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1601),
    _RegRelayDateMonth_Type()
)
regRelayDateMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regRelayDateMonth.setStatus("current")
_RegRelayDateDay_Type = Integer32
_RegRelayDateDay_Object = MibScalar
regRelayDateDay = _RegRelayDateDay_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1602),
    _RegRelayDateDay_Type()
)
regRelayDateDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regRelayDateDay.setStatus("current")
_RegRelayDateHour_Type = Integer32
_RegRelayDateHour_Object = MibScalar
regRelayDateHour = _RegRelayDateHour_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1603),
    _RegRelayDateHour_Type()
)
regRelayDateHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regRelayDateHour.setStatus("current")
_RegRelayDateMinute_Type = Integer32
_RegRelayDateMinute_Object = MibScalar
regRelayDateMinute = _RegRelayDateMinute_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1604),
    _RegRelayDateMinute_Type()
)
regRelayDateMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regRelayDateMinute.setStatus("current")
_RegRelayDateSecond_Type = Integer32
_RegRelayDateSecond_Object = MibScalar
regRelayDateSecond = _RegRelayDateSecond_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1605),
    _RegRelayDateSecond_Type()
)
regRelayDateSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regRelayDateSecond.setStatus("current")
_RegRelayID_Type = Integer32
_RegRelayID_Object = MibScalar
regRelayID = _RegRelayID_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1606),
    _RegRelayID_Type()
)
regRelayID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regRelayID.setStatus("current")
_RegRelayPosition_Type = Integer32
_RegRelayPosition_Object = MibScalar
regRelayPosition = _RegRelayPosition_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1607),
    _RegRelayPosition_Type()
)
regRelayPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regRelayPosition.setStatus("current")
_RegAdvanceRelay_Type = Integer32
_RegAdvanceRelay_Object = MibScalar
regAdvanceRelay = _RegAdvanceRelay_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1608),
    _RegAdvanceRelay_Type()
)
regAdvanceRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regAdvanceRelay.setStatus("current")
_RegDecrementRelay_Type = Integer32
_RegDecrementRelay_Object = MibScalar
regDecrementRelay = _RegDecrementRelay_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 1609),
    _RegDecrementRelay_Type()
)
regDecrementRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regDecrementRelay.setStatus("current")
_RegLog1DateYear_Type = Integer32
_RegLog1DateYear_Object = MibScalar
regLog1DateYear = _RegLog1DateYear_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2000),
    _RegLog1DateYear_Type()
)
regLog1DateYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog1DateYear.setStatus("current")
_RegLog1DateMonth_Type = Integer32
_RegLog1DateMonth_Object = MibScalar
regLog1DateMonth = _RegLog1DateMonth_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2001),
    _RegLog1DateMonth_Type()
)
regLog1DateMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog1DateMonth.setStatus("current")
_RegLog1DateDay_Type = Integer32
_RegLog1DateDay_Object = MibScalar
regLog1DateDay = _RegLog1DateDay_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2002),
    _RegLog1DateDay_Type()
)
regLog1DateDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog1DateDay.setStatus("current")
_RegLog1DateHour_Type = Integer32
_RegLog1DateHour_Object = MibScalar
regLog1DateHour = _RegLog1DateHour_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2003),
    _RegLog1DateHour_Type()
)
regLog1DateHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog1DateHour.setStatus("current")
_RegLog1DateMinute_Type = Integer32
_RegLog1DateMinute_Object = MibScalar
regLog1DateMinute = _RegLog1DateMinute_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2004),
    _RegLog1DateMinute_Type()
)
regLog1DateMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog1DateMinute.setStatus("current")
_RegLog1DateSecond_Type = Integer32
_RegLog1DateSecond_Object = MibScalar
regLog1DateSecond = _RegLog1DateSecond_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2005),
    _RegLog1DateSecond_Type()
)
regLog1DateSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog1DateSecond.setStatus("current")
_RegLog1BatteryVoltage_Type = Integer32
_RegLog1BatteryVoltage_Object = MibScalar
regLog1BatteryVoltage = _RegLog1BatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2006),
    _RegLog1BatteryVoltage_Type()
)
regLog1BatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog1BatteryVoltage.setStatus("current")
_RegLog1Temperature_Type = Integer32
_RegLog1Temperature_Object = MibScalar
regLog1Temperature = _RegLog1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2007),
    _RegLog1Temperature_Type()
)
regLog1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog1Temperature.setStatus("current")
_RegLog1Analog132V_Type = Integer32
_RegLog1Analog132V_Object = MibScalar
regLog1Analog132V = _RegLog1Analog132V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2008),
    _RegLog1Analog132V_Type()
)
regLog1Analog132V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog1Analog132V.setStatus("current")
_RegLog1Analog15V_Type = Integer32
_RegLog1Analog15V_Object = MibScalar
regLog1Analog15V = _RegLog1Analog15V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2009),
    _RegLog1Analog15V_Type()
)
regLog1Analog15V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog1Analog15V.setStatus("current")
_RegLog1Analog1420mA_Type = Integer32
_RegLog1Analog1420mA_Object = MibScalar
regLog1Analog1420mA = _RegLog1Analog1420mA_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2010),
    _RegLog1Analog1420mA_Type()
)
regLog1Analog1420mA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog1Analog1420mA.setStatus("current")
_RegLog1Analog232V_Type = Integer32
_RegLog1Analog232V_Object = MibScalar
regLog1Analog232V = _RegLog1Analog232V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2011),
    _RegLog1Analog232V_Type()
)
regLog1Analog232V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog1Analog232V.setStatus("current")
_RegLog1Analog25V_Type = Integer32
_RegLog1Analog25V_Object = MibScalar
regLog1Analog25V = _RegLog1Analog25V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2012),
    _RegLog1Analog25V_Type()
)
regLog1Analog25V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog1Analog25V.setStatus("current")
_RegLog1Analog2420mA_Type = Integer32
_RegLog1Analog2420mA_Object = MibScalar
regLog1Analog2420mA = _RegLog1Analog2420mA_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2013),
    _RegLog1Analog2420mA_Type()
)
regLog1Analog2420mA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog1Analog2420mA.setStatus("current")
_RegLog1Digital1_Type = Integer32
_RegLog1Digital1_Object = MibScalar
regLog1Digital1 = _RegLog1Digital1_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2014),
    _RegLog1Digital1_Type()
)
regLog1Digital1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog1Digital1.setStatus("current")
_RegLog1Digital2_Type = Integer32
_RegLog1Digital2_Object = MibScalar
regLog1Digital2 = _RegLog1Digital2_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2015),
    _RegLog1Digital2_Type()
)
regLog1Digital2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog1Digital2.setStatus("current")
_RegLog2DateYear_Type = Integer32
_RegLog2DateYear_Object = MibScalar
regLog2DateYear = _RegLog2DateYear_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2016),
    _RegLog2DateYear_Type()
)
regLog2DateYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog2DateYear.setStatus("current")
_RegLog2DateMonth_Type = Integer32
_RegLog2DateMonth_Object = MibScalar
regLog2DateMonth = _RegLog2DateMonth_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2017),
    _RegLog2DateMonth_Type()
)
regLog2DateMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog2DateMonth.setStatus("current")
_RegLog2DateDay_Type = Integer32
_RegLog2DateDay_Object = MibScalar
regLog2DateDay = _RegLog2DateDay_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2018),
    _RegLog2DateDay_Type()
)
regLog2DateDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog2DateDay.setStatus("current")
_RegLog2DateHour_Type = Integer32
_RegLog2DateHour_Object = MibScalar
regLog2DateHour = _RegLog2DateHour_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2019),
    _RegLog2DateHour_Type()
)
regLog2DateHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog2DateHour.setStatus("current")
_RegLog2DateMinute_Type = Integer32
_RegLog2DateMinute_Object = MibScalar
regLog2DateMinute = _RegLog2DateMinute_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2020),
    _RegLog2DateMinute_Type()
)
regLog2DateMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog2DateMinute.setStatus("current")
_RegLog2DateSecond_Type = Integer32
_RegLog2DateSecond_Object = MibScalar
regLog2DateSecond = _RegLog2DateSecond_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2021),
    _RegLog2DateSecond_Type()
)
regLog2DateSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog2DateSecond.setStatus("current")
_RegLog2BatteryVoltage_Type = Integer32
_RegLog2BatteryVoltage_Object = MibScalar
regLog2BatteryVoltage = _RegLog2BatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2022),
    _RegLog2BatteryVoltage_Type()
)
regLog2BatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog2BatteryVoltage.setStatus("current")
_RegLog2Temperature_Type = Integer32
_RegLog2Temperature_Object = MibScalar
regLog2Temperature = _RegLog2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2023),
    _RegLog2Temperature_Type()
)
regLog2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog2Temperature.setStatus("current")
_RegLog2Analog132V_Type = Integer32
_RegLog2Analog132V_Object = MibScalar
regLog2Analog132V = _RegLog2Analog132V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2024),
    _RegLog2Analog132V_Type()
)
regLog2Analog132V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog2Analog132V.setStatus("current")
_RegLog2Analog15V_Type = Integer32
_RegLog2Analog15V_Object = MibScalar
regLog2Analog15V = _RegLog2Analog15V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2025),
    _RegLog2Analog15V_Type()
)
regLog2Analog15V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog2Analog15V.setStatus("current")
_RegLog2Analog1420mA_Type = Integer32
_RegLog2Analog1420mA_Object = MibScalar
regLog2Analog1420mA = _RegLog2Analog1420mA_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2026),
    _RegLog2Analog1420mA_Type()
)
regLog2Analog1420mA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog2Analog1420mA.setStatus("current")
_RegLog2Analog232V_Type = Integer32
_RegLog2Analog232V_Object = MibScalar
regLog2Analog232V = _RegLog2Analog232V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2027),
    _RegLog2Analog232V_Type()
)
regLog2Analog232V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog2Analog232V.setStatus("current")
_RegLog2Analog25V_Type = Integer32
_RegLog2Analog25V_Object = MibScalar
regLog2Analog25V = _RegLog2Analog25V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2028),
    _RegLog2Analog25V_Type()
)
regLog2Analog25V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog2Analog25V.setStatus("current")
_RegLog2Analog2420mA_Type = Integer32
_RegLog2Analog2420mA_Object = MibScalar
regLog2Analog2420mA = _RegLog2Analog2420mA_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2029),
    _RegLog2Analog2420mA_Type()
)
regLog2Analog2420mA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog2Analog2420mA.setStatus("current")
_RegLog2Digital1_Type = Integer32
_RegLog2Digital1_Object = MibScalar
regLog2Digital1 = _RegLog2Digital1_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2030),
    _RegLog2Digital1_Type()
)
regLog2Digital1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog2Digital1.setStatus("current")
_RegLog2Digital2_Type = Integer32
_RegLog2Digital2_Object = MibScalar
regLog2Digital2 = _RegLog2Digital2_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2031),
    _RegLog2Digital2_Type()
)
regLog2Digital2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog2Digital2.setStatus("current")
_RegLog3DateYear_Type = Integer32
_RegLog3DateYear_Object = MibScalar
regLog3DateYear = _RegLog3DateYear_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2032),
    _RegLog3DateYear_Type()
)
regLog3DateYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog3DateYear.setStatus("current")
_RegLog3DateMonth_Type = Integer32
_RegLog3DateMonth_Object = MibScalar
regLog3DateMonth = _RegLog3DateMonth_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2033),
    _RegLog3DateMonth_Type()
)
regLog3DateMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog3DateMonth.setStatus("current")
_RegLog3DateDay_Type = Integer32
_RegLog3DateDay_Object = MibScalar
regLog3DateDay = _RegLog3DateDay_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2034),
    _RegLog3DateDay_Type()
)
regLog3DateDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog3DateDay.setStatus("current")
_RegLog3DateHour_Type = Integer32
_RegLog3DateHour_Object = MibScalar
regLog3DateHour = _RegLog3DateHour_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2035),
    _RegLog3DateHour_Type()
)
regLog3DateHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog3DateHour.setStatus("current")
_RegLog3DateMinute_Type = Integer32
_RegLog3DateMinute_Object = MibScalar
regLog3DateMinute = _RegLog3DateMinute_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2036),
    _RegLog3DateMinute_Type()
)
regLog3DateMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog3DateMinute.setStatus("current")
_RegLog3DateSecond_Type = Integer32
_RegLog3DateSecond_Object = MibScalar
regLog3DateSecond = _RegLog3DateSecond_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2037),
    _RegLog3DateSecond_Type()
)
regLog3DateSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog3DateSecond.setStatus("current")
_RegLog3BatteryVoltage_Type = Integer32
_RegLog3BatteryVoltage_Object = MibScalar
regLog3BatteryVoltage = _RegLog3BatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2038),
    _RegLog3BatteryVoltage_Type()
)
regLog3BatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog3BatteryVoltage.setStatus("current")
_RegLog3Temperature_Type = Integer32
_RegLog3Temperature_Object = MibScalar
regLog3Temperature = _RegLog3Temperature_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2039),
    _RegLog3Temperature_Type()
)
regLog3Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog3Temperature.setStatus("current")
_RegLog3Analog132V_Type = Integer32
_RegLog3Analog132V_Object = MibScalar
regLog3Analog132V = _RegLog3Analog132V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2040),
    _RegLog3Analog132V_Type()
)
regLog3Analog132V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog3Analog132V.setStatus("current")
_RegLog3Analog15V_Type = Integer32
_RegLog3Analog15V_Object = MibScalar
regLog3Analog15V = _RegLog3Analog15V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2041),
    _RegLog3Analog15V_Type()
)
regLog3Analog15V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog3Analog15V.setStatus("current")
_RegLog3Analog1420mA_Type = Integer32
_RegLog3Analog1420mA_Object = MibScalar
regLog3Analog1420mA = _RegLog3Analog1420mA_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2042),
    _RegLog3Analog1420mA_Type()
)
regLog3Analog1420mA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog3Analog1420mA.setStatus("current")
_RegLog3Analog232V_Type = Integer32
_RegLog3Analog232V_Object = MibScalar
regLog3Analog232V = _RegLog3Analog232V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2043),
    _RegLog3Analog232V_Type()
)
regLog3Analog232V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog3Analog232V.setStatus("current")
_RegLog3Analog25V_Type = Integer32
_RegLog3Analog25V_Object = MibScalar
regLog3Analog25V = _RegLog3Analog25V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2044),
    _RegLog3Analog25V_Type()
)
regLog3Analog25V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog3Analog25V.setStatus("current")
_RegLog3Analog2420mA_Type = Integer32
_RegLog3Analog2420mA_Object = MibScalar
regLog3Analog2420mA = _RegLog3Analog2420mA_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2045),
    _RegLog3Analog2420mA_Type()
)
regLog3Analog2420mA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog3Analog2420mA.setStatus("current")
_RegLog3Digital1_Type = Integer32
_RegLog3Digital1_Object = MibScalar
regLog3Digital1 = _RegLog3Digital1_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2046),
    _RegLog3Digital1_Type()
)
regLog3Digital1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog3Digital1.setStatus("current")
_RegLog3Digital2_Type = Integer32
_RegLog3Digital2_Object = MibScalar
regLog3Digital2 = _RegLog3Digital2_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2047),
    _RegLog3Digital2_Type()
)
regLog3Digital2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog3Digital2.setStatus("current")
_RegLog4DateYear_Type = Integer32
_RegLog4DateYear_Object = MibScalar
regLog4DateYear = _RegLog4DateYear_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2048),
    _RegLog4DateYear_Type()
)
regLog4DateYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog4DateYear.setStatus("current")
_RegLog4DateMonth_Type = Integer32
_RegLog4DateMonth_Object = MibScalar
regLog4DateMonth = _RegLog4DateMonth_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2049),
    _RegLog4DateMonth_Type()
)
regLog4DateMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog4DateMonth.setStatus("current")
_RegLog4DateDay_Type = Integer32
_RegLog4DateDay_Object = MibScalar
regLog4DateDay = _RegLog4DateDay_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2050),
    _RegLog4DateDay_Type()
)
regLog4DateDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog4DateDay.setStatus("current")
_RegLog4DateHour_Type = Integer32
_RegLog4DateHour_Object = MibScalar
regLog4DateHour = _RegLog4DateHour_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2051),
    _RegLog4DateHour_Type()
)
regLog4DateHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog4DateHour.setStatus("current")
_RegLog4DateMinute_Type = Integer32
_RegLog4DateMinute_Object = MibScalar
regLog4DateMinute = _RegLog4DateMinute_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2052),
    _RegLog4DateMinute_Type()
)
regLog4DateMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog4DateMinute.setStatus("current")
_RegLog4DateSecond_Type = Integer32
_RegLog4DateSecond_Object = MibScalar
regLog4DateSecond = _RegLog4DateSecond_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2053),
    _RegLog4DateSecond_Type()
)
regLog4DateSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog4DateSecond.setStatus("current")
_RegLog4BatteryVoltage_Type = Integer32
_RegLog4BatteryVoltage_Object = MibScalar
regLog4BatteryVoltage = _RegLog4BatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2054),
    _RegLog4BatteryVoltage_Type()
)
regLog4BatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog4BatteryVoltage.setStatus("current")
_RegLog4Temperature_Type = Integer32
_RegLog4Temperature_Object = MibScalar
regLog4Temperature = _RegLog4Temperature_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2055),
    _RegLog4Temperature_Type()
)
regLog4Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog4Temperature.setStatus("current")
_RegLog4Analog132V_Type = Integer32
_RegLog4Analog132V_Object = MibScalar
regLog4Analog132V = _RegLog4Analog132V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2056),
    _RegLog4Analog132V_Type()
)
regLog4Analog132V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog4Analog132V.setStatus("current")
_RegLog4Analog15V_Type = Integer32
_RegLog4Analog15V_Object = MibScalar
regLog4Analog15V = _RegLog4Analog15V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2057),
    _RegLog4Analog15V_Type()
)
regLog4Analog15V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog4Analog15V.setStatus("current")
_RegLog4Analog1420mA_Type = Integer32
_RegLog4Analog1420mA_Object = MibScalar
regLog4Analog1420mA = _RegLog4Analog1420mA_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2058),
    _RegLog4Analog1420mA_Type()
)
regLog4Analog1420mA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog4Analog1420mA.setStatus("current")
_RegLog4Analog232V_Type = Integer32
_RegLog4Analog232V_Object = MibScalar
regLog4Analog232V = _RegLog4Analog232V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2059),
    _RegLog4Analog232V_Type()
)
regLog4Analog232V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog4Analog232V.setStatus("current")
_RegLog4Analog25V_Type = Integer32
_RegLog4Analog25V_Object = MibScalar
regLog4Analog25V = _RegLog4Analog25V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2060),
    _RegLog4Analog25V_Type()
)
regLog4Analog25V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog4Analog25V.setStatus("current")
_RegLog4Analog2420mA_Type = Integer32
_RegLog4Analog2420mA_Object = MibScalar
regLog4Analog2420mA = _RegLog4Analog2420mA_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2061),
    _RegLog4Analog2420mA_Type()
)
regLog4Analog2420mA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog4Analog2420mA.setStatus("current")
_RegLog4Digital1_Type = Integer32
_RegLog4Digital1_Object = MibScalar
regLog4Digital1 = _RegLog4Digital1_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2062),
    _RegLog4Digital1_Type()
)
regLog4Digital1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog4Digital1.setStatus("current")
_RegLog4Digital2_Type = Integer32
_RegLog4Digital2_Object = MibScalar
regLog4Digital2 = _RegLog4Digital2_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2063),
    _RegLog4Digital2_Type()
)
regLog4Digital2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog4Digital2.setStatus("current")
_RegLog5DateYear_Type = Integer32
_RegLog5DateYear_Object = MibScalar
regLog5DateYear = _RegLog5DateYear_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2064),
    _RegLog5DateYear_Type()
)
regLog5DateYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog5DateYear.setStatus("current")
_RegLog5DateMonth_Type = Integer32
_RegLog5DateMonth_Object = MibScalar
regLog5DateMonth = _RegLog5DateMonth_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2065),
    _RegLog5DateMonth_Type()
)
regLog5DateMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog5DateMonth.setStatus("current")
_RegLog5DateDay_Type = Integer32
_RegLog5DateDay_Object = MibScalar
regLog5DateDay = _RegLog5DateDay_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2066),
    _RegLog5DateDay_Type()
)
regLog5DateDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog5DateDay.setStatus("current")
_RegLog5DateHour_Type = Integer32
_RegLog5DateHour_Object = MibScalar
regLog5DateHour = _RegLog5DateHour_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2067),
    _RegLog5DateHour_Type()
)
regLog5DateHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog5DateHour.setStatus("current")
_RegLog5DateMinute_Type = Integer32
_RegLog5DateMinute_Object = MibScalar
regLog5DateMinute = _RegLog5DateMinute_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2068),
    _RegLog5DateMinute_Type()
)
regLog5DateMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog5DateMinute.setStatus("current")
_RegLog5DateSecond_Type = Integer32
_RegLog5DateSecond_Object = MibScalar
regLog5DateSecond = _RegLog5DateSecond_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2069),
    _RegLog5DateSecond_Type()
)
regLog5DateSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog5DateSecond.setStatus("current")
_RegLog5BatteryVoltage_Type = Integer32
_RegLog5BatteryVoltage_Object = MibScalar
regLog5BatteryVoltage = _RegLog5BatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2070),
    _RegLog5BatteryVoltage_Type()
)
regLog5BatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog5BatteryVoltage.setStatus("current")
_RegLog5Temperature_Type = Integer32
_RegLog5Temperature_Object = MibScalar
regLog5Temperature = _RegLog5Temperature_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2071),
    _RegLog5Temperature_Type()
)
regLog5Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog5Temperature.setStatus("current")
_RegLog5Analog132V_Type = Integer32
_RegLog5Analog132V_Object = MibScalar
regLog5Analog132V = _RegLog5Analog132V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2072),
    _RegLog5Analog132V_Type()
)
regLog5Analog132V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog5Analog132V.setStatus("current")
_RegLog5Analog15V_Type = Integer32
_RegLog5Analog15V_Object = MibScalar
regLog5Analog15V = _RegLog5Analog15V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2073),
    _RegLog5Analog15V_Type()
)
regLog5Analog15V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog5Analog15V.setStatus("current")
_RegLog5Analog1420mA_Type = Integer32
_RegLog5Analog1420mA_Object = MibScalar
regLog5Analog1420mA = _RegLog5Analog1420mA_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2074),
    _RegLog5Analog1420mA_Type()
)
regLog5Analog1420mA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog5Analog1420mA.setStatus("current")
_RegLog5Analog232V_Type = Integer32
_RegLog5Analog232V_Object = MibScalar
regLog5Analog232V = _RegLog5Analog232V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2075),
    _RegLog5Analog232V_Type()
)
regLog5Analog232V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog5Analog232V.setStatus("current")
_RegLog5Analog25V_Type = Integer32
_RegLog5Analog25V_Object = MibScalar
regLog5Analog25V = _RegLog5Analog25V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2076),
    _RegLog5Analog25V_Type()
)
regLog5Analog25V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog5Analog25V.setStatus("current")
_RegLog5Analog2420mA_Type = Integer32
_RegLog5Analog2420mA_Object = MibScalar
regLog5Analog2420mA = _RegLog5Analog2420mA_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2077),
    _RegLog5Analog2420mA_Type()
)
regLog5Analog2420mA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog5Analog2420mA.setStatus("current")
_RegLog5Digital1_Type = Integer32
_RegLog5Digital1_Object = MibScalar
regLog5Digital1 = _RegLog5Digital1_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2078),
    _RegLog5Digital1_Type()
)
regLog5Digital1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog5Digital1.setStatus("current")
_RegLog5Digital2_Type = Integer32
_RegLog5Digital2_Object = MibScalar
regLog5Digital2 = _RegLog5Digital2_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2079),
    _RegLog5Digital2_Type()
)
regLog5Digital2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog5Digital2.setStatus("current")
_RegLog6DateYear_Type = Integer32
_RegLog6DateYear_Object = MibScalar
regLog6DateYear = _RegLog6DateYear_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2080),
    _RegLog6DateYear_Type()
)
regLog6DateYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog6DateYear.setStatus("current")
_RegLog6DateMonth_Type = Integer32
_RegLog6DateMonth_Object = MibScalar
regLog6DateMonth = _RegLog6DateMonth_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2081),
    _RegLog6DateMonth_Type()
)
regLog6DateMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog6DateMonth.setStatus("current")
_RegLog6DateDay_Type = Integer32
_RegLog6DateDay_Object = MibScalar
regLog6DateDay = _RegLog6DateDay_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2082),
    _RegLog6DateDay_Type()
)
regLog6DateDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog6DateDay.setStatus("current")
_RegLog6DateHour_Type = Integer32
_RegLog6DateHour_Object = MibScalar
regLog6DateHour = _RegLog6DateHour_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2083),
    _RegLog6DateHour_Type()
)
regLog6DateHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog6DateHour.setStatus("current")
_RegLog6DateMinute_Type = Integer32
_RegLog6DateMinute_Object = MibScalar
regLog6DateMinute = _RegLog6DateMinute_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2084),
    _RegLog6DateMinute_Type()
)
regLog6DateMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog6DateMinute.setStatus("current")
_RegLog6DateSecond_Type = Integer32
_RegLog6DateSecond_Object = MibScalar
regLog6DateSecond = _RegLog6DateSecond_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2085),
    _RegLog6DateSecond_Type()
)
regLog6DateSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog6DateSecond.setStatus("current")
_RegLog6BatteryVoltage_Type = Integer32
_RegLog6BatteryVoltage_Object = MibScalar
regLog6BatteryVoltage = _RegLog6BatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2086),
    _RegLog6BatteryVoltage_Type()
)
regLog6BatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog6BatteryVoltage.setStatus("current")
_RegLog6Temperature_Type = Integer32
_RegLog6Temperature_Object = MibScalar
regLog6Temperature = _RegLog6Temperature_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2087),
    _RegLog6Temperature_Type()
)
regLog6Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog6Temperature.setStatus("current")
_RegLog6Analog132V_Type = Integer32
_RegLog6Analog132V_Object = MibScalar
regLog6Analog132V = _RegLog6Analog132V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2088),
    _RegLog6Analog132V_Type()
)
regLog6Analog132V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog6Analog132V.setStatus("current")
_RegLog6Analog15V_Type = Integer32
_RegLog6Analog15V_Object = MibScalar
regLog6Analog15V = _RegLog6Analog15V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2089),
    _RegLog6Analog15V_Type()
)
regLog6Analog15V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog6Analog15V.setStatus("current")
_RegLog6Analog1420mA_Type = Integer32
_RegLog6Analog1420mA_Object = MibScalar
regLog6Analog1420mA = _RegLog6Analog1420mA_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2090),
    _RegLog6Analog1420mA_Type()
)
regLog6Analog1420mA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog6Analog1420mA.setStatus("current")
_RegLog6Analog232V_Type = Integer32
_RegLog6Analog232V_Object = MibScalar
regLog6Analog232V = _RegLog6Analog232V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2091),
    _RegLog6Analog232V_Type()
)
regLog6Analog232V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog6Analog232V.setStatus("current")
_RegLog6Analog25V_Type = Integer32
_RegLog6Analog25V_Object = MibScalar
regLog6Analog25V = _RegLog6Analog25V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2092),
    _RegLog6Analog25V_Type()
)
regLog6Analog25V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog6Analog25V.setStatus("current")
_RegLog6Analog2420mA_Type = Integer32
_RegLog6Analog2420mA_Object = MibScalar
regLog6Analog2420mA = _RegLog6Analog2420mA_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2093),
    _RegLog6Analog2420mA_Type()
)
regLog6Analog2420mA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog6Analog2420mA.setStatus("current")
_RegLog6Digital1_Type = Integer32
_RegLog6Digital1_Object = MibScalar
regLog6Digital1 = _RegLog6Digital1_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2094),
    _RegLog6Digital1_Type()
)
regLog6Digital1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog6Digital1.setStatus("current")
_RegLog6Digital2_Type = Integer32
_RegLog6Digital2_Object = MibScalar
regLog6Digital2 = _RegLog6Digital2_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2095),
    _RegLog6Digital2_Type()
)
regLog6Digital2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog6Digital2.setStatus("current")
_RegLog7DateYear_Type = Integer32
_RegLog7DateYear_Object = MibScalar
regLog7DateYear = _RegLog7DateYear_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2096),
    _RegLog7DateYear_Type()
)
regLog7DateYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog7DateYear.setStatus("current")
_RegLog7DateMonth_Type = Integer32
_RegLog7DateMonth_Object = MibScalar
regLog7DateMonth = _RegLog7DateMonth_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2097),
    _RegLog7DateMonth_Type()
)
regLog7DateMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog7DateMonth.setStatus("current")
_RegLog7DateDay_Type = Integer32
_RegLog7DateDay_Object = MibScalar
regLog7DateDay = _RegLog7DateDay_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2098),
    _RegLog7DateDay_Type()
)
regLog7DateDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog7DateDay.setStatus("current")
_RegLog7DateHour_Type = Integer32
_RegLog7DateHour_Object = MibScalar
regLog7DateHour = _RegLog7DateHour_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2099),
    _RegLog7DateHour_Type()
)
regLog7DateHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog7DateHour.setStatus("current")
_RegLog7DateMinute_Type = Integer32
_RegLog7DateMinute_Object = MibScalar
regLog7DateMinute = _RegLog7DateMinute_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2100),
    _RegLog7DateMinute_Type()
)
regLog7DateMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog7DateMinute.setStatus("current")
_RegLog7DateSecond_Type = Integer32
_RegLog7DateSecond_Object = MibScalar
regLog7DateSecond = _RegLog7DateSecond_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2101),
    _RegLog7DateSecond_Type()
)
regLog7DateSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog7DateSecond.setStatus("current")
_RegLog7BatteryVoltage_Type = Integer32
_RegLog7BatteryVoltage_Object = MibScalar
regLog7BatteryVoltage = _RegLog7BatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2102),
    _RegLog7BatteryVoltage_Type()
)
regLog7BatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog7BatteryVoltage.setStatus("current")
_RegLog7Temperature_Type = Integer32
_RegLog7Temperature_Object = MibScalar
regLog7Temperature = _RegLog7Temperature_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2103),
    _RegLog7Temperature_Type()
)
regLog7Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog7Temperature.setStatus("current")
_RegLog7Analog132V_Type = Integer32
_RegLog7Analog132V_Object = MibScalar
regLog7Analog132V = _RegLog7Analog132V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2104),
    _RegLog7Analog132V_Type()
)
regLog7Analog132V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog7Analog132V.setStatus("current")
_RegLog7Analog15V_Type = Integer32
_RegLog7Analog15V_Object = MibScalar
regLog7Analog15V = _RegLog7Analog15V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2105),
    _RegLog7Analog15V_Type()
)
regLog7Analog15V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog7Analog15V.setStatus("current")
_RegLog7Analog1420mA_Type = Integer32
_RegLog7Analog1420mA_Object = MibScalar
regLog7Analog1420mA = _RegLog7Analog1420mA_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2106),
    _RegLog7Analog1420mA_Type()
)
regLog7Analog1420mA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog7Analog1420mA.setStatus("current")
_RegLog7Analog232V_Type = Integer32
_RegLog7Analog232V_Object = MibScalar
regLog7Analog232V = _RegLog7Analog232V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2107),
    _RegLog7Analog232V_Type()
)
regLog7Analog232V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog7Analog232V.setStatus("current")
_RegLog7Analog25V_Type = Integer32
_RegLog7Analog25V_Object = MibScalar
regLog7Analog25V = _RegLog7Analog25V_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2108),
    _RegLog7Analog25V_Type()
)
regLog7Analog25V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog7Analog25V.setStatus("current")
_RegLog7Analog2420mA_Type = Integer32
_RegLog7Analog2420mA_Object = MibScalar
regLog7Analog2420mA = _RegLog7Analog2420mA_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2109),
    _RegLog7Analog2420mA_Type()
)
regLog7Analog2420mA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog7Analog2420mA.setStatus("current")
_RegLog7Digital1_Type = Integer32
_RegLog7Digital1_Object = MibScalar
regLog7Digital1 = _RegLog7Digital1_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2110),
    _RegLog7Digital1_Type()
)
regLog7Digital1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog7Digital1.setStatus("current")
_RegLog7Digital2_Type = Integer32
_RegLog7Digital2_Object = MibScalar
regLog7Digital2 = _RegLog7Digital2_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2111),
    _RegLog7Digital2_Type()
)
regLog7Digital2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLog7Digital2.setStatus("current")
_RegAdvance7Logs_Type = Integer32
_RegAdvance7Logs_Object = MibScalar
regAdvance7Logs = _RegAdvance7Logs_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2112),
    _RegAdvance7Logs_Type()
)
regAdvance7Logs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regAdvance7Logs.setStatus("current")
_RegDecrement7Logs_Type = Integer32
_RegDecrement7Logs_Object = MibScalar
regDecrement7Logs = _RegDecrement7Logs_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 1, 2113),
    _RegDecrement7Logs_Type()
)
regDecrement7Logs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regDecrement7Logs.setStatus("current")
_TrapMap_ObjectIdentity = ObjectIdentity
trapMap = _TrapMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 2)
)
_TrapContents_ObjectIdentity = ObjectIdentity
trapContents = _TrapContents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 2, 1)
)
_ValueControllerID_Type = SnmpAdminString
_ValueControllerID_Object = MibTableColumn
valueControllerID = _ValueControllerID_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 2, 1, 1),
    _ValueControllerID_Type()
)
valueControllerID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    valueControllerID.setStatus("current")
_ValueTrapDesc_Type = SnmpAdminString
_ValueTrapDesc_Object = MibTableColumn
valueTrapDesc = _ValueTrapDesc_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 2, 1, 2),
    _ValueTrapDesc_Type()
)
valueTrapDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    valueTrapDesc.setStatus("current")
_ValueCurrentValue_Type = Integer32
_ValueCurrentValue_Object = MibTableColumn
valueCurrentValue = _ValueCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 2, 1, 3),
    _ValueCurrentValue_Type()
)
valueCurrentValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    valueCurrentValue.setStatus("current")
_ValueTrapItem_Object = MibTableRow
valueTrapItem = _ValueTrapItem_Object(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 2, 2)
)
if mibBuilder.loadTexts:
    valueTrapItem.setStatus("current")
_History_ObjectIdentity = ObjectIdentity
history = _History_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 3)
)

# Managed Objects groups


# Notification objects

trapInputLevel = NotificationType(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 2, 1)
)
trapInputLevel.setObjects(
      *(("Rogue-Engineering-Inc-Sentinel-Remote-IO-with-SNMP", "valueControllerID"),
        ("Rogue-Engineering-Inc-Sentinel-Remote-IO-with-SNMP", "valueTrapDesc"),
        ("Rogue-Engineering-Inc-Sentinel-Remote-IO-with-SNMP", "valueCurrentValue"))
)
if mibBuilder.loadTexts:
    trapInputLevel.setStatus(
        "current"
    )

trapSequenceInputLevel = NotificationType(
    (1, 3, 6, 1, 4, 1, 28459, 228, 2, 2, 2)
)
trapSequenceInputLevel.setObjects(
    ("Rogue-Engineering-Inc-Sentinel-Remote-IO-with-SNMP", "valueTrapItem")
)
if mibBuilder.loadTexts:
    trapSequenceInputLevel.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Rogue-Engineering-Inc-Sentinel-Remote-IO-with-SNMP",
    **{"rogueEngr": rogueEngr,
       "rogueRIOS": rogueRIOS,
       "rogueSentinelv2": rogueSentinelv2,
       "regMap": regMap,
       "regFirmwareVersion": regFirmwareVersion,
       "regFirmwareRevision": regFirmwareRevision,
       "regSerialBaud": regSerialBaud,
       "regSNMPManagerIP1": regSNMPManagerIP1,
       "regSNMPManagerIP2": regSNMPManagerIP2,
       "regSNMPManagerIP3": regSNMPManagerIP3,
       "regSNMPManagerIP4": regSNMPManagerIP4,
       "regMODBUSAddress": regMODBUSAddress,
       "regMACAddress1": regMACAddress1,
       "regMACAddress2": regMACAddress2,
       "regMACAddress3": regMACAddress3,
       "regMACAddress4": regMACAddress4,
       "regMACAddress5": regMACAddress5,
       "regMACAddress6": regMACAddress6,
       "regIPAddress1": regIPAddress1,
       "regIPAddress2": regIPAddress2,
       "regIPAddress3": regIPAddress3,
       "regIPAddress4": regIPAddress4,
       "regGatewayIPAddress1": regGatewayIPAddress1,
       "regGatewayIPAddress2": regGatewayIPAddress2,
       "regGatewayIPAddress3": regGatewayIPAddress3,
       "regGatewayIPAddress4": regGatewayIPAddress4,
       "regSubnetMask1": regSubnetMask1,
       "regSubnetMask2": regSubnetMask2,
       "regSubnetMask3": regSubnetMask3,
       "regSubnetMask4": regSubnetMask4,
       "regControllerName1": regControllerName1,
       "regControllerName2": regControllerName2,
       "regControllerName3": regControllerName3,
       "regControllerName4": regControllerName4,
       "regControllerName5": regControllerName5,
       "regControllerName6": regControllerName6,
       "regControllerName7": regControllerName7,
       "regControllerName8": regControllerName8,
       "regControllerName9": regControllerName9,
       "regControllerName10": regControllerName10,
       "regControllerName11": regControllerName11,
       "regControllerName12": regControllerName12,
       "regControllerName13": regControllerName13,
       "regControllerName14": regControllerName14,
       "regControllerName15": regControllerName15,
       "regControllerName16": regControllerName16,
       "regControllerName17": regControllerName17,
       "regControllerName18": regControllerName18,
       "regControllerName19": regControllerName19,
       "regControllerName20": regControllerName20,
       "regControllerName21": regControllerName21,
       "regControllerName22": regControllerName22,
       "regControllerName23": regControllerName23,
       "regControllerName24": regControllerName24,
       "regControllerName25": regControllerName25,
       "regControllerName26": regControllerName26,
       "regControllerName27": regControllerName27,
       "regControllerName28": regControllerName28,
       "regControllerName29": regControllerName29,
       "regControllerName30": regControllerName30,
       "regControllerName31": regControllerName31,
       "regControllerName32": regControllerName32,
       "regControllerName33": regControllerName33,
       "regControllerName34": regControllerName34,
       "regControllerName35": regControllerName35,
       "regControllerName36": regControllerName36,
       "regControllerName37": regControllerName37,
       "regControllerName38": regControllerName38,
       "regControllerName39": regControllerName39,
       "regControllerName40": regControllerName40,
       "regControllerName41": regControllerName41,
       "regControllerName42": regControllerName42,
       "regControllerName43": regControllerName43,
       "regControllerName44": regControllerName44,
       "regControllerName45": regControllerName45,
       "regControllerName46": regControllerName46,
       "regControllerName47": regControllerName47,
       "regControllerName48": regControllerName48,
       "regControllerName49": regControllerName49,
       "regControllerName50": regControllerName50,
       "regControllerName51": regControllerName51,
       "regControllerName52": regControllerName52,
       "regControllerName53": regControllerName53,
       "regControllerName54": regControllerName54,
       "regControllerName55": regControllerName55,
       "regClockYear": regClockYear,
       "regClockMonth": regClockMonth,
       "regClockDay": regClockDay,
       "regClockHour": regClockHour,
       "regClockMinute": regClockMinute,
       "regClockSecond": regClockSecond,
       "regDataLoggingInterval": regDataLoggingInterval,
       "regRelay1": regRelay1,
       "regRelay2": regRelay2,
       "regBatteryLowAlarmEnable": regBatteryLowAlarmEnable,
       "regBatteryLowTriggerVoltage": regBatteryLowTriggerVoltage,
       "regBatteryLowResetVoltage": regBatteryLowResetVoltage,
       "regBatteryHighAlarmEnable": regBatteryHighAlarmEnable,
       "regBatteryHighTriggerVoltage": regBatteryHighTriggerVoltage,
       "regBatteryHighResetVoltage": regBatteryHighResetVoltage,
       "regTemperatureLowAlarmEnable": regTemperatureLowAlarmEnable,
       "regTemperatureLowTrigger": regTemperatureLowTrigger,
       "regTemperatureLowReset": regTemperatureLowReset,
       "regTemperatureHighAlarmEnable": regTemperatureHighAlarmEnable,
       "regTemperatureHighTrigger": regTemperatureHighTrigger,
       "regTemperatureHighReset": regTemperatureHighReset,
       "regAnalog1LowAlarmEnable": regAnalog1LowAlarmEnable,
       "regAnalog1LowTriggerVoltage": regAnalog1LowTriggerVoltage,
       "regAnalog1LowResetVoltage": regAnalog1LowResetVoltage,
       "regAnalog1HighAlarmEnable": regAnalog1HighAlarmEnable,
       "regAnalog1HighTriggerVoltage": regAnalog1HighTriggerVoltage,
       "regAnalog1HighResetVoltage": regAnalog1HighResetVoltage,
       "regAnalog2LowAlarmEnable": regAnalog2LowAlarmEnable,
       "regAnalog2LowTriggerVoltage": regAnalog2LowTriggerVoltage,
       "regAnalog2LowResetVoltage": regAnalog2LowResetVoltage,
       "regAnalog2HighAlarmEnable": regAnalog2HighAlarmEnable,
       "regAnalog2HighTriggerVoltage": regAnalog2HighTriggerVoltage,
       "regAnalog2HighResetVoltage": regAnalog2HighResetVoltage,
       "regDigital1TriggeredAlarmEnable": regDigital1TriggeredAlarmEnable,
       "regDigital1TriggeredCycle": regDigital1TriggeredCycle,
       "regDigital1OpenAlarmEnable": regDigital1OpenAlarmEnable,
       "regDigital1OpenCycle": regDigital1OpenCycle,
       "regDigital2TriggeredAlarmEnable": regDigital2TriggeredAlarmEnable,
       "regDigital2TriggeredCycle": regDigital2TriggeredCycle,
       "regDigital2OpenAlarmEnable": regDigital2OpenAlarmEnable,
       "regDigital2OpenCycle": regDigital2OpenCycle,
       "regHardwareAlarmEnable": regHardwareAlarmEnable,
       "regHardwareAlarmCycle": regHardwareAlarmCycle,
       "regBatteryZeroPoint": regBatteryZeroPoint,
       "regBatteryMidPoint": regBatteryMidPoint,
       "regBatteryMidPointVoltage": regBatteryMidPointVoltage,
       "regAnalog1ZeroPoint32V": regAnalog1ZeroPoint32V,
       "regAnalog1MidPoint32V": regAnalog1MidPoint32V,
       "regAnalog1MidPointVoltage32V": regAnalog1MidPointVoltage32V,
       "regAnalog1ZeroPoint5V": regAnalog1ZeroPoint5V,
       "regAnalog1MidPoint5V": regAnalog1MidPoint5V,
       "regAnalog1MidPointVoltage5V": regAnalog1MidPointVoltage5V,
       "regAnalog1ZeroPoint420mA": regAnalog1ZeroPoint420mA,
       "regAnalog1MidPoint420mA": regAnalog1MidPoint420mA,
       "regAnalog1MidPointCurrent420mA": regAnalog1MidPointCurrent420mA,
       "regAnalog2ZeroPoint32V": regAnalog2ZeroPoint32V,
       "regAnalog2MidPoint32V": regAnalog2MidPoint32V,
       "regAnalog2MidPointVoltage32V": regAnalog2MidPointVoltage32V,
       "regAnalog2ZeroPoint5V": regAnalog2ZeroPoint5V,
       "regAnalog2MidPoint5V": regAnalog2MidPoint5V,
       "regAnalog2MidPointVoltage5V": regAnalog2MidPointVoltage5V,
       "regAnalog2ZeroPoint420mA": regAnalog2ZeroPoint420mA,
       "regAnalog2MidPoint420mA": regAnalog2MidPoint420mA,
       "regAnalog2MidPointCurrent420mA": regAnalog2MidPointCurrent420mA,
       "regForceBuffers": regForceBuffers,
       "regAlarmActionBatLowTrigger": regAlarmActionBatLowTrigger,
       "regAlarmActionBatLowReset": regAlarmActionBatLowReset,
       "regAlarmActionBatHighTrigger": regAlarmActionBatHighTrigger,
       "regAlarmActionBatHighReset": regAlarmActionBatHighReset,
       "regAlarmActionTempLowTrigger": regAlarmActionTempLowTrigger,
       "regAlarmActionTempLowReset": regAlarmActionTempLowReset,
       "regAlarmActionTempHighTrigger": regAlarmActionTempHighTrigger,
       "regAlarmActionTempHighReset": regAlarmActionTempHighReset,
       "regAlarmActionAIN1LowTrigger": regAlarmActionAIN1LowTrigger,
       "regAlarmActionAIN1LowReset": regAlarmActionAIN1LowReset,
       "regAlarmActionAIN1HighTrigger": regAlarmActionAIN1HighTrigger,
       "regAlarmActionAIN1HighReset": regAlarmActionAIN1HighReset,
       "regAlarmActionAIN2LowTrigger": regAlarmActionAIN2LowTrigger,
       "regAlarmActionAIN2LowReset": regAlarmActionAIN2LowReset,
       "regAlarmActionAIN2HighTrigger": regAlarmActionAIN2HighTrigger,
       "regAlarmActionAIN2HighReset": regAlarmActionAIN2HighReset,
       "regAlarmActionDIN1Trigger": regAlarmActionDIN1Trigger,
       "regAlarmActionDIN1Reset": regAlarmActionDIN1Reset,
       "regAlarmActionDIN2Trigger": regAlarmActionDIN2Trigger,
       "regAlarmActionDIN2Reset": regAlarmActionDIN2Reset,
       "regBatteryVoltage": regBatteryVoltage,
       "regTemperature": regTemperature,
       "regAnalog132V": regAnalog132V,
       "regAnalog15V": regAnalog15V,
       "regAnalog1420mA": regAnalog1420mA,
       "regAnalog232V": regAnalog232V,
       "regAnalog25V": regAnalog25V,
       "regAnalog2420mA": regAnalog2420mA,
       "regDigital1": regDigital1,
       "regDigital2": regDigital2,
       "regLogPointCountHigh": regLogPointCountHigh,
       "regLogPointCountLow": regLogPointCountLow,
       "regAlarmPointCount": regAlarmPointCount,
       "regRelayPointCount": regRelayPointCount,
       "regCurrentLogPointHigh": regCurrentLogPointHigh,
       "regCurrentLogPointLow": regCurrentLogPointLow,
       "regCurrentAlarmPoint": regCurrentAlarmPoint,
       "regCurrentRelayPoint": regCurrentRelayPoint,
       "regEraseLogData": regEraseLogData,
       "regEraseAlarmData": regEraseAlarmData,
       "regEraseRelayData": regEraseRelayData,
       "regLogDateYear": regLogDateYear,
       "regLogDateMonth": regLogDateMonth,
       "regLogDateDay": regLogDateDay,
       "regLogDateHour": regLogDateHour,
       "regLogDateMinute": regLogDateMinute,
       "regLogDateSecond": regLogDateSecond,
       "regLogBatteryVoltage": regLogBatteryVoltage,
       "regLogTemperature": regLogTemperature,
       "regLogAnalog132V": regLogAnalog132V,
       "regLogAnalog15V": regLogAnalog15V,
       "regLogAnalog1420mA": regLogAnalog1420mA,
       "regLogAnalog232V": regLogAnalog232V,
       "regLogAnalog25V": regLogAnalog25V,
       "regLogAnalog2420mA": regLogAnalog2420mA,
       "regLogDigital1": regLogDigital1,
       "regLogDigital2": regLogDigital2,
       "regAdvanceLog": regAdvanceLog,
       "regDecrementLog": regDecrementLog,
       "regAlarmDateYear": regAlarmDateYear,
       "regAlarmDateMonth": regAlarmDateMonth,
       "regAlarmDateDay": regAlarmDateDay,
       "regAlarmDateHour": regAlarmDateHour,
       "regAlarmDateMinute": regAlarmDateMinute,
       "regAlarmDateSecond": regAlarmDateSecond,
       "regAlarmID": regAlarmID,
       "regAdvanceAlarm": regAdvanceAlarm,
       "regDecrementAlarm": regDecrementAlarm,
       "regRelayDateYear": regRelayDateYear,
       "regRelayDateMonth": regRelayDateMonth,
       "regRelayDateDay": regRelayDateDay,
       "regRelayDateHour": regRelayDateHour,
       "regRelayDateMinute": regRelayDateMinute,
       "regRelayDateSecond": regRelayDateSecond,
       "regRelayID": regRelayID,
       "regRelayPosition": regRelayPosition,
       "regAdvanceRelay": regAdvanceRelay,
       "regDecrementRelay": regDecrementRelay,
       "regLog1DateYear": regLog1DateYear,
       "regLog1DateMonth": regLog1DateMonth,
       "regLog1DateDay": regLog1DateDay,
       "regLog1DateHour": regLog1DateHour,
       "regLog1DateMinute": regLog1DateMinute,
       "regLog1DateSecond": regLog1DateSecond,
       "regLog1BatteryVoltage": regLog1BatteryVoltage,
       "regLog1Temperature": regLog1Temperature,
       "regLog1Analog132V": regLog1Analog132V,
       "regLog1Analog15V": regLog1Analog15V,
       "regLog1Analog1420mA": regLog1Analog1420mA,
       "regLog1Analog232V": regLog1Analog232V,
       "regLog1Analog25V": regLog1Analog25V,
       "regLog1Analog2420mA": regLog1Analog2420mA,
       "regLog1Digital1": regLog1Digital1,
       "regLog1Digital2": regLog1Digital2,
       "regLog2DateYear": regLog2DateYear,
       "regLog2DateMonth": regLog2DateMonth,
       "regLog2DateDay": regLog2DateDay,
       "regLog2DateHour": regLog2DateHour,
       "regLog2DateMinute": regLog2DateMinute,
       "regLog2DateSecond": regLog2DateSecond,
       "regLog2BatteryVoltage": regLog2BatteryVoltage,
       "regLog2Temperature": regLog2Temperature,
       "regLog2Analog132V": regLog2Analog132V,
       "regLog2Analog15V": regLog2Analog15V,
       "regLog2Analog1420mA": regLog2Analog1420mA,
       "regLog2Analog232V": regLog2Analog232V,
       "regLog2Analog25V": regLog2Analog25V,
       "regLog2Analog2420mA": regLog2Analog2420mA,
       "regLog2Digital1": regLog2Digital1,
       "regLog2Digital2": regLog2Digital2,
       "regLog3DateYear": regLog3DateYear,
       "regLog3DateMonth": regLog3DateMonth,
       "regLog3DateDay": regLog3DateDay,
       "regLog3DateHour": regLog3DateHour,
       "regLog3DateMinute": regLog3DateMinute,
       "regLog3DateSecond": regLog3DateSecond,
       "regLog3BatteryVoltage": regLog3BatteryVoltage,
       "regLog3Temperature": regLog3Temperature,
       "regLog3Analog132V": regLog3Analog132V,
       "regLog3Analog15V": regLog3Analog15V,
       "regLog3Analog1420mA": regLog3Analog1420mA,
       "regLog3Analog232V": regLog3Analog232V,
       "regLog3Analog25V": regLog3Analog25V,
       "regLog3Analog2420mA": regLog3Analog2420mA,
       "regLog3Digital1": regLog3Digital1,
       "regLog3Digital2": regLog3Digital2,
       "regLog4DateYear": regLog4DateYear,
       "regLog4DateMonth": regLog4DateMonth,
       "regLog4DateDay": regLog4DateDay,
       "regLog4DateHour": regLog4DateHour,
       "regLog4DateMinute": regLog4DateMinute,
       "regLog4DateSecond": regLog4DateSecond,
       "regLog4BatteryVoltage": regLog4BatteryVoltage,
       "regLog4Temperature": regLog4Temperature,
       "regLog4Analog132V": regLog4Analog132V,
       "regLog4Analog15V": regLog4Analog15V,
       "regLog4Analog1420mA": regLog4Analog1420mA,
       "regLog4Analog232V": regLog4Analog232V,
       "regLog4Analog25V": regLog4Analog25V,
       "regLog4Analog2420mA": regLog4Analog2420mA,
       "regLog4Digital1": regLog4Digital1,
       "regLog4Digital2": regLog4Digital2,
       "regLog5DateYear": regLog5DateYear,
       "regLog5DateMonth": regLog5DateMonth,
       "regLog5DateDay": regLog5DateDay,
       "regLog5DateHour": regLog5DateHour,
       "regLog5DateMinute": regLog5DateMinute,
       "regLog5DateSecond": regLog5DateSecond,
       "regLog5BatteryVoltage": regLog5BatteryVoltage,
       "regLog5Temperature": regLog5Temperature,
       "regLog5Analog132V": regLog5Analog132V,
       "regLog5Analog15V": regLog5Analog15V,
       "regLog5Analog1420mA": regLog5Analog1420mA,
       "regLog5Analog232V": regLog5Analog232V,
       "regLog5Analog25V": regLog5Analog25V,
       "regLog5Analog2420mA": regLog5Analog2420mA,
       "regLog5Digital1": regLog5Digital1,
       "regLog5Digital2": regLog5Digital2,
       "regLog6DateYear": regLog6DateYear,
       "regLog6DateMonth": regLog6DateMonth,
       "regLog6DateDay": regLog6DateDay,
       "regLog6DateHour": regLog6DateHour,
       "regLog6DateMinute": regLog6DateMinute,
       "regLog6DateSecond": regLog6DateSecond,
       "regLog6BatteryVoltage": regLog6BatteryVoltage,
       "regLog6Temperature": regLog6Temperature,
       "regLog6Analog132V": regLog6Analog132V,
       "regLog6Analog15V": regLog6Analog15V,
       "regLog6Analog1420mA": regLog6Analog1420mA,
       "regLog6Analog232V": regLog6Analog232V,
       "regLog6Analog25V": regLog6Analog25V,
       "regLog6Analog2420mA": regLog6Analog2420mA,
       "regLog6Digital1": regLog6Digital1,
       "regLog6Digital2": regLog6Digital2,
       "regLog7DateYear": regLog7DateYear,
       "regLog7DateMonth": regLog7DateMonth,
       "regLog7DateDay": regLog7DateDay,
       "regLog7DateHour": regLog7DateHour,
       "regLog7DateMinute": regLog7DateMinute,
       "regLog7DateSecond": regLog7DateSecond,
       "regLog7BatteryVoltage": regLog7BatteryVoltage,
       "regLog7Temperature": regLog7Temperature,
       "regLog7Analog132V": regLog7Analog132V,
       "regLog7Analog15V": regLog7Analog15V,
       "regLog7Analog1420mA": regLog7Analog1420mA,
       "regLog7Analog232V": regLog7Analog232V,
       "regLog7Analog25V": regLog7Analog25V,
       "regLog7Analog2420mA": regLog7Analog2420mA,
       "regLog7Digital1": regLog7Digital1,
       "regLog7Digital2": regLog7Digital2,
       "regAdvance7Logs": regAdvance7Logs,
       "regDecrement7Logs": regDecrement7Logs,
       "trapMap": trapMap,
       "trapContents": trapContents,
       "trapInputLevel": trapInputLevel,
       "valueControllerID": valueControllerID,
       "valueTrapDesc": valueTrapDesc,
       "valueCurrentValue": valueCurrentValue,
       "trapSequenceInputLevel": trapSequenceInputLevel,
       "valueTrapItem": valueTrapItem,
       "history": history}
)
