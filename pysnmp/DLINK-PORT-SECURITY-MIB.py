# SNMP MIB module (DLINK-PORT-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINK-PORT-SECURITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:30:49 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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

swPortSecMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 63)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwPortSecCtrl_ObjectIdentity = ObjectIdentity
swPortSecCtrl = _SwPortSecCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 1)
)


class _SwPortSecTrapLogState_Type(Integer32):
    """Custom type swPortSecTrapLogState based on Integer32"""
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


_SwPortSecTrapLogState_Type.__name__ = "Integer32"
_SwPortSecTrapLogState_Object = MibScalar
swPortSecTrapLogState = _SwPortSecTrapLogState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 1, 1),
    _SwPortSecTrapLogState_Type()
)
swPortSecTrapLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortSecTrapLogState.setStatus("current")
_SwPortSecSysMaxLernAddr_Type = Integer32
_SwPortSecSysMaxLernAddr_Object = MibScalar
swPortSecSysMaxLernAddr = _SwPortSecSysMaxLernAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 1, 2),
    _SwPortSecSysMaxLernAddr_Type()
)
swPortSecSysMaxLernAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortSecSysMaxLernAddr.setStatus("current")


class _SwPortSecTrapState_Type(Integer32):
    """Custom type swPortSecTrapState based on Integer32"""
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


_SwPortSecTrapState_Type.__name__ = "Integer32"
_SwPortSecTrapState_Object = MibScalar
swPortSecTrapState = _SwPortSecTrapState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 1, 3),
    _SwPortSecTrapState_Type()
)
swPortSecTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortSecTrapState.setStatus("current")


class _SwPortSecLogState_Type(Integer32):
    """Custom type swPortSecLogState based on Integer32"""
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


_SwPortSecLogState_Type.__name__ = "Integer32"
_SwPortSecLogState_Object = MibScalar
swPortSecLogState = _SwPortSecLogState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 1, 4),
    _SwPortSecLogState_Type()
)
swPortSecLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortSecLogState.setStatus("current")
_SwPortSecInfo_ObjectIdentity = ObjectIdentity
swPortSecInfo = _SwPortSecInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 2)
)
_SwPortSecMgmt_ObjectIdentity = ObjectIdentity
swPortSecMgmt = _SwPortSecMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3)
)
_SwPortSecMgmtByPort_ObjectIdentity = ObjectIdentity
swPortSecMgmtByPort = _SwPortSecMgmtByPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 1)
)
_SwPortSecPortTable_Object = MibTable
swPortSecPortTable = _SwPortSecPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 1, 1)
)
if mibBuilder.loadTexts:
    swPortSecPortTable.setStatus("current")
_SwPortSecPortEntry_Object = MibTableRow
swPortSecPortEntry = _SwPortSecPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 1, 1, 1)
)
swPortSecPortEntry.setIndexNames(
    (0, "DLINK-PORT-SECURITY-MIB", "swPortSecPortIndex"),
)
if mibBuilder.loadTexts:
    swPortSecPortEntry.setStatus("current")
_SwPortSecPortIndex_Type = Integer32
_SwPortSecPortIndex_Object = MibTableColumn
swPortSecPortIndex = _SwPortSecPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 1, 1, 1, 1),
    _SwPortSecPortIndex_Type()
)
swPortSecPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPortSecPortIndex.setStatus("current")
_SwPortSecPortMaxLernAddr_Type = Integer32
_SwPortSecPortMaxLernAddr_Object = MibTableColumn
swPortSecPortMaxLernAddr = _SwPortSecPortMaxLernAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 1, 1, 1, 2),
    _SwPortSecPortMaxLernAddr_Type()
)
swPortSecPortMaxLernAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortSecPortMaxLernAddr.setStatus("current")


class _SwPortSecPortLockAddrMode_Type(Integer32):
    """Custom type swPortSecPortLockAddrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deleteOnReset", 3),
          ("deleteOnTimeout", 2),
          ("permanent", 1))
    )


_SwPortSecPortLockAddrMode_Type.__name__ = "Integer32"
_SwPortSecPortLockAddrMode_Object = MibTableColumn
swPortSecPortLockAddrMode = _SwPortSecPortLockAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 1, 1, 1, 3),
    _SwPortSecPortLockAddrMode_Type()
)
swPortSecPortLockAddrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortSecPortLockAddrMode.setStatus("current")


class _SwPortSecPortAdmState_Type(Integer32):
    """Custom type swPortSecPortAdmState based on Integer32"""
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


_SwPortSecPortAdmState_Type.__name__ = "Integer32"
_SwPortSecPortAdmState_Object = MibTableColumn
swPortSecPortAdmState = _SwPortSecPortAdmState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 1, 1, 1, 4),
    _SwPortSecPortAdmState_Type()
)
swPortSecPortAdmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortSecPortAdmState.setStatus("current")


class _SwPortSecPortClearCtrl_Type(Integer32):
    """Custom type swPortSecPortClearCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_SwPortSecPortClearCtrl_Type.__name__ = "Integer32"
_SwPortSecPortClearCtrl_Object = MibTableColumn
swPortSecPortClearCtrl = _SwPortSecPortClearCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 1, 1, 1, 5),
    _SwPortSecPortClearCtrl_Type()
)
swPortSecPortClearCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortSecPortClearCtrl.setStatus("current")


class _SwPortSecPortViolationAction_Type(Integer32):
    """Custom type swPortSecPortViolationAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("shutdown", 2))
    )


_SwPortSecPortViolationAction_Type.__name__ = "Integer32"
_SwPortSecPortViolationAction_Object = MibTableColumn
swPortSecPortViolationAction = _SwPortSecPortViolationAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 1, 1, 1, 6),
    _SwPortSecPortViolationAction_Type()
)
swPortSecPortViolationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortSecPortViolationAction.setStatus("current")
_SwPortSecMgmtByVLAN_ObjectIdentity = ObjectIdentity
swPortSecMgmtByVLAN = _SwPortSecMgmtByVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 2)
)
_SwPortSecVLANTable_Object = MibTable
swPortSecVLANTable = _SwPortSecVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 2, 1)
)
if mibBuilder.loadTexts:
    swPortSecVLANTable.setStatus("current")
_SwPortSecVLANEntry_Object = MibTableRow
swPortSecVLANEntry = _SwPortSecVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 2, 1, 1)
)
swPortSecVLANEntry.setIndexNames(
    (0, "DLINK-PORT-SECURITY-MIB", "swPortSecVLANID"),
)
if mibBuilder.loadTexts:
    swPortSecVLANEntry.setStatus("current")


class _SwPortSecVLANID_Type(Integer32):
    """Custom type swPortSecVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwPortSecVLANID_Type.__name__ = "Integer32"
_SwPortSecVLANID_Object = MibTableColumn
swPortSecVLANID = _SwPortSecVLANID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 2, 1, 1, 1),
    _SwPortSecVLANID_Type()
)
swPortSecVLANID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPortSecVLANID.setStatus("current")
_SwPortSecVLANMaxLernAddr_Type = Integer32
_SwPortSecVLANMaxLernAddr_Object = MibTableColumn
swPortSecVLANMaxLernAddr = _SwPortSecVLANMaxLernAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 2, 1, 1, 2),
    _SwPortSecVLANMaxLernAddr_Type()
)
swPortSecVLANMaxLernAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortSecVLANMaxLernAddr.setStatus("current")


class _SwPortSecVLANClearCtrl_Type(Integer32):
    """Custom type swPortSecVLANClearCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_SwPortSecVLANClearCtrl_Type.__name__ = "Integer32"
_SwPortSecVLANClearCtrl_Object = MibTableColumn
swPortSecVLANClearCtrl = _SwPortSecVLANClearCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 2, 1, 1, 3),
    _SwPortSecVLANClearCtrl_Type()
)
swPortSecVLANClearCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortSecVLANClearCtrl.setStatus("current")
_SwPortSecMgmtByVLANOnPort_ObjectIdentity = ObjectIdentity
swPortSecMgmtByVLANOnPort = _SwPortSecMgmtByVLANOnPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 3)
)
_SwPortSecVLANOnPortTable_Object = MibTable
swPortSecVLANOnPortTable = _SwPortSecVLANOnPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 3, 1)
)
if mibBuilder.loadTexts:
    swPortSecVLANOnPortTable.setStatus("current")
_SwPortSecVLANOnPortEntry_Object = MibTableRow
swPortSecVLANOnPortEntry = _SwPortSecVLANOnPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 3, 1, 1)
)
swPortSecVLANOnPortEntry.setIndexNames(
    (0, "DLINK-PORT-SECURITY-MIB", "swPortSecPortIndex"),
    (0, "DLINK-PORT-SECURITY-MIB", "swPortSecVLANID"),
)
if mibBuilder.loadTexts:
    swPortSecVLANOnPortEntry.setStatus("current")
_SwPortSecVLANOnPortMaxLernAddr_Type = Integer32
_SwPortSecVLANOnPortMaxLernAddr_Object = MibTableColumn
swPortSecVLANOnPortMaxLernAddr = _SwPortSecVLANOnPortMaxLernAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 3, 1, 1, 1),
    _SwPortSecVLANOnPortMaxLernAddr_Type()
)
swPortSecVLANOnPortMaxLernAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortSecVLANOnPortMaxLernAddr.setStatus("current")


class _SwPortSecVLANOnPortAddCtrl_Type(Integer32):
    """Custom type swPortSecVLANOnPortAddCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("other", 1))
    )


_SwPortSecVLANOnPortAddCtrl_Type.__name__ = "Integer32"
_SwPortSecVLANOnPortAddCtrl_Object = MibTableColumn
swPortSecVLANOnPortAddCtrl = _SwPortSecVLANOnPortAddCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 3, 1, 1, 2),
    _SwPortSecVLANOnPortAddCtrl_Type()
)
swPortSecVLANOnPortAddCtrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPortSecVLANOnPortAddCtrl.setStatus("current")
_SwPortSecMgmtByVLANOnPortClearCtrl_ObjectIdentity = ObjectIdentity
swPortSecMgmtByVLANOnPortClearCtrl = _SwPortSecMgmtByVLANOnPortClearCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 3, 2)
)
_SwPortSecMgmtByVLANOnPortClearPort_Type = Integer32
_SwPortSecMgmtByVLANOnPortClearPort_Object = MibScalar
swPortSecMgmtByVLANOnPortClearPort = _SwPortSecMgmtByVLANOnPortClearPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 3, 2, 1),
    _SwPortSecMgmtByVLANOnPortClearPort_Type()
)
swPortSecMgmtByVLANOnPortClearPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortSecMgmtByVLANOnPortClearPort.setStatus("current")
_SwPortSecMgmtByVLANOnPortClearVID_Type = Integer32
_SwPortSecMgmtByVLANOnPortClearVID_Object = MibScalar
swPortSecMgmtByVLANOnPortClearVID = _SwPortSecMgmtByVLANOnPortClearVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 3, 2, 2),
    _SwPortSecMgmtByVLANOnPortClearVID_Type()
)
swPortSecMgmtByVLANOnPortClearVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortSecMgmtByVLANOnPortClearVID.setStatus("current")


class _SwPortSecMgmtByVLANOnPortClearAction_Type(Integer32):
    """Custom type swPortSecMgmtByVLANOnPortClearAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_SwPortSecMgmtByVLANOnPortClearAction_Type.__name__ = "Integer32"
_SwPortSecMgmtByVLANOnPortClearAction_Object = MibScalar
swPortSecMgmtByVLANOnPortClearAction = _SwPortSecMgmtByVLANOnPortClearAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 3, 2, 3),
    _SwPortSecMgmtByVLANOnPortClearAction_Type()
)
swPortSecMgmtByVLANOnPortClearAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortSecMgmtByVLANOnPortClearAction.setStatus("current")
_SwPortSecEntriesTable_Object = MibTable
swPortSecEntriesTable = _SwPortSecEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 4)
)
if mibBuilder.loadTexts:
    swPortSecEntriesTable.setStatus("current")
_SwPortSecEntriesEntry_Object = MibTableRow
swPortSecEntriesEntry = _SwPortSecEntriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 4, 1)
)
swPortSecEntriesEntry.setIndexNames(
    (0, "DLINK-PORT-SECURITY-MIB", "swPortSecMac"),
    (0, "DLINK-PORT-SECURITY-MIB", "swPortSecVID"),
)
if mibBuilder.loadTexts:
    swPortSecEntriesEntry.setStatus("current")
_SwPortSecMac_Type = MacAddress
_SwPortSecMac_Object = MibTableColumn
swPortSecMac = _SwPortSecMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 4, 1, 1),
    _SwPortSecMac_Type()
)
swPortSecMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortSecMac.setStatus("current")


class _SwPortSecVID_Type(Integer32):
    """Custom type swPortSecVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwPortSecVID_Type.__name__ = "Integer32"
_SwPortSecVID_Object = MibTableColumn
swPortSecVID = _SwPortSecVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 4, 1, 2),
    _SwPortSecVID_Type()
)
swPortSecVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortSecVID.setStatus("current")
_SwPortSecPort_Type = Integer32
_SwPortSecPort_Object = MibTableColumn
swPortSecPort = _SwPortSecPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 4, 1, 3),
    _SwPortSecPort_Type()
)
swPortSecPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortSecPort.setStatus("current")


class _SwPortSecDelCtrl_Type(Integer32):
    """Custom type swPortSecDelCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_SwPortSecDelCtrl_Type.__name__ = "Integer32"
_SwPortSecDelCtrl_Object = MibTableColumn
swPortSecDelCtrl = _SwPortSecDelCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 4, 1, 4),
    _SwPortSecDelCtrl_Type()
)
swPortSecDelCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortSecDelCtrl.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-PORT-SECURITY-MIB",
    **{"swPortSecMIB": swPortSecMIB,
       "swPortSecCtrl": swPortSecCtrl,
       "swPortSecTrapLogState": swPortSecTrapLogState,
       "swPortSecSysMaxLernAddr": swPortSecSysMaxLernAddr,
       "swPortSecTrapState": swPortSecTrapState,
       "swPortSecLogState": swPortSecLogState,
       "swPortSecInfo": swPortSecInfo,
       "swPortSecMgmt": swPortSecMgmt,
       "swPortSecMgmtByPort": swPortSecMgmtByPort,
       "swPortSecPortTable": swPortSecPortTable,
       "swPortSecPortEntry": swPortSecPortEntry,
       "swPortSecPortIndex": swPortSecPortIndex,
       "swPortSecPortMaxLernAddr": swPortSecPortMaxLernAddr,
       "swPortSecPortLockAddrMode": swPortSecPortLockAddrMode,
       "swPortSecPortAdmState": swPortSecPortAdmState,
       "swPortSecPortClearCtrl": swPortSecPortClearCtrl,
       "swPortSecPortViolationAction": swPortSecPortViolationAction,
       "swPortSecMgmtByVLAN": swPortSecMgmtByVLAN,
       "swPortSecVLANTable": swPortSecVLANTable,
       "swPortSecVLANEntry": swPortSecVLANEntry,
       "swPortSecVLANID": swPortSecVLANID,
       "swPortSecVLANMaxLernAddr": swPortSecVLANMaxLernAddr,
       "swPortSecVLANClearCtrl": swPortSecVLANClearCtrl,
       "swPortSecMgmtByVLANOnPort": swPortSecMgmtByVLANOnPort,
       "swPortSecVLANOnPortTable": swPortSecVLANOnPortTable,
       "swPortSecVLANOnPortEntry": swPortSecVLANOnPortEntry,
       "swPortSecVLANOnPortMaxLernAddr": swPortSecVLANOnPortMaxLernAddr,
       "swPortSecVLANOnPortAddCtrl": swPortSecVLANOnPortAddCtrl,
       "swPortSecMgmtByVLANOnPortClearCtrl": swPortSecMgmtByVLANOnPortClearCtrl,
       "swPortSecMgmtByVLANOnPortClearPort": swPortSecMgmtByVLANOnPortClearPort,
       "swPortSecMgmtByVLANOnPortClearVID": swPortSecMgmtByVLANOnPortClearVID,
       "swPortSecMgmtByVLANOnPortClearAction": swPortSecMgmtByVLANOnPortClearAction,
       "swPortSecEntriesTable": swPortSecEntriesTable,
       "swPortSecEntriesEntry": swPortSecEntriesEntry,
       "swPortSecMac": swPortSecMac,
       "swPortSecVID": swPortSecVID,
       "swPortSecPort": swPortSecPort,
       "swPortSecDelCtrl": swPortSecDelCtrl}
)
