# SNMP MIB module (ELFIQ-MODULE-FOVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELFIQ-MODULE-FOVE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:52 2024
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

(common,
 commonConformance) = mibBuilder.importSymbols(
    "ELFIQ-INC-MIB",
    "common",
    "commonConformance")

(commonComponent,
 commonNotification) = mibBuilder.importSymbols(
    "ELFIQ-MODULE-COMMON-MIB",
    "commonComponent",
    "commonNotification")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

foveInfo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FoveIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )



# MIB Managed Objects in the order of their OIDs



class _FoveIntNumber_Type(Integer32):
    """Custom type foveIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_FoveIntNumber_Type.__name__ = "Integer32"
_FoveIntNumber_Object = MibScalar
foveIntNumber = _FoveIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 2, 1),
    _FoveIntNumber_Type()
)
foveIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foveIntNumber.setStatus("current")
_FoveTable_Object = MibTable
foveTable = _FoveTable_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    foveTable.setStatus("current")
_FoveEntry_Object = MibTableRow
foveEntry = _FoveEntry_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 2, 2, 1)
)
foveEntry.setIndexNames(
    (0, "ELFIQ-MODULE-FOVE-MIB", "foveIntIndex"),
)
if mibBuilder.loadTexts:
    foveEntry.setStatus("current")
_FoveIntIndex_Type = FoveIndex
_FoveIntIndex_Object = MibTableColumn
foveIntIndex = _FoveIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 2, 2, 1, 1),
    _FoveIntIndex_Type()
)
foveIntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foveIntIndex.setStatus("current")


class _FoveIntUsed_Type(DisplayString):
    """Custom type foveIntUsed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FoveIntUsed_Type.__name__ = "DisplayString"
_FoveIntUsed_Object = MibTableColumn
foveIntUsed = _FoveIntUsed_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 2, 2, 1, 2),
    _FoveIntUsed_Type()
)
foveIntUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foveIntUsed.setStatus("current")


class _FoveIntType_Type(Integer32):
    """Custom type foveIntType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("critical", 2),
          ("management", 1))
    )


_FoveIntType_Type.__name__ = "Integer32"
_FoveIntType_Object = MibTableColumn
foveIntType = _FoveIntType_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 2, 2, 1, 3),
    _FoveIntType_Type()
)
foveIntType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foveIntType.setStatus("current")


class _FoveLocalState_Type(Integer32):
    """Custom type foveLocalState based on Integer32"""
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
        *(("dead", 5),
          ("failure", 4),
          ("managementfailure", 7),
          ("master", 2),
          ("negociation", 1),
          ("paused", 6),
          ("slave", 3))
    )


_FoveLocalState_Type.__name__ = "Integer32"
_FoveLocalState_Object = MibTableColumn
foveLocalState = _FoveLocalState_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 2, 2, 1, 4),
    _FoveLocalState_Type()
)
foveLocalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foveLocalState.setStatus("current")
_FoveRemoteId_Type = Unsigned32
_FoveRemoteId_Object = MibTableColumn
foveRemoteId = _FoveRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 2, 2, 1, 5),
    _FoveRemoteId_Type()
)
foveRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foveRemoteId.setStatus("current")
_FoveRemoteSeq_Type = Unsigned32
_FoveRemoteSeq_Object = MibTableColumn
foveRemoteSeq = _FoveRemoteSeq_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 2, 2, 1, 6),
    _FoveRemoteSeq_Type()
)
foveRemoteSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foveRemoteSeq.setStatus("current")


class _FoveRemoteState_Type(Integer32):
    """Custom type foveRemoteState based on Integer32"""
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
        *(("dead", 5),
          ("failure", 4),
          ("managementfailure", 7),
          ("master", 2),
          ("negociation", 1),
          ("paused", 6),
          ("slave", 3))
    )


_FoveRemoteState_Type.__name__ = "Integer32"
_FoveRemoteState_Object = MibTableColumn
foveRemoteState = _FoveRemoteState_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 2, 2, 1, 7),
    _FoveRemoteState_Type()
)
foveRemoteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foveRemoteState.setStatus("current")
_FoveRemoteMgmtIP_Type = IpAddress
_FoveRemoteMgmtIP_Object = MibTableColumn
foveRemoteMgmtIP = _FoveRemoteMgmtIP_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 2, 2, 1, 8),
    _FoveRemoteMgmtIP_Type()
)
foveRemoteMgmtIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foveRemoteMgmtIP.setStatus("current")


class _FoveRemoteIfName_Type(DisplayString):
    """Custom type foveRemoteIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FoveRemoteIfName_Type.__name__ = "DisplayString"
_FoveRemoteIfName_Object = MibTableColumn
foveRemoteIfName = _FoveRemoteIfName_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 2, 2, 1, 9),
    _FoveRemoteIfName_Type()
)
foveRemoteIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foveRemoteIfName.setStatus("current")
_FoveRemoteLastL2FoMSec_Type = Unsigned32
_FoveRemoteLastL2FoMSec_Object = MibTableColumn
foveRemoteLastL2FoMSec = _FoveRemoteLastL2FoMSec_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 2, 2, 1, 10),
    _FoveRemoteLastL2FoMSec_Type()
)
foveRemoteLastL2FoMSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foveRemoteLastL2FoMSec.setStatus("current")
_FoveRemoteMac_Type = MacAddress
_FoveRemoteMac_Object = MibTableColumn
foveRemoteMac = _FoveRemoteMac_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 2, 2, 1, 11),
    _FoveRemoteMac_Type()
)
foveRemoteMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foveRemoteMac.setStatus("current")


class _FoveVIPStatus_Type(Integer32):
    """Custom type foveVIPStatus based on Integer32"""
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


_FoveVIPStatus_Type.__name__ = "Integer32"
_FoveVIPStatus_Object = MibTableColumn
foveVIPStatus = _FoveVIPStatus_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 2, 2, 1, 12),
    _FoveVIPStatus_Type()
)
foveVIPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foveVIPStatus.setStatus("current")
_FoveVIP_Type = IpAddress
_FoveVIP_Object = MibTableColumn
foveVIP = _FoveVIP_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 2, 2, 1, 13),
    _FoveVIP_Type()
)
foveVIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foveVIP.setStatus("current")
_FoveNotification_ObjectIdentity = ObjectIdentity
foveNotification = _FoveNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 2, 2)
)
_FoveGroups_ObjectIdentity = ObjectIdentity
foveGroups = _FoveGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19713, 2, 1, 2)
)

# Managed Objects groups

systInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19713, 2, 1, 2, 1)
)
systInfoGroup.setObjects(
      *(("ELFIQ-MODULE-FOVE-MIB", "foveIntNumber"),
        ("ELFIQ-MODULE-FOVE-MIB", "foveIntIndex"),
        ("ELFIQ-MODULE-FOVE-MIB", "foveIntUsed"),
        ("ELFIQ-MODULE-FOVE-MIB", "foveIntType"),
        ("ELFIQ-MODULE-FOVE-MIB", "foveLocalState"),
        ("ELFIQ-MODULE-FOVE-MIB", "foveRemoteId"),
        ("ELFIQ-MODULE-FOVE-MIB", "foveRemoteSeq"),
        ("ELFIQ-MODULE-FOVE-MIB", "foveRemoteState"),
        ("ELFIQ-MODULE-FOVE-MIB", "foveRemoteMgmtIP"),
        ("ELFIQ-MODULE-FOVE-MIB", "foveRemoteIfName"),
        ("ELFIQ-MODULE-FOVE-MIB", "foveRemoteLastL2FoMSec"),
        ("ELFIQ-MODULE-FOVE-MIB", "foveRemoteMac"),
        ("ELFIQ-MODULE-FOVE-MIB", "foveVIPStatus"),
        ("ELFIQ-MODULE-FOVE-MIB", "foveVIP"))
)
if mibBuilder.loadTexts:
    systInfoGroup.setStatus("current")


# Notification objects

foveStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 2, 2, 1)
)
foveStatusChanged.setObjects(
      *(("ELFIQ-MODULE-FOVE-MIB", "foveLocalState"),
        ("ELFIQ-MODULE-FOVE-MIB", "foveRemoteState"),
        ("ELFIQ-MODULE-FOVE-MIB", "foveVIPStatus"),
        ("ELFIQ-MODULE-FOVE-MIB", "foveVIP"))
)
if mibBuilder.loadTexts:
    foveStatusChanged.setStatus(
        "current"
    )


# Notifications groups

foveNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 19713, 2, 1, 2, 2)
)
foveNotificationGroup.setObjects(
    ("ELFIQ-MODULE-FOVE-MIB", "foveStatusChanged")
)
if mibBuilder.loadTexts:
    foveNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELFIQ-MODULE-FOVE-MIB",
    **{"FoveIndex": FoveIndex,
       "foveInfo": foveInfo,
       "foveIntNumber": foveIntNumber,
       "foveTable": foveTable,
       "foveEntry": foveEntry,
       "foveIntIndex": foveIntIndex,
       "foveIntUsed": foveIntUsed,
       "foveIntType": foveIntType,
       "foveLocalState": foveLocalState,
       "foveRemoteId": foveRemoteId,
       "foveRemoteSeq": foveRemoteSeq,
       "foveRemoteState": foveRemoteState,
       "foveRemoteMgmtIP": foveRemoteMgmtIP,
       "foveRemoteIfName": foveRemoteIfName,
       "foveRemoteLastL2FoMSec": foveRemoteLastL2FoMSec,
       "foveRemoteMac": foveRemoteMac,
       "foveVIPStatus": foveVIPStatus,
       "foveVIP": foveVIP,
       "foveNotification": foveNotification,
       "foveStatusChanged": foveStatusChanged,
       "foveGroups": foveGroups,
       "systInfoGroup": systInfoGroup,
       "foveNotificationGroup": foveNotificationGroup}
)
