# SNMP MIB module (DOCS-RPHY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-RPHY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:03 2024
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

(clabProjDocsis,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjDocsis")

(DocsX509ASN1DEREncodedCertificate,) = mibBuilder.importSymbols(
    "DOCS-IETF-BPI2-MIB",
    "DocsX509ASN1DEREncodedCertificate")

(IfDirection,) = mibBuilder.importSymbols(
    "DOCS-IF3-MIB",
    "IfDirection")

(PhysicalIndex,
 PhysicalIndexOrZero) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "PhysicalIndexOrZero")

(EntitySensorDataScale,
 EntitySensorDataType,
 EntitySensorPrecision,
 EntitySensorStatus,
 EntitySensorValue) = mibBuilder.importSymbols(
    "ENTITY-SENSOR-MIB",
    "EntitySensorDataScale",
    "EntitySensorDataType",
    "EntitySensorPrecision",
    "EntitySensorStatus",
    "EntitySensorValue")

(IANAPhysicalClass,) = mibBuilder.importSymbols(
    "IANA-ENTITY-MIB",
    "IANAPhysicalClass")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber,
 InetVersion) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber",
    "InetVersion")

(IpAddressOriginTC,
 IpAddressStatusTC,
 Ipv6AddressIfIdentifierTC) = mibBuilder.importSymbols(
    "IP-MIB",
    "IpAddressOriginTC",
    "IpAddressStatusTC",
    "Ipv6AddressIfIdentifierTC")

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
    "iso")

(AutonomousType,
 DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(UUIDorZero,) = mibBuilder.importSymbols(
    "UUID-TC-MIB",
    "UUIDorZero")


# MODULE-IDENTITY

docsRphyMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30)
)
docsRphyMib.setRevisions(
        ("2017-04-13 00:00",
         "2016-12-15 00:00",
         "2016-09-29 00:00",
         "2016-04-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RphyChannelType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("dsOfdm", 2),
          ("dsScQam", 1),
          ("ndf", 3),
          ("ndr", 8),
          ("other", 0),
          ("reserved", 7),
          ("scte551Fwd", 4),
          ("scte551Ret", 9),
          ("usAtdma", 5),
          ("usOfdma", 6))
    )



class RphyEventSeverityType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("information", 6),
          ("notice", 5),
          ("warning", 4))
    )



# MIB Managed Objects in the order of their OIDs

_DocsRphyNotifications_ObjectIdentity = ObjectIdentity
docsRphyNotifications = _DocsRphyNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 0)
)
_DocsRphyObjects_ObjectIdentity = ObjectIdentity
docsRphyObjects = _DocsRphyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1)
)
_DocsRphyRpdDevMibObjects_ObjectIdentity = ObjectIdentity
docsRphyRpdDevMibObjects = _DocsRphyRpdDevMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1)
)
_DocsRphyRpdDevInfoTable_Object = MibTable
docsRphyRpdDevInfoTable = _DocsRphyRpdDevInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 1)
)
if mibBuilder.loadTexts:
    docsRphyRpdDevInfoTable.setStatus("current")
_DocsRphyRpdDevInfoEntry_Object = MibTableRow
docsRphyRpdDevInfoEntry = _DocsRphyRpdDevInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 1, 1)
)
docsRphyRpdDevInfoEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
)
if mibBuilder.loadTexts:
    docsRphyRpdDevInfoEntry.setStatus("current")
_DocsRphyRpdDevInfoUniqueId_Type = MacAddress
_DocsRphyRpdDevInfoUniqueId_Object = MibTableColumn
docsRphyRpdDevInfoUniqueId = _DocsRphyRpdDevInfoUniqueId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 1, 1, 1),
    _DocsRphyRpdDevInfoUniqueId_Type()
)
docsRphyRpdDevInfoUniqueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevInfoUniqueId.setStatus("current")
_DocsRphyRpdDevInfoSysUpTime_Type = TimeStamp
_DocsRphyRpdDevInfoSysUpTime_Object = MibTableColumn
docsRphyRpdDevInfoSysUpTime = _DocsRphyRpdDevInfoSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 1, 1, 2),
    _DocsRphyRpdDevInfoSysUpTime_Type()
)
docsRphyRpdDevInfoSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevInfoSysUpTime.setStatus("current")
_DocsRphyRpdDevInfoNumCrashFilesAvail_Type = Unsigned32
_DocsRphyRpdDevInfoNumCrashFilesAvail_Object = MibTableColumn
docsRphyRpdDevInfoNumCrashFilesAvail = _DocsRphyRpdDevInfoNumCrashFilesAvail_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 1, 1, 3),
    _DocsRphyRpdDevInfoNumCrashFilesAvail_Type()
)
docsRphyRpdDevInfoNumCrashFilesAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevInfoNumCrashFilesAvail.setStatus("current")
_DocsRphyRpdDevIdentificationTable_Object = MibTable
docsRphyRpdDevIdentificationTable = _DocsRphyRpdDevIdentificationTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 2)
)
if mibBuilder.loadTexts:
    docsRphyRpdDevIdentificationTable.setStatus("current")
_DocsRphyRpdDevIdentificationEntry_Object = MibTableRow
docsRphyRpdDevIdentificationEntry = _DocsRphyRpdDevIdentificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 2, 1)
)
docsRphyRpdDevIdentificationEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
)
if mibBuilder.loadTexts:
    docsRphyRpdDevIdentificationEntry.setStatus("current")
_DocsRphyRpdDevIdVendorName_Type = SnmpAdminString
_DocsRphyRpdDevIdVendorName_Object = MibTableColumn
docsRphyRpdDevIdVendorName = _DocsRphyRpdDevIdVendorName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 2, 1, 1),
    _DocsRphyRpdDevIdVendorName_Type()
)
docsRphyRpdDevIdVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevIdVendorName.setStatus("current")


class _DocsRphyRpdDevIdVendorId_Type(Unsigned32):
    """Custom type docsRphyRpdDevIdVendorId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdDevIdVendorId_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevIdVendorId_Object = MibTableColumn
docsRphyRpdDevIdVendorId = _DocsRphyRpdDevIdVendorId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 2, 1, 2),
    _DocsRphyRpdDevIdVendorId_Type()
)
docsRphyRpdDevIdVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevIdVendorId.setStatus("current")
_DocsRphyRpdDevIdModelNum_Type = SnmpAdminString
_DocsRphyRpdDevIdModelNum_Object = MibTableColumn
docsRphyRpdDevIdModelNum = _DocsRphyRpdDevIdModelNum_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 2, 1, 3),
    _DocsRphyRpdDevIdModelNum_Type()
)
docsRphyRpdDevIdModelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevIdModelNum.setStatus("current")


class _DocsRphyRpdDevIdSerialNum_Type(SnmpAdminString):
    """Custom type docsRphyRpdDevIdSerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DocsRphyRpdDevIdSerialNum_Type.__name__ = "SnmpAdminString"
_DocsRphyRpdDevIdSerialNum_Object = MibTableColumn
docsRphyRpdDevIdSerialNum = _DocsRphyRpdDevIdSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 2, 1, 4),
    _DocsRphyRpdDevIdSerialNum_Type()
)
docsRphyRpdDevIdSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevIdSerialNum.setStatus("current")
_DocsRphyRpdDevIdDeviceAlias_Type = SnmpAdminString
_DocsRphyRpdDevIdDeviceAlias_Object = MibTableColumn
docsRphyRpdDevIdDeviceAlias = _DocsRphyRpdDevIdDeviceAlias_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 2, 1, 5),
    _DocsRphyRpdDevIdDeviceAlias_Type()
)
docsRphyRpdDevIdDeviceAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevIdDeviceAlias.setStatus("current")
_DocsRphyRpdDevIdDeviceDescr_Type = SnmpAdminString
_DocsRphyRpdDevIdDeviceDescr_Object = MibTableColumn
docsRphyRpdDevIdDeviceDescr = _DocsRphyRpdDevIdDeviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 2, 1, 6),
    _DocsRphyRpdDevIdDeviceDescr_Type()
)
docsRphyRpdDevIdDeviceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevIdDeviceDescr.setStatus("current")
_DocsRphyRpdDevIdHwRev_Type = SnmpAdminString
_DocsRphyRpdDevIdHwRev_Object = MibTableColumn
docsRphyRpdDevIdHwRev = _DocsRphyRpdDevIdHwRev_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 2, 1, 7),
    _DocsRphyRpdDevIdHwRev_Type()
)
docsRphyRpdDevIdHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevIdHwRev.setStatus("current")
_DocsRphyRpdDevIdCurrSwVer_Type = SnmpAdminString
_DocsRphyRpdDevIdCurrSwVer_Object = MibTableColumn
docsRphyRpdDevIdCurrSwVer = _DocsRphyRpdDevIdCurrSwVer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 2, 1, 8),
    _DocsRphyRpdDevIdCurrSwVer_Type()
)
docsRphyRpdDevIdCurrSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevIdCurrSwVer.setStatus("current")
_DocsRphyRpdDevIdBootRomVer_Type = SnmpAdminString
_DocsRphyRpdDevIdBootRomVer_Object = MibTableColumn
docsRphyRpdDevIdBootRomVer = _DocsRphyRpdDevIdBootRomVer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 2, 1, 9),
    _DocsRphyRpdDevIdBootRomVer_Type()
)
docsRphyRpdDevIdBootRomVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevIdBootRomVer.setStatus("current")


class _DocsRphyRpdDevIdUsBurstRcvrVendorId_Type(Unsigned32):
    """Custom type docsRphyRpdDevIdUsBurstRcvrVendorId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdDevIdUsBurstRcvrVendorId_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevIdUsBurstRcvrVendorId_Object = MibTableColumn
docsRphyRpdDevIdUsBurstRcvrVendorId = _DocsRphyRpdDevIdUsBurstRcvrVendorId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 2, 1, 10),
    _DocsRphyRpdDevIdUsBurstRcvrVendorId_Type()
)
docsRphyRpdDevIdUsBurstRcvrVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevIdUsBurstRcvrVendorId.setStatus("current")


class _DocsRphyRpdDevIdUsBurstRcvrModelNum_Type(SnmpAdminString):
    """Custom type docsRphyRpdDevIdUsBurstRcvrModelNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 16),
    )


_DocsRphyRpdDevIdUsBurstRcvrModelNum_Type.__name__ = "SnmpAdminString"
_DocsRphyRpdDevIdUsBurstRcvrModelNum_Object = MibTableColumn
docsRphyRpdDevIdUsBurstRcvrModelNum = _DocsRphyRpdDevIdUsBurstRcvrModelNum_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 2, 1, 11),
    _DocsRphyRpdDevIdUsBurstRcvrModelNum_Type()
)
docsRphyRpdDevIdUsBurstRcvrModelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevIdUsBurstRcvrModelNum.setStatus("current")


class _DocsRphyRpdDevIdUsBurstRcvrDrivVer_Type(SnmpAdminString):
    """Custom type docsRphyRpdDevIdUsBurstRcvrDrivVer based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 16),
    )


_DocsRphyRpdDevIdUsBurstRcvrDrivVer_Type.__name__ = "SnmpAdminString"
_DocsRphyRpdDevIdUsBurstRcvrDrivVer_Object = MibTableColumn
docsRphyRpdDevIdUsBurstRcvrDrivVer = _DocsRphyRpdDevIdUsBurstRcvrDrivVer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 2, 1, 12),
    _DocsRphyRpdDevIdUsBurstRcvrDrivVer_Type()
)
docsRphyRpdDevIdUsBurstRcvrDrivVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevIdUsBurstRcvrDrivVer.setStatus("current")


class _DocsRphyRpdDevIdUsBurstRcvrSerialNum_Type(SnmpAdminString):
    """Custom type docsRphyRpdDevIdUsBurstRcvrSerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 16),
    )


_DocsRphyRpdDevIdUsBurstRcvrSerialNum_Type.__name__ = "SnmpAdminString"
_DocsRphyRpdDevIdUsBurstRcvrSerialNum_Object = MibTableColumn
docsRphyRpdDevIdUsBurstRcvrSerialNum = _DocsRphyRpdDevIdUsBurstRcvrSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 2, 1, 13),
    _DocsRphyRpdDevIdUsBurstRcvrSerialNum_Type()
)
docsRphyRpdDevIdUsBurstRcvrSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevIdUsBurstRcvrSerialNum.setStatus("current")


class _DocsRphyRpdDevIdRcpProtocolVer_Type(SnmpAdminString):
    """Custom type docsRphyRpdDevIdRcpProtocolVer based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 32),
    )


_DocsRphyRpdDevIdRcpProtocolVer_Type.__name__ = "SnmpAdminString"
_DocsRphyRpdDevIdRcpProtocolVer_Object = MibTableColumn
docsRphyRpdDevIdRcpProtocolVer = _DocsRphyRpdDevIdRcpProtocolVer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 2, 1, 14),
    _DocsRphyRpdDevIdRcpProtocolVer_Type()
)
docsRphyRpdDevIdRcpProtocolVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevIdRcpProtocolVer.setStatus("current")


class _DocsRphyRpdDevIdRcpSchemaVer_Type(SnmpAdminString):
    """Custom type docsRphyRpdDevIdRcpSchemaVer based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 32),
    )


_DocsRphyRpdDevIdRcpSchemaVer_Type.__name__ = "SnmpAdminString"
_DocsRphyRpdDevIdRcpSchemaVer_Object = MibTableColumn
docsRphyRpdDevIdRcpSchemaVer = _DocsRphyRpdDevIdRcpSchemaVer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 2, 1, 15),
    _DocsRphyRpdDevIdRcpSchemaVer_Type()
)
docsRphyRpdDevIdRcpSchemaVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevIdRcpSchemaVer.setStatus("current")
_DocsRphyRpdDevLocationTable_Object = MibTable
docsRphyRpdDevLocationTable = _DocsRphyRpdDevLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 3)
)
if mibBuilder.loadTexts:
    docsRphyRpdDevLocationTable.setStatus("current")
_DocsRphyRpdDevLocationEntry_Object = MibTableRow
docsRphyRpdDevLocationEntry = _DocsRphyRpdDevLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 3, 1)
)
docsRphyRpdDevLocationEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
)
if mibBuilder.loadTexts:
    docsRphyRpdDevLocationEntry.setStatus("current")


class _DocsRphyRpdDevLocationDescr_Type(SnmpAdminString):
    """Custom type docsRphyRpdDevLocationDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DocsRphyRpdDevLocationDescr_Type.__name__ = "SnmpAdminString"
_DocsRphyRpdDevLocationDescr_Object = MibTableColumn
docsRphyRpdDevLocationDescr = _DocsRphyRpdDevLocationDescr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 3, 1, 1),
    _DocsRphyRpdDevLocationDescr_Type()
)
docsRphyRpdDevLocationDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevLocationDescr.setStatus("current")


class _DocsRphyRpdDevLocationLatitude_Type(SnmpAdminString):
    """Custom type docsRphyRpdDevLocationLatitude based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_DocsRphyRpdDevLocationLatitude_Type.__name__ = "SnmpAdminString"
_DocsRphyRpdDevLocationLatitude_Object = MibTableColumn
docsRphyRpdDevLocationLatitude = _DocsRphyRpdDevLocationLatitude_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 3, 1, 2),
    _DocsRphyRpdDevLocationLatitude_Type()
)
docsRphyRpdDevLocationLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevLocationLatitude.setStatus("current")


class _DocsRphyRpdDevLocationLongitude_Type(SnmpAdminString):
    """Custom type docsRphyRpdDevLocationLongitude based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_DocsRphyRpdDevLocationLongitude_Type.__name__ = "SnmpAdminString"
_DocsRphyRpdDevLocationLongitude_Object = MibTableColumn
docsRphyRpdDevLocationLongitude = _DocsRphyRpdDevLocationLongitude_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 3, 1, 3),
    _DocsRphyRpdDevLocationLongitude_Type()
)
docsRphyRpdDevLocationLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevLocationLongitude.setStatus("current")
_DocsRphyRpdDevCoresConnectedTable_Object = MibTable
docsRphyRpdDevCoresConnectedTable = _DocsRphyRpdDevCoresConnectedTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 4)
)
if mibBuilder.loadTexts:
    docsRphyRpdDevCoresConnectedTable.setStatus("current")
_DocsRphyRpdDevCoresConnectedEntry_Object = MibTableRow
docsRphyRpdDevCoresConnectedEntry = _DocsRphyRpdDevCoresConnectedEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 4, 1)
)
docsRphyRpdDevCoresConnectedEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevCoresConnectedCoreId"),
)
if mibBuilder.loadTexts:
    docsRphyRpdDevCoresConnectedEntry.setStatus("current")
_DocsRphyRpdDevCoresConnectedCoreId_Type = MacAddress
_DocsRphyRpdDevCoresConnectedCoreId_Object = MibTableColumn
docsRphyRpdDevCoresConnectedCoreId = _DocsRphyRpdDevCoresConnectedCoreId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 4, 1, 1),
    _DocsRphyRpdDevCoresConnectedCoreId_Type()
)
docsRphyRpdDevCoresConnectedCoreId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevCoresConnectedCoreId.setStatus("current")
_DocsRphyRpdDevCoresConnectedAddressType_Type = InetAddressType
_DocsRphyRpdDevCoresConnectedAddressType_Object = MibTableColumn
docsRphyRpdDevCoresConnectedAddressType = _DocsRphyRpdDevCoresConnectedAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 4, 1, 2),
    _DocsRphyRpdDevCoresConnectedAddressType_Type()
)
docsRphyRpdDevCoresConnectedAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCoresConnectedAddressType.setStatus("current")
_DocsRphyRpdDevCoresConnectedAddress_Type = InetAddress
_DocsRphyRpdDevCoresConnectedAddress_Object = MibTableColumn
docsRphyRpdDevCoresConnectedAddress = _DocsRphyRpdDevCoresConnectedAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 4, 1, 3),
    _DocsRphyRpdDevCoresConnectedAddress_Type()
)
docsRphyRpdDevCoresConnectedAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCoresConnectedAddress.setStatus("current")
_DocsRphyRpdDevCoresConnectedIsPrincipal_Type = TruthValue
_DocsRphyRpdDevCoresConnectedIsPrincipal_Object = MibTableColumn
docsRphyRpdDevCoresConnectedIsPrincipal = _DocsRphyRpdDevCoresConnectedIsPrincipal_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 4, 1, 4),
    _DocsRphyRpdDevCoresConnectedIsPrincipal_Type()
)
docsRphyRpdDevCoresConnectedIsPrincipal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCoresConnectedIsPrincipal.setStatus("current")
_DocsRphyRpdDevCoresConnectedName_Type = SnmpAdminString
_DocsRphyRpdDevCoresConnectedName_Object = MibTableColumn
docsRphyRpdDevCoresConnectedName = _DocsRphyRpdDevCoresConnectedName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 4, 1, 5),
    _DocsRphyRpdDevCoresConnectedName_Type()
)
docsRphyRpdDevCoresConnectedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCoresConnectedName.setStatus("current")


class _DocsRphyRpdDevCoresConnectedVendorId_Type(Unsigned32):
    """Custom type docsRphyRpdDevCoresConnectedVendorId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdDevCoresConnectedVendorId_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevCoresConnectedVendorId_Object = MibTableColumn
docsRphyRpdDevCoresConnectedVendorId = _DocsRphyRpdDevCoresConnectedVendorId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 4, 1, 6),
    _DocsRphyRpdDevCoresConnectedVendorId_Type()
)
docsRphyRpdDevCoresConnectedVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCoresConnectedVendorId.setStatus("current")
_DocsRphyRpdDevCapabilitiesTable_Object = MibTable
docsRphyRpdDevCapabilitiesTable = _DocsRphyRpdDevCapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5)
)
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabilitiesTable.setStatus("current")
_DocsRphyRpdDevCapabilitiesEntry_Object = MibTableRow
docsRphyRpdDevCapabilitiesEntry = _DocsRphyRpdDevCapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1)
)
docsRphyRpdDevCapabilitiesEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
)
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabilitiesEntry.setStatus("current")


class _DocsRphyRpdDevCapabNumDsPorts_Type(Unsigned32):
    """Custom type docsRphyRpdDevCapabNumDsPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdDevCapabNumDsPorts_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevCapabNumDsPorts_Object = MibTableColumn
docsRphyRpdDevCapabNumDsPorts = _DocsRphyRpdDevCapabNumDsPorts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 1),
    _DocsRphyRpdDevCapabNumDsPorts_Type()
)
docsRphyRpdDevCapabNumDsPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabNumDsPorts.setStatus("current")


class _DocsRphyRpdDevCapabNumUsPorts_Type(Unsigned32):
    """Custom type docsRphyRpdDevCapabNumUsPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdDevCapabNumUsPorts_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevCapabNumUsPorts_Object = MibTableColumn
docsRphyRpdDevCapabNumUsPorts = _DocsRphyRpdDevCapabNumUsPorts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 2),
    _DocsRphyRpdDevCapabNumUsPorts_Type()
)
docsRphyRpdDevCapabNumUsPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabNumUsPorts.setStatus("current")


class _DocsRphyRpdDevCapabNumTenGeNsPorts_Type(Unsigned32):
    """Custom type docsRphyRpdDevCapabNumTenGeNsPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdDevCapabNumTenGeNsPorts_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevCapabNumTenGeNsPorts_Object = MibTableColumn
docsRphyRpdDevCapabNumTenGeNsPorts = _DocsRphyRpdDevCapabNumTenGeNsPorts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 3),
    _DocsRphyRpdDevCapabNumTenGeNsPorts_Type()
)
docsRphyRpdDevCapabNumTenGeNsPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabNumTenGeNsPorts.setStatus("current")


class _DocsRphyRpdDevCapabNumOneGeNsPorts_Type(Unsigned32):
    """Custom type docsRphyRpdDevCapabNumOneGeNsPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdDevCapabNumOneGeNsPorts_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevCapabNumOneGeNsPorts_Object = MibTableColumn
docsRphyRpdDevCapabNumOneGeNsPorts = _DocsRphyRpdDevCapabNumOneGeNsPorts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 4),
    _DocsRphyRpdDevCapabNumOneGeNsPorts_Type()
)
docsRphyRpdDevCapabNumOneGeNsPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabNumOneGeNsPorts.setStatus("current")


class _DocsRphyRpdDevCapabNumDsScQamChans_Type(Unsigned32):
    """Custom type docsRphyRpdDevCapabNumDsScQamChans based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdDevCapabNumDsScQamChans_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevCapabNumDsScQamChans_Object = MibTableColumn
docsRphyRpdDevCapabNumDsScQamChans = _DocsRphyRpdDevCapabNumDsScQamChans_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 5),
    _DocsRphyRpdDevCapabNumDsScQamChans_Type()
)
docsRphyRpdDevCapabNumDsScQamChans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabNumDsScQamChans.setStatus("current")


class _DocsRphyRpdDevCapabNumDsOfdmChans_Type(Unsigned32):
    """Custom type docsRphyRpdDevCapabNumDsOfdmChans based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdDevCapabNumDsOfdmChans_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevCapabNumDsOfdmChans_Object = MibTableColumn
docsRphyRpdDevCapabNumDsOfdmChans = _DocsRphyRpdDevCapabNumDsOfdmChans_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 6),
    _DocsRphyRpdDevCapabNumDsOfdmChans_Type()
)
docsRphyRpdDevCapabNumDsOfdmChans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabNumDsOfdmChans.setStatus("current")


class _DocsRphyRpdDevCapabNumUsScQamChans_Type(Unsigned32):
    """Custom type docsRphyRpdDevCapabNumUsScQamChans based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdDevCapabNumUsScQamChans_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevCapabNumUsScQamChans_Object = MibTableColumn
docsRphyRpdDevCapabNumUsScQamChans = _DocsRphyRpdDevCapabNumUsScQamChans_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 7),
    _DocsRphyRpdDevCapabNumUsScQamChans_Type()
)
docsRphyRpdDevCapabNumUsScQamChans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabNumUsScQamChans.setStatus("current")


class _DocsRphyRpdDevCapabNumUsOfdmaChans_Type(Unsigned32):
    """Custom type docsRphyRpdDevCapabNumUsOfdmaChans based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdDevCapabNumUsOfdmaChans_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevCapabNumUsOfdmaChans_Object = MibTableColumn
docsRphyRpdDevCapabNumUsOfdmaChans = _DocsRphyRpdDevCapabNumUsOfdmaChans_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 8),
    _DocsRphyRpdDevCapabNumUsOfdmaChans_Type()
)
docsRphyRpdDevCapabNumUsOfdmaChans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabNumUsOfdmaChans.setStatus("current")


class _DocsRphyRpdDevCapabNumDsOob55d1Chans_Type(Unsigned32):
    """Custom type docsRphyRpdDevCapabNumDsOob55d1Chans based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdDevCapabNumDsOob55d1Chans_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevCapabNumDsOob55d1Chans_Object = MibTableColumn
docsRphyRpdDevCapabNumDsOob55d1Chans = _DocsRphyRpdDevCapabNumDsOob55d1Chans_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 9),
    _DocsRphyRpdDevCapabNumDsOob55d1Chans_Type()
)
docsRphyRpdDevCapabNumDsOob55d1Chans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabNumDsOob55d1Chans.setStatus("current")


class _DocsRphyRpdDevCapabNumUsOob55d1Chans_Type(Unsigned32):
    """Custom type docsRphyRpdDevCapabNumUsOob55d1Chans based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdDevCapabNumUsOob55d1Chans_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevCapabNumUsOob55d1Chans_Object = MibTableColumn
docsRphyRpdDevCapabNumUsOob55d1Chans = _DocsRphyRpdDevCapabNumUsOob55d1Chans_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 10),
    _DocsRphyRpdDevCapabNumUsOob55d1Chans_Type()
)
docsRphyRpdDevCapabNumUsOob55d1Chans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabNumUsOob55d1Chans.setStatus("current")


class _DocsRphyRpdDevCapabNumDsOob55d2Modules_Type(Unsigned32):
    """Custom type docsRphyRpdDevCapabNumDsOob55d2Modules based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdDevCapabNumDsOob55d2Modules_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevCapabNumDsOob55d2Modules_Object = MibTableColumn
docsRphyRpdDevCapabNumDsOob55d2Modules = _DocsRphyRpdDevCapabNumDsOob55d2Modules_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 11),
    _DocsRphyRpdDevCapabNumDsOob55d2Modules_Type()
)
docsRphyRpdDevCapabNumDsOob55d2Modules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabNumDsOob55d2Modules.setStatus("current")


class _DocsRphyRpdDevCapabNumUsOob55d2Demods_Type(Unsigned32):
    """Custom type docsRphyRpdDevCapabNumUsOob55d2Demods based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdDevCapabNumUsOob55d2Demods_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevCapabNumUsOob55d2Demods_Object = MibTableColumn
docsRphyRpdDevCapabNumUsOob55d2Demods = _DocsRphyRpdDevCapabNumUsOob55d2Demods_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 12),
    _DocsRphyRpdDevCapabNumUsOob55d2Demods_Type()
)
docsRphyRpdDevCapabNumUsOob55d2Demods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabNumUsOob55d2Demods.setStatus("current")


class _DocsRphyRpdDevCapabNumNdfChans_Type(Unsigned32):
    """Custom type docsRphyRpdDevCapabNumNdfChans based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdDevCapabNumNdfChans_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevCapabNumNdfChans_Object = MibTableColumn
docsRphyRpdDevCapabNumNdfChans = _DocsRphyRpdDevCapabNumNdfChans_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 13),
    _DocsRphyRpdDevCapabNumNdfChans_Type()
)
docsRphyRpdDevCapabNumNdfChans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabNumNdfChans.setStatus("current")


class _DocsRphyRpdDevCapabNumNdrChans_Type(Unsigned32):
    """Custom type docsRphyRpdDevCapabNumNdrChans based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdDevCapabNumNdrChans_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevCapabNumNdrChans_Object = MibTableColumn
docsRphyRpdDevCapabNumNdrChans = _DocsRphyRpdDevCapabNumNdrChans_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 14),
    _DocsRphyRpdDevCapabNumNdrChans_Type()
)
docsRphyRpdDevCapabNumNdrChans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabNumNdrChans.setStatus("current")


class _DocsRphyRpdDevCapabNumDsPspFlowsPerChan_Type(Unsigned32):
    """Custom type docsRphyRpdDevCapabNumDsPspFlowsPerChan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyRpdDevCapabNumDsPspFlowsPerChan_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevCapabNumDsPspFlowsPerChan_Object = MibTableColumn
docsRphyRpdDevCapabNumDsPspFlowsPerChan = _DocsRphyRpdDevCapabNumDsPspFlowsPerChan_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 15),
    _DocsRphyRpdDevCapabNumDsPspFlowsPerChan_Type()
)
docsRphyRpdDevCapabNumDsPspFlowsPerChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabNumDsPspFlowsPerChan.setStatus("current")


class _DocsRphyRpdDevCapabNumUsPspFlowsPerChan_Type(Unsigned32):
    """Custom type docsRphyRpdDevCapabNumUsPspFlowsPerChan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyRpdDevCapabNumUsPspFlowsPerChan_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevCapabNumUsPspFlowsPerChan_Object = MibTableColumn
docsRphyRpdDevCapabNumUsPspFlowsPerChan = _DocsRphyRpdDevCapabNumUsPspFlowsPerChan_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 16),
    _DocsRphyRpdDevCapabNumUsPspFlowsPerChan_Type()
)
docsRphyRpdDevCapabNumUsPspFlowsPerChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabNumUsPspFlowsPerChan.setStatus("current")


class _DocsRphyRpdDevCapabNumAsynchVideoChans_Type(Unsigned32):
    """Custom type docsRphyRpdDevCapabNumAsynchVideoChans based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyRpdDevCapabNumAsynchVideoChans_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevCapabNumAsynchVideoChans_Object = MibTableColumn
docsRphyRpdDevCapabNumAsynchVideoChans = _DocsRphyRpdDevCapabNumAsynchVideoChans_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 17),
    _DocsRphyRpdDevCapabNumAsynchVideoChans_Type()
)
docsRphyRpdDevCapabNumAsynchVideoChans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabNumAsynchVideoChans.setStatus("current")


class _DocsRphyRpdDevCapabNumCwToneGens_Type(Unsigned32):
    """Custom type docsRphyRpdDevCapabNumCwToneGens based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyRpdDevCapabNumCwToneGens_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevCapabNumCwToneGens_Object = MibTableColumn
docsRphyRpdDevCapabNumCwToneGens = _DocsRphyRpdDevCapabNumCwToneGens_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 18),
    _DocsRphyRpdDevCapabNumCwToneGens_Type()
)
docsRphyRpdDevCapabNumCwToneGens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabNumCwToneGens.setStatus("current")
_DocsRphyRpdDevCapabLowestCwToneFreq_Type = Unsigned32
_DocsRphyRpdDevCapabLowestCwToneFreq_Object = MibTableColumn
docsRphyRpdDevCapabLowestCwToneFreq = _DocsRphyRpdDevCapabLowestCwToneFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 19),
    _DocsRphyRpdDevCapabLowestCwToneFreq_Type()
)
docsRphyRpdDevCapabLowestCwToneFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabLowestCwToneFreq.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabLowestCwToneFreq.setUnits("Hz")
_DocsRphyRpdDevCapabHighestCwToneFreq_Type = Unsigned32
_DocsRphyRpdDevCapabHighestCwToneFreq_Object = MibTableColumn
docsRphyRpdDevCapabHighestCwToneFreq = _DocsRphyRpdDevCapabHighestCwToneFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 20),
    _DocsRphyRpdDevCapabHighestCwToneFreq_Type()
)
docsRphyRpdDevCapabHighestCwToneFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabHighestCwToneFreq.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabHighestCwToneFreq.setUnits("Hz")


class _DocsRphyRpdDevCapabMaxCwTonePwr_Type(Unsigned32):
    """Custom type docsRphyRpdDevCapabMaxCwTonePwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdDevCapabMaxCwTonePwr_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevCapabMaxCwTonePwr_Object = MibTableColumn
docsRphyRpdDevCapabMaxCwTonePwr = _DocsRphyRpdDevCapabMaxCwTonePwr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 21),
    _DocsRphyRpdDevCapabMaxCwTonePwr_Type()
)
docsRphyRpdDevCapabMaxCwTonePwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabMaxCwTonePwr.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabMaxCwTonePwr.setUnits("TenthdBmV")
_DocsRphyRpdDevCapabQamAsPilot_Type = TruthValue
_DocsRphyRpdDevCapabQamAsPilot_Object = MibTableColumn
docsRphyRpdDevCapabQamAsPilot = _DocsRphyRpdDevCapabQamAsPilot_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 22),
    _DocsRphyRpdDevCapabQamAsPilot_Type()
)
docsRphyRpdDevCapabQamAsPilot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabQamAsPilot.setStatus("current")
_DocsRphyRpdDevCapabSupportsUdpEncap_Type = TruthValue
_DocsRphyRpdDevCapabSupportsUdpEncap_Object = MibTableColumn
docsRphyRpdDevCapabSupportsUdpEncap = _DocsRphyRpdDevCapabSupportsUdpEncap_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 23),
    _DocsRphyRpdDevCapabSupportsUdpEncap_Type()
)
docsRphyRpdDevCapabSupportsUdpEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabSupportsUdpEncap.setStatus("current")
_DocsRphyRpdDevCapabSupportsFlowTags_Type = TruthValue
_DocsRphyRpdDevCapabSupportsFlowTags_Object = MibTableColumn
docsRphyRpdDevCapabSupportsFlowTags = _DocsRphyRpdDevCapabSupportsFlowTags_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 24),
    _DocsRphyRpdDevCapabSupportsFlowTags_Type()
)
docsRphyRpdDevCapabSupportsFlowTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabSupportsFlowTags.setStatus("current")
_DocsRphyRpdDevCapabSupportsFreqTilt_Type = TruthValue
_DocsRphyRpdDevCapabSupportsFreqTilt_Object = MibTableColumn
docsRphyRpdDevCapabSupportsFreqTilt = _DocsRphyRpdDevCapabSupportsFreqTilt_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 25),
    _DocsRphyRpdDevCapabSupportsFreqTilt_Type()
)
docsRphyRpdDevCapabSupportsFreqTilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabSupportsFreqTilt.setStatus("current")


class _DocsRphyRpdDevCapabTiltRange_Type(Unsigned32):
    """Custom type docsRphyRpdDevCapabTiltRange based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdDevCapabTiltRange_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevCapabTiltRange_Object = MibTableColumn
docsRphyRpdDevCapabTiltRange = _DocsRphyRpdDevCapabTiltRange_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 26),
    _DocsRphyRpdDevCapabTiltRange_Type()
)
docsRphyRpdDevCapabTiltRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabTiltRange.setStatus("current")


class _DocsRphyRpdDevCapabBufferDepthMonAlertSupp_Type(Bits):
    """Custom type docsRphyRpdDevCapabBufferDepthMonAlertSupp based on Bits"""
    namedValues = NamedValues(
        *(("ndfChannels", 3),
          ("ofdmChannels", 0),
          ("scQamDocsisChannels", 1),
          ("scQamVideoChannels", 2),
          ("scte551Channels", 4),
          ("scte552Channels", 5))
    )

_DocsRphyRpdDevCapabBufferDepthMonAlertSupp_Type.__name__ = "Bits"
_DocsRphyRpdDevCapabBufferDepthMonAlertSupp_Object = MibTableColumn
docsRphyRpdDevCapabBufferDepthMonAlertSupp = _DocsRphyRpdDevCapabBufferDepthMonAlertSupp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 27),
    _DocsRphyRpdDevCapabBufferDepthMonAlertSupp_Type()
)
docsRphyRpdDevCapabBufferDepthMonAlertSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabBufferDepthMonAlertSupp.setStatus("current")


class _DocsRphyRpdDevCapabBufferDepthCfgSupp_Type(Bits):
    """Custom type docsRphyRpdDevCapabBufferDepthCfgSupp based on Bits"""
    namedValues = NamedValues(
        *(("ofdmChannels", 0),
          ("scQamDocsisChannels", 1))
    )

_DocsRphyRpdDevCapabBufferDepthCfgSupp_Type.__name__ = "Bits"
_DocsRphyRpdDevCapabBufferDepthCfgSupp_Object = MibTableColumn
docsRphyRpdDevCapabBufferDepthCfgSupp = _DocsRphyRpdDevCapabBufferDepthCfgSupp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 28),
    _DocsRphyRpdDevCapabBufferDepthCfgSupp_Type()
)
docsRphyRpdDevCapabBufferDepthCfgSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabBufferDepthCfgSupp.setStatus("current")


class _DocsRphyRpdDevCapabRpdUcdProcTime_Type(Unsigned32):
    """Custom type docsRphyRpdDevCapabRpdUcdProcTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdDevCapabRpdUcdProcTime_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevCapabRpdUcdProcTime_Object = MibTableColumn
docsRphyRpdDevCapabRpdUcdProcTime = _DocsRphyRpdDevCapabRpdUcdProcTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 29),
    _DocsRphyRpdDevCapabRpdUcdProcTime_Type()
)
docsRphyRpdDevCapabRpdUcdProcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabRpdUcdProcTime.setStatus("current")


class _DocsRphyRpdDevCapabRpdUcdChgNullGrtTime_Type(Unsigned32):
    """Custom type docsRphyRpdDevCapabRpdUcdChgNullGrtTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdDevCapabRpdUcdChgNullGrtTime_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevCapabRpdUcdChgNullGrtTime_Object = MibTableColumn
docsRphyRpdDevCapabRpdUcdChgNullGrtTime = _DocsRphyRpdDevCapabRpdUcdChgNullGrtTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 30),
    _DocsRphyRpdDevCapabRpdUcdChgNullGrtTime_Type()
)
docsRphyRpdDevCapabRpdUcdChgNullGrtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabRpdUcdChgNullGrtTime.setStatus("current")


class _DocsRphyRpdDevCapabMultiSectionTimingMerRep_Type(Integer32):
    """Custom type docsRphyRpdDevCapabMultiSectionTimingMerRep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("supportType1", 1),
          ("supportType2", 2))
    )


_DocsRphyRpdDevCapabMultiSectionTimingMerRep_Type.__name__ = "Integer32"
_DocsRphyRpdDevCapabMultiSectionTimingMerRep_Object = MibTableColumn
docsRphyRpdDevCapabMultiSectionTimingMerRep = _DocsRphyRpdDevCapabMultiSectionTimingMerRep_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 5, 1, 31),
    _DocsRphyRpdDevCapabMultiSectionTimingMerRep_Type()
)
docsRphyRpdDevCapabMultiSectionTimingMerRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCapabMultiSectionTimingMerRep.setStatus("current")
_DocsRphyRpdDevChanReachabilityTable_Object = MibTable
docsRphyRpdDevChanReachabilityTable = _DocsRphyRpdDevChanReachabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 6)
)
if mibBuilder.loadTexts:
    docsRphyRpdDevChanReachabilityTable.setStatus("current")
_DocsRphyRpdDevChanReachabilityEntry_Object = MibTableRow
docsRphyRpdDevChanReachabilityEntry = _DocsRphyRpdDevChanReachabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 6, 1)
)
docsRphyRpdDevChanReachabilityEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevChanReachabilityEnetPortIndex"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevChanReachabilityRfPortIndex"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevChanReachabilityChanType"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevChanReachabilityStartChanIndex"),
)
if mibBuilder.loadTexts:
    docsRphyRpdDevChanReachabilityEntry.setStatus("current")


class _DocsRphyRpdDevChanReachabilityEnetPortIndex_Type(Unsigned32):
    """Custom type docsRphyRpdDevChanReachabilityEnetPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyRpdDevChanReachabilityEnetPortIndex_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevChanReachabilityEnetPortIndex_Object = MibTableColumn
docsRphyRpdDevChanReachabilityEnetPortIndex = _DocsRphyRpdDevChanReachabilityEnetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 6, 1, 1),
    _DocsRphyRpdDevChanReachabilityEnetPortIndex_Type()
)
docsRphyRpdDevChanReachabilityEnetPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevChanReachabilityEnetPortIndex.setStatus("current")


class _DocsRphyRpdDevChanReachabilityRfPortIndex_Type(Unsigned32):
    """Custom type docsRphyRpdDevChanReachabilityRfPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyRpdDevChanReachabilityRfPortIndex_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevChanReachabilityRfPortIndex_Object = MibTableColumn
docsRphyRpdDevChanReachabilityRfPortIndex = _DocsRphyRpdDevChanReachabilityRfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 6, 1, 2),
    _DocsRphyRpdDevChanReachabilityRfPortIndex_Type()
)
docsRphyRpdDevChanReachabilityRfPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevChanReachabilityRfPortIndex.setStatus("current")
_DocsRphyRpdDevChanReachabilityChanType_Type = RphyChannelType
_DocsRphyRpdDevChanReachabilityChanType_Object = MibTableColumn
docsRphyRpdDevChanReachabilityChanType = _DocsRphyRpdDevChanReachabilityChanType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 6, 1, 3),
    _DocsRphyRpdDevChanReachabilityChanType_Type()
)
docsRphyRpdDevChanReachabilityChanType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevChanReachabilityChanType.setStatus("current")


class _DocsRphyRpdDevChanReachabilityStartChanIndex_Type(Unsigned32):
    """Custom type docsRphyRpdDevChanReachabilityStartChanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyRpdDevChanReachabilityStartChanIndex_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevChanReachabilityStartChanIndex_Object = MibTableColumn
docsRphyRpdDevChanReachabilityStartChanIndex = _DocsRphyRpdDevChanReachabilityStartChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 6, 1, 4),
    _DocsRphyRpdDevChanReachabilityStartChanIndex_Type()
)
docsRphyRpdDevChanReachabilityStartChanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevChanReachabilityStartChanIndex.setStatus("current")


class _DocsRphyRpdDevChanReachabilityEndChanIndex_Type(Unsigned32):
    """Custom type docsRphyRpdDevChanReachabilityEndChanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyRpdDevChanReachabilityEndChanIndex_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevChanReachabilityEndChanIndex_Object = MibTableColumn
docsRphyRpdDevChanReachabilityEndChanIndex = _DocsRphyRpdDevChanReachabilityEndChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 6, 1, 5),
    _DocsRphyRpdDevChanReachabilityEndChanIndex_Type()
)
docsRphyRpdDevChanReachabilityEndChanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevChanReachabilityEndChanIndex.setStatus("current")
_DocsRphyRpdDevDsUsRfPortAllocTable_Object = MibTable
docsRphyRpdDevDsUsRfPortAllocTable = _DocsRphyRpdDevDsUsRfPortAllocTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 7)
)
if mibBuilder.loadTexts:
    docsRphyRpdDevDsUsRfPortAllocTable.setStatus("current")
_DocsRphyRpdDevDsUsRfPortAllocEntry_Object = MibTableRow
docsRphyRpdDevDsUsRfPortAllocEntry = _DocsRphyRpdDevDsUsRfPortAllocEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 7, 1)
)
docsRphyRpdDevDsUsRfPortAllocEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevDsUsRfPortAllocIndex"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevDsUsRfPortAllocDirection"),
)
if mibBuilder.loadTexts:
    docsRphyRpdDevDsUsRfPortAllocEntry.setStatus("current")


class _DocsRphyRpdDevDsUsRfPortAllocIndex_Type(Unsigned32):
    """Custom type docsRphyRpdDevDsUsRfPortAllocIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyRpdDevDsUsRfPortAllocIndex_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevDsUsRfPortAllocIndex_Object = MibTableColumn
docsRphyRpdDevDsUsRfPortAllocIndex = _DocsRphyRpdDevDsUsRfPortAllocIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 7, 1, 1),
    _DocsRphyRpdDevDsUsRfPortAllocIndex_Type()
)
docsRphyRpdDevDsUsRfPortAllocIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevDsUsRfPortAllocIndex.setStatus("current")
_DocsRphyRpdDevDsUsRfPortAllocDirection_Type = IfDirection
_DocsRphyRpdDevDsUsRfPortAllocDirection_Object = MibTableColumn
docsRphyRpdDevDsUsRfPortAllocDirection = _DocsRphyRpdDevDsUsRfPortAllocDirection_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 7, 1, 2),
    _DocsRphyRpdDevDsUsRfPortAllocDirection_Type()
)
docsRphyRpdDevDsUsRfPortAllocDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevDsUsRfPortAllocDirection.setStatus("current")


class _DocsRphyRpdDevDsUsRfPortAllocScQamChans_Type(Unsigned32):
    """Custom type docsRphyRpdDevDsUsRfPortAllocScQamChans based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdDevDsUsRfPortAllocScQamChans_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevDsUsRfPortAllocScQamChans_Object = MibTableColumn
docsRphyRpdDevDsUsRfPortAllocScQamChans = _DocsRphyRpdDevDsUsRfPortAllocScQamChans_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 7, 1, 3),
    _DocsRphyRpdDevDsUsRfPortAllocScQamChans_Type()
)
docsRphyRpdDevDsUsRfPortAllocScQamChans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevDsUsRfPortAllocScQamChans.setStatus("current")


class _DocsRphyRpdDevDsUsRfPortAllocOfdmChans_Type(Unsigned32):
    """Custom type docsRphyRpdDevDsUsRfPortAllocOfdmChans based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdDevDsUsRfPortAllocOfdmChans_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevDsUsRfPortAllocOfdmChans_Object = MibTableColumn
docsRphyRpdDevDsUsRfPortAllocOfdmChans = _DocsRphyRpdDevDsUsRfPortAllocOfdmChans_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 7, 1, 4),
    _DocsRphyRpdDevDsUsRfPortAllocOfdmChans_Type()
)
docsRphyRpdDevDsUsRfPortAllocOfdmChans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevDsUsRfPortAllocOfdmChans.setStatus("current")


class _DocsRphyRpdDevDsUsRfPortAllocOob551Chans_Type(Unsigned32):
    """Custom type docsRphyRpdDevDsUsRfPortAllocOob551Chans based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdDevDsUsRfPortAllocOob551Chans_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevDsUsRfPortAllocOob551Chans_Object = MibTableColumn
docsRphyRpdDevDsUsRfPortAllocOob551Chans = _DocsRphyRpdDevDsUsRfPortAllocOob551Chans_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 7, 1, 5),
    _DocsRphyRpdDevDsUsRfPortAllocOob551Chans_Type()
)
docsRphyRpdDevDsUsRfPortAllocOob551Chans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevDsUsRfPortAllocOob551Chans.setStatus("current")


class _DocsRphyRpdDevDsUsRfPortAllocNdChans_Type(Unsigned32):
    """Custom type docsRphyRpdDevDsUsRfPortAllocNdChans based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdDevDsUsRfPortAllocNdChans_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevDsUsRfPortAllocNdChans_Object = MibTableColumn
docsRphyRpdDevDsUsRfPortAllocNdChans = _DocsRphyRpdDevDsUsRfPortAllocNdChans_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 7, 1, 6),
    _DocsRphyRpdDevDsUsRfPortAllocNdChans_Type()
)
docsRphyRpdDevDsUsRfPortAllocNdChans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevDsUsRfPortAllocNdChans.setStatus("current")
_DocsRphyRpdDevL2tpSessionInfoTable_Object = MibTable
docsRphyRpdDevL2tpSessionInfoTable = _DocsRphyRpdDevL2tpSessionInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 8)
)
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionInfoTable.setStatus("current")
_DocsRphyRpdDevL2tpSessionInfoEntry_Object = MibTableRow
docsRphyRpdDevL2tpSessionInfoEntry = _DocsRphyRpdDevL2tpSessionInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 8, 1)
)
docsRphyRpdDevL2tpSessionInfoEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevL2tpSessionInfoLocalLcceIpAddrType"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevL2tpSessionInfoLocalLcceIpAddr"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevL2tpSessionInfoLocalId"),
)
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionInfoEntry.setStatus("current")
_DocsRphyRpdDevL2tpSessionInfoLocalLcceIpAddrType_Type = InetAddressType
_DocsRphyRpdDevL2tpSessionInfoLocalLcceIpAddrType_Object = MibTableColumn
docsRphyRpdDevL2tpSessionInfoLocalLcceIpAddrType = _DocsRphyRpdDevL2tpSessionInfoLocalLcceIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 8, 1, 1),
    _DocsRphyRpdDevL2tpSessionInfoLocalLcceIpAddrType_Type()
)
docsRphyRpdDevL2tpSessionInfoLocalLcceIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionInfoLocalLcceIpAddrType.setStatus("current")
_DocsRphyRpdDevL2tpSessionInfoLocalLcceIpAddr_Type = InetAddress
_DocsRphyRpdDevL2tpSessionInfoLocalLcceIpAddr_Object = MibTableColumn
docsRphyRpdDevL2tpSessionInfoLocalLcceIpAddr = _DocsRphyRpdDevL2tpSessionInfoLocalLcceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 8, 1, 2),
    _DocsRphyRpdDevL2tpSessionInfoLocalLcceIpAddr_Type()
)
docsRphyRpdDevL2tpSessionInfoLocalLcceIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionInfoLocalLcceIpAddr.setStatus("current")
_DocsRphyRpdDevL2tpSessionInfoLocalId_Type = Unsigned32
_DocsRphyRpdDevL2tpSessionInfoLocalId_Object = MibTableColumn
docsRphyRpdDevL2tpSessionInfoLocalId = _DocsRphyRpdDevL2tpSessionInfoLocalId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 8, 1, 3),
    _DocsRphyRpdDevL2tpSessionInfoLocalId_Type()
)
docsRphyRpdDevL2tpSessionInfoLocalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionInfoLocalId.setStatus("current")
_DocsRphyRpdDevL2tpSessionInfoRemoteLcceIpAddrType_Type = InetAddressType
_DocsRphyRpdDevL2tpSessionInfoRemoteLcceIpAddrType_Object = MibTableColumn
docsRphyRpdDevL2tpSessionInfoRemoteLcceIpAddrType = _DocsRphyRpdDevL2tpSessionInfoRemoteLcceIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 8, 1, 4),
    _DocsRphyRpdDevL2tpSessionInfoRemoteLcceIpAddrType_Type()
)
docsRphyRpdDevL2tpSessionInfoRemoteLcceIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionInfoRemoteLcceIpAddrType.setStatus("current")
_DocsRphyRpdDevL2tpSessionInfoRemoteLcceIpAddr_Type = InetAddress
_DocsRphyRpdDevL2tpSessionInfoRemoteLcceIpAddr_Object = MibTableColumn
docsRphyRpdDevL2tpSessionInfoRemoteLcceIpAddr = _DocsRphyRpdDevL2tpSessionInfoRemoteLcceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 8, 1, 5),
    _DocsRphyRpdDevL2tpSessionInfoRemoteLcceIpAddr_Type()
)
docsRphyRpdDevL2tpSessionInfoRemoteLcceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionInfoRemoteLcceIpAddr.setStatus("current")
_DocsRphyRpdDevL2tpSessionInfoRemoteId_Type = Unsigned32
_DocsRphyRpdDevL2tpSessionInfoRemoteId_Object = MibTableColumn
docsRphyRpdDevL2tpSessionInfoRemoteId = _DocsRphyRpdDevL2tpSessionInfoRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 8, 1, 6),
    _DocsRphyRpdDevL2tpSessionInfoRemoteId_Type()
)
docsRphyRpdDevL2tpSessionInfoRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionInfoRemoteId.setStatus("current")
_DocsRphyRpdDevL2tpSessionInfoCoreId_Type = MacAddress
_DocsRphyRpdDevL2tpSessionInfoCoreId_Object = MibTableColumn
docsRphyRpdDevL2tpSessionInfoCoreId = _DocsRphyRpdDevL2tpSessionInfoCoreId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 8, 1, 7),
    _DocsRphyRpdDevL2tpSessionInfoCoreId_Type()
)
docsRphyRpdDevL2tpSessionInfoCoreId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionInfoCoreId.setStatus("current")
_DocsRphyRpdDevL2tpSessionInfoConnCtrlID_Type = Unsigned32
_DocsRphyRpdDevL2tpSessionInfoConnCtrlID_Object = MibTableColumn
docsRphyRpdDevL2tpSessionInfoConnCtrlID = _DocsRphyRpdDevL2tpSessionInfoConnCtrlID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 8, 1, 8),
    _DocsRphyRpdDevL2tpSessionInfoConnCtrlID_Type()
)
docsRphyRpdDevL2tpSessionInfoConnCtrlID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionInfoConnCtrlID.setStatus("current")
_DocsRphyRpdDevL2tpSessionInfoUdpPort_Type = InetPortNumber
_DocsRphyRpdDevL2tpSessionInfoUdpPort_Object = MibTableColumn
docsRphyRpdDevL2tpSessionInfoUdpPort = _DocsRphyRpdDevL2tpSessionInfoUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 8, 1, 9),
    _DocsRphyRpdDevL2tpSessionInfoUdpPort_Type()
)
docsRphyRpdDevL2tpSessionInfoUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionInfoUdpPort.setStatus("current")
_DocsRphyRpdDevL2tpSessionInfoDescr_Type = SnmpAdminString
_DocsRphyRpdDevL2tpSessionInfoDescr_Object = MibTableColumn
docsRphyRpdDevL2tpSessionInfoDescr = _DocsRphyRpdDevL2tpSessionInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 8, 1, 10),
    _DocsRphyRpdDevL2tpSessionInfoDescr_Type()
)
docsRphyRpdDevL2tpSessionInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionInfoDescr.setStatus("current")


class _DocsRphyRpdDevL2tpSessionInfoSessionType_Type(Integer32):
    """Custom type docsRphyRpdDevL2tpSessionInfoSessionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mpt", 2),
          ("psp", 1))
    )


_DocsRphyRpdDevL2tpSessionInfoSessionType_Type.__name__ = "Integer32"
_DocsRphyRpdDevL2tpSessionInfoSessionType_Object = MibTableColumn
docsRphyRpdDevL2tpSessionInfoSessionType = _DocsRphyRpdDevL2tpSessionInfoSessionType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 8, 1, 11),
    _DocsRphyRpdDevL2tpSessionInfoSessionType_Type()
)
docsRphyRpdDevL2tpSessionInfoSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionInfoSessionType.setStatus("current")


class _DocsRphyRpdDevL2tpSessionInfoSessionSubType_Type(Integer32):
    """Custom type docsRphyRpdDevL2tpSessionInfoSessionSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("mcm", 3),
          ("mptLegacy", 1),
          ("psp551Fwd", 16),
          ("psp551Ret", 17),
          ("psp552Fwd", 18),
          ("psp552Ret", 19),
          ("pspBwReqOfdma", 8),
          ("pspBwReqScQam", 7),
          ("pspDepiMultichannel", 4),
          ("pspLegacy", 2),
          ("pspMapOfdma", 13),
          ("pspMapScQam", 12),
          ("pspNdf", 20),
          ("pspNdr", 21),
          ("pspPnm", 15),
          ("pspProbe", 9),
          ("pspRngReqOfdma", 11),
          ("pspRngReqScQam", 10),
          ("pspSpecman", 14),
          ("pspUepiOfdma", 6),
          ("pspUepiScQam", 5))
    )


_DocsRphyRpdDevL2tpSessionInfoSessionSubType_Type.__name__ = "Integer32"
_DocsRphyRpdDevL2tpSessionInfoSessionSubType_Object = MibTableColumn
docsRphyRpdDevL2tpSessionInfoSessionSubType = _DocsRphyRpdDevL2tpSessionInfoSessionSubType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 8, 1, 12),
    _DocsRphyRpdDevL2tpSessionInfoSessionSubType_Type()
)
docsRphyRpdDevL2tpSessionInfoSessionSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionInfoSessionSubType.setStatus("current")
_DocsRphyRpdDevL2tpSessionInfoMaxPayload_Type = Unsigned32
_DocsRphyRpdDevL2tpSessionInfoMaxPayload_Object = MibTableColumn
docsRphyRpdDevL2tpSessionInfoMaxPayload = _DocsRphyRpdDevL2tpSessionInfoMaxPayload_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 8, 1, 13),
    _DocsRphyRpdDevL2tpSessionInfoMaxPayload_Type()
)
docsRphyRpdDevL2tpSessionInfoMaxPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionInfoMaxPayload.setStatus("current")
_DocsRphyRpdDevL2tpSessionInfoPathPayload_Type = Unsigned32
_DocsRphyRpdDevL2tpSessionInfoPathPayload_Object = MibTableColumn
docsRphyRpdDevL2tpSessionInfoPathPayload = _DocsRphyRpdDevL2tpSessionInfoPathPayload_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 8, 1, 14),
    _DocsRphyRpdDevL2tpSessionInfoPathPayload_Type()
)
docsRphyRpdDevL2tpSessionInfoPathPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionInfoPathPayload.setStatus("current")
_DocsRphyRpdDevL2tpSessionInfoRpdIfMtu_Type = Unsigned32
_DocsRphyRpdDevL2tpSessionInfoRpdIfMtu_Object = MibTableColumn
docsRphyRpdDevL2tpSessionInfoRpdIfMtu = _DocsRphyRpdDevL2tpSessionInfoRpdIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 8, 1, 15),
    _DocsRphyRpdDevL2tpSessionInfoRpdIfMtu_Type()
)
docsRphyRpdDevL2tpSessionInfoRpdIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionInfoRpdIfMtu.setStatus("current")
_DocsRphyRpdDevL2tpSessionInfoCoreIfMtu_Type = Unsigned32
_DocsRphyRpdDevL2tpSessionInfoCoreIfMtu_Object = MibTableColumn
docsRphyRpdDevL2tpSessionInfoCoreIfMtu = _DocsRphyRpdDevL2tpSessionInfoCoreIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 8, 1, 16),
    _DocsRphyRpdDevL2tpSessionInfoCoreIfMtu_Type()
)
docsRphyRpdDevL2tpSessionInfoCoreIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionInfoCoreIfMtu.setStatus("current")


class _DocsRphyRpdDevL2tpSessionInfoErrorCode_Type(Integer32):
    """Custom type docsRphyRpdDevL2tpSessionInfoErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ifAdminStatusSetToDown", 6),
          ("invalidInterfaceValue", 3),
          ("invalidMACInterfaceValue", 2),
          ("l2tpv3Error", 5),
          ("noResourcesForInterfaceIndex", 4),
          ("none", 1))
    )


_DocsRphyRpdDevL2tpSessionInfoErrorCode_Type.__name__ = "Integer32"
_DocsRphyRpdDevL2tpSessionInfoErrorCode_Object = MibTableColumn
docsRphyRpdDevL2tpSessionInfoErrorCode = _DocsRphyRpdDevL2tpSessionInfoErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 8, 1, 17),
    _DocsRphyRpdDevL2tpSessionInfoErrorCode_Type()
)
docsRphyRpdDevL2tpSessionInfoErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionInfoErrorCode.setStatus("current")
_DocsRphyRpdDevL2tpSessionInfoCreationTime_Type = TimeStamp
_DocsRphyRpdDevL2tpSessionInfoCreationTime_Object = MibTableColumn
docsRphyRpdDevL2tpSessionInfoCreationTime = _DocsRphyRpdDevL2tpSessionInfoCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 8, 1, 18),
    _DocsRphyRpdDevL2tpSessionInfoCreationTime_Type()
)
docsRphyRpdDevL2tpSessionInfoCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionInfoCreationTime.setStatus("current")


class _DocsRphyRpdDevL2tpSessionInfoOperStatus_Type(Integer32):
    """Custom type docsRphyRpdDevL2tpSessionInfoOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 3),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("other", 1),
          ("testing", 4),
          ("up", 2))
    )


_DocsRphyRpdDevL2tpSessionInfoOperStatus_Type.__name__ = "Integer32"
_DocsRphyRpdDevL2tpSessionInfoOperStatus_Object = MibTableColumn
docsRphyRpdDevL2tpSessionInfoOperStatus = _DocsRphyRpdDevL2tpSessionInfoOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 8, 1, 19),
    _DocsRphyRpdDevL2tpSessionInfoOperStatus_Type()
)
docsRphyRpdDevL2tpSessionInfoOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionInfoOperStatus.setStatus("current")


class _DocsRphyRpdDevL2tpSessionInfoLocalStatus_Type(Bits):
    """Custom type docsRphyRpdDevL2tpSessionInfoLocalStatus based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("psnPwRxFault", 4),
          ("psnPwTxFault", 5),
          ("pwNotForwarding", 1),
          ("servicePwRxFault", 2),
          ("servicePwTxFault", 3))
    )

_DocsRphyRpdDevL2tpSessionInfoLocalStatus_Type.__name__ = "Bits"
_DocsRphyRpdDevL2tpSessionInfoLocalStatus_Object = MibTableColumn
docsRphyRpdDevL2tpSessionInfoLocalStatus = _DocsRphyRpdDevL2tpSessionInfoLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 8, 1, 20),
    _DocsRphyRpdDevL2tpSessionInfoLocalStatus_Type()
)
docsRphyRpdDevL2tpSessionInfoLocalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionInfoLocalStatus.setStatus("current")
_DocsRphyRpdDevL2tpSessionInfoLastChange_Type = TimeTicks
_DocsRphyRpdDevL2tpSessionInfoLastChange_Object = MibTableColumn
docsRphyRpdDevL2tpSessionInfoLastChange = _DocsRphyRpdDevL2tpSessionInfoLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 8, 1, 21),
    _DocsRphyRpdDevL2tpSessionInfoLastChange_Type()
)
docsRphyRpdDevL2tpSessionInfoLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionInfoLastChange.setStatus("current")
_DocsRphyRpdDevL2tpSessionStatsTable_Object = MibTable
docsRphyRpdDevL2tpSessionStatsTable = _DocsRphyRpdDevL2tpSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 9)
)
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionStatsTable.setStatus("current")
_DocsRphyRpdDevL2tpSessionStatsEntry_Object = MibTableRow
docsRphyRpdDevL2tpSessionStatsEntry = _DocsRphyRpdDevL2tpSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionStatsEntry.setStatus("current")
_DocsRphyRpdDevL2tpSessionStatsOutOfSeqPkts_Type = Counter32
_DocsRphyRpdDevL2tpSessionStatsOutOfSeqPkts_Object = MibTableColumn
docsRphyRpdDevL2tpSessionStatsOutOfSeqPkts = _DocsRphyRpdDevL2tpSessionStatsOutOfSeqPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 9, 1, 1),
    _DocsRphyRpdDevL2tpSessionStatsOutOfSeqPkts_Type()
)
docsRphyRpdDevL2tpSessionStatsOutOfSeqPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevL2tpSessionStatsOutOfSeqPkts.setStatus("current")
_DocsRphyRpdDevDiagStatusTable_Object = MibTable
docsRphyRpdDevDiagStatusTable = _DocsRphyRpdDevDiagStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 10)
)
if mibBuilder.loadTexts:
    docsRphyRpdDevDiagStatusTable.setStatus("current")
_DocsRphyRpdDevDiagStatusEntry_Object = MibTableRow
docsRphyRpdDevDiagStatusEntry = _DocsRphyRpdDevDiagStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 10, 1)
)
docsRphyRpdDevDiagStatusEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
)
if mibBuilder.loadTexts:
    docsRphyRpdDevDiagStatusEntry.setStatus("current")
_DocsRphyRpdDevDiagStatusProbableCause_Type = SnmpAdminString
_DocsRphyRpdDevDiagStatusProbableCause_Object = MibTableColumn
docsRphyRpdDevDiagStatusProbableCause = _DocsRphyRpdDevDiagStatusProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 10, 1, 1),
    _DocsRphyRpdDevDiagStatusProbableCause_Type()
)
docsRphyRpdDevDiagStatusProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevDiagStatusProbableCause.setStatus("current")
_DocsRphyRpdDevDiagStatusAdditionalText_Type = SnmpAdminString
_DocsRphyRpdDevDiagStatusAdditionalText_Object = MibTableColumn
docsRphyRpdDevDiagStatusAdditionalText = _DocsRphyRpdDevDiagStatusAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 10, 1, 2),
    _DocsRphyRpdDevDiagStatusAdditionalText_Type()
)
docsRphyRpdDevDiagStatusAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevDiagStatusAdditionalText.setStatus("current")
_DocsRphyRpdDevDiagStatusSeverityLevel_Type = RphyEventSeverityType
_DocsRphyRpdDevDiagStatusSeverityLevel_Object = MibTableColumn
docsRphyRpdDevDiagStatusSeverityLevel = _DocsRphyRpdDevDiagStatusSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 10, 1, 3),
    _DocsRphyRpdDevDiagStatusSeverityLevel_Type()
)
docsRphyRpdDevDiagStatusSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevDiagStatusSeverityLevel.setStatus("current")
_DocsRphyRpdDevDepiMcastSessionTable_Object = MibTable
docsRphyRpdDevDepiMcastSessionTable = _DocsRphyRpdDevDepiMcastSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 11)
)
if mibBuilder.loadTexts:
    docsRphyRpdDevDepiMcastSessionTable.setStatus("current")
_DocsRphyRpdDevDepiMcastSessionEntry_Object = MibTableRow
docsRphyRpdDevDepiMcastSessionEntry = _DocsRphyRpdDevDepiMcastSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 11, 1)
)
docsRphyRpdDevDepiMcastSessionEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevDepiMcastSessionIpAddrType"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevDepiMcastSessionGrpIpAddr"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevDepiMcastSessionSrcIpAddr"),
)
if mibBuilder.loadTexts:
    docsRphyRpdDevDepiMcastSessionEntry.setStatus("current")
_DocsRphyRpdDevDepiMcastSessionIpAddrType_Type = InetAddressType
_DocsRphyRpdDevDepiMcastSessionIpAddrType_Object = MibTableColumn
docsRphyRpdDevDepiMcastSessionIpAddrType = _DocsRphyRpdDevDepiMcastSessionIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 11, 1, 1),
    _DocsRphyRpdDevDepiMcastSessionIpAddrType_Type()
)
docsRphyRpdDevDepiMcastSessionIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevDepiMcastSessionIpAddrType.setStatus("current")
_DocsRphyRpdDevDepiMcastSessionGrpIpAddr_Type = InetAddress
_DocsRphyRpdDevDepiMcastSessionGrpIpAddr_Object = MibTableColumn
docsRphyRpdDevDepiMcastSessionGrpIpAddr = _DocsRphyRpdDevDepiMcastSessionGrpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 11, 1, 2),
    _DocsRphyRpdDevDepiMcastSessionGrpIpAddr_Type()
)
docsRphyRpdDevDepiMcastSessionGrpIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevDepiMcastSessionGrpIpAddr.setStatus("current")
_DocsRphyRpdDevDepiMcastSessionSrcIpAddr_Type = InetAddress
_DocsRphyRpdDevDepiMcastSessionSrcIpAddr_Object = MibTableColumn
docsRphyRpdDevDepiMcastSessionSrcIpAddr = _DocsRphyRpdDevDepiMcastSessionSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 11, 1, 3),
    _DocsRphyRpdDevDepiMcastSessionSrcIpAddr_Type()
)
docsRphyRpdDevDepiMcastSessionSrcIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevDepiMcastSessionSrcIpAddr.setStatus("current")
_DocsRphyRpdDevDepiMcastSessionLocalLcceIpAddr_Type = InetAddress
_DocsRphyRpdDevDepiMcastSessionLocalLcceIpAddr_Object = MibTableColumn
docsRphyRpdDevDepiMcastSessionLocalLcceIpAddr = _DocsRphyRpdDevDepiMcastSessionLocalLcceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 11, 1, 4),
    _DocsRphyRpdDevDepiMcastSessionLocalLcceIpAddr_Type()
)
docsRphyRpdDevDepiMcastSessionLocalLcceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevDepiMcastSessionLocalLcceIpAddr.setStatus("current")
_DocsRphyRpdDevDepiMcastSessionRemoteLcceIpAddr_Type = InetAddress
_DocsRphyRpdDevDepiMcastSessionRemoteLcceIpAddr_Object = MibTableColumn
docsRphyRpdDevDepiMcastSessionRemoteLcceIpAddr = _DocsRphyRpdDevDepiMcastSessionRemoteLcceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 11, 1, 5),
    _DocsRphyRpdDevDepiMcastSessionRemoteLcceIpAddr_Type()
)
docsRphyRpdDevDepiMcastSessionRemoteLcceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevDepiMcastSessionRemoteLcceIpAddr.setStatus("current")


class _DocsRphyRpdDevDepiMcastSessionId_Type(Unsigned32):
    """Custom type docsRphyRpdDevDepiMcastSessionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2147483649, 2147549183),
    )


_DocsRphyRpdDevDepiMcastSessionId_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevDepiMcastSessionId_Object = MibTableColumn
docsRphyRpdDevDepiMcastSessionId = _DocsRphyRpdDevDepiMcastSessionId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 11, 1, 6),
    _DocsRphyRpdDevDepiMcastSessionId_Type()
)
docsRphyRpdDevDepiMcastSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevDepiMcastSessionId.setStatus("current")
_DocsRphyRpdDevDepiMcastSessionJoinTime_Type = DateAndTime
_DocsRphyRpdDevDepiMcastSessionJoinTime_Object = MibTableColumn
docsRphyRpdDevDepiMcastSessionJoinTime = _DocsRphyRpdDevDepiMcastSessionJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 11, 1, 7),
    _DocsRphyRpdDevDepiMcastSessionJoinTime_Type()
)
docsRphyRpdDevDepiMcastSessionJoinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevDepiMcastSessionJoinTime.setStatus("current")
_DocsRphyRpdDevEventLogTable_Object = MibTable
docsRphyRpdDevEventLogTable = _DocsRphyRpdDevEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 12)
)
if mibBuilder.loadTexts:
    docsRphyRpdDevEventLogTable.setStatus("current")
_DocsRphyRpdDevEventLogEntry_Object = MibTableRow
docsRphyRpdDevEventLogEntry = _DocsRphyRpdDevEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 12, 1)
)
docsRphyRpdDevEventLogEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevEventLogIndex"),
)
if mibBuilder.loadTexts:
    docsRphyRpdDevEventLogEntry.setStatus("current")
_DocsRphyRpdDevEventLogIndex_Type = Unsigned32
_DocsRphyRpdDevEventLogIndex_Object = MibTableColumn
docsRphyRpdDevEventLogIndex = _DocsRphyRpdDevEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 12, 1, 1),
    _DocsRphyRpdDevEventLogIndex_Type()
)
docsRphyRpdDevEventLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevEventLogIndex.setStatus("current")
_DocsRphyRpdDevEventLogFirstTime_Type = DateAndTime
_DocsRphyRpdDevEventLogFirstTime_Object = MibTableColumn
docsRphyRpdDevEventLogFirstTime = _DocsRphyRpdDevEventLogFirstTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 12, 1, 2),
    _DocsRphyRpdDevEventLogFirstTime_Type()
)
docsRphyRpdDevEventLogFirstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevEventLogFirstTime.setStatus("current")
_DocsRphyRpdDevEventLogLastTime_Type = DateAndTime
_DocsRphyRpdDevEventLogLastTime_Object = MibTableColumn
docsRphyRpdDevEventLogLastTime = _DocsRphyRpdDevEventLogLastTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 12, 1, 3),
    _DocsRphyRpdDevEventLogLastTime_Type()
)
docsRphyRpdDevEventLogLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevEventLogLastTime.setStatus("current")
_DocsRphyRpdDevEventLogCounts_Type = Counter32
_DocsRphyRpdDevEventLogCounts_Object = MibTableColumn
docsRphyRpdDevEventLogCounts = _DocsRphyRpdDevEventLogCounts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 12, 1, 4),
    _DocsRphyRpdDevEventLogCounts_Type()
)
docsRphyRpdDevEventLogCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevEventLogCounts.setStatus("current")
_DocsRphyRpdDevEventLogLevel_Type = RphyEventSeverityType
_DocsRphyRpdDevEventLogLevel_Object = MibTableColumn
docsRphyRpdDevEventLogLevel = _DocsRphyRpdDevEventLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 12, 1, 5),
    _DocsRphyRpdDevEventLogLevel_Type()
)
docsRphyRpdDevEventLogLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevEventLogLevel.setStatus("current")
_DocsRphyRpdDevEventLogId_Type = Unsigned32
_DocsRphyRpdDevEventLogId_Object = MibTableColumn
docsRphyRpdDevEventLogId = _DocsRphyRpdDevEventLogId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 12, 1, 6),
    _DocsRphyRpdDevEventLogId_Type()
)
docsRphyRpdDevEventLogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevEventLogId.setStatus("current")
_DocsRphyRpdDevEventLogText_Type = SnmpAdminString
_DocsRphyRpdDevEventLogText_Object = MibTableColumn
docsRphyRpdDevEventLogText = _DocsRphyRpdDevEventLogText_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 12, 1, 7),
    _DocsRphyRpdDevEventLogText_Type()
)
docsRphyRpdDevEventLogText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevEventLogText.setStatus("current")
_DocsRphyRpdDevOob551UsChanStatusTable_Object = MibTable
docsRphyRpdDevOob551UsChanStatusTable = _DocsRphyRpdDevOob551UsChanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 13)
)
if mibBuilder.loadTexts:
    docsRphyRpdDevOob551UsChanStatusTable.setStatus("current")
_DocsRphyRpdDevOob551UsChanStatusEntry_Object = MibTableRow
docsRphyRpdDevOob551UsChanStatusEntry = _DocsRphyRpdDevOob551UsChanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 13, 1)
)
docsRphyRpdDevOob551UsChanStatusEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevOob551UsChanStatusRfPort"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevOob551UsChanStatusChannelId"),
)
if mibBuilder.loadTexts:
    docsRphyRpdDevOob551UsChanStatusEntry.setStatus("current")
_DocsRphyRpdDevOob551UsChanStatusRfPort_Type = Unsigned32
_DocsRphyRpdDevOob551UsChanStatusRfPort_Object = MibTableColumn
docsRphyRpdDevOob551UsChanStatusRfPort = _DocsRphyRpdDevOob551UsChanStatusRfPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 13, 1, 1),
    _DocsRphyRpdDevOob551UsChanStatusRfPort_Type()
)
docsRphyRpdDevOob551UsChanStatusRfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevOob551UsChanStatusRfPort.setStatus("current")
_DocsRphyRpdDevOob551UsChanStatusChannelId_Type = Unsigned32
_DocsRphyRpdDevOob551UsChanStatusChannelId_Object = MibTableColumn
docsRphyRpdDevOob551UsChanStatusChannelId = _DocsRphyRpdDevOob551UsChanStatusChannelId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 13, 1, 2),
    _DocsRphyRpdDevOob551UsChanStatusChannelId_Type()
)
docsRphyRpdDevOob551UsChanStatusChannelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevOob551UsChanStatusChannelId.setStatus("current")
_DocsRphyRpdDevOob551UsChanStatusNcIpAddrType_Type = InetAddressType
_DocsRphyRpdDevOob551UsChanStatusNcIpAddrType_Object = MibTableColumn
docsRphyRpdDevOob551UsChanStatusNcIpAddrType = _DocsRphyRpdDevOob551UsChanStatusNcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 13, 1, 3),
    _DocsRphyRpdDevOob551UsChanStatusNcIpAddrType_Type()
)
docsRphyRpdDevOob551UsChanStatusNcIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevOob551UsChanStatusNcIpAddrType.setStatus("current")
_DocsRphyRpdDevOob551UsChanStatusNcIpAddr_Type = InetAddress
_DocsRphyRpdDevOob551UsChanStatusNcIpAddr_Object = MibTableColumn
docsRphyRpdDevOob551UsChanStatusNcIpAddr = _DocsRphyRpdDevOob551UsChanStatusNcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 13, 1, 4),
    _DocsRphyRpdDevOob551UsChanStatusNcIpAddr_Type()
)
docsRphyRpdDevOob551UsChanStatusNcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevOob551UsChanStatusNcIpAddr.setStatus("current")
_DocsRphyRpdDevOob551UsChanStatusArpdSrcIpAddrType_Type = InetAddressType
_DocsRphyRpdDevOob551UsChanStatusArpdSrcIpAddrType_Object = MibTableColumn
docsRphyRpdDevOob551UsChanStatusArpdSrcIpAddrType = _DocsRphyRpdDevOob551UsChanStatusArpdSrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 13, 1, 5),
    _DocsRphyRpdDevOob551UsChanStatusArpdSrcIpAddrType_Type()
)
docsRphyRpdDevOob551UsChanStatusArpdSrcIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevOob551UsChanStatusArpdSrcIpAddrType.setStatus("current")
_DocsRphyRpdDevOob551UsChanStatusArpdSrcIpAddr_Type = InetAddress
_DocsRphyRpdDevOob551UsChanStatusArpdSrcIpAddr_Object = MibTableColumn
docsRphyRpdDevOob551UsChanStatusArpdSrcIpAddr = _DocsRphyRpdDevOob551UsChanStatusArpdSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 13, 1, 6),
    _DocsRphyRpdDevOob551UsChanStatusArpdSrcIpAddr_Type()
)
docsRphyRpdDevOob551UsChanStatusArpdSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevOob551UsChanStatusArpdSrcIpAddr.setStatus("current")
_DocsRphyRpdDevOob551UsChanStatusPerfectCellsRcvd_Type = Counter64
_DocsRphyRpdDevOob551UsChanStatusPerfectCellsRcvd_Object = MibTableColumn
docsRphyRpdDevOob551UsChanStatusPerfectCellsRcvd = _DocsRphyRpdDevOob551UsChanStatusPerfectCellsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 13, 1, 7),
    _DocsRphyRpdDevOob551UsChanStatusPerfectCellsRcvd_Type()
)
docsRphyRpdDevOob551UsChanStatusPerfectCellsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevOob551UsChanStatusPerfectCellsRcvd.setStatus("current")
_DocsRphyRpdDevOob551UsChanStatusCorrectedCellsRcvd_Type = Counter64
_DocsRphyRpdDevOob551UsChanStatusCorrectedCellsRcvd_Object = MibTableColumn
docsRphyRpdDevOob551UsChanStatusCorrectedCellsRcvd = _DocsRphyRpdDevOob551UsChanStatusCorrectedCellsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 13, 1, 8),
    _DocsRphyRpdDevOob551UsChanStatusCorrectedCellsRcvd_Type()
)
docsRphyRpdDevOob551UsChanStatusCorrectedCellsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevOob551UsChanStatusCorrectedCellsRcvd.setStatus("current")
_DocsRphyRpdDevOob551UsChanStatusUncorrectableCellsRcvd_Type = Counter64
_DocsRphyRpdDevOob551UsChanStatusUncorrectableCellsRcvd_Object = MibTableColumn
docsRphyRpdDevOob551UsChanStatusUncorrectableCellsRcvd = _DocsRphyRpdDevOob551UsChanStatusUncorrectableCellsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 13, 1, 9),
    _DocsRphyRpdDevOob551UsChanStatusUncorrectableCellsRcvd_Type()
)
docsRphyRpdDevOob551UsChanStatusUncorrectableCellsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevOob551UsChanStatusUncorrectableCellsRcvd.setStatus("current")
_DocsRphyRpdDevOob551UsChanStatusTotalCellsRcvd_Type = Counter64
_DocsRphyRpdDevOob551UsChanStatusTotalCellsRcvd_Object = MibTableColumn
docsRphyRpdDevOob551UsChanStatusTotalCellsRcvd = _DocsRphyRpdDevOob551UsChanStatusTotalCellsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 13, 1, 10),
    _DocsRphyRpdDevOob551UsChanStatusTotalCellsRcvd_Type()
)
docsRphyRpdDevOob551UsChanStatusTotalCellsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevOob551UsChanStatusTotalCellsRcvd.setStatus("current")
_DocsRphyRpdDevOob551UsChanStatusPwrLevel_Type = Integer32
_DocsRphyRpdDevOob551UsChanStatusPwrLevel_Object = MibTableColumn
docsRphyRpdDevOob551UsChanStatusPwrLevel = _DocsRphyRpdDevOob551UsChanStatusPwrLevel_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 13, 1, 11),
    _DocsRphyRpdDevOob551UsChanStatusPwrLevel_Type()
)
docsRphyRpdDevOob551UsChanStatusPwrLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevOob551UsChanStatusPwrLevel.setStatus("current")
_DocsRphyRpdDevOob551UsChanStatusMaxPwrLevel_Type = Integer32
_DocsRphyRpdDevOob551UsChanStatusMaxPwrLevel_Object = MibTableColumn
docsRphyRpdDevOob551UsChanStatusMaxPwrLevel = _DocsRphyRpdDevOob551UsChanStatusMaxPwrLevel_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 13, 1, 12),
    _DocsRphyRpdDevOob551UsChanStatusMaxPwrLevel_Type()
)
docsRphyRpdDevOob551UsChanStatusMaxPwrLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevOob551UsChanStatusMaxPwrLevel.setStatus("current")
_DocsRphyRpdDevOob551UsChanStatusMinPwrLevel_Type = Integer32
_DocsRphyRpdDevOob551UsChanStatusMinPwrLevel_Object = MibTableColumn
docsRphyRpdDevOob551UsChanStatusMinPwrLevel = _DocsRphyRpdDevOob551UsChanStatusMinPwrLevel_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 13, 1, 13),
    _DocsRphyRpdDevOob551UsChanStatusMinPwrLevel_Type()
)
docsRphyRpdDevOob551UsChanStatusMinPwrLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevOob551UsChanStatusMinPwrLevel.setStatus("current")
_DocsRphyRpdDevOob551UsChanStatusCounterDiscontinuityTime_Type = TimeStamp
_DocsRphyRpdDevOob551UsChanStatusCounterDiscontinuityTime_Object = MibTableColumn
docsRphyRpdDevOob551UsChanStatusCounterDiscontinuityTime = _DocsRphyRpdDevOob551UsChanStatusCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 13, 1, 14),
    _DocsRphyRpdDevOob551UsChanStatusCounterDiscontinuityTime_Type()
)
docsRphyRpdDevOob551UsChanStatusCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevOob551UsChanStatusCounterDiscontinuityTime.setStatus("current")
_DocsRphyRpdDevCrashDataFileStatusTable_Object = MibTable
docsRphyRpdDevCrashDataFileStatusTable = _DocsRphyRpdDevCrashDataFileStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 14)
)
if mibBuilder.loadTexts:
    docsRphyRpdDevCrashDataFileStatusTable.setStatus("current")
_DocsRphyRpdDevCrashDataFileStatusEntry_Object = MibTableRow
docsRphyRpdDevCrashDataFileStatusEntry = _DocsRphyRpdDevCrashDataFileStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 14, 1)
)
docsRphyRpdDevCrashDataFileStatusEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevCrashDataFileStatusIndex"),
)
if mibBuilder.loadTexts:
    docsRphyRpdDevCrashDataFileStatusEntry.setStatus("current")
_DocsRphyRpdDevCrashDataFileStatusIndex_Type = Unsigned32
_DocsRphyRpdDevCrashDataFileStatusIndex_Object = MibTableColumn
docsRphyRpdDevCrashDataFileStatusIndex = _DocsRphyRpdDevCrashDataFileStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 14, 1, 1),
    _DocsRphyRpdDevCrashDataFileStatusIndex_Type()
)
docsRphyRpdDevCrashDataFileStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevCrashDataFileStatusIndex.setStatus("current")


class _DocsRphyRpdDevCrashDataFileStatusFilename_Type(SnmpAdminString):
    """Custom type docsRphyRpdDevCrashDataFileStatusFilename based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DocsRphyRpdDevCrashDataFileStatusFilename_Type.__name__ = "SnmpAdminString"
_DocsRphyRpdDevCrashDataFileStatusFilename_Object = MibTableColumn
docsRphyRpdDevCrashDataFileStatusFilename = _DocsRphyRpdDevCrashDataFileStatusFilename_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 14, 1, 2),
    _DocsRphyRpdDevCrashDataFileStatusFilename_Type()
)
docsRphyRpdDevCrashDataFileStatusFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCrashDataFileStatusFilename.setStatus("current")


class _DocsRphyRpdDevCrashDataFileStatusFileStatus_Type(Integer32):
    """Custom type docsRphyRpdDevCrashDataFileStatusFileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("availableForUpload", 2),
          ("error", 7),
          ("other", 1),
          ("uploadCancelled", 6),
          ("uploadCompleted", 4),
          ("uploadInProgress", 3),
          ("uploadPending", 5))
    )


_DocsRphyRpdDevCrashDataFileStatusFileStatus_Type.__name__ = "Integer32"
_DocsRphyRpdDevCrashDataFileStatusFileStatus_Object = MibTableColumn
docsRphyRpdDevCrashDataFileStatusFileStatus = _DocsRphyRpdDevCrashDataFileStatusFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 14, 1, 3),
    _DocsRphyRpdDevCrashDataFileStatusFileStatus_Type()
)
docsRphyRpdDevCrashDataFileStatusFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevCrashDataFileStatusFileStatus.setStatus("current")
_DocsRphyRpdDevUsSignalQualityTable_Object = MibTable
docsRphyRpdDevUsSignalQualityTable = _DocsRphyRpdDevUsSignalQualityTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 15)
)
if mibBuilder.loadTexts:
    docsRphyRpdDevUsSignalQualityTable.setStatus("current")
_DocsRphyRpdDevUsSignalQualityEntry_Object = MibTableRow
docsRphyRpdDevUsSignalQualityEntry = _DocsRphyRpdDevUsSignalQualityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 15, 1)
)
docsRphyRpdDevUsSignalQualityEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevUsSignalQualityRfPort"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevUsSignalQualityChannelIfIndex"),
)
if mibBuilder.loadTexts:
    docsRphyRpdDevUsSignalQualityEntry.setStatus("current")
_DocsRphyRpdDevUsSignalQualityRfPort_Type = Unsigned32
_DocsRphyRpdDevUsSignalQualityRfPort_Object = MibTableColumn
docsRphyRpdDevUsSignalQualityRfPort = _DocsRphyRpdDevUsSignalQualityRfPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 15, 1, 1),
    _DocsRphyRpdDevUsSignalQualityRfPort_Type()
)
docsRphyRpdDevUsSignalQualityRfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevUsSignalQualityRfPort.setStatus("current")
_DocsRphyRpdDevUsSignalQualityChannelIfIndex_Type = InterfaceIndex
_DocsRphyRpdDevUsSignalQualityChannelIfIndex_Object = MibTableColumn
docsRphyRpdDevUsSignalQualityChannelIfIndex = _DocsRphyRpdDevUsSignalQualityChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 15, 1, 2),
    _DocsRphyRpdDevUsSignalQualityChannelIfIndex_Type()
)
docsRphyRpdDevUsSignalQualityChannelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevUsSignalQualityChannelIfIndex.setStatus("current")


class _DocsRphyRpdDevUsSignalQualityRxMer_Type(Integer32):
    """Custom type docsRphyRpdDevUsSignalQualityRxMer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_DocsRphyRpdDevUsSignalQualityRxMer_Type.__name__ = "Integer32"
_DocsRphyRpdDevUsSignalQualityRxMer_Object = MibTableColumn
docsRphyRpdDevUsSignalQualityRxMer = _DocsRphyRpdDevUsSignalQualityRxMer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 15, 1, 3),
    _DocsRphyRpdDevUsSignalQualityRxMer_Type()
)
docsRphyRpdDevUsSignalQualityRxMer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevUsSignalQualityRxMer.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyRpdDevUsSignalQualityRxMer.setUnits("TenthdB")
_DocsRphyRpdDevUsSignalQualityRxMerSamples_Type = Unsigned32
_DocsRphyRpdDevUsSignalQualityRxMerSamples_Object = MibTableColumn
docsRphyRpdDevUsSignalQualityRxMerSamples = _DocsRphyRpdDevUsSignalQualityRxMerSamples_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 15, 1, 4),
    _DocsRphyRpdDevUsSignalQualityRxMerSamples_Type()
)
docsRphyRpdDevUsSignalQualityRxMerSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevUsSignalQualityRxMerSamples.setStatus("current")
_DocsRphyRpdDevUsSignalQualityUnerroreds_Type = Counter64
_DocsRphyRpdDevUsSignalQualityUnerroreds_Object = MibTableColumn
docsRphyRpdDevUsSignalQualityUnerroreds = _DocsRphyRpdDevUsSignalQualityUnerroreds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 15, 1, 5),
    _DocsRphyRpdDevUsSignalQualityUnerroreds_Type()
)
docsRphyRpdDevUsSignalQualityUnerroreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevUsSignalQualityUnerroreds.setStatus("current")
_DocsRphyRpdDevUsSignalQualityCorrecteds_Type = Counter64
_DocsRphyRpdDevUsSignalQualityCorrecteds_Object = MibTableColumn
docsRphyRpdDevUsSignalQualityCorrecteds = _DocsRphyRpdDevUsSignalQualityCorrecteds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 15, 1, 6),
    _DocsRphyRpdDevUsSignalQualityCorrecteds_Type()
)
docsRphyRpdDevUsSignalQualityCorrecteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevUsSignalQualityCorrecteds.setStatus("current")
_DocsRphyRpdDevUsSignalQualityUncorrectables_Type = Counter64
_DocsRphyRpdDevUsSignalQualityUncorrectables_Object = MibTableColumn
docsRphyRpdDevUsSignalQualityUncorrectables = _DocsRphyRpdDevUsSignalQualityUncorrectables_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 1, 15, 1, 7),
    _DocsRphyRpdDevUsSignalQualityUncorrectables_Type()
)
docsRphyRpdDevUsSignalQualityUncorrectables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevUsSignalQualityUncorrectables.setStatus("current")
_DocsRphyRpdIfMibObjects_ObjectIdentity = ObjectIdentity
docsRphyRpdIfMibObjects = _DocsRphyRpdIfMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2)
)
_DocsRphyRpdIfPhysEntityTable_Object = MibTable
docsRphyRpdIfPhysEntityTable = _DocsRphyRpdIfPhysEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 1)
)
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntityTable.setStatus("current")
_DocsRphyRpdIfPhysEntityEntry_Object = MibTableRow
docsRphyRpdIfPhysEntityEntry = _DocsRphyRpdIfPhysEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 1, 1)
)
docsRphyRpdIfPhysEntityEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntityIndex"),
)
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntityEntry.setStatus("current")
_DocsRphyRpdIfPhysEntityIndex_Type = PhysicalIndex
_DocsRphyRpdIfPhysEntityIndex_Object = MibTableColumn
docsRphyRpdIfPhysEntityIndex = _DocsRphyRpdIfPhysEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 1, 1, 1),
    _DocsRphyRpdIfPhysEntityIndex_Type()
)
docsRphyRpdIfPhysEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntityIndex.setStatus("current")
_DocsRphyRpdIfPhysEntityDescr_Type = SnmpAdminString
_DocsRphyRpdIfPhysEntityDescr_Object = MibTableColumn
docsRphyRpdIfPhysEntityDescr = _DocsRphyRpdIfPhysEntityDescr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 1, 1, 2),
    _DocsRphyRpdIfPhysEntityDescr_Type()
)
docsRphyRpdIfPhysEntityDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntityDescr.setStatus("current")
_DocsRphyRpdIfPhysEntityVendorType_Type = AutonomousType
_DocsRphyRpdIfPhysEntityVendorType_Object = MibTableColumn
docsRphyRpdIfPhysEntityVendorType = _DocsRphyRpdIfPhysEntityVendorType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 1, 1, 3),
    _DocsRphyRpdIfPhysEntityVendorType_Type()
)
docsRphyRpdIfPhysEntityVendorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntityVendorType.setStatus("current")
_DocsRphyRpdIfPhysEntityContainedIn_Type = PhysicalIndexOrZero
_DocsRphyRpdIfPhysEntityContainedIn_Object = MibTableColumn
docsRphyRpdIfPhysEntityContainedIn = _DocsRphyRpdIfPhysEntityContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 1, 1, 4),
    _DocsRphyRpdIfPhysEntityContainedIn_Type()
)
docsRphyRpdIfPhysEntityContainedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntityContainedIn.setStatus("current")
_DocsRphyRpdIfPhysEntityClass_Type = IANAPhysicalClass
_DocsRphyRpdIfPhysEntityClass_Object = MibTableColumn
docsRphyRpdIfPhysEntityClass = _DocsRphyRpdIfPhysEntityClass_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 1, 1, 5),
    _DocsRphyRpdIfPhysEntityClass_Type()
)
docsRphyRpdIfPhysEntityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntityClass.setStatus("current")


class _DocsRphyRpdIfPhysEntityParentRelPos_Type(Integer32):
    """Custom type docsRphyRpdIfPhysEntityParentRelPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_DocsRphyRpdIfPhysEntityParentRelPos_Type.__name__ = "Integer32"
_DocsRphyRpdIfPhysEntityParentRelPos_Object = MibTableColumn
docsRphyRpdIfPhysEntityParentRelPos = _DocsRphyRpdIfPhysEntityParentRelPos_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 1, 1, 6),
    _DocsRphyRpdIfPhysEntityParentRelPos_Type()
)
docsRphyRpdIfPhysEntityParentRelPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntityParentRelPos.setStatus("current")
_DocsRphyRpdIfPhysEntityName_Type = SnmpAdminString
_DocsRphyRpdIfPhysEntityName_Object = MibTableColumn
docsRphyRpdIfPhysEntityName = _DocsRphyRpdIfPhysEntityName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 1, 1, 7),
    _DocsRphyRpdIfPhysEntityName_Type()
)
docsRphyRpdIfPhysEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntityName.setStatus("current")
_DocsRphyRpdIfPhysEntityHardwareRev_Type = SnmpAdminString
_DocsRphyRpdIfPhysEntityHardwareRev_Object = MibTableColumn
docsRphyRpdIfPhysEntityHardwareRev = _DocsRphyRpdIfPhysEntityHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 1, 1, 8),
    _DocsRphyRpdIfPhysEntityHardwareRev_Type()
)
docsRphyRpdIfPhysEntityHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntityHardwareRev.setStatus("current")
_DocsRphyRpdIfPhysEntityFirmwareRev_Type = SnmpAdminString
_DocsRphyRpdIfPhysEntityFirmwareRev_Object = MibTableColumn
docsRphyRpdIfPhysEntityFirmwareRev = _DocsRphyRpdIfPhysEntityFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 1, 1, 9),
    _DocsRphyRpdIfPhysEntityFirmwareRev_Type()
)
docsRphyRpdIfPhysEntityFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntityFirmwareRev.setStatus("current")
_DocsRphyRpdIfPhysEntitySoftwareRev_Type = SnmpAdminString
_DocsRphyRpdIfPhysEntitySoftwareRev_Object = MibTableColumn
docsRphyRpdIfPhysEntitySoftwareRev = _DocsRphyRpdIfPhysEntitySoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 1, 1, 10),
    _DocsRphyRpdIfPhysEntitySoftwareRev_Type()
)
docsRphyRpdIfPhysEntitySoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntitySoftwareRev.setStatus("current")


class _DocsRphyRpdIfPhysEntitySerialNum_Type(SnmpAdminString):
    """Custom type docsRphyRpdIfPhysEntitySerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DocsRphyRpdIfPhysEntitySerialNum_Type.__name__ = "SnmpAdminString"
_DocsRphyRpdIfPhysEntitySerialNum_Object = MibTableColumn
docsRphyRpdIfPhysEntitySerialNum = _DocsRphyRpdIfPhysEntitySerialNum_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 1, 1, 11),
    _DocsRphyRpdIfPhysEntitySerialNum_Type()
)
docsRphyRpdIfPhysEntitySerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntitySerialNum.setStatus("current")
_DocsRphyRpdIfPhysEntityMfgName_Type = SnmpAdminString
_DocsRphyRpdIfPhysEntityMfgName_Object = MibTableColumn
docsRphyRpdIfPhysEntityMfgName = _DocsRphyRpdIfPhysEntityMfgName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 1, 1, 12),
    _DocsRphyRpdIfPhysEntityMfgName_Type()
)
docsRphyRpdIfPhysEntityMfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntityMfgName.setStatus("current")
_DocsRphyRpdIfPhysEntityModelName_Type = SnmpAdminString
_DocsRphyRpdIfPhysEntityModelName_Object = MibTableColumn
docsRphyRpdIfPhysEntityModelName = _DocsRphyRpdIfPhysEntityModelName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 1, 1, 13),
    _DocsRphyRpdIfPhysEntityModelName_Type()
)
docsRphyRpdIfPhysEntityModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntityModelName.setStatus("current")


class _DocsRphyRpdIfPhysEntityAlias_Type(SnmpAdminString):
    """Custom type docsRphyRpdIfPhysEntityAlias based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DocsRphyRpdIfPhysEntityAlias_Type.__name__ = "SnmpAdminString"
_DocsRphyRpdIfPhysEntityAlias_Object = MibTableColumn
docsRphyRpdIfPhysEntityAlias = _DocsRphyRpdIfPhysEntityAlias_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 1, 1, 14),
    _DocsRphyRpdIfPhysEntityAlias_Type()
)
docsRphyRpdIfPhysEntityAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntityAlias.setStatus("current")


class _DocsRphyRpdIfPhysEntityAssetID_Type(SnmpAdminString):
    """Custom type docsRphyRpdIfPhysEntityAssetID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DocsRphyRpdIfPhysEntityAssetID_Type.__name__ = "SnmpAdminString"
_DocsRphyRpdIfPhysEntityAssetID_Object = MibTableColumn
docsRphyRpdIfPhysEntityAssetID = _DocsRphyRpdIfPhysEntityAssetID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 1, 1, 15),
    _DocsRphyRpdIfPhysEntityAssetID_Type()
)
docsRphyRpdIfPhysEntityAssetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntityAssetID.setStatus("current")
_DocsRphyRpdIfPhysEntityIsFRU_Type = TruthValue
_DocsRphyRpdIfPhysEntityIsFRU_Object = MibTableColumn
docsRphyRpdIfPhysEntityIsFRU = _DocsRphyRpdIfPhysEntityIsFRU_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 1, 1, 16),
    _DocsRphyRpdIfPhysEntityIsFRU_Type()
)
docsRphyRpdIfPhysEntityIsFRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntityIsFRU.setStatus("current")
_DocsRphyRpdIfPhysEntityMfgDate_Type = DateAndTime
_DocsRphyRpdIfPhysEntityMfgDate_Object = MibTableColumn
docsRphyRpdIfPhysEntityMfgDate = _DocsRphyRpdIfPhysEntityMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 1, 1, 17),
    _DocsRphyRpdIfPhysEntityMfgDate_Type()
)
docsRphyRpdIfPhysEntityMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntityMfgDate.setStatus("current")
_DocsRphyRpdIfPhysEntityUris_Type = OctetString
_DocsRphyRpdIfPhysEntityUris_Object = MibTableColumn
docsRphyRpdIfPhysEntityUris = _DocsRphyRpdIfPhysEntityUris_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 1, 1, 18),
    _DocsRphyRpdIfPhysEntityUris_Type()
)
docsRphyRpdIfPhysEntityUris.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntityUris.setStatus("current")
_DocsRphyRpdIfPhysEntityUUID_Type = UUIDorZero
_DocsRphyRpdIfPhysEntityUUID_Object = MibTableColumn
docsRphyRpdIfPhysEntityUUID = _DocsRphyRpdIfPhysEntityUUID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 1, 1, 19),
    _DocsRphyRpdIfPhysEntityUUID_Type()
)
docsRphyRpdIfPhysEntityUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntityUUID.setStatus("current")
_DocsRphyRpdIfPhysEntityCoreIfIndex_Type = InterfaceIndexOrZero
_DocsRphyRpdIfPhysEntityCoreIfIndex_Object = MibTableColumn
docsRphyRpdIfPhysEntityCoreIfIndex = _DocsRphyRpdIfPhysEntityCoreIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 1, 1, 20),
    _DocsRphyRpdIfPhysEntityCoreIfIndex_Type()
)
docsRphyRpdIfPhysEntityCoreIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntityCoreIfIndex.setStatus("current")
_DocsRphyRpdIfPhysEntSensorTable_Object = MibTable
docsRphyRpdIfPhysEntSensorTable = _DocsRphyRpdIfPhysEntSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 2)
)
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntSensorTable.setStatus("current")
_DocsRphyRpdIfPhysEntSensorEntry_Object = MibTableRow
docsRphyRpdIfPhysEntSensorEntry = _DocsRphyRpdIfPhysEntSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 2, 1)
)
docsRphyRpdIfPhysEntSensorEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntityIndex"),
)
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntSensorEntry.setStatus("current")
_DocsRphyRpdIfPhysEntSensorType_Type = EntitySensorDataType
_DocsRphyRpdIfPhysEntSensorType_Object = MibTableColumn
docsRphyRpdIfPhysEntSensorType = _DocsRphyRpdIfPhysEntSensorType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 2, 1, 1),
    _DocsRphyRpdIfPhysEntSensorType_Type()
)
docsRphyRpdIfPhysEntSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntSensorType.setStatus("current")
_DocsRphyRpdIfPhysEntSensorScale_Type = EntitySensorDataScale
_DocsRphyRpdIfPhysEntSensorScale_Object = MibTableColumn
docsRphyRpdIfPhysEntSensorScale = _DocsRphyRpdIfPhysEntSensorScale_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 2, 1, 2),
    _DocsRphyRpdIfPhysEntSensorScale_Type()
)
docsRphyRpdIfPhysEntSensorScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntSensorScale.setStatus("current")
_DocsRphyRpdIfPhysEntSensorPrecision_Type = EntitySensorPrecision
_DocsRphyRpdIfPhysEntSensorPrecision_Object = MibTableColumn
docsRphyRpdIfPhysEntSensorPrecision = _DocsRphyRpdIfPhysEntSensorPrecision_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 2, 1, 3),
    _DocsRphyRpdIfPhysEntSensorPrecision_Type()
)
docsRphyRpdIfPhysEntSensorPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntSensorPrecision.setStatus("current")
_DocsRphyRpdIfPhysEntSensorValue_Type = EntitySensorValue
_DocsRphyRpdIfPhysEntSensorValue_Object = MibTableColumn
docsRphyRpdIfPhysEntSensorValue = _DocsRphyRpdIfPhysEntSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 2, 1, 4),
    _DocsRphyRpdIfPhysEntSensorValue_Type()
)
docsRphyRpdIfPhysEntSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntSensorValue.setStatus("current")
_DocsRphyRpdIfPhysEntSensorOperStatus_Type = EntitySensorStatus
_DocsRphyRpdIfPhysEntSensorOperStatus_Object = MibTableColumn
docsRphyRpdIfPhysEntSensorOperStatus = _DocsRphyRpdIfPhysEntSensorOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 2, 1, 5),
    _DocsRphyRpdIfPhysEntSensorOperStatus_Type()
)
docsRphyRpdIfPhysEntSensorOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntSensorOperStatus.setStatus("current")
_DocsRphyRpdIfPhysEntSensorUnitsDisplay_Type = SnmpAdminString
_DocsRphyRpdIfPhysEntSensorUnitsDisplay_Object = MibTableColumn
docsRphyRpdIfPhysEntSensorUnitsDisplay = _DocsRphyRpdIfPhysEntSensorUnitsDisplay_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 2, 1, 6),
    _DocsRphyRpdIfPhysEntSensorUnitsDisplay_Type()
)
docsRphyRpdIfPhysEntSensorUnitsDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntSensorUnitsDisplay.setStatus("current")
_DocsRphyRpdIfPhysEntSensorValueTimeStamp_Type = TimeStamp
_DocsRphyRpdIfPhysEntSensorValueTimeStamp_Object = MibTableColumn
docsRphyRpdIfPhysEntSensorValueTimeStamp = _DocsRphyRpdIfPhysEntSensorValueTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 2, 1, 7),
    _DocsRphyRpdIfPhysEntSensorValueTimeStamp_Type()
)
docsRphyRpdIfPhysEntSensorValueTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntSensorValueTimeStamp.setStatus("current")
_DocsRphyRpdIfPhysEntSensorValueUpdateRate_Type = Unsigned32
_DocsRphyRpdIfPhysEntSensorValueUpdateRate_Object = MibTableColumn
docsRphyRpdIfPhysEntSensorValueUpdateRate = _DocsRphyRpdIfPhysEntSensorValueUpdateRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 2, 1, 8),
    _DocsRphyRpdIfPhysEntSensorValueUpdateRate_Type()
)
docsRphyRpdIfPhysEntSensorValueUpdateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntSensorValueUpdateRate.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyRpdIfPhysEntSensorValueUpdateRate.setUnits("milliseconds")
_DocsRphyRpdIfEnetTable_Object = MibTable
docsRphyRpdIfEnetTable = _DocsRphyRpdIfEnetTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 3)
)
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetTable.setStatus("current")
_DocsRphyRpdIfEnetEntry_Object = MibTableRow
docsRphyRpdIfEnetEntry = _DocsRphyRpdIfEnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 3, 1)
)
docsRphyRpdIfEnetEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdIfEnetPortIndex"),
)
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetEntry.setStatus("current")


class _DocsRphyRpdIfEnetPortIndex_Type(Unsigned32):
    """Custom type docsRphyRpdIfEnetPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyRpdIfEnetPortIndex_Type.__name__ = "Unsigned32"
_DocsRphyRpdIfEnetPortIndex_Object = MibTableColumn
docsRphyRpdIfEnetPortIndex = _DocsRphyRpdIfEnetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 3, 1, 1),
    _DocsRphyRpdIfEnetPortIndex_Type()
)
docsRphyRpdIfEnetPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetPortIndex.setStatus("current")


class _DocsRphyRpdIfEnetDescr_Type(SnmpAdminString):
    """Custom type docsRphyRpdIfEnetDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DocsRphyRpdIfEnetDescr_Type.__name__ = "SnmpAdminString"
_DocsRphyRpdIfEnetDescr_Object = MibTableColumn
docsRphyRpdIfEnetDescr = _DocsRphyRpdIfEnetDescr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 3, 1, 2),
    _DocsRphyRpdIfEnetDescr_Type()
)
docsRphyRpdIfEnetDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetDescr.setStatus("current")
_DocsRphyRpdIfEnetName_Type = SnmpAdminString
_DocsRphyRpdIfEnetName_Object = MibTableColumn
docsRphyRpdIfEnetName = _DocsRphyRpdIfEnetName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 3, 1, 3),
    _DocsRphyRpdIfEnetName_Type()
)
docsRphyRpdIfEnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetName.setStatus("current")


class _DocsRphyRpdIfEnetAlias_Type(SnmpAdminString):
    """Custom type docsRphyRpdIfEnetAlias based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DocsRphyRpdIfEnetAlias_Type.__name__ = "SnmpAdminString"
_DocsRphyRpdIfEnetAlias_Object = MibTableColumn
docsRphyRpdIfEnetAlias = _DocsRphyRpdIfEnetAlias_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 3, 1, 4),
    _DocsRphyRpdIfEnetAlias_Type()
)
docsRphyRpdIfEnetAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetAlias.setStatus("current")
_DocsRphyRpdIfEnetType_Type = IANAifType
_DocsRphyRpdIfEnetType_Object = MibTableColumn
docsRphyRpdIfEnetType = _DocsRphyRpdIfEnetType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 3, 1, 5),
    _DocsRphyRpdIfEnetType_Type()
)
docsRphyRpdIfEnetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetType.setStatus("current")
_DocsRphyRpdIfEnetMtu_Type = Integer32
_DocsRphyRpdIfEnetMtu_Object = MibTableColumn
docsRphyRpdIfEnetMtu = _DocsRphyRpdIfEnetMtu_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 3, 1, 6),
    _DocsRphyRpdIfEnetMtu_Type()
)
docsRphyRpdIfEnetMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetMtu.setStatus("current")
_DocsRphyRpdIfEnetPhysAddress_Type = PhysAddress
_DocsRphyRpdIfEnetPhysAddress_Object = MibTableColumn
docsRphyRpdIfEnetPhysAddress = _DocsRphyRpdIfEnetPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 3, 1, 7),
    _DocsRphyRpdIfEnetPhysAddress_Type()
)
docsRphyRpdIfEnetPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetPhysAddress.setStatus("current")


class _DocsRphyRpdIfEnetAdminStatus_Type(Integer32):
    """Custom type docsRphyRpdIfEnetAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_DocsRphyRpdIfEnetAdminStatus_Type.__name__ = "Integer32"
_DocsRphyRpdIfEnetAdminStatus_Object = MibTableColumn
docsRphyRpdIfEnetAdminStatus = _DocsRphyRpdIfEnetAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 3, 1, 8),
    _DocsRphyRpdIfEnetAdminStatus_Type()
)
docsRphyRpdIfEnetAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetAdminStatus.setStatus("current")


class _DocsRphyRpdIfEnetOperStatus_Type(Integer32):
    """Custom type docsRphyRpdIfEnetOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_DocsRphyRpdIfEnetOperStatus_Type.__name__ = "Integer32"
_DocsRphyRpdIfEnetOperStatus_Object = MibTableColumn
docsRphyRpdIfEnetOperStatus = _DocsRphyRpdIfEnetOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 3, 1, 9),
    _DocsRphyRpdIfEnetOperStatus_Type()
)
docsRphyRpdIfEnetOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetOperStatus.setStatus("current")
_DocsRphyRpdIfEnetLastChange_Type = TimeTicks
_DocsRphyRpdIfEnetLastChange_Object = MibTableColumn
docsRphyRpdIfEnetLastChange = _DocsRphyRpdIfEnetLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 3, 1, 10),
    _DocsRphyRpdIfEnetLastChange_Type()
)
docsRphyRpdIfEnetLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetLastChange.setStatus("current")
_DocsRphyRpdIfEnetLinkUpDownTrapEnable_Type = TruthValue
_DocsRphyRpdIfEnetLinkUpDownTrapEnable_Object = MibTableColumn
docsRphyRpdIfEnetLinkUpDownTrapEnable = _DocsRphyRpdIfEnetLinkUpDownTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 3, 1, 11),
    _DocsRphyRpdIfEnetLinkUpDownTrapEnable_Type()
)
docsRphyRpdIfEnetLinkUpDownTrapEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetLinkUpDownTrapEnable.setStatus("current")
_DocsRphyRpdIfEnetHighSpeed_Type = Gauge32
_DocsRphyRpdIfEnetHighSpeed_Object = MibTableColumn
docsRphyRpdIfEnetHighSpeed = _DocsRphyRpdIfEnetHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 3, 1, 12),
    _DocsRphyRpdIfEnetHighSpeed_Type()
)
docsRphyRpdIfEnetHighSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetHighSpeed.setStatus("current")
_DocsRphyRpdIfEnetPromiscuousMode_Type = TruthValue
_DocsRphyRpdIfEnetPromiscuousMode_Object = MibTableColumn
docsRphyRpdIfEnetPromiscuousMode = _DocsRphyRpdIfEnetPromiscuousMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 3, 1, 13),
    _DocsRphyRpdIfEnetPromiscuousMode_Type()
)
docsRphyRpdIfEnetPromiscuousMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetPromiscuousMode.setStatus("current")
_DocsRphyRpdIfEnetConnectorPresent_Type = TruthValue
_DocsRphyRpdIfEnetConnectorPresent_Object = MibTableColumn
docsRphyRpdIfEnetConnectorPresent = _DocsRphyRpdIfEnetConnectorPresent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 3, 1, 14),
    _DocsRphyRpdIfEnetConnectorPresent_Type()
)
docsRphyRpdIfEnetConnectorPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetConnectorPresent.setStatus("current")
_DocsRphyRpdIfEnetStatsTable_Object = MibTable
docsRphyRpdIfEnetStatsTable = _DocsRphyRpdIfEnetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 4)
)
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetStatsTable.setStatus("current")
_DocsRphyRpdIfEnetStatsEntry_Object = MibTableRow
docsRphyRpdIfEnetStatsEntry = _DocsRphyRpdIfEnetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetStatsEntry.setStatus("current")
_DocsRphyRpdIfEnetStatsInOctets_Type = Counter64
_DocsRphyRpdIfEnetStatsInOctets_Object = MibTableColumn
docsRphyRpdIfEnetStatsInOctets = _DocsRphyRpdIfEnetStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 4, 1, 1),
    _DocsRphyRpdIfEnetStatsInOctets_Type()
)
docsRphyRpdIfEnetStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetStatsInOctets.setStatus("current")
_DocsRphyRpdIfEnetStatsOutOctets_Type = Counter64
_DocsRphyRpdIfEnetStatsOutOctets_Object = MibTableColumn
docsRphyRpdIfEnetStatsOutOctets = _DocsRphyRpdIfEnetStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 4, 1, 2),
    _DocsRphyRpdIfEnetStatsOutOctets_Type()
)
docsRphyRpdIfEnetStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetStatsOutOctets.setStatus("current")
_DocsRphyRpdIfEnetStatsInFrames_Type = Counter64
_DocsRphyRpdIfEnetStatsInFrames_Object = MibTableColumn
docsRphyRpdIfEnetStatsInFrames = _DocsRphyRpdIfEnetStatsInFrames_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 4, 1, 3),
    _DocsRphyRpdIfEnetStatsInFrames_Type()
)
docsRphyRpdIfEnetStatsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetStatsInFrames.setStatus("current")
_DocsRphyRpdIfEnetStatsOutFrames_Type = Counter64
_DocsRphyRpdIfEnetStatsOutFrames_Object = MibTableColumn
docsRphyRpdIfEnetStatsOutFrames = _DocsRphyRpdIfEnetStatsOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 4, 1, 4),
    _DocsRphyRpdIfEnetStatsOutFrames_Type()
)
docsRphyRpdIfEnetStatsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetStatsOutFrames.setStatus("current")
_DocsRphyRpdIfEnetStatsInUnicastOctets_Type = Counter64
_DocsRphyRpdIfEnetStatsInUnicastOctets_Object = MibTableColumn
docsRphyRpdIfEnetStatsInUnicastOctets = _DocsRphyRpdIfEnetStatsInUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 4, 1, 5),
    _DocsRphyRpdIfEnetStatsInUnicastOctets_Type()
)
docsRphyRpdIfEnetStatsInUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetStatsInUnicastOctets.setStatus("current")
_DocsRphyRpdIfEnetStatsOutUnicastOctets_Type = Counter64
_DocsRphyRpdIfEnetStatsOutUnicastOctets_Object = MibTableColumn
docsRphyRpdIfEnetStatsOutUnicastOctets = _DocsRphyRpdIfEnetStatsOutUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 4, 1, 6),
    _DocsRphyRpdIfEnetStatsOutUnicastOctets_Type()
)
docsRphyRpdIfEnetStatsOutUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetStatsOutUnicastOctets.setStatus("current")
_DocsRphyRpdIfEnetStatsInUnicastFrames_Type = Counter64
_DocsRphyRpdIfEnetStatsInUnicastFrames_Object = MibTableColumn
docsRphyRpdIfEnetStatsInUnicastFrames = _DocsRphyRpdIfEnetStatsInUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 4, 1, 7),
    _DocsRphyRpdIfEnetStatsInUnicastFrames_Type()
)
docsRphyRpdIfEnetStatsInUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetStatsInUnicastFrames.setStatus("current")
_DocsRphyRpdIfEnetStatsOutUnicastFrames_Type = Counter64
_DocsRphyRpdIfEnetStatsOutUnicastFrames_Object = MibTableColumn
docsRphyRpdIfEnetStatsOutUnicastFrames = _DocsRphyRpdIfEnetStatsOutUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 4, 1, 8),
    _DocsRphyRpdIfEnetStatsOutUnicastFrames_Type()
)
docsRphyRpdIfEnetStatsOutUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetStatsOutUnicastFrames.setStatus("current")
_DocsRphyRpdIfEnetStatsInMulticastOctets_Type = Counter64
_DocsRphyRpdIfEnetStatsInMulticastOctets_Object = MibTableColumn
docsRphyRpdIfEnetStatsInMulticastOctets = _DocsRphyRpdIfEnetStatsInMulticastOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 4, 1, 9),
    _DocsRphyRpdIfEnetStatsInMulticastOctets_Type()
)
docsRphyRpdIfEnetStatsInMulticastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetStatsInMulticastOctets.setStatus("current")
_DocsRphyRpdIfEnetStatsOutMulticastOctets_Type = Counter64
_DocsRphyRpdIfEnetStatsOutMulticastOctets_Object = MibTableColumn
docsRphyRpdIfEnetStatsOutMulticastOctets = _DocsRphyRpdIfEnetStatsOutMulticastOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 4, 1, 10),
    _DocsRphyRpdIfEnetStatsOutMulticastOctets_Type()
)
docsRphyRpdIfEnetStatsOutMulticastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetStatsOutMulticastOctets.setStatus("current")
_DocsRphyRpdIfEnetStatsInMulticastFrames_Type = Counter64
_DocsRphyRpdIfEnetStatsInMulticastFrames_Object = MibTableColumn
docsRphyRpdIfEnetStatsInMulticastFrames = _DocsRphyRpdIfEnetStatsInMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 4, 1, 11),
    _DocsRphyRpdIfEnetStatsInMulticastFrames_Type()
)
docsRphyRpdIfEnetStatsInMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetStatsInMulticastFrames.setStatus("current")
_DocsRphyRpdIfEnetStatsOutMulticastFrames_Type = Counter64
_DocsRphyRpdIfEnetStatsOutMulticastFrames_Object = MibTableColumn
docsRphyRpdIfEnetStatsOutMulticastFrames = _DocsRphyRpdIfEnetStatsOutMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 4, 1, 12),
    _DocsRphyRpdIfEnetStatsOutMulticastFrames_Type()
)
docsRphyRpdIfEnetStatsOutMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetStatsOutMulticastFrames.setStatus("current")
_DocsRphyRpdIfEnetStatsInBroadcastOctets_Type = Counter64
_DocsRphyRpdIfEnetStatsInBroadcastOctets_Object = MibTableColumn
docsRphyRpdIfEnetStatsInBroadcastOctets = _DocsRphyRpdIfEnetStatsInBroadcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 4, 1, 13),
    _DocsRphyRpdIfEnetStatsInBroadcastOctets_Type()
)
docsRphyRpdIfEnetStatsInBroadcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetStatsInBroadcastOctets.setStatus("current")
_DocsRphyRpdIfEnetStatsOutBroadcastOctets_Type = Counter64
_DocsRphyRpdIfEnetStatsOutBroadcastOctets_Object = MibTableColumn
docsRphyRpdIfEnetStatsOutBroadcastOctets = _DocsRphyRpdIfEnetStatsOutBroadcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 4, 1, 14),
    _DocsRphyRpdIfEnetStatsOutBroadcastOctets_Type()
)
docsRphyRpdIfEnetStatsOutBroadcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetStatsOutBroadcastOctets.setStatus("current")
_DocsRphyRpdIfEnetStatsInBroadcastFrames_Type = Counter64
_DocsRphyRpdIfEnetStatsInBroadcastFrames_Object = MibTableColumn
docsRphyRpdIfEnetStatsInBroadcastFrames = _DocsRphyRpdIfEnetStatsInBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 4, 1, 15),
    _DocsRphyRpdIfEnetStatsInBroadcastFrames_Type()
)
docsRphyRpdIfEnetStatsInBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetStatsInBroadcastFrames.setStatus("current")
_DocsRphyRpdIfEnetStatsOutBroadcastFrames_Type = Counter64
_DocsRphyRpdIfEnetStatsOutBroadcastFrames_Object = MibTableColumn
docsRphyRpdIfEnetStatsOutBroadcastFrames = _DocsRphyRpdIfEnetStatsOutBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 4, 1, 16),
    _DocsRphyRpdIfEnetStatsOutBroadcastFrames_Type()
)
docsRphyRpdIfEnetStatsOutBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetStatsOutBroadcastFrames.setStatus("current")
_DocsRphyRpdIfEnetStatsInDiscards_Type = Counter64
_DocsRphyRpdIfEnetStatsInDiscards_Object = MibTableColumn
docsRphyRpdIfEnetStatsInDiscards = _DocsRphyRpdIfEnetStatsInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 4, 1, 17),
    _DocsRphyRpdIfEnetStatsInDiscards_Type()
)
docsRphyRpdIfEnetStatsInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetStatsInDiscards.setStatus("current")
_DocsRphyRpdIfEnetStatsOutDiscards_Type = Counter64
_DocsRphyRpdIfEnetStatsOutDiscards_Object = MibTableColumn
docsRphyRpdIfEnetStatsOutDiscards = _DocsRphyRpdIfEnetStatsOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 4, 1, 18),
    _DocsRphyRpdIfEnetStatsOutDiscards_Type()
)
docsRphyRpdIfEnetStatsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetStatsOutDiscards.setStatus("current")
_DocsRphyRpdIfEnetStatsInErrors_Type = Counter64
_DocsRphyRpdIfEnetStatsInErrors_Object = MibTableColumn
docsRphyRpdIfEnetStatsInErrors = _DocsRphyRpdIfEnetStatsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 4, 1, 19),
    _DocsRphyRpdIfEnetStatsInErrors_Type()
)
docsRphyRpdIfEnetStatsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetStatsInErrors.setStatus("current")
_DocsRphyRpdIfEnetStatsOutErrors_Type = Counter64
_DocsRphyRpdIfEnetStatsOutErrors_Object = MibTableColumn
docsRphyRpdIfEnetStatsOutErrors = _DocsRphyRpdIfEnetStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 4, 1, 20),
    _DocsRphyRpdIfEnetStatsOutErrors_Type()
)
docsRphyRpdIfEnetStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetStatsOutErrors.setStatus("current")
_DocsRphyRpdIfEnetStatsInUnknownProtos_Type = Counter64
_DocsRphyRpdIfEnetStatsInUnknownProtos_Object = MibTableColumn
docsRphyRpdIfEnetStatsInUnknownProtos = _DocsRphyRpdIfEnetStatsInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 4, 1, 21),
    _DocsRphyRpdIfEnetStatsInUnknownProtos_Type()
)
docsRphyRpdIfEnetStatsInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetStatsInUnknownProtos.setStatus("current")
_DocsRphyRpdIfEnetStatsCounterDiscontinuityTime_Type = TimeStamp
_DocsRphyRpdIfEnetStatsCounterDiscontinuityTime_Object = MibTableColumn
docsRphyRpdIfEnetStatsCounterDiscontinuityTime = _DocsRphyRpdIfEnetStatsCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 4, 1, 22),
    _DocsRphyRpdIfEnetStatsCounterDiscontinuityTime_Type()
)
docsRphyRpdIfEnetStatsCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfEnetStatsCounterDiscontinuityTime.setStatus("current")
_DocsRphyRpdIfRpdEnetToCoreEntityMapTable_Object = MibTable
docsRphyRpdIfRpdEnetToCoreEntityMapTable = _DocsRphyRpdIfRpdEnetToCoreEntityMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 5)
)
if mibBuilder.loadTexts:
    docsRphyRpdIfRpdEnetToCoreEntityMapTable.setStatus("current")
_DocsRphyRpdIfRpdEnetToCoreEntityMapEntry_Object = MibTableRow
docsRphyRpdIfRpdEnetToCoreEntityMapEntry = _DocsRphyRpdIfRpdEnetToCoreEntityMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 5, 1)
)
docsRphyRpdIfRpdEnetToCoreEntityMapEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdIfEnetPortIndex"),
)
if mibBuilder.loadTexts:
    docsRphyRpdIfRpdEnetToCoreEntityMapEntry.setStatus("current")
_DocsRphyRpdIfRpdEnetToCoreEntityMapEntityIndex_Type = Unsigned32
_DocsRphyRpdIfRpdEnetToCoreEntityMapEntityIndex_Object = MibTableColumn
docsRphyRpdIfRpdEnetToCoreEntityMapEntityIndex = _DocsRphyRpdIfRpdEnetToCoreEntityMapEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 5, 1, 1),
    _DocsRphyRpdIfRpdEnetToCoreEntityMapEntityIndex_Type()
)
docsRphyRpdIfRpdEnetToCoreEntityMapEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfRpdEnetToCoreEntityMapEntityIndex.setStatus("current")
_DocsRphyRpdIfCoreToRpdMapTable_Object = MibTable
docsRphyRpdIfCoreToRpdMapTable = _DocsRphyRpdIfCoreToRpdMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 6)
)
if mibBuilder.loadTexts:
    docsRphyRpdIfCoreToRpdMapTable.setStatus("current")
_DocsRphyRpdIfCoreToRpdMapEntry_Object = MibTableRow
docsRphyRpdIfCoreToRpdMapEntry = _DocsRphyRpdIfCoreToRpdMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 6, 1)
)
docsRphyRpdIfCoreToRpdMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsRphyRpdIfCoreToRpdMapEntry.setStatus("current")
_DocsRphyRpdIfCoreToRpdMapRpdUniqueId_Type = MacAddress
_DocsRphyRpdIfCoreToRpdMapRpdUniqueId_Object = MibTableColumn
docsRphyRpdIfCoreToRpdMapRpdUniqueId = _DocsRphyRpdIfCoreToRpdMapRpdUniqueId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 6, 1, 1),
    _DocsRphyRpdIfCoreToRpdMapRpdUniqueId_Type()
)
docsRphyRpdIfCoreToRpdMapRpdUniqueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfCoreToRpdMapRpdUniqueId.setStatus("current")
_DocsRphyRpdIfCoreToRpdMapRpdRfPortDirection_Type = IfDirection
_DocsRphyRpdIfCoreToRpdMapRpdRfPortDirection_Object = MibTableColumn
docsRphyRpdIfCoreToRpdMapRpdRfPortDirection = _DocsRphyRpdIfCoreToRpdMapRpdRfPortDirection_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 6, 1, 2),
    _DocsRphyRpdIfCoreToRpdMapRpdRfPortDirection_Type()
)
docsRphyRpdIfCoreToRpdMapRpdRfPortDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfCoreToRpdMapRpdRfPortDirection.setStatus("current")


class _DocsRphyRpdIfCoreToRpdMapRpdRfPortIndex_Type(Unsigned32):
    """Custom type docsRphyRpdIfCoreToRpdMapRpdRfPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyRpdIfCoreToRpdMapRpdRfPortIndex_Type.__name__ = "Unsigned32"
_DocsRphyRpdIfCoreToRpdMapRpdRfPortIndex_Object = MibTableColumn
docsRphyRpdIfCoreToRpdMapRpdRfPortIndex = _DocsRphyRpdIfCoreToRpdMapRpdRfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 6, 1, 3),
    _DocsRphyRpdIfCoreToRpdMapRpdRfPortIndex_Type()
)
docsRphyRpdIfCoreToRpdMapRpdRfPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfCoreToRpdMapRpdRfPortIndex.setStatus("current")
_DocsRphyRpdIfCoreToRpdMapRpdRfChanType_Type = RphyChannelType
_DocsRphyRpdIfCoreToRpdMapRpdRfChanType_Object = MibTableColumn
docsRphyRpdIfCoreToRpdMapRpdRfChanType = _DocsRphyRpdIfCoreToRpdMapRpdRfChanType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 6, 1, 4),
    _DocsRphyRpdIfCoreToRpdMapRpdRfChanType_Type()
)
docsRphyRpdIfCoreToRpdMapRpdRfChanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfCoreToRpdMapRpdRfChanType.setStatus("current")


class _DocsRphyRpdIfCoreToRpdMapRpdRfChanIndex_Type(Unsigned32):
    """Custom type docsRphyRpdIfCoreToRpdMapRpdRfChanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyRpdIfCoreToRpdMapRpdRfChanIndex_Type.__name__ = "Unsigned32"
_DocsRphyRpdIfCoreToRpdMapRpdRfChanIndex_Object = MibTableColumn
docsRphyRpdIfCoreToRpdMapRpdRfChanIndex = _DocsRphyRpdIfCoreToRpdMapRpdRfChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 6, 1, 5),
    _DocsRphyRpdIfCoreToRpdMapRpdRfChanIndex_Type()
)
docsRphyRpdIfCoreToRpdMapRpdRfChanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfCoreToRpdMapRpdRfChanIndex.setStatus("current")
_DocsRphyRpdIfRpdToCoreMapTable_Object = MibTable
docsRphyRpdIfRpdToCoreMapTable = _DocsRphyRpdIfRpdToCoreMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 7)
)
if mibBuilder.loadTexts:
    docsRphyRpdIfRpdToCoreMapTable.setStatus("current")
_DocsRphyRpdIfRpdToCoreMapEntry_Object = MibTableRow
docsRphyRpdIfRpdToCoreMapEntry = _DocsRphyRpdIfRpdToCoreMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 7, 1)
)
docsRphyRpdIfRpdToCoreMapEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdIfRpdToCoreMapRpdRfPortDirection"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdIfRpdToCoreMapRpdRfPortIndex"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdIfRpdToCoreMapRpdRfChanType"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdIfRpdToCoreMapRpdRfChanIndex"),
)
if mibBuilder.loadTexts:
    docsRphyRpdIfRpdToCoreMapEntry.setStatus("current")
_DocsRphyRpdIfRpdToCoreMapRpdRfPortDirection_Type = IfDirection
_DocsRphyRpdIfRpdToCoreMapRpdRfPortDirection_Object = MibTableColumn
docsRphyRpdIfRpdToCoreMapRpdRfPortDirection = _DocsRphyRpdIfRpdToCoreMapRpdRfPortDirection_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 7, 1, 1),
    _DocsRphyRpdIfRpdToCoreMapRpdRfPortDirection_Type()
)
docsRphyRpdIfRpdToCoreMapRpdRfPortDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdIfRpdToCoreMapRpdRfPortDirection.setStatus("current")


class _DocsRphyRpdIfRpdToCoreMapRpdRfPortIndex_Type(Unsigned32):
    """Custom type docsRphyRpdIfRpdToCoreMapRpdRfPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyRpdIfRpdToCoreMapRpdRfPortIndex_Type.__name__ = "Unsigned32"
_DocsRphyRpdIfRpdToCoreMapRpdRfPortIndex_Object = MibTableColumn
docsRphyRpdIfRpdToCoreMapRpdRfPortIndex = _DocsRphyRpdIfRpdToCoreMapRpdRfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 7, 1, 2),
    _DocsRphyRpdIfRpdToCoreMapRpdRfPortIndex_Type()
)
docsRphyRpdIfRpdToCoreMapRpdRfPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdIfRpdToCoreMapRpdRfPortIndex.setStatus("current")
_DocsRphyRpdIfRpdToCoreMapRpdRfChanType_Type = RphyChannelType
_DocsRphyRpdIfRpdToCoreMapRpdRfChanType_Object = MibTableColumn
docsRphyRpdIfRpdToCoreMapRpdRfChanType = _DocsRphyRpdIfRpdToCoreMapRpdRfChanType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 7, 1, 3),
    _DocsRphyRpdIfRpdToCoreMapRpdRfChanType_Type()
)
docsRphyRpdIfRpdToCoreMapRpdRfChanType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdIfRpdToCoreMapRpdRfChanType.setStatus("current")


class _DocsRphyRpdIfRpdToCoreMapRpdRfChanIndex_Type(Unsigned32):
    """Custom type docsRphyRpdIfRpdToCoreMapRpdRfChanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyRpdIfRpdToCoreMapRpdRfChanIndex_Type.__name__ = "Unsigned32"
_DocsRphyRpdIfRpdToCoreMapRpdRfChanIndex_Object = MibTableColumn
docsRphyRpdIfRpdToCoreMapRpdRfChanIndex = _DocsRphyRpdIfRpdToCoreMapRpdRfChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 7, 1, 4),
    _DocsRphyRpdIfRpdToCoreMapRpdRfChanIndex_Type()
)
docsRphyRpdIfRpdToCoreMapRpdRfChanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdIfRpdToCoreMapRpdRfChanIndex.setStatus("current")
_DocsRphyRpdIfRpdToCoreMapCoreIfIndex_Type = InterfaceIndex
_DocsRphyRpdIfRpdToCoreMapCoreIfIndex_Object = MibTableColumn
docsRphyRpdIfRpdToCoreMapCoreIfIndex = _DocsRphyRpdIfRpdToCoreMapCoreIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 2, 7, 1, 5),
    _DocsRphyRpdIfRpdToCoreMapCoreIfIndex_Type()
)
docsRphyRpdIfRpdToCoreMapCoreIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIfRpdToCoreMapCoreIfIndex.setStatus("current")
_DocsRphyRpdIpMibObjects_ObjectIdentity = ObjectIdentity
docsRphyRpdIpMibObjects = _DocsRphyRpdIpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3)
)
_DocsRphyRpdIpv4GrpTable_Object = MibTable
docsRphyRpdIpv4GrpTable = _DocsRphyRpdIpv4GrpTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 1)
)
if mibBuilder.loadTexts:
    docsRphyRpdIpv4GrpTable.setStatus("current")
_DocsRphyRpdIpv4GrpEntry_Object = MibTableRow
docsRphyRpdIpv4GrpEntry = _DocsRphyRpdIpv4GrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 1, 1)
)
docsRphyRpdIpv4GrpEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
)
if mibBuilder.loadTexts:
    docsRphyRpdIpv4GrpEntry.setStatus("current")


class _DocsRphyRpdIpv4GrpDefaultTTL_Type(Integer32):
    """Custom type docsRphyRpdIpv4GrpDefaultTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DocsRphyRpdIpv4GrpDefaultTTL_Type.__name__ = "Integer32"
_DocsRphyRpdIpv4GrpDefaultTTL_Object = MibTableColumn
docsRphyRpdIpv4GrpDefaultTTL = _DocsRphyRpdIpv4GrpDefaultTTL_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 1, 1, 1),
    _DocsRphyRpdIpv4GrpDefaultTTL_Type()
)
docsRphyRpdIpv4GrpDefaultTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpv4GrpDefaultTTL.setStatus("current")
_DocsRphyRpdIpv4GrpInterfaceTableLastChange_Type = TimeStamp
_DocsRphyRpdIpv4GrpInterfaceTableLastChange_Object = MibTableColumn
docsRphyRpdIpv4GrpInterfaceTableLastChange = _DocsRphyRpdIpv4GrpInterfaceTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 1, 1, 2),
    _DocsRphyRpdIpv4GrpInterfaceTableLastChange_Type()
)
docsRphyRpdIpv4GrpInterfaceTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpv4GrpInterfaceTableLastChange.setStatus("current")
_DocsRphyRpdIpv6GrpTable_Object = MibTable
docsRphyRpdIpv6GrpTable = _DocsRphyRpdIpv6GrpTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 2)
)
if mibBuilder.loadTexts:
    docsRphyRpdIpv6GrpTable.setStatus("current")
_DocsRphyRpdIpv6GrpEntry_Object = MibTableRow
docsRphyRpdIpv6GrpEntry = _DocsRphyRpdIpv6GrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 2, 1)
)
docsRphyRpdIpv6GrpEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
)
if mibBuilder.loadTexts:
    docsRphyRpdIpv6GrpEntry.setStatus("current")


class _DocsRphyRpdIpv6GrpIpDefaultHopLimit_Type(Integer32):
    """Custom type docsRphyRpdIpv6GrpIpDefaultHopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyRpdIpv6GrpIpDefaultHopLimit_Type.__name__ = "Integer32"
_DocsRphyRpdIpv6GrpIpDefaultHopLimit_Object = MibTableColumn
docsRphyRpdIpv6GrpIpDefaultHopLimit = _DocsRphyRpdIpv6GrpIpDefaultHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 2, 1, 1),
    _DocsRphyRpdIpv6GrpIpDefaultHopLimit_Type()
)
docsRphyRpdIpv6GrpIpDefaultHopLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpv6GrpIpDefaultHopLimit.setStatus("current")
_DocsRphyRpdIpv6GrpInterfaceTableLastChange_Type = TimeStamp
_DocsRphyRpdIpv6GrpInterfaceTableLastChange_Object = MibTableColumn
docsRphyRpdIpv6GrpInterfaceTableLastChange = _DocsRphyRpdIpv6GrpInterfaceTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 2, 1, 2),
    _DocsRphyRpdIpv6GrpInterfaceTableLastChange_Type()
)
docsRphyRpdIpv6GrpInterfaceTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpv6GrpInterfaceTableLastChange.setStatus("current")
_DocsRphyRpdIpv6GrpIfStatsTableLastChange_Type = TimeStamp
_DocsRphyRpdIpv6GrpIfStatsTableLastChange_Object = MibTableColumn
docsRphyRpdIpv6GrpIfStatsTableLastChange = _DocsRphyRpdIpv6GrpIfStatsTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 2, 1, 3),
    _DocsRphyRpdIpv6GrpIfStatsTableLastChange_Type()
)
docsRphyRpdIpv6GrpIfStatsTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpv6GrpIfStatsTableLastChange.setStatus("current")
_DocsRphyRpdIpv4InterfaceTable_Object = MibTable
docsRphyRpdIpv4InterfaceTable = _DocsRphyRpdIpv4InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 3)
)
if mibBuilder.loadTexts:
    docsRphyRpdIpv4InterfaceTable.setStatus("current")
_DocsRphyRpdIpv4InterfaceEntry_Object = MibTableRow
docsRphyRpdIpv4InterfaceEntry = _DocsRphyRpdIpv4InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 3, 1)
)
docsRphyRpdIpv4InterfaceEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdIfEnetPortIndex"),
)
if mibBuilder.loadTexts:
    docsRphyRpdIpv4InterfaceEntry.setStatus("current")


class _DocsRphyRpdIpv4InterfaceEnableStatus_Type(Integer32):
    """Custom type docsRphyRpdIpv4InterfaceEnableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_DocsRphyRpdIpv4InterfaceEnableStatus_Type.__name__ = "Integer32"
_DocsRphyRpdIpv4InterfaceEnableStatus_Object = MibTableColumn
docsRphyRpdIpv4InterfaceEnableStatus = _DocsRphyRpdIpv4InterfaceEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 3, 1, 1),
    _DocsRphyRpdIpv4InterfaceEnableStatus_Type()
)
docsRphyRpdIpv4InterfaceEnableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpv4InterfaceEnableStatus.setStatus("current")
_DocsRphyRpdIpv4InterfaceRetransmitTime_Type = Unsigned32
_DocsRphyRpdIpv4InterfaceRetransmitTime_Object = MibTableColumn
docsRphyRpdIpv4InterfaceRetransmitTime = _DocsRphyRpdIpv4InterfaceRetransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 3, 1, 2),
    _DocsRphyRpdIpv4InterfaceRetransmitTime_Type()
)
docsRphyRpdIpv4InterfaceRetransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpv4InterfaceRetransmitTime.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyRpdIpv4InterfaceRetransmitTime.setUnits("milliseconds")
_DocsRphyRpdIpv6InterfaceTable_Object = MibTable
docsRphyRpdIpv6InterfaceTable = _DocsRphyRpdIpv6InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 4)
)
if mibBuilder.loadTexts:
    docsRphyRpdIpv6InterfaceTable.setStatus("current")
_DocsRphyRpdIpv6InterfaceEntry_Object = MibTableRow
docsRphyRpdIpv6InterfaceEntry = _DocsRphyRpdIpv6InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 4, 1)
)
docsRphyRpdIpv6InterfaceEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdIfEnetPortIndex"),
)
if mibBuilder.loadTexts:
    docsRphyRpdIpv6InterfaceEntry.setStatus("current")
_DocsRphyRpdIpv6InterfaceIdentifier_Type = Ipv6AddressIfIdentifierTC
_DocsRphyRpdIpv6InterfaceIdentifier_Object = MibTableColumn
docsRphyRpdIpv6InterfaceIdentifier = _DocsRphyRpdIpv6InterfaceIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 4, 1, 1),
    _DocsRphyRpdIpv6InterfaceIdentifier_Type()
)
docsRphyRpdIpv6InterfaceIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpv6InterfaceIdentifier.setStatus("current")


class _DocsRphyRpdIpv6InterfaceEnableStatus_Type(Integer32):
    """Custom type docsRphyRpdIpv6InterfaceEnableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_DocsRphyRpdIpv6InterfaceEnableStatus_Type.__name__ = "Integer32"
_DocsRphyRpdIpv6InterfaceEnableStatus_Object = MibTableColumn
docsRphyRpdIpv6InterfaceEnableStatus = _DocsRphyRpdIpv6InterfaceEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 4, 1, 2),
    _DocsRphyRpdIpv6InterfaceEnableStatus_Type()
)
docsRphyRpdIpv6InterfaceEnableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpv6InterfaceEnableStatus.setStatus("current")
_DocsRphyRpdIpv6InterfaceReachableTime_Type = Unsigned32
_DocsRphyRpdIpv6InterfaceReachableTime_Object = MibTableColumn
docsRphyRpdIpv6InterfaceReachableTime = _DocsRphyRpdIpv6InterfaceReachableTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 4, 1, 3),
    _DocsRphyRpdIpv6InterfaceReachableTime_Type()
)
docsRphyRpdIpv6InterfaceReachableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpv6InterfaceReachableTime.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyRpdIpv6InterfaceReachableTime.setUnits("milliseconds")
_DocsRphyRpdIpv6InterfaceRetransmitTime_Type = Unsigned32
_DocsRphyRpdIpv6InterfaceRetransmitTime_Object = MibTableColumn
docsRphyRpdIpv6InterfaceRetransmitTime = _DocsRphyRpdIpv6InterfaceRetransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 4, 1, 4),
    _DocsRphyRpdIpv6InterfaceRetransmitTime_Type()
)
docsRphyRpdIpv6InterfaceRetransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpv6InterfaceRetransmitTime.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyRpdIpv6InterfaceRetransmitTime.setUnits("milliseconds")
_DocsRphyRpdIpIfStatsTable_Object = MibTable
docsRphyRpdIpIfStatsTable = _DocsRphyRpdIpIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 5)
)
if mibBuilder.loadTexts:
    docsRphyRpdIpIfStatsTable.setStatus("current")
_DocsRphyRpdIpIfStatsEntry_Object = MibTableRow
docsRphyRpdIpIfStatsEntry = _DocsRphyRpdIpIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 5, 1)
)
docsRphyRpdIpIfStatsEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdIpIfStatsIPVersion"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdIfEnetPortIndex"),
)
if mibBuilder.loadTexts:
    docsRphyRpdIpIfStatsEntry.setStatus("current")
_DocsRphyRpdIpIfStatsIPVersion_Type = InetVersion
_DocsRphyRpdIpIfStatsIPVersion_Object = MibTableColumn
docsRphyRpdIpIfStatsIPVersion = _DocsRphyRpdIpIfStatsIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 5, 1, 1),
    _DocsRphyRpdIpIfStatsIPVersion_Type()
)
docsRphyRpdIpIfStatsIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdIpIfStatsIPVersion.setStatus("current")
_DocsRphyRpdIpIfStatsInReceives_Type = Counter64
_DocsRphyRpdIpIfStatsInReceives_Object = MibTableColumn
docsRphyRpdIpIfStatsInReceives = _DocsRphyRpdIpIfStatsInReceives_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 5, 1, 2),
    _DocsRphyRpdIpIfStatsInReceives_Type()
)
docsRphyRpdIpIfStatsInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpIfStatsInReceives.setStatus("current")
_DocsRphyRpdIpIfStatsInOctets_Type = Counter64
_DocsRphyRpdIpIfStatsInOctets_Object = MibTableColumn
docsRphyRpdIpIfStatsInOctets = _DocsRphyRpdIpIfStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 5, 1, 3),
    _DocsRphyRpdIpIfStatsInOctets_Type()
)
docsRphyRpdIpIfStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpIfStatsInOctets.setStatus("current")
_DocsRphyRpdIpIfStatsInHdrErrors_Type = Counter64
_DocsRphyRpdIpIfStatsInHdrErrors_Object = MibTableColumn
docsRphyRpdIpIfStatsInHdrErrors = _DocsRphyRpdIpIfStatsInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 5, 1, 4),
    _DocsRphyRpdIpIfStatsInHdrErrors_Type()
)
docsRphyRpdIpIfStatsInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpIfStatsInHdrErrors.setStatus("current")
_DocsRphyRpdIpIfStatsInNoRoutes_Type = Counter64
_DocsRphyRpdIpIfStatsInNoRoutes_Object = MibTableColumn
docsRphyRpdIpIfStatsInNoRoutes = _DocsRphyRpdIpIfStatsInNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 5, 1, 5),
    _DocsRphyRpdIpIfStatsInNoRoutes_Type()
)
docsRphyRpdIpIfStatsInNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpIfStatsInNoRoutes.setStatus("current")
_DocsRphyRpdIpIfStatsInAddrErrors_Type = Counter64
_DocsRphyRpdIpIfStatsInAddrErrors_Object = MibTableColumn
docsRphyRpdIpIfStatsInAddrErrors = _DocsRphyRpdIpIfStatsInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 5, 1, 6),
    _DocsRphyRpdIpIfStatsInAddrErrors_Type()
)
docsRphyRpdIpIfStatsInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpIfStatsInAddrErrors.setStatus("current")
_DocsRphyRpdIpIfStatsInUnknownProtos_Type = Counter64
_DocsRphyRpdIpIfStatsInUnknownProtos_Object = MibTableColumn
docsRphyRpdIpIfStatsInUnknownProtos = _DocsRphyRpdIpIfStatsInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 5, 1, 7),
    _DocsRphyRpdIpIfStatsInUnknownProtos_Type()
)
docsRphyRpdIpIfStatsInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpIfStatsInUnknownProtos.setStatus("current")
_DocsRphyRpdIpIfStatsInTruncatedPkts_Type = Counter64
_DocsRphyRpdIpIfStatsInTruncatedPkts_Object = MibTableColumn
docsRphyRpdIpIfStatsInTruncatedPkts = _DocsRphyRpdIpIfStatsInTruncatedPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 5, 1, 8),
    _DocsRphyRpdIpIfStatsInTruncatedPkts_Type()
)
docsRphyRpdIpIfStatsInTruncatedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpIfStatsInTruncatedPkts.setStatus("current")
_DocsRphyRpdIpIfStatsInDiscards_Type = Counter64
_DocsRphyRpdIpIfStatsInDiscards_Object = MibTableColumn
docsRphyRpdIpIfStatsInDiscards = _DocsRphyRpdIpIfStatsInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 5, 1, 9),
    _DocsRphyRpdIpIfStatsInDiscards_Type()
)
docsRphyRpdIpIfStatsInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpIfStatsInDiscards.setStatus("current")
_DocsRphyRpdIpIfStatsInDelivers_Type = Counter64
_DocsRphyRpdIpIfStatsInDelivers_Object = MibTableColumn
docsRphyRpdIpIfStatsInDelivers = _DocsRphyRpdIpIfStatsInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 5, 1, 10),
    _DocsRphyRpdIpIfStatsInDelivers_Type()
)
docsRphyRpdIpIfStatsInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpIfStatsInDelivers.setStatus("current")
_DocsRphyRpdIpIfStatsOutRequests_Type = Counter64
_DocsRphyRpdIpIfStatsOutRequests_Object = MibTableColumn
docsRphyRpdIpIfStatsOutRequests = _DocsRphyRpdIpIfStatsOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 5, 1, 11),
    _DocsRphyRpdIpIfStatsOutRequests_Type()
)
docsRphyRpdIpIfStatsOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpIfStatsOutRequests.setStatus("current")
_DocsRphyRpdIpIfStatsOutDiscards_Type = Counter64
_DocsRphyRpdIpIfStatsOutDiscards_Object = MibTableColumn
docsRphyRpdIpIfStatsOutDiscards = _DocsRphyRpdIpIfStatsOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 5, 1, 12),
    _DocsRphyRpdIpIfStatsOutDiscards_Type()
)
docsRphyRpdIpIfStatsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpIfStatsOutDiscards.setStatus("current")
_DocsRphyRpdIpIfStatsOutTransmits_Type = Counter64
_DocsRphyRpdIpIfStatsOutTransmits_Object = MibTableColumn
docsRphyRpdIpIfStatsOutTransmits = _DocsRphyRpdIpIfStatsOutTransmits_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 5, 1, 13),
    _DocsRphyRpdIpIfStatsOutTransmits_Type()
)
docsRphyRpdIpIfStatsOutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpIfStatsOutTransmits.setStatus("current")
_DocsRphyRpdIpIfStatsOutOctets_Type = Counter64
_DocsRphyRpdIpIfStatsOutOctets_Object = MibTableColumn
docsRphyRpdIpIfStatsOutOctets = _DocsRphyRpdIpIfStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 5, 1, 14),
    _DocsRphyRpdIpIfStatsOutOctets_Type()
)
docsRphyRpdIpIfStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpIfStatsOutOctets.setStatus("current")
_DocsRphyRpdIpIfStatsInMcastPkts_Type = Counter64
_DocsRphyRpdIpIfStatsInMcastPkts_Object = MibTableColumn
docsRphyRpdIpIfStatsInMcastPkts = _DocsRphyRpdIpIfStatsInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 5, 1, 15),
    _DocsRphyRpdIpIfStatsInMcastPkts_Type()
)
docsRphyRpdIpIfStatsInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpIfStatsInMcastPkts.setStatus("current")
_DocsRphyRpdIpIfStatsInMcastOctets_Type = Counter64
_DocsRphyRpdIpIfStatsInMcastOctets_Object = MibTableColumn
docsRphyRpdIpIfStatsInMcastOctets = _DocsRphyRpdIpIfStatsInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 5, 1, 16),
    _DocsRphyRpdIpIfStatsInMcastOctets_Type()
)
docsRphyRpdIpIfStatsInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpIfStatsInMcastOctets.setStatus("current")
_DocsRphyRpdIpIfStatsOutMcastPkts_Type = Counter64
_DocsRphyRpdIpIfStatsOutMcastPkts_Object = MibTableColumn
docsRphyRpdIpIfStatsOutMcastPkts = _DocsRphyRpdIpIfStatsOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 5, 1, 17),
    _DocsRphyRpdIpIfStatsOutMcastPkts_Type()
)
docsRphyRpdIpIfStatsOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpIfStatsOutMcastPkts.setStatus("current")
_DocsRphyRpdIpIfStatsOutMcastOctets_Type = Counter64
_DocsRphyRpdIpIfStatsOutMcastOctets_Object = MibTableColumn
docsRphyRpdIpIfStatsOutMcastOctets = _DocsRphyRpdIpIfStatsOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 5, 1, 18),
    _DocsRphyRpdIpIfStatsOutMcastOctets_Type()
)
docsRphyRpdIpIfStatsOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpIfStatsOutMcastOctets.setStatus("current")
_DocsRphyRpdIpIfStatsDiscontinuityTime_Type = TimeStamp
_DocsRphyRpdIpIfStatsDiscontinuityTime_Object = MibTableColumn
docsRphyRpdIpIfStatsDiscontinuityTime = _DocsRphyRpdIpIfStatsDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 5, 1, 19),
    _DocsRphyRpdIpIfStatsDiscontinuityTime_Type()
)
docsRphyRpdIpIfStatsDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpIfStatsDiscontinuityTime.setStatus("current")
_DocsRphyRpdIpIfStatsRefreshRate_Type = Unsigned32
_DocsRphyRpdIpIfStatsRefreshRate_Object = MibTableColumn
docsRphyRpdIpIfStatsRefreshRate = _DocsRphyRpdIpIfStatsRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 5, 1, 20),
    _DocsRphyRpdIpIfStatsRefreshRate_Type()
)
docsRphyRpdIpIfStatsRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpIfStatsRefreshRate.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyRpdIpIfStatsRefreshRate.setUnits("milli-seconds")
_DocsRphyRpdIpAddressTable_Object = MibTable
docsRphyRpdIpAddressTable = _DocsRphyRpdIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 6)
)
if mibBuilder.loadTexts:
    docsRphyRpdIpAddressTable.setStatus("current")
_DocsRphyRpdIpAddressEntry_Object = MibTableRow
docsRphyRpdIpAddressEntry = _DocsRphyRpdIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 6, 1)
)
docsRphyRpdIpAddressEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdIpAddressAddrType"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdIpAddressAddr"),
)
if mibBuilder.loadTexts:
    docsRphyRpdIpAddressEntry.setStatus("current")
_DocsRphyRpdIpAddressAddrType_Type = InetAddressType
_DocsRphyRpdIpAddressAddrType_Object = MibTableColumn
docsRphyRpdIpAddressAddrType = _DocsRphyRpdIpAddressAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 6, 1, 1),
    _DocsRphyRpdIpAddressAddrType_Type()
)
docsRphyRpdIpAddressAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdIpAddressAddrType.setStatus("current")
_DocsRphyRpdIpAddressAddr_Type = InetAddress
_DocsRphyRpdIpAddressAddr_Object = MibTableColumn
docsRphyRpdIpAddressAddr = _DocsRphyRpdIpAddressAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 6, 1, 2),
    _DocsRphyRpdIpAddressAddr_Type()
)
docsRphyRpdIpAddressAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdIpAddressAddr.setStatus("current")


class _DocsRphyRpdIpAddressEnetPortIndex_Type(Unsigned32):
    """Custom type docsRphyRpdIpAddressEnetPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyRpdIpAddressEnetPortIndex_Type.__name__ = "Unsigned32"
_DocsRphyRpdIpAddressEnetPortIndex_Object = MibTableColumn
docsRphyRpdIpAddressEnetPortIndex = _DocsRphyRpdIpAddressEnetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 6, 1, 3),
    _DocsRphyRpdIpAddressEnetPortIndex_Type()
)
docsRphyRpdIpAddressEnetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpAddressEnetPortIndex.setStatus("current")


class _DocsRphyRpdIpAddressType_Type(Integer32):
    """Custom type docsRphyRpdIpAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("anycast", 2),
          ("broadcast", 3),
          ("unicast", 1))
    )


_DocsRphyRpdIpAddressType_Type.__name__ = "Integer32"
_DocsRphyRpdIpAddressType_Object = MibTableColumn
docsRphyRpdIpAddressType = _DocsRphyRpdIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 6, 1, 4),
    _DocsRphyRpdIpAddressType_Type()
)
docsRphyRpdIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpAddressType.setStatus("current")
_DocsRphyRpdIpAddressPrefixLen_Type = InetAddressPrefixLength
_DocsRphyRpdIpAddressPrefixLen_Object = MibTableColumn
docsRphyRpdIpAddressPrefixLen = _DocsRphyRpdIpAddressPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 6, 1, 5),
    _DocsRphyRpdIpAddressPrefixLen_Type()
)
docsRphyRpdIpAddressPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpAddressPrefixLen.setStatus("current")
_DocsRphyRpdIpAddressOrigin_Type = IpAddressOriginTC
_DocsRphyRpdIpAddressOrigin_Object = MibTableColumn
docsRphyRpdIpAddressOrigin = _DocsRphyRpdIpAddressOrigin_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 6, 1, 6),
    _DocsRphyRpdIpAddressOrigin_Type()
)
docsRphyRpdIpAddressOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpAddressOrigin.setStatus("current")
_DocsRphyRpdIpAddressStatus_Type = IpAddressStatusTC
_DocsRphyRpdIpAddressStatus_Object = MibTableColumn
docsRphyRpdIpAddressStatus = _DocsRphyRpdIpAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 6, 1, 7),
    _DocsRphyRpdIpAddressStatus_Type()
)
docsRphyRpdIpAddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpAddressStatus.setStatus("current")
_DocsRphyRpdIpAddressCreated_Type = TimeStamp
_DocsRphyRpdIpAddressCreated_Object = MibTableColumn
docsRphyRpdIpAddressCreated = _DocsRphyRpdIpAddressCreated_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 6, 1, 8),
    _DocsRphyRpdIpAddressCreated_Type()
)
docsRphyRpdIpAddressCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpAddressCreated.setStatus("current")
_DocsRphyRpdIpAddressLastChanged_Type = TimeStamp
_DocsRphyRpdIpAddressLastChanged_Object = MibTableColumn
docsRphyRpdIpAddressLastChanged = _DocsRphyRpdIpAddressLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 6, 1, 9),
    _DocsRphyRpdIpAddressLastChanged_Type()
)
docsRphyRpdIpAddressLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpAddressLastChanged.setStatus("current")
_DocsRphyRpdIpNetToPhysicalTable_Object = MibTable
docsRphyRpdIpNetToPhysicalTable = _DocsRphyRpdIpNetToPhysicalTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 7)
)
if mibBuilder.loadTexts:
    docsRphyRpdIpNetToPhysicalTable.setStatus("current")
_DocsRphyRpdIpNetToPhysicalEntry_Object = MibTableRow
docsRphyRpdIpNetToPhysicalEntry = _DocsRphyRpdIpNetToPhysicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 7, 1)
)
docsRphyRpdIpNetToPhysicalEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdIfEnetPortIndex"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdIpNetToPhysicalNetAddressType"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdIpNetToPhysicalNetAddress"),
)
if mibBuilder.loadTexts:
    docsRphyRpdIpNetToPhysicalEntry.setStatus("current")
_DocsRphyRpdIpNetToPhysicalNetAddressType_Type = InetAddressType
_DocsRphyRpdIpNetToPhysicalNetAddressType_Object = MibTableColumn
docsRphyRpdIpNetToPhysicalNetAddressType = _DocsRphyRpdIpNetToPhysicalNetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 7, 1, 1),
    _DocsRphyRpdIpNetToPhysicalNetAddressType_Type()
)
docsRphyRpdIpNetToPhysicalNetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdIpNetToPhysicalNetAddressType.setStatus("current")
_DocsRphyRpdIpNetToPhysicalNetAddress_Type = InetAddress
_DocsRphyRpdIpNetToPhysicalNetAddress_Object = MibTableColumn
docsRphyRpdIpNetToPhysicalNetAddress = _DocsRphyRpdIpNetToPhysicalNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 7, 1, 2),
    _DocsRphyRpdIpNetToPhysicalNetAddress_Type()
)
docsRphyRpdIpNetToPhysicalNetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdIpNetToPhysicalNetAddress.setStatus("current")


class _DocsRphyRpdIpNetToPhysicalPhysAddress_Type(PhysAddress):
    """Custom type docsRphyRpdIpNetToPhysicalPhysAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_DocsRphyRpdIpNetToPhysicalPhysAddress_Type.__name__ = "PhysAddress"
_DocsRphyRpdIpNetToPhysicalPhysAddress_Object = MibTableColumn
docsRphyRpdIpNetToPhysicalPhysAddress = _DocsRphyRpdIpNetToPhysicalPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 7, 1, 3),
    _DocsRphyRpdIpNetToPhysicalPhysAddress_Type()
)
docsRphyRpdIpNetToPhysicalPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpNetToPhysicalPhysAddress.setStatus("current")
_DocsRphyRpdIpNetToPhysicalLastUpdated_Type = TimeStamp
_DocsRphyRpdIpNetToPhysicalLastUpdated_Object = MibTableColumn
docsRphyRpdIpNetToPhysicalLastUpdated = _DocsRphyRpdIpNetToPhysicalLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 7, 1, 4),
    _DocsRphyRpdIpNetToPhysicalLastUpdated_Type()
)
docsRphyRpdIpNetToPhysicalLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpNetToPhysicalLastUpdated.setStatus("current")


class _DocsRphyRpdIpNetToPhysicalType_Type(Integer32):
    """Custom type docsRphyRpdIpNetToPhysicalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 3),
          ("invalid", 2),
          ("local", 5),
          ("other", 1),
          ("static", 4))
    )


_DocsRphyRpdIpNetToPhysicalType_Type.__name__ = "Integer32"
_DocsRphyRpdIpNetToPhysicalType_Object = MibTableColumn
docsRphyRpdIpNetToPhysicalType = _DocsRphyRpdIpNetToPhysicalType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 7, 1, 5),
    _DocsRphyRpdIpNetToPhysicalType_Type()
)
docsRphyRpdIpNetToPhysicalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpNetToPhysicalType.setStatus("current")


class _DocsRphyRpdIpNetToPhysicalState_Type(Integer32):
    """Custom type docsRphyRpdIpNetToPhysicalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("delay", 3),
          ("incomplete", 7),
          ("invalid", 5),
          ("probe", 4),
          ("reachable", 1),
          ("stale", 2),
          ("unknown", 6))
    )


_DocsRphyRpdIpNetToPhysicalState_Type.__name__ = "Integer32"
_DocsRphyRpdIpNetToPhysicalState_Object = MibTableColumn
docsRphyRpdIpNetToPhysicalState = _DocsRphyRpdIpNetToPhysicalState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 7, 1, 6),
    _DocsRphyRpdIpNetToPhysicalState_Type()
)
docsRphyRpdIpNetToPhysicalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpNetToPhysicalState.setStatus("current")
_DocsRphyRpdIpDefaultRouterTable_Object = MibTable
docsRphyRpdIpDefaultRouterTable = _DocsRphyRpdIpDefaultRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 8)
)
if mibBuilder.loadTexts:
    docsRphyRpdIpDefaultRouterTable.setStatus("current")
_DocsRphyRpdIpDefaultRouterEntry_Object = MibTableRow
docsRphyRpdIpDefaultRouterEntry = _DocsRphyRpdIpDefaultRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 8, 1)
)
docsRphyRpdIpDefaultRouterEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdIpDefaultRouterAddressType"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdIpDefaultRouterAddress"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdIfEnetPortIndex"),
)
if mibBuilder.loadTexts:
    docsRphyRpdIpDefaultRouterEntry.setStatus("current")
_DocsRphyRpdIpDefaultRouterAddressType_Type = InetAddressType
_DocsRphyRpdIpDefaultRouterAddressType_Object = MibTableColumn
docsRphyRpdIpDefaultRouterAddressType = _DocsRphyRpdIpDefaultRouterAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 8, 1, 1),
    _DocsRphyRpdIpDefaultRouterAddressType_Type()
)
docsRphyRpdIpDefaultRouterAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdIpDefaultRouterAddressType.setStatus("current")
_DocsRphyRpdIpDefaultRouterAddress_Type = InetAddress
_DocsRphyRpdIpDefaultRouterAddress_Object = MibTableColumn
docsRphyRpdIpDefaultRouterAddress = _DocsRphyRpdIpDefaultRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 8, 1, 2),
    _DocsRphyRpdIpDefaultRouterAddress_Type()
)
docsRphyRpdIpDefaultRouterAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdIpDefaultRouterAddress.setStatus("current")


class _DocsRphyRpdIpDefaultRouterLifetime_Type(Unsigned32):
    """Custom type docsRphyRpdIpDefaultRouterLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyRpdIpDefaultRouterLifetime_Type.__name__ = "Unsigned32"
_DocsRphyRpdIpDefaultRouterLifetime_Object = MibTableColumn
docsRphyRpdIpDefaultRouterLifetime = _DocsRphyRpdIpDefaultRouterLifetime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 8, 1, 3),
    _DocsRphyRpdIpDefaultRouterLifetime_Type()
)
docsRphyRpdIpDefaultRouterLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpDefaultRouterLifetime.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyRpdIpDefaultRouterLifetime.setUnits("seconds")


class _DocsRphyRpdIpDefaultRouterPreference_Type(Integer32):
    """Custom type docsRphyRpdIpDefaultRouterPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", -1),
          ("medium", 0),
          ("reserved", -2))
    )


_DocsRphyRpdIpDefaultRouterPreference_Type.__name__ = "Integer32"
_DocsRphyRpdIpDefaultRouterPreference_Object = MibTableColumn
docsRphyRpdIpDefaultRouterPreference = _DocsRphyRpdIpDefaultRouterPreference_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 8, 1, 4),
    _DocsRphyRpdIpDefaultRouterPreference_Type()
)
docsRphyRpdIpDefaultRouterPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpDefaultRouterPreference.setStatus("current")
_DocsRphyRpdIpIcmpMibObjects_ObjectIdentity = ObjectIdentity
docsRphyRpdIpIcmpMibObjects = _DocsRphyRpdIpIcmpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 9)
)
_DocsRphyRpdIpIcmpMsgStatsTable_Object = MibTable
docsRphyRpdIpIcmpMsgStatsTable = _DocsRphyRpdIpIcmpMsgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 9, 1)
)
if mibBuilder.loadTexts:
    docsRphyRpdIpIcmpMsgStatsTable.setStatus("current")
_DocsRphyRpdIpIcmpMsgStatsEntry_Object = MibTableRow
docsRphyRpdIpIcmpMsgStatsEntry = _DocsRphyRpdIpIcmpMsgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 9, 1, 1)
)
docsRphyRpdIpIcmpMsgStatsEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdIpIcmpMsgStatsIPVersion"),
    (0, "DOCS-RPHY-MIB", "docsRphyRpdIpIcmpMsgStatsType"),
)
if mibBuilder.loadTexts:
    docsRphyRpdIpIcmpMsgStatsEntry.setStatus("current")
_DocsRphyRpdIpIcmpMsgStatsIPVersion_Type = InetVersion
_DocsRphyRpdIpIcmpMsgStatsIPVersion_Object = MibTableColumn
docsRphyRpdIpIcmpMsgStatsIPVersion = _DocsRphyRpdIpIcmpMsgStatsIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 9, 1, 1, 1),
    _DocsRphyRpdIpIcmpMsgStatsIPVersion_Type()
)
docsRphyRpdIpIcmpMsgStatsIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdIpIcmpMsgStatsIPVersion.setStatus("current")


class _DocsRphyRpdIpIcmpMsgStatsType_Type(Integer32):
    """Custom type docsRphyRpdIpIcmpMsgStatsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyRpdIpIcmpMsgStatsType_Type.__name__ = "Integer32"
_DocsRphyRpdIpIcmpMsgStatsType_Object = MibTableColumn
docsRphyRpdIpIcmpMsgStatsType = _DocsRphyRpdIpIcmpMsgStatsType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 9, 1, 1, 2),
    _DocsRphyRpdIpIcmpMsgStatsType_Type()
)
docsRphyRpdIpIcmpMsgStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdIpIcmpMsgStatsType.setStatus("current")
_DocsRphyRpdIpIcmpMsgStatsInPkts_Type = Counter64
_DocsRphyRpdIpIcmpMsgStatsInPkts_Object = MibTableColumn
docsRphyRpdIpIcmpMsgStatsInPkts = _DocsRphyRpdIpIcmpMsgStatsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 9, 1, 1, 3),
    _DocsRphyRpdIpIcmpMsgStatsInPkts_Type()
)
docsRphyRpdIpIcmpMsgStatsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpIcmpMsgStatsInPkts.setStatus("current")
_DocsRphyRpdIpIcmpMsgStatsOutPkts_Type = Counter64
_DocsRphyRpdIpIcmpMsgStatsOutPkts_Object = MibTableColumn
docsRphyRpdIpIcmpMsgStatsOutPkts = _DocsRphyRpdIpIcmpMsgStatsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 3, 9, 1, 1, 4),
    _DocsRphyRpdIpIcmpMsgStatsOutPkts_Type()
)
docsRphyRpdIpIcmpMsgStatsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdIpIcmpMsgStatsOutPkts.setStatus("current")
_DocsRphyCcapMibObjects_ObjectIdentity = ObjectIdentity
docsRphyCcapMibObjects = _DocsRphyCcapMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4)
)
_DocsRphyCcapL2tpSessionInfoTable_Object = MibTable
docsRphyCcapL2tpSessionInfoTable = _DocsRphyCcapL2tpSessionInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 1)
)
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionInfoTable.setStatus("current")
_DocsRphyCcapL2tpSessionInfoEntry_Object = MibTableRow
docsRphyCcapL2tpSessionInfoEntry = _DocsRphyCcapL2tpSessionInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 1, 1)
)
docsRphyCcapL2tpSessionInfoEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoLocalLcceIpAddrType"),
    (0, "DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoLocalLcceIpAddr"),
    (0, "DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoLocalId"),
)
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionInfoEntry.setStatus("current")
_DocsRphyCcapL2tpSessionInfoLocalLcceIpAddrType_Type = InetAddressType
_DocsRphyCcapL2tpSessionInfoLocalLcceIpAddrType_Object = MibTableColumn
docsRphyCcapL2tpSessionInfoLocalLcceIpAddrType = _DocsRphyCcapL2tpSessionInfoLocalLcceIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 1, 1, 1),
    _DocsRphyCcapL2tpSessionInfoLocalLcceIpAddrType_Type()
)
docsRphyCcapL2tpSessionInfoLocalLcceIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionInfoLocalLcceIpAddrType.setStatus("current")
_DocsRphyCcapL2tpSessionInfoLocalLcceIpAddr_Type = InetAddress
_DocsRphyCcapL2tpSessionInfoLocalLcceIpAddr_Object = MibTableColumn
docsRphyCcapL2tpSessionInfoLocalLcceIpAddr = _DocsRphyCcapL2tpSessionInfoLocalLcceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 1, 1, 2),
    _DocsRphyCcapL2tpSessionInfoLocalLcceIpAddr_Type()
)
docsRphyCcapL2tpSessionInfoLocalLcceIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionInfoLocalLcceIpAddr.setStatus("current")
_DocsRphyCcapL2tpSessionInfoLocalId_Type = Unsigned32
_DocsRphyCcapL2tpSessionInfoLocalId_Object = MibTableColumn
docsRphyCcapL2tpSessionInfoLocalId = _DocsRphyCcapL2tpSessionInfoLocalId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 1, 1, 3),
    _DocsRphyCcapL2tpSessionInfoLocalId_Type()
)
docsRphyCcapL2tpSessionInfoLocalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionInfoLocalId.setStatus("current")
_DocsRphyCcapL2tpSessionInfoRemoteLcceIpAddrType_Type = InetAddressType
_DocsRphyCcapL2tpSessionInfoRemoteLcceIpAddrType_Object = MibTableColumn
docsRphyCcapL2tpSessionInfoRemoteLcceIpAddrType = _DocsRphyCcapL2tpSessionInfoRemoteLcceIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 1, 1, 4),
    _DocsRphyCcapL2tpSessionInfoRemoteLcceIpAddrType_Type()
)
docsRphyCcapL2tpSessionInfoRemoteLcceIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionInfoRemoteLcceIpAddrType.setStatus("current")
_DocsRphyCcapL2tpSessionInfoRemoteLcceIpAddr_Type = InetAddress
_DocsRphyCcapL2tpSessionInfoRemoteLcceIpAddr_Object = MibTableColumn
docsRphyCcapL2tpSessionInfoRemoteLcceIpAddr = _DocsRphyCcapL2tpSessionInfoRemoteLcceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 1, 1, 5),
    _DocsRphyCcapL2tpSessionInfoRemoteLcceIpAddr_Type()
)
docsRphyCcapL2tpSessionInfoRemoteLcceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionInfoRemoteLcceIpAddr.setStatus("current")
_DocsRphyCcapL2tpSessionInfoRemoteId_Type = Unsigned32
_DocsRphyCcapL2tpSessionInfoRemoteId_Object = MibTableColumn
docsRphyCcapL2tpSessionInfoRemoteId = _DocsRphyCcapL2tpSessionInfoRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 1, 1, 6),
    _DocsRphyCcapL2tpSessionInfoRemoteId_Type()
)
docsRphyCcapL2tpSessionInfoRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionInfoRemoteId.setStatus("current")
_DocsRphyCcapL2tpSessionInfoCoreId_Type = MacAddress
_DocsRphyCcapL2tpSessionInfoCoreId_Object = MibTableColumn
docsRphyCcapL2tpSessionInfoCoreId = _DocsRphyCcapL2tpSessionInfoCoreId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 1, 1, 7),
    _DocsRphyCcapL2tpSessionInfoCoreId_Type()
)
docsRphyCcapL2tpSessionInfoCoreId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionInfoCoreId.setStatus("current")
_DocsRphyCcapL2tpSessionInfoConnCtrlID_Type = Unsigned32
_DocsRphyCcapL2tpSessionInfoConnCtrlID_Object = MibTableColumn
docsRphyCcapL2tpSessionInfoConnCtrlID = _DocsRphyCcapL2tpSessionInfoConnCtrlID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 1, 1, 8),
    _DocsRphyCcapL2tpSessionInfoConnCtrlID_Type()
)
docsRphyCcapL2tpSessionInfoConnCtrlID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionInfoConnCtrlID.setStatus("current")
_DocsRphyCcapL2tpSessionInfoUdpPort_Type = InetPortNumber
_DocsRphyCcapL2tpSessionInfoUdpPort_Object = MibTableColumn
docsRphyCcapL2tpSessionInfoUdpPort = _DocsRphyCcapL2tpSessionInfoUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 1, 1, 9),
    _DocsRphyCcapL2tpSessionInfoUdpPort_Type()
)
docsRphyCcapL2tpSessionInfoUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionInfoUdpPort.setStatus("current")
_DocsRphyCcapL2tpSessionInfoDescr_Type = SnmpAdminString
_DocsRphyCcapL2tpSessionInfoDescr_Object = MibTableColumn
docsRphyCcapL2tpSessionInfoDescr = _DocsRphyCcapL2tpSessionInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 1, 1, 10),
    _DocsRphyCcapL2tpSessionInfoDescr_Type()
)
docsRphyCcapL2tpSessionInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionInfoDescr.setStatus("current")


class _DocsRphyCcapL2tpSessionInfoSessionType_Type(Integer32):
    """Custom type docsRphyCcapL2tpSessionInfoSessionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mpt", 2),
          ("psp", 1))
    )


_DocsRphyCcapL2tpSessionInfoSessionType_Type.__name__ = "Integer32"
_DocsRphyCcapL2tpSessionInfoSessionType_Object = MibTableColumn
docsRphyCcapL2tpSessionInfoSessionType = _DocsRphyCcapL2tpSessionInfoSessionType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 1, 1, 11),
    _DocsRphyCcapL2tpSessionInfoSessionType_Type()
)
docsRphyCcapL2tpSessionInfoSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionInfoSessionType.setStatus("current")


class _DocsRphyCcapL2tpSessionInfoSessionSubType_Type(Integer32):
    """Custom type docsRphyCcapL2tpSessionInfoSessionSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("mcm", 3),
          ("mptLegacy", 1),
          ("psp551Fwd", 16),
          ("psp551Ret", 17),
          ("psp552Fwd", 18),
          ("psp552Ret", 19),
          ("pspBwReqOfdma", 8),
          ("pspBwReqScQam", 7),
          ("pspDepiMultichannel", 4),
          ("pspLegacy", 2),
          ("pspMapOfdma", 13),
          ("pspMapScQam", 12),
          ("pspNdf", 20),
          ("pspNdr", 21),
          ("pspPnm", 15),
          ("pspProbe", 9),
          ("pspRngReqOfdma", 11),
          ("pspRngReqScQam", 10),
          ("pspSpecman", 14),
          ("pspUepiOfdma", 6),
          ("pspUepiScQam", 5))
    )


_DocsRphyCcapL2tpSessionInfoSessionSubType_Type.__name__ = "Integer32"
_DocsRphyCcapL2tpSessionInfoSessionSubType_Object = MibTableColumn
docsRphyCcapL2tpSessionInfoSessionSubType = _DocsRphyCcapL2tpSessionInfoSessionSubType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 1, 1, 12),
    _DocsRphyCcapL2tpSessionInfoSessionSubType_Type()
)
docsRphyCcapL2tpSessionInfoSessionSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionInfoSessionSubType.setStatus("current")
_DocsRphyCcapL2tpSessionInfoMaxPayload_Type = Unsigned32
_DocsRphyCcapL2tpSessionInfoMaxPayload_Object = MibTableColumn
docsRphyCcapL2tpSessionInfoMaxPayload = _DocsRphyCcapL2tpSessionInfoMaxPayload_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 1, 1, 13),
    _DocsRphyCcapL2tpSessionInfoMaxPayload_Type()
)
docsRphyCcapL2tpSessionInfoMaxPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionInfoMaxPayload.setStatus("current")
_DocsRphyCcapL2tpSessionInfoPathPayload_Type = Unsigned32
_DocsRphyCcapL2tpSessionInfoPathPayload_Object = MibTableColumn
docsRphyCcapL2tpSessionInfoPathPayload = _DocsRphyCcapL2tpSessionInfoPathPayload_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 1, 1, 14),
    _DocsRphyCcapL2tpSessionInfoPathPayload_Type()
)
docsRphyCcapL2tpSessionInfoPathPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionInfoPathPayload.setStatus("current")
_DocsRphyCcapL2tpSessionInfoRpdIfMtu_Type = Unsigned32
_DocsRphyCcapL2tpSessionInfoRpdIfMtu_Object = MibTableColumn
docsRphyCcapL2tpSessionInfoRpdIfMtu = _DocsRphyCcapL2tpSessionInfoRpdIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 1, 1, 15),
    _DocsRphyCcapL2tpSessionInfoRpdIfMtu_Type()
)
docsRphyCcapL2tpSessionInfoRpdIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionInfoRpdIfMtu.setStatus("current")
_DocsRphyCcapL2tpSessionInfoCoreIfMtu_Type = Unsigned32
_DocsRphyCcapL2tpSessionInfoCoreIfMtu_Object = MibTableColumn
docsRphyCcapL2tpSessionInfoCoreIfMtu = _DocsRphyCcapL2tpSessionInfoCoreIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 1, 1, 16),
    _DocsRphyCcapL2tpSessionInfoCoreIfMtu_Type()
)
docsRphyCcapL2tpSessionInfoCoreIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionInfoCoreIfMtu.setStatus("current")
_DocsRphyCcapL2tpSessionInfoIncludeDOCSISMsgs_Type = TruthValue
_DocsRphyCcapL2tpSessionInfoIncludeDOCSISMsgs_Object = MibTableColumn
docsRphyCcapL2tpSessionInfoIncludeDOCSISMsgs = _DocsRphyCcapL2tpSessionInfoIncludeDOCSISMsgs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 1, 1, 17),
    _DocsRphyCcapL2tpSessionInfoIncludeDOCSISMsgs_Type()
)
docsRphyCcapL2tpSessionInfoIncludeDOCSISMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionInfoIncludeDOCSISMsgs.setStatus("current")


class _DocsRphyCcapL2tpSessionInfoErrorCode_Type(Integer32):
    """Custom type docsRphyCcapL2tpSessionInfoErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ifAdminStatusSetToDown", 6),
          ("invalidInterfaceValue", 3),
          ("invalidMACInterfaceValue", 2),
          ("l2tpv3Error", 5),
          ("noResourcesForInterfaceIndex", 4),
          ("none", 1))
    )


_DocsRphyCcapL2tpSessionInfoErrorCode_Type.__name__ = "Integer32"
_DocsRphyCcapL2tpSessionInfoErrorCode_Object = MibTableColumn
docsRphyCcapL2tpSessionInfoErrorCode = _DocsRphyCcapL2tpSessionInfoErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 1, 1, 18),
    _DocsRphyCcapL2tpSessionInfoErrorCode_Type()
)
docsRphyCcapL2tpSessionInfoErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionInfoErrorCode.setStatus("current")
_DocsRphyCcapL2tpSessionInfoCreationTime_Type = TimeStamp
_DocsRphyCcapL2tpSessionInfoCreationTime_Object = MibTableColumn
docsRphyCcapL2tpSessionInfoCreationTime = _DocsRphyCcapL2tpSessionInfoCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 1, 1, 19),
    _DocsRphyCcapL2tpSessionInfoCreationTime_Type()
)
docsRphyCcapL2tpSessionInfoCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionInfoCreationTime.setStatus("current")


class _DocsRphyCcapL2tpSessionInfoOperStatus_Type(Integer32):
    """Custom type docsRphyCcapL2tpSessionInfoOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 3),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("other", 1),
          ("testing", 4),
          ("up", 2))
    )


_DocsRphyCcapL2tpSessionInfoOperStatus_Type.__name__ = "Integer32"
_DocsRphyCcapL2tpSessionInfoOperStatus_Object = MibTableColumn
docsRphyCcapL2tpSessionInfoOperStatus = _DocsRphyCcapL2tpSessionInfoOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 1, 1, 20),
    _DocsRphyCcapL2tpSessionInfoOperStatus_Type()
)
docsRphyCcapL2tpSessionInfoOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionInfoOperStatus.setStatus("current")


class _DocsRphyCcapL2tpSessionInfoLocalStatus_Type(Bits):
    """Custom type docsRphyCcapL2tpSessionInfoLocalStatus based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("psnPwRxFault", 4),
          ("psnPwTxFault", 5),
          ("pwNotForwarding", 1),
          ("servicePwRxFault", 2),
          ("servicePwTxFault", 3))
    )

_DocsRphyCcapL2tpSessionInfoLocalStatus_Type.__name__ = "Bits"
_DocsRphyCcapL2tpSessionInfoLocalStatus_Object = MibTableColumn
docsRphyCcapL2tpSessionInfoLocalStatus = _DocsRphyCcapL2tpSessionInfoLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 1, 1, 21),
    _DocsRphyCcapL2tpSessionInfoLocalStatus_Type()
)
docsRphyCcapL2tpSessionInfoLocalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionInfoLocalStatus.setStatus("current")
_DocsRphyCcapL2tpSessionInfoLastChange_Type = TimeTicks
_DocsRphyCcapL2tpSessionInfoLastChange_Object = MibTableColumn
docsRphyCcapL2tpSessionInfoLastChange = _DocsRphyCcapL2tpSessionInfoLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 1, 1, 22),
    _DocsRphyCcapL2tpSessionInfoLastChange_Type()
)
docsRphyCcapL2tpSessionInfoLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionInfoLastChange.setStatus("current")
_DocsRphyCcapL2tpSessionFlowTable_Object = MibTable
docsRphyCcapL2tpSessionFlowTable = _DocsRphyCcapL2tpSessionFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 2)
)
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionFlowTable.setStatus("current")
_DocsRphyCcapL2tpSessionFlowEntry_Object = MibTableRow
docsRphyCcapL2tpSessionFlowEntry = _DocsRphyCcapL2tpSessionFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 2, 1)
)
docsRphyCcapL2tpSessionFlowEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoLocalLcceIpAddrType"),
    (0, "DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoLocalLcceIpAddr"),
    (0, "DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoLocalId"),
    (0, "DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionFlowPspFlowId"),
)
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionFlowEntry.setStatus("current")
_DocsRphyCcapL2tpSessionFlowPspFlowId_Type = Unsigned32
_DocsRphyCcapL2tpSessionFlowPspFlowId_Object = MibTableColumn
docsRphyCcapL2tpSessionFlowPspFlowId = _DocsRphyCcapL2tpSessionFlowPspFlowId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 2, 1, 1),
    _DocsRphyCcapL2tpSessionFlowPspFlowId_Type()
)
docsRphyCcapL2tpSessionFlowPspFlowId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionFlowPspFlowId.setStatus("current")
_DocsRphyCcapL2tpSessionStatsTable_Object = MibTable
docsRphyCcapL2tpSessionStatsTable = _DocsRphyCcapL2tpSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 3)
)
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionStatsTable.setStatus("current")
_DocsRphyCcapL2tpSessionStatsEntry_Object = MibTableRow
docsRphyCcapL2tpSessionStatsEntry = _DocsRphyCcapL2tpSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionStatsEntry.setStatus("current")
_DocsRphyCcapL2tpSessionStatsOutOfSeqPkts_Type = Counter32
_DocsRphyCcapL2tpSessionStatsOutOfSeqPkts_Object = MibTableColumn
docsRphyCcapL2tpSessionStatsOutOfSeqPkts = _DocsRphyCcapL2tpSessionStatsOutOfSeqPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 3, 1, 1),
    _DocsRphyCcapL2tpSessionStatsOutOfSeqPkts_Type()
)
docsRphyCcapL2tpSessionStatsOutOfSeqPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapL2tpSessionStatsOutOfSeqPkts.setStatus("current")
_DocsRphyCcapCinDsLatencyTable_Object = MibTable
docsRphyCcapCinDsLatencyTable = _DocsRphyCcapCinDsLatencyTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 4)
)
if mibBuilder.loadTexts:
    docsRphyCcapCinDsLatencyTable.setStatus("current")
_DocsRphyCcapCinDsLatencyEntry_Object = MibTableRow
docsRphyCcapCinDsLatencyEntry = _DocsRphyCcapCinDsLatencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 4, 1)
)
if mibBuilder.loadTexts:
    docsRphyCcapCinDsLatencyEntry.setStatus("current")
_DocsRphyCcapCinDsLatencyLastVal_Type = Unsigned32
_DocsRphyCcapCinDsLatencyLastVal_Object = MibTableColumn
docsRphyCcapCinDsLatencyLastVal = _DocsRphyCcapCinDsLatencyLastVal_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 4, 1, 1),
    _DocsRphyCcapCinDsLatencyLastVal_Type()
)
docsRphyCcapCinDsLatencyLastVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapCinDsLatencyLastVal.setStatus("current")
_DocsRphyCcapCinDsLatencyLastValTime_Type = TimeTicks
_DocsRphyCcapCinDsLatencyLastValTime_Object = MibTableColumn
docsRphyCcapCinDsLatencyLastValTime = _DocsRphyCcapCinDsLatencyLastValTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 4, 1, 2),
    _DocsRphyCcapCinDsLatencyLastValTime_Type()
)
docsRphyCcapCinDsLatencyLastValTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapCinDsLatencyLastValTime.setStatus("current")
_DocsRphyCcapCinDsLatencyInterval_Type = Unsigned32
_DocsRphyCcapCinDsLatencyInterval_Object = MibTableColumn
docsRphyCcapCinDsLatencyInterval = _DocsRphyCcapCinDsLatencyInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 4, 1, 3),
    _DocsRphyCcapCinDsLatencyInterval_Type()
)
docsRphyCcapCinDsLatencyInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapCinDsLatencyInterval.setStatus("current")
_DocsRphyCcapSessionCinDsLatencyStatsTable_Object = MibTable
docsRphyCcapSessionCinDsLatencyStatsTable = _DocsRphyCcapSessionCinDsLatencyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 5)
)
if mibBuilder.loadTexts:
    docsRphyCcapSessionCinDsLatencyStatsTable.setStatus("current")
_DocsRphyCcapSessionCinDsLatencyStatsEntry_Object = MibTableRow
docsRphyCcapSessionCinDsLatencyStatsEntry = _DocsRphyCcapSessionCinDsLatencyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 5, 1)
)
docsRphyCcapSessionCinDsLatencyStatsEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoLocalLcceIpAddrType"),
    (0, "DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoLocalLcceIpAddr"),
    (0, "DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoLocalId"),
    (0, "DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionFlowPspFlowId"),
    (0, "DOCS-RPHY-MIB", "docsRphyCcapSessionCinDsLatencyStatsIntervalSeq"),
)
if mibBuilder.loadTexts:
    docsRphyCcapSessionCinDsLatencyStatsEntry.setStatus("current")
_DocsRphyCcapSessionCinDsLatencyStatsIntervalSeq_Type = Unsigned32
_DocsRphyCcapSessionCinDsLatencyStatsIntervalSeq_Object = MibTableColumn
docsRphyCcapSessionCinDsLatencyStatsIntervalSeq = _DocsRphyCcapSessionCinDsLatencyStatsIntervalSeq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 5, 1, 1),
    _DocsRphyCcapSessionCinDsLatencyStatsIntervalSeq_Type()
)
docsRphyCcapSessionCinDsLatencyStatsIntervalSeq.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyCcapSessionCinDsLatencyStatsIntervalSeq.setStatus("current")
_DocsRphyCcapSessionCinDsLatencyStatsVal_Type = Unsigned32
_DocsRphyCcapSessionCinDsLatencyStatsVal_Object = MibTableColumn
docsRphyCcapSessionCinDsLatencyStatsVal = _DocsRphyCcapSessionCinDsLatencyStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 5, 1, 2),
    _DocsRphyCcapSessionCinDsLatencyStatsVal_Type()
)
docsRphyCcapSessionCinDsLatencyStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapSessionCinDsLatencyStatsVal.setStatus("current")
_DocsRphyCcapSessionCinDsLatencyStatsValTime_Type = TimeTicks
_DocsRphyCcapSessionCinDsLatencyStatsValTime_Object = MibTableColumn
docsRphyCcapSessionCinDsLatencyStatsValTime = _DocsRphyCcapSessionCinDsLatencyStatsValTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 4, 5, 1, 3),
    _DocsRphyCcapSessionCinDsLatencyStatsValTime_Type()
)
docsRphyCcapSessionCinDsLatencyStatsValTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapSessionCinDsLatencyStatsValTime.setStatus("current")
_DocsRphyCcapSecMibObjects_ObjectIdentity = ObjectIdentity
docsRphyCcapSecMibObjects = _DocsRphyCcapSecMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 5)
)
_DocsRphyCcapSecServerCertSubject_Type = SnmpAdminString
_DocsRphyCcapSecServerCertSubject_Object = MibScalar
docsRphyCcapSecServerCertSubject = _DocsRphyCcapSecServerCertSubject_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 5, 1),
    _DocsRphyCcapSecServerCertSubject_Type()
)
docsRphyCcapSecServerCertSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapSecServerCertSubject.setStatus("current")
_DocsRphyCcapSecServerCertIssuer_Type = SnmpAdminString
_DocsRphyCcapSecServerCertIssuer_Object = MibScalar
docsRphyCcapSecServerCertIssuer = _DocsRphyCcapSecServerCertIssuer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 5, 2),
    _DocsRphyCcapSecServerCertIssuer_Type()
)
docsRphyCcapSecServerCertIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapSecServerCertIssuer.setStatus("current")


class _DocsRphyCcapSecServerCertSerialNumber_Type(OctetString):
    """Custom type docsRphyCcapSecServerCertSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DocsRphyCcapSecServerCertSerialNumber_Type.__name__ = "OctetString"
_DocsRphyCcapSecServerCertSerialNumber_Object = MibScalar
docsRphyCcapSecServerCertSerialNumber = _DocsRphyCcapSecServerCertSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 5, 3),
    _DocsRphyCcapSecServerCertSerialNumber_Type()
)
docsRphyCcapSecServerCertSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapSecServerCertSerialNumber.setStatus("current")


class _DocsRphyCcapSecServerCertSource_Type(Integer32):
    """Custom type docsRphyCcapSecServerCertSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("authentInfo", 5),
          ("compiledIntoCode", 6),
          ("configurationFile", 2),
          ("externalDatabase", 3),
          ("other", 4),
          ("snmp", 1))
    )


_DocsRphyCcapSecServerCertSource_Type.__name__ = "Integer32"
_DocsRphyCcapSecServerCertSource_Object = MibScalar
docsRphyCcapSecServerCertSource = _DocsRphyCcapSecServerCertSource_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 5, 4),
    _DocsRphyCcapSecServerCertSource_Type()
)
docsRphyCcapSecServerCertSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapSecServerCertSource.setStatus("current")
_DocsRphyCcapSecServerCertCert_Type = DocsX509ASN1DEREncodedCertificate
_DocsRphyCcapSecServerCertCert_Object = MibScalar
docsRphyCcapSecServerCertCert = _DocsRphyCcapSecServerCertCert_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 5, 5),
    _DocsRphyCcapSecServerCertCert_Type()
)
docsRphyCcapSecServerCertCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapSecServerCertCert.setStatus("current")


class _DocsRphyCcapSecServerCertCertThumbprint_Type(OctetString):
    """Custom type docsRphyCcapSecServerCertCertThumbprint based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_DocsRphyCcapSecServerCertCertThumbprint_Type.__name__ = "OctetString"
_DocsRphyCcapSecServerCertCertThumbprint_Object = MibScalar
docsRphyCcapSecServerCertCertThumbprint = _DocsRphyCcapSecServerCertCertThumbprint_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 1, 5, 6),
    _DocsRphyCcapSecServerCertCertThumbprint_Type()
)
docsRphyCcapSecServerCertCertThumbprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyCcapSecServerCertCertThumbprint.setStatus("current")
_DocsRphyConformance_ObjectIdentity = ObjectIdentity
docsRphyConformance = _DocsRphyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 2)
)
_DocsRphyCompliances_ObjectIdentity = ObjectIdentity
docsRphyCompliances = _DocsRphyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 2, 1)
)
_DocsRphyGroups_ObjectIdentity = ObjectIdentity
docsRphyGroups = _DocsRphyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 2, 2)
)
docsRphyRpdDevL2tpSessionInfoEntry.registerAugmentions(
    ("DOCS-RPHY-MIB",
     "docsRphyRpdDevL2tpSessionStatsEntry")
)
docsRphyRpdDevL2tpSessionStatsEntry.setIndexNames(*docsRphyRpdDevL2tpSessionInfoEntry.getIndexNames())
docsRphyRpdIfEnetEntry.registerAugmentions(
    ("DOCS-RPHY-MIB",
     "docsRphyRpdIfEnetStatsEntry")
)
docsRphyRpdIfEnetStatsEntry.setIndexNames(*docsRphyRpdIfEnetEntry.getIndexNames())
docsRphyCcapL2tpSessionFlowEntry.registerAugmentions(
    ("DOCS-RPHY-MIB",
     "docsRphyCcapL2tpSessionStatsEntry")
)
docsRphyCcapL2tpSessionStatsEntry.setIndexNames(*docsRphyCcapL2tpSessionFlowEntry.getIndexNames())
docsRphyCcapL2tpSessionFlowEntry.registerAugmentions(
    ("DOCS-RPHY-MIB",
     "docsRphyCcapCinDsLatencyEntry")
)
docsRphyCcapCinDsLatencyEntry.setIndexNames(*docsRphyCcapL2tpSessionFlowEntry.getIndexNames())

# Managed Objects groups

docsRphyRpdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 2, 2, 1)
)
docsRphyRpdGroup.setObjects(
      *(("DOCS-RPHY-MIB", "docsRphyRpdDevInfoSysUpTime"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevInfoNumCrashFilesAvail"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevIdVendorName"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevIdVendorId"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevIdModelNum"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevIdSerialNum"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevIdDeviceAlias"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevIdDeviceDescr"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevIdHwRev"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevIdCurrSwVer"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevIdBootRomVer"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevIdUsBurstRcvrVendorId"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevIdUsBurstRcvrModelNum"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevIdUsBurstRcvrDrivVer"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevIdUsBurstRcvrSerialNum"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevIdRcpProtocolVer"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevIdRcpSchemaVer"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevLocationDescr"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevLocationLatitude"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevLocationLongitude"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCoresConnectedAddressType"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCoresConnectedAddress"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCoresConnectedIsPrincipal"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCoresConnectedName"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCoresConnectedVendorId"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabNumDsPorts"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabNumUsPorts"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabNumTenGeNsPorts"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabNumOneGeNsPorts"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabNumDsScQamChans"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabNumDsOfdmChans"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabNumUsScQamChans"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabNumUsOfdmaChans"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabNumDsOob55d1Chans"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabNumUsOob55d1Chans"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabNumDsOob55d2Modules"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabNumUsOob55d2Demods"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabNumNdfChans"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabNumNdrChans"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabNumDsPspFlowsPerChan"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabNumUsPspFlowsPerChan"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabNumAsynchVideoChans"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabNumCwToneGens"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabLowestCwToneFreq"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabHighestCwToneFreq"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabMaxCwTonePwr"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabQamAsPilot"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabSupportsUdpEncap"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabSupportsFlowTags"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabSupportsFreqTilt"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabTiltRange"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabBufferDepthMonAlertSupp"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabBufferDepthCfgSupp"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabRpdUcdProcTime"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabRpdUcdChgNullGrtTime"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCapabMultiSectionTimingMerRep"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevChanReachabilityEndChanIndex"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevDsUsRfPortAllocScQamChans"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevDsUsRfPortAllocOfdmChans"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevDsUsRfPortAllocOob551Chans"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevDsUsRfPortAllocNdChans"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevL2tpSessionInfoRemoteLcceIpAddrType"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevL2tpSessionInfoRemoteLcceIpAddr"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevL2tpSessionInfoRemoteId"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevL2tpSessionInfoCoreId"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevL2tpSessionInfoConnCtrlID"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevL2tpSessionInfoUdpPort"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevL2tpSessionInfoDescr"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevL2tpSessionInfoSessionType"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevL2tpSessionInfoSessionSubType"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevL2tpSessionInfoMaxPayload"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevL2tpSessionInfoPathPayload"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevL2tpSessionInfoRpdIfMtu"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevL2tpSessionInfoCoreIfMtu"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevL2tpSessionInfoErrorCode"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevL2tpSessionInfoCreationTime"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevL2tpSessionInfoOperStatus"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevL2tpSessionInfoLocalStatus"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevL2tpSessionInfoLastChange"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevL2tpSessionStatsOutOfSeqPkts"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevDiagStatusProbableCause"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevDiagStatusAdditionalText"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevDiagStatusSeverityLevel"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevDepiMcastSessionLocalLcceIpAddr"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevDepiMcastSessionRemoteLcceIpAddr"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevDepiMcastSessionId"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevDepiMcastSessionJoinTime"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevEventLogFirstTime"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevEventLogLastTime"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevEventLogCounts"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevEventLogLevel"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevEventLogId"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevEventLogText"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevOob551UsChanStatusNcIpAddrType"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevOob551UsChanStatusNcIpAddr"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevOob551UsChanStatusArpdSrcIpAddrType"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevOob551UsChanStatusArpdSrcIpAddr"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevOob551UsChanStatusPerfectCellsRcvd"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevOob551UsChanStatusCorrectedCellsRcvd"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevOob551UsChanStatusUncorrectableCellsRcvd"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevOob551UsChanStatusTotalCellsRcvd"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevOob551UsChanStatusPwrLevel"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevOob551UsChanStatusMaxPwrLevel"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevOob551UsChanStatusMinPwrLevel"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevOob551UsChanStatusCounterDiscontinuityTime"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCrashDataFileStatusFilename"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevCrashDataFileStatusFileStatus"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevUsSignalQualityRxMer"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevUsSignalQualityRxMerSamples"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevUsSignalQualityUnerroreds"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevUsSignalQualityCorrecteds"),
        ("DOCS-RPHY-MIB", "docsRphyRpdDevUsSignalQualityUncorrectables"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntityDescr"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntityVendorType"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntityContainedIn"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntityClass"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntityParentRelPos"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntityName"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntityHardwareRev"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntityFirmwareRev"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntitySoftwareRev"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntitySerialNum"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntityMfgName"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntityModelName"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntityAlias"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntityAssetID"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntityIsFRU"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntityMfgDate"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntityUris"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntityUUID"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntityCoreIfIndex"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntSensorType"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntSensorScale"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntSensorPrecision"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntSensorValue"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntSensorOperStatus"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntSensorUnitsDisplay"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntSensorValueTimeStamp"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfPhysEntSensorValueUpdateRate"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetDescr"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetName"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetAlias"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetType"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetMtu"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetPhysAddress"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetAdminStatus"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetOperStatus"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetLastChange"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetLinkUpDownTrapEnable"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetHighSpeed"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetPromiscuousMode"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetConnectorPresent"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetStatsInOctets"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetStatsOutOctets"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetStatsInFrames"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetStatsOutFrames"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetStatsInUnicastOctets"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetStatsOutUnicastOctets"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetStatsInUnicastFrames"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetStatsOutUnicastFrames"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetStatsInMulticastOctets"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetStatsOutMulticastOctets"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetStatsInMulticastFrames"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetStatsOutMulticastFrames"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetStatsInBroadcastOctets"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetStatsOutBroadcastOctets"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetStatsInBroadcastFrames"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetStatsOutBroadcastFrames"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetStatsInDiscards"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetStatsOutDiscards"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetStatsInErrors"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetStatsOutErrors"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetStatsInUnknownProtos"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfEnetStatsCounterDiscontinuityTime"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfRpdEnetToCoreEntityMapEntityIndex"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfCoreToRpdMapRpdUniqueId"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfCoreToRpdMapRpdRfPortDirection"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfCoreToRpdMapRpdRfPortIndex"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfCoreToRpdMapRpdRfChanType"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfCoreToRpdMapRpdRfChanIndex"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIfRpdToCoreMapCoreIfIndex"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpv4GrpDefaultTTL"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpv4GrpInterfaceTableLastChange"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpv6GrpIpDefaultHopLimit"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpv6GrpInterfaceTableLastChange"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpv6GrpIfStatsTableLastChange"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpv4InterfaceEnableStatus"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpv4InterfaceRetransmitTime"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpv6InterfaceIdentifier"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpv6InterfaceEnableStatus"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpv6InterfaceReachableTime"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpv6InterfaceRetransmitTime"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpIfStatsInReceives"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpIfStatsInOctets"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpIfStatsInHdrErrors"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpIfStatsInNoRoutes"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpIfStatsInAddrErrors"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpIfStatsInUnknownProtos"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpIfStatsInTruncatedPkts"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpIfStatsInDiscards"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpIfStatsInDelivers"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpIfStatsOutRequests"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpIfStatsOutDiscards"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpIfStatsOutTransmits"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpIfStatsOutOctets"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpIfStatsInMcastPkts"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpIfStatsInMcastOctets"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpIfStatsOutMcastPkts"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpIfStatsOutMcastOctets"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpIfStatsDiscontinuityTime"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpIfStatsRefreshRate"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpAddressEnetPortIndex"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpAddressPrefixLen"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpAddressType"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpAddressOrigin"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpAddressStatus"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpAddressCreated"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpAddressLastChanged"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpNetToPhysicalPhysAddress"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpNetToPhysicalLastUpdated"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpNetToPhysicalType"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpNetToPhysicalState"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpDefaultRouterLifetime"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpDefaultRouterPreference"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpIcmpMsgStatsInPkts"),
        ("DOCS-RPHY-MIB", "docsRphyRpdIpIcmpMsgStatsOutPkts"))
)
if mibBuilder.loadTexts:
    docsRphyRpdGroup.setStatus("current")

docsRphyCcapCoreGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 2, 2, 2)
)
docsRphyCcapCoreGroup.setObjects(
      *(("DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoRemoteLcceIpAddrType"),
        ("DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoRemoteLcceIpAddr"),
        ("DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoRemoteId"),
        ("DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoCoreId"),
        ("DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoConnCtrlID"),
        ("DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoUdpPort"),
        ("DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoDescr"),
        ("DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoSessionType"),
        ("DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoSessionSubType"),
        ("DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoMaxPayload"),
        ("DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoPathPayload"),
        ("DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoRpdIfMtu"),
        ("DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoCoreIfMtu"),
        ("DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoIncludeDOCSISMsgs"),
        ("DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoErrorCode"),
        ("DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoCreationTime"),
        ("DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoOperStatus"),
        ("DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoLocalStatus"),
        ("DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionInfoLastChange"),
        ("DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionFlowPspFlowId"),
        ("DOCS-RPHY-MIB", "docsRphyCcapL2tpSessionStatsOutOfSeqPkts"),
        ("DOCS-RPHY-MIB", "docsRphyCcapCinDsLatencyLastVal"),
        ("DOCS-RPHY-MIB", "docsRphyCcapCinDsLatencyLastValTime"),
        ("DOCS-RPHY-MIB", "docsRphyCcapCinDsLatencyInterval"),
        ("DOCS-RPHY-MIB", "docsRphyCcapSessionCinDsLatencyStatsVal"),
        ("DOCS-RPHY-MIB", "docsRphyCcapSessionCinDsLatencyStatsValTime"))
)
if mibBuilder.loadTexts:
    docsRphyCcapCoreGroup.setStatus("current")

docsRphyCcapSecGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 2, 2, 3)
)
docsRphyCcapSecGroup.setObjects(
      *(("DOCS-RPHY-MIB", "docsRphyCcapSecServerCertSubject"),
        ("DOCS-RPHY-MIB", "docsRphyCcapSecServerCertIssuer"),
        ("DOCS-RPHY-MIB", "docsRphyCcapSecServerCertSerialNumber"),
        ("DOCS-RPHY-MIB", "docsRphyCcapSecServerCertSource"),
        ("DOCS-RPHY-MIB", "docsRphyCcapSecServerCertCert"),
        ("DOCS-RPHY-MIB", "docsRphyCcapSecServerCertCertThumbprint"))
)
if mibBuilder.loadTexts:
    docsRphyCcapSecGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsRphyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 30, 2, 1, 1)
)
if mibBuilder.loadTexts:
    docsRphyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-RPHY-MIB",
    **{"RphyChannelType": RphyChannelType,
       "RphyEventSeverityType": RphyEventSeverityType,
       "docsRphyMib": docsRphyMib,
       "docsRphyNotifications": docsRphyNotifications,
       "docsRphyObjects": docsRphyObjects,
       "docsRphyRpdDevMibObjects": docsRphyRpdDevMibObjects,
       "docsRphyRpdDevInfoTable": docsRphyRpdDevInfoTable,
       "docsRphyRpdDevInfoEntry": docsRphyRpdDevInfoEntry,
       "docsRphyRpdDevInfoUniqueId": docsRphyRpdDevInfoUniqueId,
       "docsRphyRpdDevInfoSysUpTime": docsRphyRpdDevInfoSysUpTime,
       "docsRphyRpdDevInfoNumCrashFilesAvail": docsRphyRpdDevInfoNumCrashFilesAvail,
       "docsRphyRpdDevIdentificationTable": docsRphyRpdDevIdentificationTable,
       "docsRphyRpdDevIdentificationEntry": docsRphyRpdDevIdentificationEntry,
       "docsRphyRpdDevIdVendorName": docsRphyRpdDevIdVendorName,
       "docsRphyRpdDevIdVendorId": docsRphyRpdDevIdVendorId,
       "docsRphyRpdDevIdModelNum": docsRphyRpdDevIdModelNum,
       "docsRphyRpdDevIdSerialNum": docsRphyRpdDevIdSerialNum,
       "docsRphyRpdDevIdDeviceAlias": docsRphyRpdDevIdDeviceAlias,
       "docsRphyRpdDevIdDeviceDescr": docsRphyRpdDevIdDeviceDescr,
       "docsRphyRpdDevIdHwRev": docsRphyRpdDevIdHwRev,
       "docsRphyRpdDevIdCurrSwVer": docsRphyRpdDevIdCurrSwVer,
       "docsRphyRpdDevIdBootRomVer": docsRphyRpdDevIdBootRomVer,
       "docsRphyRpdDevIdUsBurstRcvrVendorId": docsRphyRpdDevIdUsBurstRcvrVendorId,
       "docsRphyRpdDevIdUsBurstRcvrModelNum": docsRphyRpdDevIdUsBurstRcvrModelNum,
       "docsRphyRpdDevIdUsBurstRcvrDrivVer": docsRphyRpdDevIdUsBurstRcvrDrivVer,
       "docsRphyRpdDevIdUsBurstRcvrSerialNum": docsRphyRpdDevIdUsBurstRcvrSerialNum,
       "docsRphyRpdDevIdRcpProtocolVer": docsRphyRpdDevIdRcpProtocolVer,
       "docsRphyRpdDevIdRcpSchemaVer": docsRphyRpdDevIdRcpSchemaVer,
       "docsRphyRpdDevLocationTable": docsRphyRpdDevLocationTable,
       "docsRphyRpdDevLocationEntry": docsRphyRpdDevLocationEntry,
       "docsRphyRpdDevLocationDescr": docsRphyRpdDevLocationDescr,
       "docsRphyRpdDevLocationLatitude": docsRphyRpdDevLocationLatitude,
       "docsRphyRpdDevLocationLongitude": docsRphyRpdDevLocationLongitude,
       "docsRphyRpdDevCoresConnectedTable": docsRphyRpdDevCoresConnectedTable,
       "docsRphyRpdDevCoresConnectedEntry": docsRphyRpdDevCoresConnectedEntry,
       "docsRphyRpdDevCoresConnectedCoreId": docsRphyRpdDevCoresConnectedCoreId,
       "docsRphyRpdDevCoresConnectedAddressType": docsRphyRpdDevCoresConnectedAddressType,
       "docsRphyRpdDevCoresConnectedAddress": docsRphyRpdDevCoresConnectedAddress,
       "docsRphyRpdDevCoresConnectedIsPrincipal": docsRphyRpdDevCoresConnectedIsPrincipal,
       "docsRphyRpdDevCoresConnectedName": docsRphyRpdDevCoresConnectedName,
       "docsRphyRpdDevCoresConnectedVendorId": docsRphyRpdDevCoresConnectedVendorId,
       "docsRphyRpdDevCapabilitiesTable": docsRphyRpdDevCapabilitiesTable,
       "docsRphyRpdDevCapabilitiesEntry": docsRphyRpdDevCapabilitiesEntry,
       "docsRphyRpdDevCapabNumDsPorts": docsRphyRpdDevCapabNumDsPorts,
       "docsRphyRpdDevCapabNumUsPorts": docsRphyRpdDevCapabNumUsPorts,
       "docsRphyRpdDevCapabNumTenGeNsPorts": docsRphyRpdDevCapabNumTenGeNsPorts,
       "docsRphyRpdDevCapabNumOneGeNsPorts": docsRphyRpdDevCapabNumOneGeNsPorts,
       "docsRphyRpdDevCapabNumDsScQamChans": docsRphyRpdDevCapabNumDsScQamChans,
       "docsRphyRpdDevCapabNumDsOfdmChans": docsRphyRpdDevCapabNumDsOfdmChans,
       "docsRphyRpdDevCapabNumUsScQamChans": docsRphyRpdDevCapabNumUsScQamChans,
       "docsRphyRpdDevCapabNumUsOfdmaChans": docsRphyRpdDevCapabNumUsOfdmaChans,
       "docsRphyRpdDevCapabNumDsOob55d1Chans": docsRphyRpdDevCapabNumDsOob55d1Chans,
       "docsRphyRpdDevCapabNumUsOob55d1Chans": docsRphyRpdDevCapabNumUsOob55d1Chans,
       "docsRphyRpdDevCapabNumDsOob55d2Modules": docsRphyRpdDevCapabNumDsOob55d2Modules,
       "docsRphyRpdDevCapabNumUsOob55d2Demods": docsRphyRpdDevCapabNumUsOob55d2Demods,
       "docsRphyRpdDevCapabNumNdfChans": docsRphyRpdDevCapabNumNdfChans,
       "docsRphyRpdDevCapabNumNdrChans": docsRphyRpdDevCapabNumNdrChans,
       "docsRphyRpdDevCapabNumDsPspFlowsPerChan": docsRphyRpdDevCapabNumDsPspFlowsPerChan,
       "docsRphyRpdDevCapabNumUsPspFlowsPerChan": docsRphyRpdDevCapabNumUsPspFlowsPerChan,
       "docsRphyRpdDevCapabNumAsynchVideoChans": docsRphyRpdDevCapabNumAsynchVideoChans,
       "docsRphyRpdDevCapabNumCwToneGens": docsRphyRpdDevCapabNumCwToneGens,
       "docsRphyRpdDevCapabLowestCwToneFreq": docsRphyRpdDevCapabLowestCwToneFreq,
       "docsRphyRpdDevCapabHighestCwToneFreq": docsRphyRpdDevCapabHighestCwToneFreq,
       "docsRphyRpdDevCapabMaxCwTonePwr": docsRphyRpdDevCapabMaxCwTonePwr,
       "docsRphyRpdDevCapabQamAsPilot": docsRphyRpdDevCapabQamAsPilot,
       "docsRphyRpdDevCapabSupportsUdpEncap": docsRphyRpdDevCapabSupportsUdpEncap,
       "docsRphyRpdDevCapabSupportsFlowTags": docsRphyRpdDevCapabSupportsFlowTags,
       "docsRphyRpdDevCapabSupportsFreqTilt": docsRphyRpdDevCapabSupportsFreqTilt,
       "docsRphyRpdDevCapabTiltRange": docsRphyRpdDevCapabTiltRange,
       "docsRphyRpdDevCapabBufferDepthMonAlertSupp": docsRphyRpdDevCapabBufferDepthMonAlertSupp,
       "docsRphyRpdDevCapabBufferDepthCfgSupp": docsRphyRpdDevCapabBufferDepthCfgSupp,
       "docsRphyRpdDevCapabRpdUcdProcTime": docsRphyRpdDevCapabRpdUcdProcTime,
       "docsRphyRpdDevCapabRpdUcdChgNullGrtTime": docsRphyRpdDevCapabRpdUcdChgNullGrtTime,
       "docsRphyRpdDevCapabMultiSectionTimingMerRep": docsRphyRpdDevCapabMultiSectionTimingMerRep,
       "docsRphyRpdDevChanReachabilityTable": docsRphyRpdDevChanReachabilityTable,
       "docsRphyRpdDevChanReachabilityEntry": docsRphyRpdDevChanReachabilityEntry,
       "docsRphyRpdDevChanReachabilityEnetPortIndex": docsRphyRpdDevChanReachabilityEnetPortIndex,
       "docsRphyRpdDevChanReachabilityRfPortIndex": docsRphyRpdDevChanReachabilityRfPortIndex,
       "docsRphyRpdDevChanReachabilityChanType": docsRphyRpdDevChanReachabilityChanType,
       "docsRphyRpdDevChanReachabilityStartChanIndex": docsRphyRpdDevChanReachabilityStartChanIndex,
       "docsRphyRpdDevChanReachabilityEndChanIndex": docsRphyRpdDevChanReachabilityEndChanIndex,
       "docsRphyRpdDevDsUsRfPortAllocTable": docsRphyRpdDevDsUsRfPortAllocTable,
       "docsRphyRpdDevDsUsRfPortAllocEntry": docsRphyRpdDevDsUsRfPortAllocEntry,
       "docsRphyRpdDevDsUsRfPortAllocIndex": docsRphyRpdDevDsUsRfPortAllocIndex,
       "docsRphyRpdDevDsUsRfPortAllocDirection": docsRphyRpdDevDsUsRfPortAllocDirection,
       "docsRphyRpdDevDsUsRfPortAllocScQamChans": docsRphyRpdDevDsUsRfPortAllocScQamChans,
       "docsRphyRpdDevDsUsRfPortAllocOfdmChans": docsRphyRpdDevDsUsRfPortAllocOfdmChans,
       "docsRphyRpdDevDsUsRfPortAllocOob551Chans": docsRphyRpdDevDsUsRfPortAllocOob551Chans,
       "docsRphyRpdDevDsUsRfPortAllocNdChans": docsRphyRpdDevDsUsRfPortAllocNdChans,
       "docsRphyRpdDevL2tpSessionInfoTable": docsRphyRpdDevL2tpSessionInfoTable,
       "docsRphyRpdDevL2tpSessionInfoEntry": docsRphyRpdDevL2tpSessionInfoEntry,
       "docsRphyRpdDevL2tpSessionInfoLocalLcceIpAddrType": docsRphyRpdDevL2tpSessionInfoLocalLcceIpAddrType,
       "docsRphyRpdDevL2tpSessionInfoLocalLcceIpAddr": docsRphyRpdDevL2tpSessionInfoLocalLcceIpAddr,
       "docsRphyRpdDevL2tpSessionInfoLocalId": docsRphyRpdDevL2tpSessionInfoLocalId,
       "docsRphyRpdDevL2tpSessionInfoRemoteLcceIpAddrType": docsRphyRpdDevL2tpSessionInfoRemoteLcceIpAddrType,
       "docsRphyRpdDevL2tpSessionInfoRemoteLcceIpAddr": docsRphyRpdDevL2tpSessionInfoRemoteLcceIpAddr,
       "docsRphyRpdDevL2tpSessionInfoRemoteId": docsRphyRpdDevL2tpSessionInfoRemoteId,
       "docsRphyRpdDevL2tpSessionInfoCoreId": docsRphyRpdDevL2tpSessionInfoCoreId,
       "docsRphyRpdDevL2tpSessionInfoConnCtrlID": docsRphyRpdDevL2tpSessionInfoConnCtrlID,
       "docsRphyRpdDevL2tpSessionInfoUdpPort": docsRphyRpdDevL2tpSessionInfoUdpPort,
       "docsRphyRpdDevL2tpSessionInfoDescr": docsRphyRpdDevL2tpSessionInfoDescr,
       "docsRphyRpdDevL2tpSessionInfoSessionType": docsRphyRpdDevL2tpSessionInfoSessionType,
       "docsRphyRpdDevL2tpSessionInfoSessionSubType": docsRphyRpdDevL2tpSessionInfoSessionSubType,
       "docsRphyRpdDevL2tpSessionInfoMaxPayload": docsRphyRpdDevL2tpSessionInfoMaxPayload,
       "docsRphyRpdDevL2tpSessionInfoPathPayload": docsRphyRpdDevL2tpSessionInfoPathPayload,
       "docsRphyRpdDevL2tpSessionInfoRpdIfMtu": docsRphyRpdDevL2tpSessionInfoRpdIfMtu,
       "docsRphyRpdDevL2tpSessionInfoCoreIfMtu": docsRphyRpdDevL2tpSessionInfoCoreIfMtu,
       "docsRphyRpdDevL2tpSessionInfoErrorCode": docsRphyRpdDevL2tpSessionInfoErrorCode,
       "docsRphyRpdDevL2tpSessionInfoCreationTime": docsRphyRpdDevL2tpSessionInfoCreationTime,
       "docsRphyRpdDevL2tpSessionInfoOperStatus": docsRphyRpdDevL2tpSessionInfoOperStatus,
       "docsRphyRpdDevL2tpSessionInfoLocalStatus": docsRphyRpdDevL2tpSessionInfoLocalStatus,
       "docsRphyRpdDevL2tpSessionInfoLastChange": docsRphyRpdDevL2tpSessionInfoLastChange,
       "docsRphyRpdDevL2tpSessionStatsTable": docsRphyRpdDevL2tpSessionStatsTable,
       "docsRphyRpdDevL2tpSessionStatsEntry": docsRphyRpdDevL2tpSessionStatsEntry,
       "docsRphyRpdDevL2tpSessionStatsOutOfSeqPkts": docsRphyRpdDevL2tpSessionStatsOutOfSeqPkts,
       "docsRphyRpdDevDiagStatusTable": docsRphyRpdDevDiagStatusTable,
       "docsRphyRpdDevDiagStatusEntry": docsRphyRpdDevDiagStatusEntry,
       "docsRphyRpdDevDiagStatusProbableCause": docsRphyRpdDevDiagStatusProbableCause,
       "docsRphyRpdDevDiagStatusAdditionalText": docsRphyRpdDevDiagStatusAdditionalText,
       "docsRphyRpdDevDiagStatusSeverityLevel": docsRphyRpdDevDiagStatusSeverityLevel,
       "docsRphyRpdDevDepiMcastSessionTable": docsRphyRpdDevDepiMcastSessionTable,
       "docsRphyRpdDevDepiMcastSessionEntry": docsRphyRpdDevDepiMcastSessionEntry,
       "docsRphyRpdDevDepiMcastSessionIpAddrType": docsRphyRpdDevDepiMcastSessionIpAddrType,
       "docsRphyRpdDevDepiMcastSessionGrpIpAddr": docsRphyRpdDevDepiMcastSessionGrpIpAddr,
       "docsRphyRpdDevDepiMcastSessionSrcIpAddr": docsRphyRpdDevDepiMcastSessionSrcIpAddr,
       "docsRphyRpdDevDepiMcastSessionLocalLcceIpAddr": docsRphyRpdDevDepiMcastSessionLocalLcceIpAddr,
       "docsRphyRpdDevDepiMcastSessionRemoteLcceIpAddr": docsRphyRpdDevDepiMcastSessionRemoteLcceIpAddr,
       "docsRphyRpdDevDepiMcastSessionId": docsRphyRpdDevDepiMcastSessionId,
       "docsRphyRpdDevDepiMcastSessionJoinTime": docsRphyRpdDevDepiMcastSessionJoinTime,
       "docsRphyRpdDevEventLogTable": docsRphyRpdDevEventLogTable,
       "docsRphyRpdDevEventLogEntry": docsRphyRpdDevEventLogEntry,
       "docsRphyRpdDevEventLogIndex": docsRphyRpdDevEventLogIndex,
       "docsRphyRpdDevEventLogFirstTime": docsRphyRpdDevEventLogFirstTime,
       "docsRphyRpdDevEventLogLastTime": docsRphyRpdDevEventLogLastTime,
       "docsRphyRpdDevEventLogCounts": docsRphyRpdDevEventLogCounts,
       "docsRphyRpdDevEventLogLevel": docsRphyRpdDevEventLogLevel,
       "docsRphyRpdDevEventLogId": docsRphyRpdDevEventLogId,
       "docsRphyRpdDevEventLogText": docsRphyRpdDevEventLogText,
       "docsRphyRpdDevOob551UsChanStatusTable": docsRphyRpdDevOob551UsChanStatusTable,
       "docsRphyRpdDevOob551UsChanStatusEntry": docsRphyRpdDevOob551UsChanStatusEntry,
       "docsRphyRpdDevOob551UsChanStatusRfPort": docsRphyRpdDevOob551UsChanStatusRfPort,
       "docsRphyRpdDevOob551UsChanStatusChannelId": docsRphyRpdDevOob551UsChanStatusChannelId,
       "docsRphyRpdDevOob551UsChanStatusNcIpAddrType": docsRphyRpdDevOob551UsChanStatusNcIpAddrType,
       "docsRphyRpdDevOob551UsChanStatusNcIpAddr": docsRphyRpdDevOob551UsChanStatusNcIpAddr,
       "docsRphyRpdDevOob551UsChanStatusArpdSrcIpAddrType": docsRphyRpdDevOob551UsChanStatusArpdSrcIpAddrType,
       "docsRphyRpdDevOob551UsChanStatusArpdSrcIpAddr": docsRphyRpdDevOob551UsChanStatusArpdSrcIpAddr,
       "docsRphyRpdDevOob551UsChanStatusPerfectCellsRcvd": docsRphyRpdDevOob551UsChanStatusPerfectCellsRcvd,
       "docsRphyRpdDevOob551UsChanStatusCorrectedCellsRcvd": docsRphyRpdDevOob551UsChanStatusCorrectedCellsRcvd,
       "docsRphyRpdDevOob551UsChanStatusUncorrectableCellsRcvd": docsRphyRpdDevOob551UsChanStatusUncorrectableCellsRcvd,
       "docsRphyRpdDevOob551UsChanStatusTotalCellsRcvd": docsRphyRpdDevOob551UsChanStatusTotalCellsRcvd,
       "docsRphyRpdDevOob551UsChanStatusPwrLevel": docsRphyRpdDevOob551UsChanStatusPwrLevel,
       "docsRphyRpdDevOob551UsChanStatusMaxPwrLevel": docsRphyRpdDevOob551UsChanStatusMaxPwrLevel,
       "docsRphyRpdDevOob551UsChanStatusMinPwrLevel": docsRphyRpdDevOob551UsChanStatusMinPwrLevel,
       "docsRphyRpdDevOob551UsChanStatusCounterDiscontinuityTime": docsRphyRpdDevOob551UsChanStatusCounterDiscontinuityTime,
       "docsRphyRpdDevCrashDataFileStatusTable": docsRphyRpdDevCrashDataFileStatusTable,
       "docsRphyRpdDevCrashDataFileStatusEntry": docsRphyRpdDevCrashDataFileStatusEntry,
       "docsRphyRpdDevCrashDataFileStatusIndex": docsRphyRpdDevCrashDataFileStatusIndex,
       "docsRphyRpdDevCrashDataFileStatusFilename": docsRphyRpdDevCrashDataFileStatusFilename,
       "docsRphyRpdDevCrashDataFileStatusFileStatus": docsRphyRpdDevCrashDataFileStatusFileStatus,
       "docsRphyRpdDevUsSignalQualityTable": docsRphyRpdDevUsSignalQualityTable,
       "docsRphyRpdDevUsSignalQualityEntry": docsRphyRpdDevUsSignalQualityEntry,
       "docsRphyRpdDevUsSignalQualityRfPort": docsRphyRpdDevUsSignalQualityRfPort,
       "docsRphyRpdDevUsSignalQualityChannelIfIndex": docsRphyRpdDevUsSignalQualityChannelIfIndex,
       "docsRphyRpdDevUsSignalQualityRxMer": docsRphyRpdDevUsSignalQualityRxMer,
       "docsRphyRpdDevUsSignalQualityRxMerSamples": docsRphyRpdDevUsSignalQualityRxMerSamples,
       "docsRphyRpdDevUsSignalQualityUnerroreds": docsRphyRpdDevUsSignalQualityUnerroreds,
       "docsRphyRpdDevUsSignalQualityCorrecteds": docsRphyRpdDevUsSignalQualityCorrecteds,
       "docsRphyRpdDevUsSignalQualityUncorrectables": docsRphyRpdDevUsSignalQualityUncorrectables,
       "docsRphyRpdIfMibObjects": docsRphyRpdIfMibObjects,
       "docsRphyRpdIfPhysEntityTable": docsRphyRpdIfPhysEntityTable,
       "docsRphyRpdIfPhysEntityEntry": docsRphyRpdIfPhysEntityEntry,
       "docsRphyRpdIfPhysEntityIndex": docsRphyRpdIfPhysEntityIndex,
       "docsRphyRpdIfPhysEntityDescr": docsRphyRpdIfPhysEntityDescr,
       "docsRphyRpdIfPhysEntityVendorType": docsRphyRpdIfPhysEntityVendorType,
       "docsRphyRpdIfPhysEntityContainedIn": docsRphyRpdIfPhysEntityContainedIn,
       "docsRphyRpdIfPhysEntityClass": docsRphyRpdIfPhysEntityClass,
       "docsRphyRpdIfPhysEntityParentRelPos": docsRphyRpdIfPhysEntityParentRelPos,
       "docsRphyRpdIfPhysEntityName": docsRphyRpdIfPhysEntityName,
       "docsRphyRpdIfPhysEntityHardwareRev": docsRphyRpdIfPhysEntityHardwareRev,
       "docsRphyRpdIfPhysEntityFirmwareRev": docsRphyRpdIfPhysEntityFirmwareRev,
       "docsRphyRpdIfPhysEntitySoftwareRev": docsRphyRpdIfPhysEntitySoftwareRev,
       "docsRphyRpdIfPhysEntitySerialNum": docsRphyRpdIfPhysEntitySerialNum,
       "docsRphyRpdIfPhysEntityMfgName": docsRphyRpdIfPhysEntityMfgName,
       "docsRphyRpdIfPhysEntityModelName": docsRphyRpdIfPhysEntityModelName,
       "docsRphyRpdIfPhysEntityAlias": docsRphyRpdIfPhysEntityAlias,
       "docsRphyRpdIfPhysEntityAssetID": docsRphyRpdIfPhysEntityAssetID,
       "docsRphyRpdIfPhysEntityIsFRU": docsRphyRpdIfPhysEntityIsFRU,
       "docsRphyRpdIfPhysEntityMfgDate": docsRphyRpdIfPhysEntityMfgDate,
       "docsRphyRpdIfPhysEntityUris": docsRphyRpdIfPhysEntityUris,
       "docsRphyRpdIfPhysEntityUUID": docsRphyRpdIfPhysEntityUUID,
       "docsRphyRpdIfPhysEntityCoreIfIndex": docsRphyRpdIfPhysEntityCoreIfIndex,
       "docsRphyRpdIfPhysEntSensorTable": docsRphyRpdIfPhysEntSensorTable,
       "docsRphyRpdIfPhysEntSensorEntry": docsRphyRpdIfPhysEntSensorEntry,
       "docsRphyRpdIfPhysEntSensorType": docsRphyRpdIfPhysEntSensorType,
       "docsRphyRpdIfPhysEntSensorScale": docsRphyRpdIfPhysEntSensorScale,
       "docsRphyRpdIfPhysEntSensorPrecision": docsRphyRpdIfPhysEntSensorPrecision,
       "docsRphyRpdIfPhysEntSensorValue": docsRphyRpdIfPhysEntSensorValue,
       "docsRphyRpdIfPhysEntSensorOperStatus": docsRphyRpdIfPhysEntSensorOperStatus,
       "docsRphyRpdIfPhysEntSensorUnitsDisplay": docsRphyRpdIfPhysEntSensorUnitsDisplay,
       "docsRphyRpdIfPhysEntSensorValueTimeStamp": docsRphyRpdIfPhysEntSensorValueTimeStamp,
       "docsRphyRpdIfPhysEntSensorValueUpdateRate": docsRphyRpdIfPhysEntSensorValueUpdateRate,
       "docsRphyRpdIfEnetTable": docsRphyRpdIfEnetTable,
       "docsRphyRpdIfEnetEntry": docsRphyRpdIfEnetEntry,
       "docsRphyRpdIfEnetPortIndex": docsRphyRpdIfEnetPortIndex,
       "docsRphyRpdIfEnetDescr": docsRphyRpdIfEnetDescr,
       "docsRphyRpdIfEnetName": docsRphyRpdIfEnetName,
       "docsRphyRpdIfEnetAlias": docsRphyRpdIfEnetAlias,
       "docsRphyRpdIfEnetType": docsRphyRpdIfEnetType,
       "docsRphyRpdIfEnetMtu": docsRphyRpdIfEnetMtu,
       "docsRphyRpdIfEnetPhysAddress": docsRphyRpdIfEnetPhysAddress,
       "docsRphyRpdIfEnetAdminStatus": docsRphyRpdIfEnetAdminStatus,
       "docsRphyRpdIfEnetOperStatus": docsRphyRpdIfEnetOperStatus,
       "docsRphyRpdIfEnetLastChange": docsRphyRpdIfEnetLastChange,
       "docsRphyRpdIfEnetLinkUpDownTrapEnable": docsRphyRpdIfEnetLinkUpDownTrapEnable,
       "docsRphyRpdIfEnetHighSpeed": docsRphyRpdIfEnetHighSpeed,
       "docsRphyRpdIfEnetPromiscuousMode": docsRphyRpdIfEnetPromiscuousMode,
       "docsRphyRpdIfEnetConnectorPresent": docsRphyRpdIfEnetConnectorPresent,
       "docsRphyRpdIfEnetStatsTable": docsRphyRpdIfEnetStatsTable,
       "docsRphyRpdIfEnetStatsEntry": docsRphyRpdIfEnetStatsEntry,
       "docsRphyRpdIfEnetStatsInOctets": docsRphyRpdIfEnetStatsInOctets,
       "docsRphyRpdIfEnetStatsOutOctets": docsRphyRpdIfEnetStatsOutOctets,
       "docsRphyRpdIfEnetStatsInFrames": docsRphyRpdIfEnetStatsInFrames,
       "docsRphyRpdIfEnetStatsOutFrames": docsRphyRpdIfEnetStatsOutFrames,
       "docsRphyRpdIfEnetStatsInUnicastOctets": docsRphyRpdIfEnetStatsInUnicastOctets,
       "docsRphyRpdIfEnetStatsOutUnicastOctets": docsRphyRpdIfEnetStatsOutUnicastOctets,
       "docsRphyRpdIfEnetStatsInUnicastFrames": docsRphyRpdIfEnetStatsInUnicastFrames,
       "docsRphyRpdIfEnetStatsOutUnicastFrames": docsRphyRpdIfEnetStatsOutUnicastFrames,
       "docsRphyRpdIfEnetStatsInMulticastOctets": docsRphyRpdIfEnetStatsInMulticastOctets,
       "docsRphyRpdIfEnetStatsOutMulticastOctets": docsRphyRpdIfEnetStatsOutMulticastOctets,
       "docsRphyRpdIfEnetStatsInMulticastFrames": docsRphyRpdIfEnetStatsInMulticastFrames,
       "docsRphyRpdIfEnetStatsOutMulticastFrames": docsRphyRpdIfEnetStatsOutMulticastFrames,
       "docsRphyRpdIfEnetStatsInBroadcastOctets": docsRphyRpdIfEnetStatsInBroadcastOctets,
       "docsRphyRpdIfEnetStatsOutBroadcastOctets": docsRphyRpdIfEnetStatsOutBroadcastOctets,
       "docsRphyRpdIfEnetStatsInBroadcastFrames": docsRphyRpdIfEnetStatsInBroadcastFrames,
       "docsRphyRpdIfEnetStatsOutBroadcastFrames": docsRphyRpdIfEnetStatsOutBroadcastFrames,
       "docsRphyRpdIfEnetStatsInDiscards": docsRphyRpdIfEnetStatsInDiscards,
       "docsRphyRpdIfEnetStatsOutDiscards": docsRphyRpdIfEnetStatsOutDiscards,
       "docsRphyRpdIfEnetStatsInErrors": docsRphyRpdIfEnetStatsInErrors,
       "docsRphyRpdIfEnetStatsOutErrors": docsRphyRpdIfEnetStatsOutErrors,
       "docsRphyRpdIfEnetStatsInUnknownProtos": docsRphyRpdIfEnetStatsInUnknownProtos,
       "docsRphyRpdIfEnetStatsCounterDiscontinuityTime": docsRphyRpdIfEnetStatsCounterDiscontinuityTime,
       "docsRphyRpdIfRpdEnetToCoreEntityMapTable": docsRphyRpdIfRpdEnetToCoreEntityMapTable,
       "docsRphyRpdIfRpdEnetToCoreEntityMapEntry": docsRphyRpdIfRpdEnetToCoreEntityMapEntry,
       "docsRphyRpdIfRpdEnetToCoreEntityMapEntityIndex": docsRphyRpdIfRpdEnetToCoreEntityMapEntityIndex,
       "docsRphyRpdIfCoreToRpdMapTable": docsRphyRpdIfCoreToRpdMapTable,
       "docsRphyRpdIfCoreToRpdMapEntry": docsRphyRpdIfCoreToRpdMapEntry,
       "docsRphyRpdIfCoreToRpdMapRpdUniqueId": docsRphyRpdIfCoreToRpdMapRpdUniqueId,
       "docsRphyRpdIfCoreToRpdMapRpdRfPortDirection": docsRphyRpdIfCoreToRpdMapRpdRfPortDirection,
       "docsRphyRpdIfCoreToRpdMapRpdRfPortIndex": docsRphyRpdIfCoreToRpdMapRpdRfPortIndex,
       "docsRphyRpdIfCoreToRpdMapRpdRfChanType": docsRphyRpdIfCoreToRpdMapRpdRfChanType,
       "docsRphyRpdIfCoreToRpdMapRpdRfChanIndex": docsRphyRpdIfCoreToRpdMapRpdRfChanIndex,
       "docsRphyRpdIfRpdToCoreMapTable": docsRphyRpdIfRpdToCoreMapTable,
       "docsRphyRpdIfRpdToCoreMapEntry": docsRphyRpdIfRpdToCoreMapEntry,
       "docsRphyRpdIfRpdToCoreMapRpdRfPortDirection": docsRphyRpdIfRpdToCoreMapRpdRfPortDirection,
       "docsRphyRpdIfRpdToCoreMapRpdRfPortIndex": docsRphyRpdIfRpdToCoreMapRpdRfPortIndex,
       "docsRphyRpdIfRpdToCoreMapRpdRfChanType": docsRphyRpdIfRpdToCoreMapRpdRfChanType,
       "docsRphyRpdIfRpdToCoreMapRpdRfChanIndex": docsRphyRpdIfRpdToCoreMapRpdRfChanIndex,
       "docsRphyRpdIfRpdToCoreMapCoreIfIndex": docsRphyRpdIfRpdToCoreMapCoreIfIndex,
       "docsRphyRpdIpMibObjects": docsRphyRpdIpMibObjects,
       "docsRphyRpdIpv4GrpTable": docsRphyRpdIpv4GrpTable,
       "docsRphyRpdIpv4GrpEntry": docsRphyRpdIpv4GrpEntry,
       "docsRphyRpdIpv4GrpDefaultTTL": docsRphyRpdIpv4GrpDefaultTTL,
       "docsRphyRpdIpv4GrpInterfaceTableLastChange": docsRphyRpdIpv4GrpInterfaceTableLastChange,
       "docsRphyRpdIpv6GrpTable": docsRphyRpdIpv6GrpTable,
       "docsRphyRpdIpv6GrpEntry": docsRphyRpdIpv6GrpEntry,
       "docsRphyRpdIpv6GrpIpDefaultHopLimit": docsRphyRpdIpv6GrpIpDefaultHopLimit,
       "docsRphyRpdIpv6GrpInterfaceTableLastChange": docsRphyRpdIpv6GrpInterfaceTableLastChange,
       "docsRphyRpdIpv6GrpIfStatsTableLastChange": docsRphyRpdIpv6GrpIfStatsTableLastChange,
       "docsRphyRpdIpv4InterfaceTable": docsRphyRpdIpv4InterfaceTable,
       "docsRphyRpdIpv4InterfaceEntry": docsRphyRpdIpv4InterfaceEntry,
       "docsRphyRpdIpv4InterfaceEnableStatus": docsRphyRpdIpv4InterfaceEnableStatus,
       "docsRphyRpdIpv4InterfaceRetransmitTime": docsRphyRpdIpv4InterfaceRetransmitTime,
       "docsRphyRpdIpv6InterfaceTable": docsRphyRpdIpv6InterfaceTable,
       "docsRphyRpdIpv6InterfaceEntry": docsRphyRpdIpv6InterfaceEntry,
       "docsRphyRpdIpv6InterfaceIdentifier": docsRphyRpdIpv6InterfaceIdentifier,
       "docsRphyRpdIpv6InterfaceEnableStatus": docsRphyRpdIpv6InterfaceEnableStatus,
       "docsRphyRpdIpv6InterfaceReachableTime": docsRphyRpdIpv6InterfaceReachableTime,
       "docsRphyRpdIpv6InterfaceRetransmitTime": docsRphyRpdIpv6InterfaceRetransmitTime,
       "docsRphyRpdIpIfStatsTable": docsRphyRpdIpIfStatsTable,
       "docsRphyRpdIpIfStatsEntry": docsRphyRpdIpIfStatsEntry,
       "docsRphyRpdIpIfStatsIPVersion": docsRphyRpdIpIfStatsIPVersion,
       "docsRphyRpdIpIfStatsInReceives": docsRphyRpdIpIfStatsInReceives,
       "docsRphyRpdIpIfStatsInOctets": docsRphyRpdIpIfStatsInOctets,
       "docsRphyRpdIpIfStatsInHdrErrors": docsRphyRpdIpIfStatsInHdrErrors,
       "docsRphyRpdIpIfStatsInNoRoutes": docsRphyRpdIpIfStatsInNoRoutes,
       "docsRphyRpdIpIfStatsInAddrErrors": docsRphyRpdIpIfStatsInAddrErrors,
       "docsRphyRpdIpIfStatsInUnknownProtos": docsRphyRpdIpIfStatsInUnknownProtos,
       "docsRphyRpdIpIfStatsInTruncatedPkts": docsRphyRpdIpIfStatsInTruncatedPkts,
       "docsRphyRpdIpIfStatsInDiscards": docsRphyRpdIpIfStatsInDiscards,
       "docsRphyRpdIpIfStatsInDelivers": docsRphyRpdIpIfStatsInDelivers,
       "docsRphyRpdIpIfStatsOutRequests": docsRphyRpdIpIfStatsOutRequests,
       "docsRphyRpdIpIfStatsOutDiscards": docsRphyRpdIpIfStatsOutDiscards,
       "docsRphyRpdIpIfStatsOutTransmits": docsRphyRpdIpIfStatsOutTransmits,
       "docsRphyRpdIpIfStatsOutOctets": docsRphyRpdIpIfStatsOutOctets,
       "docsRphyRpdIpIfStatsInMcastPkts": docsRphyRpdIpIfStatsInMcastPkts,
       "docsRphyRpdIpIfStatsInMcastOctets": docsRphyRpdIpIfStatsInMcastOctets,
       "docsRphyRpdIpIfStatsOutMcastPkts": docsRphyRpdIpIfStatsOutMcastPkts,
       "docsRphyRpdIpIfStatsOutMcastOctets": docsRphyRpdIpIfStatsOutMcastOctets,
       "docsRphyRpdIpIfStatsDiscontinuityTime": docsRphyRpdIpIfStatsDiscontinuityTime,
       "docsRphyRpdIpIfStatsRefreshRate": docsRphyRpdIpIfStatsRefreshRate,
       "docsRphyRpdIpAddressTable": docsRphyRpdIpAddressTable,
       "docsRphyRpdIpAddressEntry": docsRphyRpdIpAddressEntry,
       "docsRphyRpdIpAddressAddrType": docsRphyRpdIpAddressAddrType,
       "docsRphyRpdIpAddressAddr": docsRphyRpdIpAddressAddr,
       "docsRphyRpdIpAddressEnetPortIndex": docsRphyRpdIpAddressEnetPortIndex,
       "docsRphyRpdIpAddressType": docsRphyRpdIpAddressType,
       "docsRphyRpdIpAddressPrefixLen": docsRphyRpdIpAddressPrefixLen,
       "docsRphyRpdIpAddressOrigin": docsRphyRpdIpAddressOrigin,
       "docsRphyRpdIpAddressStatus": docsRphyRpdIpAddressStatus,
       "docsRphyRpdIpAddressCreated": docsRphyRpdIpAddressCreated,
       "docsRphyRpdIpAddressLastChanged": docsRphyRpdIpAddressLastChanged,
       "docsRphyRpdIpNetToPhysicalTable": docsRphyRpdIpNetToPhysicalTable,
       "docsRphyRpdIpNetToPhysicalEntry": docsRphyRpdIpNetToPhysicalEntry,
       "docsRphyRpdIpNetToPhysicalNetAddressType": docsRphyRpdIpNetToPhysicalNetAddressType,
       "docsRphyRpdIpNetToPhysicalNetAddress": docsRphyRpdIpNetToPhysicalNetAddress,
       "docsRphyRpdIpNetToPhysicalPhysAddress": docsRphyRpdIpNetToPhysicalPhysAddress,
       "docsRphyRpdIpNetToPhysicalLastUpdated": docsRphyRpdIpNetToPhysicalLastUpdated,
       "docsRphyRpdIpNetToPhysicalType": docsRphyRpdIpNetToPhysicalType,
       "docsRphyRpdIpNetToPhysicalState": docsRphyRpdIpNetToPhysicalState,
       "docsRphyRpdIpDefaultRouterTable": docsRphyRpdIpDefaultRouterTable,
       "docsRphyRpdIpDefaultRouterEntry": docsRphyRpdIpDefaultRouterEntry,
       "docsRphyRpdIpDefaultRouterAddressType": docsRphyRpdIpDefaultRouterAddressType,
       "docsRphyRpdIpDefaultRouterAddress": docsRphyRpdIpDefaultRouterAddress,
       "docsRphyRpdIpDefaultRouterLifetime": docsRphyRpdIpDefaultRouterLifetime,
       "docsRphyRpdIpDefaultRouterPreference": docsRphyRpdIpDefaultRouterPreference,
       "docsRphyRpdIpIcmpMibObjects": docsRphyRpdIpIcmpMibObjects,
       "docsRphyRpdIpIcmpMsgStatsTable": docsRphyRpdIpIcmpMsgStatsTable,
       "docsRphyRpdIpIcmpMsgStatsEntry": docsRphyRpdIpIcmpMsgStatsEntry,
       "docsRphyRpdIpIcmpMsgStatsIPVersion": docsRphyRpdIpIcmpMsgStatsIPVersion,
       "docsRphyRpdIpIcmpMsgStatsType": docsRphyRpdIpIcmpMsgStatsType,
       "docsRphyRpdIpIcmpMsgStatsInPkts": docsRphyRpdIpIcmpMsgStatsInPkts,
       "docsRphyRpdIpIcmpMsgStatsOutPkts": docsRphyRpdIpIcmpMsgStatsOutPkts,
       "docsRphyCcapMibObjects": docsRphyCcapMibObjects,
       "docsRphyCcapL2tpSessionInfoTable": docsRphyCcapL2tpSessionInfoTable,
       "docsRphyCcapL2tpSessionInfoEntry": docsRphyCcapL2tpSessionInfoEntry,
       "docsRphyCcapL2tpSessionInfoLocalLcceIpAddrType": docsRphyCcapL2tpSessionInfoLocalLcceIpAddrType,
       "docsRphyCcapL2tpSessionInfoLocalLcceIpAddr": docsRphyCcapL2tpSessionInfoLocalLcceIpAddr,
       "docsRphyCcapL2tpSessionInfoLocalId": docsRphyCcapL2tpSessionInfoLocalId,
       "docsRphyCcapL2tpSessionInfoRemoteLcceIpAddrType": docsRphyCcapL2tpSessionInfoRemoteLcceIpAddrType,
       "docsRphyCcapL2tpSessionInfoRemoteLcceIpAddr": docsRphyCcapL2tpSessionInfoRemoteLcceIpAddr,
       "docsRphyCcapL2tpSessionInfoRemoteId": docsRphyCcapL2tpSessionInfoRemoteId,
       "docsRphyCcapL2tpSessionInfoCoreId": docsRphyCcapL2tpSessionInfoCoreId,
       "docsRphyCcapL2tpSessionInfoConnCtrlID": docsRphyCcapL2tpSessionInfoConnCtrlID,
       "docsRphyCcapL2tpSessionInfoUdpPort": docsRphyCcapL2tpSessionInfoUdpPort,
       "docsRphyCcapL2tpSessionInfoDescr": docsRphyCcapL2tpSessionInfoDescr,
       "docsRphyCcapL2tpSessionInfoSessionType": docsRphyCcapL2tpSessionInfoSessionType,
       "docsRphyCcapL2tpSessionInfoSessionSubType": docsRphyCcapL2tpSessionInfoSessionSubType,
       "docsRphyCcapL2tpSessionInfoMaxPayload": docsRphyCcapL2tpSessionInfoMaxPayload,
       "docsRphyCcapL2tpSessionInfoPathPayload": docsRphyCcapL2tpSessionInfoPathPayload,
       "docsRphyCcapL2tpSessionInfoRpdIfMtu": docsRphyCcapL2tpSessionInfoRpdIfMtu,
       "docsRphyCcapL2tpSessionInfoCoreIfMtu": docsRphyCcapL2tpSessionInfoCoreIfMtu,
       "docsRphyCcapL2tpSessionInfoIncludeDOCSISMsgs": docsRphyCcapL2tpSessionInfoIncludeDOCSISMsgs,
       "docsRphyCcapL2tpSessionInfoErrorCode": docsRphyCcapL2tpSessionInfoErrorCode,
       "docsRphyCcapL2tpSessionInfoCreationTime": docsRphyCcapL2tpSessionInfoCreationTime,
       "docsRphyCcapL2tpSessionInfoOperStatus": docsRphyCcapL2tpSessionInfoOperStatus,
       "docsRphyCcapL2tpSessionInfoLocalStatus": docsRphyCcapL2tpSessionInfoLocalStatus,
       "docsRphyCcapL2tpSessionInfoLastChange": docsRphyCcapL2tpSessionInfoLastChange,
       "docsRphyCcapL2tpSessionFlowTable": docsRphyCcapL2tpSessionFlowTable,
       "docsRphyCcapL2tpSessionFlowEntry": docsRphyCcapL2tpSessionFlowEntry,
       "docsRphyCcapL2tpSessionFlowPspFlowId": docsRphyCcapL2tpSessionFlowPspFlowId,
       "docsRphyCcapL2tpSessionStatsTable": docsRphyCcapL2tpSessionStatsTable,
       "docsRphyCcapL2tpSessionStatsEntry": docsRphyCcapL2tpSessionStatsEntry,
       "docsRphyCcapL2tpSessionStatsOutOfSeqPkts": docsRphyCcapL2tpSessionStatsOutOfSeqPkts,
       "docsRphyCcapCinDsLatencyTable": docsRphyCcapCinDsLatencyTable,
       "docsRphyCcapCinDsLatencyEntry": docsRphyCcapCinDsLatencyEntry,
       "docsRphyCcapCinDsLatencyLastVal": docsRphyCcapCinDsLatencyLastVal,
       "docsRphyCcapCinDsLatencyLastValTime": docsRphyCcapCinDsLatencyLastValTime,
       "docsRphyCcapCinDsLatencyInterval": docsRphyCcapCinDsLatencyInterval,
       "docsRphyCcapSessionCinDsLatencyStatsTable": docsRphyCcapSessionCinDsLatencyStatsTable,
       "docsRphyCcapSessionCinDsLatencyStatsEntry": docsRphyCcapSessionCinDsLatencyStatsEntry,
       "docsRphyCcapSessionCinDsLatencyStatsIntervalSeq": docsRphyCcapSessionCinDsLatencyStatsIntervalSeq,
       "docsRphyCcapSessionCinDsLatencyStatsVal": docsRphyCcapSessionCinDsLatencyStatsVal,
       "docsRphyCcapSessionCinDsLatencyStatsValTime": docsRphyCcapSessionCinDsLatencyStatsValTime,
       "docsRphyCcapSecMibObjects": docsRphyCcapSecMibObjects,
       "docsRphyCcapSecServerCertSubject": docsRphyCcapSecServerCertSubject,
       "docsRphyCcapSecServerCertIssuer": docsRphyCcapSecServerCertIssuer,
       "docsRphyCcapSecServerCertSerialNumber": docsRphyCcapSecServerCertSerialNumber,
       "docsRphyCcapSecServerCertSource": docsRphyCcapSecServerCertSource,
       "docsRphyCcapSecServerCertCert": docsRphyCcapSecServerCertCert,
       "docsRphyCcapSecServerCertCertThumbprint": docsRphyCcapSecServerCertCertThumbprint,
       "docsRphyConformance": docsRphyConformance,
       "docsRphyCompliances": docsRphyCompliances,
       "docsRphyCompliance": docsRphyCompliance,
       "docsRphyGroups": docsRphyGroups,
       "docsRphyRpdGroup": docsRphyRpdGroup,
       "docsRphyCcapCoreGroup": docsRphyCcapCoreGroup,
       "docsRphyCcapSecGroup": docsRphyCcapSecGroup}
)
