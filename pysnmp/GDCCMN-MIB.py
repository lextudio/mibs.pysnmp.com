# SNMP MIB module (GDCCMN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GDCCMN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:29 2024
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Gdc_ObjectIdentity = ObjectIdentity
gdc = _Gdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498)
)
_Cmn_ObjectIdentity = ObjectIdentity
cmn = _Cmn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 1)
)
_CmnTrap_ObjectIdentity = ObjectIdentity
cmnTrap = _CmnTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 1, 1)
)


class _CmnTrapGlobal_Type(Integer32):
    """Custom type cmnTrapGlobal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CmnTrapGlobal_Type.__name__ = "Integer32"
_CmnTrapGlobal_Object = MibScalar
cmnTrapGlobal = _CmnTrapGlobal_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 1, 1),
    _CmnTrapGlobal_Type()
)
cmnTrapGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmnTrapGlobal.setStatus("mandatory")
_CmnTrapAddrNumber_Type = Integer32
_CmnTrapAddrNumber_Object = MibScalar
cmnTrapAddrNumber = _CmnTrapAddrNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 1, 2),
    _CmnTrapAddrNumber_Type()
)
cmnTrapAddrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmnTrapAddrNumber.setStatus("mandatory")
_CmnTrapAddrTable_Object = MibTable
cmnTrapAddrTable = _CmnTrapAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cmnTrapAddrTable.setStatus("mandatory")
_CmnTrapAddrEntry_Object = MibTableRow
cmnTrapAddrEntry = _CmnTrapAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 1, 3, 1)
)
cmnTrapAddrEntry.setIndexNames(
    (0, "GDCCMN-MIB", "cmnTrapAddrIpDest"),
    (0, "GDCCMN-MIB", "cmnTrapAddrUdpDest"),
)
if mibBuilder.loadTexts:
    cmnTrapAddrEntry.setStatus("mandatory")
_CmnTrapAddrIpDest_Type = IpAddress
_CmnTrapAddrIpDest_Object = MibTableColumn
cmnTrapAddrIpDest = _CmnTrapAddrIpDest_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 1, 3, 1, 1),
    _CmnTrapAddrIpDest_Type()
)
cmnTrapAddrIpDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmnTrapAddrIpDest.setStatus("mandatory")
_CmnTrapAddrUdpDest_Type = Integer32
_CmnTrapAddrUdpDest_Object = MibTableColumn
cmnTrapAddrUdpDest = _CmnTrapAddrUdpDest_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 1, 3, 1, 2),
    _CmnTrapAddrUdpDest_Type()
)
cmnTrapAddrUdpDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmnTrapAddrUdpDest.setStatus("mandatory")


class _CmnTrapAddrCommunity_Type(DisplayString):
    """Custom type cmnTrapAddrCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CmnTrapAddrCommunity_Type.__name__ = "DisplayString"
_CmnTrapAddrCommunity_Object = MibTableColumn
cmnTrapAddrCommunity = _CmnTrapAddrCommunity_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 1, 3, 1, 3),
    _CmnTrapAddrCommunity_Type()
)
cmnTrapAddrCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmnTrapAddrCommunity.setStatus("mandatory")


class _CmnTrapAddrStatus_Type(Integer32):
    """Custom type cmnTrapAddrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_CmnTrapAddrStatus_Type.__name__ = "Integer32"
_CmnTrapAddrStatus_Object = MibTableColumn
cmnTrapAddrStatus = _CmnTrapAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 1, 3, 1, 4),
    _CmnTrapAddrStatus_Type()
)
cmnTrapAddrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmnTrapAddrStatus.setStatus("mandatory")
_CmnCommName_ObjectIdentity = ObjectIdentity
cmnCommName = _CmnCommName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 1, 2)
)
_CmnCommunityNumber_Type = Integer32
_CmnCommunityNumber_Object = MibScalar
cmnCommunityNumber = _CmnCommunityNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 2, 1),
    _CmnCommunityNumber_Type()
)
cmnCommunityNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmnCommunityNumber.setStatus("mandatory")
_CmnCommunityTable_Object = MibTable
cmnCommunityTable = _CmnCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cmnCommunityTable.setStatus("mandatory")
_CmnCommunityEntry_Object = MibTableRow
cmnCommunityEntry = _CmnCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 2, 2, 1)
)
cmnCommunityEntry.setIndexNames(
    (0, "GDCCMN-MIB", "cmnCommunityIndex"),
)
if mibBuilder.loadTexts:
    cmnCommunityEntry.setStatus("mandatory")
_CmnCommunityIndex_Type = Integer32
_CmnCommunityIndex_Object = MibTableColumn
cmnCommunityIndex = _CmnCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 2, 2, 1, 1),
    _CmnCommunityIndex_Type()
)
cmnCommunityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmnCommunityIndex.setStatus("mandatory")


class _CmnCommunityName_Type(DisplayString):
    """Custom type cmnCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CmnCommunityName_Type.__name__ = "DisplayString"
_CmnCommunityName_Object = MibTableColumn
cmnCommunityName = _CmnCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 2, 2, 1, 2),
    _CmnCommunityName_Type()
)
cmnCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmnCommunityName.setStatus("mandatory")


class _CmnCommunityAccess_Type(Integer32):
    """Custom type cmnCommunityAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAccess", 3),
          ("readOnly", 1),
          ("readWrite", 2))
    )


_CmnCommunityAccess_Type.__name__ = "Integer32"
_CmnCommunityAccess_Object = MibTableColumn
cmnCommunityAccess = _CmnCommunityAccess_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 2, 2, 1, 3),
    _CmnCommunityAccess_Type()
)
cmnCommunityAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmnCommunityAccess.setStatus("mandatory")


class _CmnCommunityStatus_Type(Integer32):
    """Custom type cmnCommunityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_CmnCommunityStatus_Type.__name__ = "Integer32"
_CmnCommunityStatus_Object = MibTableColumn
cmnCommunityStatus = _CmnCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 2, 2, 1, 4),
    _CmnCommunityStatus_Type()
)
cmnCommunityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmnCommunityStatus.setStatus("mandatory")


class _CmnMIBVersion_Type(DisplayString):
    """Custom type cmnMIBVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_CmnMIBVersion_Type.__name__ = "DisplayString"
_CmnMIBVersion_Object = MibScalar
cmnMIBVersion = _CmnMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 3),
    _CmnMIBVersion_Type()
)
cmnMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmnMIBVersion.setStatus("mandatory")
_CmnAlarm_ObjectIdentity = ObjectIdentity
cmnAlarm = _CmnAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 1, 4)
)
_CmnAlarmStatusTable_Object = MibTable
cmnAlarmStatusTable = _CmnAlarmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cmnAlarmStatusTable.setStatus("mandatory")
_CmnAlarmStatusEntry_Object = MibTableRow
cmnAlarmStatusEntry = _CmnAlarmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 4, 1, 1)
)
cmnAlarmStatusEntry.setIndexNames(
    (0, "GDCCMN-MIB", "cmnAlarmStatusIndex"),
    (0, "GDCCMN-MIB", "cmnAlarmStatusIdentifier"),
)
if mibBuilder.loadTexts:
    cmnAlarmStatusEntry.setStatus("mandatory")
_CmnAlarmStatusIndex_Type = Integer32
_CmnAlarmStatusIndex_Object = MibTableColumn
cmnAlarmStatusIndex = _CmnAlarmStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 4, 1, 1, 1),
    _CmnAlarmStatusIndex_Type()
)
cmnAlarmStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmnAlarmStatusIndex.setStatus("mandatory")
_CmnAlarmStatusIdentifier_Type = ObjectIdentifier
_CmnAlarmStatusIdentifier_Object = MibTableColumn
cmnAlarmStatusIdentifier = _CmnAlarmStatusIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 4, 1, 1, 2),
    _CmnAlarmStatusIdentifier_Type()
)
cmnAlarmStatusIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmnAlarmStatusIdentifier.setStatus("mandatory")


class _CmnAlarmCurrentStatus_Type(Integer32):
    """Custom type cmnAlarmCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_CmnAlarmCurrentStatus_Type.__name__ = "Integer32"
_CmnAlarmCurrentStatus_Object = MibTableColumn
cmnAlarmCurrentStatus = _CmnAlarmCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 4, 1, 1, 3),
    _CmnAlarmCurrentStatus_Type()
)
cmnAlarmCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmnAlarmCurrentStatus.setStatus("mandatory")
_CmnAlarmMaskTable_Object = MibTable
cmnAlarmMaskTable = _CmnAlarmMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cmnAlarmMaskTable.setStatus("mandatory")
_CmnAlarmMaskEntry_Object = MibTableRow
cmnAlarmMaskEntry = _CmnAlarmMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 4, 2, 1)
)
cmnAlarmMaskEntry.setIndexNames(
    (0, "GDCCMN-MIB", "cmnAlarmMaskIndex"),
    (0, "GDCCMN-MIB", "cmnAlarmMaskIdentifier"),
)
if mibBuilder.loadTexts:
    cmnAlarmMaskEntry.setStatus("mandatory")
_CmnAlarmMaskIndex_Type = Integer32
_CmnAlarmMaskIndex_Object = MibTableColumn
cmnAlarmMaskIndex = _CmnAlarmMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 4, 2, 1, 1),
    _CmnAlarmMaskIndex_Type()
)
cmnAlarmMaskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmnAlarmMaskIndex.setStatus("mandatory")
_CmnAlarmMaskIdentifier_Type = ObjectIdentifier
_CmnAlarmMaskIdentifier_Object = MibTableColumn
cmnAlarmMaskIdentifier = _CmnAlarmMaskIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 4, 2, 1, 2),
    _CmnAlarmMaskIdentifier_Type()
)
cmnAlarmMaskIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmnAlarmMaskIdentifier.setStatus("mandatory")


class _CmnAlarmMask_Type(Integer32):
    """Custom type cmnAlarmMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mask", 1),
          ("unmask", 2))
    )


_CmnAlarmMask_Type.__name__ = "Integer32"
_CmnAlarmMask_Object = MibTableColumn
cmnAlarmMask = _CmnAlarmMask_Object(
    (1, 3, 6, 1, 4, 1, 498, 1, 4, 2, 1, 3),
    _CmnAlarmMask_Type()
)
cmnAlarmMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmnAlarmMask.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cmnAlarmStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 498, 1, 4, 0, 1)
)
cmnAlarmStatusTrap.setObjects(
    ("GDCCMN-MIB", "cmnAlarmCurrentStatus")
)
if mibBuilder.loadTexts:
    cmnAlarmStatusTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GDCCMN-MIB",
    **{"gdc": gdc,
       "cmn": cmn,
       "cmnTrap": cmnTrap,
       "cmnTrapGlobal": cmnTrapGlobal,
       "cmnTrapAddrNumber": cmnTrapAddrNumber,
       "cmnTrapAddrTable": cmnTrapAddrTable,
       "cmnTrapAddrEntry": cmnTrapAddrEntry,
       "cmnTrapAddrIpDest": cmnTrapAddrIpDest,
       "cmnTrapAddrUdpDest": cmnTrapAddrUdpDest,
       "cmnTrapAddrCommunity": cmnTrapAddrCommunity,
       "cmnTrapAddrStatus": cmnTrapAddrStatus,
       "cmnCommName": cmnCommName,
       "cmnCommunityNumber": cmnCommunityNumber,
       "cmnCommunityTable": cmnCommunityTable,
       "cmnCommunityEntry": cmnCommunityEntry,
       "cmnCommunityIndex": cmnCommunityIndex,
       "cmnCommunityName": cmnCommunityName,
       "cmnCommunityAccess": cmnCommunityAccess,
       "cmnCommunityStatus": cmnCommunityStatus,
       "cmnMIBVersion": cmnMIBVersion,
       "cmnAlarm": cmnAlarm,
       "cmnAlarmStatusTrap": cmnAlarmStatusTrap,
       "cmnAlarmStatusTable": cmnAlarmStatusTable,
       "cmnAlarmStatusEntry": cmnAlarmStatusEntry,
       "cmnAlarmStatusIndex": cmnAlarmStatusIndex,
       "cmnAlarmStatusIdentifier": cmnAlarmStatusIdentifier,
       "cmnAlarmCurrentStatus": cmnAlarmCurrentStatus,
       "cmnAlarmMaskTable": cmnAlarmMaskTable,
       "cmnAlarmMaskEntry": cmnAlarmMaskEntry,
       "cmnAlarmMaskIndex": cmnAlarmMaskIndex,
       "cmnAlarmMaskIdentifier": cmnAlarmMaskIdentifier,
       "cmnAlarmMask": cmnAlarmMask}
)
