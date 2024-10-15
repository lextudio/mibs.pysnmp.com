# SNMP MIB module (VIDEOFRAME-GENERIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VIDEOFRAME-GENERIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:29 2024
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(system,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "system")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(vfGeneric,
 vfMIBModules) = mibBuilder.importSymbols(
    "VIDEOFRAME-REGISTRATIONS-MIB",
    "vfGeneric",
    "vfMIBModules")


# MODULE-IDENTITY

videoframeGenericMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 6, 1, 2)
)
videoframeGenericMIB.setRevisions(
        ("1901-01-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SysObjectID_Type = ObjectIdentifier
_SysObjectID_Object = MibScalar
sysObjectID = _SysObjectID_Object(
    (1, 3, 6, 1, 2, 1, 1, 2),
    _SysObjectID_Type()
)
sysObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysObjectID.setStatus("current")
_VfBox_ObjectIdentity = ObjectIdentity
vfBox = _VfBox_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 3, 1)
)
_VfBoxEvents_ObjectIdentity = ObjectIdentity
vfBoxEvents = _VfBoxEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 3, 1, 0)
)
_VfMaxBoxes_Type = Integer32
_VfMaxBoxes_Object = MibScalar
vfMaxBoxes = _VfMaxBoxes_Object(
    (1, 3, 6, 1, 4, 1, 4596, 3, 1, 1),
    _VfMaxBoxes_Type()
)
vfMaxBoxes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfMaxBoxes.setStatus("current")
_VfBoxTableNextIndex_Type = Integer32
_VfBoxTableNextIndex_Object = MibScalar
vfBoxTableNextIndex = _VfBoxTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4596, 3, 1, 2),
    _VfBoxTableNextIndex_Type()
)
vfBoxTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfBoxTableNextIndex.setStatus("current")
_VfBoxTable_Object = MibTable
vfBoxTable = _VfBoxTable_Object(
    (1, 3, 6, 1, 4, 1, 4596, 3, 1, 3)
)
if mibBuilder.loadTexts:
    vfBoxTable.setStatus("current")
_VfBoxEntry_Object = MibTableRow
vfBoxEntry = _VfBoxEntry_Object(
    (1, 3, 6, 1, 4, 1, 4596, 3, 1, 3, 1)
)
vfBoxEntry.setIndexNames(
    (0, "VIDEOFRAME-GENERIC-MIB", "vfBoxId"),
)
if mibBuilder.loadTexts:
    vfBoxEntry.setStatus("current")
_VfBoxEntryIndex_Type = Integer32
_VfBoxEntryIndex_Object = MibTableColumn
vfBoxEntryIndex = _VfBoxEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 4596, 3, 1, 3, 1, 1),
    _VfBoxEntryIndex_Type()
)
vfBoxEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vfBoxEntryIndex.setStatus("current")


class _VfBoxId_Type(DisplayString):
    """Custom type vfBoxId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_VfBoxId_Type.__name__ = "DisplayString"
_VfBoxId_Object = MibTableColumn
vfBoxId = _VfBoxId_Object(
    (1, 3, 6, 1, 4, 1, 4596, 3, 1, 3, 1, 2),
    _VfBoxId_Type()
)
vfBoxId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vfBoxId.setStatus("current")


class _VfBoxPartNo_Type(DisplayString):
    """Custom type vfBoxPartNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_VfBoxPartNo_Type.__name__ = "DisplayString"
_VfBoxPartNo_Object = MibTableColumn
vfBoxPartNo = _VfBoxPartNo_Object(
    (1, 3, 6, 1, 4, 1, 4596, 3, 1, 3, 1, 3),
    _VfBoxPartNo_Type()
)
vfBoxPartNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vfBoxPartNo.setStatus("current")


class _VfBoxPsAStatus_Type(Integer32):
    """Custom type vfBoxPsAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_VfBoxPsAStatus_Type.__name__ = "Integer32"
_VfBoxPsAStatus_Object = MibTableColumn
vfBoxPsAStatus = _VfBoxPsAStatus_Object(
    (1, 3, 6, 1, 4, 1, 4596, 3, 1, 3, 1, 4),
    _VfBoxPsAStatus_Type()
)
vfBoxPsAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfBoxPsAStatus.setStatus("current")


class _VfBoxPsBStatus_Type(Integer32):
    """Custom type vfBoxPsBStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_VfBoxPsBStatus_Type.__name__ = "Integer32"
_VfBoxPsBStatus_Object = MibTableColumn
vfBoxPsBStatus = _VfBoxPsBStatus_Object(
    (1, 3, 6, 1, 4, 1, 4596, 3, 1, 3, 1, 5),
    _VfBoxPsBStatus_Type()
)
vfBoxPsBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfBoxPsBStatus.setStatus("current")


class _VfBoxFailoverStatus_Type(Integer32):
    """Custom type vfBoxFailoverStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 1),
          ("main", 2))
    )


_VfBoxFailoverStatus_Type.__name__ = "Integer32"
_VfBoxFailoverStatus_Object = MibTableColumn
vfBoxFailoverStatus = _VfBoxFailoverStatus_Object(
    (1, 3, 6, 1, 4, 1, 4596, 3, 1, 3, 1, 6),
    _VfBoxFailoverStatus_Type()
)
vfBoxFailoverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfBoxFailoverStatus.setStatus("current")


class _VfBoxTrapEnable_Type(Integer32):
    """Custom type vfBoxTrapEnable based on Integer32"""
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


_VfBoxTrapEnable_Type.__name__ = "Integer32"
_VfBoxTrapEnable_Object = MibTableColumn
vfBoxTrapEnable = _VfBoxTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4596, 3, 1, 3, 1, 7),
    _VfBoxTrapEnable_Type()
)
vfBoxTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vfBoxTrapEnable.setStatus("current")


class _VfBoxSoftwareRev_Type(DisplayString):
    """Custom type vfBoxSoftwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VfBoxSoftwareRev_Type.__name__ = "DisplayString"
_VfBoxSoftwareRev_Object = MibTableColumn
vfBoxSoftwareRev = _VfBoxSoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 4596, 3, 1, 3, 1, 8),
    _VfBoxSoftwareRev_Type()
)
vfBoxSoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfBoxSoftwareRev.setStatus("current")


class _VfBoxState_Type(Integer32):
    """Custom type vfBoxState based on Integer32"""
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
        *(("vfBoxDisabled", 4),
          ("vfBoxFaulty", 3),
          ("vfBoxIdling", 5),
          ("vfBoxInMaintenance", 2),
          ("vfBoxInitializing", 6),
          ("vfBoxResetting", 7),
          ("vfBoxRunning", 1))
    )


_VfBoxState_Type.__name__ = "Integer32"
_VfBoxState_Object = MibTableColumn
vfBoxState = _VfBoxState_Object(
    (1, 3, 6, 1, 4, 1, 4596, 3, 1, 3, 1, 9),
    _VfBoxState_Type()
)
vfBoxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfBoxState.setStatus("current")
_VfBoxEntryStatus_Type = RowStatus
_VfBoxEntryStatus_Object = MibTableColumn
vfBoxEntryStatus = _VfBoxEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4596, 3, 1, 3, 1, 10),
    _VfBoxEntryStatus_Type()
)
vfBoxEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vfBoxEntryStatus.setStatus("current")
_VfAgent_ObjectIdentity = ObjectIdentity
vfAgent = _VfAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 3, 2)
)


class _VfAgentTrapEnable_Type(Integer32):
    """Custom type vfAgentTrapEnable based on Integer32"""
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


_VfAgentTrapEnable_Type.__name__ = "Integer32"
_VfAgentTrapEnable_Object = MibScalar
vfAgentTrapEnable = _VfAgentTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4596, 3, 2, 1),
    _VfAgentTrapEnable_Type()
)
vfAgentTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vfAgentTrapEnable.setStatus("current")
_VfTrapTargMaxTargets_Type = Integer32
_VfTrapTargMaxTargets_Object = MibScalar
vfTrapTargMaxTargets = _VfTrapTargMaxTargets_Object(
    (1, 3, 6, 1, 4, 1, 4596, 3, 2, 2),
    _VfTrapTargMaxTargets_Type()
)
vfTrapTargMaxTargets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfTrapTargMaxTargets.setStatus("current")
_VfTrapTargCfgTableNextIndex_Type = Integer32
_VfTrapTargCfgTableNextIndex_Object = MibScalar
vfTrapTargCfgTableNextIndex = _VfTrapTargCfgTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4596, 3, 2, 3),
    _VfTrapTargCfgTableNextIndex_Type()
)
vfTrapTargCfgTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfTrapTargCfgTableNextIndex.setStatus("current")
_VfTrapTargCfgTable_Object = MibTable
vfTrapTargCfgTable = _VfTrapTargCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4596, 3, 2, 4)
)
if mibBuilder.loadTexts:
    vfTrapTargCfgTable.setStatus("current")
_VfTrapTargCfgEntry_Object = MibTableRow
vfTrapTargCfgEntry = _VfTrapTargCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4596, 3, 2, 4, 1)
)
vfTrapTargCfgEntry.setIndexNames(
    (0, "VIDEOFRAME-GENERIC-MIB", "vfTrapTargCfgIndex"),
)
if mibBuilder.loadTexts:
    vfTrapTargCfgEntry.setStatus("current")
_VfTrapTargCfgIndex_Type = Integer32
_VfTrapTargCfgIndex_Object = MibTableColumn
vfTrapTargCfgIndex = _VfTrapTargCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 4596, 3, 2, 4, 1, 1),
    _VfTrapTargCfgIndex_Type()
)
vfTrapTargCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vfTrapTargCfgIndex.setStatus("current")
_VfTrapTargCfgIpAddress_Type = IpAddress
_VfTrapTargCfgIpAddress_Object = MibTableColumn
vfTrapTargCfgIpAddress = _VfTrapTargCfgIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4596, 3, 2, 4, 1, 2),
    _VfTrapTargCfgIpAddress_Type()
)
vfTrapTargCfgIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vfTrapTargCfgIpAddress.setStatus("current")


class _VfTrapTargCfgCommunity_Type(DisplayString):
    """Custom type vfTrapTargCfgCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VfTrapTargCfgCommunity_Type.__name__ = "DisplayString"
_VfTrapTargCfgCommunity_Object = MibTableColumn
vfTrapTargCfgCommunity = _VfTrapTargCfgCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4596, 3, 2, 4, 1, 3),
    _VfTrapTargCfgCommunity_Type()
)
vfTrapTargCfgCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vfTrapTargCfgCommunity.setStatus("current")
_VfTrapTargCfgEntryStatus_Type = RowStatus
_VfTrapTargCfgEntryStatus_Object = MibTableColumn
vfTrapTargCfgEntryStatus = _VfTrapTargCfgEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4596, 3, 2, 4, 1, 4),
    _VfTrapTargCfgEntryStatus_Type()
)
vfTrapTargCfgEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vfTrapTargCfgEntryStatus.setStatus("current")

# Managed Objects groups


# Notification objects

boxPsAEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4596, 3, 1, 0, 1)
)
boxPsAEvent.setObjects(
      *(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"),
        ("VIDEOFRAME-GENERIC-MIB", "vfBoxPsAStatus"))
)
if mibBuilder.loadTexts:
    boxPsAEvent.setStatus(
        "current"
    )

boxPsBEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4596, 3, 1, 0, 2)
)
boxPsBEvent.setObjects(
      *(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"),
        ("VIDEOFRAME-GENERIC-MIB", "vfBoxPsAStatus"))
)
if mibBuilder.loadTexts:
    boxPsBEvent.setStatus(
        "current"
    )

boxFailoverEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4596, 3, 1, 0, 3)
)
boxFailoverEvent.setObjects(
      *(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"),
        ("VIDEOFRAME-GENERIC-MIB", "vfBoxFailoverStatus"))
)
if mibBuilder.loadTexts:
    boxFailoverEvent.setStatus(
        "current"
    )

boxStateChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4596, 3, 1, 0, 4)
)
boxStateChangeEvent.setObjects(
      *(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"),
        ("VIDEOFRAME-GENERIC-MIB", "vfBoxState"))
)
if mibBuilder.loadTexts:
    boxStateChangeEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIDEOFRAME-GENERIC-MIB",
    **{"sysObjectID": sysObjectID,
       "vfBox": vfBox,
       "vfBoxEvents": vfBoxEvents,
       "boxPsAEvent": boxPsAEvent,
       "boxPsBEvent": boxPsBEvent,
       "boxFailoverEvent": boxFailoverEvent,
       "boxStateChangeEvent": boxStateChangeEvent,
       "vfMaxBoxes": vfMaxBoxes,
       "vfBoxTableNextIndex": vfBoxTableNextIndex,
       "vfBoxTable": vfBoxTable,
       "vfBoxEntry": vfBoxEntry,
       "vfBoxEntryIndex": vfBoxEntryIndex,
       "vfBoxId": vfBoxId,
       "vfBoxPartNo": vfBoxPartNo,
       "vfBoxPsAStatus": vfBoxPsAStatus,
       "vfBoxPsBStatus": vfBoxPsBStatus,
       "vfBoxFailoverStatus": vfBoxFailoverStatus,
       "vfBoxTrapEnable": vfBoxTrapEnable,
       "vfBoxSoftwareRev": vfBoxSoftwareRev,
       "vfBoxState": vfBoxState,
       "vfBoxEntryStatus": vfBoxEntryStatus,
       "vfAgent": vfAgent,
       "vfAgentTrapEnable": vfAgentTrapEnable,
       "vfTrapTargMaxTargets": vfTrapTargMaxTargets,
       "vfTrapTargCfgTableNextIndex": vfTrapTargCfgTableNextIndex,
       "vfTrapTargCfgTable": vfTrapTargCfgTable,
       "vfTrapTargCfgEntry": vfTrapTargCfgEntry,
       "vfTrapTargCfgIndex": vfTrapTargCfgIndex,
       "vfTrapTargCfgIpAddress": vfTrapTargCfgIpAddress,
       "vfTrapTargCfgCommunity": vfTrapTargCfgCommunity,
       "vfTrapTargCfgEntryStatus": vfTrapTargCfgEntryStatus,
       "videoframeGenericMIB": videoframeGenericMIB}
)
