# SNMP MIB module (ALCATEL-IND1-FIPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-FIPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:03 2024
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

(softentIND1Fips,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Fips")

(MultiChassisId,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-MULTI-CHASSIS-MIB",
    "MultiChassisId")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

alcatelIND1FipsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FipsFCMAP(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class Fcid(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class Wwpn(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class Wwnn(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1FipsMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1FipsMIBNotifications = _AlcatelIND1FipsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1FipsMIBNotifications.setStatus("current")
_AlcatelIND1FipsMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1FipsMIBObjects = _AlcatelIND1FipsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1FipsMIBObjects.setStatus("current")
_AlaFipsInfo_ObjectIdentity = ObjectIdentity
alaFipsInfo = _AlaFipsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 1)
)


class _AlaFipsConfigFilterResourceLimit_Type(Integer32):
    """Custom type alaFipsConfigFilterResourceLimit based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlaFipsConfigFilterResourceLimit_Type.__name__ = "Integer32"
_AlaFipsConfigFilterResourceLimit_Object = MibScalar
alaFipsConfigFilterResourceLimit = _AlaFipsConfigFilterResourceLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 1, 1),
    _AlaFipsConfigFilterResourceLimit_Type()
)
alaFipsConfigFilterResourceLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaFipsConfigFilterResourceLimit.setStatus("current")


class _AlaFipsConfigFIPSAdmin_Type(Integer32):
    """Custom type alaFipsConfigFIPSAdmin based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaFipsConfigFIPSAdmin_Type.__name__ = "Integer32"
_AlaFipsConfigFIPSAdmin_Object = MibScalar
alaFipsConfigFIPSAdmin = _AlaFipsConfigFIPSAdmin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 1, 2),
    _AlaFipsConfigFIPSAdmin_Type()
)
alaFipsConfigFIPSAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaFipsConfigFIPSAdmin.setStatus("current")


class _AlaFipsConfigAddressMode_Type(Integer32):
    """Custom type alaFipsConfigAddressMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fpma", 1),
          ("spma", 2))
    )


_AlaFipsConfigAddressMode_Type.__name__ = "Integer32"
_AlaFipsConfigAddressMode_Object = MibScalar
alaFipsConfigAddressMode = _AlaFipsConfigAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 1, 3),
    _AlaFipsConfigAddressMode_Type()
)
alaFipsConfigAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaFipsConfigAddressMode.setStatus("current")


class _AlaFipsConfigPriorityOne_Type(Integer32):
    """Custom type alaFipsConfigPriorityOne based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaFipsConfigPriorityOne_Type.__name__ = "Integer32"
_AlaFipsConfigPriorityOne_Object = MibScalar
alaFipsConfigPriorityOne = _AlaFipsConfigPriorityOne_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 1, 4),
    _AlaFipsConfigPriorityOne_Type()
)
alaFipsConfigPriorityOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaFipsConfigPriorityOne.setStatus("current")


class _AlaFipsConfigPriorityTwo_Type(Integer32):
    """Custom type alaFipsConfigPriorityTwo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AlaFipsConfigPriorityTwo_Type.__name__ = "Integer32"
_AlaFipsConfigPriorityTwo_Object = MibScalar
alaFipsConfigPriorityTwo = _AlaFipsConfigPriorityTwo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 1, 5),
    _AlaFipsConfigPriorityTwo_Type()
)
alaFipsConfigPriorityTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaFipsConfigPriorityTwo.setStatus("current")


class _AlaFipsTotalNumFilterResource_Type(Unsigned32):
    """Custom type alaFipsTotalNumFilterResource based on Unsigned32"""
    defaultValue = 256


_AlaFipsTotalNumFilterResource_Object = MibScalar
alaFipsTotalNumFilterResource = _AlaFipsTotalNumFilterResource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 1, 6),
    _AlaFipsTotalNumFilterResource_Type()
)
alaFipsTotalNumFilterResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsTotalNumFilterResource.setStatus("current")


class _AlaFipsUsedNumFilterResource_Type(Unsigned32):
    """Custom type alaFipsUsedNumFilterResource based on Unsigned32"""
    defaultValue = 0


_AlaFipsUsedNumFilterResource_Object = MibScalar
alaFipsUsedNumFilterResource = _AlaFipsUsedNumFilterResource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 1, 7),
    _AlaFipsUsedNumFilterResource_Type()
)
alaFipsUsedNumFilterResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsUsedNumFilterResource.setStatus("current")
_AlaFipsConfigStatsClear_Type = Unsigned32
_AlaFipsConfigStatsClear_Object = MibScalar
alaFipsConfigStatsClear = _AlaFipsConfigStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 1, 8),
    _AlaFipsConfigStatsClear_Type()
)
alaFipsConfigStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaFipsConfigStatsClear.setStatus("current")


class _AlaFipsConfigPrioProtection_Type(Integer32):
    """Custom type alaFipsConfigPrioProtection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaFipsConfigPrioProtection_Type.__name__ = "Integer32"
_AlaFipsConfigPrioProtection_Object = MibScalar
alaFipsConfigPrioProtection = _AlaFipsConfigPrioProtection_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 1, 9),
    _AlaFipsConfigPrioProtection_Type()
)
alaFipsConfigPrioProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaFipsConfigPrioProtection.setStatus("current")


class _AlaFipsConfigPriorityProtectionAction_Type(Integer32):
    """Custom type alaFipsConfigPriorityProtectionAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("remark", 2))
    )


_AlaFipsConfigPriorityProtectionAction_Type.__name__ = "Integer32"
_AlaFipsConfigPriorityProtectionAction_Object = MibScalar
alaFipsConfigPriorityProtectionAction = _AlaFipsConfigPriorityProtectionAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 1, 10),
    _AlaFipsConfigPriorityProtectionAction_Type()
)
alaFipsConfigPriorityProtectionAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaFipsConfigPriorityProtectionAction.setStatus("current")


class _AlaFipsConfigPriorityProtectionRemarkVal_Type(Integer32):
    """Custom type alaFipsConfigPriorityProtectionRemarkVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AlaFipsConfigPriorityProtectionRemarkVal_Type.__name__ = "Integer32"
_AlaFipsConfigPriorityProtectionRemarkVal_Object = MibScalar
alaFipsConfigPriorityProtectionRemarkVal = _AlaFipsConfigPriorityProtectionRemarkVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 1, 11),
    _AlaFipsConfigPriorityProtectionRemarkVal_Type()
)
alaFipsConfigPriorityProtectionRemarkVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaFipsConfigPriorityProtectionRemarkVal.setStatus("current")


class _AlaFipsConfigHouseKeepingTimePeriod_Type(Unsigned32):
    """Custom type alaFipsConfigHouseKeepingTimePeriod based on Unsigned32"""
    defaultValue = 300


_AlaFipsConfigHouseKeepingTimePeriod_Object = MibScalar
alaFipsConfigHouseKeepingTimePeriod = _AlaFipsConfigHouseKeepingTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 1, 12),
    _AlaFipsConfigHouseKeepingTimePeriod_Type()
)
alaFipsConfigHouseKeepingTimePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaFipsConfigHouseKeepingTimePeriod.setStatus("current")


class _AlaFipsConfigSWReinsertStatus_Type(Integer32):
    """Custom type alaFipsConfigSWReinsertStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaFipsConfigSWReinsertStatus_Type.__name__ = "Integer32"
_AlaFipsConfigSWReinsertStatus_Object = MibScalar
alaFipsConfigSWReinsertStatus = _AlaFipsConfigSWReinsertStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 1, 13),
    _AlaFipsConfigSWReinsertStatus_Type()
)
alaFipsConfigSWReinsertStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaFipsConfigSWReinsertStatus.setStatus("current")


class _AlaFipsConfigSessClear_Type(Integer32):
    """Custom type alaFipsConfigSessClear based on Integer32"""
    defaultValue = 7

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
        *(("all", 1),
          ("eTunnel", 4),
          ("fips", 5),
          ("none", 7),
          ("npiv", 2),
          ("npivPending", 6),
          ("reverseNpiv", 3))
    )


_AlaFipsConfigSessClear_Type.__name__ = "Integer32"
_AlaFipsConfigSessClear_Object = MibScalar
alaFipsConfigSessClear = _AlaFipsConfigSessClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 1, 14),
    _AlaFipsConfigSessClear_Type()
)
alaFipsConfigSessClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaFipsConfigSessClear.setStatus("current")
_AlaFipsVlan_ObjectIdentity = ObjectIdentity
alaFipsVlan = _AlaFipsVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 2)
)
_AlaFipsVlanTable_Object = MibTable
alaFipsVlanTable = _AlaFipsVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaFipsVlanTable.setStatus("current")
_AlaFipsVlanEntry_Object = MibTableRow
alaFipsVlanEntry = _AlaFipsVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 2, 1, 1)
)
alaFipsVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsVlanId"),
)
if mibBuilder.loadTexts:
    alaFipsVlanEntry.setStatus("current")


class _AlaFipsVlanId_Type(Integer32):
    """Custom type alaFipsVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaFipsVlanId_Type.__name__ = "Integer32"
_AlaFipsVlanId_Object = MibTableColumn
alaFipsVlanId = _AlaFipsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 2, 1, 1, 1),
    _AlaFipsVlanId_Type()
)
alaFipsVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsVlanId.setStatus("current")


class _AlaFipsVlanFCMap_Type(FipsFCMAP):
    """Custom type alaFipsVlanFCMap based on FipsFCMAP"""
    defaultHexValue = "000000"


_AlaFipsVlanFCMap_Object = MibTableColumn
alaFipsVlanFCMap = _AlaFipsVlanFCMap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 2, 1, 1, 2),
    _AlaFipsVlanFCMap_Type()
)
alaFipsVlanFCMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFipsVlanFCMap.setStatus("current")
_AlaFipsVlanStatsClear_Type = Unsigned32
_AlaFipsVlanStatsClear_Object = MibTableColumn
alaFipsVlanStatsClear = _AlaFipsVlanStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 2, 1, 1, 3),
    _AlaFipsVlanStatsClear_Type()
)
alaFipsVlanStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFipsVlanStatsClear.setStatus("current")


class _AlaFipsVlanStatsFnreClear_Type(Integer32):
    """Custom type alaFipsVlanStatsFnreClear based on Integer32"""
    defaultValue = 6

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
        *(("all", 1),
          ("eTunnel", 5),
          ("fips", 2),
          ("none", 6),
          ("npiv", 3),
          ("reverseNpiv", 4))
    )


_AlaFipsVlanStatsFnreClear_Type.__name__ = "Integer32"
_AlaFipsVlanStatsFnreClear_Object = MibTableColumn
alaFipsVlanStatsFnreClear = _AlaFipsVlanStatsFnreClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 2, 1, 1, 4),
    _AlaFipsVlanStatsFnreClear_Type()
)
alaFipsVlanStatsFnreClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFipsVlanStatsFnreClear.setStatus("current")
_AlaFipsVlanEnodeStats_ObjectIdentity = ObjectIdentity
alaFipsVlanEnodeStats = _AlaFipsVlanEnodeStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 3)
)
_AlaFipsVlanEnodeStatsTable_Object = MibTable
alaFipsVlanEnodeStatsTable = _AlaFipsVlanEnodeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alaFipsVlanEnodeStatsTable.setStatus("current")
_AlaFipsVlanEnodeStatsEntry_Object = MibTableRow
alaFipsVlanEnodeStatsEntry = _AlaFipsVlanEnodeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 3, 1, 1)
)
alaFipsVlanEnodeStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsVlanEnodeStatsVlanId"),
)
if mibBuilder.loadTexts:
    alaFipsVlanEnodeStatsEntry.setStatus("current")


class _AlaFipsVlanEnodeStatsVlanId_Type(Integer32):
    """Custom type alaFipsVlanEnodeStatsVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaFipsVlanEnodeStatsVlanId_Type.__name__ = "Integer32"
_AlaFipsVlanEnodeStatsVlanId_Object = MibTableColumn
alaFipsVlanEnodeStatsVlanId = _AlaFipsVlanEnodeStatsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 3, 1, 1, 1),
    _AlaFipsVlanEnodeStatsVlanId_Type()
)
alaFipsVlanEnodeStatsVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsVlanEnodeStatsVlanId.setStatus("current")


class _AlaFipsVlanEnodeStatsSessions_Type(Unsigned32):
    """Custom type alaFipsVlanEnodeStatsSessions based on Unsigned32"""
    defaultValue = 0


_AlaFipsVlanEnodeStatsSessions_Object = MibTableColumn
alaFipsVlanEnodeStatsSessions = _AlaFipsVlanEnodeStatsSessions_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 3, 1, 1, 2),
    _AlaFipsVlanEnodeStatsSessions_Type()
)
alaFipsVlanEnodeStatsSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanEnodeStatsSessions.setStatus("current")
_AlaFipsVlanEnodeStatsMds_Type = Counter32
_AlaFipsVlanEnodeStatsMds_Object = MibTableColumn
alaFipsVlanEnodeStatsMds = _AlaFipsVlanEnodeStatsMds_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 3, 1, 1, 3),
    _AlaFipsVlanEnodeStatsMds_Type()
)
alaFipsVlanEnodeStatsMds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanEnodeStatsMds.setStatus("current")
_AlaFipsVlanEnodeStatsUds_Type = Counter32
_AlaFipsVlanEnodeStatsUds_Object = MibTableColumn
alaFipsVlanEnodeStatsUds = _AlaFipsVlanEnodeStatsUds_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 3, 1, 1, 4),
    _AlaFipsVlanEnodeStatsUds_Type()
)
alaFipsVlanEnodeStatsUds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanEnodeStatsUds.setStatus("current")
_AlaFipsVlanEnodeStatsFlogi_Type = Counter32
_AlaFipsVlanEnodeStatsFlogi_Object = MibTableColumn
alaFipsVlanEnodeStatsFlogi = _AlaFipsVlanEnodeStatsFlogi_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 3, 1, 1, 5),
    _AlaFipsVlanEnodeStatsFlogi_Type()
)
alaFipsVlanEnodeStatsFlogi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanEnodeStatsFlogi.setStatus("current")
_AlaFipsVlanEnodeStatsFdisc_Type = Counter32
_AlaFipsVlanEnodeStatsFdisc_Object = MibTableColumn
alaFipsVlanEnodeStatsFdisc = _AlaFipsVlanEnodeStatsFdisc_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 3, 1, 1, 6),
    _AlaFipsVlanEnodeStatsFdisc_Type()
)
alaFipsVlanEnodeStatsFdisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanEnodeStatsFdisc.setStatus("current")
_AlaFipsVlanEnodeStatsLogo_Type = Counter32
_AlaFipsVlanEnodeStatsLogo_Object = MibTableColumn
alaFipsVlanEnodeStatsLogo = _AlaFipsVlanEnodeStatsLogo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 3, 1, 1, 7),
    _AlaFipsVlanEnodeStatsLogo_Type()
)
alaFipsVlanEnodeStatsLogo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanEnodeStatsLogo.setStatus("current")
_AlaFipsVlanEnodeStatsEka_Type = Counter32
_AlaFipsVlanEnodeStatsEka_Object = MibTableColumn
alaFipsVlanEnodeStatsEka = _AlaFipsVlanEnodeStatsEka_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 3, 1, 1, 8),
    _AlaFipsVlanEnodeStatsEka_Type()
)
alaFipsVlanEnodeStatsEka.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanEnodeStatsEka.setStatus("current")
_AlaFipsVlanEnodeStatsVnka_Type = Counter32
_AlaFipsVlanEnodeStatsVnka_Object = MibTableColumn
alaFipsVlanEnodeStatsVnka = _AlaFipsVlanEnodeStatsVnka_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 3, 1, 1, 9),
    _AlaFipsVlanEnodeStatsVnka_Type()
)
alaFipsVlanEnodeStatsVnka.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanEnodeStatsVnka.setStatus("current")
_AlaFipsVlanEnodeStatsClear_Type = Unsigned32
_AlaFipsVlanEnodeStatsClear_Object = MibTableColumn
alaFipsVlanEnodeStatsClear = _AlaFipsVlanEnodeStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 3, 1, 1, 10),
    _AlaFipsVlanEnodeStatsClear_Type()
)
alaFipsVlanEnodeStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaFipsVlanEnodeStatsClear.setStatus("current")
_AlaFipsVlanFcfStats_ObjectIdentity = ObjectIdentity
alaFipsVlanFcfStats = _AlaFipsVlanFcfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 4)
)
_AlaFipsVlanFcfStatsTable_Object = MibTable
alaFipsVlanFcfStatsTable = _AlaFipsVlanFcfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    alaFipsVlanFcfStatsTable.setStatus("current")
_AlaFipsVlanFcfStatsEntry_Object = MibTableRow
alaFipsVlanFcfStatsEntry = _AlaFipsVlanFcfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 4, 1, 1)
)
alaFipsVlanFcfStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsVlanFcfStatsVlanId"),
)
if mibBuilder.loadTexts:
    alaFipsVlanFcfStatsEntry.setStatus("current")


class _AlaFipsVlanFcfStatsVlanId_Type(Integer32):
    """Custom type alaFipsVlanFcfStatsVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaFipsVlanFcfStatsVlanId_Type.__name__ = "Integer32"
_AlaFipsVlanFcfStatsVlanId_Object = MibTableColumn
alaFipsVlanFcfStatsVlanId = _AlaFipsVlanFcfStatsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 4, 1, 1, 1),
    _AlaFipsVlanFcfStatsVlanId_Type()
)
alaFipsVlanFcfStatsVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsVlanFcfStatsVlanId.setStatus("current")


class _AlaFipsVlanFcfStatsSessions_Type(Unsigned32):
    """Custom type alaFipsVlanFcfStatsSessions based on Unsigned32"""
    defaultValue = 0


_AlaFipsVlanFcfStatsSessions_Object = MibTableColumn
alaFipsVlanFcfStatsSessions = _AlaFipsVlanFcfStatsSessions_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 4, 1, 1, 2),
    _AlaFipsVlanFcfStatsSessions_Type()
)
alaFipsVlanFcfStatsSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanFcfStatsSessions.setStatus("current")
_AlaFipsVlanFcfStatsMda_Type = Counter32
_AlaFipsVlanFcfStatsMda_Object = MibTableColumn
alaFipsVlanFcfStatsMda = _AlaFipsVlanFcfStatsMda_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 4, 1, 1, 3),
    _AlaFipsVlanFcfStatsMda_Type()
)
alaFipsVlanFcfStatsMda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanFcfStatsMda.setStatus("current")
_AlaFipsVlanFcfStatsUda_Type = Counter32
_AlaFipsVlanFcfStatsUda_Object = MibTableColumn
alaFipsVlanFcfStatsUda = _AlaFipsVlanFcfStatsUda_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 4, 1, 1, 4),
    _AlaFipsVlanFcfStatsUda_Type()
)
alaFipsVlanFcfStatsUda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanFcfStatsUda.setStatus("current")
_AlaFipsVlanFcfStatsFlogiAcc_Type = Counter32
_AlaFipsVlanFcfStatsFlogiAcc_Object = MibTableColumn
alaFipsVlanFcfStatsFlogiAcc = _AlaFipsVlanFcfStatsFlogiAcc_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 4, 1, 1, 5),
    _AlaFipsVlanFcfStatsFlogiAcc_Type()
)
alaFipsVlanFcfStatsFlogiAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanFcfStatsFlogiAcc.setStatus("current")
_AlaFipsVlanFcfStatsFlogiRjt_Type = Counter32
_AlaFipsVlanFcfStatsFlogiRjt_Object = MibTableColumn
alaFipsVlanFcfStatsFlogiRjt = _AlaFipsVlanFcfStatsFlogiRjt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 4, 1, 1, 6),
    _AlaFipsVlanFcfStatsFlogiRjt_Type()
)
alaFipsVlanFcfStatsFlogiRjt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanFcfStatsFlogiRjt.setStatus("current")
_AlaFipsVlanFcfStatsFdiscRjt_Type = Counter32
_AlaFipsVlanFcfStatsFdiscRjt_Object = MibTableColumn
alaFipsVlanFcfStatsFdiscRjt = _AlaFipsVlanFcfStatsFdiscRjt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 4, 1, 1, 7),
    _AlaFipsVlanFcfStatsFdiscRjt_Type()
)
alaFipsVlanFcfStatsFdiscRjt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanFcfStatsFdiscRjt.setStatus("current")
_AlaFipsVlanFcfStatsLogoAcc_Type = Counter32
_AlaFipsVlanFcfStatsLogoAcc_Object = MibTableColumn
alaFipsVlanFcfStatsLogoAcc = _AlaFipsVlanFcfStatsLogoAcc_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 4, 1, 1, 8),
    _AlaFipsVlanFcfStatsLogoAcc_Type()
)
alaFipsVlanFcfStatsLogoAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanFcfStatsLogoAcc.setStatus("current")
_AlaFipsVlanFcfStatsLogoRjt_Type = Counter32
_AlaFipsVlanFcfStatsLogoRjt_Object = MibTableColumn
alaFipsVlanFcfStatsLogoRjt = _AlaFipsVlanFcfStatsLogoRjt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 4, 1, 1, 9),
    _AlaFipsVlanFcfStatsLogoRjt_Type()
)
alaFipsVlanFcfStatsLogoRjt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanFcfStatsLogoRjt.setStatus("current")
_AlaFipsVlanFcfStatsCvl_Type = Counter32
_AlaFipsVlanFcfStatsCvl_Object = MibTableColumn
alaFipsVlanFcfStatsCvl = _AlaFipsVlanFcfStatsCvl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 4, 1, 1, 10),
    _AlaFipsVlanFcfStatsCvl_Type()
)
alaFipsVlanFcfStatsCvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanFcfStatsCvl.setStatus("current")
_AlaFipsVlanFcfStatsClear_Type = Unsigned32
_AlaFipsVlanFcfStatsClear_Object = MibTableColumn
alaFipsVlanFcfStatsClear = _AlaFipsVlanFcfStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 4, 1, 1, 11),
    _AlaFipsVlanFcfStatsClear_Type()
)
alaFipsVlanFcfStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaFipsVlanFcfStatsClear.setStatus("current")
_AlaFipsVlanFcfStatsFdiscAcc_Type = Counter32
_AlaFipsVlanFcfStatsFdiscAcc_Object = MibTableColumn
alaFipsVlanFcfStatsFdiscAcc = _AlaFipsVlanFcfStatsFdiscAcc_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 4, 1, 1, 12),
    _AlaFipsVlanFcfStatsFdiscAcc_Type()
)
alaFipsVlanFcfStatsFdiscAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanFcfStatsFdiscAcc.setStatus("current")
_AlaFipsIntf_ObjectIdentity = ObjectIdentity
alaFipsIntf = _AlaFipsIntf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 5)
)
_AlaFipsIntfTable_Object = MibTable
alaFipsIntfTable = _AlaFipsIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    alaFipsIntfTable.setStatus("current")
_AlaFipsIntfEntry_Object = MibTableRow
alaFipsIntfEntry = _AlaFipsIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 5, 1, 1)
)
alaFipsIntfEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsIntfIfIndex"),
)
if mibBuilder.loadTexts:
    alaFipsIntfEntry.setStatus("current")
_AlaFipsIntfIfIndex_Type = InterfaceIndexOrZero
_AlaFipsIntfIfIndex_Object = MibTableColumn
alaFipsIntfIfIndex = _AlaFipsIntfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 5, 1, 1, 1),
    _AlaFipsIntfIfIndex_Type()
)
alaFipsIntfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsIntfIfIndex.setStatus("current")


class _AlaFipsIntfOperStatus_Type(Integer32):
    """Custom type alaFipsIntfOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaFipsIntfOperStatus_Type.__name__ = "Integer32"
_AlaFipsIntfOperStatus_Object = MibTableColumn
alaFipsIntfOperStatus = _AlaFipsIntfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 5, 1, 1, 2),
    _AlaFipsIntfOperStatus_Type()
)
alaFipsIntfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfOperStatus.setStatus("current")


class _AlaFipsIntfPortRole_Type(Integer32):
    """Custom type alaFipsIntfPortRole based on Integer32"""
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
        *(("edge", 1),
          ("enode", 2),
          ("fcf", 3),
          ("mixed", 4),
          ("trusted", 5),
          ("ve", 6))
    )


_AlaFipsIntfPortRole_Type.__name__ = "Integer32"
_AlaFipsIntfPortRole_Object = MibTableColumn
alaFipsIntfPortRole = _AlaFipsIntfPortRole_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 5, 1, 1, 3),
    _AlaFipsIntfPortRole_Type()
)
alaFipsIntfPortRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFipsIntfPortRole.setStatus("current")


class _AlaFipsIntfRowStatus_Type(RowStatus):
    """Custom type alaFipsIntfRowStatus based on RowStatus"""


_AlaFipsIntfRowStatus_Object = MibTableColumn
alaFipsIntfRowStatus = _AlaFipsIntfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 5, 1, 1, 4),
    _AlaFipsIntfRowStatus_Type()
)
alaFipsIntfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFipsIntfRowStatus.setStatus("current")
_AlaFipsIntfStatsClear_Type = Unsigned32
_AlaFipsIntfStatsClear_Object = MibTableColumn
alaFipsIntfStatsClear = _AlaFipsIntfStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 5, 1, 1, 5),
    _AlaFipsIntfStatsClear_Type()
)
alaFipsIntfStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFipsIntfStatsClear.setStatus("current")


class _AlaFipsIntfStatsFnreClear_Type(Integer32):
    """Custom type alaFipsIntfStatsFnreClear based on Integer32"""
    defaultValue = 6

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
        *(("all", 1),
          ("eTunnel", 5),
          ("fips", 2),
          ("none", 6),
          ("npiv", 3),
          ("reverseNpiv", 4))
    )


_AlaFipsIntfStatsFnreClear_Type.__name__ = "Integer32"
_AlaFipsIntfStatsFnreClear_Object = MibTableColumn
alaFipsIntfStatsFnreClear = _AlaFipsIntfStatsFnreClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 5, 1, 1, 6),
    _AlaFipsIntfStatsFnreClear_Type()
)
alaFipsIntfStatsFnreClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFipsIntfStatsFnreClear.setStatus("current")
_AlaFipsIntfEnodeStats_ObjectIdentity = ObjectIdentity
alaFipsIntfEnodeStats = _AlaFipsIntfEnodeStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 6)
)
_AlaFipsIntfEnodeStatsTable_Object = MibTable
alaFipsIntfEnodeStatsTable = _AlaFipsIntfEnodeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    alaFipsIntfEnodeStatsTable.setStatus("current")
_AlaFipsIntfEnodeStatsEntry_Object = MibTableRow
alaFipsIntfEnodeStatsEntry = _AlaFipsIntfEnodeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 6, 1, 1)
)
alaFipsIntfEnodeStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsIntfEnodeStatsIfIndex"),
)
if mibBuilder.loadTexts:
    alaFipsIntfEnodeStatsEntry.setStatus("current")
_AlaFipsIntfEnodeStatsIfIndex_Type = InterfaceIndexOrZero
_AlaFipsIntfEnodeStatsIfIndex_Object = MibTableColumn
alaFipsIntfEnodeStatsIfIndex = _AlaFipsIntfEnodeStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 6, 1, 1, 1),
    _AlaFipsIntfEnodeStatsIfIndex_Type()
)
alaFipsIntfEnodeStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsIntfEnodeStatsIfIndex.setStatus("current")


class _AlaFipsIntfEnodeStatsSessions_Type(Unsigned32):
    """Custom type alaFipsIntfEnodeStatsSessions based on Unsigned32"""
    defaultValue = 0


_AlaFipsIntfEnodeStatsSessions_Object = MibTableColumn
alaFipsIntfEnodeStatsSessions = _AlaFipsIntfEnodeStatsSessions_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 6, 1, 1, 2),
    _AlaFipsIntfEnodeStatsSessions_Type()
)
alaFipsIntfEnodeStatsSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfEnodeStatsSessions.setStatus("current")
_AlaFipsIntfEnodeStatsMds_Type = Counter32
_AlaFipsIntfEnodeStatsMds_Object = MibTableColumn
alaFipsIntfEnodeStatsMds = _AlaFipsIntfEnodeStatsMds_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 6, 1, 1, 3),
    _AlaFipsIntfEnodeStatsMds_Type()
)
alaFipsIntfEnodeStatsMds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfEnodeStatsMds.setStatus("current")
_AlaFipsIntfEnodeStatsUds_Type = Counter32
_AlaFipsIntfEnodeStatsUds_Object = MibTableColumn
alaFipsIntfEnodeStatsUds = _AlaFipsIntfEnodeStatsUds_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 6, 1, 1, 4),
    _AlaFipsIntfEnodeStatsUds_Type()
)
alaFipsIntfEnodeStatsUds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfEnodeStatsUds.setStatus("current")
_AlaFipsIntfEnodeStatsFlogi_Type = Counter32
_AlaFipsIntfEnodeStatsFlogi_Object = MibTableColumn
alaFipsIntfEnodeStatsFlogi = _AlaFipsIntfEnodeStatsFlogi_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 6, 1, 1, 5),
    _AlaFipsIntfEnodeStatsFlogi_Type()
)
alaFipsIntfEnodeStatsFlogi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfEnodeStatsFlogi.setStatus("current")
_AlaFipsIntfEnodeStatsFdisc_Type = Counter32
_AlaFipsIntfEnodeStatsFdisc_Object = MibTableColumn
alaFipsIntfEnodeStatsFdisc = _AlaFipsIntfEnodeStatsFdisc_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 6, 1, 1, 6),
    _AlaFipsIntfEnodeStatsFdisc_Type()
)
alaFipsIntfEnodeStatsFdisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfEnodeStatsFdisc.setStatus("current")
_AlaFipsIntfEnodeStatsLogo_Type = Counter32
_AlaFipsIntfEnodeStatsLogo_Object = MibTableColumn
alaFipsIntfEnodeStatsLogo = _AlaFipsIntfEnodeStatsLogo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 6, 1, 1, 7),
    _AlaFipsIntfEnodeStatsLogo_Type()
)
alaFipsIntfEnodeStatsLogo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfEnodeStatsLogo.setStatus("current")
_AlaFipsIntfEnodeStatsEka_Type = Counter32
_AlaFipsIntfEnodeStatsEka_Object = MibTableColumn
alaFipsIntfEnodeStatsEka = _AlaFipsIntfEnodeStatsEka_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 6, 1, 1, 8),
    _AlaFipsIntfEnodeStatsEka_Type()
)
alaFipsIntfEnodeStatsEka.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfEnodeStatsEka.setStatus("current")
_AlaFipsIntfEnodeStatsVnka_Type = Counter32
_AlaFipsIntfEnodeStatsVnka_Object = MibTableColumn
alaFipsIntfEnodeStatsVnka = _AlaFipsIntfEnodeStatsVnka_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 6, 1, 1, 9),
    _AlaFipsIntfEnodeStatsVnka_Type()
)
alaFipsIntfEnodeStatsVnka.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfEnodeStatsVnka.setStatus("current")
_AlaFipsIntfEnodeStatsClear_Type = Unsigned32
_AlaFipsIntfEnodeStatsClear_Object = MibTableColumn
alaFipsIntfEnodeStatsClear = _AlaFipsIntfEnodeStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 6, 1, 1, 10),
    _AlaFipsIntfEnodeStatsClear_Type()
)
alaFipsIntfEnodeStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaFipsIntfEnodeStatsClear.setStatus("current")
_AlaFipsIntfFcfStats_ObjectIdentity = ObjectIdentity
alaFipsIntfFcfStats = _AlaFipsIntfFcfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 7)
)
_AlaFipsIntfFcfStatsTable_Object = MibTable
alaFipsIntfFcfStatsTable = _AlaFipsIntfFcfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    alaFipsIntfFcfStatsTable.setStatus("current")
_AlaFipsIntfFcfStatsEntry_Object = MibTableRow
alaFipsIntfFcfStatsEntry = _AlaFipsIntfFcfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 7, 1, 1)
)
alaFipsIntfFcfStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsIntfFcfStatsIfIndex"),
)
if mibBuilder.loadTexts:
    alaFipsIntfFcfStatsEntry.setStatus("current")
_AlaFipsIntfFcfStatsIfIndex_Type = InterfaceIndexOrZero
_AlaFipsIntfFcfStatsIfIndex_Object = MibTableColumn
alaFipsIntfFcfStatsIfIndex = _AlaFipsIntfFcfStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 7, 1, 1, 1),
    _AlaFipsIntfFcfStatsIfIndex_Type()
)
alaFipsIntfFcfStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsIntfFcfStatsIfIndex.setStatus("current")


class _AlaFipsIntfFcfStatsSessions_Type(Unsigned32):
    """Custom type alaFipsIntfFcfStatsSessions based on Unsigned32"""
    defaultValue = 0


_AlaFipsIntfFcfStatsSessions_Object = MibTableColumn
alaFipsIntfFcfStatsSessions = _AlaFipsIntfFcfStatsSessions_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 7, 1, 1, 2),
    _AlaFipsIntfFcfStatsSessions_Type()
)
alaFipsIntfFcfStatsSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfFcfStatsSessions.setStatus("current")
_AlaFipsIntfFcfStatsMda_Type = Counter32
_AlaFipsIntfFcfStatsMda_Object = MibTableColumn
alaFipsIntfFcfStatsMda = _AlaFipsIntfFcfStatsMda_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 7, 1, 1, 3),
    _AlaFipsIntfFcfStatsMda_Type()
)
alaFipsIntfFcfStatsMda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfFcfStatsMda.setStatus("current")
_AlaFipsIntfFcfStatsUda_Type = Counter32
_AlaFipsIntfFcfStatsUda_Object = MibTableColumn
alaFipsIntfFcfStatsUda = _AlaFipsIntfFcfStatsUda_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 7, 1, 1, 4),
    _AlaFipsIntfFcfStatsUda_Type()
)
alaFipsIntfFcfStatsUda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfFcfStatsUda.setStatus("current")
_AlaFipsIntfFcfStatsFlogiAcc_Type = Counter32
_AlaFipsIntfFcfStatsFlogiAcc_Object = MibTableColumn
alaFipsIntfFcfStatsFlogiAcc = _AlaFipsIntfFcfStatsFlogiAcc_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 7, 1, 1, 5),
    _AlaFipsIntfFcfStatsFlogiAcc_Type()
)
alaFipsIntfFcfStatsFlogiAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfFcfStatsFlogiAcc.setStatus("current")
_AlaFipsIntfFcfStatsFdiscRjt_Type = Counter32
_AlaFipsIntfFcfStatsFdiscRjt_Object = MibTableColumn
alaFipsIntfFcfStatsFdiscRjt = _AlaFipsIntfFcfStatsFdiscRjt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 7, 1, 1, 6),
    _AlaFipsIntfFcfStatsFdiscRjt_Type()
)
alaFipsIntfFcfStatsFdiscRjt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfFcfStatsFdiscRjt.setStatus("current")
_AlaFipsIntfFcfStatsFlogiRjt_Type = Counter32
_AlaFipsIntfFcfStatsFlogiRjt_Object = MibTableColumn
alaFipsIntfFcfStatsFlogiRjt = _AlaFipsIntfFcfStatsFlogiRjt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 7, 1, 1, 7),
    _AlaFipsIntfFcfStatsFlogiRjt_Type()
)
alaFipsIntfFcfStatsFlogiRjt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfFcfStatsFlogiRjt.setStatus("current")
_AlaFipsIntfFcfStatsLogoAcc_Type = Counter32
_AlaFipsIntfFcfStatsLogoAcc_Object = MibTableColumn
alaFipsIntfFcfStatsLogoAcc = _AlaFipsIntfFcfStatsLogoAcc_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 7, 1, 1, 8),
    _AlaFipsIntfFcfStatsLogoAcc_Type()
)
alaFipsIntfFcfStatsLogoAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfFcfStatsLogoAcc.setStatus("current")
_AlaFipsIntfFcfStatsLogoRjt_Type = Counter32
_AlaFipsIntfFcfStatsLogoRjt_Object = MibTableColumn
alaFipsIntfFcfStatsLogoRjt = _AlaFipsIntfFcfStatsLogoRjt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 7, 1, 1, 9),
    _AlaFipsIntfFcfStatsLogoRjt_Type()
)
alaFipsIntfFcfStatsLogoRjt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfFcfStatsLogoRjt.setStatus("current")
_AlaFipsIntfFcfStatsCvl_Type = Counter32
_AlaFipsIntfFcfStatsCvl_Object = MibTableColumn
alaFipsIntfFcfStatsCvl = _AlaFipsIntfFcfStatsCvl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 7, 1, 1, 10),
    _AlaFipsIntfFcfStatsCvl_Type()
)
alaFipsIntfFcfStatsCvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfFcfStatsCvl.setStatus("current")
_AlaFipsIntfFcfStatsClear_Type = Unsigned32
_AlaFipsIntfFcfStatsClear_Object = MibTableColumn
alaFipsIntfFcfStatsClear = _AlaFipsIntfFcfStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 7, 1, 1, 11),
    _AlaFipsIntfFcfStatsClear_Type()
)
alaFipsIntfFcfStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaFipsIntfFcfStatsClear.setStatus("current")
_AlaFipsIntfFcfStatsFdiscAcc_Type = Counter32
_AlaFipsIntfFcfStatsFdiscAcc_Object = MibTableColumn
alaFipsIntfFcfStatsFdiscAcc = _AlaFipsIntfFcfStatsFdiscAcc_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 7, 1, 1, 12),
    _AlaFipsIntfFcfStatsFdiscAcc_Type()
)
alaFipsIntfFcfStatsFdiscAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfFcfStatsFdiscAcc.setStatus("current")
_AlaFipsFcf_ObjectIdentity = ObjectIdentity
alaFipsFcf = _AlaFipsFcf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 8)
)
_AlaFipsFcfTable_Object = MibTable
alaFipsFcfTable = _AlaFipsFcfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    alaFipsFcfTable.setStatus("current")
_AlaFipsFcfEntry_Object = MibTableRow
alaFipsFcfEntry = _AlaFipsFcfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 8, 1, 1)
)
alaFipsFcfEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsFcfMAC"),
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsFcfVlan"),
)
if mibBuilder.loadTexts:
    alaFipsFcfEntry.setStatus("current")
_AlaFipsFcfMAC_Type = MacAddress
_AlaFipsFcfMAC_Object = MibTableColumn
alaFipsFcfMAC = _AlaFipsFcfMAC_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 8, 1, 1, 1),
    _AlaFipsFcfMAC_Type()
)
alaFipsFcfMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsFcfMAC.setStatus("current")


class _AlaFipsFcfVlan_Type(Integer32):
    """Custom type alaFipsFcfVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaFipsFcfVlan_Type.__name__ = "Integer32"
_AlaFipsFcfVlan_Object = MibTableColumn
alaFipsFcfVlan = _AlaFipsFcfVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 8, 1, 1, 2),
    _AlaFipsFcfVlan_Type()
)
alaFipsFcfVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsFcfVlan.setStatus("current")
_AlaFipsFcfIntf_Type = InterfaceIndex
_AlaFipsFcfIntf_Object = MibTableColumn
alaFipsFcfIntf = _AlaFipsFcfIntf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 8, 1, 1, 3),
    _AlaFipsFcfIntf_Type()
)
alaFipsFcfIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsFcfIntf.setStatus("current")
_AlaFipsFcfSessions_Type = Unsigned32
_AlaFipsFcfSessions_Object = MibTableColumn
alaFipsFcfSessions = _AlaFipsFcfSessions_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 8, 1, 1, 4),
    _AlaFipsFcfSessions_Type()
)
alaFipsFcfSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsFcfSessions.setStatus("current")


class _AlaFipsFcfConfigType_Type(Integer32):
    """Custom type alaFipsFcfConfigType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fpma", 1),
          ("spma", 2))
    )


_AlaFipsFcfConfigType_Type.__name__ = "Integer32"
_AlaFipsFcfConfigType_Object = MibTableColumn
alaFipsFcfConfigType = _AlaFipsFcfConfigType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 8, 1, 1, 5),
    _AlaFipsFcfConfigType_Type()
)
alaFipsFcfConfigType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFipsFcfConfigType.setStatus("current")


class _AlaFipsFcfRowStatus_Type(RowStatus):
    """Custom type alaFipsFcfRowStatus based on RowStatus"""


_AlaFipsFcfRowStatus_Object = MibTableColumn
alaFipsFcfRowStatus = _AlaFipsFcfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 8, 1, 1, 6),
    _AlaFipsFcfRowStatus_Type()
)
alaFipsFcfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFipsFcfRowStatus.setStatus("current")


class _AlaFipsFcfAvailForLogin_Type(Integer32):
    """Custom type alaFipsFcfAvailForLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaFipsFcfAvailForLogin_Type.__name__ = "Integer32"
_AlaFipsFcfAvailForLogin_Object = MibTableColumn
alaFipsFcfAvailForLogin = _AlaFipsFcfAvailForLogin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 8, 1, 1, 7),
    _AlaFipsFcfAvailForLogin_Type()
)
alaFipsFcfAvailForLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsFcfAvailForLogin.setStatus("current")


class _AlaFipsFcfMaxFcoeFrmSizeVerified_Type(Integer32):
    """Custom type alaFipsFcfMaxFcoeFrmSizeVerified based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaFipsFcfMaxFcoeFrmSizeVerified_Type.__name__ = "Integer32"
_AlaFipsFcfMaxFcoeFrmSizeVerified_Object = MibTableColumn
alaFipsFcfMaxFcoeFrmSizeVerified = _AlaFipsFcfMaxFcoeFrmSizeVerified_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 8, 1, 1, 8),
    _AlaFipsFcfMaxFcoeFrmSizeVerified_Type()
)
alaFipsFcfMaxFcoeFrmSizeVerified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsFcfMaxFcoeFrmSizeVerified.setStatus("current")


class _AlaFipsFcfPriority_Type(Unsigned32):
    """Custom type alaFipsFcfPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaFipsFcfPriority_Type.__name__ = "Unsigned32"
_AlaFipsFcfPriority_Object = MibTableColumn
alaFipsFcfPriority = _AlaFipsFcfPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 8, 1, 1, 9),
    _AlaFipsFcfPriority_Type()
)
alaFipsFcfPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsFcfPriority.setStatus("current")


class _AlaFipsFcfType_Type(Integer32):
    """Custom type alaFipsFcfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("npiv", 3),
          ("static", 2))
    )


_AlaFipsFcfType_Type.__name__ = "Integer32"
_AlaFipsFcfType_Object = MibTableColumn
alaFipsFcfType = _AlaFipsFcfType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 8, 1, 1, 10),
    _AlaFipsFcfType_Type()
)
alaFipsFcfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsFcfType.setStatus("current")
_AlaFipsSession_ObjectIdentity = ObjectIdentity
alaFipsSession = _AlaFipsSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 9)
)
_AlaFipsSessionTable_Object = MibTable
alaFipsSessionTable = _AlaFipsSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    alaFipsSessionTable.setStatus("current")
_AlaFipsSessionEntry_Object = MibTableRow
alaFipsSessionEntry = _AlaFipsSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 9, 1, 1)
)
alaFipsSessionEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsSessionEnodeMAC"),
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsSessionVNMAC"),
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsSessionVlanId"),
)
if mibBuilder.loadTexts:
    alaFipsSessionEntry.setStatus("current")
_AlaFipsSessionEnodeMAC_Type = MacAddress
_AlaFipsSessionEnodeMAC_Object = MibTableColumn
alaFipsSessionEnodeMAC = _AlaFipsSessionEnodeMAC_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 9, 1, 1, 1),
    _AlaFipsSessionEnodeMAC_Type()
)
alaFipsSessionEnodeMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsSessionEnodeMAC.setStatus("current")
_AlaFipsSessionVNMAC_Type = MacAddress
_AlaFipsSessionVNMAC_Object = MibTableColumn
alaFipsSessionVNMAC = _AlaFipsSessionVNMAC_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 9, 1, 1, 2),
    _AlaFipsSessionVNMAC_Type()
)
alaFipsSessionVNMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsSessionVNMAC.setStatus("current")


class _AlaFipsSessionVlanId_Type(Integer32):
    """Custom type alaFipsSessionVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaFipsSessionVlanId_Type.__name__ = "Integer32"
_AlaFipsSessionVlanId_Object = MibTableColumn
alaFipsSessionVlanId = _AlaFipsSessionVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 9, 1, 1, 3),
    _AlaFipsSessionVlanId_Type()
)
alaFipsSessionVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsSessionVlanId.setStatus("current")
_AlaFipsSessionIfIndex_Type = InterfaceIndex
_AlaFipsSessionIfIndex_Object = MibTableColumn
alaFipsSessionIfIndex = _AlaFipsSessionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 9, 1, 1, 4),
    _AlaFipsSessionIfIndex_Type()
)
alaFipsSessionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsSessionIfIndex.setStatus("current")


class _AlaFipsSessionFCFMAC_Type(MacAddress):
    """Custom type alaFipsSessionFCFMAC based on MacAddress"""
    defaultHexValue = "000000000000"


_AlaFipsSessionFCFMAC_Object = MibTableColumn
alaFipsSessionFCFMAC = _AlaFipsSessionFCFMAC_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 9, 1, 1, 5),
    _AlaFipsSessionFCFMAC_Type()
)
alaFipsSessionFCFMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFipsSessionFCFMAC.setStatus("current")


class _AlaFipsSessionStatus_Type(Integer32):
    """Custom type alaFipsSessionStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 2),
          ("pending", 1))
    )


_AlaFipsSessionStatus_Type.__name__ = "Integer32"
_AlaFipsSessionStatus_Object = MibTableColumn
alaFipsSessionStatus = _AlaFipsSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 9, 1, 1, 6),
    _AlaFipsSessionStatus_Type()
)
alaFipsSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsSessionStatus.setStatus("current")
_AlaFipsSessionLoginTime_Type = TimeStamp
_AlaFipsSessionLoginTime_Object = MibTableColumn
alaFipsSessionLoginTime = _AlaFipsSessionLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 9, 1, 1, 7),
    _AlaFipsSessionLoginTime_Type()
)
alaFipsSessionLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsSessionLoginTime.setStatus("current")
_AlaFipsSessionLoginTimeDate_Type = DateAndTime
_AlaFipsSessionLoginTimeDate_Object = MibTableColumn
alaFipsSessionLoginTimeDate = _AlaFipsSessionLoginTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 9, 1, 1, 8),
    _AlaFipsSessionLoginTimeDate_Type()
)
alaFipsSessionLoginTimeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsSessionLoginTimeDate.setStatus("current")
_AlaFipsNotificationObj_ObjectIdentity = ObjectIdentity
alaFipsNotificationObj = _AlaFipsNotificationObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 10)
)


class _AlaFipsFilterResourceUsage_Type(Integer32):
    """Custom type alaFipsFilterResourceUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlaFipsFilterResourceUsage_Type.__name__ = "Integer32"
_AlaFipsFilterResourceUsage_Object = MibScalar
alaFipsFilterResourceUsage = _AlaFipsFilterResourceUsage_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 10, 1),
    _AlaFipsFilterResourceUsage_Type()
)
alaFipsFilterResourceUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaFipsFilterResourceUsage.setStatus("current")
_AlaFcVsan_ObjectIdentity = ObjectIdentity
alaFcVsan = _AlaFcVsan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 11)
)
_AlaFcVsanTable_Object = MibTable
alaFcVsanTable = _AlaFcVsanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    alaFcVsanTable.setStatus("current")
_AlaFcVsanEntry_Object = MibTableRow
alaFcVsanEntry = _AlaFcVsanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 11, 1, 1)
)
alaFcVsanEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFcVsanNumber"),
)
if mibBuilder.loadTexts:
    alaFcVsanEntry.setStatus("current")


class _AlaFcVsanNumber_Type(Integer32):
    """Custom type alaFcVsanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaFcVsanNumber_Type.__name__ = "Integer32"
_AlaFcVsanNumber_Object = MibTableColumn
alaFcVsanNumber = _AlaFcVsanNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 11, 1, 1, 1),
    _AlaFcVsanNumber_Type()
)
alaFcVsanNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFcVsanNumber.setStatus("current")


class _AlaFcVsanDescription_Type(SnmpAdminString):
    """Custom type alaFcVsanDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaFcVsanDescription_Type.__name__ = "SnmpAdminString"
_AlaFcVsanDescription_Object = MibTableColumn
alaFcVsanDescription = _AlaFcVsanDescription_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 11, 1, 1, 2),
    _AlaFcVsanDescription_Type()
)
alaFcVsanDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFcVsanDescription.setStatus("current")


class _AlaFcVsanAdmStatus_Type(Integer32):
    """Custom type alaFcVsanAdmStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AlaFcVsanAdmStatus_Type.__name__ = "Integer32"
_AlaFcVsanAdmStatus_Object = MibTableColumn
alaFcVsanAdmStatus = _AlaFcVsanAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 11, 1, 1, 3),
    _AlaFcVsanAdmStatus_Type()
)
alaFcVsanAdmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFcVsanAdmStatus.setStatus("current")


class _AlaFcVsanOperStatus_Type(Integer32):
    """Custom type alaFcVsanOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AlaFcVsanOperStatus_Type.__name__ = "Integer32"
_AlaFcVsanOperStatus_Object = MibTableColumn
alaFcVsanOperStatus = _AlaFcVsanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 11, 1, 1, 4),
    _AlaFcVsanOperStatus_Type()
)
alaFcVsanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcVsanOperStatus.setStatus("current")
_AlaFcVsanRowStatus_Type = RowStatus
_AlaFcVsanRowStatus_Object = MibTableColumn
alaFcVsanRowStatus = _AlaFcVsanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 11, 1, 1, 5),
    _AlaFcVsanRowStatus_Type()
)
alaFcVsanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFcVsanRowStatus.setStatus("current")
_AlaFcVfpa_ObjectIdentity = ObjectIdentity
alaFcVfpa = _AlaFcVfpa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 12)
)
_AlaFcVfpaTable_Object = MibTable
alaFcVfpaTable = _AlaFcVfpaTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 12, 1)
)
if mibBuilder.loadTexts:
    alaFcVfpaTable.setStatus("current")
_AlaFcVfpaEntry_Object = MibTableRow
alaFcVfpaEntry = _AlaFcVfpaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 12, 1, 1)
)
alaFcVfpaEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFcVfpaVsanNumber"),
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFcVfpaIfIndex"),
)
if mibBuilder.loadTexts:
    alaFcVfpaEntry.setStatus("current")


class _AlaFcVfpaVsanNumber_Type(Integer32):
    """Custom type alaFcVfpaVsanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaFcVfpaVsanNumber_Type.__name__ = "Integer32"
_AlaFcVfpaVsanNumber_Object = MibTableColumn
alaFcVfpaVsanNumber = _AlaFcVfpaVsanNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 12, 1, 1, 1),
    _AlaFcVfpaVsanNumber_Type()
)
alaFcVfpaVsanNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFcVfpaVsanNumber.setStatus("current")


class _AlaFcVfpaIfIndex_Type(Unsigned32):
    """Custom type alaFcVfpaIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 4294967295),
    )


_AlaFcVfpaIfIndex_Type.__name__ = "Unsigned32"
_AlaFcVfpaIfIndex_Object = MibTableColumn
alaFcVfpaIfIndex = _AlaFcVfpaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 12, 1, 1, 2),
    _AlaFcVfpaIfIndex_Type()
)
alaFcVfpaIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFcVfpaIfIndex.setStatus("current")


class _AlaFcVfpaState_Type(Integer32):
    """Custom type alaFcVfpaState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0),
          ("inactive", 2))
    )


_AlaFcVfpaState_Type.__name__ = "Integer32"
_AlaFcVfpaState_Object = MibTableColumn
alaFcVfpaState = _AlaFcVfpaState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 12, 1, 1, 3),
    _AlaFcVfpaState_Type()
)
alaFcVfpaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcVfpaState.setStatus("current")
_AlaFcVfpaRowStatus_Type = RowStatus
_AlaFcVfpaRowStatus_Object = MibTableColumn
alaFcVfpaRowStatus = _AlaFcVfpaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 12, 1, 1, 4),
    _AlaFcVfpaRowStatus_Type()
)
alaFcVfpaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFcVfpaRowStatus.setStatus("current")
_AlaFcIntf_ObjectIdentity = ObjectIdentity
alaFcIntf = _AlaFcIntf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 13)
)
_AlaFcIntfTable_Object = MibTable
alaFcIntfTable = _AlaFcIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 13, 1)
)
if mibBuilder.loadTexts:
    alaFcIntfTable.setStatus("current")
_AlaFcIntfEntry_Object = MibTableRow
alaFcIntfEntry = _AlaFcIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 13, 1, 1)
)
alaFcIntfEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFcIntfIfIndex"),
)
if mibBuilder.loadTexts:
    alaFcIntfEntry.setStatus("current")
_AlaFcIntfIfIndex_Type = InterfaceIndexOrZero
_AlaFcIntfIfIndex_Object = MibTableColumn
alaFcIntfIfIndex = _AlaFcIntfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 13, 1, 1, 1),
    _AlaFcIntfIfIndex_Type()
)
alaFcIntfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFcIntfIfIndex.setStatus("current")


class _AlaFcIntfOperStatus_Type(Integer32):
    """Custom type alaFcIntfOperStatus based on Integer32"""
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


_AlaFcIntfOperStatus_Type.__name__ = "Integer32"
_AlaFcIntfOperStatus_Object = MibTableColumn
alaFcIntfOperStatus = _AlaFcIntfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 13, 1, 1, 2),
    _AlaFcIntfOperStatus_Type()
)
alaFcIntfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfOperStatus.setStatus("current")


class _AlaFcIntfMode_Type(Integer32):
    """Custom type alaFcIntfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("f", 2),
          ("np", 1),
          ("te", 3))
    )


_AlaFcIntfMode_Type.__name__ = "Integer32"
_AlaFcIntfMode_Object = MibTableColumn
alaFcIntfMode = _AlaFcIntfMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 13, 1, 1, 3),
    _AlaFcIntfMode_Type()
)
alaFcIntfMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFcIntfMode.setStatus("current")


class _AlaFcIntfBbScN_Type(Integer32):
    """Custom type alaFcIntfBbScN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaFcIntfBbScN_Type.__name__ = "Integer32"
_AlaFcIntfBbScN_Object = MibTableColumn
alaFcIntfBbScN = _AlaFcIntfBbScN_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 13, 1, 1, 4),
    _AlaFcIntfBbScN_Type()
)
alaFcIntfBbScN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFcIntfBbScN.setStatus("current")


class _AlaFcIntfClassOfService_Type(Integer32):
    """Custom type alaFcIntfClassOfService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("class2", 1),
          ("class3", 2),
          ("class3andF", 4),
          ("classF", 3))
    )


_AlaFcIntfClassOfService_Type.__name__ = "Integer32"
_AlaFcIntfClassOfService_Object = MibTableColumn
alaFcIntfClassOfService = _AlaFcIntfClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 13, 1, 1, 5),
    _AlaFcIntfClassOfService_Type()
)
alaFcIntfClassOfService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfClassOfService.setStatus("current")
_AlaFcIntfFcid_Type = Fcid
_AlaFcIntfFcid_Object = MibTableColumn
alaFcIntfFcid = _AlaFcIntfFcid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 13, 1, 1, 6),
    _AlaFcIntfFcid_Type()
)
alaFcIntfFcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfFcid.setStatus("current")
_AlaFcIntfWwpn_Type = Wwpn
_AlaFcIntfWwpn_Object = MibTableColumn
alaFcIntfWwpn = _AlaFcIntfWwpn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 13, 1, 1, 7),
    _AlaFcIntfWwpn_Type()
)
alaFcIntfWwpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfWwpn.setStatus("current")


class _AlaFcIntfLoginState_Type(Integer32):
    """Custom type alaFcIntfLoginState based on Integer32"""
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
        *(("down", 5),
          ("elpSent", 3),
          ("flogiSent", 2),
          ("sessionClearing", 4),
          ("up", 1))
    )


_AlaFcIntfLoginState_Type.__name__ = "Integer32"
_AlaFcIntfLoginState_Object = MibTableColumn
alaFcIntfLoginState = _AlaFcIntfLoginState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 13, 1, 1, 8),
    _AlaFcIntfLoginState_Type()
)
alaFcIntfLoginState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfLoginState.setStatus("current")


class _AlaFcIntfRowStatus_Type(RowStatus):
    """Custom type alaFcIntfRowStatus based on RowStatus"""


_AlaFcIntfRowStatus_Object = MibTableColumn
alaFcIntfRowStatus = _AlaFcIntfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 13, 1, 1, 9),
    _AlaFcIntfRowStatus_Type()
)
alaFcIntfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFcIntfRowStatus.setStatus("current")


class _AlaFcIntfStatsClear_Type(Integer32):
    """Custom type alaFcIntfStatsClear based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("none", 2))
    )


_AlaFcIntfStatsClear_Type.__name__ = "Integer32"
_AlaFcIntfStatsClear_Object = MibTableColumn
alaFcIntfStatsClear = _AlaFcIntfStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 13, 1, 1, 10),
    _AlaFcIntfStatsClear_Type()
)
alaFcIntfStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFcIntfStatsClear.setStatus("current")
_AlaFcNpivStaticLoadBalance_ObjectIdentity = ObjectIdentity
alaFcNpivStaticLoadBalance = _AlaFcNpivStaticLoadBalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 14)
)
_AlaFcNpivStaticLoadBalanceTable_Object = MibTable
alaFcNpivStaticLoadBalanceTable = _AlaFcNpivStaticLoadBalanceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 14, 1)
)
if mibBuilder.loadTexts:
    alaFcNpivStaticLoadBalanceTable.setStatus("current")
_AlaFcNpivStaticLoadBalanceEntry_Object = MibTableRow
alaFcNpivStaticLoadBalanceEntry = _AlaFcNpivStaticLoadBalanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 14, 1, 1)
)
alaFcNpivStaticLoadBalanceEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFcNpivStaticLoadBalanceFcIfIndex"),
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFcNpivStaticLoadBalanceEthIfIndex"),
)
if mibBuilder.loadTexts:
    alaFcNpivStaticLoadBalanceEntry.setStatus("current")
_AlaFcNpivStaticLoadBalanceFcIfIndex_Type = InterfaceIndexOrZero
_AlaFcNpivStaticLoadBalanceFcIfIndex_Object = MibTableColumn
alaFcNpivStaticLoadBalanceFcIfIndex = _AlaFcNpivStaticLoadBalanceFcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 14, 1, 1, 1),
    _AlaFcNpivStaticLoadBalanceFcIfIndex_Type()
)
alaFcNpivStaticLoadBalanceFcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFcNpivStaticLoadBalanceFcIfIndex.setStatus("current")
_AlaFcNpivStaticLoadBalanceEthIfIndex_Type = InterfaceIndexOrZero
_AlaFcNpivStaticLoadBalanceEthIfIndex_Object = MibTableColumn
alaFcNpivStaticLoadBalanceEthIfIndex = _AlaFcNpivStaticLoadBalanceEthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 14, 1, 1, 2),
    _AlaFcNpivStaticLoadBalanceEthIfIndex_Type()
)
alaFcNpivStaticLoadBalanceEthIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFcNpivStaticLoadBalanceEthIfIndex.setStatus("current")


class _AlaFcNpivStaticLoadBalanceRowStatus_Type(RowStatus):
    """Custom type alaFcNpivStaticLoadBalanceRowStatus based on RowStatus"""


_AlaFcNpivStaticLoadBalanceRowStatus_Object = MibTableColumn
alaFcNpivStaticLoadBalanceRowStatus = _AlaFcNpivStaticLoadBalanceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 14, 1, 1, 3),
    _AlaFcNpivStaticLoadBalanceRowStatus_Type()
)
alaFcNpivStaticLoadBalanceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFcNpivStaticLoadBalanceRowStatus.setStatus("current")
_AlaFcNode_ObjectIdentity = ObjectIdentity
alaFcNode = _AlaFcNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 15)
)
_AlaFcNodeTable_Object = MibTable
alaFcNodeTable = _AlaFcNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 15, 1)
)
if mibBuilder.loadTexts:
    alaFcNodeTable.setStatus("current")
_AlaFcNodeEntry_Object = MibTableRow
alaFcNodeEntry = _AlaFcNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 15, 1, 1)
)
alaFcNodeEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFcNodeIfIndex"),
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFcNodeWwpn"),
)
if mibBuilder.loadTexts:
    alaFcNodeEntry.setStatus("current")
_AlaFcNodeIfIndex_Type = InterfaceIndex
_AlaFcNodeIfIndex_Object = MibTableColumn
alaFcNodeIfIndex = _AlaFcNodeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 15, 1, 1, 1),
    _AlaFcNodeIfIndex_Type()
)
alaFcNodeIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFcNodeIfIndex.setStatus("current")
_AlaFcNodeWwpn_Type = Wwpn
_AlaFcNodeWwpn_Object = MibTableColumn
alaFcNodeWwpn = _AlaFcNodeWwpn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 15, 1, 1, 2),
    _AlaFcNodeWwpn_Type()
)
alaFcNodeWwpn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFcNodeWwpn.setStatus("current")


class _AlaFcNodeVsanNumber_Type(Integer32):
    """Custom type alaFcNodeVsanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaFcNodeVsanNumber_Type.__name__ = "Integer32"
_AlaFcNodeVsanNumber_Object = MibTableColumn
alaFcNodeVsanNumber = _AlaFcNodeVsanNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 15, 1, 1, 3),
    _AlaFcNodeVsanNumber_Type()
)
alaFcNodeVsanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcNodeVsanNumber.setStatus("current")


class _AlaFcNodeVlanNumber_Type(Integer32):
    """Custom type alaFcNodeVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaFcNodeVlanNumber_Type.__name__ = "Integer32"
_AlaFcNodeVlanNumber_Object = MibTableColumn
alaFcNodeVlanNumber = _AlaFcNodeVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 15, 1, 1, 4),
    _AlaFcNodeVlanNumber_Type()
)
alaFcNodeVlanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcNodeVlanNumber.setStatus("current")
_AlaFcNodeFcid_Type = Fcid
_AlaFcNodeFcid_Object = MibTableColumn
alaFcNodeFcid = _AlaFcNodeFcid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 15, 1, 1, 5),
    _AlaFcNodeFcid_Type()
)
alaFcNodeFcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcNodeFcid.setStatus("current")
_AlaFcNodeWwnn_Type = Wwnn
_AlaFcNodeWwnn_Object = MibTableColumn
alaFcNodeWwnn = _AlaFcNodeWwnn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 15, 1, 1, 6),
    _AlaFcNodeWwnn_Type()
)
alaFcNodeWwnn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcNodeWwnn.setStatus("current")
_AlaFcSess_ObjectIdentity = ObjectIdentity
alaFcSess = _AlaFcSess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 16)
)
_AlaFcSessTable_Object = MibTable
alaFcSessTable = _AlaFcSessTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 16, 1)
)
if mibBuilder.loadTexts:
    alaFcSessTable.setStatus("current")
_AlaFcSessEntry_Object = MibTableRow
alaFcSessEntry = _AlaFcSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 16, 1, 1)
)
alaFcSessEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFcSessIfIndex"),
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFcSessWwpn"),
)
if mibBuilder.loadTexts:
    alaFcSessEntry.setStatus("current")
_AlaFcSessIfIndex_Type = InterfaceIndex
_AlaFcSessIfIndex_Object = MibTableColumn
alaFcSessIfIndex = _AlaFcSessIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 16, 1, 1, 1),
    _AlaFcSessIfIndex_Type()
)
alaFcSessIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFcSessIfIndex.setStatus("current")
_AlaFcSessWwpn_Type = Wwpn
_AlaFcSessWwpn_Object = MibTableColumn
alaFcSessWwpn = _AlaFcSessWwpn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 16, 1, 1, 2),
    _AlaFcSessWwpn_Type()
)
alaFcSessWwpn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFcSessWwpn.setStatus("current")


class _AlaFcSessVsanNumber_Type(Integer32):
    """Custom type alaFcSessVsanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaFcSessVsanNumber_Type.__name__ = "Integer32"
_AlaFcSessVsanNumber_Object = MibTableColumn
alaFcSessVsanNumber = _AlaFcSessVsanNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 16, 1, 1, 3),
    _AlaFcSessVsanNumber_Type()
)
alaFcSessVsanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcSessVsanNumber.setStatus("current")


class _AlaFcSessStatus_Type(Integer32):
    """Custom type alaFcSessStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pending", 1),
          ("success", 2))
    )


_AlaFcSessStatus_Type.__name__ = "Integer32"
_AlaFcSessStatus_Object = MibTableColumn
alaFcSessStatus = _AlaFcSessStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 16, 1, 1, 4),
    _AlaFcSessStatus_Type()
)
alaFcSessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcSessStatus.setStatus("current")


class _AlaFcSessIntfMode_Type(Integer32):
    """Custom type alaFcSessIntfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("f", 2),
          ("np", 1),
          ("te", 3))
    )


_AlaFcSessIntfMode_Type.__name__ = "Integer32"
_AlaFcSessIntfMode_Object = MibTableColumn
alaFcSessIntfMode = _AlaFcSessIntfMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 16, 1, 1, 5),
    _AlaFcSessIntfMode_Type()
)
alaFcSessIntfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcSessIntfMode.setStatus("current")
_AlaFcSessFcid_Type = Fcid
_AlaFcSessFcid_Object = MibTableColumn
alaFcSessFcid = _AlaFcSessFcid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 16, 1, 1, 6),
    _AlaFcSessFcid_Type()
)
alaFcSessFcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcSessFcid.setStatus("current")


class _AlaFcSessType_Type(Integer32):
    """Custom type alaFcSessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("elp", 3),
          ("fdisc", 1),
          ("flogi", 2))
    )


_AlaFcSessType_Type.__name__ = "Integer32"
_AlaFcSessType_Object = MibTableColumn
alaFcSessType = _AlaFcSessType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 16, 1, 1, 7),
    _AlaFcSessType_Type()
)
alaFcSessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcSessType.setStatus("current")
_AlaFcSessTunnelId_Type = Unsigned32
_AlaFcSessTunnelId_Object = MibTableColumn
alaFcSessTunnelId = _AlaFcSessTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 16, 1, 1, 8),
    _AlaFcSessTunnelId_Type()
)
alaFcSessTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcSessTunnelId.setStatus("current")
_AlaFcIntfNpivStats_ObjectIdentity = ObjectIdentity
alaFcIntfNpivStats = _AlaFcIntfNpivStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 17)
)
_AlaFcIntfNpivStatsTable_Object = MibTable
alaFcIntfNpivStatsTable = _AlaFcIntfNpivStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 17, 1)
)
if mibBuilder.loadTexts:
    alaFcIntfNpivStatsTable.setStatus("current")
_AlaFcIntfNpivStatsEntry_Object = MibTableRow
alaFcIntfNpivStatsEntry = _AlaFcIntfNpivStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 17, 1, 1)
)
alaFcIntfNpivStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFcIntfNpivStatsIfIndex"),
)
if mibBuilder.loadTexts:
    alaFcIntfNpivStatsEntry.setStatus("current")
_AlaFcIntfNpivStatsIfIndex_Type = InterfaceIndex
_AlaFcIntfNpivStatsIfIndex_Object = MibTableColumn
alaFcIntfNpivStatsIfIndex = _AlaFcIntfNpivStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 17, 1, 1, 1),
    _AlaFcIntfNpivStatsIfIndex_Type()
)
alaFcIntfNpivStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFcIntfNpivStatsIfIndex.setStatus("current")
_AlaFcIntfNpivStatsTxFlogis_Type = Counter32
_AlaFcIntfNpivStatsTxFlogis_Object = MibTableColumn
alaFcIntfNpivStatsTxFlogis = _AlaFcIntfNpivStatsTxFlogis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 17, 1, 1, 2),
    _AlaFcIntfNpivStatsTxFlogis_Type()
)
alaFcIntfNpivStatsTxFlogis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfNpivStatsTxFlogis.setStatus("current")
_AlaFcIntfNpivStatsTxFdiscs_Type = Counter32
_AlaFcIntfNpivStatsTxFdiscs_Object = MibTableColumn
alaFcIntfNpivStatsTxFdiscs = _AlaFcIntfNpivStatsTxFdiscs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 17, 1, 1, 3),
    _AlaFcIntfNpivStatsTxFdiscs_Type()
)
alaFcIntfNpivStatsTxFdiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfNpivStatsTxFdiscs.setStatus("current")
_AlaFcIntfNpivStatsRxLsAccs_Type = Counter32
_AlaFcIntfNpivStatsRxLsAccs_Object = MibTableColumn
alaFcIntfNpivStatsRxLsAccs = _AlaFcIntfNpivStatsRxLsAccs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 17, 1, 1, 4),
    _AlaFcIntfNpivStatsRxLsAccs_Type()
)
alaFcIntfNpivStatsRxLsAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfNpivStatsRxLsAccs.setStatus("current")
_AlaFcIntfNpivStatsRxFlogos_Type = Counter32
_AlaFcIntfNpivStatsRxFlogos_Object = MibTableColumn
alaFcIntfNpivStatsRxFlogos = _AlaFcIntfNpivStatsRxFlogos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 17, 1, 1, 5),
    _AlaFcIntfNpivStatsRxFlogos_Type()
)
alaFcIntfNpivStatsRxFlogos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfNpivStatsRxFlogos.setStatus("current")
_AlaFcIntfNpivStatsRxFlogiLsRjts_Type = Counter32
_AlaFcIntfNpivStatsRxFlogiLsRjts_Object = MibTableColumn
alaFcIntfNpivStatsRxFlogiLsRjts = _AlaFcIntfNpivStatsRxFlogiLsRjts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 17, 1, 1, 6),
    _AlaFcIntfNpivStatsRxFlogiLsRjts_Type()
)
alaFcIntfNpivStatsRxFlogiLsRjts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfNpivStatsRxFlogiLsRjts.setStatus("current")
_AlaFcIntfNpivStatsRxFdiscLsRjts_Type = Counter32
_AlaFcIntfNpivStatsRxFdiscLsRjts_Object = MibTableColumn
alaFcIntfNpivStatsRxFdiscLsRjts = _AlaFcIntfNpivStatsRxFdiscLsRjts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 17, 1, 1, 7),
    _AlaFcIntfNpivStatsRxFdiscLsRjts_Type()
)
alaFcIntfNpivStatsRxFdiscLsRjts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfNpivStatsRxFdiscLsRjts.setStatus("current")
_AlaFcIntfNpivStatsTxFlogos_Type = Counter32
_AlaFcIntfNpivStatsTxFlogos_Object = MibTableColumn
alaFcIntfNpivStatsTxFlogos = _AlaFcIntfNpivStatsTxFlogos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 17, 1, 1, 8),
    _AlaFcIntfNpivStatsTxFlogos_Type()
)
alaFcIntfNpivStatsTxFlogos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfNpivStatsTxFlogos.setStatus("current")


class _AlaFcIntfNpivStatsClear_Type(Integer32):
    """Custom type alaFcIntfNpivStatsClear based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("none", 2))
    )


_AlaFcIntfNpivStatsClear_Type.__name__ = "Integer32"
_AlaFcIntfNpivStatsClear_Object = MibTableColumn
alaFcIntfNpivStatsClear = _AlaFcIntfNpivStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 17, 1, 1, 9),
    _AlaFcIntfNpivStatsClear_Type()
)
alaFcIntfNpivStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaFcIntfNpivStatsClear.setStatus("current")
_AlaFcVsanNpivStats_ObjectIdentity = ObjectIdentity
alaFcVsanNpivStats = _AlaFcVsanNpivStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 18)
)
_AlaFcVsanNpivStatsTable_Object = MibTable
alaFcVsanNpivStatsTable = _AlaFcVsanNpivStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 18, 1)
)
if mibBuilder.loadTexts:
    alaFcVsanNpivStatsTable.setStatus("current")
_AlaFcVsanNpivStatsEntry_Object = MibTableRow
alaFcVsanNpivStatsEntry = _AlaFcVsanNpivStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 18, 1, 1)
)
alaFcVsanNpivStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFcVsanNpivStatsVsan"),
)
if mibBuilder.loadTexts:
    alaFcVsanNpivStatsEntry.setStatus("current")


class _AlaFcVsanNpivStatsVsan_Type(Integer32):
    """Custom type alaFcVsanNpivStatsVsan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaFcVsanNpivStatsVsan_Type.__name__ = "Integer32"
_AlaFcVsanNpivStatsVsan_Object = MibTableColumn
alaFcVsanNpivStatsVsan = _AlaFcVsanNpivStatsVsan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 18, 1, 1, 1),
    _AlaFcVsanNpivStatsVsan_Type()
)
alaFcVsanNpivStatsVsan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFcVsanNpivStatsVsan.setStatus("current")
_AlaFcVsanNpivStatsTxFlogis_Type = Counter32
_AlaFcVsanNpivStatsTxFlogis_Object = MibTableColumn
alaFcVsanNpivStatsTxFlogis = _AlaFcVsanNpivStatsTxFlogis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 18, 1, 1, 2),
    _AlaFcVsanNpivStatsTxFlogis_Type()
)
alaFcVsanNpivStatsTxFlogis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcVsanNpivStatsTxFlogis.setStatus("current")
_AlaFcVsanNpivStatsTxFdiscs_Type = Counter32
_AlaFcVsanNpivStatsTxFdiscs_Object = MibTableColumn
alaFcVsanNpivStatsTxFdiscs = _AlaFcVsanNpivStatsTxFdiscs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 18, 1, 1, 3),
    _AlaFcVsanNpivStatsTxFdiscs_Type()
)
alaFcVsanNpivStatsTxFdiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcVsanNpivStatsTxFdiscs.setStatus("current")
_AlaFcVsanNpivStatsRxLsAccs_Type = Counter32
_AlaFcVsanNpivStatsRxLsAccs_Object = MibTableColumn
alaFcVsanNpivStatsRxLsAccs = _AlaFcVsanNpivStatsRxLsAccs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 18, 1, 1, 4),
    _AlaFcVsanNpivStatsRxLsAccs_Type()
)
alaFcVsanNpivStatsRxLsAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcVsanNpivStatsRxLsAccs.setStatus("current")
_AlaFcVsanNpivStatsRxFlogos_Type = Counter32
_AlaFcVsanNpivStatsRxFlogos_Object = MibTableColumn
alaFcVsanNpivStatsRxFlogos = _AlaFcVsanNpivStatsRxFlogos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 18, 1, 1, 5),
    _AlaFcVsanNpivStatsRxFlogos_Type()
)
alaFcVsanNpivStatsRxFlogos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcVsanNpivStatsRxFlogos.setStatus("current")
_AlaFcVsanNpivStatsRxFlogiLsRjts_Type = Counter32
_AlaFcVsanNpivStatsRxFlogiLsRjts_Object = MibTableColumn
alaFcVsanNpivStatsRxFlogiLsRjts = _AlaFcVsanNpivStatsRxFlogiLsRjts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 18, 1, 1, 6),
    _AlaFcVsanNpivStatsRxFlogiLsRjts_Type()
)
alaFcVsanNpivStatsRxFlogiLsRjts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcVsanNpivStatsRxFlogiLsRjts.setStatus("current")
_AlaFcVsanNpivStatsRxFdiscLsRjts_Type = Counter32
_AlaFcVsanNpivStatsRxFdiscLsRjts_Object = MibTableColumn
alaFcVsanNpivStatsRxFdiscLsRjts = _AlaFcVsanNpivStatsRxFdiscLsRjts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 18, 1, 1, 7),
    _AlaFcVsanNpivStatsRxFdiscLsRjts_Type()
)
alaFcVsanNpivStatsRxFdiscLsRjts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcVsanNpivStatsRxFdiscLsRjts.setStatus("current")
_AlaFcVsanNpivStatsTxFlogos_Type = Counter32
_AlaFcVsanNpivStatsTxFlogos_Object = MibTableColumn
alaFcVsanNpivStatsTxFlogos = _AlaFcVsanNpivStatsTxFlogos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 18, 1, 1, 8),
    _AlaFcVsanNpivStatsTxFlogos_Type()
)
alaFcVsanNpivStatsTxFlogos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcVsanNpivStatsTxFlogos.setStatus("current")
_AlaFcIntfRnpivStats_ObjectIdentity = ObjectIdentity
alaFcIntfRnpivStats = _AlaFcIntfRnpivStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 19)
)
_AlaFcIntfRnpivStatsTable_Object = MibTable
alaFcIntfRnpivStatsTable = _AlaFcIntfRnpivStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 19, 1)
)
if mibBuilder.loadTexts:
    alaFcIntfRnpivStatsTable.setStatus("current")
_AlaFcIntfRnpivStatsEntry_Object = MibTableRow
alaFcIntfRnpivStatsEntry = _AlaFcIntfRnpivStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 19, 1, 1)
)
alaFcIntfRnpivStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFcIntfRnpivStatsIfIndex"),
)
if mibBuilder.loadTexts:
    alaFcIntfRnpivStatsEntry.setStatus("current")
_AlaFcIntfRnpivStatsIfIndex_Type = InterfaceIndex
_AlaFcIntfRnpivStatsIfIndex_Object = MibTableColumn
alaFcIntfRnpivStatsIfIndex = _AlaFcIntfRnpivStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 19, 1, 1, 1),
    _AlaFcIntfRnpivStatsIfIndex_Type()
)
alaFcIntfRnpivStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFcIntfRnpivStatsIfIndex.setStatus("current")
_AlaFcIntfRnpivStatsRxFlogis_Type = Counter32
_AlaFcIntfRnpivStatsRxFlogis_Object = MibTableColumn
alaFcIntfRnpivStatsRxFlogis = _AlaFcIntfRnpivStatsRxFlogis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 19, 1, 1, 2),
    _AlaFcIntfRnpivStatsRxFlogis_Type()
)
alaFcIntfRnpivStatsRxFlogis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfRnpivStatsRxFlogis.setStatus("current")
_AlaFcIntfRnpivStatsRxFdiscs_Type = Counter32
_AlaFcIntfRnpivStatsRxFdiscs_Object = MibTableColumn
alaFcIntfRnpivStatsRxFdiscs = _AlaFcIntfRnpivStatsRxFdiscs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 19, 1, 1, 3),
    _AlaFcIntfRnpivStatsRxFdiscs_Type()
)
alaFcIntfRnpivStatsRxFdiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfRnpivStatsRxFdiscs.setStatus("current")
_AlaFcIntfRnpivStatsTxFlogiLsAccs_Type = Counter32
_AlaFcIntfRnpivStatsTxFlogiLsAccs_Object = MibTableColumn
alaFcIntfRnpivStatsTxFlogiLsAccs = _AlaFcIntfRnpivStatsTxFlogiLsAccs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 19, 1, 1, 4),
    _AlaFcIntfRnpivStatsTxFlogiLsAccs_Type()
)
alaFcIntfRnpivStatsTxFlogiLsAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfRnpivStatsTxFlogiLsAccs.setStatus("current")
_AlaFcIntfRnpivStatsTxFdiscLsAccs_Type = Counter32
_AlaFcIntfRnpivStatsTxFdiscLsAccs_Object = MibTableColumn
alaFcIntfRnpivStatsTxFdiscLsAccs = _AlaFcIntfRnpivStatsTxFdiscLsAccs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 19, 1, 1, 5),
    _AlaFcIntfRnpivStatsTxFdiscLsAccs_Type()
)
alaFcIntfRnpivStatsTxFdiscLsAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfRnpivStatsTxFdiscLsAccs.setStatus("current")
_AlaFcIntfRnpivStatsTxFlogos_Type = Counter32
_AlaFcIntfRnpivStatsTxFlogos_Object = MibTableColumn
alaFcIntfRnpivStatsTxFlogos = _AlaFcIntfRnpivStatsTxFlogos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 19, 1, 1, 6),
    _AlaFcIntfRnpivStatsTxFlogos_Type()
)
alaFcIntfRnpivStatsTxFlogos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfRnpivStatsTxFlogos.setStatus("current")
_AlaFcIntfRnpivStatsTxFlogiLsRjts_Type = Counter32
_AlaFcIntfRnpivStatsTxFlogiLsRjts_Object = MibTableColumn
alaFcIntfRnpivStatsTxFlogiLsRjts = _AlaFcIntfRnpivStatsTxFlogiLsRjts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 19, 1, 1, 7),
    _AlaFcIntfRnpivStatsTxFlogiLsRjts_Type()
)
alaFcIntfRnpivStatsTxFlogiLsRjts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfRnpivStatsTxFlogiLsRjts.setStatus("current")
_AlaFcIntfRnpivStatsTxFdiscLsRjts_Type = Counter32
_AlaFcIntfRnpivStatsTxFdiscLsRjts_Object = MibTableColumn
alaFcIntfRnpivStatsTxFdiscLsRjts = _AlaFcIntfRnpivStatsTxFdiscLsRjts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 19, 1, 1, 8),
    _AlaFcIntfRnpivStatsTxFdiscLsRjts_Type()
)
alaFcIntfRnpivStatsTxFdiscLsRjts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfRnpivStatsTxFdiscLsRjts.setStatus("current")
_AlaFcIntfRnpivStatsRxFlogos_Type = Counter32
_AlaFcIntfRnpivStatsRxFlogos_Object = MibTableColumn
alaFcIntfRnpivStatsRxFlogos = _AlaFcIntfRnpivStatsRxFlogos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 19, 1, 1, 9),
    _AlaFcIntfRnpivStatsRxFlogos_Type()
)
alaFcIntfRnpivStatsRxFlogos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfRnpivStatsRxFlogos.setStatus("current")


class _AlaFcIntfRnpivStatsClear_Type(Integer32):
    """Custom type alaFcIntfRnpivStatsClear based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("none", 2))
    )


_AlaFcIntfRnpivStatsClear_Type.__name__ = "Integer32"
_AlaFcIntfRnpivStatsClear_Object = MibTableColumn
alaFcIntfRnpivStatsClear = _AlaFcIntfRnpivStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 19, 1, 1, 10),
    _AlaFcIntfRnpivStatsClear_Type()
)
alaFcIntfRnpivStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaFcIntfRnpivStatsClear.setStatus("current")
_AlaFcVsanRnpivStats_ObjectIdentity = ObjectIdentity
alaFcVsanRnpivStats = _AlaFcVsanRnpivStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 20)
)
_AlaFcVsanRnpivStatsTable_Object = MibTable
alaFcVsanRnpivStatsTable = _AlaFcVsanRnpivStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 20, 1)
)
if mibBuilder.loadTexts:
    alaFcVsanRnpivStatsTable.setStatus("current")
_AlaFcVsanRnpivStatsEntry_Object = MibTableRow
alaFcVsanRnpivStatsEntry = _AlaFcVsanRnpivStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 20, 1, 1)
)
alaFcVsanRnpivStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFcVsanRnpivStatsVsan"),
)
if mibBuilder.loadTexts:
    alaFcVsanRnpivStatsEntry.setStatus("current")


class _AlaFcVsanRnpivStatsVsan_Type(Integer32):
    """Custom type alaFcVsanRnpivStatsVsan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaFcVsanRnpivStatsVsan_Type.__name__ = "Integer32"
_AlaFcVsanRnpivStatsVsan_Object = MibTableColumn
alaFcVsanRnpivStatsVsan = _AlaFcVsanRnpivStatsVsan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 20, 1, 1, 1),
    _AlaFcVsanRnpivStatsVsan_Type()
)
alaFcVsanRnpivStatsVsan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFcVsanRnpivStatsVsan.setStatus("current")
_AlaFcVsanRnpivStatsRxFlogis_Type = Counter32
_AlaFcVsanRnpivStatsRxFlogis_Object = MibTableColumn
alaFcVsanRnpivStatsRxFlogis = _AlaFcVsanRnpivStatsRxFlogis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 20, 1, 1, 2),
    _AlaFcVsanRnpivStatsRxFlogis_Type()
)
alaFcVsanRnpivStatsRxFlogis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcVsanRnpivStatsRxFlogis.setStatus("current")
_AlaFcVsanRnpivStatsRxFdiscs_Type = Counter32
_AlaFcVsanRnpivStatsRxFdiscs_Object = MibTableColumn
alaFcVsanRnpivStatsRxFdiscs = _AlaFcVsanRnpivStatsRxFdiscs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 20, 1, 1, 3),
    _AlaFcVsanRnpivStatsRxFdiscs_Type()
)
alaFcVsanRnpivStatsRxFdiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcVsanRnpivStatsRxFdiscs.setStatus("current")
_AlaFcVsanRnpivStatsTxFlogiLsAccs_Type = Counter32
_AlaFcVsanRnpivStatsTxFlogiLsAccs_Object = MibTableColumn
alaFcVsanRnpivStatsTxFlogiLsAccs = _AlaFcVsanRnpivStatsTxFlogiLsAccs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 20, 1, 1, 4),
    _AlaFcVsanRnpivStatsTxFlogiLsAccs_Type()
)
alaFcVsanRnpivStatsTxFlogiLsAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcVsanRnpivStatsTxFlogiLsAccs.setStatus("current")
_AlaFcVsanRnpivStatsTxFdiscLsAccs_Type = Counter32
_AlaFcVsanRnpivStatsTxFdiscLsAccs_Object = MibTableColumn
alaFcVsanRnpivStatsTxFdiscLsAccs = _AlaFcVsanRnpivStatsTxFdiscLsAccs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 20, 1, 1, 5),
    _AlaFcVsanRnpivStatsTxFdiscLsAccs_Type()
)
alaFcVsanRnpivStatsTxFdiscLsAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcVsanRnpivStatsTxFdiscLsAccs.setStatus("current")
_AlaFcVsanRnpivStatsTxFlogos_Type = Counter32
_AlaFcVsanRnpivStatsTxFlogos_Object = MibTableColumn
alaFcVsanRnpivStatsTxFlogos = _AlaFcVsanRnpivStatsTxFlogos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 20, 1, 1, 6),
    _AlaFcVsanRnpivStatsTxFlogos_Type()
)
alaFcVsanRnpivStatsTxFlogos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcVsanRnpivStatsTxFlogos.setStatus("current")
_AlaFcVsanRnpivStatsTxFlogiLsRjts_Type = Counter32
_AlaFcVsanRnpivStatsTxFlogiLsRjts_Object = MibTableColumn
alaFcVsanRnpivStatsTxFlogiLsRjts = _AlaFcVsanRnpivStatsTxFlogiLsRjts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 20, 1, 1, 7),
    _AlaFcVsanRnpivStatsTxFlogiLsRjts_Type()
)
alaFcVsanRnpivStatsTxFlogiLsRjts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcVsanRnpivStatsTxFlogiLsRjts.setStatus("current")
_AlaFcVsanRnpivStatsTxFdiscLsRjts_Type = Counter32
_AlaFcVsanRnpivStatsTxFdiscLsRjts_Object = MibTableColumn
alaFcVsanRnpivStatsTxFdiscLsRjts = _AlaFcVsanRnpivStatsTxFdiscLsRjts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 20, 1, 1, 8),
    _AlaFcVsanRnpivStatsTxFdiscLsRjts_Type()
)
alaFcVsanRnpivStatsTxFdiscLsRjts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcVsanRnpivStatsTxFdiscLsRjts.setStatus("current")
_AlaFcVsanRnpivStatsRxFlogos_Type = Counter32
_AlaFcVsanRnpivStatsRxFlogos_Object = MibTableColumn
alaFcVsanRnpivStatsRxFlogos = _AlaFcVsanRnpivStatsRxFlogos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 20, 1, 1, 9),
    _AlaFcVsanRnpivStatsRxFlogos_Type()
)
alaFcVsanRnpivStatsRxFlogos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcVsanRnpivStatsRxFlogos.setStatus("current")
_AlaFcInfo_ObjectIdentity = ObjectIdentity
alaFcInfo = _AlaFcInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 21)
)


class _AlaFcConfigSessClear_Type(Integer32):
    """Custom type alaFcConfigSessClear based on Integer32"""
    defaultValue = 5

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
        *(("all", 1),
          ("eTunnel", 4),
          ("none", 5),
          ("npiv", 2),
          ("reverseNpiv", 3))
    )


_AlaFcConfigSessClear_Type.__name__ = "Integer32"
_AlaFcConfigSessClear_Object = MibScalar
alaFcConfigSessClear = _AlaFcConfigSessClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 21, 1),
    _AlaFcConfigSessClear_Type()
)
alaFcConfigSessClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaFcConfigSessClear.setStatus("current")


class _AlaFcConfigStatsClear_Type(Integer32):
    """Custom type alaFcConfigStatsClear based on Integer32"""
    defaultValue = 5

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
        *(("all", 1),
          ("eTunnel", 4),
          ("none", 5),
          ("npiv", 2),
          ("reverseNpiv", 3))
    )


_AlaFcConfigStatsClear_Type.__name__ = "Integer32"
_AlaFcConfigStatsClear_Object = MibScalar
alaFcConfigStatsClear = _AlaFcConfigStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 21, 2),
    _AlaFcConfigStatsClear_Type()
)
alaFcConfigStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaFcConfigStatsClear.setStatus("current")


class _AlaFcConfigNpivLoadBalance_Type(Integer32):
    """Custom type alaFcConfigNpivLoadBalance based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("dynamicReorder", 2),
          ("enodeBased", 3))
    )


_AlaFcConfigNpivLoadBalance_Type.__name__ = "Integer32"
_AlaFcConfigNpivLoadBalance_Object = MibScalar
alaFcConfigNpivLoadBalance = _AlaFcConfigNpivLoadBalance_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 21, 3),
    _AlaFcConfigNpivLoadBalance_Type()
)
alaFcConfigNpivLoadBalance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaFcConfigNpivLoadBalance.setStatus("current")
_AlaFcConfigWwnn_Type = Wwnn
_AlaFcConfigWwnn_Object = MibScalar
alaFcConfigWwnn = _AlaFcConfigWwnn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 21, 4),
    _AlaFcConfigWwnn_Type()
)
alaFcConfigWwnn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaFcConfigWwnn.setStatus("current")
_AlaFipsVlanNpivDiscStats_ObjectIdentity = ObjectIdentity
alaFipsVlanNpivDiscStats = _AlaFipsVlanNpivDiscStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 22)
)
_AlaFipsVlanNpivDiscStatsTable_Object = MibTable
alaFipsVlanNpivDiscStatsTable = _AlaFipsVlanNpivDiscStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 22, 1)
)
if mibBuilder.loadTexts:
    alaFipsVlanNpivDiscStatsTable.setStatus("current")
_AlaFipsVlanNpivDiscStatsEntry_Object = MibTableRow
alaFipsVlanNpivDiscStatsEntry = _AlaFipsVlanNpivDiscStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 22, 1, 1)
)
alaFipsVlanNpivDiscStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsVlanNpivDiscStatsVlanId"),
)
if mibBuilder.loadTexts:
    alaFipsVlanNpivDiscStatsEntry.setStatus("current")


class _AlaFipsVlanNpivDiscStatsVlanId_Type(Integer32):
    """Custom type alaFipsVlanNpivDiscStatsVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaFipsVlanNpivDiscStatsVlanId_Type.__name__ = "Integer32"
_AlaFipsVlanNpivDiscStatsVlanId_Object = MibTableColumn
alaFipsVlanNpivDiscStatsVlanId = _AlaFipsVlanNpivDiscStatsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 22, 1, 1, 1),
    _AlaFipsVlanNpivDiscStatsVlanId_Type()
)
alaFipsVlanNpivDiscStatsVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsVlanNpivDiscStatsVlanId.setStatus("current")
_AlaFipsVlanNpivDiscStatsRxVlanDiscRqs_Type = Counter32
_AlaFipsVlanNpivDiscStatsRxVlanDiscRqs_Object = MibTableColumn
alaFipsVlanNpivDiscStatsRxVlanDiscRqs = _AlaFipsVlanNpivDiscStatsRxVlanDiscRqs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 22, 1, 1, 2),
    _AlaFipsVlanNpivDiscStatsRxVlanDiscRqs_Type()
)
alaFipsVlanNpivDiscStatsRxVlanDiscRqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanNpivDiscStatsRxVlanDiscRqs.setStatus("current")
_AlaFipsVlanNpivDiscStatsTxVlanDiscResps_Type = Counter32
_AlaFipsVlanNpivDiscStatsTxVlanDiscResps_Object = MibTableColumn
alaFipsVlanNpivDiscStatsTxVlanDiscResps = _AlaFipsVlanNpivDiscStatsTxVlanDiscResps_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 22, 1, 1, 3),
    _AlaFipsVlanNpivDiscStatsTxVlanDiscResps_Type()
)
alaFipsVlanNpivDiscStatsTxVlanDiscResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanNpivDiscStatsTxVlanDiscResps.setStatus("current")
_AlaFipsVlanNpivDiscStatsRxMdss_Type = Counter32
_AlaFipsVlanNpivDiscStatsRxMdss_Object = MibTableColumn
alaFipsVlanNpivDiscStatsRxMdss = _AlaFipsVlanNpivDiscStatsRxMdss_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 22, 1, 1, 4),
    _AlaFipsVlanNpivDiscStatsRxMdss_Type()
)
alaFipsVlanNpivDiscStatsRxMdss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanNpivDiscStatsRxMdss.setStatus("current")
_AlaFipsVlanNpivDiscStatsRxUdss_Type = Counter32
_AlaFipsVlanNpivDiscStatsRxUdss_Object = MibTableColumn
alaFipsVlanNpivDiscStatsRxUdss = _AlaFipsVlanNpivDiscStatsRxUdss_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 22, 1, 1, 5),
    _AlaFipsVlanNpivDiscStatsRxUdss_Type()
)
alaFipsVlanNpivDiscStatsRxUdss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanNpivDiscStatsRxUdss.setStatus("current")
_AlaFipsVlanNpivDiscStatsTxMdas_Type = Counter32
_AlaFipsVlanNpivDiscStatsTxMdas_Object = MibTableColumn
alaFipsVlanNpivDiscStatsTxMdas = _AlaFipsVlanNpivDiscStatsTxMdas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 22, 1, 1, 6),
    _AlaFipsVlanNpivDiscStatsTxMdas_Type()
)
alaFipsVlanNpivDiscStatsTxMdas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanNpivDiscStatsTxMdas.setStatus("current")
_AlaFipsVlanNpivDiscStatsTxUdas_Type = Counter32
_AlaFipsVlanNpivDiscStatsTxUdas_Object = MibTableColumn
alaFipsVlanNpivDiscStatsTxUdas = _AlaFipsVlanNpivDiscStatsTxUdas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 22, 1, 1, 7),
    _AlaFipsVlanNpivDiscStatsTxUdas_Type()
)
alaFipsVlanNpivDiscStatsTxUdas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanNpivDiscStatsTxUdas.setStatus("current")
_AlaFipsIntfNpivDiscStats_ObjectIdentity = ObjectIdentity
alaFipsIntfNpivDiscStats = _AlaFipsIntfNpivDiscStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 23)
)
_AlaFipsIntfNpivDiscStatsTable_Object = MibTable
alaFipsIntfNpivDiscStatsTable = _AlaFipsIntfNpivDiscStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 23, 1)
)
if mibBuilder.loadTexts:
    alaFipsIntfNpivDiscStatsTable.setStatus("current")
_AlaFipsIntfNpivDiscStatsEntry_Object = MibTableRow
alaFipsIntfNpivDiscStatsEntry = _AlaFipsIntfNpivDiscStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 23, 1, 1)
)
alaFipsIntfNpivDiscStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsIntfNpivDiscStatsIfIndex"),
)
if mibBuilder.loadTexts:
    alaFipsIntfNpivDiscStatsEntry.setStatus("current")
_AlaFipsIntfNpivDiscStatsIfIndex_Type = InterfaceIndex
_AlaFipsIntfNpivDiscStatsIfIndex_Object = MibTableColumn
alaFipsIntfNpivDiscStatsIfIndex = _AlaFipsIntfNpivDiscStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 23, 1, 1, 1),
    _AlaFipsIntfNpivDiscStatsIfIndex_Type()
)
alaFipsIntfNpivDiscStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsIntfNpivDiscStatsIfIndex.setStatus("current")
_AlaFipsIntfNpivDiscStatsRxVlanDiscRqs_Type = Counter32
_AlaFipsIntfNpivDiscStatsRxVlanDiscRqs_Object = MibTableColumn
alaFipsIntfNpivDiscStatsRxVlanDiscRqs = _AlaFipsIntfNpivDiscStatsRxVlanDiscRqs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 23, 1, 1, 2),
    _AlaFipsIntfNpivDiscStatsRxVlanDiscRqs_Type()
)
alaFipsIntfNpivDiscStatsRxVlanDiscRqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfNpivDiscStatsRxVlanDiscRqs.setStatus("current")
_AlaFipsIntfNpivDiscStatsTxVlanDiscResps_Type = Counter32
_AlaFipsIntfNpivDiscStatsTxVlanDiscResps_Object = MibTableColumn
alaFipsIntfNpivDiscStatsTxVlanDiscResps = _AlaFipsIntfNpivDiscStatsTxVlanDiscResps_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 23, 1, 1, 3),
    _AlaFipsIntfNpivDiscStatsTxVlanDiscResps_Type()
)
alaFipsIntfNpivDiscStatsTxVlanDiscResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfNpivDiscStatsTxVlanDiscResps.setStatus("current")
_AlaFipsIntfNpivDiscStatsRxMdss_Type = Counter32
_AlaFipsIntfNpivDiscStatsRxMdss_Object = MibTableColumn
alaFipsIntfNpivDiscStatsRxMdss = _AlaFipsIntfNpivDiscStatsRxMdss_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 23, 1, 1, 4),
    _AlaFipsIntfNpivDiscStatsRxMdss_Type()
)
alaFipsIntfNpivDiscStatsRxMdss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfNpivDiscStatsRxMdss.setStatus("current")
_AlaFipsIntfNpivDiscStatsRxUdss_Type = Counter32
_AlaFipsIntfNpivDiscStatsRxUdss_Object = MibTableColumn
alaFipsIntfNpivDiscStatsRxUdss = _AlaFipsIntfNpivDiscStatsRxUdss_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 23, 1, 1, 5),
    _AlaFipsIntfNpivDiscStatsRxUdss_Type()
)
alaFipsIntfNpivDiscStatsRxUdss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfNpivDiscStatsRxUdss.setStatus("current")
_AlaFipsIntfNpivDiscStatsTxMdas_Type = Counter32
_AlaFipsIntfNpivDiscStatsTxMdas_Object = MibTableColumn
alaFipsIntfNpivDiscStatsTxMdas = _AlaFipsIntfNpivDiscStatsTxMdas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 23, 1, 1, 6),
    _AlaFipsIntfNpivDiscStatsTxMdas_Type()
)
alaFipsIntfNpivDiscStatsTxMdas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfNpivDiscStatsTxMdas.setStatus("current")
_AlaFipsIntfNpivDiscStatsTxUdas_Type = Counter32
_AlaFipsIntfNpivDiscStatsTxUdas_Object = MibTableColumn
alaFipsIntfNpivDiscStatsTxUdas = _AlaFipsIntfNpivDiscStatsTxUdas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 23, 1, 1, 7),
    _AlaFipsIntfNpivDiscStatsTxUdas_Type()
)
alaFipsIntfNpivDiscStatsTxUdas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfNpivDiscStatsTxUdas.setStatus("current")
_AlaFipsVlanNpivLoginStats_ObjectIdentity = ObjectIdentity
alaFipsVlanNpivLoginStats = _AlaFipsVlanNpivLoginStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 24)
)
_AlaFipsVlanNpivLoginStatsTable_Object = MibTable
alaFipsVlanNpivLoginStatsTable = _AlaFipsVlanNpivLoginStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 24, 1)
)
if mibBuilder.loadTexts:
    alaFipsVlanNpivLoginStatsTable.setStatus("current")
_AlaFipsVlanNpivLoginStatsEntry_Object = MibTableRow
alaFipsVlanNpivLoginStatsEntry = _AlaFipsVlanNpivLoginStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 24, 1, 1)
)
alaFipsVlanNpivLoginStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsVlanNpivLoginStatsVlanId"),
)
if mibBuilder.loadTexts:
    alaFipsVlanNpivLoginStatsEntry.setStatus("current")


class _AlaFipsVlanNpivLoginStatsVlanId_Type(Integer32):
    """Custom type alaFipsVlanNpivLoginStatsVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaFipsVlanNpivLoginStatsVlanId_Type.__name__ = "Integer32"
_AlaFipsVlanNpivLoginStatsVlanId_Object = MibTableColumn
alaFipsVlanNpivLoginStatsVlanId = _AlaFipsVlanNpivLoginStatsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 24, 1, 1, 1),
    _AlaFipsVlanNpivLoginStatsVlanId_Type()
)
alaFipsVlanNpivLoginStatsVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsVlanNpivLoginStatsVlanId.setStatus("current")
_AlaFipsVlanNpivLoginStatsRxFlogis_Type = Counter32
_AlaFipsVlanNpivLoginStatsRxFlogis_Object = MibTableColumn
alaFipsVlanNpivLoginStatsRxFlogis = _AlaFipsVlanNpivLoginStatsRxFlogis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 24, 1, 1, 2),
    _AlaFipsVlanNpivLoginStatsRxFlogis_Type()
)
alaFipsVlanNpivLoginStatsRxFlogis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanNpivLoginStatsRxFlogis.setStatus("current")
_AlaFipsVlanNpivLoginStatsRxFdiscs_Type = Counter32
_AlaFipsVlanNpivLoginStatsRxFdiscs_Object = MibTableColumn
alaFipsVlanNpivLoginStatsRxFdiscs = _AlaFipsVlanNpivLoginStatsRxFdiscs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 24, 1, 1, 3),
    _AlaFipsVlanNpivLoginStatsRxFdiscs_Type()
)
alaFipsVlanNpivLoginStatsRxFdiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanNpivLoginStatsRxFdiscs.setStatus("current")
_AlaFipsVlanNpivLoginStatsTxFlogiAccs_Type = Counter32
_AlaFipsVlanNpivLoginStatsTxFlogiAccs_Object = MibTableColumn
alaFipsVlanNpivLoginStatsTxFlogiAccs = _AlaFipsVlanNpivLoginStatsTxFlogiAccs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 24, 1, 1, 4),
    _AlaFipsVlanNpivLoginStatsTxFlogiAccs_Type()
)
alaFipsVlanNpivLoginStatsTxFlogiAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanNpivLoginStatsTxFlogiAccs.setStatus("current")
_AlaFipsVlanNpivLoginStatsTxFlogiLsRjts_Type = Counter32
_AlaFipsVlanNpivLoginStatsTxFlogiLsRjts_Object = MibTableColumn
alaFipsVlanNpivLoginStatsTxFlogiLsRjts = _AlaFipsVlanNpivLoginStatsTxFlogiLsRjts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 24, 1, 1, 5),
    _AlaFipsVlanNpivLoginStatsTxFlogiLsRjts_Type()
)
alaFipsVlanNpivLoginStatsTxFlogiLsRjts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanNpivLoginStatsTxFlogiLsRjts.setStatus("current")
_AlaFipsVlanNpivLoginStatsTxFdiscLsRjts_Type = Counter32
_AlaFipsVlanNpivLoginStatsTxFdiscLsRjts_Object = MibTableColumn
alaFipsVlanNpivLoginStatsTxFdiscLsRjts = _AlaFipsVlanNpivLoginStatsTxFdiscLsRjts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 24, 1, 1, 6),
    _AlaFipsVlanNpivLoginStatsTxFdiscLsRjts_Type()
)
alaFipsVlanNpivLoginStatsTxFdiscLsRjts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanNpivLoginStatsTxFdiscLsRjts.setStatus("current")
_AlaFipsVlanNpivLoginStatsRxLogos_Type = Counter32
_AlaFipsVlanNpivLoginStatsRxLogos_Object = MibTableColumn
alaFipsVlanNpivLoginStatsRxLogos = _AlaFipsVlanNpivLoginStatsRxLogos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 24, 1, 1, 7),
    _AlaFipsVlanNpivLoginStatsRxLogos_Type()
)
alaFipsVlanNpivLoginStatsRxLogos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanNpivLoginStatsRxLogos.setStatus("current")
_AlaFipsVlanNpivLoginStatsTxCvls_Type = Counter32
_AlaFipsVlanNpivLoginStatsTxCvls_Object = MibTableColumn
alaFipsVlanNpivLoginStatsTxCvls = _AlaFipsVlanNpivLoginStatsTxCvls_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 24, 1, 1, 8),
    _AlaFipsVlanNpivLoginStatsTxCvls_Type()
)
alaFipsVlanNpivLoginStatsTxCvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanNpivLoginStatsTxCvls.setStatus("current")
_AlaFipsVlanNpivLoginStatsRxEkas_Type = Counter32
_AlaFipsVlanNpivLoginStatsRxEkas_Object = MibTableColumn
alaFipsVlanNpivLoginStatsRxEkas = _AlaFipsVlanNpivLoginStatsRxEkas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 24, 1, 1, 9),
    _AlaFipsVlanNpivLoginStatsRxEkas_Type()
)
alaFipsVlanNpivLoginStatsRxEkas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanNpivLoginStatsRxEkas.setStatus("current")
_AlaFipsVlanNpivLoginStatsRxVnkas_Type = Counter32
_AlaFipsVlanNpivLoginStatsRxVnkas_Object = MibTableColumn
alaFipsVlanNpivLoginStatsRxVnkas = _AlaFipsVlanNpivLoginStatsRxVnkas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 24, 1, 1, 10),
    _AlaFipsVlanNpivLoginStatsRxVnkas_Type()
)
alaFipsVlanNpivLoginStatsRxVnkas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanNpivLoginStatsRxVnkas.setStatus("current")
_AlaFipsVlanNpivLoginStatsTxFDiscAccs_Type = Counter32
_AlaFipsVlanNpivLoginStatsTxFDiscAccs_Object = MibTableColumn
alaFipsVlanNpivLoginStatsTxFDiscAccs = _AlaFipsVlanNpivLoginStatsTxFDiscAccs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 24, 1, 1, 11),
    _AlaFipsVlanNpivLoginStatsTxFDiscAccs_Type()
)
alaFipsVlanNpivLoginStatsTxFDiscAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanNpivLoginStatsTxFDiscAccs.setStatus("current")
_AlaFipsVlanNpivLoginStatsTxFlogoAccs_Type = Counter32
_AlaFipsVlanNpivLoginStatsTxFlogoAccs_Object = MibTableColumn
alaFipsVlanNpivLoginStatsTxFlogoAccs = _AlaFipsVlanNpivLoginStatsTxFlogoAccs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 24, 1, 1, 12),
    _AlaFipsVlanNpivLoginStatsTxFlogoAccs_Type()
)
alaFipsVlanNpivLoginStatsTxFlogoAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanNpivLoginStatsTxFlogoAccs.setStatus("current")
_AlaFipsVlanNpivLoginStatsTxFLogoLsRjts_Type = Counter32
_AlaFipsVlanNpivLoginStatsTxFLogoLsRjts_Object = MibTableColumn
alaFipsVlanNpivLoginStatsTxFLogoLsRjts = _AlaFipsVlanNpivLoginStatsTxFLogoLsRjts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 24, 1, 1, 13),
    _AlaFipsVlanNpivLoginStatsTxFLogoLsRjts_Type()
)
alaFipsVlanNpivLoginStatsTxFLogoLsRjts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanNpivLoginStatsTxFLogoLsRjts.setStatus("current")
_AlaFipsIntfNpivLoginStats_ObjectIdentity = ObjectIdentity
alaFipsIntfNpivLoginStats = _AlaFipsIntfNpivLoginStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 25)
)
_AlaFipsIntfNpivLoginStatsTable_Object = MibTable
alaFipsIntfNpivLoginStatsTable = _AlaFipsIntfNpivLoginStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 25, 1)
)
if mibBuilder.loadTexts:
    alaFipsIntfNpivLoginStatsTable.setStatus("current")
_AlaFipsIntfNpivLoginStatsEntry_Object = MibTableRow
alaFipsIntfNpivLoginStatsEntry = _AlaFipsIntfNpivLoginStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 25, 1, 1)
)
alaFipsIntfNpivLoginStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsIntfNpivLoginStatsIfIndex"),
)
if mibBuilder.loadTexts:
    alaFipsIntfNpivLoginStatsEntry.setStatus("current")
_AlaFipsIntfNpivLoginStatsIfIndex_Type = InterfaceIndex
_AlaFipsIntfNpivLoginStatsIfIndex_Object = MibTableColumn
alaFipsIntfNpivLoginStatsIfIndex = _AlaFipsIntfNpivLoginStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 25, 1, 1, 1),
    _AlaFipsIntfNpivLoginStatsIfIndex_Type()
)
alaFipsIntfNpivLoginStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsIntfNpivLoginStatsIfIndex.setStatus("current")
_AlaFipsIntfNpivLoginStatsRxFlogis_Type = Counter32
_AlaFipsIntfNpivLoginStatsRxFlogis_Object = MibTableColumn
alaFipsIntfNpivLoginStatsRxFlogis = _AlaFipsIntfNpivLoginStatsRxFlogis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 25, 1, 1, 2),
    _AlaFipsIntfNpivLoginStatsRxFlogis_Type()
)
alaFipsIntfNpivLoginStatsRxFlogis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfNpivLoginStatsRxFlogis.setStatus("current")
_AlaFipsIntfNpivLoginStatsRxFdiscs_Type = Counter32
_AlaFipsIntfNpivLoginStatsRxFdiscs_Object = MibTableColumn
alaFipsIntfNpivLoginStatsRxFdiscs = _AlaFipsIntfNpivLoginStatsRxFdiscs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 25, 1, 1, 3),
    _AlaFipsIntfNpivLoginStatsRxFdiscs_Type()
)
alaFipsIntfNpivLoginStatsRxFdiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfNpivLoginStatsRxFdiscs.setStatus("current")
_AlaFipsIntfNpivLoginStatsTxFlogiAccs_Type = Counter32
_AlaFipsIntfNpivLoginStatsTxFlogiAccs_Object = MibTableColumn
alaFipsIntfNpivLoginStatsTxFlogiAccs = _AlaFipsIntfNpivLoginStatsTxFlogiAccs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 25, 1, 1, 4),
    _AlaFipsIntfNpivLoginStatsTxFlogiAccs_Type()
)
alaFipsIntfNpivLoginStatsTxFlogiAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfNpivLoginStatsTxFlogiAccs.setStatus("current")
_AlaFipsIntfNpivLoginStatsTxFlogiLsRjts_Type = Counter32
_AlaFipsIntfNpivLoginStatsTxFlogiLsRjts_Object = MibTableColumn
alaFipsIntfNpivLoginStatsTxFlogiLsRjts = _AlaFipsIntfNpivLoginStatsTxFlogiLsRjts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 25, 1, 1, 5),
    _AlaFipsIntfNpivLoginStatsTxFlogiLsRjts_Type()
)
alaFipsIntfNpivLoginStatsTxFlogiLsRjts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfNpivLoginStatsTxFlogiLsRjts.setStatus("current")
_AlaFipsIntfNpivLoginStatsTxFdiscLsRjts_Type = Counter32
_AlaFipsIntfNpivLoginStatsTxFdiscLsRjts_Object = MibTableColumn
alaFipsIntfNpivLoginStatsTxFdiscLsRjts = _AlaFipsIntfNpivLoginStatsTxFdiscLsRjts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 25, 1, 1, 6),
    _AlaFipsIntfNpivLoginStatsTxFdiscLsRjts_Type()
)
alaFipsIntfNpivLoginStatsTxFdiscLsRjts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfNpivLoginStatsTxFdiscLsRjts.setStatus("current")
_AlaFipsIntfNpivLoginStatsRxLogos_Type = Counter32
_AlaFipsIntfNpivLoginStatsRxLogos_Object = MibTableColumn
alaFipsIntfNpivLoginStatsRxLogos = _AlaFipsIntfNpivLoginStatsRxLogos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 25, 1, 1, 7),
    _AlaFipsIntfNpivLoginStatsRxLogos_Type()
)
alaFipsIntfNpivLoginStatsRxLogos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfNpivLoginStatsRxLogos.setStatus("current")
_AlaFipsIntfNpivLoginStatsTxCvls_Type = Counter32
_AlaFipsIntfNpivLoginStatsTxCvls_Object = MibTableColumn
alaFipsIntfNpivLoginStatsTxCvls = _AlaFipsIntfNpivLoginStatsTxCvls_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 25, 1, 1, 8),
    _AlaFipsIntfNpivLoginStatsTxCvls_Type()
)
alaFipsIntfNpivLoginStatsTxCvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfNpivLoginStatsTxCvls.setStatus("current")
_AlaFipsIntfNpivLoginStatsRxEkas_Type = Counter32
_AlaFipsIntfNpivLoginStatsRxEkas_Object = MibTableColumn
alaFipsIntfNpivLoginStatsRxEkas = _AlaFipsIntfNpivLoginStatsRxEkas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 25, 1, 1, 9),
    _AlaFipsIntfNpivLoginStatsRxEkas_Type()
)
alaFipsIntfNpivLoginStatsRxEkas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfNpivLoginStatsRxEkas.setStatus("current")
_AlaFipsIntfNpivLoginStatsRxVnkas_Type = Counter32
_AlaFipsIntfNpivLoginStatsRxVnkas_Object = MibTableColumn
alaFipsIntfNpivLoginStatsRxVnkas = _AlaFipsIntfNpivLoginStatsRxVnkas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 25, 1, 1, 10),
    _AlaFipsIntfNpivLoginStatsRxVnkas_Type()
)
alaFipsIntfNpivLoginStatsRxVnkas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfNpivLoginStatsRxVnkas.setStatus("current")
_AlaFipsIntfNpivLoginStatsTxFDiscAccs_Type = Counter32
_AlaFipsIntfNpivLoginStatsTxFDiscAccs_Object = MibTableColumn
alaFipsIntfNpivLoginStatsTxFDiscAccs = _AlaFipsIntfNpivLoginStatsTxFDiscAccs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 25, 1, 1, 11),
    _AlaFipsIntfNpivLoginStatsTxFDiscAccs_Type()
)
alaFipsIntfNpivLoginStatsTxFDiscAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfNpivLoginStatsTxFDiscAccs.setStatus("current")
_AlaFipsIntfNpivLoginStatsTxFlogoAccs_Type = Counter32
_AlaFipsIntfNpivLoginStatsTxFlogoAccs_Object = MibTableColumn
alaFipsIntfNpivLoginStatsTxFlogoAccs = _AlaFipsIntfNpivLoginStatsTxFlogoAccs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 25, 1, 1, 12),
    _AlaFipsIntfNpivLoginStatsTxFlogoAccs_Type()
)
alaFipsIntfNpivLoginStatsTxFlogoAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfNpivLoginStatsTxFlogoAccs.setStatus("current")
_AlaFipsIntfNpivLoginStatsTxFLogoLsRjts_Type = Counter32
_AlaFipsIntfNpivLoginStatsTxFLogoLsRjts_Object = MibTableColumn
alaFipsIntfNpivLoginStatsTxFLogoLsRjts = _AlaFipsIntfNpivLoginStatsTxFLogoLsRjts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 25, 1, 1, 13),
    _AlaFipsIntfNpivLoginStatsTxFLogoLsRjts_Type()
)
alaFipsIntfNpivLoginStatsTxFLogoLsRjts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfNpivLoginStatsTxFLogoLsRjts.setStatus("current")
_AlaFipsVlanRnpivDiscStats_ObjectIdentity = ObjectIdentity
alaFipsVlanRnpivDiscStats = _AlaFipsVlanRnpivDiscStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 26)
)
_AlaFipsVlanRnpivDiscStatsTable_Object = MibTable
alaFipsVlanRnpivDiscStatsTable = _AlaFipsVlanRnpivDiscStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 26, 1)
)
if mibBuilder.loadTexts:
    alaFipsVlanRnpivDiscStatsTable.setStatus("current")
_AlaFipsVlanRnpivDiscStatsEntry_Object = MibTableRow
alaFipsVlanRnpivDiscStatsEntry = _AlaFipsVlanRnpivDiscStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 26, 1, 1)
)
alaFipsVlanRnpivDiscStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsVlanRnpivDiscStatsVlanId"),
)
if mibBuilder.loadTexts:
    alaFipsVlanRnpivDiscStatsEntry.setStatus("current")


class _AlaFipsVlanRnpivDiscStatsVlanId_Type(Integer32):
    """Custom type alaFipsVlanRnpivDiscStatsVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaFipsVlanRnpivDiscStatsVlanId_Type.__name__ = "Integer32"
_AlaFipsVlanRnpivDiscStatsVlanId_Object = MibTableColumn
alaFipsVlanRnpivDiscStatsVlanId = _AlaFipsVlanRnpivDiscStatsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 26, 1, 1, 1),
    _AlaFipsVlanRnpivDiscStatsVlanId_Type()
)
alaFipsVlanRnpivDiscStatsVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsVlanRnpivDiscStatsVlanId.setStatus("current")
_AlaFipsVlanRnpivDiscStatsRxMdas_Type = Counter32
_AlaFipsVlanRnpivDiscStatsRxMdas_Object = MibTableColumn
alaFipsVlanRnpivDiscStatsRxMdas = _AlaFipsVlanRnpivDiscStatsRxMdas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 26, 1, 1, 2),
    _AlaFipsVlanRnpivDiscStatsRxMdas_Type()
)
alaFipsVlanRnpivDiscStatsRxMdas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanRnpivDiscStatsRxMdas.setStatus("current")
_AlaFipsVlanRnpivDiscStatsRxUdas_Type = Counter32
_AlaFipsVlanRnpivDiscStatsRxUdas_Object = MibTableColumn
alaFipsVlanRnpivDiscStatsRxUdas = _AlaFipsVlanRnpivDiscStatsRxUdas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 26, 1, 1, 3),
    _AlaFipsVlanRnpivDiscStatsRxUdas_Type()
)
alaFipsVlanRnpivDiscStatsRxUdas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanRnpivDiscStatsRxUdas.setStatus("current")
_AlaFipsVlanRnpivDiscStatsTxMdss_Type = Counter32
_AlaFipsVlanRnpivDiscStatsTxMdss_Object = MibTableColumn
alaFipsVlanRnpivDiscStatsTxMdss = _AlaFipsVlanRnpivDiscStatsTxMdss_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 26, 1, 1, 4),
    _AlaFipsVlanRnpivDiscStatsTxMdss_Type()
)
alaFipsVlanRnpivDiscStatsTxMdss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanRnpivDiscStatsTxMdss.setStatus("current")
_AlaFipsVlanRnpivDiscStatsTxUdss_Type = Counter32
_AlaFipsVlanRnpivDiscStatsTxUdss_Object = MibTableColumn
alaFipsVlanRnpivDiscStatsTxUdss = _AlaFipsVlanRnpivDiscStatsTxUdss_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 26, 1, 1, 5),
    _AlaFipsVlanRnpivDiscStatsTxUdss_Type()
)
alaFipsVlanRnpivDiscStatsTxUdss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanRnpivDiscStatsTxUdss.setStatus("current")
_AlaFipsIntfRnpivDiscStats_ObjectIdentity = ObjectIdentity
alaFipsIntfRnpivDiscStats = _AlaFipsIntfRnpivDiscStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 27)
)
_AlaFipsIntfRnpivDiscStatsTable_Object = MibTable
alaFipsIntfRnpivDiscStatsTable = _AlaFipsIntfRnpivDiscStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 27, 1)
)
if mibBuilder.loadTexts:
    alaFipsIntfRnpivDiscStatsTable.setStatus("current")
_AlaFipsIntfRnpivDiscStatsEntry_Object = MibTableRow
alaFipsIntfRnpivDiscStatsEntry = _AlaFipsIntfRnpivDiscStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 27, 1, 1)
)
alaFipsIntfRnpivDiscStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsIntfRnpivDiscStatsIfIndex"),
)
if mibBuilder.loadTexts:
    alaFipsIntfRnpivDiscStatsEntry.setStatus("current")
_AlaFipsIntfRnpivDiscStatsIfIndex_Type = InterfaceIndex
_AlaFipsIntfRnpivDiscStatsIfIndex_Object = MibTableColumn
alaFipsIntfRnpivDiscStatsIfIndex = _AlaFipsIntfRnpivDiscStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 27, 1, 1, 1),
    _AlaFipsIntfRnpivDiscStatsIfIndex_Type()
)
alaFipsIntfRnpivDiscStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsIntfRnpivDiscStatsIfIndex.setStatus("current")
_AlaFipsIntfRnpivDiscStatsRxMdas_Type = Counter32
_AlaFipsIntfRnpivDiscStatsRxMdas_Object = MibTableColumn
alaFipsIntfRnpivDiscStatsRxMdas = _AlaFipsIntfRnpivDiscStatsRxMdas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 27, 1, 1, 2),
    _AlaFipsIntfRnpivDiscStatsRxMdas_Type()
)
alaFipsIntfRnpivDiscStatsRxMdas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfRnpivDiscStatsRxMdas.setStatus("current")
_AlaFipsIntfRnpivDiscStatsRxUdas_Type = Counter32
_AlaFipsIntfRnpivDiscStatsRxUdas_Object = MibTableColumn
alaFipsIntfRnpivDiscStatsRxUdas = _AlaFipsIntfRnpivDiscStatsRxUdas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 27, 1, 1, 3),
    _AlaFipsIntfRnpivDiscStatsRxUdas_Type()
)
alaFipsIntfRnpivDiscStatsRxUdas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfRnpivDiscStatsRxUdas.setStatus("current")
_AlaFipsIntfRnpivDiscStatsTxMdss_Type = Counter32
_AlaFipsIntfRnpivDiscStatsTxMdss_Object = MibTableColumn
alaFipsIntfRnpivDiscStatsTxMdss = _AlaFipsIntfRnpivDiscStatsTxMdss_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 27, 1, 1, 4),
    _AlaFipsIntfRnpivDiscStatsTxMdss_Type()
)
alaFipsIntfRnpivDiscStatsTxMdss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfRnpivDiscStatsTxMdss.setStatus("current")
_AlaFipsIntfRnpivDiscStatsTxUdss_Type = Counter32
_AlaFipsIntfRnpivDiscStatsTxUdss_Object = MibTableColumn
alaFipsIntfRnpivDiscStatsTxUdss = _AlaFipsIntfRnpivDiscStatsTxUdss_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 27, 1, 1, 5),
    _AlaFipsIntfRnpivDiscStatsTxUdss_Type()
)
alaFipsIntfRnpivDiscStatsTxUdss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfRnpivDiscStatsTxUdss.setStatus("current")
_AlaFipsVlanRnpivLoginStats_ObjectIdentity = ObjectIdentity
alaFipsVlanRnpivLoginStats = _AlaFipsVlanRnpivLoginStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 28)
)
_AlaFipsVlanRnpivLoginStatsTable_Object = MibTable
alaFipsVlanRnpivLoginStatsTable = _AlaFipsVlanRnpivLoginStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 28, 1)
)
if mibBuilder.loadTexts:
    alaFipsVlanRnpivLoginStatsTable.setStatus("current")
_AlaFipsVlanRnpivLoginStatsEntry_Object = MibTableRow
alaFipsVlanRnpivLoginStatsEntry = _AlaFipsVlanRnpivLoginStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 28, 1, 1)
)
alaFipsVlanRnpivLoginStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsVlanRnpivLoginStatsVlanId"),
)
if mibBuilder.loadTexts:
    alaFipsVlanRnpivLoginStatsEntry.setStatus("current")


class _AlaFipsVlanRnpivLoginStatsVlanId_Type(Integer32):
    """Custom type alaFipsVlanRnpivLoginStatsVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaFipsVlanRnpivLoginStatsVlanId_Type.__name__ = "Integer32"
_AlaFipsVlanRnpivLoginStatsVlanId_Object = MibTableColumn
alaFipsVlanRnpivLoginStatsVlanId = _AlaFipsVlanRnpivLoginStatsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 28, 1, 1, 1),
    _AlaFipsVlanRnpivLoginStatsVlanId_Type()
)
alaFipsVlanRnpivLoginStatsVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsVlanRnpivLoginStatsVlanId.setStatus("current")
_AlaFipsVlanRnpivLoginStatsTxFlogis_Type = Counter32
_AlaFipsVlanRnpivLoginStatsTxFlogis_Object = MibTableColumn
alaFipsVlanRnpivLoginStatsTxFlogis = _AlaFipsVlanRnpivLoginStatsTxFlogis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 28, 1, 1, 2),
    _AlaFipsVlanRnpivLoginStatsTxFlogis_Type()
)
alaFipsVlanRnpivLoginStatsTxFlogis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanRnpivLoginStatsTxFlogis.setStatus("current")
_AlaFipsVlanRnpivLoginStatsTxFdiscs_Type = Counter32
_AlaFipsVlanRnpivLoginStatsTxFdiscs_Object = MibTableColumn
alaFipsVlanRnpivLoginStatsTxFdiscs = _AlaFipsVlanRnpivLoginStatsTxFdiscs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 28, 1, 1, 3),
    _AlaFipsVlanRnpivLoginStatsTxFdiscs_Type()
)
alaFipsVlanRnpivLoginStatsTxFdiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanRnpivLoginStatsTxFdiscs.setStatus("current")
_AlaFipsVlanRnpivLoginStatsRxLsAccs_Type = Counter32
_AlaFipsVlanRnpivLoginStatsRxLsAccs_Object = MibTableColumn
alaFipsVlanRnpivLoginStatsRxLsAccs = _AlaFipsVlanRnpivLoginStatsRxLsAccs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 28, 1, 1, 4),
    _AlaFipsVlanRnpivLoginStatsRxLsAccs_Type()
)
alaFipsVlanRnpivLoginStatsRxLsAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanRnpivLoginStatsRxLsAccs.setStatus("current")
_AlaFipsVlanRnpivLoginStatsRxFlogiLsRjts_Type = Counter32
_AlaFipsVlanRnpivLoginStatsRxFlogiLsRjts_Object = MibTableColumn
alaFipsVlanRnpivLoginStatsRxFlogiLsRjts = _AlaFipsVlanRnpivLoginStatsRxFlogiLsRjts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 28, 1, 1, 5),
    _AlaFipsVlanRnpivLoginStatsRxFlogiLsRjts_Type()
)
alaFipsVlanRnpivLoginStatsRxFlogiLsRjts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanRnpivLoginStatsRxFlogiLsRjts.setStatus("current")
_AlaFipsVlanRnpivLoginStatsRxFdiscLsRjts_Type = Counter32
_AlaFipsVlanRnpivLoginStatsRxFdiscLsRjts_Object = MibTableColumn
alaFipsVlanRnpivLoginStatsRxFdiscLsRjts = _AlaFipsVlanRnpivLoginStatsRxFdiscLsRjts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 28, 1, 1, 6),
    _AlaFipsVlanRnpivLoginStatsRxFdiscLsRjts_Type()
)
alaFipsVlanRnpivLoginStatsRxFdiscLsRjts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanRnpivLoginStatsRxFdiscLsRjts.setStatus("current")
_AlaFipsVlanRnpivLoginStatsRxCvls_Type = Counter32
_AlaFipsVlanRnpivLoginStatsRxCvls_Object = MibTableColumn
alaFipsVlanRnpivLoginStatsRxCvls = _AlaFipsVlanRnpivLoginStatsRxCvls_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 28, 1, 1, 7),
    _AlaFipsVlanRnpivLoginStatsRxCvls_Type()
)
alaFipsVlanRnpivLoginStatsRxCvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanRnpivLoginStatsRxCvls.setStatus("current")
_AlaFipsVlanRnpivLoginStatsTxLogos_Type = Counter32
_AlaFipsVlanRnpivLoginStatsTxLogos_Object = MibTableColumn
alaFipsVlanRnpivLoginStatsTxLogos = _AlaFipsVlanRnpivLoginStatsTxLogos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 28, 1, 1, 8),
    _AlaFipsVlanRnpivLoginStatsTxLogos_Type()
)
alaFipsVlanRnpivLoginStatsTxLogos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanRnpivLoginStatsTxLogos.setStatus("current")
_AlaFipsVlanRnpivLoginStatsTxVnkas_Type = Counter32
_AlaFipsVlanRnpivLoginStatsTxVnkas_Object = MibTableColumn
alaFipsVlanRnpivLoginStatsTxVnkas = _AlaFipsVlanRnpivLoginStatsTxVnkas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 28, 1, 1, 9),
    _AlaFipsVlanRnpivLoginStatsTxVnkas_Type()
)
alaFipsVlanRnpivLoginStatsTxVnkas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanRnpivLoginStatsTxVnkas.setStatus("current")
_AlaFipsVlanRnpivLoginStatsTxEkas_Type = Counter32
_AlaFipsVlanRnpivLoginStatsTxEkas_Object = MibTableColumn
alaFipsVlanRnpivLoginStatsTxEkas = _AlaFipsVlanRnpivLoginStatsTxEkas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 28, 1, 1, 10),
    _AlaFipsVlanRnpivLoginStatsTxEkas_Type()
)
alaFipsVlanRnpivLoginStatsTxEkas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsVlanRnpivLoginStatsTxEkas.setStatus("current")
_AlaFipsIntfRnpivLoginStats_ObjectIdentity = ObjectIdentity
alaFipsIntfRnpivLoginStats = _AlaFipsIntfRnpivLoginStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 29)
)
_AlaFipsIntfRnpivLoginStatsTable_Object = MibTable
alaFipsIntfRnpivLoginStatsTable = _AlaFipsIntfRnpivLoginStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 29, 1)
)
if mibBuilder.loadTexts:
    alaFipsIntfRnpivLoginStatsTable.setStatus("current")
_AlaFipsIntfRnpivLoginStatsEntry_Object = MibTableRow
alaFipsIntfRnpivLoginStatsEntry = _AlaFipsIntfRnpivLoginStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 29, 1, 1)
)
alaFipsIntfRnpivLoginStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsIntfRnpivLoginStatsIfIndex"),
)
if mibBuilder.loadTexts:
    alaFipsIntfRnpivLoginStatsEntry.setStatus("current")
_AlaFipsIntfRnpivLoginStatsIfIndex_Type = InterfaceIndex
_AlaFipsIntfRnpivLoginStatsIfIndex_Object = MibTableColumn
alaFipsIntfRnpivLoginStatsIfIndex = _AlaFipsIntfRnpivLoginStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 29, 1, 1, 1),
    _AlaFipsIntfRnpivLoginStatsIfIndex_Type()
)
alaFipsIntfRnpivLoginStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsIntfRnpivLoginStatsIfIndex.setStatus("current")
_AlaFipsIntfRnpivLoginStatsTxFlogis_Type = Counter32
_AlaFipsIntfRnpivLoginStatsTxFlogis_Object = MibTableColumn
alaFipsIntfRnpivLoginStatsTxFlogis = _AlaFipsIntfRnpivLoginStatsTxFlogis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 29, 1, 1, 2),
    _AlaFipsIntfRnpivLoginStatsTxFlogis_Type()
)
alaFipsIntfRnpivLoginStatsTxFlogis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfRnpivLoginStatsTxFlogis.setStatus("current")
_AlaFipsIntfRnpivLoginStatsTxFdiscs_Type = Counter32
_AlaFipsIntfRnpivLoginStatsTxFdiscs_Object = MibTableColumn
alaFipsIntfRnpivLoginStatsTxFdiscs = _AlaFipsIntfRnpivLoginStatsTxFdiscs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 29, 1, 1, 3),
    _AlaFipsIntfRnpivLoginStatsTxFdiscs_Type()
)
alaFipsIntfRnpivLoginStatsTxFdiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfRnpivLoginStatsTxFdiscs.setStatus("current")
_AlaFipsIntfRnpivLoginStatsRxLsAccs_Type = Counter32
_AlaFipsIntfRnpivLoginStatsRxLsAccs_Object = MibTableColumn
alaFipsIntfRnpivLoginStatsRxLsAccs = _AlaFipsIntfRnpivLoginStatsRxLsAccs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 29, 1, 1, 4),
    _AlaFipsIntfRnpivLoginStatsRxLsAccs_Type()
)
alaFipsIntfRnpivLoginStatsRxLsAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfRnpivLoginStatsRxLsAccs.setStatus("current")
_AlaFipsIntfRnpivLoginStatsRxFlogiLsRjts_Type = Counter32
_AlaFipsIntfRnpivLoginStatsRxFlogiLsRjts_Object = MibTableColumn
alaFipsIntfRnpivLoginStatsRxFlogiLsRjts = _AlaFipsIntfRnpivLoginStatsRxFlogiLsRjts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 29, 1, 1, 5),
    _AlaFipsIntfRnpivLoginStatsRxFlogiLsRjts_Type()
)
alaFipsIntfRnpivLoginStatsRxFlogiLsRjts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfRnpivLoginStatsRxFlogiLsRjts.setStatus("current")
_AlaFipsIntfRnpivLoginStatsRxFdiscLsRjts_Type = Counter32
_AlaFipsIntfRnpivLoginStatsRxFdiscLsRjts_Object = MibTableColumn
alaFipsIntfRnpivLoginStatsRxFdiscLsRjts = _AlaFipsIntfRnpivLoginStatsRxFdiscLsRjts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 29, 1, 1, 6),
    _AlaFipsIntfRnpivLoginStatsRxFdiscLsRjts_Type()
)
alaFipsIntfRnpivLoginStatsRxFdiscLsRjts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfRnpivLoginStatsRxFdiscLsRjts.setStatus("current")
_AlaFipsIntfRnpivLoginStatsRxCvls_Type = Counter32
_AlaFipsIntfRnpivLoginStatsRxCvls_Object = MibTableColumn
alaFipsIntfRnpivLoginStatsRxCvls = _AlaFipsIntfRnpivLoginStatsRxCvls_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 29, 1, 1, 7),
    _AlaFipsIntfRnpivLoginStatsRxCvls_Type()
)
alaFipsIntfRnpivLoginStatsRxCvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfRnpivLoginStatsRxCvls.setStatus("current")
_AlaFipsIntfRnpivLoginStatsTxLogos_Type = Counter32
_AlaFipsIntfRnpivLoginStatsTxLogos_Object = MibTableColumn
alaFipsIntfRnpivLoginStatsTxLogos = _AlaFipsIntfRnpivLoginStatsTxLogos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 29, 1, 1, 8),
    _AlaFipsIntfRnpivLoginStatsTxLogos_Type()
)
alaFipsIntfRnpivLoginStatsTxLogos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfRnpivLoginStatsTxLogos.setStatus("current")
_AlaFipsIntfRnpivLoginStatsTxVnkas_Type = Counter32
_AlaFipsIntfRnpivLoginStatsTxVnkas_Object = MibTableColumn
alaFipsIntfRnpivLoginStatsTxVnkas = _AlaFipsIntfRnpivLoginStatsTxVnkas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 29, 1, 1, 9),
    _AlaFipsIntfRnpivLoginStatsTxVnkas_Type()
)
alaFipsIntfRnpivLoginStatsTxVnkas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfRnpivLoginStatsTxVnkas.setStatus("current")
_AlaFipsIntfRnpivLoginStatsTxEkas_Type = Counter32
_AlaFipsIntfRnpivLoginStatsTxEkas_Object = MibTableColumn
alaFipsIntfRnpivLoginStatsTxEkas = _AlaFipsIntfRnpivLoginStatsTxEkas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 29, 1, 1, 10),
    _AlaFipsIntfRnpivLoginStatsTxEkas_Type()
)
alaFipsIntfRnpivLoginStatsTxEkas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsIntfRnpivLoginStatsTxEkas.setStatus("current")
_AlaFipsEtunnelVePortStats_ObjectIdentity = ObjectIdentity
alaFipsEtunnelVePortStats = _AlaFipsEtunnelVePortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 30)
)
_AlaFipsEtunnelVePortStatsTable_Object = MibTable
alaFipsEtunnelVePortStatsTable = _AlaFipsEtunnelVePortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 30, 1)
)
if mibBuilder.loadTexts:
    alaFipsEtunnelVePortStatsTable.setStatus("current")
_AlaFipsEtunnelVePortStatsEntry_Object = MibTableRow
alaFipsEtunnelVePortStatsEntry = _AlaFipsEtunnelVePortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 30, 1, 1)
)
alaFipsEtunnelVePortStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelVePortStatsTunnelId"),
)
if mibBuilder.loadTexts:
    alaFipsEtunnelVePortStatsEntry.setStatus("current")
_AlaFipsEtunnelVePortStatsTunnelId_Type = Unsigned32
_AlaFipsEtunnelVePortStatsTunnelId_Object = MibTableColumn
alaFipsEtunnelVePortStatsTunnelId = _AlaFipsEtunnelVePortStatsTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 30, 1, 1, 1),
    _AlaFipsEtunnelVePortStatsTunnelId_Type()
)
alaFipsEtunnelVePortStatsTunnelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsEtunnelVePortStatsTunnelId.setStatus("current")
_AlaFipsEtunnelVePortStatsRxMdss_Type = Counter32
_AlaFipsEtunnelVePortStatsRxMdss_Object = MibTableColumn
alaFipsEtunnelVePortStatsRxMdss = _AlaFipsEtunnelVePortStatsRxMdss_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 30, 1, 1, 2),
    _AlaFipsEtunnelVePortStatsRxMdss_Type()
)
alaFipsEtunnelVePortStatsRxMdss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelVePortStatsRxMdss.setStatus("current")
_AlaFipsEtunnelVePortStatsRxUdss_Type = Counter32
_AlaFipsEtunnelVePortStatsRxUdss_Object = MibTableColumn
alaFipsEtunnelVePortStatsRxUdss = _AlaFipsEtunnelVePortStatsRxUdss_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 30, 1, 1, 3),
    _AlaFipsEtunnelVePortStatsRxUdss_Type()
)
alaFipsEtunnelVePortStatsRxUdss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelVePortStatsRxUdss.setStatus("current")
_AlaFipsEtunnelVePortStatsRxMdas_Type = Counter32
_AlaFipsEtunnelVePortStatsRxMdas_Object = MibTableColumn
alaFipsEtunnelVePortStatsRxMdas = _AlaFipsEtunnelVePortStatsRxMdas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 30, 1, 1, 4),
    _AlaFipsEtunnelVePortStatsRxMdas_Type()
)
alaFipsEtunnelVePortStatsRxMdas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelVePortStatsRxMdas.setStatus("current")
_AlaFipsEtunnelVePortStatsRxUdas_Type = Counter32
_AlaFipsEtunnelVePortStatsRxUdas_Object = MibTableColumn
alaFipsEtunnelVePortStatsRxUdas = _AlaFipsEtunnelVePortStatsRxUdas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 30, 1, 1, 5),
    _AlaFipsEtunnelVePortStatsRxUdas_Type()
)
alaFipsEtunnelVePortStatsRxUdas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelVePortStatsRxUdas.setStatus("current")
_AlaFipsEtunnelVePortStatsRxElpReqs_Type = Counter32
_AlaFipsEtunnelVePortStatsRxElpReqs_Object = MibTableColumn
alaFipsEtunnelVePortStatsRxElpReqs = _AlaFipsEtunnelVePortStatsRxElpReqs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 30, 1, 1, 6),
    _AlaFipsEtunnelVePortStatsRxElpReqs_Type()
)
alaFipsEtunnelVePortStatsRxElpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelVePortStatsRxElpReqs.setStatus("current")
_AlaFipsEtunnelVePortStatsRxSwAccs_Type = Counter32
_AlaFipsEtunnelVePortStatsRxSwAccs_Object = MibTableColumn
alaFipsEtunnelVePortStatsRxSwAccs = _AlaFipsEtunnelVePortStatsRxSwAccs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 30, 1, 1, 7),
    _AlaFipsEtunnelVePortStatsRxSwAccs_Type()
)
alaFipsEtunnelVePortStatsRxSwAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelVePortStatsRxSwAccs.setStatus("current")
_AlaFipsEtunnelVePortStatsRxSwRjts_Type = Counter32
_AlaFipsEtunnelVePortStatsRxSwRjts_Object = MibTableColumn
alaFipsEtunnelVePortStatsRxSwRjts = _AlaFipsEtunnelVePortStatsRxSwRjts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 30, 1, 1, 8),
    _AlaFipsEtunnelVePortStatsRxSwRjts_Type()
)
alaFipsEtunnelVePortStatsRxSwRjts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelVePortStatsRxSwRjts.setStatus("current")
_AlaFipsEtunnelVePortStatsRxCvls_Type = Counter32
_AlaFipsEtunnelVePortStatsRxCvls_Object = MibTableColumn
alaFipsEtunnelVePortStatsRxCvls = _AlaFipsEtunnelVePortStatsRxCvls_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 30, 1, 1, 9),
    _AlaFipsEtunnelVePortStatsRxCvls_Type()
)
alaFipsEtunnelVePortStatsRxCvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelVePortStatsRxCvls.setStatus("current")
_AlaFipsEtunnelVePortStatsTxMdss_Type = Counter32
_AlaFipsEtunnelVePortStatsTxMdss_Object = MibTableColumn
alaFipsEtunnelVePortStatsTxMdss = _AlaFipsEtunnelVePortStatsTxMdss_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 30, 1, 1, 10),
    _AlaFipsEtunnelVePortStatsTxMdss_Type()
)
alaFipsEtunnelVePortStatsTxMdss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelVePortStatsTxMdss.setStatus("current")
_AlaFipsEtunnelVePortStatsTxUdss_Type = Counter32
_AlaFipsEtunnelVePortStatsTxUdss_Object = MibTableColumn
alaFipsEtunnelVePortStatsTxUdss = _AlaFipsEtunnelVePortStatsTxUdss_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 30, 1, 1, 11),
    _AlaFipsEtunnelVePortStatsTxUdss_Type()
)
alaFipsEtunnelVePortStatsTxUdss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelVePortStatsTxUdss.setStatus("current")
_AlaFipsEtunnelVePortStatsTxMdas_Type = Counter32
_AlaFipsEtunnelVePortStatsTxMdas_Object = MibTableColumn
alaFipsEtunnelVePortStatsTxMdas = _AlaFipsEtunnelVePortStatsTxMdas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 30, 1, 1, 12),
    _AlaFipsEtunnelVePortStatsTxMdas_Type()
)
alaFipsEtunnelVePortStatsTxMdas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelVePortStatsTxMdas.setStatus("current")
_AlaFipsEtunnelVePortStatsTxUdas_Type = Counter32
_AlaFipsEtunnelVePortStatsTxUdas_Object = MibTableColumn
alaFipsEtunnelVePortStatsTxUdas = _AlaFipsEtunnelVePortStatsTxUdas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 30, 1, 1, 13),
    _AlaFipsEtunnelVePortStatsTxUdas_Type()
)
alaFipsEtunnelVePortStatsTxUdas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelVePortStatsTxUdas.setStatus("current")
_AlaFipsEtunnelVePortStatsTxElpReqs_Type = Counter32
_AlaFipsEtunnelVePortStatsTxElpReqs_Object = MibTableColumn
alaFipsEtunnelVePortStatsTxElpReqs = _AlaFipsEtunnelVePortStatsTxElpReqs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 30, 1, 1, 14),
    _AlaFipsEtunnelVePortStatsTxElpReqs_Type()
)
alaFipsEtunnelVePortStatsTxElpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelVePortStatsTxElpReqs.setStatus("current")
_AlaFipsEtunnelVePortStatsTxSwAccs_Type = Counter32
_AlaFipsEtunnelVePortStatsTxSwAccs_Object = MibTableColumn
alaFipsEtunnelVePortStatsTxSwAccs = _AlaFipsEtunnelVePortStatsTxSwAccs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 30, 1, 1, 15),
    _AlaFipsEtunnelVePortStatsTxSwAccs_Type()
)
alaFipsEtunnelVePortStatsTxSwAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelVePortStatsTxSwAccs.setStatus("current")
_AlaFipsEtunnelVePortStatsTxSwRjts_Type = Counter32
_AlaFipsEtunnelVePortStatsTxSwRjts_Object = MibTableColumn
alaFipsEtunnelVePortStatsTxSwRjts = _AlaFipsEtunnelVePortStatsTxSwRjts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 30, 1, 1, 16),
    _AlaFipsEtunnelVePortStatsTxSwRjts_Type()
)
alaFipsEtunnelVePortStatsTxSwRjts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelVePortStatsTxSwRjts.setStatus("current")
_AlaFipsEtunnelVePortStatsTxCvls_Type = Counter32
_AlaFipsEtunnelVePortStatsTxCvls_Object = MibTableColumn
alaFipsEtunnelVePortStatsTxCvls = _AlaFipsEtunnelVePortStatsTxCvls_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 30, 1, 1, 17),
    _AlaFipsEtunnelVePortStatsTxCvls_Type()
)
alaFipsEtunnelVePortStatsTxCvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelVePortStatsTxCvls.setStatus("current")


class _AlaFipsEtunnelVePortStatsClear_Type(Integer32):
    """Custom type alaFipsEtunnelVePortStatsClear based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("none", 2))
    )


_AlaFipsEtunnelVePortStatsClear_Type.__name__ = "Integer32"
_AlaFipsEtunnelVePortStatsClear_Object = MibTableColumn
alaFipsEtunnelVePortStatsClear = _AlaFipsEtunnelVePortStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 30, 1, 1, 18),
    _AlaFipsEtunnelVePortStatsClear_Type()
)
alaFipsEtunnelVePortStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaFipsEtunnelVePortStatsClear.setStatus("current")
_AlaFipsEtunnelTePortStats_ObjectIdentity = ObjectIdentity
alaFipsEtunnelTePortStats = _AlaFipsEtunnelTePortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 31)
)
_AlaFipsEtunnelTePortStatsTable_Object = MibTable
alaFipsEtunnelTePortStatsTable = _AlaFipsEtunnelTePortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 31, 1)
)
if mibBuilder.loadTexts:
    alaFipsEtunnelTePortStatsTable.setStatus("current")
_AlaFipsEtunnelTePortStatsEntry_Object = MibTableRow
alaFipsEtunnelTePortStatsEntry = _AlaFipsEtunnelTePortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 31, 1, 1)
)
alaFipsEtunnelTePortStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelTePortStatsTunnelId"),
)
if mibBuilder.loadTexts:
    alaFipsEtunnelTePortStatsEntry.setStatus("current")
_AlaFipsEtunnelTePortStatsTunnelId_Type = Unsigned32
_AlaFipsEtunnelTePortStatsTunnelId_Object = MibTableColumn
alaFipsEtunnelTePortStatsTunnelId = _AlaFipsEtunnelTePortStatsTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 31, 1, 1, 1),
    _AlaFipsEtunnelTePortStatsTunnelId_Type()
)
alaFipsEtunnelTePortStatsTunnelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsEtunnelTePortStatsTunnelId.setStatus("current")
_AlaFipsEtunnelTePortStatsRxElpReqs_Type = Counter32
_AlaFipsEtunnelTePortStatsRxElpReqs_Object = MibTableColumn
alaFipsEtunnelTePortStatsRxElpReqs = _AlaFipsEtunnelTePortStatsRxElpReqs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 31, 1, 1, 2),
    _AlaFipsEtunnelTePortStatsRxElpReqs_Type()
)
alaFipsEtunnelTePortStatsRxElpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelTePortStatsRxElpReqs.setStatus("current")
_AlaFipsEtunnelTePortStatsRxSwAccs_Type = Counter32
_AlaFipsEtunnelTePortStatsRxSwAccs_Object = MibTableColumn
alaFipsEtunnelTePortStatsRxSwAccs = _AlaFipsEtunnelTePortStatsRxSwAccs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 31, 1, 1, 3),
    _AlaFipsEtunnelTePortStatsRxSwAccs_Type()
)
alaFipsEtunnelTePortStatsRxSwAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelTePortStatsRxSwAccs.setStatus("current")
_AlaFipsEtunnelTePortStatsRxSwRjts_Type = Counter32
_AlaFipsEtunnelTePortStatsRxSwRjts_Object = MibTableColumn
alaFipsEtunnelTePortStatsRxSwRjts = _AlaFipsEtunnelTePortStatsRxSwRjts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 31, 1, 1, 4),
    _AlaFipsEtunnelTePortStatsRxSwRjts_Type()
)
alaFipsEtunnelTePortStatsRxSwRjts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelTePortStatsRxSwRjts.setStatus("current")
_AlaFipsEtunnelTePortStatsTxElpReqs_Type = Counter32
_AlaFipsEtunnelTePortStatsTxElpReqs_Object = MibTableColumn
alaFipsEtunnelTePortStatsTxElpReqs = _AlaFipsEtunnelTePortStatsTxElpReqs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 31, 1, 1, 5),
    _AlaFipsEtunnelTePortStatsTxElpReqs_Type()
)
alaFipsEtunnelTePortStatsTxElpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelTePortStatsTxElpReqs.setStatus("current")
_AlaFipsEtunnelTePortStatsTxSwAccs_Type = Counter32
_AlaFipsEtunnelTePortStatsTxSwAccs_Object = MibTableColumn
alaFipsEtunnelTePortStatsTxSwAccs = _AlaFipsEtunnelTePortStatsTxSwAccs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 31, 1, 1, 6),
    _AlaFipsEtunnelTePortStatsTxSwAccs_Type()
)
alaFipsEtunnelTePortStatsTxSwAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelTePortStatsTxSwAccs.setStatus("current")
_AlaFipsEtunnelTePortStatsTxSwRjts_Type = Counter32
_AlaFipsEtunnelTePortStatsTxSwRjts_Object = MibTableColumn
alaFipsEtunnelTePortStatsTxSwRjts = _AlaFipsEtunnelTePortStatsTxSwRjts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 31, 1, 1, 7),
    _AlaFipsEtunnelTePortStatsTxSwRjts_Type()
)
alaFipsEtunnelTePortStatsTxSwRjts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelTePortStatsTxSwRjts.setStatus("current")


class _AlaFipsEtunnelTePortStatsClear_Type(Integer32):
    """Custom type alaFipsEtunnelTePortStatsClear based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("none", 2))
    )


_AlaFipsEtunnelTePortStatsClear_Type.__name__ = "Integer32"
_AlaFipsEtunnelTePortStatsClear_Object = MibTableColumn
alaFipsEtunnelTePortStatsClear = _AlaFipsEtunnelTePortStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 31, 1, 1, 8),
    _AlaFipsEtunnelTePortStatsClear_Type()
)
alaFipsEtunnelTePortStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaFipsEtunnelTePortStatsClear.setStatus("current")
_AlaFipsVsanVlanMap_ObjectIdentity = ObjectIdentity
alaFipsVsanVlanMap = _AlaFipsVsanVlanMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 32)
)
_AlaFipsVsanVlanMapTable_Object = MibTable
alaFipsVsanVlanMapTable = _AlaFipsVsanVlanMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 32, 1)
)
if mibBuilder.loadTexts:
    alaFipsVsanVlanMapTable.setStatus("current")
_AlaFipsVsanVlanMapEntry_Object = MibTableRow
alaFipsVsanVlanMapEntry = _AlaFipsVsanVlanMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 32, 1, 1)
)
alaFipsVsanVlanMapEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsVsanVlanMapVsanNumber"),
)
if mibBuilder.loadTexts:
    alaFipsVsanVlanMapEntry.setStatus("current")


class _AlaFipsVsanVlanMapVsanNumber_Type(Integer32):
    """Custom type alaFipsVsanVlanMapVsanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaFipsVsanVlanMapVsanNumber_Type.__name__ = "Integer32"
_AlaFipsVsanVlanMapVsanNumber_Object = MibTableColumn
alaFipsVsanVlanMapVsanNumber = _AlaFipsVsanVlanMapVsanNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 32, 1, 1, 1),
    _AlaFipsVsanVlanMapVsanNumber_Type()
)
alaFipsVsanVlanMapVsanNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsVsanVlanMapVsanNumber.setStatus("current")


class _AlaFipsVsanVlanMapVlanNumber_Type(Integer32):
    """Custom type alaFipsVsanVlanMapVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaFipsVsanVlanMapVlanNumber_Type.__name__ = "Integer32"
_AlaFipsVsanVlanMapVlanNumber_Object = MibTableColumn
alaFipsVsanVlanMapVlanNumber = _AlaFipsVsanVlanMapVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 32, 1, 1, 2),
    _AlaFipsVsanVlanMapVlanNumber_Type()
)
alaFipsVsanVlanMapVlanNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFipsVsanVlanMapVlanNumber.setStatus("current")
_AlaFipsVsanVlanMapRowStatus_Type = RowStatus
_AlaFipsVsanVlanMapRowStatus_Object = MibTableColumn
alaFipsVsanVlanMapRowStatus = _AlaFipsVsanVlanMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 32, 1, 1, 3),
    _AlaFipsVsanVlanMapRowStatus_Type()
)
alaFipsVsanVlanMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFipsVsanVlanMapRowStatus.setStatus("current")
_AlaFipsDiscAdvt_ObjectIdentity = ObjectIdentity
alaFipsDiscAdvt = _AlaFipsDiscAdvt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 33)
)
_AlaFipsDiscAdvtTable_Object = MibTable
alaFipsDiscAdvtTable = _AlaFipsDiscAdvtTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 33, 1)
)
if mibBuilder.loadTexts:
    alaFipsDiscAdvtTable.setStatus("current")
_AlaFipsDiscAdvtEntry_Object = MibTableRow
alaFipsDiscAdvtEntry = _AlaFipsDiscAdvtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 33, 1, 1)
)
alaFipsDiscAdvtEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsDiscAdvtVlanId"),
)
if mibBuilder.loadTexts:
    alaFipsDiscAdvtEntry.setStatus("current")


class _AlaFipsDiscAdvtVlanId_Type(Integer32):
    """Custom type alaFipsDiscAdvtVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaFipsDiscAdvtVlanId_Type.__name__ = "Integer32"
_AlaFipsDiscAdvtVlanId_Object = MibTableColumn
alaFipsDiscAdvtVlanId = _AlaFipsDiscAdvtVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 33, 1, 1, 1),
    _AlaFipsDiscAdvtVlanId_Type()
)
alaFipsDiscAdvtVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsDiscAdvtVlanId.setStatus("current")


class _AlaFipsDiscAdvtAbit_Type(Integer32):
    """Custom type alaFipsDiscAdvtAbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AlaFipsDiscAdvtAbit_Type.__name__ = "Integer32"
_AlaFipsDiscAdvtAbit_Object = MibTableColumn
alaFipsDiscAdvtAbit = _AlaFipsDiscAdvtAbit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 33, 1, 1, 2),
    _AlaFipsDiscAdvtAbit_Type()
)
alaFipsDiscAdvtAbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFipsDiscAdvtAbit.setStatus("current")


class _AlaFipsDiscAdvtFkaAdvPeriod_Type(Integer32):
    """Custom type alaFipsDiscAdvtFkaAdvPeriod based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 90),
    )


_AlaFipsDiscAdvtFkaAdvPeriod_Type.__name__ = "Integer32"
_AlaFipsDiscAdvtFkaAdvPeriod_Object = MibTableColumn
alaFipsDiscAdvtFkaAdvPeriod = _AlaFipsDiscAdvtFkaAdvPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 33, 1, 1, 3),
    _AlaFipsDiscAdvtFkaAdvPeriod_Type()
)
alaFipsDiscAdvtFkaAdvPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFipsDiscAdvtFkaAdvPeriod.setStatus("current")


class _AlaFipsDiscAdvtPriority_Type(Unsigned32):
    """Custom type alaFipsDiscAdvtPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaFipsDiscAdvtPriority_Type.__name__ = "Unsigned32"
_AlaFipsDiscAdvtPriority_Object = MibTableColumn
alaFipsDiscAdvtPriority = _AlaFipsDiscAdvtPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 33, 1, 1, 4),
    _AlaFipsDiscAdvtPriority_Type()
)
alaFipsDiscAdvtPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFipsDiscAdvtPriority.setStatus("current")
_AlaFipsDiscAdvtUdsRetries_Type = Unsigned32
_AlaFipsDiscAdvtUdsRetries_Object = MibTableColumn
alaFipsDiscAdvtUdsRetries = _AlaFipsDiscAdvtUdsRetries_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 33, 1, 1, 5),
    _AlaFipsDiscAdvtUdsRetries_Type()
)
alaFipsDiscAdvtUdsRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFipsDiscAdvtUdsRetries.setStatus("current")
_AlaFipsDiscAdvtRowStatus_Type = RowStatus
_AlaFipsDiscAdvtRowStatus_Object = MibTableColumn
alaFipsDiscAdvtRowStatus = _AlaFipsDiscAdvtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 33, 1, 1, 6),
    _AlaFipsDiscAdvtRowStatus_Type()
)
alaFipsDiscAdvtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFipsDiscAdvtRowStatus.setStatus("current")
_AlaFipsEtunnel_ObjectIdentity = ObjectIdentity
alaFipsEtunnel = _AlaFipsEtunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 34)
)
_AlaFipsEtunnelTable_Object = MibTable
alaFipsEtunnelTable = _AlaFipsEtunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 34, 1)
)
if mibBuilder.loadTexts:
    alaFipsEtunnelTable.setStatus("current")
_AlaFipsEtunnelEntry_Object = MibTableRow
alaFipsEtunnelEntry = _AlaFipsEtunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 34, 1, 1)
)
alaFipsEtunnelEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelId"),
)
if mibBuilder.loadTexts:
    alaFipsEtunnelEntry.setStatus("current")
_AlaFipsEtunnelId_Type = Unsigned32
_AlaFipsEtunnelId_Object = MibTableColumn
alaFipsEtunnelId = _AlaFipsEtunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 34, 1, 1, 1),
    _AlaFipsEtunnelId_Type()
)
alaFipsEtunnelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsEtunnelId.setStatus("current")


class _AlaFipsEtunnelVlanId_Type(Integer32):
    """Custom type alaFipsEtunnelVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaFipsEtunnelVlanId_Type.__name__ = "Integer32"
_AlaFipsEtunnelVlanId_Object = MibTableColumn
alaFipsEtunnelVlanId = _AlaFipsEtunnelVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 34, 1, 1, 2),
    _AlaFipsEtunnelVlanId_Type()
)
alaFipsEtunnelVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFipsEtunnelVlanId.setStatus("current")
_AlaFipsEtunnelIfIndexOne_Type = InterfaceIndexOrZero
_AlaFipsEtunnelIfIndexOne_Object = MibTableColumn
alaFipsEtunnelIfIndexOne = _AlaFipsEtunnelIfIndexOne_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 34, 1, 1, 3),
    _AlaFipsEtunnelIfIndexOne_Type()
)
alaFipsEtunnelIfIndexOne.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFipsEtunnelIfIndexOne.setStatus("current")
_AlaFipsEtunnelIfIndexTwo_Type = InterfaceIndexOrZero
_AlaFipsEtunnelIfIndexTwo_Object = MibTableColumn
alaFipsEtunnelIfIndexTwo = _AlaFipsEtunnelIfIndexTwo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 34, 1, 1, 4),
    _AlaFipsEtunnelIfIndexTwo_Type()
)
alaFipsEtunnelIfIndexTwo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFipsEtunnelIfIndexTwo.setStatus("current")
_AlaFipsEtunnelRowStatus_Type = RowStatus
_AlaFipsEtunnelRowStatus_Object = MibTableColumn
alaFipsEtunnelRowStatus = _AlaFipsEtunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 34, 1, 1, 5),
    _AlaFipsEtunnelRowStatus_Type()
)
alaFipsEtunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFipsEtunnelRowStatus.setStatus("current")


class _AlaFipsEtunnelStatsClear_Type(Integer32):
    """Custom type alaFipsEtunnelStatsClear based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("none", 2))
    )


_AlaFipsEtunnelStatsClear_Type.__name__ = "Integer32"
_AlaFipsEtunnelStatsClear_Object = MibTableColumn
alaFipsEtunnelStatsClear = _AlaFipsEtunnelStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 34, 1, 1, 6),
    _AlaFipsEtunnelStatsClear_Type()
)
alaFipsEtunnelStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFipsEtunnelStatsClear.setStatus("current")
_AlaFipsNpivSession_ObjectIdentity = ObjectIdentity
alaFipsNpivSession = _AlaFipsNpivSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 35)
)
_AlaFipsNpivSessionTable_Object = MibTable
alaFipsNpivSessionTable = _AlaFipsNpivSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 35, 1)
)
if mibBuilder.loadTexts:
    alaFipsNpivSessionTable.setStatus("current")
_AlaFipsNpivSessionEntry_Object = MibTableRow
alaFipsNpivSessionEntry = _AlaFipsNpivSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 35, 1, 1)
)
alaFipsNpivSessionEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsNpivSessionEnodeMAC"),
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsNpivSessionVNMAC"),
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsNpivSessionVlanId"),
)
if mibBuilder.loadTexts:
    alaFipsNpivSessionEntry.setStatus("current")
_AlaFipsNpivSessionEnodeMAC_Type = MacAddress
_AlaFipsNpivSessionEnodeMAC_Object = MibTableColumn
alaFipsNpivSessionEnodeMAC = _AlaFipsNpivSessionEnodeMAC_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 35, 1, 1, 1),
    _AlaFipsNpivSessionEnodeMAC_Type()
)
alaFipsNpivSessionEnodeMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsNpivSessionEnodeMAC.setStatus("current")
_AlaFipsNpivSessionVNMAC_Type = MacAddress
_AlaFipsNpivSessionVNMAC_Object = MibTableColumn
alaFipsNpivSessionVNMAC = _AlaFipsNpivSessionVNMAC_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 35, 1, 1, 2),
    _AlaFipsNpivSessionVNMAC_Type()
)
alaFipsNpivSessionVNMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsNpivSessionVNMAC.setStatus("current")


class _AlaFipsNpivSessionVlanId_Type(Integer32):
    """Custom type alaFipsNpivSessionVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaFipsNpivSessionVlanId_Type.__name__ = "Integer32"
_AlaFipsNpivSessionVlanId_Object = MibTableColumn
alaFipsNpivSessionVlanId = _AlaFipsNpivSessionVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 35, 1, 1, 3),
    _AlaFipsNpivSessionVlanId_Type()
)
alaFipsNpivSessionVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsNpivSessionVlanId.setStatus("current")
_AlaFipsNpivSessionInIfIndex_Type = InterfaceIndex
_AlaFipsNpivSessionInIfIndex_Object = MibTableColumn
alaFipsNpivSessionInIfIndex = _AlaFipsNpivSessionInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 35, 1, 1, 4),
    _AlaFipsNpivSessionInIfIndex_Type()
)
alaFipsNpivSessionInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsNpivSessionInIfIndex.setStatus("current")
_AlaFipsNpivSessionOutIfIndex_Type = InterfaceIndex
_AlaFipsNpivSessionOutIfIndex_Object = MibTableColumn
alaFipsNpivSessionOutIfIndex = _AlaFipsNpivSessionOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 35, 1, 1, 5),
    _AlaFipsNpivSessionOutIfIndex_Type()
)
alaFipsNpivSessionOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsNpivSessionOutIfIndex.setStatus("current")


class _AlaFipsNpivSessionFCFMAC_Type(MacAddress):
    """Custom type alaFipsNpivSessionFCFMAC based on MacAddress"""
    defaultHexValue = "000000000000"


_AlaFipsNpivSessionFCFMAC_Object = MibTableColumn
alaFipsNpivSessionFCFMAC = _AlaFipsNpivSessionFCFMAC_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 35, 1, 1, 6),
    _AlaFipsNpivSessionFCFMAC_Type()
)
alaFipsNpivSessionFCFMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFipsNpivSessionFCFMAC.setStatus("current")


class _AlaFipsNpivSessionStatus_Type(Integer32):
    """Custom type alaFipsNpivSessionStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 2),
          ("pending", 1))
    )


_AlaFipsNpivSessionStatus_Type.__name__ = "Integer32"
_AlaFipsNpivSessionStatus_Object = MibTableColumn
alaFipsNpivSessionStatus = _AlaFipsNpivSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 35, 1, 1, 7),
    _AlaFipsNpivSessionStatus_Type()
)
alaFipsNpivSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsNpivSessionStatus.setStatus("current")
_AlaFipsNpivSessionLoginTimeDate_Type = DateAndTime
_AlaFipsNpivSessionLoginTimeDate_Object = MibTableColumn
alaFipsNpivSessionLoginTimeDate = _AlaFipsNpivSessionLoginTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 35, 1, 1, 8),
    _AlaFipsNpivSessionLoginTimeDate_Type()
)
alaFipsNpivSessionLoginTimeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsNpivSessionLoginTimeDate.setStatus("current")
_AlaFipsRnpivSession_ObjectIdentity = ObjectIdentity
alaFipsRnpivSession = _AlaFipsRnpivSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 36)
)
_AlaFipsRnpivSessionTable_Object = MibTable
alaFipsRnpivSessionTable = _AlaFipsRnpivSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 36, 1)
)
if mibBuilder.loadTexts:
    alaFipsRnpivSessionTable.setStatus("current")
_AlaFipsRnpivSessionEntry_Object = MibTableRow
alaFipsRnpivSessionEntry = _AlaFipsRnpivSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 36, 1, 1)
)
alaFipsRnpivSessionEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsRnpivSessionFcid"),
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsRnpivSessionVsanId"),
)
if mibBuilder.loadTexts:
    alaFipsRnpivSessionEntry.setStatus("current")
_AlaFipsRnpivSessionFcid_Type = Fcid
_AlaFipsRnpivSessionFcid_Object = MibTableColumn
alaFipsRnpivSessionFcid = _AlaFipsRnpivSessionFcid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 36, 1, 1, 1),
    _AlaFipsRnpivSessionFcid_Type()
)
alaFipsRnpivSessionFcid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsRnpivSessionFcid.setStatus("current")


class _AlaFipsRnpivSessionVsanId_Type(Integer32):
    """Custom type alaFipsRnpivSessionVsanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaFipsRnpivSessionVsanId_Type.__name__ = "Integer32"
_AlaFipsRnpivSessionVsanId_Object = MibTableColumn
alaFipsRnpivSessionVsanId = _AlaFipsRnpivSessionVsanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 36, 1, 1, 2),
    _AlaFipsRnpivSessionVsanId_Type()
)
alaFipsRnpivSessionVsanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsRnpivSessionVsanId.setStatus("current")
_AlaFipsRnpivSessionVNMAC_Type = MacAddress
_AlaFipsRnpivSessionVNMAC_Object = MibTableColumn
alaFipsRnpivSessionVNMAC = _AlaFipsRnpivSessionVNMAC_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 36, 1, 1, 3),
    _AlaFipsRnpivSessionVNMAC_Type()
)
alaFipsRnpivSessionVNMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsRnpivSessionVNMAC.setStatus("current")


class _AlaFipsRnpivSessionVlanId_Type(Integer32):
    """Custom type alaFipsRnpivSessionVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaFipsRnpivSessionVlanId_Type.__name__ = "Integer32"
_AlaFipsRnpivSessionVlanId_Object = MibTableColumn
alaFipsRnpivSessionVlanId = _AlaFipsRnpivSessionVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 36, 1, 1, 4),
    _AlaFipsRnpivSessionVlanId_Type()
)
alaFipsRnpivSessionVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsRnpivSessionVlanId.setStatus("current")
_AlaFipsRnpivSessionInIfIndex_Type = InterfaceIndex
_AlaFipsRnpivSessionInIfIndex_Object = MibTableColumn
alaFipsRnpivSessionInIfIndex = _AlaFipsRnpivSessionInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 36, 1, 1, 5),
    _AlaFipsRnpivSessionInIfIndex_Type()
)
alaFipsRnpivSessionInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsRnpivSessionInIfIndex.setStatus("current")
_AlaFipsRnpivSessionOutIfIndex_Type = InterfaceIndex
_AlaFipsRnpivSessionOutIfIndex_Object = MibTableColumn
alaFipsRnpivSessionOutIfIndex = _AlaFipsRnpivSessionOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 36, 1, 1, 6),
    _AlaFipsRnpivSessionOutIfIndex_Type()
)
alaFipsRnpivSessionOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsRnpivSessionOutIfIndex.setStatus("current")


class _AlaFipsRnpivSessionFCFMAC_Type(MacAddress):
    """Custom type alaFipsRnpivSessionFCFMAC based on MacAddress"""
    defaultHexValue = "000000000000"


_AlaFipsRnpivSessionFCFMAC_Object = MibTableColumn
alaFipsRnpivSessionFCFMAC = _AlaFipsRnpivSessionFCFMAC_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 36, 1, 1, 7),
    _AlaFipsRnpivSessionFCFMAC_Type()
)
alaFipsRnpivSessionFCFMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsRnpivSessionFCFMAC.setStatus("current")


class _AlaFipsRnpivSessionStatus_Type(Integer32):
    """Custom type alaFipsRnpivSessionStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 2),
          ("pending", 1))
    )


_AlaFipsRnpivSessionStatus_Type.__name__ = "Integer32"
_AlaFipsRnpivSessionStatus_Object = MibTableColumn
alaFipsRnpivSessionStatus = _AlaFipsRnpivSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 36, 1, 1, 8),
    _AlaFipsRnpivSessionStatus_Type()
)
alaFipsRnpivSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsRnpivSessionStatus.setStatus("current")
_AlaFipsRnpivSessionLoginTimeDate_Type = DateAndTime
_AlaFipsRnpivSessionLoginTimeDate_Object = MibTableColumn
alaFipsRnpivSessionLoginTimeDate = _AlaFipsRnpivSessionLoginTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 36, 1, 1, 9),
    _AlaFipsRnpivSessionLoginTimeDate_Type()
)
alaFipsRnpivSessionLoginTimeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsRnpivSessionLoginTimeDate.setStatus("current")
_AlaFipsEtunnelSession_ObjectIdentity = ObjectIdentity
alaFipsEtunnelSession = _AlaFipsEtunnelSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 37)
)
_AlaFipsEtunnelSessionTable_Object = MibTable
alaFipsEtunnelSessionTable = _AlaFipsEtunnelSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 37, 1)
)
if mibBuilder.loadTexts:
    alaFipsEtunnelSessionTable.setStatus("current")
_AlaFipsEtunnelSessionEntry_Object = MibTableRow
alaFipsEtunnelSessionEntry = _AlaFipsEtunnelSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 37, 1, 1)
)
alaFipsEtunnelSessionEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelSessionTunnelId"),
)
if mibBuilder.loadTexts:
    alaFipsEtunnelSessionEntry.setStatus("current")
_AlaFipsEtunnelSessionTunnelId_Type = Unsigned32
_AlaFipsEtunnelSessionTunnelId_Object = MibTableColumn
alaFipsEtunnelSessionTunnelId = _AlaFipsEtunnelSessionTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 37, 1, 1, 1),
    _AlaFipsEtunnelSessionTunnelId_Type()
)
alaFipsEtunnelSessionTunnelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFipsEtunnelSessionTunnelId.setStatus("current")


class _AlaFipsEtunnelSessionVlanId_Type(Integer32):
    """Custom type alaFipsEtunnelSessionVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaFipsEtunnelSessionVlanId_Type.__name__ = "Integer32"
_AlaFipsEtunnelSessionVlanId_Object = MibTableColumn
alaFipsEtunnelSessionVlanId = _AlaFipsEtunnelSessionVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 37, 1, 1, 2),
    _AlaFipsEtunnelSessionVlanId_Type()
)
alaFipsEtunnelSessionVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelSessionVlanId.setStatus("current")
_AlaFipsEtunnelSessionInIfIndex_Type = InterfaceIndex
_AlaFipsEtunnelSessionInIfIndex_Object = MibTableColumn
alaFipsEtunnelSessionInIfIndex = _AlaFipsEtunnelSessionInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 37, 1, 1, 3),
    _AlaFipsEtunnelSessionInIfIndex_Type()
)
alaFipsEtunnelSessionInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelSessionInIfIndex.setStatus("current")
_AlaFipsEtunnelSessionOutIfIndex_Type = InterfaceIndex
_AlaFipsEtunnelSessionOutIfIndex_Object = MibTableColumn
alaFipsEtunnelSessionOutIfIndex = _AlaFipsEtunnelSessionOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 37, 1, 1, 4),
    _AlaFipsEtunnelSessionOutIfIndex_Type()
)
alaFipsEtunnelSessionOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelSessionOutIfIndex.setStatus("current")


class _AlaFipsEtunnelSessionFCFMAC_Type(MacAddress):
    """Custom type alaFipsEtunnelSessionFCFMAC based on MacAddress"""
    defaultHexValue = "000000000000"


_AlaFipsEtunnelSessionFCFMAC_Object = MibTableColumn
alaFipsEtunnelSessionFCFMAC = _AlaFipsEtunnelSessionFCFMAC_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 37, 1, 1, 5),
    _AlaFipsEtunnelSessionFCFMAC_Type()
)
alaFipsEtunnelSessionFCFMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaFipsEtunnelSessionFCFMAC.setStatus("current")


class _AlaFipsEtunnelSessionStatus_Type(Integer32):
    """Custom type alaFipsEtunnelSessionStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 2),
          ("pending", 1))
    )


_AlaFipsEtunnelSessionStatus_Type.__name__ = "Integer32"
_AlaFipsEtunnelSessionStatus_Object = MibTableColumn
alaFipsEtunnelSessionStatus = _AlaFipsEtunnelSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 37, 1, 1, 6),
    _AlaFipsEtunnelSessionStatus_Type()
)
alaFipsEtunnelSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelSessionStatus.setStatus("current")
_AlaFipsEtunnelSessionLoginTimeDate_Type = DateAndTime
_AlaFipsEtunnelSessionLoginTimeDate_Object = MibTableColumn
alaFipsEtunnelSessionLoginTimeDate = _AlaFipsEtunnelSessionLoginTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 37, 1, 1, 7),
    _AlaFipsEtunnelSessionLoginTimeDate_Type()
)
alaFipsEtunnelSessionLoginTimeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelSessionLoginTimeDate.setStatus("current")


class _AlaFipsEtunnelSessionPairMode_Type(Integer32):
    """Custom type alaFipsEtunnelSessionPairMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("te-to-te", 2),
          ("teToVe", 1))
    )


_AlaFipsEtunnelSessionPairMode_Type.__name__ = "Integer32"
_AlaFipsEtunnelSessionPairMode_Object = MibTableColumn
alaFipsEtunnelSessionPairMode = _AlaFipsEtunnelSessionPairMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 37, 1, 1, 8),
    _AlaFipsEtunnelSessionPairMode_Type()
)
alaFipsEtunnelSessionPairMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFipsEtunnelSessionPairMode.setStatus("current")
_AlaFcNpivLoadBalSess_ObjectIdentity = ObjectIdentity
alaFcNpivLoadBalSess = _AlaFcNpivLoadBalSess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 38)
)
_AlaFcNpivLoadBalSessTable_Object = MibTable
alaFcNpivLoadBalSessTable = _AlaFcNpivLoadBalSessTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 38, 1)
)
if mibBuilder.loadTexts:
    alaFcNpivLoadBalSessTable.setStatus("current")
_AlaFcNpivLoadBalSessEntry_Object = MibTableRow
alaFcNpivLoadBalSessEntry = _AlaFcNpivLoadBalSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 38, 1, 1)
)
alaFcNpivLoadBalSessEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFcNpivLoadBalSessIfIndex"),
)
if mibBuilder.loadTexts:
    alaFcNpivLoadBalSessEntry.setStatus("current")
_AlaFcNpivLoadBalSessIfIndex_Type = InterfaceIndex
_AlaFcNpivLoadBalSessIfIndex_Object = MibTableColumn
alaFcNpivLoadBalSessIfIndex = _AlaFcNpivLoadBalSessIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 38, 1, 1, 1),
    _AlaFcNpivLoadBalSessIfIndex_Type()
)
alaFcNpivLoadBalSessIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFcNpivLoadBalSessIfIndex.setStatus("current")
_AlaFcNpivLoadBalSessCount_Type = Unsigned32
_AlaFcNpivLoadBalSessCount_Object = MibTableColumn
alaFcNpivLoadBalSessCount = _AlaFcNpivLoadBalSessCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 38, 1, 1, 2),
    _AlaFcNpivLoadBalSessCount_Type()
)
alaFcNpivLoadBalSessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcNpivLoadBalSessCount.setStatus("current")
_AlaFcIntfEtunnelStats_ObjectIdentity = ObjectIdentity
alaFcIntfEtunnelStats = _AlaFcIntfEtunnelStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 39)
)
_AlaFcIntfEtunnelStatsTable_Object = MibTable
alaFcIntfEtunnelStatsTable = _AlaFcIntfEtunnelStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 39, 1)
)
if mibBuilder.loadTexts:
    alaFcIntfEtunnelStatsTable.setStatus("current")
_AlaFcIntfEtunnelStatsEntry_Object = MibTableRow
alaFcIntfEtunnelStatsEntry = _AlaFcIntfEtunnelStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 39, 1, 1)
)
alaFcIntfEtunnelStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-FIPS-MIB", "alaFcIntfEtunnelStatsIfIndex"),
)
if mibBuilder.loadTexts:
    alaFcIntfEtunnelStatsEntry.setStatus("current")
_AlaFcIntfEtunnelStatsIfIndex_Type = InterfaceIndex
_AlaFcIntfEtunnelStatsIfIndex_Object = MibTableColumn
alaFcIntfEtunnelStatsIfIndex = _AlaFcIntfEtunnelStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 39, 1, 1, 1),
    _AlaFcIntfEtunnelStatsIfIndex_Type()
)
alaFcIntfEtunnelStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaFcIntfEtunnelStatsIfIndex.setStatus("current")
_AlaFcIntfEtunnelStatsTunnelId_Type = Unsigned32
_AlaFcIntfEtunnelStatsTunnelId_Object = MibTableColumn
alaFcIntfEtunnelStatsTunnelId = _AlaFcIntfEtunnelStatsTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 39, 1, 1, 2),
    _AlaFcIntfEtunnelStatsTunnelId_Type()
)
alaFcIntfEtunnelStatsTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfEtunnelStatsTunnelId.setStatus("current")
_AlaFcIntfEtunnelStatsRxElpReqs_Type = Counter32
_AlaFcIntfEtunnelStatsRxElpReqs_Object = MibTableColumn
alaFcIntfEtunnelStatsRxElpReqs = _AlaFcIntfEtunnelStatsRxElpReqs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 39, 1, 1, 3),
    _AlaFcIntfEtunnelStatsRxElpReqs_Type()
)
alaFcIntfEtunnelStatsRxElpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfEtunnelStatsRxElpReqs.setStatus("current")
_AlaFcIntfEtunnelStatsRxSwAccs_Type = Counter32
_AlaFcIntfEtunnelStatsRxSwAccs_Object = MibTableColumn
alaFcIntfEtunnelStatsRxSwAccs = _AlaFcIntfEtunnelStatsRxSwAccs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 39, 1, 1, 4),
    _AlaFcIntfEtunnelStatsRxSwAccs_Type()
)
alaFcIntfEtunnelStatsRxSwAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfEtunnelStatsRxSwAccs.setStatus("current")
_AlaFcIntfEtunnelStatsRxSwRjts_Type = Counter32
_AlaFcIntfEtunnelStatsRxSwRjts_Object = MibTableColumn
alaFcIntfEtunnelStatsRxSwRjts = _AlaFcIntfEtunnelStatsRxSwRjts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 39, 1, 1, 5),
    _AlaFcIntfEtunnelStatsRxSwRjts_Type()
)
alaFcIntfEtunnelStatsRxSwRjts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfEtunnelStatsRxSwRjts.setStatus("current")
_AlaFcIntfEtunnelStatsTxElpReqs_Type = Counter32
_AlaFcIntfEtunnelStatsTxElpReqs_Object = MibTableColumn
alaFcIntfEtunnelStatsTxElpReqs = _AlaFcIntfEtunnelStatsTxElpReqs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 39, 1, 1, 6),
    _AlaFcIntfEtunnelStatsTxElpReqs_Type()
)
alaFcIntfEtunnelStatsTxElpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfEtunnelStatsTxElpReqs.setStatus("current")
_AlaFcIntfEtunnelStatsTxSwAccs_Type = Counter32
_AlaFcIntfEtunnelStatsTxSwAccs_Object = MibTableColumn
alaFcIntfEtunnelStatsTxSwAccs = _AlaFcIntfEtunnelStatsTxSwAccs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 39, 1, 1, 7),
    _AlaFcIntfEtunnelStatsTxSwAccs_Type()
)
alaFcIntfEtunnelStatsTxSwAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfEtunnelStatsTxSwAccs.setStatus("current")
_AlaFcIntfEtunnelStatsTxSwRjts_Type = Counter32
_AlaFcIntfEtunnelStatsTxSwRjts_Object = MibTableColumn
alaFcIntfEtunnelStatsTxSwRjts = _AlaFcIntfEtunnelStatsTxSwRjts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 1, 39, 1, 1, 8),
    _AlaFcIntfEtunnelStatsTxSwRjts_Type()
)
alaFcIntfEtunnelStatsTxSwRjts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaFcIntfEtunnelStatsTxSwRjts.setStatus("current")
_AlcatelIND1FipsMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1FipsMIBConformance = _AlcatelIND1FipsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1FipsMIBConformance.setStatus("current")
_AlcatelIND1FipsMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1FipsMIBGroups = _AlcatelIND1FipsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1FipsMIBGroups.setStatus("current")
_AlcatelIND1FipsMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1FipsMIBCompliances = _AlcatelIND1FipsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1FipsMIBCompliances.setStatus("current")

# Managed Objects groups

alaFipsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 1)
)
alaFipsInfoGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFipsConfigFilterResourceLimit"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsConfigFIPSAdmin"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsConfigAddressMode"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsConfigPriorityOne"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsConfigPriorityTwo"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsTotalNumFilterResource"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsUsedNumFilterResource"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsConfigStatsClear"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsConfigPrioProtection"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsConfigPriorityProtectionAction"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsConfigPriorityProtectionRemarkVal"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsConfigHouseKeepingTimePeriod"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsConfigSWReinsertStatus"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsConfigSessClear"))
)
if mibBuilder.loadTexts:
    alaFipsInfoGroup.setStatus("current")

alaFipsVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 2)
)
alaFipsVlanGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanFCMap"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanStatsClear"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanStatsFnreClear"))
)
if mibBuilder.loadTexts:
    alaFipsVlanGroup.setStatus("current")

alaFipsVlanEnodeStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 3)
)
alaFipsVlanEnodeStatsGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanEnodeStatsSessions"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanEnodeStatsMds"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanEnodeStatsUds"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanEnodeStatsFlogi"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanEnodeStatsFdisc"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanEnodeStatsLogo"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanEnodeStatsEka"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanEnodeStatsVnka"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanEnodeStatsClear"))
)
if mibBuilder.loadTexts:
    alaFipsVlanEnodeStatsGroup.setStatus("current")

alaFipsVlanFcfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 4)
)
alaFipsVlanFcfStatsGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanFcfStatsSessions"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanFcfStatsMda"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanFcfStatsUda"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanFcfStatsFlogiAcc"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanFcfStatsFlogiRjt"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanFcfStatsFdiscRjt"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanFcfStatsLogoAcc"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanFcfStatsLogoRjt"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanFcfStatsCvl"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanFcfStatsClear"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanFcfStatsFdiscAcc"))
)
if mibBuilder.loadTexts:
    alaFipsVlanFcfStatsGroup.setStatus("current")

alaFipsIntfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 5)
)
alaFipsIntfGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfOperStatus"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfPortRole"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfRowStatus"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfStatsClear"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfStatsFnreClear"))
)
if mibBuilder.loadTexts:
    alaFipsIntfGroup.setStatus("current")

alaFipsIntfEnodeStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 6)
)
alaFipsIntfEnodeStatsGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfEnodeStatsSessions"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfEnodeStatsMds"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfEnodeStatsUds"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfEnodeStatsFlogi"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfEnodeStatsFdisc"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfEnodeStatsLogo"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfEnodeStatsEka"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfEnodeStatsVnka"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfEnodeStatsClear"))
)
if mibBuilder.loadTexts:
    alaFipsIntfEnodeStatsGroup.setStatus("current")

alaFipsIntfFcfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 7)
)
alaFipsIntfFcfStatsGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfFcfStatsSessions"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfFcfStatsMda"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfFcfStatsUda"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfFcfStatsFlogiAcc"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfFcfStatsFlogiRjt"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfFcfStatsFdiscRjt"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfFcfStatsLogoAcc"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfFcfStatsLogoRjt"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfFcfStatsCvl"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfFcfStatsClear"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfFcfStatsFdiscAcc"))
)
if mibBuilder.loadTexts:
    alaFipsIntfFcfStatsGroup.setStatus("current")

alaFipsFcfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 8)
)
alaFipsFcfGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFipsFcfIntf"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsFcfSessions"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsFcfConfigType"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsFcfRowStatus"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsFcfAvailForLogin"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsFcfMaxFcoeFrmSizeVerified"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsFcfPriority"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsFcfType"))
)
if mibBuilder.loadTexts:
    alaFipsFcfGroup.setStatus("current")

alaFipsSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 9)
)
alaFipsSessionGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFipsSessionIfIndex"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsSessionFCFMAC"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsSessionStatus"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsSessionLoginTime"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsSessionLoginTimeDate"))
)
if mibBuilder.loadTexts:
    alaFipsSessionGroup.setStatus("current")

alaFipsNotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 10)
)
alaFipsNotificationObjectGroup.setObjects(
    ("ALCATEL-IND1-FIPS-MIB", "alaFipsFilterResourceUsage")
)
if mibBuilder.loadTexts:
    alaFipsNotificationObjectGroup.setStatus("current")

alaFcVsanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 12)
)
alaFcVsanGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFcVsanDescription"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcVsanAdmStatus"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcVsanOperStatus"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcVsanRowStatus"))
)
if mibBuilder.loadTexts:
    alaFcVsanGroup.setStatus("current")

alaFcVfpaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 13)
)
alaFcVfpaGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFcVfpaState"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcVfpaRowStatus"))
)
if mibBuilder.loadTexts:
    alaFcVfpaGroup.setStatus("current")

alaFcIntfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 14)
)
alaFcIntfGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFcIntfOperStatus"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfMode"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfBbScN"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfClassOfService"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfFcid"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfWwpn"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfLoginState"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfRowStatus"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfStatsClear"))
)
if mibBuilder.loadTexts:
    alaFcIntfGroup.setStatus("current")

alaFcNpivStaticLoadBalanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 15)
)
alaFcNpivStaticLoadBalanceGroup.setObjects(
    ("ALCATEL-IND1-FIPS-MIB", "alaFcNpivStaticLoadBalanceRowStatus")
)
if mibBuilder.loadTexts:
    alaFcNpivStaticLoadBalanceGroup.setStatus("current")

alaFcNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 16)
)
alaFcNodeGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFcNodeVsanNumber"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcNodeVlanNumber"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcNodeFcid"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcNodeWwnn"))
)
if mibBuilder.loadTexts:
    alaFcNodeGroup.setStatus("current")

alaFcSessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 17)
)
alaFcSessGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFcSessVsanNumber"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcSessStatus"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcSessIntfMode"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcSessFcid"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcSessType"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcSessTunnelId"))
)
if mibBuilder.loadTexts:
    alaFcSessGroup.setStatus("current")

alaFcIntfNpivStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 18)
)
alaFcIntfNpivStatsGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFcIntfNpivStatsTxFlogis"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfNpivStatsTxFdiscs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfNpivStatsRxLsAccs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfNpivStatsRxFlogos"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfNpivStatsRxFlogiLsRjts"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfNpivStatsRxFdiscLsRjts"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfNpivStatsTxFlogos"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfNpivStatsClear"))
)
if mibBuilder.loadTexts:
    alaFcIntfNpivStatsGroup.setStatus("current")

alaFcVsanNpivStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 19)
)
alaFcVsanNpivStatsGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFcVsanNpivStatsTxFlogis"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcVsanNpivStatsTxFdiscs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcVsanNpivStatsRxLsAccs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcVsanNpivStatsRxFlogos"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcVsanNpivStatsRxFlogiLsRjts"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcVsanNpivStatsRxFdiscLsRjts"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcVsanNpivStatsTxFlogos"))
)
if mibBuilder.loadTexts:
    alaFcVsanNpivStatsGroup.setStatus("current")

alaFcIntfRnpivStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 20)
)
alaFcIntfRnpivStatsGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFcIntfRnpivStatsRxFlogis"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfRnpivStatsRxFdiscs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfRnpivStatsTxFlogiLsAccs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfRnpivStatsTxFdiscLsAccs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfRnpivStatsTxFlogos"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfRnpivStatsTxFlogiLsRjts"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfRnpivStatsTxFdiscLsRjts"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfRnpivStatsRxFlogos"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfRnpivStatsClear"))
)
if mibBuilder.loadTexts:
    alaFcIntfRnpivStatsGroup.setStatus("current")

alaFcVsanRnpivStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 21)
)
alaFcVsanRnpivStatsGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFcVsanRnpivStatsRxFlogis"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcVsanRnpivStatsRxFdiscs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcVsanRnpivStatsTxFlogiLsAccs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcVsanRnpivStatsTxFdiscLsAccs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcVsanRnpivStatsTxFlogos"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcVsanRnpivStatsTxFlogiLsRjts"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcVsanRnpivStatsTxFdiscLsRjts"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcVsanRnpivStatsRxFlogos"))
)
if mibBuilder.loadTexts:
    alaFcVsanRnpivStatsGroup.setStatus("current")

alaFcInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 22)
)
alaFcInfoGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFcConfigSessClear"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcConfigStatsClear"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcConfigNpivLoadBalance"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcConfigWwnn"))
)
if mibBuilder.loadTexts:
    alaFcInfoGroup.setStatus("current")

alaFipsVlanNpivDiscStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 23)
)
alaFipsVlanNpivDiscStatsGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanNpivDiscStatsRxVlanDiscRqs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanNpivDiscStatsTxVlanDiscResps"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanNpivDiscStatsRxMdss"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanNpivDiscStatsRxUdss"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanNpivDiscStatsTxMdas"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanNpivDiscStatsTxUdas"))
)
if mibBuilder.loadTexts:
    alaFipsVlanNpivDiscStatsGroup.setStatus("current")

alaFipsIntfNpivDiscStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 24)
)
alaFipsIntfNpivDiscStatsGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfNpivDiscStatsRxVlanDiscRqs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfNpivDiscStatsTxVlanDiscResps"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfNpivDiscStatsRxMdss"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfNpivDiscStatsRxUdss"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfNpivDiscStatsTxMdas"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfNpivDiscStatsTxUdas"))
)
if mibBuilder.loadTexts:
    alaFipsIntfNpivDiscStatsGroup.setStatus("current")

alaFipsVlanNpivLoginStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 25)
)
alaFipsVlanNpivLoginStatsGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanNpivLoginStatsRxFlogis"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanNpivLoginStatsRxFdiscs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanNpivLoginStatsTxFlogiAccs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanNpivLoginStatsTxFlogiLsRjts"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanNpivLoginStatsTxFdiscLsRjts"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanNpivLoginStatsRxLogos"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanNpivLoginStatsTxCvls"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanNpivLoginStatsRxEkas"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanNpivLoginStatsRxVnkas"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanNpivLoginStatsTxFDiscAccs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanNpivLoginStatsTxFlogoAccs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanNpivLoginStatsTxFLogoLsRjts"))
)
if mibBuilder.loadTexts:
    alaFipsVlanNpivLoginStatsGroup.setStatus("current")

alaFipsIntfNpivLoginStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 26)
)
alaFipsIntfNpivLoginStatsGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfNpivLoginStatsRxFlogis"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfNpivLoginStatsRxFdiscs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfNpivLoginStatsTxFlogiAccs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfNpivLoginStatsTxFlogiLsRjts"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfNpivLoginStatsTxFdiscLsRjts"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfNpivLoginStatsRxLogos"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfNpivLoginStatsTxCvls"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfNpivLoginStatsRxEkas"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfNpivLoginStatsRxVnkas"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfNpivLoginStatsTxFDiscAccs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfNpivLoginStatsTxFlogoAccs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfNpivLoginStatsTxFLogoLsRjts"))
)
if mibBuilder.loadTexts:
    alaFipsIntfNpivLoginStatsGroup.setStatus("current")

alaFipsVlanRnpivDiscStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 27)
)
alaFipsVlanRnpivDiscStatsGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanRnpivDiscStatsRxMdas"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanRnpivDiscStatsRxUdas"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanRnpivDiscStatsTxMdss"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanRnpivDiscStatsTxUdss"))
)
if mibBuilder.loadTexts:
    alaFipsVlanRnpivDiscStatsGroup.setStatus("current")

alaFipsIntfRnpivDiscStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 28)
)
alaFipsIntfRnpivDiscStatsGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfRnpivDiscStatsRxMdas"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfRnpivDiscStatsRxUdas"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfRnpivDiscStatsTxMdss"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfRnpivDiscStatsTxUdss"))
)
if mibBuilder.loadTexts:
    alaFipsIntfRnpivDiscStatsGroup.setStatus("current")

alaFipsVlanRnpivLoginStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 29)
)
alaFipsVlanRnpivLoginStatsGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanRnpivLoginStatsTxFlogis"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanRnpivLoginStatsTxFdiscs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanRnpivLoginStatsRxLsAccs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanRnpivLoginStatsRxFlogiLsRjts"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanRnpivLoginStatsRxFdiscLsRjts"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanRnpivLoginStatsRxCvls"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanRnpivLoginStatsTxLogos"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanRnpivLoginStatsTxVnkas"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVlanRnpivLoginStatsTxEkas"))
)
if mibBuilder.loadTexts:
    alaFipsVlanRnpivLoginStatsGroup.setStatus("current")

alaFipsIntfRnpivLoginStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 30)
)
alaFipsIntfRnpivLoginStatsGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfRnpivLoginStatsTxFlogis"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfRnpivLoginStatsTxFdiscs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfRnpivLoginStatsRxLsAccs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfRnpivLoginStatsRxFlogiLsRjts"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfRnpivLoginStatsRxFdiscLsRjts"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfRnpivLoginStatsRxCvls"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfRnpivLoginStatsTxLogos"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfRnpivLoginStatsTxVnkas"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsIntfRnpivLoginStatsTxEkas"))
)
if mibBuilder.loadTexts:
    alaFipsIntfRnpivLoginStatsGroup.setStatus("current")

alaFipsEtunnelVePortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 31)
)
alaFipsEtunnelVePortStatsGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelVePortStatsRxMdss"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelVePortStatsRxUdss"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelVePortStatsRxMdas"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelVePortStatsRxUdas"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelVePortStatsRxElpReqs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelVePortStatsRxSwAccs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelVePortStatsRxSwRjts"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelVePortStatsRxCvls"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelVePortStatsTxMdss"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelVePortStatsTxUdss"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelVePortStatsTxMdas"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelVePortStatsTxUdas"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelVePortStatsTxElpReqs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelVePortStatsTxSwAccs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelVePortStatsTxSwRjts"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelVePortStatsTxCvls"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelVePortStatsClear"))
)
if mibBuilder.loadTexts:
    alaFipsEtunnelVePortStatsGroup.setStatus("current")

alaFipsEtunnelTePortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 32)
)
alaFipsEtunnelTePortStatsGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelTePortStatsRxElpReqs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelTePortStatsRxSwAccs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelTePortStatsRxSwRjts"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelTePortStatsTxElpReqs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelTePortStatsTxSwAccs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelTePortStatsTxSwRjts"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelTePortStatsClear"))
)
if mibBuilder.loadTexts:
    alaFipsEtunnelTePortStatsGroup.setStatus("current")

alaFipsVsanVlanMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 33)
)
alaFipsVsanVlanMapGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFipsVsanVlanMapVlanNumber"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsVsanVlanMapRowStatus"))
)
if mibBuilder.loadTexts:
    alaFipsVsanVlanMapGroup.setStatus("current")

alaFipsDiscAdvtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 34)
)
alaFipsDiscAdvtGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFipsDiscAdvtAbit"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsDiscAdvtFkaAdvPeriod"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsDiscAdvtPriority"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsDiscAdvtUdsRetries"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsDiscAdvtRowStatus"))
)
if mibBuilder.loadTexts:
    alaFipsDiscAdvtGroup.setStatus("current")

alaFipsEtunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 35)
)
alaFipsEtunnelGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelVlanId"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelIfIndexOne"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelIfIndexTwo"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelRowStatus"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelStatsClear"))
)
if mibBuilder.loadTexts:
    alaFipsEtunnelGroup.setStatus("current")

alaFipsNpivSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 36)
)
alaFipsNpivSessionGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFipsNpivSessionInIfIndex"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsNpivSessionOutIfIndex"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsNpivSessionFCFMAC"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsNpivSessionStatus"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsNpivSessionLoginTimeDate"))
)
if mibBuilder.loadTexts:
    alaFipsNpivSessionGroup.setStatus("current")

alaFipsRnpivSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 37)
)
alaFipsRnpivSessionGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFipsRnpivSessionVNMAC"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsRnpivSessionVlanId"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsRnpivSessionInIfIndex"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsRnpivSessionOutIfIndex"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsRnpivSessionFCFMAC"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsRnpivSessionStatus"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsRnpivSessionLoginTimeDate"))
)
if mibBuilder.loadTexts:
    alaFipsRnpivSessionGroup.setStatus("current")

alaFipsEtunnelSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 38)
)
alaFipsEtunnelSessionGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelSessionVlanId"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelSessionInIfIndex"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelSessionOutIfIndex"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelSessionFCFMAC"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelSessionStatus"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelSessionLoginTimeDate"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFipsEtunnelSessionPairMode"))
)
if mibBuilder.loadTexts:
    alaFipsEtunnelSessionGroup.setStatus("current")

alaFcNpivLoadBalSessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 39)
)
alaFcNpivLoadBalSessGroup.setObjects(
    ("ALCATEL-IND1-FIPS-MIB", "alaFcNpivLoadBalSessCount")
)
if mibBuilder.loadTexts:
    alaFcNpivLoadBalSessGroup.setStatus("current")

alaFcIntfEtunnelStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 40)
)
alaFcIntfEtunnelStatsGroup.setObjects(
      *(("ALCATEL-IND1-FIPS-MIB", "alaFcIntfEtunnelStatsTunnelId"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfEtunnelStatsRxElpReqs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfEtunnelStatsRxSwAccs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfEtunnelStatsRxSwRjts"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfEtunnelStatsTxElpReqs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfEtunnelStatsTxSwAccs"),
        ("ALCATEL-IND1-FIPS-MIB", "alaFcIntfEtunnelStatsTxSwRjts"))
)
if mibBuilder.loadTexts:
    alaFcIntfEtunnelStatsGroup.setStatus("current")


# Notification objects

alaFipsResourceThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 0, 1)
)
alaFipsResourceThresholdReached.setObjects(
    ("ALCATEL-IND1-FIPS-MIB", "alaFipsFilterResourceUsage")
)
if mibBuilder.loadTexts:
    alaFipsResourceThresholdReached.setStatus(
        "current"
    )


# Notifications groups

alaFipsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 1, 11)
)
alaFipsNotificationGroup.setObjects(
    ("ALCATEL-IND1-FIPS-MIB", "alaFipsResourceThresholdReached")
)
if mibBuilder.loadTexts:
    alaFipsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1FipsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1FipsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-FIPS-MIB",
    **{"FipsFCMAP": FipsFCMAP,
       "Fcid": Fcid,
       "Wwpn": Wwpn,
       "Wwnn": Wwnn,
       "alcatelIND1FipsMIB": alcatelIND1FipsMIB,
       "alcatelIND1FipsMIBNotifications": alcatelIND1FipsMIBNotifications,
       "alaFipsResourceThresholdReached": alaFipsResourceThresholdReached,
       "alcatelIND1FipsMIBObjects": alcatelIND1FipsMIBObjects,
       "alaFipsInfo": alaFipsInfo,
       "alaFipsConfigFilterResourceLimit": alaFipsConfigFilterResourceLimit,
       "alaFipsConfigFIPSAdmin": alaFipsConfigFIPSAdmin,
       "alaFipsConfigAddressMode": alaFipsConfigAddressMode,
       "alaFipsConfigPriorityOne": alaFipsConfigPriorityOne,
       "alaFipsConfigPriorityTwo": alaFipsConfigPriorityTwo,
       "alaFipsTotalNumFilterResource": alaFipsTotalNumFilterResource,
       "alaFipsUsedNumFilterResource": alaFipsUsedNumFilterResource,
       "alaFipsConfigStatsClear": alaFipsConfigStatsClear,
       "alaFipsConfigPrioProtection": alaFipsConfigPrioProtection,
       "alaFipsConfigPriorityProtectionAction": alaFipsConfigPriorityProtectionAction,
       "alaFipsConfigPriorityProtectionRemarkVal": alaFipsConfigPriorityProtectionRemarkVal,
       "alaFipsConfigHouseKeepingTimePeriod": alaFipsConfigHouseKeepingTimePeriod,
       "alaFipsConfigSWReinsertStatus": alaFipsConfigSWReinsertStatus,
       "alaFipsConfigSessClear": alaFipsConfigSessClear,
       "alaFipsVlan": alaFipsVlan,
       "alaFipsVlanTable": alaFipsVlanTable,
       "alaFipsVlanEntry": alaFipsVlanEntry,
       "alaFipsVlanId": alaFipsVlanId,
       "alaFipsVlanFCMap": alaFipsVlanFCMap,
       "alaFipsVlanStatsClear": alaFipsVlanStatsClear,
       "alaFipsVlanStatsFnreClear": alaFipsVlanStatsFnreClear,
       "alaFipsVlanEnodeStats": alaFipsVlanEnodeStats,
       "alaFipsVlanEnodeStatsTable": alaFipsVlanEnodeStatsTable,
       "alaFipsVlanEnodeStatsEntry": alaFipsVlanEnodeStatsEntry,
       "alaFipsVlanEnodeStatsVlanId": alaFipsVlanEnodeStatsVlanId,
       "alaFipsVlanEnodeStatsSessions": alaFipsVlanEnodeStatsSessions,
       "alaFipsVlanEnodeStatsMds": alaFipsVlanEnodeStatsMds,
       "alaFipsVlanEnodeStatsUds": alaFipsVlanEnodeStatsUds,
       "alaFipsVlanEnodeStatsFlogi": alaFipsVlanEnodeStatsFlogi,
       "alaFipsVlanEnodeStatsFdisc": alaFipsVlanEnodeStatsFdisc,
       "alaFipsVlanEnodeStatsLogo": alaFipsVlanEnodeStatsLogo,
       "alaFipsVlanEnodeStatsEka": alaFipsVlanEnodeStatsEka,
       "alaFipsVlanEnodeStatsVnka": alaFipsVlanEnodeStatsVnka,
       "alaFipsVlanEnodeStatsClear": alaFipsVlanEnodeStatsClear,
       "alaFipsVlanFcfStats": alaFipsVlanFcfStats,
       "alaFipsVlanFcfStatsTable": alaFipsVlanFcfStatsTable,
       "alaFipsVlanFcfStatsEntry": alaFipsVlanFcfStatsEntry,
       "alaFipsVlanFcfStatsVlanId": alaFipsVlanFcfStatsVlanId,
       "alaFipsVlanFcfStatsSessions": alaFipsVlanFcfStatsSessions,
       "alaFipsVlanFcfStatsMda": alaFipsVlanFcfStatsMda,
       "alaFipsVlanFcfStatsUda": alaFipsVlanFcfStatsUda,
       "alaFipsVlanFcfStatsFlogiAcc": alaFipsVlanFcfStatsFlogiAcc,
       "alaFipsVlanFcfStatsFlogiRjt": alaFipsVlanFcfStatsFlogiRjt,
       "alaFipsVlanFcfStatsFdiscRjt": alaFipsVlanFcfStatsFdiscRjt,
       "alaFipsVlanFcfStatsLogoAcc": alaFipsVlanFcfStatsLogoAcc,
       "alaFipsVlanFcfStatsLogoRjt": alaFipsVlanFcfStatsLogoRjt,
       "alaFipsVlanFcfStatsCvl": alaFipsVlanFcfStatsCvl,
       "alaFipsVlanFcfStatsClear": alaFipsVlanFcfStatsClear,
       "alaFipsVlanFcfStatsFdiscAcc": alaFipsVlanFcfStatsFdiscAcc,
       "alaFipsIntf": alaFipsIntf,
       "alaFipsIntfTable": alaFipsIntfTable,
       "alaFipsIntfEntry": alaFipsIntfEntry,
       "alaFipsIntfIfIndex": alaFipsIntfIfIndex,
       "alaFipsIntfOperStatus": alaFipsIntfOperStatus,
       "alaFipsIntfPortRole": alaFipsIntfPortRole,
       "alaFipsIntfRowStatus": alaFipsIntfRowStatus,
       "alaFipsIntfStatsClear": alaFipsIntfStatsClear,
       "alaFipsIntfStatsFnreClear": alaFipsIntfStatsFnreClear,
       "alaFipsIntfEnodeStats": alaFipsIntfEnodeStats,
       "alaFipsIntfEnodeStatsTable": alaFipsIntfEnodeStatsTable,
       "alaFipsIntfEnodeStatsEntry": alaFipsIntfEnodeStatsEntry,
       "alaFipsIntfEnodeStatsIfIndex": alaFipsIntfEnodeStatsIfIndex,
       "alaFipsIntfEnodeStatsSessions": alaFipsIntfEnodeStatsSessions,
       "alaFipsIntfEnodeStatsMds": alaFipsIntfEnodeStatsMds,
       "alaFipsIntfEnodeStatsUds": alaFipsIntfEnodeStatsUds,
       "alaFipsIntfEnodeStatsFlogi": alaFipsIntfEnodeStatsFlogi,
       "alaFipsIntfEnodeStatsFdisc": alaFipsIntfEnodeStatsFdisc,
       "alaFipsIntfEnodeStatsLogo": alaFipsIntfEnodeStatsLogo,
       "alaFipsIntfEnodeStatsEka": alaFipsIntfEnodeStatsEka,
       "alaFipsIntfEnodeStatsVnka": alaFipsIntfEnodeStatsVnka,
       "alaFipsIntfEnodeStatsClear": alaFipsIntfEnodeStatsClear,
       "alaFipsIntfFcfStats": alaFipsIntfFcfStats,
       "alaFipsIntfFcfStatsTable": alaFipsIntfFcfStatsTable,
       "alaFipsIntfFcfStatsEntry": alaFipsIntfFcfStatsEntry,
       "alaFipsIntfFcfStatsIfIndex": alaFipsIntfFcfStatsIfIndex,
       "alaFipsIntfFcfStatsSessions": alaFipsIntfFcfStatsSessions,
       "alaFipsIntfFcfStatsMda": alaFipsIntfFcfStatsMda,
       "alaFipsIntfFcfStatsUda": alaFipsIntfFcfStatsUda,
       "alaFipsIntfFcfStatsFlogiAcc": alaFipsIntfFcfStatsFlogiAcc,
       "alaFipsIntfFcfStatsFdiscRjt": alaFipsIntfFcfStatsFdiscRjt,
       "alaFipsIntfFcfStatsFlogiRjt": alaFipsIntfFcfStatsFlogiRjt,
       "alaFipsIntfFcfStatsLogoAcc": alaFipsIntfFcfStatsLogoAcc,
       "alaFipsIntfFcfStatsLogoRjt": alaFipsIntfFcfStatsLogoRjt,
       "alaFipsIntfFcfStatsCvl": alaFipsIntfFcfStatsCvl,
       "alaFipsIntfFcfStatsClear": alaFipsIntfFcfStatsClear,
       "alaFipsIntfFcfStatsFdiscAcc": alaFipsIntfFcfStatsFdiscAcc,
       "alaFipsFcf": alaFipsFcf,
       "alaFipsFcfTable": alaFipsFcfTable,
       "alaFipsFcfEntry": alaFipsFcfEntry,
       "alaFipsFcfMAC": alaFipsFcfMAC,
       "alaFipsFcfVlan": alaFipsFcfVlan,
       "alaFipsFcfIntf": alaFipsFcfIntf,
       "alaFipsFcfSessions": alaFipsFcfSessions,
       "alaFipsFcfConfigType": alaFipsFcfConfigType,
       "alaFipsFcfRowStatus": alaFipsFcfRowStatus,
       "alaFipsFcfAvailForLogin": alaFipsFcfAvailForLogin,
       "alaFipsFcfMaxFcoeFrmSizeVerified": alaFipsFcfMaxFcoeFrmSizeVerified,
       "alaFipsFcfPriority": alaFipsFcfPriority,
       "alaFipsFcfType": alaFipsFcfType,
       "alaFipsSession": alaFipsSession,
       "alaFipsSessionTable": alaFipsSessionTable,
       "alaFipsSessionEntry": alaFipsSessionEntry,
       "alaFipsSessionEnodeMAC": alaFipsSessionEnodeMAC,
       "alaFipsSessionVNMAC": alaFipsSessionVNMAC,
       "alaFipsSessionVlanId": alaFipsSessionVlanId,
       "alaFipsSessionIfIndex": alaFipsSessionIfIndex,
       "alaFipsSessionFCFMAC": alaFipsSessionFCFMAC,
       "alaFipsSessionStatus": alaFipsSessionStatus,
       "alaFipsSessionLoginTime": alaFipsSessionLoginTime,
       "alaFipsSessionLoginTimeDate": alaFipsSessionLoginTimeDate,
       "alaFipsNotificationObj": alaFipsNotificationObj,
       "alaFipsFilterResourceUsage": alaFipsFilterResourceUsage,
       "alaFcVsan": alaFcVsan,
       "alaFcVsanTable": alaFcVsanTable,
       "alaFcVsanEntry": alaFcVsanEntry,
       "alaFcVsanNumber": alaFcVsanNumber,
       "alaFcVsanDescription": alaFcVsanDescription,
       "alaFcVsanAdmStatus": alaFcVsanAdmStatus,
       "alaFcVsanOperStatus": alaFcVsanOperStatus,
       "alaFcVsanRowStatus": alaFcVsanRowStatus,
       "alaFcVfpa": alaFcVfpa,
       "alaFcVfpaTable": alaFcVfpaTable,
       "alaFcVfpaEntry": alaFcVfpaEntry,
       "alaFcVfpaVsanNumber": alaFcVfpaVsanNumber,
       "alaFcVfpaIfIndex": alaFcVfpaIfIndex,
       "alaFcVfpaState": alaFcVfpaState,
       "alaFcVfpaRowStatus": alaFcVfpaRowStatus,
       "alaFcIntf": alaFcIntf,
       "alaFcIntfTable": alaFcIntfTable,
       "alaFcIntfEntry": alaFcIntfEntry,
       "alaFcIntfIfIndex": alaFcIntfIfIndex,
       "alaFcIntfOperStatus": alaFcIntfOperStatus,
       "alaFcIntfMode": alaFcIntfMode,
       "alaFcIntfBbScN": alaFcIntfBbScN,
       "alaFcIntfClassOfService": alaFcIntfClassOfService,
       "alaFcIntfFcid": alaFcIntfFcid,
       "alaFcIntfWwpn": alaFcIntfWwpn,
       "alaFcIntfLoginState": alaFcIntfLoginState,
       "alaFcIntfRowStatus": alaFcIntfRowStatus,
       "alaFcIntfStatsClear": alaFcIntfStatsClear,
       "alaFcNpivStaticLoadBalance": alaFcNpivStaticLoadBalance,
       "alaFcNpivStaticLoadBalanceTable": alaFcNpivStaticLoadBalanceTable,
       "alaFcNpivStaticLoadBalanceEntry": alaFcNpivStaticLoadBalanceEntry,
       "alaFcNpivStaticLoadBalanceFcIfIndex": alaFcNpivStaticLoadBalanceFcIfIndex,
       "alaFcNpivStaticLoadBalanceEthIfIndex": alaFcNpivStaticLoadBalanceEthIfIndex,
       "alaFcNpivStaticLoadBalanceRowStatus": alaFcNpivStaticLoadBalanceRowStatus,
       "alaFcNode": alaFcNode,
       "alaFcNodeTable": alaFcNodeTable,
       "alaFcNodeEntry": alaFcNodeEntry,
       "alaFcNodeIfIndex": alaFcNodeIfIndex,
       "alaFcNodeWwpn": alaFcNodeWwpn,
       "alaFcNodeVsanNumber": alaFcNodeVsanNumber,
       "alaFcNodeVlanNumber": alaFcNodeVlanNumber,
       "alaFcNodeFcid": alaFcNodeFcid,
       "alaFcNodeWwnn": alaFcNodeWwnn,
       "alaFcSess": alaFcSess,
       "alaFcSessTable": alaFcSessTable,
       "alaFcSessEntry": alaFcSessEntry,
       "alaFcSessIfIndex": alaFcSessIfIndex,
       "alaFcSessWwpn": alaFcSessWwpn,
       "alaFcSessVsanNumber": alaFcSessVsanNumber,
       "alaFcSessStatus": alaFcSessStatus,
       "alaFcSessIntfMode": alaFcSessIntfMode,
       "alaFcSessFcid": alaFcSessFcid,
       "alaFcSessType": alaFcSessType,
       "alaFcSessTunnelId": alaFcSessTunnelId,
       "alaFcIntfNpivStats": alaFcIntfNpivStats,
       "alaFcIntfNpivStatsTable": alaFcIntfNpivStatsTable,
       "alaFcIntfNpivStatsEntry": alaFcIntfNpivStatsEntry,
       "alaFcIntfNpivStatsIfIndex": alaFcIntfNpivStatsIfIndex,
       "alaFcIntfNpivStatsTxFlogis": alaFcIntfNpivStatsTxFlogis,
       "alaFcIntfNpivStatsTxFdiscs": alaFcIntfNpivStatsTxFdiscs,
       "alaFcIntfNpivStatsRxLsAccs": alaFcIntfNpivStatsRxLsAccs,
       "alaFcIntfNpivStatsRxFlogos": alaFcIntfNpivStatsRxFlogos,
       "alaFcIntfNpivStatsRxFlogiLsRjts": alaFcIntfNpivStatsRxFlogiLsRjts,
       "alaFcIntfNpivStatsRxFdiscLsRjts": alaFcIntfNpivStatsRxFdiscLsRjts,
       "alaFcIntfNpivStatsTxFlogos": alaFcIntfNpivStatsTxFlogos,
       "alaFcIntfNpivStatsClear": alaFcIntfNpivStatsClear,
       "alaFcVsanNpivStats": alaFcVsanNpivStats,
       "alaFcVsanNpivStatsTable": alaFcVsanNpivStatsTable,
       "alaFcVsanNpivStatsEntry": alaFcVsanNpivStatsEntry,
       "alaFcVsanNpivStatsVsan": alaFcVsanNpivStatsVsan,
       "alaFcVsanNpivStatsTxFlogis": alaFcVsanNpivStatsTxFlogis,
       "alaFcVsanNpivStatsTxFdiscs": alaFcVsanNpivStatsTxFdiscs,
       "alaFcVsanNpivStatsRxLsAccs": alaFcVsanNpivStatsRxLsAccs,
       "alaFcVsanNpivStatsRxFlogos": alaFcVsanNpivStatsRxFlogos,
       "alaFcVsanNpivStatsRxFlogiLsRjts": alaFcVsanNpivStatsRxFlogiLsRjts,
       "alaFcVsanNpivStatsRxFdiscLsRjts": alaFcVsanNpivStatsRxFdiscLsRjts,
       "alaFcVsanNpivStatsTxFlogos": alaFcVsanNpivStatsTxFlogos,
       "alaFcIntfRnpivStats": alaFcIntfRnpivStats,
       "alaFcIntfRnpivStatsTable": alaFcIntfRnpivStatsTable,
       "alaFcIntfRnpivStatsEntry": alaFcIntfRnpivStatsEntry,
       "alaFcIntfRnpivStatsIfIndex": alaFcIntfRnpivStatsIfIndex,
       "alaFcIntfRnpivStatsRxFlogis": alaFcIntfRnpivStatsRxFlogis,
       "alaFcIntfRnpivStatsRxFdiscs": alaFcIntfRnpivStatsRxFdiscs,
       "alaFcIntfRnpivStatsTxFlogiLsAccs": alaFcIntfRnpivStatsTxFlogiLsAccs,
       "alaFcIntfRnpivStatsTxFdiscLsAccs": alaFcIntfRnpivStatsTxFdiscLsAccs,
       "alaFcIntfRnpivStatsTxFlogos": alaFcIntfRnpivStatsTxFlogos,
       "alaFcIntfRnpivStatsTxFlogiLsRjts": alaFcIntfRnpivStatsTxFlogiLsRjts,
       "alaFcIntfRnpivStatsTxFdiscLsRjts": alaFcIntfRnpivStatsTxFdiscLsRjts,
       "alaFcIntfRnpivStatsRxFlogos": alaFcIntfRnpivStatsRxFlogos,
       "alaFcIntfRnpivStatsClear": alaFcIntfRnpivStatsClear,
       "alaFcVsanRnpivStats": alaFcVsanRnpivStats,
       "alaFcVsanRnpivStatsTable": alaFcVsanRnpivStatsTable,
       "alaFcVsanRnpivStatsEntry": alaFcVsanRnpivStatsEntry,
       "alaFcVsanRnpivStatsVsan": alaFcVsanRnpivStatsVsan,
       "alaFcVsanRnpivStatsRxFlogis": alaFcVsanRnpivStatsRxFlogis,
       "alaFcVsanRnpivStatsRxFdiscs": alaFcVsanRnpivStatsRxFdiscs,
       "alaFcVsanRnpivStatsTxFlogiLsAccs": alaFcVsanRnpivStatsTxFlogiLsAccs,
       "alaFcVsanRnpivStatsTxFdiscLsAccs": alaFcVsanRnpivStatsTxFdiscLsAccs,
       "alaFcVsanRnpivStatsTxFlogos": alaFcVsanRnpivStatsTxFlogos,
       "alaFcVsanRnpivStatsTxFlogiLsRjts": alaFcVsanRnpivStatsTxFlogiLsRjts,
       "alaFcVsanRnpivStatsTxFdiscLsRjts": alaFcVsanRnpivStatsTxFdiscLsRjts,
       "alaFcVsanRnpivStatsRxFlogos": alaFcVsanRnpivStatsRxFlogos,
       "alaFcInfo": alaFcInfo,
       "alaFcConfigSessClear": alaFcConfigSessClear,
       "alaFcConfigStatsClear": alaFcConfigStatsClear,
       "alaFcConfigNpivLoadBalance": alaFcConfigNpivLoadBalance,
       "alaFcConfigWwnn": alaFcConfigWwnn,
       "alaFipsVlanNpivDiscStats": alaFipsVlanNpivDiscStats,
       "alaFipsVlanNpivDiscStatsTable": alaFipsVlanNpivDiscStatsTable,
       "alaFipsVlanNpivDiscStatsEntry": alaFipsVlanNpivDiscStatsEntry,
       "alaFipsVlanNpivDiscStatsVlanId": alaFipsVlanNpivDiscStatsVlanId,
       "alaFipsVlanNpivDiscStatsRxVlanDiscRqs": alaFipsVlanNpivDiscStatsRxVlanDiscRqs,
       "alaFipsVlanNpivDiscStatsTxVlanDiscResps": alaFipsVlanNpivDiscStatsTxVlanDiscResps,
       "alaFipsVlanNpivDiscStatsRxMdss": alaFipsVlanNpivDiscStatsRxMdss,
       "alaFipsVlanNpivDiscStatsRxUdss": alaFipsVlanNpivDiscStatsRxUdss,
       "alaFipsVlanNpivDiscStatsTxMdas": alaFipsVlanNpivDiscStatsTxMdas,
       "alaFipsVlanNpivDiscStatsTxUdas": alaFipsVlanNpivDiscStatsTxUdas,
       "alaFipsIntfNpivDiscStats": alaFipsIntfNpivDiscStats,
       "alaFipsIntfNpivDiscStatsTable": alaFipsIntfNpivDiscStatsTable,
       "alaFipsIntfNpivDiscStatsEntry": alaFipsIntfNpivDiscStatsEntry,
       "alaFipsIntfNpivDiscStatsIfIndex": alaFipsIntfNpivDiscStatsIfIndex,
       "alaFipsIntfNpivDiscStatsRxVlanDiscRqs": alaFipsIntfNpivDiscStatsRxVlanDiscRqs,
       "alaFipsIntfNpivDiscStatsTxVlanDiscResps": alaFipsIntfNpivDiscStatsTxVlanDiscResps,
       "alaFipsIntfNpivDiscStatsRxMdss": alaFipsIntfNpivDiscStatsRxMdss,
       "alaFipsIntfNpivDiscStatsRxUdss": alaFipsIntfNpivDiscStatsRxUdss,
       "alaFipsIntfNpivDiscStatsTxMdas": alaFipsIntfNpivDiscStatsTxMdas,
       "alaFipsIntfNpivDiscStatsTxUdas": alaFipsIntfNpivDiscStatsTxUdas,
       "alaFipsVlanNpivLoginStats": alaFipsVlanNpivLoginStats,
       "alaFipsVlanNpivLoginStatsTable": alaFipsVlanNpivLoginStatsTable,
       "alaFipsVlanNpivLoginStatsEntry": alaFipsVlanNpivLoginStatsEntry,
       "alaFipsVlanNpivLoginStatsVlanId": alaFipsVlanNpivLoginStatsVlanId,
       "alaFipsVlanNpivLoginStatsRxFlogis": alaFipsVlanNpivLoginStatsRxFlogis,
       "alaFipsVlanNpivLoginStatsRxFdiscs": alaFipsVlanNpivLoginStatsRxFdiscs,
       "alaFipsVlanNpivLoginStatsTxFlogiAccs": alaFipsVlanNpivLoginStatsTxFlogiAccs,
       "alaFipsVlanNpivLoginStatsTxFlogiLsRjts": alaFipsVlanNpivLoginStatsTxFlogiLsRjts,
       "alaFipsVlanNpivLoginStatsTxFdiscLsRjts": alaFipsVlanNpivLoginStatsTxFdiscLsRjts,
       "alaFipsVlanNpivLoginStatsRxLogos": alaFipsVlanNpivLoginStatsRxLogos,
       "alaFipsVlanNpivLoginStatsTxCvls": alaFipsVlanNpivLoginStatsTxCvls,
       "alaFipsVlanNpivLoginStatsRxEkas": alaFipsVlanNpivLoginStatsRxEkas,
       "alaFipsVlanNpivLoginStatsRxVnkas": alaFipsVlanNpivLoginStatsRxVnkas,
       "alaFipsVlanNpivLoginStatsTxFDiscAccs": alaFipsVlanNpivLoginStatsTxFDiscAccs,
       "alaFipsVlanNpivLoginStatsTxFlogoAccs": alaFipsVlanNpivLoginStatsTxFlogoAccs,
       "alaFipsVlanNpivLoginStatsTxFLogoLsRjts": alaFipsVlanNpivLoginStatsTxFLogoLsRjts,
       "alaFipsIntfNpivLoginStats": alaFipsIntfNpivLoginStats,
       "alaFipsIntfNpivLoginStatsTable": alaFipsIntfNpivLoginStatsTable,
       "alaFipsIntfNpivLoginStatsEntry": alaFipsIntfNpivLoginStatsEntry,
       "alaFipsIntfNpivLoginStatsIfIndex": alaFipsIntfNpivLoginStatsIfIndex,
       "alaFipsIntfNpivLoginStatsRxFlogis": alaFipsIntfNpivLoginStatsRxFlogis,
       "alaFipsIntfNpivLoginStatsRxFdiscs": alaFipsIntfNpivLoginStatsRxFdiscs,
       "alaFipsIntfNpivLoginStatsTxFlogiAccs": alaFipsIntfNpivLoginStatsTxFlogiAccs,
       "alaFipsIntfNpivLoginStatsTxFlogiLsRjts": alaFipsIntfNpivLoginStatsTxFlogiLsRjts,
       "alaFipsIntfNpivLoginStatsTxFdiscLsRjts": alaFipsIntfNpivLoginStatsTxFdiscLsRjts,
       "alaFipsIntfNpivLoginStatsRxLogos": alaFipsIntfNpivLoginStatsRxLogos,
       "alaFipsIntfNpivLoginStatsTxCvls": alaFipsIntfNpivLoginStatsTxCvls,
       "alaFipsIntfNpivLoginStatsRxEkas": alaFipsIntfNpivLoginStatsRxEkas,
       "alaFipsIntfNpivLoginStatsRxVnkas": alaFipsIntfNpivLoginStatsRxVnkas,
       "alaFipsIntfNpivLoginStatsTxFDiscAccs": alaFipsIntfNpivLoginStatsTxFDiscAccs,
       "alaFipsIntfNpivLoginStatsTxFlogoAccs": alaFipsIntfNpivLoginStatsTxFlogoAccs,
       "alaFipsIntfNpivLoginStatsTxFLogoLsRjts": alaFipsIntfNpivLoginStatsTxFLogoLsRjts,
       "alaFipsVlanRnpivDiscStats": alaFipsVlanRnpivDiscStats,
       "alaFipsVlanRnpivDiscStatsTable": alaFipsVlanRnpivDiscStatsTable,
       "alaFipsVlanRnpivDiscStatsEntry": alaFipsVlanRnpivDiscStatsEntry,
       "alaFipsVlanRnpivDiscStatsVlanId": alaFipsVlanRnpivDiscStatsVlanId,
       "alaFipsVlanRnpivDiscStatsRxMdas": alaFipsVlanRnpivDiscStatsRxMdas,
       "alaFipsVlanRnpivDiscStatsRxUdas": alaFipsVlanRnpivDiscStatsRxUdas,
       "alaFipsVlanRnpivDiscStatsTxMdss": alaFipsVlanRnpivDiscStatsTxMdss,
       "alaFipsVlanRnpivDiscStatsTxUdss": alaFipsVlanRnpivDiscStatsTxUdss,
       "alaFipsIntfRnpivDiscStats": alaFipsIntfRnpivDiscStats,
       "alaFipsIntfRnpivDiscStatsTable": alaFipsIntfRnpivDiscStatsTable,
       "alaFipsIntfRnpivDiscStatsEntry": alaFipsIntfRnpivDiscStatsEntry,
       "alaFipsIntfRnpivDiscStatsIfIndex": alaFipsIntfRnpivDiscStatsIfIndex,
       "alaFipsIntfRnpivDiscStatsRxMdas": alaFipsIntfRnpivDiscStatsRxMdas,
       "alaFipsIntfRnpivDiscStatsRxUdas": alaFipsIntfRnpivDiscStatsRxUdas,
       "alaFipsIntfRnpivDiscStatsTxMdss": alaFipsIntfRnpivDiscStatsTxMdss,
       "alaFipsIntfRnpivDiscStatsTxUdss": alaFipsIntfRnpivDiscStatsTxUdss,
       "alaFipsVlanRnpivLoginStats": alaFipsVlanRnpivLoginStats,
       "alaFipsVlanRnpivLoginStatsTable": alaFipsVlanRnpivLoginStatsTable,
       "alaFipsVlanRnpivLoginStatsEntry": alaFipsVlanRnpivLoginStatsEntry,
       "alaFipsVlanRnpivLoginStatsVlanId": alaFipsVlanRnpivLoginStatsVlanId,
       "alaFipsVlanRnpivLoginStatsTxFlogis": alaFipsVlanRnpivLoginStatsTxFlogis,
       "alaFipsVlanRnpivLoginStatsTxFdiscs": alaFipsVlanRnpivLoginStatsTxFdiscs,
       "alaFipsVlanRnpivLoginStatsRxLsAccs": alaFipsVlanRnpivLoginStatsRxLsAccs,
       "alaFipsVlanRnpivLoginStatsRxFlogiLsRjts": alaFipsVlanRnpivLoginStatsRxFlogiLsRjts,
       "alaFipsVlanRnpivLoginStatsRxFdiscLsRjts": alaFipsVlanRnpivLoginStatsRxFdiscLsRjts,
       "alaFipsVlanRnpivLoginStatsRxCvls": alaFipsVlanRnpivLoginStatsRxCvls,
       "alaFipsVlanRnpivLoginStatsTxLogos": alaFipsVlanRnpivLoginStatsTxLogos,
       "alaFipsVlanRnpivLoginStatsTxVnkas": alaFipsVlanRnpivLoginStatsTxVnkas,
       "alaFipsVlanRnpivLoginStatsTxEkas": alaFipsVlanRnpivLoginStatsTxEkas,
       "alaFipsIntfRnpivLoginStats": alaFipsIntfRnpivLoginStats,
       "alaFipsIntfRnpivLoginStatsTable": alaFipsIntfRnpivLoginStatsTable,
       "alaFipsIntfRnpivLoginStatsEntry": alaFipsIntfRnpivLoginStatsEntry,
       "alaFipsIntfRnpivLoginStatsIfIndex": alaFipsIntfRnpivLoginStatsIfIndex,
       "alaFipsIntfRnpivLoginStatsTxFlogis": alaFipsIntfRnpivLoginStatsTxFlogis,
       "alaFipsIntfRnpivLoginStatsTxFdiscs": alaFipsIntfRnpivLoginStatsTxFdiscs,
       "alaFipsIntfRnpivLoginStatsRxLsAccs": alaFipsIntfRnpivLoginStatsRxLsAccs,
       "alaFipsIntfRnpivLoginStatsRxFlogiLsRjts": alaFipsIntfRnpivLoginStatsRxFlogiLsRjts,
       "alaFipsIntfRnpivLoginStatsRxFdiscLsRjts": alaFipsIntfRnpivLoginStatsRxFdiscLsRjts,
       "alaFipsIntfRnpivLoginStatsRxCvls": alaFipsIntfRnpivLoginStatsRxCvls,
       "alaFipsIntfRnpivLoginStatsTxLogos": alaFipsIntfRnpivLoginStatsTxLogos,
       "alaFipsIntfRnpivLoginStatsTxVnkas": alaFipsIntfRnpivLoginStatsTxVnkas,
       "alaFipsIntfRnpivLoginStatsTxEkas": alaFipsIntfRnpivLoginStatsTxEkas,
       "alaFipsEtunnelVePortStats": alaFipsEtunnelVePortStats,
       "alaFipsEtunnelVePortStatsTable": alaFipsEtunnelVePortStatsTable,
       "alaFipsEtunnelVePortStatsEntry": alaFipsEtunnelVePortStatsEntry,
       "alaFipsEtunnelVePortStatsTunnelId": alaFipsEtunnelVePortStatsTunnelId,
       "alaFipsEtunnelVePortStatsRxMdss": alaFipsEtunnelVePortStatsRxMdss,
       "alaFipsEtunnelVePortStatsRxUdss": alaFipsEtunnelVePortStatsRxUdss,
       "alaFipsEtunnelVePortStatsRxMdas": alaFipsEtunnelVePortStatsRxMdas,
       "alaFipsEtunnelVePortStatsRxUdas": alaFipsEtunnelVePortStatsRxUdas,
       "alaFipsEtunnelVePortStatsRxElpReqs": alaFipsEtunnelVePortStatsRxElpReqs,
       "alaFipsEtunnelVePortStatsRxSwAccs": alaFipsEtunnelVePortStatsRxSwAccs,
       "alaFipsEtunnelVePortStatsRxSwRjts": alaFipsEtunnelVePortStatsRxSwRjts,
       "alaFipsEtunnelVePortStatsRxCvls": alaFipsEtunnelVePortStatsRxCvls,
       "alaFipsEtunnelVePortStatsTxMdss": alaFipsEtunnelVePortStatsTxMdss,
       "alaFipsEtunnelVePortStatsTxUdss": alaFipsEtunnelVePortStatsTxUdss,
       "alaFipsEtunnelVePortStatsTxMdas": alaFipsEtunnelVePortStatsTxMdas,
       "alaFipsEtunnelVePortStatsTxUdas": alaFipsEtunnelVePortStatsTxUdas,
       "alaFipsEtunnelVePortStatsTxElpReqs": alaFipsEtunnelVePortStatsTxElpReqs,
       "alaFipsEtunnelVePortStatsTxSwAccs": alaFipsEtunnelVePortStatsTxSwAccs,
       "alaFipsEtunnelVePortStatsTxSwRjts": alaFipsEtunnelVePortStatsTxSwRjts,
       "alaFipsEtunnelVePortStatsTxCvls": alaFipsEtunnelVePortStatsTxCvls,
       "alaFipsEtunnelVePortStatsClear": alaFipsEtunnelVePortStatsClear,
       "alaFipsEtunnelTePortStats": alaFipsEtunnelTePortStats,
       "alaFipsEtunnelTePortStatsTable": alaFipsEtunnelTePortStatsTable,
       "alaFipsEtunnelTePortStatsEntry": alaFipsEtunnelTePortStatsEntry,
       "alaFipsEtunnelTePortStatsTunnelId": alaFipsEtunnelTePortStatsTunnelId,
       "alaFipsEtunnelTePortStatsRxElpReqs": alaFipsEtunnelTePortStatsRxElpReqs,
       "alaFipsEtunnelTePortStatsRxSwAccs": alaFipsEtunnelTePortStatsRxSwAccs,
       "alaFipsEtunnelTePortStatsRxSwRjts": alaFipsEtunnelTePortStatsRxSwRjts,
       "alaFipsEtunnelTePortStatsTxElpReqs": alaFipsEtunnelTePortStatsTxElpReqs,
       "alaFipsEtunnelTePortStatsTxSwAccs": alaFipsEtunnelTePortStatsTxSwAccs,
       "alaFipsEtunnelTePortStatsTxSwRjts": alaFipsEtunnelTePortStatsTxSwRjts,
       "alaFipsEtunnelTePortStatsClear": alaFipsEtunnelTePortStatsClear,
       "alaFipsVsanVlanMap": alaFipsVsanVlanMap,
       "alaFipsVsanVlanMapTable": alaFipsVsanVlanMapTable,
       "alaFipsVsanVlanMapEntry": alaFipsVsanVlanMapEntry,
       "alaFipsVsanVlanMapVsanNumber": alaFipsVsanVlanMapVsanNumber,
       "alaFipsVsanVlanMapVlanNumber": alaFipsVsanVlanMapVlanNumber,
       "alaFipsVsanVlanMapRowStatus": alaFipsVsanVlanMapRowStatus,
       "alaFipsDiscAdvt": alaFipsDiscAdvt,
       "alaFipsDiscAdvtTable": alaFipsDiscAdvtTable,
       "alaFipsDiscAdvtEntry": alaFipsDiscAdvtEntry,
       "alaFipsDiscAdvtVlanId": alaFipsDiscAdvtVlanId,
       "alaFipsDiscAdvtAbit": alaFipsDiscAdvtAbit,
       "alaFipsDiscAdvtFkaAdvPeriod": alaFipsDiscAdvtFkaAdvPeriod,
       "alaFipsDiscAdvtPriority": alaFipsDiscAdvtPriority,
       "alaFipsDiscAdvtUdsRetries": alaFipsDiscAdvtUdsRetries,
       "alaFipsDiscAdvtRowStatus": alaFipsDiscAdvtRowStatus,
       "alaFipsEtunnel": alaFipsEtunnel,
       "alaFipsEtunnelTable": alaFipsEtunnelTable,
       "alaFipsEtunnelEntry": alaFipsEtunnelEntry,
       "alaFipsEtunnelId": alaFipsEtunnelId,
       "alaFipsEtunnelVlanId": alaFipsEtunnelVlanId,
       "alaFipsEtunnelIfIndexOne": alaFipsEtunnelIfIndexOne,
       "alaFipsEtunnelIfIndexTwo": alaFipsEtunnelIfIndexTwo,
       "alaFipsEtunnelRowStatus": alaFipsEtunnelRowStatus,
       "alaFipsEtunnelStatsClear": alaFipsEtunnelStatsClear,
       "alaFipsNpivSession": alaFipsNpivSession,
       "alaFipsNpivSessionTable": alaFipsNpivSessionTable,
       "alaFipsNpivSessionEntry": alaFipsNpivSessionEntry,
       "alaFipsNpivSessionEnodeMAC": alaFipsNpivSessionEnodeMAC,
       "alaFipsNpivSessionVNMAC": alaFipsNpivSessionVNMAC,
       "alaFipsNpivSessionVlanId": alaFipsNpivSessionVlanId,
       "alaFipsNpivSessionInIfIndex": alaFipsNpivSessionInIfIndex,
       "alaFipsNpivSessionOutIfIndex": alaFipsNpivSessionOutIfIndex,
       "alaFipsNpivSessionFCFMAC": alaFipsNpivSessionFCFMAC,
       "alaFipsNpivSessionStatus": alaFipsNpivSessionStatus,
       "alaFipsNpivSessionLoginTimeDate": alaFipsNpivSessionLoginTimeDate,
       "alaFipsRnpivSession": alaFipsRnpivSession,
       "alaFipsRnpivSessionTable": alaFipsRnpivSessionTable,
       "alaFipsRnpivSessionEntry": alaFipsRnpivSessionEntry,
       "alaFipsRnpivSessionFcid": alaFipsRnpivSessionFcid,
       "alaFipsRnpivSessionVsanId": alaFipsRnpivSessionVsanId,
       "alaFipsRnpivSessionVNMAC": alaFipsRnpivSessionVNMAC,
       "alaFipsRnpivSessionVlanId": alaFipsRnpivSessionVlanId,
       "alaFipsRnpivSessionInIfIndex": alaFipsRnpivSessionInIfIndex,
       "alaFipsRnpivSessionOutIfIndex": alaFipsRnpivSessionOutIfIndex,
       "alaFipsRnpivSessionFCFMAC": alaFipsRnpivSessionFCFMAC,
       "alaFipsRnpivSessionStatus": alaFipsRnpivSessionStatus,
       "alaFipsRnpivSessionLoginTimeDate": alaFipsRnpivSessionLoginTimeDate,
       "alaFipsEtunnelSession": alaFipsEtunnelSession,
       "alaFipsEtunnelSessionTable": alaFipsEtunnelSessionTable,
       "alaFipsEtunnelSessionEntry": alaFipsEtunnelSessionEntry,
       "alaFipsEtunnelSessionTunnelId": alaFipsEtunnelSessionTunnelId,
       "alaFipsEtunnelSessionVlanId": alaFipsEtunnelSessionVlanId,
       "alaFipsEtunnelSessionInIfIndex": alaFipsEtunnelSessionInIfIndex,
       "alaFipsEtunnelSessionOutIfIndex": alaFipsEtunnelSessionOutIfIndex,
       "alaFipsEtunnelSessionFCFMAC": alaFipsEtunnelSessionFCFMAC,
       "alaFipsEtunnelSessionStatus": alaFipsEtunnelSessionStatus,
       "alaFipsEtunnelSessionLoginTimeDate": alaFipsEtunnelSessionLoginTimeDate,
       "alaFipsEtunnelSessionPairMode": alaFipsEtunnelSessionPairMode,
       "alaFcNpivLoadBalSess": alaFcNpivLoadBalSess,
       "alaFcNpivLoadBalSessTable": alaFcNpivLoadBalSessTable,
       "alaFcNpivLoadBalSessEntry": alaFcNpivLoadBalSessEntry,
       "alaFcNpivLoadBalSessIfIndex": alaFcNpivLoadBalSessIfIndex,
       "alaFcNpivLoadBalSessCount": alaFcNpivLoadBalSessCount,
       "alaFcIntfEtunnelStats": alaFcIntfEtunnelStats,
       "alaFcIntfEtunnelStatsTable": alaFcIntfEtunnelStatsTable,
       "alaFcIntfEtunnelStatsEntry": alaFcIntfEtunnelStatsEntry,
       "alaFcIntfEtunnelStatsIfIndex": alaFcIntfEtunnelStatsIfIndex,
       "alaFcIntfEtunnelStatsTunnelId": alaFcIntfEtunnelStatsTunnelId,
       "alaFcIntfEtunnelStatsRxElpReqs": alaFcIntfEtunnelStatsRxElpReqs,
       "alaFcIntfEtunnelStatsRxSwAccs": alaFcIntfEtunnelStatsRxSwAccs,
       "alaFcIntfEtunnelStatsRxSwRjts": alaFcIntfEtunnelStatsRxSwRjts,
       "alaFcIntfEtunnelStatsTxElpReqs": alaFcIntfEtunnelStatsTxElpReqs,
       "alaFcIntfEtunnelStatsTxSwAccs": alaFcIntfEtunnelStatsTxSwAccs,
       "alaFcIntfEtunnelStatsTxSwRjts": alaFcIntfEtunnelStatsTxSwRjts,
       "alcatelIND1FipsMIBConformance": alcatelIND1FipsMIBConformance,
       "alcatelIND1FipsMIBGroups": alcatelIND1FipsMIBGroups,
       "alaFipsInfoGroup": alaFipsInfoGroup,
       "alaFipsVlanGroup": alaFipsVlanGroup,
       "alaFipsVlanEnodeStatsGroup": alaFipsVlanEnodeStatsGroup,
       "alaFipsVlanFcfStatsGroup": alaFipsVlanFcfStatsGroup,
       "alaFipsIntfGroup": alaFipsIntfGroup,
       "alaFipsIntfEnodeStatsGroup": alaFipsIntfEnodeStatsGroup,
       "alaFipsIntfFcfStatsGroup": alaFipsIntfFcfStatsGroup,
       "alaFipsFcfGroup": alaFipsFcfGroup,
       "alaFipsSessionGroup": alaFipsSessionGroup,
       "alaFipsNotificationObjectGroup": alaFipsNotificationObjectGroup,
       "alaFipsNotificationGroup": alaFipsNotificationGroup,
       "alaFcVsanGroup": alaFcVsanGroup,
       "alaFcVfpaGroup": alaFcVfpaGroup,
       "alaFcIntfGroup": alaFcIntfGroup,
       "alaFcNpivStaticLoadBalanceGroup": alaFcNpivStaticLoadBalanceGroup,
       "alaFcNodeGroup": alaFcNodeGroup,
       "alaFcSessGroup": alaFcSessGroup,
       "alaFcIntfNpivStatsGroup": alaFcIntfNpivStatsGroup,
       "alaFcVsanNpivStatsGroup": alaFcVsanNpivStatsGroup,
       "alaFcIntfRnpivStatsGroup": alaFcIntfRnpivStatsGroup,
       "alaFcVsanRnpivStatsGroup": alaFcVsanRnpivStatsGroup,
       "alaFcInfoGroup": alaFcInfoGroup,
       "alaFipsVlanNpivDiscStatsGroup": alaFipsVlanNpivDiscStatsGroup,
       "alaFipsIntfNpivDiscStatsGroup": alaFipsIntfNpivDiscStatsGroup,
       "alaFipsVlanNpivLoginStatsGroup": alaFipsVlanNpivLoginStatsGroup,
       "alaFipsIntfNpivLoginStatsGroup": alaFipsIntfNpivLoginStatsGroup,
       "alaFipsVlanRnpivDiscStatsGroup": alaFipsVlanRnpivDiscStatsGroup,
       "alaFipsIntfRnpivDiscStatsGroup": alaFipsIntfRnpivDiscStatsGroup,
       "alaFipsVlanRnpivLoginStatsGroup": alaFipsVlanRnpivLoginStatsGroup,
       "alaFipsIntfRnpivLoginStatsGroup": alaFipsIntfRnpivLoginStatsGroup,
       "alaFipsEtunnelVePortStatsGroup": alaFipsEtunnelVePortStatsGroup,
       "alaFipsEtunnelTePortStatsGroup": alaFipsEtunnelTePortStatsGroup,
       "alaFipsVsanVlanMapGroup": alaFipsVsanVlanMapGroup,
       "alaFipsDiscAdvtGroup": alaFipsDiscAdvtGroup,
       "alaFipsEtunnelGroup": alaFipsEtunnelGroup,
       "alaFipsNpivSessionGroup": alaFipsNpivSessionGroup,
       "alaFipsRnpivSessionGroup": alaFipsRnpivSessionGroup,
       "alaFipsEtunnelSessionGroup": alaFipsEtunnelSessionGroup,
       "alaFcNpivLoadBalSessGroup": alaFcNpivLoadBalSessGroup,
       "alaFcIntfEtunnelStatsGroup": alaFcIntfEtunnelStatsGroup,
       "alcatelIND1FipsMIBCompliances": alcatelIND1FipsMIBCompliances,
       "alcatelIND1FipsMIBCompliance": alcatelIND1FipsMIBCompliance}
)
