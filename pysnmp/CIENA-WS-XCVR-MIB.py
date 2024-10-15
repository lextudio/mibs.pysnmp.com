# SNMP MIB module (CIENA-WS-XCVR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIENA-WS-XCVR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:12 2024
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

(cienaWsConfig,) = mibBuilder.importSymbols(
    "CIENA-WS-MIB",
    "cienaWsConfig")

(ChannelsNumber,
 ConnectorTypeDescEnum,
 Decimal1Dig,
 EnabledDisabledEnum,
 NameString,
 PtpId,
 StringMaxl128,
 StringMaxl16,
 StringMaxl254,
 StringMaxl32,
 XcvrId,
 XcvrMode,
 XcvrType) = mibBuilder.importSymbols(
    "CIENA-WS-TYPEDEFS-MIB",
    "ChannelsNumber",
    "ConnectorTypeDescEnum",
    "Decimal1Dig",
    "EnabledDisabledEnum",
    "NameString",
    "PtpId",
    "StringMaxl128",
    "StringMaxl16",
    "StringMaxl254",
    "StringMaxl32",
    "XcvrId",
    "XcvrMode",
    "XcvrType")

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

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cienaWsXcvrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15)
)
cienaWsXcvrMIB.setRevisions(
        ("2016-12-12 00:00",
         "2016-06-14 00:00",
         "2015-02-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class XcvrOpEnum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("empty", 0),
          ("lowpowermode", 4),
          ("uncertified", 3),
          ("unknown", 5),
          ("up", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CienaWsXcvrObjects_ObjectIdentity = ObjectIdentity
cienaWsXcvrObjects = _CienaWsXcvrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 1)
)
_CienaWsXcvrConformance_ObjectIdentity = ObjectIdentity
cienaWsXcvrConformance = _CienaWsXcvrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 2)
)
_CienaWsXcvrGroups_ObjectIdentity = ObjectIdentity
cienaWsXcvrGroups = _CienaWsXcvrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 2, 1)
)
_CienaWsXcvrCompliances_ObjectIdentity = ObjectIdentity
cienaWsXcvrCompliances = _CienaWsXcvrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 2, 2)
)
_CwsXcvrXcvrsTable_Object = MibTable
cwsXcvrXcvrsTable = _CwsXcvrXcvrsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 3)
)
if mibBuilder.loadTexts:
    cwsXcvrXcvrsTable.setStatus("current")
_CwsXcvrXcvrsEntry_Object = MibTableRow
cwsXcvrXcvrsEntry = _CwsXcvrXcvrsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 3, 1)
)
cwsXcvrXcvrsEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"),
)
if mibBuilder.loadTexts:
    cwsXcvrXcvrsEntry.setStatus("current")


class _CwsXcvrXcvrsXcvrIndex_Type(Integer32):
    """Custom type cwsXcvrXcvrsXcvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrXcvrsXcvrIndex_Type.__name__ = "Integer32"
_CwsXcvrXcvrsXcvrIndex_Object = MibTableColumn
cwsXcvrXcvrsXcvrIndex = _CwsXcvrXcvrsXcvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 3, 1, 1),
    _CwsXcvrXcvrsXcvrIndex_Type()
)
cwsXcvrXcvrsXcvrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrXcvrsXcvrIndex.setStatus("current")
_CwsXcvrXcvrIdTable_Object = MibTable
cwsXcvrXcvrIdTable = _CwsXcvrXcvrIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 4)
)
if mibBuilder.loadTexts:
    cwsXcvrXcvrIdTable.setStatus("current")
_CwsXcvrXcvrIdEntry_Object = MibTableRow
cwsXcvrXcvrIdEntry = _CwsXcvrXcvrIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 4, 1)
)
cwsXcvrXcvrIdEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrXcvrIdEntry.setStatus("current")


class _CwsXcvrXcvrIdTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrXcvrIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrXcvrIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrXcvrIdTableSnmpKey_Object = MibTableColumn
cwsXcvrXcvrIdTableSnmpKey = _CwsXcvrXcvrIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 4, 1, 1),
    _CwsXcvrXcvrIdTableSnmpKey_Type()
)
cwsXcvrXcvrIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrXcvrIdTableSnmpKey.setStatus("current")
_CwsXcvrXcvrIdName_Type = NameString
_CwsXcvrXcvrIdName_Object = MibTableColumn
cwsXcvrXcvrIdName = _CwsXcvrXcvrIdName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 4, 1, 2),
    _CwsXcvrXcvrIdName_Type()
)
cwsXcvrXcvrIdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrXcvrIdName.setStatus("current")
_CwsXcvrXcvrIdDescription_Type = StringMaxl128
_CwsXcvrXcvrIdDescription_Object = MibTableColumn
cwsXcvrXcvrIdDescription = _CwsXcvrXcvrIdDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 4, 1, 3),
    _CwsXcvrXcvrIdDescription_Type()
)
cwsXcvrXcvrIdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrXcvrIdDescription.setStatus("current")
_CwsXcvrXcvrStateTable_Object = MibTable
cwsXcvrXcvrStateTable = _CwsXcvrXcvrStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 5)
)
if mibBuilder.loadTexts:
    cwsXcvrXcvrStateTable.setStatus("current")
_CwsXcvrXcvrStateEntry_Object = MibTableRow
cwsXcvrXcvrStateEntry = _CwsXcvrXcvrStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 5, 1)
)
cwsXcvrXcvrStateEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrXcvrStateEntry.setStatus("current")


class _CwsXcvrXcvrStateTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrXcvrStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrXcvrStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrXcvrStateTableSnmpKey_Object = MibTableColumn
cwsXcvrXcvrStateTableSnmpKey = _CwsXcvrXcvrStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 5, 1, 1),
    _CwsXcvrXcvrStateTableSnmpKey_Type()
)
cwsXcvrXcvrStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrXcvrStateTableSnmpKey.setStatus("current")
_CwsXcvrXcvrStateAdminState_Type = EnabledDisabledEnum
_CwsXcvrXcvrStateAdminState_Object = MibTableColumn
cwsXcvrXcvrStateAdminState = _CwsXcvrXcvrStateAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 5, 1, 2),
    _CwsXcvrXcvrStateAdminState_Type()
)
cwsXcvrXcvrStateAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrXcvrStateAdminState.setStatus("current")
_CwsXcvrXcvrStateOperationalState_Type = XcvrOpEnum
_CwsXcvrXcvrStateOperationalState_Object = MibTableColumn
cwsXcvrXcvrStateOperationalState = _CwsXcvrXcvrStateOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 5, 1, 3),
    _CwsXcvrXcvrStateOperationalState_Type()
)
cwsXcvrXcvrStateOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrXcvrStateOperationalState.setStatus("current")


class _CwsXcvrXcvrStatePowerState_Type(Integer32):
    """Custom type cwsXcvrXcvrStatePowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("normal", 0))
    )


_CwsXcvrXcvrStatePowerState_Type.__name__ = "Integer32"
_CwsXcvrXcvrStatePowerState_Object = MibTableColumn
cwsXcvrXcvrStatePowerState = _CwsXcvrXcvrStatePowerState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 5, 1, 4),
    _CwsXcvrXcvrStatePowerState_Type()
)
cwsXcvrXcvrStatePowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrXcvrStatePowerState.setStatus("current")
_CwsXcvrXcvrPropertiesTable_Object = MibTable
cwsXcvrXcvrPropertiesTable = _CwsXcvrXcvrPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 6)
)
if mibBuilder.loadTexts:
    cwsXcvrXcvrPropertiesTable.setStatus("current")
_CwsXcvrXcvrPropertiesEntry_Object = MibTableRow
cwsXcvrXcvrPropertiesEntry = _CwsXcvrXcvrPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 6, 1)
)
cwsXcvrXcvrPropertiesEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrPropertiesTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrXcvrPropertiesEntry.setStatus("current")


class _CwsXcvrXcvrPropertiesTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrXcvrPropertiesTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrXcvrPropertiesTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrXcvrPropertiesTableSnmpKey_Object = MibTableColumn
cwsXcvrXcvrPropertiesTableSnmpKey = _CwsXcvrXcvrPropertiesTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 6, 1, 1),
    _CwsXcvrXcvrPropertiesTableSnmpKey_Type()
)
cwsXcvrXcvrPropertiesTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrXcvrPropertiesTableSnmpKey.setStatus("current")
_CwsXcvrXcvrPropertiesType_Type = XcvrType
_CwsXcvrXcvrPropertiesType_Object = MibTableColumn
cwsXcvrXcvrPropertiesType = _CwsXcvrXcvrPropertiesType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 6, 1, 2),
    _CwsXcvrXcvrPropertiesType_Type()
)
cwsXcvrXcvrPropertiesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrXcvrPropertiesType.setStatus("current")
_CwsXcvrXcvrPropertiesMode_Type = XcvrMode
_CwsXcvrXcvrPropertiesMode_Object = MibTableColumn
cwsXcvrXcvrPropertiesMode = _CwsXcvrXcvrPropertiesMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 6, 1, 3),
    _CwsXcvrXcvrPropertiesMode_Type()
)
cwsXcvrXcvrPropertiesMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrXcvrPropertiesMode.setStatus("current")
_CwsXcvrXcvrPropertiesNumberOfChannels_Type = ChannelsNumber
_CwsXcvrXcvrPropertiesNumberOfChannels_Object = MibTableColumn
cwsXcvrXcvrPropertiesNumberOfChannels = _CwsXcvrXcvrPropertiesNumberOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 6, 1, 4),
    _CwsXcvrXcvrPropertiesNumberOfChannels_Type()
)
cwsXcvrXcvrPropertiesNumberOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrXcvrPropertiesNumberOfChannels.setStatus("current")
_CwsXcvrChildPtpIdTable_Object = MibTable
cwsXcvrChildPtpIdTable = _CwsXcvrChildPtpIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 7)
)
if mibBuilder.loadTexts:
    cwsXcvrChildPtpIdTable.setStatus("current")
_CwsXcvrChildPtpIdEntry_Object = MibTableRow
cwsXcvrChildPtpIdEntry = _CwsXcvrChildPtpIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 7, 1)
)
cwsXcvrChildPtpIdEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrPropertiesTableSnmpKey"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrChildPtpIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrChildPtpIdEntry.setStatus("current")


class _CwsXcvrChildPtpIdTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrChildPtpIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrChildPtpIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrChildPtpIdTableSnmpKey_Object = MibTableColumn
cwsXcvrChildPtpIdTableSnmpKey = _CwsXcvrChildPtpIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 7, 1, 1),
    _CwsXcvrChildPtpIdTableSnmpKey_Type()
)
cwsXcvrChildPtpIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrChildPtpIdTableSnmpKey.setStatus("current")
_CwsXcvrChildPtpId_Type = PtpId
_CwsXcvrChildPtpId_Object = MibTableColumn
cwsXcvrChildPtpId = _CwsXcvrChildPtpId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 7, 1, 2),
    _CwsXcvrChildPtpId_Type()
)
cwsXcvrChildPtpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrChildPtpId.setStatus("current")
_CwsXcvrCienaIdTable_Object = MibTable
cwsXcvrCienaIdTable = _CwsXcvrCienaIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 8)
)
if mibBuilder.loadTexts:
    cwsXcvrCienaIdTable.setStatus("current")
_CwsXcvrCienaIdEntry_Object = MibTableRow
cwsXcvrCienaIdEntry = _CwsXcvrCienaIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 8, 1)
)
cwsXcvrCienaIdEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrCienaIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrCienaIdEntry.setStatus("current")


class _CwsXcvrCienaIdTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrCienaIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrCienaIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrCienaIdTableSnmpKey_Object = MibTableColumn
cwsXcvrCienaIdTableSnmpKey = _CwsXcvrCienaIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 8, 1, 1),
    _CwsXcvrCienaIdTableSnmpKey_Type()
)
cwsXcvrCienaIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrCienaIdTableSnmpKey.setStatus("current")
_CwsXcvrCienaIdCienaItemNumber_Type = StringMaxl32
_CwsXcvrCienaIdCienaItemNumber_Object = MibTableColumn
cwsXcvrCienaIdCienaItemNumber = _CwsXcvrCienaIdCienaItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 8, 1, 2),
    _CwsXcvrCienaIdCienaItemNumber_Type()
)
cwsXcvrCienaIdCienaItemNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrCienaIdCienaItemNumber.setStatus("current")
_CwsXcvrCienaIdRevision_Type = StringMaxl32
_CwsXcvrCienaIdRevision_Object = MibTableColumn
cwsXcvrCienaIdRevision = _CwsXcvrCienaIdRevision_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 8, 1, 3),
    _CwsXcvrCienaIdRevision_Type()
)
cwsXcvrCienaIdRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrCienaIdRevision.setStatus("current")
_CwsXcvrCienaIdDescription_Type = StringMaxl254
_CwsXcvrCienaIdDescription_Object = MibTableColumn
cwsXcvrCienaIdDescription = _CwsXcvrCienaIdDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 8, 1, 4),
    _CwsXcvrCienaIdDescription_Type()
)
cwsXcvrCienaIdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrCienaIdDescription.setStatus("current")
_CwsXcvrVendorIdTable_Object = MibTable
cwsXcvrVendorIdTable = _CwsXcvrVendorIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 9)
)
if mibBuilder.loadTexts:
    cwsXcvrVendorIdTable.setStatus("current")
_CwsXcvrVendorIdEntry_Object = MibTableRow
cwsXcvrVendorIdEntry = _CwsXcvrVendorIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 9, 1)
)
cwsXcvrVendorIdEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrVendorIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrVendorIdEntry.setStatus("current")


class _CwsXcvrVendorIdTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrVendorIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrVendorIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrVendorIdTableSnmpKey_Object = MibTableColumn
cwsXcvrVendorIdTableSnmpKey = _CwsXcvrVendorIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 9, 1, 1),
    _CwsXcvrVendorIdTableSnmpKey_Type()
)
cwsXcvrVendorIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrVendorIdTableSnmpKey.setStatus("current")
_CwsXcvrVendorIdName_Type = StringMaxl32
_CwsXcvrVendorIdName_Object = MibTableColumn
cwsXcvrVendorIdName = _CwsXcvrVendorIdName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 9, 1, 2),
    _CwsXcvrVendorIdName_Type()
)
cwsXcvrVendorIdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrVendorIdName.setStatus("current")
_CwsXcvrVendorIdPartNumber_Type = StringMaxl32
_CwsXcvrVendorIdPartNumber_Object = MibTableColumn
cwsXcvrVendorIdPartNumber = _CwsXcvrVendorIdPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 9, 1, 3),
    _CwsXcvrVendorIdPartNumber_Type()
)
cwsXcvrVendorIdPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrVendorIdPartNumber.setStatus("current")
_CwsXcvrVendorIdRevision_Type = StringMaxl32
_CwsXcvrVendorIdRevision_Object = MibTableColumn
cwsXcvrVendorIdRevision = _CwsXcvrVendorIdRevision_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 9, 1, 4),
    _CwsXcvrVendorIdRevision_Type()
)
cwsXcvrVendorIdRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrVendorIdRevision.setStatus("current")
_CwsXcvrVendorIdSerialNumber_Type = StringMaxl32
_CwsXcvrVendorIdSerialNumber_Object = MibTableColumn
cwsXcvrVendorIdSerialNumber = _CwsXcvrVendorIdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 9, 1, 5),
    _CwsXcvrVendorIdSerialNumber_Type()
)
cwsXcvrVendorIdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrVendorIdSerialNumber.setStatus("current")
_CwsXcvrVendorIdManufacturedDate_Type = StringMaxl16
_CwsXcvrVendorIdManufacturedDate_Object = MibTableColumn
cwsXcvrVendorIdManufacturedDate = _CwsXcvrVendorIdManufacturedDate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 9, 1, 6),
    _CwsXcvrVendorIdManufacturedDate_Type()
)
cwsXcvrVendorIdManufacturedDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrVendorIdManufacturedDate.setStatus("current")
_CwsXcvrDeviceIdTable_Object = MibTable
cwsXcvrDeviceIdTable = _CwsXcvrDeviceIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 10)
)
if mibBuilder.loadTexts:
    cwsXcvrDeviceIdTable.setStatus("current")
_CwsXcvrDeviceIdEntry_Object = MibTableRow
cwsXcvrDeviceIdEntry = _CwsXcvrDeviceIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 10, 1)
)
cwsXcvrDeviceIdEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrDeviceIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrDeviceIdEntry.setStatus("current")


class _CwsXcvrDeviceIdTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrDeviceIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrDeviceIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrDeviceIdTableSnmpKey_Object = MibTableColumn
cwsXcvrDeviceIdTableSnmpKey = _CwsXcvrDeviceIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 10, 1, 1),
    _CwsXcvrDeviceIdTableSnmpKey_Type()
)
cwsXcvrDeviceIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrDeviceIdTableSnmpKey.setStatus("current")
_CwsXcvrDeviceIdConnectorType_Type = ConnectorTypeDescEnum
_CwsXcvrDeviceIdConnectorType_Object = MibTableColumn
cwsXcvrDeviceIdConnectorType = _CwsXcvrDeviceIdConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 10, 1, 2),
    _CwsXcvrDeviceIdConnectorType_Type()
)
cwsXcvrDeviceIdConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrDeviceIdConnectorType.setStatus("current")
_CwsXcvrVendorTransmitterTable_Object = MibTable
cwsXcvrVendorTransmitterTable = _CwsXcvrVendorTransmitterTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 11)
)
if mibBuilder.loadTexts:
    cwsXcvrVendorTransmitterTable.setStatus("current")
_CwsXcvrVendorTransmitterEntry_Object = MibTableRow
cwsXcvrVendorTransmitterEntry = _CwsXcvrVendorTransmitterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 11, 1)
)
cwsXcvrVendorTransmitterEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrVendorTransmitterTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrVendorTransmitterEntry.setStatus("current")


class _CwsXcvrVendorTransmitterTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrVendorTransmitterTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrVendorTransmitterTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrVendorTransmitterTableSnmpKey_Object = MibTableColumn
cwsXcvrVendorTransmitterTableSnmpKey = _CwsXcvrVendorTransmitterTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 11, 1, 1),
    _CwsXcvrVendorTransmitterTableSnmpKey_Type()
)
cwsXcvrVendorTransmitterTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrVendorTransmitterTableSnmpKey.setStatus("current")
_CwsXcvrVendorTransmitterNominalBitRate_Type = StringMaxl16
_CwsXcvrVendorTransmitterNominalBitRate_Object = MibTableColumn
cwsXcvrVendorTransmitterNominalBitRate = _CwsXcvrVendorTransmitterNominalBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 11, 1, 2),
    _CwsXcvrVendorTransmitterNominalBitRate_Type()
)
cwsXcvrVendorTransmitterNominalBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrVendorTransmitterNominalBitRate.setStatus("current")
_CwsXcvrVendorDiagnosticMonitoringTable_Object = MibTable
cwsXcvrVendorDiagnosticMonitoringTable = _CwsXcvrVendorDiagnosticMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 12)
)
if mibBuilder.loadTexts:
    cwsXcvrVendorDiagnosticMonitoringTable.setStatus("current")
_CwsXcvrVendorDiagnosticMonitoringEntry_Object = MibTableRow
cwsXcvrVendorDiagnosticMonitoringEntry = _CwsXcvrVendorDiagnosticMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 12, 1)
)
cwsXcvrVendorDiagnosticMonitoringEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrVendorDiagnosticMonitoringTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrVendorDiagnosticMonitoringEntry.setStatus("current")


class _CwsXcvrVendorDiagnosticMonitoringTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrVendorDiagnosticMonitoringTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrVendorDiagnosticMonitoringTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrVendorDiagnosticMonitoringTableSnmpKey_Object = MibTableColumn
cwsXcvrVendorDiagnosticMonitoringTableSnmpKey = _CwsXcvrVendorDiagnosticMonitoringTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 12, 1, 1),
    _CwsXcvrVendorDiagnosticMonitoringTableSnmpKey_Type()
)
cwsXcvrVendorDiagnosticMonitoringTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrVendorDiagnosticMonitoringTableSnmpKey.setStatus("current")


class _CwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement_Type(Integer32):
    """Custom type cwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("averagepower", 1),
          ("no", 3),
          ("yes", 2),
          ("zeroma", 0))
    )


_CwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement_Type.__name__ = "Integer32"
_CwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement_Object = MibTableColumn
cwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement = _CwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 12, 1, 2),
    _CwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement_Type()
)
cwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement.setStatus("current")


class _CwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement_Type(Integer32):
    """Custom type cwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 3),
          ("notsupported", 0),
          ("supported", 1),
          ("yes", 2))
    )


_CwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement_Type.__name__ = "Integer32"
_CwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement_Object = MibTableColumn
cwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement = _CwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 12, 1, 3),
    _CwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement_Type()
)
cwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement.setStatus("current")
_CwsXcvrTemperatureTable_Object = MibTable
cwsXcvrTemperatureTable = _CwsXcvrTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 13)
)
if mibBuilder.loadTexts:
    cwsXcvrTemperatureTable.setStatus("current")
_CwsXcvrTemperatureEntry_Object = MibTableRow
cwsXcvrTemperatureEntry = _CwsXcvrTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 13, 1)
)
cwsXcvrTemperatureEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrTemperatureTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrTemperatureEntry.setStatus("current")


class _CwsXcvrTemperatureTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrTemperatureTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrTemperatureTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrTemperatureTableSnmpKey_Object = MibTableColumn
cwsXcvrTemperatureTableSnmpKey = _CwsXcvrTemperatureTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 13, 1, 1),
    _CwsXcvrTemperatureTableSnmpKey_Type()
)
cwsXcvrTemperatureTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrTemperatureTableSnmpKey.setStatus("current")
_CwsXcvrTemperatureActual_Type = Integer32
_CwsXcvrTemperatureActual_Object = MibTableColumn
cwsXcvrTemperatureActual = _CwsXcvrTemperatureActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 13, 1, 2),
    _CwsXcvrTemperatureActual_Type()
)
cwsXcvrTemperatureActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTemperatureActual.setStatus("current")
_CwsXcvrTemperatureStatusTable_Object = MibTable
cwsXcvrTemperatureStatusTable = _CwsXcvrTemperatureStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 14)
)
if mibBuilder.loadTexts:
    cwsXcvrTemperatureStatusTable.setStatus("current")
_CwsXcvrTemperatureStatusEntry_Object = MibTableRow
cwsXcvrTemperatureStatusEntry = _CwsXcvrTemperatureStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 14, 1)
)
cwsXcvrTemperatureStatusEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrTemperatureStatusTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrTemperatureStatusEntry.setStatus("current")


class _CwsXcvrTemperatureStatusTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrTemperatureStatusTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrTemperatureStatusTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrTemperatureStatusTableSnmpKey_Object = MibTableColumn
cwsXcvrTemperatureStatusTableSnmpKey = _CwsXcvrTemperatureStatusTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 14, 1, 1),
    _CwsXcvrTemperatureStatusTableSnmpKey_Type()
)
cwsXcvrTemperatureStatusTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrTemperatureStatusTableSnmpKey.setStatus("current")
_CwsXcvrTemperatureStatusHighAlarmStatus_Type = TruthValue
_CwsXcvrTemperatureStatusHighAlarmStatus_Object = MibTableColumn
cwsXcvrTemperatureStatusHighAlarmStatus = _CwsXcvrTemperatureStatusHighAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 14, 1, 2),
    _CwsXcvrTemperatureStatusHighAlarmStatus_Type()
)
cwsXcvrTemperatureStatusHighAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTemperatureStatusHighAlarmStatus.setStatus("current")
_CwsXcvrTemperatureStatusLowAlarmStatus_Type = TruthValue
_CwsXcvrTemperatureStatusLowAlarmStatus_Object = MibTableColumn
cwsXcvrTemperatureStatusLowAlarmStatus = _CwsXcvrTemperatureStatusLowAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 14, 1, 3),
    _CwsXcvrTemperatureStatusLowAlarmStatus_Type()
)
cwsXcvrTemperatureStatusLowAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTemperatureStatusLowAlarmStatus.setStatus("current")
_CwsXcvrTemperatureStatusHighWarningStatus_Type = TruthValue
_CwsXcvrTemperatureStatusHighWarningStatus_Object = MibTableColumn
cwsXcvrTemperatureStatusHighWarningStatus = _CwsXcvrTemperatureStatusHighWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 14, 1, 4),
    _CwsXcvrTemperatureStatusHighWarningStatus_Type()
)
cwsXcvrTemperatureStatusHighWarningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTemperatureStatusHighWarningStatus.setStatus("current")
_CwsXcvrTemperatureStatusLowWarningStatus_Type = TruthValue
_CwsXcvrTemperatureStatusLowWarningStatus_Object = MibTableColumn
cwsXcvrTemperatureStatusLowWarningStatus = _CwsXcvrTemperatureStatusLowWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 14, 1, 5),
    _CwsXcvrTemperatureStatusLowWarningStatus_Type()
)
cwsXcvrTemperatureStatusLowWarningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTemperatureStatusLowWarningStatus.setStatus("current")
_CwsXcvrTemperatureThresholdTable_Object = MibTable
cwsXcvrTemperatureThresholdTable = _CwsXcvrTemperatureThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 15)
)
if mibBuilder.loadTexts:
    cwsXcvrTemperatureThresholdTable.setStatus("current")
_CwsXcvrTemperatureThresholdEntry_Object = MibTableRow
cwsXcvrTemperatureThresholdEntry = _CwsXcvrTemperatureThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 15, 1)
)
cwsXcvrTemperatureThresholdEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrTemperatureThresholdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrTemperatureThresholdEntry.setStatus("current")


class _CwsXcvrTemperatureThresholdTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrTemperatureThresholdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrTemperatureThresholdTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrTemperatureThresholdTableSnmpKey_Object = MibTableColumn
cwsXcvrTemperatureThresholdTableSnmpKey = _CwsXcvrTemperatureThresholdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 15, 1, 1),
    _CwsXcvrTemperatureThresholdTableSnmpKey_Type()
)
cwsXcvrTemperatureThresholdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrTemperatureThresholdTableSnmpKey.setStatus("current")
_CwsXcvrTemperatureThresholdHighAlarmThreshold_Type = Integer32
_CwsXcvrTemperatureThresholdHighAlarmThreshold_Object = MibTableColumn
cwsXcvrTemperatureThresholdHighAlarmThreshold = _CwsXcvrTemperatureThresholdHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 15, 1, 2),
    _CwsXcvrTemperatureThresholdHighAlarmThreshold_Type()
)
cwsXcvrTemperatureThresholdHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTemperatureThresholdHighAlarmThreshold.setStatus("current")
_CwsXcvrTemperatureThresholdLowAlarmThreshold_Type = Integer32
_CwsXcvrTemperatureThresholdLowAlarmThreshold_Object = MibTableColumn
cwsXcvrTemperatureThresholdLowAlarmThreshold = _CwsXcvrTemperatureThresholdLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 15, 1, 3),
    _CwsXcvrTemperatureThresholdLowAlarmThreshold_Type()
)
cwsXcvrTemperatureThresholdLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTemperatureThresholdLowAlarmThreshold.setStatus("current")
_CwsXcvrTemperatureThresholdHighWarningThreshold_Type = Integer32
_CwsXcvrTemperatureThresholdHighWarningThreshold_Object = MibTableColumn
cwsXcvrTemperatureThresholdHighWarningThreshold = _CwsXcvrTemperatureThresholdHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 15, 1, 4),
    _CwsXcvrTemperatureThresholdHighWarningThreshold_Type()
)
cwsXcvrTemperatureThresholdHighWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTemperatureThresholdHighWarningThreshold.setStatus("current")
_CwsXcvrTemperatureThresholdLowWarningThreshold_Type = Integer32
_CwsXcvrTemperatureThresholdLowWarningThreshold_Object = MibTableColumn
cwsXcvrTemperatureThresholdLowWarningThreshold = _CwsXcvrTemperatureThresholdLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 15, 1, 5),
    _CwsXcvrTemperatureThresholdLowWarningThreshold_Type()
)
cwsXcvrTemperatureThresholdLowWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTemperatureThresholdLowWarningThreshold.setStatus("current")
_CwsXcvrChannelDiagnosticsTable_Object = MibTable
cwsXcvrChannelDiagnosticsTable = _CwsXcvrChannelDiagnosticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 16)
)
if mibBuilder.loadTexts:
    cwsXcvrChannelDiagnosticsTable.setStatus("current")
_CwsXcvrChannelDiagnosticsEntry_Object = MibTableRow
cwsXcvrChannelDiagnosticsEntry = _CwsXcvrChannelDiagnosticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 16, 1)
)
cwsXcvrChannelDiagnosticsEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrChannelDiagnosticsChannelNumber"),
)
if mibBuilder.loadTexts:
    cwsXcvrChannelDiagnosticsEntry.setStatus("current")


class _CwsXcvrChannelDiagnosticsChannelNumber_Type(Integer32):
    """Custom type cwsXcvrChannelDiagnosticsChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrChannelDiagnosticsChannelNumber_Type.__name__ = "Integer32"
_CwsXcvrChannelDiagnosticsChannelNumber_Object = MibTableColumn
cwsXcvrChannelDiagnosticsChannelNumber = _CwsXcvrChannelDiagnosticsChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 16, 1, 1),
    _CwsXcvrChannelDiagnosticsChannelNumber_Type()
)
cwsXcvrChannelDiagnosticsChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrChannelDiagnosticsChannelNumber.setStatus("current")
_CwsXcvrChannelRxPowerTable_Object = MibTable
cwsXcvrChannelRxPowerTable = _CwsXcvrChannelRxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 17)
)
if mibBuilder.loadTexts:
    cwsXcvrChannelRxPowerTable.setStatus("current")
_CwsXcvrChannelRxPowerEntry_Object = MibTableRow
cwsXcvrChannelRxPowerEntry = _CwsXcvrChannelRxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 17, 1)
)
cwsXcvrChannelRxPowerEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrChannelDiagnosticsChannelNumber"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrChannelRxPowerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrChannelRxPowerEntry.setStatus("current")


class _CwsXcvrChannelRxPowerTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrChannelRxPowerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrChannelRxPowerTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrChannelRxPowerTableSnmpKey_Object = MibTableColumn
cwsXcvrChannelRxPowerTableSnmpKey = _CwsXcvrChannelRxPowerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 17, 1, 1),
    _CwsXcvrChannelRxPowerTableSnmpKey_Type()
)
cwsXcvrChannelRxPowerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrChannelRxPowerTableSnmpKey.setStatus("current")
_CwsXcvrChannelRxPowerActual_Type = Decimal1Dig
_CwsXcvrChannelRxPowerActual_Object = MibTableColumn
cwsXcvrChannelRxPowerActual = _CwsXcvrChannelRxPowerActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 17, 1, 2),
    _CwsXcvrChannelRxPowerActual_Type()
)
cwsXcvrChannelRxPowerActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrChannelRxPowerActual.setStatus("current")
_CwsXcvrRxPowerStatusTable_Object = MibTable
cwsXcvrRxPowerStatusTable = _CwsXcvrRxPowerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 18)
)
if mibBuilder.loadTexts:
    cwsXcvrRxPowerStatusTable.setStatus("current")
_CwsXcvrRxPowerStatusEntry_Object = MibTableRow
cwsXcvrRxPowerStatusEntry = _CwsXcvrRxPowerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 18, 1)
)
cwsXcvrRxPowerStatusEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrChannelDiagnosticsChannelNumber"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrRxPowerStatusTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrRxPowerStatusEntry.setStatus("current")


class _CwsXcvrRxPowerStatusTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrRxPowerStatusTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrRxPowerStatusTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrRxPowerStatusTableSnmpKey_Object = MibTableColumn
cwsXcvrRxPowerStatusTableSnmpKey = _CwsXcvrRxPowerStatusTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 18, 1, 1),
    _CwsXcvrRxPowerStatusTableSnmpKey_Type()
)
cwsXcvrRxPowerStatusTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrRxPowerStatusTableSnmpKey.setStatus("current")
_CwsXcvrRxPowerStatusHighAlarmStatus_Type = TruthValue
_CwsXcvrRxPowerStatusHighAlarmStatus_Object = MibTableColumn
cwsXcvrRxPowerStatusHighAlarmStatus = _CwsXcvrRxPowerStatusHighAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 18, 1, 2),
    _CwsXcvrRxPowerStatusHighAlarmStatus_Type()
)
cwsXcvrRxPowerStatusHighAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrRxPowerStatusHighAlarmStatus.setStatus("current")
_CwsXcvrRxPowerStatusLowAlarmStatus_Type = TruthValue
_CwsXcvrRxPowerStatusLowAlarmStatus_Object = MibTableColumn
cwsXcvrRxPowerStatusLowAlarmStatus = _CwsXcvrRxPowerStatusLowAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 18, 1, 3),
    _CwsXcvrRxPowerStatusLowAlarmStatus_Type()
)
cwsXcvrRxPowerStatusLowAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrRxPowerStatusLowAlarmStatus.setStatus("current")
_CwsXcvrRxPowerStatusHighWarningStatus_Type = TruthValue
_CwsXcvrRxPowerStatusHighWarningStatus_Object = MibTableColumn
cwsXcvrRxPowerStatusHighWarningStatus = _CwsXcvrRxPowerStatusHighWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 18, 1, 4),
    _CwsXcvrRxPowerStatusHighWarningStatus_Type()
)
cwsXcvrRxPowerStatusHighWarningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrRxPowerStatusHighWarningStatus.setStatus("current")
_CwsXcvrRxPowerStatusLowWarningStatus_Type = TruthValue
_CwsXcvrRxPowerStatusLowWarningStatus_Object = MibTableColumn
cwsXcvrRxPowerStatusLowWarningStatus = _CwsXcvrRxPowerStatusLowWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 18, 1, 5),
    _CwsXcvrRxPowerStatusLowWarningStatus_Type()
)
cwsXcvrRxPowerStatusLowWarningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrRxPowerStatusLowWarningStatus.setStatus("current")
_CwsXcvrRxPowerThresholdTable_Object = MibTable
cwsXcvrRxPowerThresholdTable = _CwsXcvrRxPowerThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 19)
)
if mibBuilder.loadTexts:
    cwsXcvrRxPowerThresholdTable.setStatus("current")
_CwsXcvrRxPowerThresholdEntry_Object = MibTableRow
cwsXcvrRxPowerThresholdEntry = _CwsXcvrRxPowerThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 19, 1)
)
cwsXcvrRxPowerThresholdEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrChannelDiagnosticsChannelNumber"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrRxPowerThresholdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrRxPowerThresholdEntry.setStatus("current")


class _CwsXcvrRxPowerThresholdTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrRxPowerThresholdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrRxPowerThresholdTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrRxPowerThresholdTableSnmpKey_Object = MibTableColumn
cwsXcvrRxPowerThresholdTableSnmpKey = _CwsXcvrRxPowerThresholdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 19, 1, 1),
    _CwsXcvrRxPowerThresholdTableSnmpKey_Type()
)
cwsXcvrRxPowerThresholdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrRxPowerThresholdTableSnmpKey.setStatus("current")
_CwsXcvrRxPowerThresholdHighAlarmThreshold_Type = Decimal1Dig
_CwsXcvrRxPowerThresholdHighAlarmThreshold_Object = MibTableColumn
cwsXcvrRxPowerThresholdHighAlarmThreshold = _CwsXcvrRxPowerThresholdHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 19, 1, 2),
    _CwsXcvrRxPowerThresholdHighAlarmThreshold_Type()
)
cwsXcvrRxPowerThresholdHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrRxPowerThresholdHighAlarmThreshold.setStatus("current")
_CwsXcvrRxPowerThresholdLowAlarmThreshold_Type = Decimal1Dig
_CwsXcvrRxPowerThresholdLowAlarmThreshold_Object = MibTableColumn
cwsXcvrRxPowerThresholdLowAlarmThreshold = _CwsXcvrRxPowerThresholdLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 19, 1, 3),
    _CwsXcvrRxPowerThresholdLowAlarmThreshold_Type()
)
cwsXcvrRxPowerThresholdLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrRxPowerThresholdLowAlarmThreshold.setStatus("current")
_CwsXcvrRxPowerThresholdHighWarningThreshold_Type = Decimal1Dig
_CwsXcvrRxPowerThresholdHighWarningThreshold_Object = MibTableColumn
cwsXcvrRxPowerThresholdHighWarningThreshold = _CwsXcvrRxPowerThresholdHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 19, 1, 4),
    _CwsXcvrRxPowerThresholdHighWarningThreshold_Type()
)
cwsXcvrRxPowerThresholdHighWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrRxPowerThresholdHighWarningThreshold.setStatus("current")
_CwsXcvrRxPowerThresholdLowWarningThreshold_Type = Decimal1Dig
_CwsXcvrRxPowerThresholdLowWarningThreshold_Object = MibTableColumn
cwsXcvrRxPowerThresholdLowWarningThreshold = _CwsXcvrRxPowerThresholdLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 19, 1, 5),
    _CwsXcvrRxPowerThresholdLowWarningThreshold_Type()
)
cwsXcvrRxPowerThresholdLowWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrRxPowerThresholdLowWarningThreshold.setStatus("current")
_CwsXcvrChannelTxPowerTable_Object = MibTable
cwsXcvrChannelTxPowerTable = _CwsXcvrChannelTxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 20)
)
if mibBuilder.loadTexts:
    cwsXcvrChannelTxPowerTable.setStatus("current")
_CwsXcvrChannelTxPowerEntry_Object = MibTableRow
cwsXcvrChannelTxPowerEntry = _CwsXcvrChannelTxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 20, 1)
)
cwsXcvrChannelTxPowerEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrChannelDiagnosticsChannelNumber"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrChannelTxPowerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrChannelTxPowerEntry.setStatus("current")


class _CwsXcvrChannelTxPowerTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrChannelTxPowerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrChannelTxPowerTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrChannelTxPowerTableSnmpKey_Object = MibTableColumn
cwsXcvrChannelTxPowerTableSnmpKey = _CwsXcvrChannelTxPowerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 20, 1, 1),
    _CwsXcvrChannelTxPowerTableSnmpKey_Type()
)
cwsXcvrChannelTxPowerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrChannelTxPowerTableSnmpKey.setStatus("current")
_CwsXcvrChannelTxPowerActual_Type = Decimal1Dig
_CwsXcvrChannelTxPowerActual_Object = MibTableColumn
cwsXcvrChannelTxPowerActual = _CwsXcvrChannelTxPowerActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 20, 1, 2),
    _CwsXcvrChannelTxPowerActual_Type()
)
cwsXcvrChannelTxPowerActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrChannelTxPowerActual.setStatus("current")
_CwsXcvrTxPowerStatusTable_Object = MibTable
cwsXcvrTxPowerStatusTable = _CwsXcvrTxPowerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 21)
)
if mibBuilder.loadTexts:
    cwsXcvrTxPowerStatusTable.setStatus("current")
_CwsXcvrTxPowerStatusEntry_Object = MibTableRow
cwsXcvrTxPowerStatusEntry = _CwsXcvrTxPowerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 21, 1)
)
cwsXcvrTxPowerStatusEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrChannelDiagnosticsChannelNumber"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrTxPowerStatusTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrTxPowerStatusEntry.setStatus("current")


class _CwsXcvrTxPowerStatusTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrTxPowerStatusTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrTxPowerStatusTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrTxPowerStatusTableSnmpKey_Object = MibTableColumn
cwsXcvrTxPowerStatusTableSnmpKey = _CwsXcvrTxPowerStatusTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 21, 1, 1),
    _CwsXcvrTxPowerStatusTableSnmpKey_Type()
)
cwsXcvrTxPowerStatusTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrTxPowerStatusTableSnmpKey.setStatus("current")
_CwsXcvrTxPowerStatusHighAlarmStatus_Type = TruthValue
_CwsXcvrTxPowerStatusHighAlarmStatus_Object = MibTableColumn
cwsXcvrTxPowerStatusHighAlarmStatus = _CwsXcvrTxPowerStatusHighAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 21, 1, 2),
    _CwsXcvrTxPowerStatusHighAlarmStatus_Type()
)
cwsXcvrTxPowerStatusHighAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTxPowerStatusHighAlarmStatus.setStatus("current")
_CwsXcvrTxPowerStatusLowAlarmStatus_Type = TruthValue
_CwsXcvrTxPowerStatusLowAlarmStatus_Object = MibTableColumn
cwsXcvrTxPowerStatusLowAlarmStatus = _CwsXcvrTxPowerStatusLowAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 21, 1, 3),
    _CwsXcvrTxPowerStatusLowAlarmStatus_Type()
)
cwsXcvrTxPowerStatusLowAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTxPowerStatusLowAlarmStatus.setStatus("current")
_CwsXcvrTxPowerStatusHighWarningStatus_Type = TruthValue
_CwsXcvrTxPowerStatusHighWarningStatus_Object = MibTableColumn
cwsXcvrTxPowerStatusHighWarningStatus = _CwsXcvrTxPowerStatusHighWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 21, 1, 4),
    _CwsXcvrTxPowerStatusHighWarningStatus_Type()
)
cwsXcvrTxPowerStatusHighWarningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTxPowerStatusHighWarningStatus.setStatus("current")
_CwsXcvrTxPowerStatusLowWarningStatus_Type = TruthValue
_CwsXcvrTxPowerStatusLowWarningStatus_Object = MibTableColumn
cwsXcvrTxPowerStatusLowWarningStatus = _CwsXcvrTxPowerStatusLowWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 21, 1, 5),
    _CwsXcvrTxPowerStatusLowWarningStatus_Type()
)
cwsXcvrTxPowerStatusLowWarningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTxPowerStatusLowWarningStatus.setStatus("current")
_CwsXcvrTxPowerThresholdTable_Object = MibTable
cwsXcvrTxPowerThresholdTable = _CwsXcvrTxPowerThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 22)
)
if mibBuilder.loadTexts:
    cwsXcvrTxPowerThresholdTable.setStatus("current")
_CwsXcvrTxPowerThresholdEntry_Object = MibTableRow
cwsXcvrTxPowerThresholdEntry = _CwsXcvrTxPowerThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 22, 1)
)
cwsXcvrTxPowerThresholdEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrChannelDiagnosticsChannelNumber"),
    (0, "CIENA-WS-XCVR-MIB", "cwsXcvrTxPowerThresholdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrTxPowerThresholdEntry.setStatus("current")


class _CwsXcvrTxPowerThresholdTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrTxPowerThresholdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrTxPowerThresholdTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrTxPowerThresholdTableSnmpKey_Object = MibTableColumn
cwsXcvrTxPowerThresholdTableSnmpKey = _CwsXcvrTxPowerThresholdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 22, 1, 1),
    _CwsXcvrTxPowerThresholdTableSnmpKey_Type()
)
cwsXcvrTxPowerThresholdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrTxPowerThresholdTableSnmpKey.setStatus("current")
_CwsXcvrTxPowerThresholdHighAlarmThreshold_Type = Decimal1Dig
_CwsXcvrTxPowerThresholdHighAlarmThreshold_Object = MibTableColumn
cwsXcvrTxPowerThresholdHighAlarmThreshold = _CwsXcvrTxPowerThresholdHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 22, 1, 2),
    _CwsXcvrTxPowerThresholdHighAlarmThreshold_Type()
)
cwsXcvrTxPowerThresholdHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTxPowerThresholdHighAlarmThreshold.setStatus("current")
_CwsXcvrTxPowerThresholdLowAlarmThreshold_Type = Decimal1Dig
_CwsXcvrTxPowerThresholdLowAlarmThreshold_Object = MibTableColumn
cwsXcvrTxPowerThresholdLowAlarmThreshold = _CwsXcvrTxPowerThresholdLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 22, 1, 3),
    _CwsXcvrTxPowerThresholdLowAlarmThreshold_Type()
)
cwsXcvrTxPowerThresholdLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTxPowerThresholdLowAlarmThreshold.setStatus("current")
_CwsXcvrTxPowerThresholdHighWarningThreshold_Type = Decimal1Dig
_CwsXcvrTxPowerThresholdHighWarningThreshold_Object = MibTableColumn
cwsXcvrTxPowerThresholdHighWarningThreshold = _CwsXcvrTxPowerThresholdHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 22, 1, 4),
    _CwsXcvrTxPowerThresholdHighWarningThreshold_Type()
)
cwsXcvrTxPowerThresholdHighWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTxPowerThresholdHighWarningThreshold.setStatus("current")
_CwsXcvrTxPowerThresholdLowWarningThreshold_Type = Decimal1Dig
_CwsXcvrTxPowerThresholdLowWarningThreshold_Object = MibTableColumn
cwsXcvrTxPowerThresholdLowWarningThreshold = _CwsXcvrTxPowerThresholdLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 22, 1, 5),
    _CwsXcvrTxPowerThresholdLowWarningThreshold_Type()
)
cwsXcvrTxPowerThresholdLowWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTxPowerThresholdLowWarningThreshold.setStatus("current")

# Managed Objects groups

cienaWsXcvrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 2, 1, 1)
)
cienaWsXcvrGroup.setObjects(
      *(("CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrXcvrIdName"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrXcvrIdDescription"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrXcvrStateAdminState"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrXcvrStateOperationalState"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrXcvrStatePowerState"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrXcvrPropertiesType"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrXcvrPropertiesMode"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrXcvrPropertiesNumberOfChannels"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrCienaIdCienaItemNumber"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrCienaIdRevision"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrCienaIdDescription"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrVendorIdName"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrVendorIdPartNumber"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrVendorIdRevision"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrVendorIdSerialNumber"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrVendorIdManufacturedDate"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrDeviceIdConnectorType"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrVendorTransmitterNominalBitRate"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrTemperatureActual"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrTemperatureStatusHighAlarmStatus"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrTemperatureStatusLowAlarmStatus"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrTemperatureStatusHighWarningStatus"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrTemperatureStatusLowWarningStatus"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrTemperatureThresholdHighAlarmThreshold"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrTemperatureThresholdLowAlarmThreshold"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrTemperatureThresholdHighWarningThreshold"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrTemperatureThresholdLowWarningThreshold"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrChannelDiagnosticsChannelNumber"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrChannelRxPowerActual"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrRxPowerStatusHighAlarmStatus"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrRxPowerStatusLowAlarmStatus"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrRxPowerStatusHighWarningStatus"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrRxPowerStatusLowWarningStatus"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrRxPowerThresholdHighAlarmThreshold"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrRxPowerThresholdLowAlarmThreshold"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrRxPowerThresholdHighWarningThreshold"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrRxPowerThresholdLowWarningThreshold"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrChannelTxPowerActual"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrTxPowerStatusHighAlarmStatus"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrTxPowerStatusLowAlarmStatus"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrTxPowerStatusHighWarningStatus"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrTxPowerStatusLowWarningStatus"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrTxPowerThresholdHighAlarmThreshold"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrTxPowerThresholdLowAlarmThreshold"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrTxPowerThresholdHighWarningThreshold"),
        ("CIENA-WS-XCVR-MIB", "cwsXcvrTxPowerThresholdLowWarningThreshold"))
)
if mibBuilder.loadTexts:
    cienaWsXcvrGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cienaWsXcvrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cienaWsXcvrCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-XCVR-MIB",
    **{"XcvrOpEnum": XcvrOpEnum,
       "cienaWsXcvrMIB": cienaWsXcvrMIB,
       "cienaWsXcvrObjects": cienaWsXcvrObjects,
       "cienaWsXcvrConformance": cienaWsXcvrConformance,
       "cienaWsXcvrGroups": cienaWsXcvrGroups,
       "cienaWsXcvrGroup": cienaWsXcvrGroup,
       "cienaWsXcvrCompliances": cienaWsXcvrCompliances,
       "cienaWsXcvrCompliance": cienaWsXcvrCompliance,
       "cwsXcvrXcvrsTable": cwsXcvrXcvrsTable,
       "cwsXcvrXcvrsEntry": cwsXcvrXcvrsEntry,
       "cwsXcvrXcvrsXcvrIndex": cwsXcvrXcvrsXcvrIndex,
       "cwsXcvrXcvrIdTable": cwsXcvrXcvrIdTable,
       "cwsXcvrXcvrIdEntry": cwsXcvrXcvrIdEntry,
       "cwsXcvrXcvrIdTableSnmpKey": cwsXcvrXcvrIdTableSnmpKey,
       "cwsXcvrXcvrIdName": cwsXcvrXcvrIdName,
       "cwsXcvrXcvrIdDescription": cwsXcvrXcvrIdDescription,
       "cwsXcvrXcvrStateTable": cwsXcvrXcvrStateTable,
       "cwsXcvrXcvrStateEntry": cwsXcvrXcvrStateEntry,
       "cwsXcvrXcvrStateTableSnmpKey": cwsXcvrXcvrStateTableSnmpKey,
       "cwsXcvrXcvrStateAdminState": cwsXcvrXcvrStateAdminState,
       "cwsXcvrXcvrStateOperationalState": cwsXcvrXcvrStateOperationalState,
       "cwsXcvrXcvrStatePowerState": cwsXcvrXcvrStatePowerState,
       "cwsXcvrXcvrPropertiesTable": cwsXcvrXcvrPropertiesTable,
       "cwsXcvrXcvrPropertiesEntry": cwsXcvrXcvrPropertiesEntry,
       "cwsXcvrXcvrPropertiesTableSnmpKey": cwsXcvrXcvrPropertiesTableSnmpKey,
       "cwsXcvrXcvrPropertiesType": cwsXcvrXcvrPropertiesType,
       "cwsXcvrXcvrPropertiesMode": cwsXcvrXcvrPropertiesMode,
       "cwsXcvrXcvrPropertiesNumberOfChannels": cwsXcvrXcvrPropertiesNumberOfChannels,
       "cwsXcvrChildPtpIdTable": cwsXcvrChildPtpIdTable,
       "cwsXcvrChildPtpIdEntry": cwsXcvrChildPtpIdEntry,
       "cwsXcvrChildPtpIdTableSnmpKey": cwsXcvrChildPtpIdTableSnmpKey,
       "cwsXcvrChildPtpId": cwsXcvrChildPtpId,
       "cwsXcvrCienaIdTable": cwsXcvrCienaIdTable,
       "cwsXcvrCienaIdEntry": cwsXcvrCienaIdEntry,
       "cwsXcvrCienaIdTableSnmpKey": cwsXcvrCienaIdTableSnmpKey,
       "cwsXcvrCienaIdCienaItemNumber": cwsXcvrCienaIdCienaItemNumber,
       "cwsXcvrCienaIdRevision": cwsXcvrCienaIdRevision,
       "cwsXcvrCienaIdDescription": cwsXcvrCienaIdDescription,
       "cwsXcvrVendorIdTable": cwsXcvrVendorIdTable,
       "cwsXcvrVendorIdEntry": cwsXcvrVendorIdEntry,
       "cwsXcvrVendorIdTableSnmpKey": cwsXcvrVendorIdTableSnmpKey,
       "cwsXcvrVendorIdName": cwsXcvrVendorIdName,
       "cwsXcvrVendorIdPartNumber": cwsXcvrVendorIdPartNumber,
       "cwsXcvrVendorIdRevision": cwsXcvrVendorIdRevision,
       "cwsXcvrVendorIdSerialNumber": cwsXcvrVendorIdSerialNumber,
       "cwsXcvrVendorIdManufacturedDate": cwsXcvrVendorIdManufacturedDate,
       "cwsXcvrDeviceIdTable": cwsXcvrDeviceIdTable,
       "cwsXcvrDeviceIdEntry": cwsXcvrDeviceIdEntry,
       "cwsXcvrDeviceIdTableSnmpKey": cwsXcvrDeviceIdTableSnmpKey,
       "cwsXcvrDeviceIdConnectorType": cwsXcvrDeviceIdConnectorType,
       "cwsXcvrVendorTransmitterTable": cwsXcvrVendorTransmitterTable,
       "cwsXcvrVendorTransmitterEntry": cwsXcvrVendorTransmitterEntry,
       "cwsXcvrVendorTransmitterTableSnmpKey": cwsXcvrVendorTransmitterTableSnmpKey,
       "cwsXcvrVendorTransmitterNominalBitRate": cwsXcvrVendorTransmitterNominalBitRate,
       "cwsXcvrVendorDiagnosticMonitoringTable": cwsXcvrVendorDiagnosticMonitoringTable,
       "cwsXcvrVendorDiagnosticMonitoringEntry": cwsXcvrVendorDiagnosticMonitoringEntry,
       "cwsXcvrVendorDiagnosticMonitoringTableSnmpKey": cwsXcvrVendorDiagnosticMonitoringTableSnmpKey,
       "cwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement": cwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement,
       "cwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement": cwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement,
       "cwsXcvrTemperatureTable": cwsXcvrTemperatureTable,
       "cwsXcvrTemperatureEntry": cwsXcvrTemperatureEntry,
       "cwsXcvrTemperatureTableSnmpKey": cwsXcvrTemperatureTableSnmpKey,
       "cwsXcvrTemperatureActual": cwsXcvrTemperatureActual,
       "cwsXcvrTemperatureStatusTable": cwsXcvrTemperatureStatusTable,
       "cwsXcvrTemperatureStatusEntry": cwsXcvrTemperatureStatusEntry,
       "cwsXcvrTemperatureStatusTableSnmpKey": cwsXcvrTemperatureStatusTableSnmpKey,
       "cwsXcvrTemperatureStatusHighAlarmStatus": cwsXcvrTemperatureStatusHighAlarmStatus,
       "cwsXcvrTemperatureStatusLowAlarmStatus": cwsXcvrTemperatureStatusLowAlarmStatus,
       "cwsXcvrTemperatureStatusHighWarningStatus": cwsXcvrTemperatureStatusHighWarningStatus,
       "cwsXcvrTemperatureStatusLowWarningStatus": cwsXcvrTemperatureStatusLowWarningStatus,
       "cwsXcvrTemperatureThresholdTable": cwsXcvrTemperatureThresholdTable,
       "cwsXcvrTemperatureThresholdEntry": cwsXcvrTemperatureThresholdEntry,
       "cwsXcvrTemperatureThresholdTableSnmpKey": cwsXcvrTemperatureThresholdTableSnmpKey,
       "cwsXcvrTemperatureThresholdHighAlarmThreshold": cwsXcvrTemperatureThresholdHighAlarmThreshold,
       "cwsXcvrTemperatureThresholdLowAlarmThreshold": cwsXcvrTemperatureThresholdLowAlarmThreshold,
       "cwsXcvrTemperatureThresholdHighWarningThreshold": cwsXcvrTemperatureThresholdHighWarningThreshold,
       "cwsXcvrTemperatureThresholdLowWarningThreshold": cwsXcvrTemperatureThresholdLowWarningThreshold,
       "cwsXcvrChannelDiagnosticsTable": cwsXcvrChannelDiagnosticsTable,
       "cwsXcvrChannelDiagnosticsEntry": cwsXcvrChannelDiagnosticsEntry,
       "cwsXcvrChannelDiagnosticsChannelNumber": cwsXcvrChannelDiagnosticsChannelNumber,
       "cwsXcvrChannelRxPowerTable": cwsXcvrChannelRxPowerTable,
       "cwsXcvrChannelRxPowerEntry": cwsXcvrChannelRxPowerEntry,
       "cwsXcvrChannelRxPowerTableSnmpKey": cwsXcvrChannelRxPowerTableSnmpKey,
       "cwsXcvrChannelRxPowerActual": cwsXcvrChannelRxPowerActual,
       "cwsXcvrRxPowerStatusTable": cwsXcvrRxPowerStatusTable,
       "cwsXcvrRxPowerStatusEntry": cwsXcvrRxPowerStatusEntry,
       "cwsXcvrRxPowerStatusTableSnmpKey": cwsXcvrRxPowerStatusTableSnmpKey,
       "cwsXcvrRxPowerStatusHighAlarmStatus": cwsXcvrRxPowerStatusHighAlarmStatus,
       "cwsXcvrRxPowerStatusLowAlarmStatus": cwsXcvrRxPowerStatusLowAlarmStatus,
       "cwsXcvrRxPowerStatusHighWarningStatus": cwsXcvrRxPowerStatusHighWarningStatus,
       "cwsXcvrRxPowerStatusLowWarningStatus": cwsXcvrRxPowerStatusLowWarningStatus,
       "cwsXcvrRxPowerThresholdTable": cwsXcvrRxPowerThresholdTable,
       "cwsXcvrRxPowerThresholdEntry": cwsXcvrRxPowerThresholdEntry,
       "cwsXcvrRxPowerThresholdTableSnmpKey": cwsXcvrRxPowerThresholdTableSnmpKey,
       "cwsXcvrRxPowerThresholdHighAlarmThreshold": cwsXcvrRxPowerThresholdHighAlarmThreshold,
       "cwsXcvrRxPowerThresholdLowAlarmThreshold": cwsXcvrRxPowerThresholdLowAlarmThreshold,
       "cwsXcvrRxPowerThresholdHighWarningThreshold": cwsXcvrRxPowerThresholdHighWarningThreshold,
       "cwsXcvrRxPowerThresholdLowWarningThreshold": cwsXcvrRxPowerThresholdLowWarningThreshold,
       "cwsXcvrChannelTxPowerTable": cwsXcvrChannelTxPowerTable,
       "cwsXcvrChannelTxPowerEntry": cwsXcvrChannelTxPowerEntry,
       "cwsXcvrChannelTxPowerTableSnmpKey": cwsXcvrChannelTxPowerTableSnmpKey,
       "cwsXcvrChannelTxPowerActual": cwsXcvrChannelTxPowerActual,
       "cwsXcvrTxPowerStatusTable": cwsXcvrTxPowerStatusTable,
       "cwsXcvrTxPowerStatusEntry": cwsXcvrTxPowerStatusEntry,
       "cwsXcvrTxPowerStatusTableSnmpKey": cwsXcvrTxPowerStatusTableSnmpKey,
       "cwsXcvrTxPowerStatusHighAlarmStatus": cwsXcvrTxPowerStatusHighAlarmStatus,
       "cwsXcvrTxPowerStatusLowAlarmStatus": cwsXcvrTxPowerStatusLowAlarmStatus,
       "cwsXcvrTxPowerStatusHighWarningStatus": cwsXcvrTxPowerStatusHighWarningStatus,
       "cwsXcvrTxPowerStatusLowWarningStatus": cwsXcvrTxPowerStatusLowWarningStatus,
       "cwsXcvrTxPowerThresholdTable": cwsXcvrTxPowerThresholdTable,
       "cwsXcvrTxPowerThresholdEntry": cwsXcvrTxPowerThresholdEntry,
       "cwsXcvrTxPowerThresholdTableSnmpKey": cwsXcvrTxPowerThresholdTableSnmpKey,
       "cwsXcvrTxPowerThresholdHighAlarmThreshold": cwsXcvrTxPowerThresholdHighAlarmThreshold,
       "cwsXcvrTxPowerThresholdLowAlarmThreshold": cwsXcvrTxPowerThresholdLowAlarmThreshold,
       "cwsXcvrTxPowerThresholdHighWarningThreshold": cwsXcvrTxPowerThresholdHighWarningThreshold,
       "cwsXcvrTxPowerThresholdLowWarningThreshold": cwsXcvrTxPowerThresholdLowWarningThreshold}
)
