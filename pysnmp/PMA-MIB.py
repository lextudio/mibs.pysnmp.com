# SNMP MIB module (PMA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PMA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:03 2024
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

(IbDataPort,
 infinibandMIB) = mibBuilder.importSymbols(
    "IB-TC-MIB",
    "IbDataPort",
    "infinibandMIB")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ibPmaMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 117, 6)
)
ibPmaMIB.setRevisions(
        ("2005-09-01 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IbPmaObjects_ObjectIdentity = ObjectIdentity
ibPmaObjects = _IbPmaObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 6, 1)
)
_IbPmaPortCntrsInfo_ObjectIdentity = ObjectIdentity
ibPmaPortCntrsInfo = _IbPmaPortCntrsInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 6, 1, 1)
)
_IbPmaPortCntrsTable_Object = MibTable
ibPmaPortCntrsTable = _IbPmaPortCntrsTable_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ibPmaPortCntrsTable.setStatus("current")
_IbPmaPortCntrsEntry_Object = MibTableRow
ibPmaPortCntrsEntry = _IbPmaPortCntrsEntry_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 1, 1, 1)
)
ibPmaPortCntrsEntry.setIndexNames(
    (0, "PMA-MIB", "ibPmaPortCntrsIndex"),
)
if mibBuilder.loadTexts:
    ibPmaPortCntrsEntry.setStatus("current")
_IbPmaPortCntrsIndex_Type = IbDataPort
_IbPmaPortCntrsIndex_Object = MibTableColumn
ibPmaPortCntrsIndex = _IbPmaPortCntrsIndex_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 1, 1, 1, 1),
    _IbPmaPortCntrsIndex_Type()
)
ibPmaPortCntrsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibPmaPortCntrsIndex.setStatus("current")


class _IbPmaSymbolErrCounter_Type(Unsigned32):
    """Custom type ibPmaSymbolErrCounter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaSymbolErrCounter_Type.__name__ = "Unsigned32"
_IbPmaSymbolErrCounter_Object = MibTableColumn
ibPmaSymbolErrCounter = _IbPmaSymbolErrCounter_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 1, 1, 1, 2),
    _IbPmaSymbolErrCounter_Type()
)
ibPmaSymbolErrCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaSymbolErrCounter.setStatus("current")


class _IbPmaLinkErrRecoveryCntr_Type(Unsigned32):
    """Custom type ibPmaLinkErrRecoveryCntr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaLinkErrRecoveryCntr_Type.__name__ = "Unsigned32"
_IbPmaLinkErrRecoveryCntr_Object = MibTableColumn
ibPmaLinkErrRecoveryCntr = _IbPmaLinkErrRecoveryCntr_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 1, 1, 1, 3),
    _IbPmaLinkErrRecoveryCntr_Type()
)
ibPmaLinkErrRecoveryCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaLinkErrRecoveryCntr.setStatus("current")


class _IbPmaLinkDownedCntr_Type(Unsigned32):
    """Custom type ibPmaLinkDownedCntr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaLinkDownedCntr_Type.__name__ = "Unsigned32"
_IbPmaLinkDownedCntr_Object = MibTableColumn
ibPmaLinkDownedCntr = _IbPmaLinkDownedCntr_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 1, 1, 1, 4),
    _IbPmaLinkDownedCntr_Type()
)
ibPmaLinkDownedCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaLinkDownedCntr.setStatus("current")


class _IbPmaPortRcvErr_Type(Unsigned32):
    """Custom type ibPmaPortRcvErr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortRcvErr_Type.__name__ = "Unsigned32"
_IbPmaPortRcvErr_Object = MibTableColumn
ibPmaPortRcvErr = _IbPmaPortRcvErr_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 1, 1, 1, 5),
    _IbPmaPortRcvErr_Type()
)
ibPmaPortRcvErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortRcvErr.setStatus("current")


class _IbPmaPortRcvRemPhysErr_Type(Unsigned32):
    """Custom type ibPmaPortRcvRemPhysErr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortRcvRemPhysErr_Type.__name__ = "Unsigned32"
_IbPmaPortRcvRemPhysErr_Object = MibTableColumn
ibPmaPortRcvRemPhysErr = _IbPmaPortRcvRemPhysErr_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 1, 1, 1, 6),
    _IbPmaPortRcvRemPhysErr_Type()
)
ibPmaPortRcvRemPhysErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortRcvRemPhysErr.setStatus("current")


class _IbPmaPortRcvSwitchRelayErr_Type(Unsigned32):
    """Custom type ibPmaPortRcvSwitchRelayErr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortRcvSwitchRelayErr_Type.__name__ = "Unsigned32"
_IbPmaPortRcvSwitchRelayErr_Object = MibTableColumn
ibPmaPortRcvSwitchRelayErr = _IbPmaPortRcvSwitchRelayErr_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 1, 1, 1, 7),
    _IbPmaPortRcvSwitchRelayErr_Type()
)
ibPmaPortRcvSwitchRelayErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortRcvSwitchRelayErr.setStatus("current")


class _IbPmaPortXmitDiscard_Type(Unsigned32):
    """Custom type ibPmaPortXmitDiscard based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortXmitDiscard_Type.__name__ = "Unsigned32"
_IbPmaPortXmitDiscard_Object = MibTableColumn
ibPmaPortXmitDiscard = _IbPmaPortXmitDiscard_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 1, 1, 1, 8),
    _IbPmaPortXmitDiscard_Type()
)
ibPmaPortXmitDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortXmitDiscard.setStatus("current")


class _IbPmaPortXmitConstraintErr_Type(Unsigned32):
    """Custom type ibPmaPortXmitConstraintErr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortXmitConstraintErr_Type.__name__ = "Unsigned32"
_IbPmaPortXmitConstraintErr_Object = MibTableColumn
ibPmaPortXmitConstraintErr = _IbPmaPortXmitConstraintErr_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 1, 1, 1, 9),
    _IbPmaPortXmitConstraintErr_Type()
)
ibPmaPortXmitConstraintErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortXmitConstraintErr.setStatus("current")


class _IbPmaPortRcvConstraintErr_Type(Unsigned32):
    """Custom type ibPmaPortRcvConstraintErr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortRcvConstraintErr_Type.__name__ = "Unsigned32"
_IbPmaPortRcvConstraintErr_Object = MibTableColumn
ibPmaPortRcvConstraintErr = _IbPmaPortRcvConstraintErr_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 1, 1, 1, 10),
    _IbPmaPortRcvConstraintErr_Type()
)
ibPmaPortRcvConstraintErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortRcvConstraintErr.setStatus("current")


class _IbPmaLocalLinkIntegrityErr_Type(Unsigned32):
    """Custom type ibPmaLocalLinkIntegrityErr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_IbPmaLocalLinkIntegrityErr_Type.__name__ = "Unsigned32"
_IbPmaLocalLinkIntegrityErr_Object = MibTableColumn
ibPmaLocalLinkIntegrityErr = _IbPmaLocalLinkIntegrityErr_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 1, 1, 1, 11),
    _IbPmaLocalLinkIntegrityErr_Type()
)
ibPmaLocalLinkIntegrityErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaLocalLinkIntegrityErr.setStatus("current")


class _IbPmaExcessBufOverrunErr_Type(Unsigned32):
    """Custom type ibPmaExcessBufOverrunErr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_IbPmaExcessBufOverrunErr_Type.__name__ = "Unsigned32"
_IbPmaExcessBufOverrunErr_Object = MibTableColumn
ibPmaExcessBufOverrunErr = _IbPmaExcessBufOverrunErr_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 1, 1, 1, 12),
    _IbPmaExcessBufOverrunErr_Type()
)
ibPmaExcessBufOverrunErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaExcessBufOverrunErr.setStatus("current")


class _IbPmaVl15Dropped_Type(Unsigned32):
    """Custom type ibPmaVl15Dropped based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaVl15Dropped_Type.__name__ = "Unsigned32"
_IbPmaVl15Dropped_Object = MibTableColumn
ibPmaVl15Dropped = _IbPmaVl15Dropped_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 1, 1, 1, 13),
    _IbPmaVl15Dropped_Type()
)
ibPmaVl15Dropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaVl15Dropped.setStatus("current")
_IbPmaPortCntrsOptTable_Object = MibTable
ibPmaPortCntrsOptTable = _IbPmaPortCntrsOptTable_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ibPmaPortCntrsOptTable.setStatus("current")
_IbPmaPortCntrsOptEntry_Object = MibTableRow
ibPmaPortCntrsOptEntry = _IbPmaPortCntrsOptEntry_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 1, 2, 1)
)
ibPmaPortCntrsOptEntry.setIndexNames(
    (0, "PMA-MIB", "ibPmaPortCntrsOptIndex"),
)
if mibBuilder.loadTexts:
    ibPmaPortCntrsOptEntry.setStatus("current")
_IbPmaPortCntrsOptIndex_Type = IbDataPort
_IbPmaPortCntrsOptIndex_Object = MibTableColumn
ibPmaPortCntrsOptIndex = _IbPmaPortCntrsOptIndex_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 1, 2, 1, 1),
    _IbPmaPortCntrsOptIndex_Type()
)
ibPmaPortCntrsOptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibPmaPortCntrsOptIndex.setStatus("current")


class _IbPmaPortXmitData_Type(Unsigned32):
    """Custom type ibPmaPortXmitData based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortXmitData_Type.__name__ = "Unsigned32"
_IbPmaPortXmitData_Object = MibTableColumn
ibPmaPortXmitData = _IbPmaPortXmitData_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 1, 2, 1, 2),
    _IbPmaPortXmitData_Type()
)
ibPmaPortXmitData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortXmitData.setStatus("current")


class _IbPmaPortRcvData_Type(Unsigned32):
    """Custom type ibPmaPortRcvData based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortRcvData_Type.__name__ = "Unsigned32"
_IbPmaPortRcvData_Object = MibTableColumn
ibPmaPortRcvData = _IbPmaPortRcvData_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 1, 2, 1, 3),
    _IbPmaPortRcvData_Type()
)
ibPmaPortRcvData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortRcvData.setStatus("current")


class _IbPmaPortXmitPkts_Type(Unsigned32):
    """Custom type ibPmaPortXmitPkts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortXmitPkts_Type.__name__ = "Unsigned32"
_IbPmaPortXmitPkts_Object = MibTableColumn
ibPmaPortXmitPkts = _IbPmaPortXmitPkts_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 1, 2, 1, 4),
    _IbPmaPortXmitPkts_Type()
)
ibPmaPortXmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortXmitPkts.setStatus("current")


class _IbPmaPortRcvPkts_Type(Unsigned32):
    """Custom type ibPmaPortRcvPkts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortRcvPkts_Type.__name__ = "Unsigned32"
_IbPmaPortRcvPkts_Object = MibTableColumn
ibPmaPortRcvPkts = _IbPmaPortRcvPkts_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 1, 2, 1, 5),
    _IbPmaPortRcvPkts_Type()
)
ibPmaPortRcvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortRcvPkts.setStatus("current")
_IbPmaPortXmitRecvInfo_ObjectIdentity = ObjectIdentity
ibPmaPortXmitRecvInfo = _IbPmaPortXmitRecvInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 6, 1, 2)
)
_IbPmaPortRcvErrTable_Object = MibTable
ibPmaPortRcvErrTable = _IbPmaPortRcvErrTable_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ibPmaPortRcvErrTable.setStatus("current")
_IbPmaPortRcvErrEntry_Object = MibTableRow
ibPmaPortRcvErrEntry = _IbPmaPortRcvErrEntry_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 2, 1, 1)
)
ibPmaPortRcvErrEntry.setIndexNames(
    (0, "PMA-MIB", "ibPmaPortRcvErrIndex"),
)
if mibBuilder.loadTexts:
    ibPmaPortRcvErrEntry.setStatus("current")
_IbPmaPortRcvErrIndex_Type = IbDataPort
_IbPmaPortRcvErrIndex_Object = MibTableColumn
ibPmaPortRcvErrIndex = _IbPmaPortRcvErrIndex_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 2, 1, 1, 1),
    _IbPmaPortRcvErrIndex_Type()
)
ibPmaPortRcvErrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibPmaPortRcvErrIndex.setStatus("current")


class _IbPmaPortRcvErrLocalPhysErrs_Type(Unsigned32):
    """Custom type ibPmaPortRcvErrLocalPhysErrs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortRcvErrLocalPhysErrs_Type.__name__ = "Unsigned32"
_IbPmaPortRcvErrLocalPhysErrs_Object = MibTableColumn
ibPmaPortRcvErrLocalPhysErrs = _IbPmaPortRcvErrLocalPhysErrs_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 2, 1, 1, 2),
    _IbPmaPortRcvErrLocalPhysErrs_Type()
)
ibPmaPortRcvErrLocalPhysErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortRcvErrLocalPhysErrs.setStatus("current")


class _IbPmaPortMalformedPacketErrs_Type(Unsigned32):
    """Custom type ibPmaPortMalformedPacketErrs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortMalformedPacketErrs_Type.__name__ = "Unsigned32"
_IbPmaPortMalformedPacketErrs_Object = MibTableColumn
ibPmaPortMalformedPacketErrs = _IbPmaPortMalformedPacketErrs_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 2, 1, 1, 3),
    _IbPmaPortMalformedPacketErrs_Type()
)
ibPmaPortMalformedPacketErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortMalformedPacketErrs.setStatus("current")


class _IbPmaPortBufferOverrunErrs_Type(Unsigned32):
    """Custom type ibPmaPortBufferOverrunErrs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortBufferOverrunErrs_Type.__name__ = "Unsigned32"
_IbPmaPortBufferOverrunErrs_Object = MibTableColumn
ibPmaPortBufferOverrunErrs = _IbPmaPortBufferOverrunErrs_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 2, 1, 1, 4),
    _IbPmaPortBufferOverrunErrs_Type()
)
ibPmaPortBufferOverrunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortBufferOverrunErrs.setStatus("current")


class _IbPmaPortDLIDMappingErrs_Type(Unsigned32):
    """Custom type ibPmaPortDLIDMappingErrs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortDLIDMappingErrs_Type.__name__ = "Unsigned32"
_IbPmaPortDLIDMappingErrs_Object = MibTableColumn
ibPmaPortDLIDMappingErrs = _IbPmaPortDLIDMappingErrs_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 2, 1, 1, 5),
    _IbPmaPortDLIDMappingErrs_Type()
)
ibPmaPortDLIDMappingErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortDLIDMappingErrs.setStatus("current")


class _IbPmaPortVLMappingErrs_Type(Unsigned32):
    """Custom type ibPmaPortVLMappingErrs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortVLMappingErrs_Type.__name__ = "Unsigned32"
_IbPmaPortVLMappingErrs_Object = MibTableColumn
ibPmaPortVLMappingErrs = _IbPmaPortVLMappingErrs_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 2, 1, 1, 6),
    _IbPmaPortVLMappingErrs_Type()
)
ibPmaPortVLMappingErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVLMappingErrs.setStatus("current")


class _IbPmaPortLoopingErrs_Type(Unsigned32):
    """Custom type ibPmaPortLoopingErrs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortLoopingErrs_Type.__name__ = "Unsigned32"
_IbPmaPortLoopingErrs_Object = MibTableColumn
ibPmaPortLoopingErrs = _IbPmaPortLoopingErrs_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 2, 1, 1, 7),
    _IbPmaPortLoopingErrs_Type()
)
ibPmaPortLoopingErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortLoopingErrs.setStatus("current")
_IbPmaPortXmitDiscardTable_Object = MibTable
ibPmaPortXmitDiscardTable = _IbPmaPortXmitDiscardTable_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ibPmaPortXmitDiscardTable.setStatus("current")
_IbPmaPortXmitDiscardEntry_Object = MibTableRow
ibPmaPortXmitDiscardEntry = _IbPmaPortXmitDiscardEntry_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 2, 2, 1)
)
ibPmaPortXmitDiscardEntry.setIndexNames(
    (0, "PMA-MIB", "ibPmaPortXmitDiscardIndex"),
)
if mibBuilder.loadTexts:
    ibPmaPortXmitDiscardEntry.setStatus("current")
_IbPmaPortXmitDiscardIndex_Type = IbDataPort
_IbPmaPortXmitDiscardIndex_Object = MibTableColumn
ibPmaPortXmitDiscardIndex = _IbPmaPortXmitDiscardIndex_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 2, 2, 1, 1),
    _IbPmaPortXmitDiscardIndex_Type()
)
ibPmaPortXmitDiscardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibPmaPortXmitDiscardIndex.setStatus("current")


class _IbPmaPortInactiveDiscards_Type(Unsigned32):
    """Custom type ibPmaPortInactiveDiscards based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortInactiveDiscards_Type.__name__ = "Unsigned32"
_IbPmaPortInactiveDiscards_Object = MibTableColumn
ibPmaPortInactiveDiscards = _IbPmaPortInactiveDiscards_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 2, 2, 1, 2),
    _IbPmaPortInactiveDiscards_Type()
)
ibPmaPortInactiveDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortInactiveDiscards.setStatus("current")


class _IbPmaPortNeighborMtuDiscards_Type(Unsigned32):
    """Custom type ibPmaPortNeighborMtuDiscards based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortNeighborMtuDiscards_Type.__name__ = "Unsigned32"
_IbPmaPortNeighborMtuDiscards_Object = MibTableColumn
ibPmaPortNeighborMtuDiscards = _IbPmaPortNeighborMtuDiscards_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 2, 2, 1, 3),
    _IbPmaPortNeighborMtuDiscards_Type()
)
ibPmaPortNeighborMtuDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortNeighborMtuDiscards.setStatus("current")


class _IbPmaPortSwLifetimeLimitDiscards_Type(Unsigned32):
    """Custom type ibPmaPortSwLifetimeLimitDiscards based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortSwLifetimeLimitDiscards_Type.__name__ = "Unsigned32"
_IbPmaPortSwLifetimeLimitDiscards_Object = MibTableColumn
ibPmaPortSwLifetimeLimitDiscards = _IbPmaPortSwLifetimeLimitDiscards_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 2, 2, 1, 4),
    _IbPmaPortSwLifetimeLimitDiscards_Type()
)
ibPmaPortSwLifetimeLimitDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortSwLifetimeLimitDiscards.setStatus("current")


class _IbPmaPortSwHoqLimitDiscards_Type(Unsigned32):
    """Custom type ibPmaPortSwHoqLimitDiscards based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortSwHoqLimitDiscards_Type.__name__ = "Unsigned32"
_IbPmaPortSwHoqLimitDiscards_Object = MibTableColumn
ibPmaPortSwHoqLimitDiscards = _IbPmaPortSwHoqLimitDiscards_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 2, 2, 1, 5),
    _IbPmaPortSwHoqLimitDiscards_Type()
)
ibPmaPortSwHoqLimitDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortSwHoqLimitDiscards.setStatus("current")
_IbPmaPortFlowCtlCntrsTable_Object = MibTable
ibPmaPortFlowCtlCntrsTable = _IbPmaPortFlowCtlCntrsTable_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ibPmaPortFlowCtlCntrsTable.setStatus("current")
_IbPmaPortFlowCtlCntrsEntry_Object = MibTableRow
ibPmaPortFlowCtlCntrsEntry = _IbPmaPortFlowCtlCntrsEntry_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 2, 3, 1)
)
ibPmaPortFlowCtlCntrsEntry.setIndexNames(
    (0, "PMA-MIB", "ibPmaPortFlowCtlCntrsIndex"),
)
if mibBuilder.loadTexts:
    ibPmaPortFlowCtlCntrsEntry.setStatus("current")
_IbPmaPortFlowCtlCntrsIndex_Type = IbDataPort
_IbPmaPortFlowCtlCntrsIndex_Object = MibTableColumn
ibPmaPortFlowCtlCntrsIndex = _IbPmaPortFlowCtlCntrsIndex_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 2, 3, 1, 1),
    _IbPmaPortFlowCtlCntrsIndex_Type()
)
ibPmaPortFlowCtlCntrsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibPmaPortFlowCtlCntrsIndex.setStatus("current")


class _IbPmaPortFlowCtlXmitFlowPkts_Type(Unsigned32):
    """Custom type ibPmaPortFlowCtlXmitFlowPkts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortFlowCtlXmitFlowPkts_Type.__name__ = "Unsigned32"
_IbPmaPortFlowCtlXmitFlowPkts_Object = MibTableColumn
ibPmaPortFlowCtlXmitFlowPkts = _IbPmaPortFlowCtlXmitFlowPkts_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 2, 3, 1, 2),
    _IbPmaPortFlowCtlXmitFlowPkts_Type()
)
ibPmaPortFlowCtlXmitFlowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortFlowCtlXmitFlowPkts.setStatus("current")


class _IbPmaPortFlowCtlRcvFlowPkts_Type(Unsigned32):
    """Custom type ibPmaPortFlowCtlRcvFlowPkts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortFlowCtlRcvFlowPkts_Type.__name__ = "Unsigned32"
_IbPmaPortFlowCtlRcvFlowPkts_Object = MibTableColumn
ibPmaPortFlowCtlRcvFlowPkts = _IbPmaPortFlowCtlRcvFlowPkts_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 2, 3, 1, 3),
    _IbPmaPortFlowCtlRcvFlowPkts_Type()
)
ibPmaPortFlowCtlRcvFlowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortFlowCtlRcvFlowPkts.setStatus("current")
_IbPmaPortOpCodeInfo_ObjectIdentity = ObjectIdentity
ibPmaPortOpCodeInfo = _IbPmaPortOpCodeInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 6, 1, 3)
)
_IbPmaPortOpCodeRcvCntrsTable_Object = MibTable
ibPmaPortOpCodeRcvCntrsTable = _IbPmaPortOpCodeRcvCntrsTable_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ibPmaPortOpCodeRcvCntrsTable.setStatus("current")
_IbPmaPortOpCodeRcvCntrsEntry_Object = MibTableRow
ibPmaPortOpCodeRcvCntrsEntry = _IbPmaPortOpCodeRcvCntrsEntry_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 1, 1)
)
ibPmaPortOpCodeRcvCntrsEntry.setIndexNames(
    (0, "PMA-MIB", "ibPmaPortOpCodeRcvCntrsPortIndex"),
    (0, "PMA-MIB", "ibPmaPortOpCodeRcvCntrsIndex"),
)
if mibBuilder.loadTexts:
    ibPmaPortOpCodeRcvCntrsEntry.setStatus("current")
_IbPmaPortOpCodeRcvCntrsPortIndex_Type = IbDataPort
_IbPmaPortOpCodeRcvCntrsPortIndex_Object = MibTableColumn
ibPmaPortOpCodeRcvCntrsPortIndex = _IbPmaPortOpCodeRcvCntrsPortIndex_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 1, 1, 1),
    _IbPmaPortOpCodeRcvCntrsPortIndex_Type()
)
ibPmaPortOpCodeRcvCntrsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibPmaPortOpCodeRcvCntrsPortIndex.setStatus("current")


class _IbPmaPortOpCodeRcvCntrsIndex_Type(Unsigned32):
    """Custom type ibPmaPortOpCodeRcvCntrsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IbPmaPortOpCodeRcvCntrsIndex_Type.__name__ = "Unsigned32"
_IbPmaPortOpCodeRcvCntrsIndex_Object = MibTableColumn
ibPmaPortOpCodeRcvCntrsIndex = _IbPmaPortOpCodeRcvCntrsIndex_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 1, 1, 2),
    _IbPmaPortOpCodeRcvCntrsIndex_Type()
)
ibPmaPortOpCodeRcvCntrsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibPmaPortOpCodeRcvCntrsIndex.setStatus("current")
_IbPmaPortOpCodeRcvCntrsRcvPkts_Type = Counter32
_IbPmaPortOpCodeRcvCntrsRcvPkts_Object = MibTableColumn
ibPmaPortOpCodeRcvCntrsRcvPkts = _IbPmaPortOpCodeRcvCntrsRcvPkts_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 1, 1, 3),
    _IbPmaPortOpCodeRcvCntrsRcvPkts_Type()
)
ibPmaPortOpCodeRcvCntrsRcvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortOpCodeRcvCntrsRcvPkts.setStatus("current")
_IbPmaPortOpCodeRcvCntrsRcvData_Type = Counter32
_IbPmaPortOpCodeRcvCntrsRcvData_Object = MibTableColumn
ibPmaPortOpCodeRcvCntrsRcvData = _IbPmaPortOpCodeRcvCntrsRcvData_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 1, 1, 4),
    _IbPmaPortOpCodeRcvCntrsRcvData_Type()
)
ibPmaPortOpCodeRcvCntrsRcvData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortOpCodeRcvCntrsRcvData.setStatus("current")
_IbPmaPortOpCodeVlCntrsTable_Object = MibTable
ibPmaPortOpCodeVlCntrsTable = _IbPmaPortOpCodeVlCntrsTable_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ibPmaPortOpCodeVlCntrsTable.setStatus("current")
_IbPmaPortOpCodeVlCntrsEntry_Object = MibTableRow
ibPmaPortOpCodeVlCntrsEntry = _IbPmaPortOpCodeVlCntrsEntry_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 2, 1)
)
ibPmaPortOpCodeVlCntrsEntry.setIndexNames(
    (0, "PMA-MIB", "ibPmaPortOpCodeVlCntrsPortIndex"),
    (0, "PMA-MIB", "ibPmaPortOpCodeVlCntrsIndex"),
)
if mibBuilder.loadTexts:
    ibPmaPortOpCodeVlCntrsEntry.setStatus("current")
_IbPmaPortOpCodeVlCntrsPortIndex_Type = IbDataPort
_IbPmaPortOpCodeVlCntrsPortIndex_Object = MibTableColumn
ibPmaPortOpCodeVlCntrsPortIndex = _IbPmaPortOpCodeVlCntrsPortIndex_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 2, 1, 1),
    _IbPmaPortOpCodeVlCntrsPortIndex_Type()
)
ibPmaPortOpCodeVlCntrsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibPmaPortOpCodeVlCntrsPortIndex.setStatus("current")


class _IbPmaPortOpCodeVlCntrsIndex_Type(Unsigned32):
    """Custom type ibPmaPortOpCodeVlCntrsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IbPmaPortOpCodeVlCntrsIndex_Type.__name__ = "Unsigned32"
_IbPmaPortOpCodeVlCntrsIndex_Object = MibTableColumn
ibPmaPortOpCodeVlCntrsIndex = _IbPmaPortOpCodeVlCntrsIndex_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 2, 1, 2),
    _IbPmaPortOpCodeVlCntrsIndex_Type()
)
ibPmaPortOpCodeVlCntrsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibPmaPortOpCodeVlCntrsIndex.setStatus("current")


class _IbPmaPortVlOpPkt0_Type(Unsigned32):
    """Custom type ibPmaPortVlOpPkt0 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortVlOpPkt0_Type.__name__ = "Unsigned32"
_IbPmaPortVlOpPkt0_Object = MibTableColumn
ibPmaPortVlOpPkt0 = _IbPmaPortVlOpPkt0_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 2, 1, 3),
    _IbPmaPortVlOpPkt0_Type()
)
ibPmaPortVlOpPkt0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpPkt0.setStatus("current")


class _IbPmaPortVlOpPkt1_Type(Unsigned32):
    """Custom type ibPmaPortVlOpPkt1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortVlOpPkt1_Type.__name__ = "Unsigned32"
_IbPmaPortVlOpPkt1_Object = MibTableColumn
ibPmaPortVlOpPkt1 = _IbPmaPortVlOpPkt1_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 2, 1, 4),
    _IbPmaPortVlOpPkt1_Type()
)
ibPmaPortVlOpPkt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpPkt1.setStatus("current")


class _IbPmaPortVlOpPkt2_Type(Unsigned32):
    """Custom type ibPmaPortVlOpPkt2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortVlOpPkt2_Type.__name__ = "Unsigned32"
_IbPmaPortVlOpPkt2_Object = MibTableColumn
ibPmaPortVlOpPkt2 = _IbPmaPortVlOpPkt2_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 2, 1, 5),
    _IbPmaPortVlOpPkt2_Type()
)
ibPmaPortVlOpPkt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpPkt2.setStatus("current")


class _IbPmaPortVlOpPkt3_Type(Unsigned32):
    """Custom type ibPmaPortVlOpPkt3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortVlOpPkt3_Type.__name__ = "Unsigned32"
_IbPmaPortVlOpPkt3_Object = MibTableColumn
ibPmaPortVlOpPkt3 = _IbPmaPortVlOpPkt3_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 2, 1, 6),
    _IbPmaPortVlOpPkt3_Type()
)
ibPmaPortVlOpPkt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpPkt3.setStatus("current")


class _IbPmaPortVlOpPkt4_Type(Unsigned32):
    """Custom type ibPmaPortVlOpPkt4 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortVlOpPkt4_Type.__name__ = "Unsigned32"
_IbPmaPortVlOpPkt4_Object = MibTableColumn
ibPmaPortVlOpPkt4 = _IbPmaPortVlOpPkt4_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 2, 1, 7),
    _IbPmaPortVlOpPkt4_Type()
)
ibPmaPortVlOpPkt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpPkt4.setStatus("current")


class _IbPmaPortVlOpPkt5_Type(Unsigned32):
    """Custom type ibPmaPortVlOpPkt5 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortVlOpPkt5_Type.__name__ = "Unsigned32"
_IbPmaPortVlOpPkt5_Object = MibTableColumn
ibPmaPortVlOpPkt5 = _IbPmaPortVlOpPkt5_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 2, 1, 8),
    _IbPmaPortVlOpPkt5_Type()
)
ibPmaPortVlOpPkt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpPkt5.setStatus("current")


class _IbPmaPortVlOpPkt6_Type(Unsigned32):
    """Custom type ibPmaPortVlOpPkt6 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortVlOpPkt6_Type.__name__ = "Unsigned32"
_IbPmaPortVlOpPkt6_Object = MibTableColumn
ibPmaPortVlOpPkt6 = _IbPmaPortVlOpPkt6_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 2, 1, 9),
    _IbPmaPortVlOpPkt6_Type()
)
ibPmaPortVlOpPkt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpPkt6.setStatus("current")


class _IbPmaPortVlOpPkt7_Type(Unsigned32):
    """Custom type ibPmaPortVlOpPkt7 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortVlOpPkt7_Type.__name__ = "Unsigned32"
_IbPmaPortVlOpPkt7_Object = MibTableColumn
ibPmaPortVlOpPkt7 = _IbPmaPortVlOpPkt7_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 2, 1, 10),
    _IbPmaPortVlOpPkt7_Type()
)
ibPmaPortVlOpPkt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpPkt7.setStatus("current")


class _IbPmaPortVlOpPkt8_Type(Unsigned32):
    """Custom type ibPmaPortVlOpPkt8 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortVlOpPkt8_Type.__name__ = "Unsigned32"
_IbPmaPortVlOpPkt8_Object = MibTableColumn
ibPmaPortVlOpPkt8 = _IbPmaPortVlOpPkt8_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 2, 1, 11),
    _IbPmaPortVlOpPkt8_Type()
)
ibPmaPortVlOpPkt8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpPkt8.setStatus("current")


class _IbPmaPortVlOpPkt9_Type(Unsigned32):
    """Custom type ibPmaPortVlOpPkt9 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortVlOpPkt9_Type.__name__ = "Unsigned32"
_IbPmaPortVlOpPkt9_Object = MibTableColumn
ibPmaPortVlOpPkt9 = _IbPmaPortVlOpPkt9_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 2, 1, 12),
    _IbPmaPortVlOpPkt9_Type()
)
ibPmaPortVlOpPkt9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpPkt9.setStatus("current")


class _IbPmaPortVlOpPkt10_Type(Unsigned32):
    """Custom type ibPmaPortVlOpPkt10 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortVlOpPkt10_Type.__name__ = "Unsigned32"
_IbPmaPortVlOpPkt10_Object = MibTableColumn
ibPmaPortVlOpPkt10 = _IbPmaPortVlOpPkt10_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 2, 1, 13),
    _IbPmaPortVlOpPkt10_Type()
)
ibPmaPortVlOpPkt10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpPkt10.setStatus("current")


class _IbPmaPortVlOpPkt11_Type(Unsigned32):
    """Custom type ibPmaPortVlOpPkt11 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortVlOpPkt11_Type.__name__ = "Unsigned32"
_IbPmaPortVlOpPkt11_Object = MibTableColumn
ibPmaPortVlOpPkt11 = _IbPmaPortVlOpPkt11_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 2, 1, 14),
    _IbPmaPortVlOpPkt11_Type()
)
ibPmaPortVlOpPkt11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpPkt11.setStatus("current")


class _IbPmaPortVlOpPkt12_Type(Unsigned32):
    """Custom type ibPmaPortVlOpPkt12 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortVlOpPkt12_Type.__name__ = "Unsigned32"
_IbPmaPortVlOpPkt12_Object = MibTableColumn
ibPmaPortVlOpPkt12 = _IbPmaPortVlOpPkt12_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 2, 1, 15),
    _IbPmaPortVlOpPkt12_Type()
)
ibPmaPortVlOpPkt12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpPkt12.setStatus("current")


class _IbPmaPortVlOpPkt13_Type(Unsigned32):
    """Custom type ibPmaPortVlOpPkt13 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortVlOpPkt13_Type.__name__ = "Unsigned32"
_IbPmaPortVlOpPkt13_Object = MibTableColumn
ibPmaPortVlOpPkt13 = _IbPmaPortVlOpPkt13_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 2, 1, 16),
    _IbPmaPortVlOpPkt13_Type()
)
ibPmaPortVlOpPkt13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpPkt13.setStatus("current")


class _IbPmaPortVlOpPkt14_Type(Unsigned32):
    """Custom type ibPmaPortVlOpPkt14 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortVlOpPkt14_Type.__name__ = "Unsigned32"
_IbPmaPortVlOpPkt14_Object = MibTableColumn
ibPmaPortVlOpPkt14 = _IbPmaPortVlOpPkt14_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 2, 1, 17),
    _IbPmaPortVlOpPkt14_Type()
)
ibPmaPortVlOpPkt14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpPkt14.setStatus("current")


class _IbPmaPortVlOpPkt15_Type(Unsigned32):
    """Custom type ibPmaPortVlOpPkt15 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbPmaPortVlOpPkt15_Type.__name__ = "Unsigned32"
_IbPmaPortVlOpPkt15_Object = MibTableColumn
ibPmaPortVlOpPkt15 = _IbPmaPortVlOpPkt15_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 2, 1, 18),
    _IbPmaPortVlOpPkt15_Type()
)
ibPmaPortVlOpPkt15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpPkt15.setStatus("current")
_IbPmaPortOpCodeVlDataCntrsTable_Object = MibTable
ibPmaPortOpCodeVlDataCntrsTable = _IbPmaPortOpCodeVlDataCntrsTable_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ibPmaPortOpCodeVlDataCntrsTable.setStatus("current")
_IbPmaPortOpCodeVlDataCntrsEntry_Object = MibTableRow
ibPmaPortOpCodeVlDataCntrsEntry = _IbPmaPortOpCodeVlDataCntrsEntry_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 3, 1)
)
ibPmaPortOpCodeVlDataCntrsEntry.setIndexNames(
    (0, "PMA-MIB", "ibPmaPortOpCodeVlDataPortIndex"),
    (0, "PMA-MIB", "ibPmaPortOpCodeVlDataIndex"),
)
if mibBuilder.loadTexts:
    ibPmaPortOpCodeVlDataCntrsEntry.setStatus("current")
_IbPmaPortOpCodeVlDataPortIndex_Type = IbDataPort
_IbPmaPortOpCodeVlDataPortIndex_Object = MibTableColumn
ibPmaPortOpCodeVlDataPortIndex = _IbPmaPortOpCodeVlDataPortIndex_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 3, 1, 1),
    _IbPmaPortOpCodeVlDataPortIndex_Type()
)
ibPmaPortOpCodeVlDataPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibPmaPortOpCodeVlDataPortIndex.setStatus("current")


class _IbPmaPortOpCodeVlDataIndex_Type(Unsigned32):
    """Custom type ibPmaPortOpCodeVlDataIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IbPmaPortOpCodeVlDataIndex_Type.__name__ = "Unsigned32"
_IbPmaPortOpCodeVlDataIndex_Object = MibTableColumn
ibPmaPortOpCodeVlDataIndex = _IbPmaPortOpCodeVlDataIndex_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 3, 1, 2),
    _IbPmaPortOpCodeVlDataIndex_Type()
)
ibPmaPortOpCodeVlDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibPmaPortOpCodeVlDataIndex.setStatus("current")
_IbPmaPortVlOpData0_Type = Counter32
_IbPmaPortVlOpData0_Object = MibTableColumn
ibPmaPortVlOpData0 = _IbPmaPortVlOpData0_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 3, 1, 3),
    _IbPmaPortVlOpData0_Type()
)
ibPmaPortVlOpData0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpData0.setStatus("current")
_IbPmaPortVlOpData1_Type = Counter32
_IbPmaPortVlOpData1_Object = MibTableColumn
ibPmaPortVlOpData1 = _IbPmaPortVlOpData1_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 3, 1, 4),
    _IbPmaPortVlOpData1_Type()
)
ibPmaPortVlOpData1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpData1.setStatus("current")
_IbPmaPortVlOpData2_Type = Counter32
_IbPmaPortVlOpData2_Object = MibTableColumn
ibPmaPortVlOpData2 = _IbPmaPortVlOpData2_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 3, 1, 5),
    _IbPmaPortVlOpData2_Type()
)
ibPmaPortVlOpData2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpData2.setStatus("current")
_IbPmaPortVlOpData3_Type = Counter32
_IbPmaPortVlOpData3_Object = MibTableColumn
ibPmaPortVlOpData3 = _IbPmaPortVlOpData3_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 3, 1, 6),
    _IbPmaPortVlOpData3_Type()
)
ibPmaPortVlOpData3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpData3.setStatus("current")
_IbPmaPortVlOpData4_Type = Counter32
_IbPmaPortVlOpData4_Object = MibTableColumn
ibPmaPortVlOpData4 = _IbPmaPortVlOpData4_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 3, 1, 7),
    _IbPmaPortVlOpData4_Type()
)
ibPmaPortVlOpData4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpData4.setStatus("current")
_IbPmaPortVlOpData5_Type = Counter32
_IbPmaPortVlOpData5_Object = MibTableColumn
ibPmaPortVlOpData5 = _IbPmaPortVlOpData5_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 3, 1, 8),
    _IbPmaPortVlOpData5_Type()
)
ibPmaPortVlOpData5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpData5.setStatus("current")
_IbPmaPortVlOpData6_Type = Counter32
_IbPmaPortVlOpData6_Object = MibTableColumn
ibPmaPortVlOpData6 = _IbPmaPortVlOpData6_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 3, 1, 9),
    _IbPmaPortVlOpData6_Type()
)
ibPmaPortVlOpData6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpData6.setStatus("current")
_IbPmaPortVlOpData7_Type = Counter32
_IbPmaPortVlOpData7_Object = MibTableColumn
ibPmaPortVlOpData7 = _IbPmaPortVlOpData7_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 3, 1, 10),
    _IbPmaPortVlOpData7_Type()
)
ibPmaPortVlOpData7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpData7.setStatus("current")
_IbPmaPortVlOpData8_Type = Counter32
_IbPmaPortVlOpData8_Object = MibTableColumn
ibPmaPortVlOpData8 = _IbPmaPortVlOpData8_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 3, 1, 11),
    _IbPmaPortVlOpData8_Type()
)
ibPmaPortVlOpData8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpData8.setStatus("current")
_IbPmaPortVlOpData9_Type = Counter32
_IbPmaPortVlOpData9_Object = MibTableColumn
ibPmaPortVlOpData9 = _IbPmaPortVlOpData9_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 3, 1, 12),
    _IbPmaPortVlOpData9_Type()
)
ibPmaPortVlOpData9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpData9.setStatus("current")
_IbPmaPortVlOpData10_Type = Counter32
_IbPmaPortVlOpData10_Object = MibTableColumn
ibPmaPortVlOpData10 = _IbPmaPortVlOpData10_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 3, 1, 13),
    _IbPmaPortVlOpData10_Type()
)
ibPmaPortVlOpData10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpData10.setStatus("current")
_IbPmaPortVlOpData11_Type = Counter32
_IbPmaPortVlOpData11_Object = MibTableColumn
ibPmaPortVlOpData11 = _IbPmaPortVlOpData11_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 3, 1, 14),
    _IbPmaPortVlOpData11_Type()
)
ibPmaPortVlOpData11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpData11.setStatus("current")
_IbPmaPortVlOpData12_Type = Counter32
_IbPmaPortVlOpData12_Object = MibTableColumn
ibPmaPortVlOpData12 = _IbPmaPortVlOpData12_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 3, 1, 15),
    _IbPmaPortVlOpData12_Type()
)
ibPmaPortVlOpData12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpData12.setStatus("current")
_IbPmaPortVlOpData13_Type = Counter32
_IbPmaPortVlOpData13_Object = MibTableColumn
ibPmaPortVlOpData13 = _IbPmaPortVlOpData13_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 3, 1, 16),
    _IbPmaPortVlOpData13_Type()
)
ibPmaPortVlOpData13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpData13.setStatus("current")
_IbPmaPortVlOpData14_Type = Counter32
_IbPmaPortVlOpData14_Object = MibTableColumn
ibPmaPortVlOpData14 = _IbPmaPortVlOpData14_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 3, 1, 17),
    _IbPmaPortVlOpData14_Type()
)
ibPmaPortVlOpData14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpData14.setStatus("current")
_IbPmaPortVlOpData15_Type = Counter32
_IbPmaPortVlOpData15_Object = MibTableColumn
ibPmaPortVlOpData15 = _IbPmaPortVlOpData15_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 3, 3, 1, 18),
    _IbPmaPortVlOpData15_Type()
)
ibPmaPortVlOpData15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlOpData15.setStatus("current")
_IbPmaPortVlInfo_ObjectIdentity = ObjectIdentity
ibPmaPortVlInfo = _IbPmaPortVlInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 6, 1, 4)
)
_IbPmaPortVlXmitFCUpErrTable_Object = MibTable
ibPmaPortVlXmitFCUpErrTable = _IbPmaPortVlXmitFCUpErrTable_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ibPmaPortVlXmitFCUpErrTable.setStatus("current")
_IbPmaPortVlXmitFCUpErrEntry_Object = MibTableRow
ibPmaPortVlXmitFCUpErrEntry = _IbPmaPortVlXmitFCUpErrEntry_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 1, 1)
)
ibPmaPortVlXmitFCUpErrEntry.setIndexNames(
    (0, "PMA-MIB", "ibPmaPortVlXmitFCUpErrPortIndex"),
)
if mibBuilder.loadTexts:
    ibPmaPortVlXmitFCUpErrEntry.setStatus("current")
_IbPmaPortVlXmitFCUpErrPortIndex_Type = IbDataPort
_IbPmaPortVlXmitFCUpErrPortIndex_Object = MibTableColumn
ibPmaPortVlXmitFCUpErrPortIndex = _IbPmaPortVlXmitFCUpErrPortIndex_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 1, 1, 1),
    _IbPmaPortVlXmitFCUpErrPortIndex_Type()
)
ibPmaPortVlXmitFCUpErrPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitFCUpErrPortIndex.setStatus("current")


class _IbPmaPortVlXmitFCUpErr0_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitFCUpErr0 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitFCUpErr0_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitFCUpErr0_Object = MibTableColumn
ibPmaPortVlXmitFCUpErr0 = _IbPmaPortVlXmitFCUpErr0_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 1, 1, 2),
    _IbPmaPortVlXmitFCUpErr0_Type()
)
ibPmaPortVlXmitFCUpErr0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitFCUpErr0.setStatus("current")


class _IbPmaPortVlXmitFCUpErr1_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitFCUpErr1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitFCUpErr1_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitFCUpErr1_Object = MibTableColumn
ibPmaPortVlXmitFCUpErr1 = _IbPmaPortVlXmitFCUpErr1_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 1, 1, 3),
    _IbPmaPortVlXmitFCUpErr1_Type()
)
ibPmaPortVlXmitFCUpErr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitFCUpErr1.setStatus("current")


class _IbPmaPortVlXmitFCUpErr2_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitFCUpErr2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitFCUpErr2_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitFCUpErr2_Object = MibTableColumn
ibPmaPortVlXmitFCUpErr2 = _IbPmaPortVlXmitFCUpErr2_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 1, 1, 4),
    _IbPmaPortVlXmitFCUpErr2_Type()
)
ibPmaPortVlXmitFCUpErr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitFCUpErr2.setStatus("current")


class _IbPmaPortVlXmitFCUpErr3_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitFCUpErr3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitFCUpErr3_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitFCUpErr3_Object = MibTableColumn
ibPmaPortVlXmitFCUpErr3 = _IbPmaPortVlXmitFCUpErr3_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 1, 1, 5),
    _IbPmaPortVlXmitFCUpErr3_Type()
)
ibPmaPortVlXmitFCUpErr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitFCUpErr3.setStatus("current")


class _IbPmaPortVlXmitFCUpErr4_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitFCUpErr4 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitFCUpErr4_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitFCUpErr4_Object = MibTableColumn
ibPmaPortVlXmitFCUpErr4 = _IbPmaPortVlXmitFCUpErr4_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 1, 1, 6),
    _IbPmaPortVlXmitFCUpErr4_Type()
)
ibPmaPortVlXmitFCUpErr4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitFCUpErr4.setStatus("current")


class _IbPmaPortVlXmitFCUpErr5_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitFCUpErr5 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitFCUpErr5_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitFCUpErr5_Object = MibTableColumn
ibPmaPortVlXmitFCUpErr5 = _IbPmaPortVlXmitFCUpErr5_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 1, 1, 7),
    _IbPmaPortVlXmitFCUpErr5_Type()
)
ibPmaPortVlXmitFCUpErr5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitFCUpErr5.setStatus("current")


class _IbPmaPortVlXmitFCUpErr6_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitFCUpErr6 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitFCUpErr6_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitFCUpErr6_Object = MibTableColumn
ibPmaPortVlXmitFCUpErr6 = _IbPmaPortVlXmitFCUpErr6_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 1, 1, 8),
    _IbPmaPortVlXmitFCUpErr6_Type()
)
ibPmaPortVlXmitFCUpErr6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitFCUpErr6.setStatus("current")


class _IbPmaPortVlXmitFCUpErr7_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitFCUpErr7 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitFCUpErr7_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitFCUpErr7_Object = MibTableColumn
ibPmaPortVlXmitFCUpErr7 = _IbPmaPortVlXmitFCUpErr7_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 1, 1, 9),
    _IbPmaPortVlXmitFCUpErr7_Type()
)
ibPmaPortVlXmitFCUpErr7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitFCUpErr7.setStatus("current")


class _IbPmaPortVlXmitFCUpErr8_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitFCUpErr8 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitFCUpErr8_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitFCUpErr8_Object = MibTableColumn
ibPmaPortVlXmitFCUpErr8 = _IbPmaPortVlXmitFCUpErr8_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 1, 1, 10),
    _IbPmaPortVlXmitFCUpErr8_Type()
)
ibPmaPortVlXmitFCUpErr8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitFCUpErr8.setStatus("current")


class _IbPmaPortVlXmitFCUpErr9_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitFCUpErr9 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitFCUpErr9_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitFCUpErr9_Object = MibTableColumn
ibPmaPortVlXmitFCUpErr9 = _IbPmaPortVlXmitFCUpErr9_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 1, 1, 11),
    _IbPmaPortVlXmitFCUpErr9_Type()
)
ibPmaPortVlXmitFCUpErr9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitFCUpErr9.setStatus("current")


class _IbPmaPortVlXmitFCUpErr10_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitFCUpErr10 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitFCUpErr10_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitFCUpErr10_Object = MibTableColumn
ibPmaPortVlXmitFCUpErr10 = _IbPmaPortVlXmitFCUpErr10_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 1, 1, 12),
    _IbPmaPortVlXmitFCUpErr10_Type()
)
ibPmaPortVlXmitFCUpErr10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitFCUpErr10.setStatus("current")


class _IbPmaPortVlXmitFCUpErr11_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitFCUpErr11 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitFCUpErr11_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitFCUpErr11_Object = MibTableColumn
ibPmaPortVlXmitFCUpErr11 = _IbPmaPortVlXmitFCUpErr11_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 1, 1, 13),
    _IbPmaPortVlXmitFCUpErr11_Type()
)
ibPmaPortVlXmitFCUpErr11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitFCUpErr11.setStatus("current")


class _IbPmaPortVlXmitFCUpErr12_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitFCUpErr12 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitFCUpErr12_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitFCUpErr12_Object = MibTableColumn
ibPmaPortVlXmitFCUpErr12 = _IbPmaPortVlXmitFCUpErr12_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 1, 1, 14),
    _IbPmaPortVlXmitFCUpErr12_Type()
)
ibPmaPortVlXmitFCUpErr12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitFCUpErr12.setStatus("current")


class _IbPmaPortVlXmitFCUpErr13_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitFCUpErr13 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitFCUpErr13_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitFCUpErr13_Object = MibTableColumn
ibPmaPortVlXmitFCUpErr13 = _IbPmaPortVlXmitFCUpErr13_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 1, 1, 15),
    _IbPmaPortVlXmitFCUpErr13_Type()
)
ibPmaPortVlXmitFCUpErr13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitFCUpErr13.setStatus("current")


class _IbPmaPortVlXmitFCUpErr14_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitFCUpErr14 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitFCUpErr14_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitFCUpErr14_Object = MibTableColumn
ibPmaPortVlXmitFCUpErr14 = _IbPmaPortVlXmitFCUpErr14_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 1, 1, 16),
    _IbPmaPortVlXmitFCUpErr14_Type()
)
ibPmaPortVlXmitFCUpErr14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitFCUpErr14.setStatus("current")


class _IbPmaPortVlXmitFCUpErr15_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitFCUpErr15 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitFCUpErr15_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitFCUpErr15_Object = MibTableColumn
ibPmaPortVlXmitFCUpErr15 = _IbPmaPortVlXmitFCUpErr15_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 1, 1, 17),
    _IbPmaPortVlXmitFCUpErr15_Type()
)
ibPmaPortVlXmitFCUpErr15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitFCUpErr15.setStatus("current")
_IbPmaPortVlXmitWaitCntrsTable_Object = MibTable
ibPmaPortVlXmitWaitCntrsTable = _IbPmaPortVlXmitWaitCntrsTable_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ibPmaPortVlXmitWaitCntrsTable.setStatus("current")
_IbPmaPortVlXmitWaitCntrsEntry_Object = MibTableRow
ibPmaPortVlXmitWaitCntrsEntry = _IbPmaPortVlXmitWaitCntrsEntry_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 2, 1)
)
ibPmaPortVlXmitWaitCntrsEntry.setIndexNames(
    (0, "PMA-MIB", "ibPmaPortVlXmitWaitCntrsIndex"),
)
if mibBuilder.loadTexts:
    ibPmaPortVlXmitWaitCntrsEntry.setStatus("current")
_IbPmaPortVlXmitWaitCntrsIndex_Type = IbDataPort
_IbPmaPortVlXmitWaitCntrsIndex_Object = MibTableColumn
ibPmaPortVlXmitWaitCntrsIndex = _IbPmaPortVlXmitWaitCntrsIndex_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 2, 1, 1),
    _IbPmaPortVlXmitWaitCntrsIndex_Type()
)
ibPmaPortVlXmitWaitCntrsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitWaitCntrsIndex.setStatus("current")


class _IbPmaPortVlXmitWait0_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitWait0 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitWait0_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitWait0_Object = MibTableColumn
ibPmaPortVlXmitWait0 = _IbPmaPortVlXmitWait0_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 2, 1, 2),
    _IbPmaPortVlXmitWait0_Type()
)
ibPmaPortVlXmitWait0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitWait0.setStatus("current")


class _IbPmaPortVlXmitWait1_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitWait1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitWait1_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitWait1_Object = MibTableColumn
ibPmaPortVlXmitWait1 = _IbPmaPortVlXmitWait1_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 2, 1, 3),
    _IbPmaPortVlXmitWait1_Type()
)
ibPmaPortVlXmitWait1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitWait1.setStatus("current")


class _IbPmaPortVlXmitWait2_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitWait2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitWait2_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitWait2_Object = MibTableColumn
ibPmaPortVlXmitWait2 = _IbPmaPortVlXmitWait2_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 2, 1, 4),
    _IbPmaPortVlXmitWait2_Type()
)
ibPmaPortVlXmitWait2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitWait2.setStatus("current")


class _IbPmaPortVlXmitWait3_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitWait3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitWait3_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitWait3_Object = MibTableColumn
ibPmaPortVlXmitWait3 = _IbPmaPortVlXmitWait3_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 2, 1, 5),
    _IbPmaPortVlXmitWait3_Type()
)
ibPmaPortVlXmitWait3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitWait3.setStatus("current")


class _IbPmaPortVlXmitWait4_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitWait4 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitWait4_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitWait4_Object = MibTableColumn
ibPmaPortVlXmitWait4 = _IbPmaPortVlXmitWait4_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 2, 1, 6),
    _IbPmaPortVlXmitWait4_Type()
)
ibPmaPortVlXmitWait4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitWait4.setStatus("current")


class _IbPmaPortVlXmitWait5_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitWait5 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitWait5_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitWait5_Object = MibTableColumn
ibPmaPortVlXmitWait5 = _IbPmaPortVlXmitWait5_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 2, 1, 7),
    _IbPmaPortVlXmitWait5_Type()
)
ibPmaPortVlXmitWait5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitWait5.setStatus("current")


class _IbPmaPortVlXmitWait6_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitWait6 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitWait6_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitWait6_Object = MibTableColumn
ibPmaPortVlXmitWait6 = _IbPmaPortVlXmitWait6_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 2, 1, 8),
    _IbPmaPortVlXmitWait6_Type()
)
ibPmaPortVlXmitWait6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitWait6.setStatus("current")


class _IbPmaPortVlXmitWait7_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitWait7 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitWait7_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitWait7_Object = MibTableColumn
ibPmaPortVlXmitWait7 = _IbPmaPortVlXmitWait7_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 2, 1, 9),
    _IbPmaPortVlXmitWait7_Type()
)
ibPmaPortVlXmitWait7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitWait7.setStatus("current")


class _IbPmaPortVlXmitWait8_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitWait8 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitWait8_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitWait8_Object = MibTableColumn
ibPmaPortVlXmitWait8 = _IbPmaPortVlXmitWait8_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 2, 1, 10),
    _IbPmaPortVlXmitWait8_Type()
)
ibPmaPortVlXmitWait8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitWait8.setStatus("current")


class _IbPmaPortVlXmitWait9_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitWait9 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitWait9_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitWait9_Object = MibTableColumn
ibPmaPortVlXmitWait9 = _IbPmaPortVlXmitWait9_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 2, 1, 11),
    _IbPmaPortVlXmitWait9_Type()
)
ibPmaPortVlXmitWait9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitWait9.setStatus("current")


class _IbPmaPortVlXmitWait10_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitWait10 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitWait10_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitWait10_Object = MibTableColumn
ibPmaPortVlXmitWait10 = _IbPmaPortVlXmitWait10_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 2, 1, 12),
    _IbPmaPortVlXmitWait10_Type()
)
ibPmaPortVlXmitWait10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitWait10.setStatus("current")


class _IbPmaPortVlXmitWait11_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitWait11 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitWait11_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitWait11_Object = MibTableColumn
ibPmaPortVlXmitWait11 = _IbPmaPortVlXmitWait11_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 2, 1, 13),
    _IbPmaPortVlXmitWait11_Type()
)
ibPmaPortVlXmitWait11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitWait11.setStatus("current")


class _IbPmaPortVlXmitWait12_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitWait12 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitWait12_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitWait12_Object = MibTableColumn
ibPmaPortVlXmitWait12 = _IbPmaPortVlXmitWait12_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 2, 1, 14),
    _IbPmaPortVlXmitWait12_Type()
)
ibPmaPortVlXmitWait12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitWait12.setStatus("current")


class _IbPmaPortVlXmitWait13_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitWait13 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitWait13_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitWait13_Object = MibTableColumn
ibPmaPortVlXmitWait13 = _IbPmaPortVlXmitWait13_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 2, 1, 15),
    _IbPmaPortVlXmitWait13_Type()
)
ibPmaPortVlXmitWait13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitWait13.setStatus("current")


class _IbPmaPortVlXmitWait14_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitWait14 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitWait14_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitWait14_Object = MibTableColumn
ibPmaPortVlXmitWait14 = _IbPmaPortVlXmitWait14_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 2, 1, 16),
    _IbPmaPortVlXmitWait14_Type()
)
ibPmaPortVlXmitWait14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitWait14.setStatus("current")


class _IbPmaPortVlXmitWait15_Type(Unsigned32):
    """Custom type ibPmaPortVlXmitWait15 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlXmitWait15_Type.__name__ = "Unsigned32"
_IbPmaPortVlXmitWait15_Object = MibTableColumn
ibPmaPortVlXmitWait15 = _IbPmaPortVlXmitWait15_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 2, 1, 17),
    _IbPmaPortVlXmitWait15_Type()
)
ibPmaPortVlXmitWait15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlXmitWait15.setStatus("current")
_IbPmaPortVlSwCongestionTable_Object = MibTable
ibPmaPortVlSwCongestionTable = _IbPmaPortVlSwCongestionTable_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 3)
)
if mibBuilder.loadTexts:
    ibPmaPortVlSwCongestionTable.setStatus("current")
_IbPmaPortVlSwCongestionEntry_Object = MibTableRow
ibPmaPortVlSwCongestionEntry = _IbPmaPortVlSwCongestionEntry_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 3, 1)
)
ibPmaPortVlSwCongestionEntry.setIndexNames(
    (0, "PMA-MIB", "ibPmaPortVlSwCongestionIndex"),
)
if mibBuilder.loadTexts:
    ibPmaPortVlSwCongestionEntry.setStatus("current")
_IbPmaPortVlSwCongestionIndex_Type = IbDataPort
_IbPmaPortVlSwCongestionIndex_Object = MibTableColumn
ibPmaPortVlSwCongestionIndex = _IbPmaPortVlSwCongestionIndex_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 3, 1, 1),
    _IbPmaPortVlSwCongestionIndex_Type()
)
ibPmaPortVlSwCongestionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibPmaPortVlSwCongestionIndex.setStatus("current")


class _IbPmaPortVlSwCongestion0_Type(Unsigned32):
    """Custom type ibPmaPortVlSwCongestion0 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlSwCongestion0_Type.__name__ = "Unsigned32"
_IbPmaPortVlSwCongestion0_Object = MibTableColumn
ibPmaPortVlSwCongestion0 = _IbPmaPortVlSwCongestion0_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 3, 1, 2),
    _IbPmaPortVlSwCongestion0_Type()
)
ibPmaPortVlSwCongestion0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlSwCongestion0.setStatus("current")


class _IbPmaPortVlSwCongestion1_Type(Unsigned32):
    """Custom type ibPmaPortVlSwCongestion1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlSwCongestion1_Type.__name__ = "Unsigned32"
_IbPmaPortVlSwCongestion1_Object = MibTableColumn
ibPmaPortVlSwCongestion1 = _IbPmaPortVlSwCongestion1_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 3, 1, 3),
    _IbPmaPortVlSwCongestion1_Type()
)
ibPmaPortVlSwCongestion1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlSwCongestion1.setStatus("current")


class _IbPmaPortVlSwCongestion2_Type(Unsigned32):
    """Custom type ibPmaPortVlSwCongestion2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlSwCongestion2_Type.__name__ = "Unsigned32"
_IbPmaPortVlSwCongestion2_Object = MibTableColumn
ibPmaPortVlSwCongestion2 = _IbPmaPortVlSwCongestion2_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 3, 1, 4),
    _IbPmaPortVlSwCongestion2_Type()
)
ibPmaPortVlSwCongestion2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlSwCongestion2.setStatus("current")


class _IbPmaPortVlSwCongestion3_Type(Unsigned32):
    """Custom type ibPmaPortVlSwCongestion3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlSwCongestion3_Type.__name__ = "Unsigned32"
_IbPmaPortVlSwCongestion3_Object = MibTableColumn
ibPmaPortVlSwCongestion3 = _IbPmaPortVlSwCongestion3_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 3, 1, 5),
    _IbPmaPortVlSwCongestion3_Type()
)
ibPmaPortVlSwCongestion3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlSwCongestion3.setStatus("current")


class _IbPmaPortVlSwCongestion4_Type(Unsigned32):
    """Custom type ibPmaPortVlSwCongestion4 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlSwCongestion4_Type.__name__ = "Unsigned32"
_IbPmaPortVlSwCongestion4_Object = MibTableColumn
ibPmaPortVlSwCongestion4 = _IbPmaPortVlSwCongestion4_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 3, 1, 6),
    _IbPmaPortVlSwCongestion4_Type()
)
ibPmaPortVlSwCongestion4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlSwCongestion4.setStatus("current")


class _IbPmaPortVlSwCongestion5_Type(Unsigned32):
    """Custom type ibPmaPortVlSwCongestion5 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlSwCongestion5_Type.__name__ = "Unsigned32"
_IbPmaPortVlSwCongestion5_Object = MibTableColumn
ibPmaPortVlSwCongestion5 = _IbPmaPortVlSwCongestion5_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 3, 1, 7),
    _IbPmaPortVlSwCongestion5_Type()
)
ibPmaPortVlSwCongestion5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlSwCongestion5.setStatus("current")


class _IbPmaPortVlSwCongestion6_Type(Unsigned32):
    """Custom type ibPmaPortVlSwCongestion6 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlSwCongestion6_Type.__name__ = "Unsigned32"
_IbPmaPortVlSwCongestion6_Object = MibTableColumn
ibPmaPortVlSwCongestion6 = _IbPmaPortVlSwCongestion6_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 3, 1, 8),
    _IbPmaPortVlSwCongestion6_Type()
)
ibPmaPortVlSwCongestion6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlSwCongestion6.setStatus("current")


class _IbPmaPortVlSwCongestion7_Type(Unsigned32):
    """Custom type ibPmaPortVlSwCongestion7 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlSwCongestion7_Type.__name__ = "Unsigned32"
_IbPmaPortVlSwCongestion7_Object = MibTableColumn
ibPmaPortVlSwCongestion7 = _IbPmaPortVlSwCongestion7_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 3, 1, 9),
    _IbPmaPortVlSwCongestion7_Type()
)
ibPmaPortVlSwCongestion7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlSwCongestion7.setStatus("current")


class _IbPmaPortVlSwCongestion8_Type(Unsigned32):
    """Custom type ibPmaPortVlSwCongestion8 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlSwCongestion8_Type.__name__ = "Unsigned32"
_IbPmaPortVlSwCongestion8_Object = MibTableColumn
ibPmaPortVlSwCongestion8 = _IbPmaPortVlSwCongestion8_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 3, 1, 10),
    _IbPmaPortVlSwCongestion8_Type()
)
ibPmaPortVlSwCongestion8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlSwCongestion8.setStatus("current")


class _IbPmaPortVlSwCongestion9_Type(Unsigned32):
    """Custom type ibPmaPortVlSwCongestion9 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlSwCongestion9_Type.__name__ = "Unsigned32"
_IbPmaPortVlSwCongestion9_Object = MibTableColumn
ibPmaPortVlSwCongestion9 = _IbPmaPortVlSwCongestion9_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 3, 1, 11),
    _IbPmaPortVlSwCongestion9_Type()
)
ibPmaPortVlSwCongestion9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlSwCongestion9.setStatus("current")


class _IbPmaPortVlSwCongestion10_Type(Unsigned32):
    """Custom type ibPmaPortVlSwCongestion10 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlSwCongestion10_Type.__name__ = "Unsigned32"
_IbPmaPortVlSwCongestion10_Object = MibTableColumn
ibPmaPortVlSwCongestion10 = _IbPmaPortVlSwCongestion10_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 3, 1, 12),
    _IbPmaPortVlSwCongestion10_Type()
)
ibPmaPortVlSwCongestion10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlSwCongestion10.setStatus("current")


class _IbPmaPortVlSwCongestion11_Type(Unsigned32):
    """Custom type ibPmaPortVlSwCongestion11 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlSwCongestion11_Type.__name__ = "Unsigned32"
_IbPmaPortVlSwCongestion11_Object = MibTableColumn
ibPmaPortVlSwCongestion11 = _IbPmaPortVlSwCongestion11_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 3, 1, 13),
    _IbPmaPortVlSwCongestion11_Type()
)
ibPmaPortVlSwCongestion11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlSwCongestion11.setStatus("current")


class _IbPmaPortVlSwCongestion12_Type(Unsigned32):
    """Custom type ibPmaPortVlSwCongestion12 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlSwCongestion12_Type.__name__ = "Unsigned32"
_IbPmaPortVlSwCongestion12_Object = MibTableColumn
ibPmaPortVlSwCongestion12 = _IbPmaPortVlSwCongestion12_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 3, 1, 14),
    _IbPmaPortVlSwCongestion12_Type()
)
ibPmaPortVlSwCongestion12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlSwCongestion12.setStatus("current")


class _IbPmaPortVlSwCongestion13_Type(Unsigned32):
    """Custom type ibPmaPortVlSwCongestion13 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlSwCongestion13_Type.__name__ = "Unsigned32"
_IbPmaPortVlSwCongestion13_Object = MibTableColumn
ibPmaPortVlSwCongestion13 = _IbPmaPortVlSwCongestion13_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 3, 1, 15),
    _IbPmaPortVlSwCongestion13_Type()
)
ibPmaPortVlSwCongestion13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlSwCongestion13.setStatus("current")


class _IbPmaPortVlSwCongestion14_Type(Unsigned32):
    """Custom type ibPmaPortVlSwCongestion14 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlSwCongestion14_Type.__name__ = "Unsigned32"
_IbPmaPortVlSwCongestion14_Object = MibTableColumn
ibPmaPortVlSwCongestion14 = _IbPmaPortVlSwCongestion14_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 3, 1, 16),
    _IbPmaPortVlSwCongestion14_Type()
)
ibPmaPortVlSwCongestion14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlSwCongestion14.setStatus("current")


class _IbPmaPortVlSwCongestion15_Type(Unsigned32):
    """Custom type ibPmaPortVlSwCongestion15 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbPmaPortVlSwCongestion15_Type.__name__ = "Unsigned32"
_IbPmaPortVlSwCongestion15_Object = MibTableColumn
ibPmaPortVlSwCongestion15 = _IbPmaPortVlSwCongestion15_Object(
    (1, 3, 6, 1, 3, 117, 6, 1, 4, 3, 1, 17),
    _IbPmaPortVlSwCongestion15_Type()
)
ibPmaPortVlSwCongestion15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPmaPortVlSwCongestion15.setStatus("current")
_IbPmaConformance_ObjectIdentity = ObjectIdentity
ibPmaConformance = _IbPmaConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 6, 2)
)
_IbPmaCompliances_ObjectIdentity = ObjectIdentity
ibPmaCompliances = _IbPmaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 6, 2, 1)
)
_IbPmaGroups_ObjectIdentity = ObjectIdentity
ibPmaGroups = _IbPmaGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 6, 2, 2)
)

# Managed Objects groups

ibPmaPortCntrsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 6, 2, 2, 1)
)
ibPmaPortCntrsMandatoryGroup.setObjects(
      *(("PMA-MIB", "ibPmaSymbolErrCounter"),
        ("PMA-MIB", "ibPmaLinkErrRecoveryCntr"),
        ("PMA-MIB", "ibPmaLinkDownedCntr"),
        ("PMA-MIB", "ibPmaPortRcvErr"),
        ("PMA-MIB", "ibPmaPortRcvRemPhysErr"),
        ("PMA-MIB", "ibPmaPortRcvSwitchRelayErr"),
        ("PMA-MIB", "ibPmaPortXmitDiscard"),
        ("PMA-MIB", "ibPmaPortXmitConstraintErr"),
        ("PMA-MIB", "ibPmaPortRcvConstraintErr"),
        ("PMA-MIB", "ibPmaLocalLinkIntegrityErr"),
        ("PMA-MIB", "ibPmaExcessBufOverrunErr"),
        ("PMA-MIB", "ibPmaVl15Dropped"))
)
if mibBuilder.loadTexts:
    ibPmaPortCntrsMandatoryGroup.setStatus("current")

ibPmaPortCntrsOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 6, 2, 2, 2)
)
ibPmaPortCntrsOptionalGroup.setObjects(
      *(("PMA-MIB", "ibPmaPortXmitData"),
        ("PMA-MIB", "ibPmaPortRcvData"),
        ("PMA-MIB", "ibPmaPortXmitPkts"),
        ("PMA-MIB", "ibPmaPortRcvPkts"))
)
if mibBuilder.loadTexts:
    ibPmaPortCntrsOptionalGroup.setStatus("current")

ibPmaPortRcvErrGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 6, 2, 2, 3)
)
ibPmaPortRcvErrGroup.setObjects(
      *(("PMA-MIB", "ibPmaPortRcvErrLocalPhysErrs"),
        ("PMA-MIB", "ibPmaPortMalformedPacketErrs"),
        ("PMA-MIB", "ibPmaPortBufferOverrunErrs"),
        ("PMA-MIB", "ibPmaPortDLIDMappingErrs"),
        ("PMA-MIB", "ibPmaPortVLMappingErrs"),
        ("PMA-MIB", "ibPmaPortLoopingErrs"))
)
if mibBuilder.loadTexts:
    ibPmaPortRcvErrGroup.setStatus("current")

ibPmaPortXmitDiscardGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 6, 2, 2, 4)
)
ibPmaPortXmitDiscardGroup.setObjects(
      *(("PMA-MIB", "ibPmaPortInactiveDiscards"),
        ("PMA-MIB", "ibPmaPortNeighborMtuDiscards"),
        ("PMA-MIB", "ibPmaPortSwLifetimeLimitDiscards"),
        ("PMA-MIB", "ibPmaPortSwHoqLimitDiscards"))
)
if mibBuilder.loadTexts:
    ibPmaPortXmitDiscardGroup.setStatus("current")

ibPmaPortFlowCtlCntrsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 6, 2, 2, 5)
)
ibPmaPortFlowCtlCntrsGroup.setObjects(
      *(("PMA-MIB", "ibPmaPortFlowCtlXmitFlowPkts"),
        ("PMA-MIB", "ibPmaPortFlowCtlRcvFlowPkts"))
)
if mibBuilder.loadTexts:
    ibPmaPortFlowCtlCntrsGroup.setStatus("current")

ibPmaPortOpCodeRcvCntrsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 6, 2, 2, 6)
)
ibPmaPortOpCodeRcvCntrsGroup.setObjects(
      *(("PMA-MIB", "ibPmaPortOpCodeRcvCntrsRcvPkts"),
        ("PMA-MIB", "ibPmaPortOpCodeRcvCntrsRcvData"))
)
if mibBuilder.loadTexts:
    ibPmaPortOpCodeRcvCntrsGroup.setStatus("current")

ibPmaPortOpCodeVlCntrsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 6, 2, 2, 7)
)
ibPmaPortOpCodeVlCntrsGroup.setObjects(
      *(("PMA-MIB", "ibPmaPortVlOpPkt0"),
        ("PMA-MIB", "ibPmaPortVlOpPkt1"),
        ("PMA-MIB", "ibPmaPortVlOpPkt2"),
        ("PMA-MIB", "ibPmaPortVlOpPkt3"),
        ("PMA-MIB", "ibPmaPortVlOpPkt4"),
        ("PMA-MIB", "ibPmaPortVlOpPkt5"),
        ("PMA-MIB", "ibPmaPortVlOpPkt6"),
        ("PMA-MIB", "ibPmaPortVlOpPkt7"),
        ("PMA-MIB", "ibPmaPortVlOpPkt8"),
        ("PMA-MIB", "ibPmaPortVlOpPkt9"),
        ("PMA-MIB", "ibPmaPortVlOpPkt10"),
        ("PMA-MIB", "ibPmaPortVlOpPkt11"),
        ("PMA-MIB", "ibPmaPortVlOpPkt12"),
        ("PMA-MIB", "ibPmaPortVlOpPkt13"),
        ("PMA-MIB", "ibPmaPortVlOpPkt14"),
        ("PMA-MIB", "ibPmaPortVlOpPkt15"))
)
if mibBuilder.loadTexts:
    ibPmaPortOpCodeVlCntrsGroup.setStatus("current")

ibPmaPortOpCodeVlDataCntrsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 6, 2, 2, 8)
)
ibPmaPortOpCodeVlDataCntrsGroup.setObjects(
      *(("PMA-MIB", "ibPmaPortVlOpData0"),
        ("PMA-MIB", "ibPmaPortVlOpData1"),
        ("PMA-MIB", "ibPmaPortVlOpData2"),
        ("PMA-MIB", "ibPmaPortVlOpData3"),
        ("PMA-MIB", "ibPmaPortVlOpData4"),
        ("PMA-MIB", "ibPmaPortVlOpData5"),
        ("PMA-MIB", "ibPmaPortVlOpData6"),
        ("PMA-MIB", "ibPmaPortVlOpData7"),
        ("PMA-MIB", "ibPmaPortVlOpData8"),
        ("PMA-MIB", "ibPmaPortVlOpData9"),
        ("PMA-MIB", "ibPmaPortVlOpData10"),
        ("PMA-MIB", "ibPmaPortVlOpData11"),
        ("PMA-MIB", "ibPmaPortVlOpData12"),
        ("PMA-MIB", "ibPmaPortVlOpData13"),
        ("PMA-MIB", "ibPmaPortVlOpData14"),
        ("PMA-MIB", "ibPmaPortVlOpData15"))
)
if mibBuilder.loadTexts:
    ibPmaPortOpCodeVlDataCntrsGroup.setStatus("current")

ibPmaPortVlXmitFCUpErrGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 6, 2, 2, 9)
)
ibPmaPortVlXmitFCUpErrGroup.setObjects(
      *(("PMA-MIB", "ibPmaPortVlXmitFCUpErr0"),
        ("PMA-MIB", "ibPmaPortVlXmitFCUpErr1"),
        ("PMA-MIB", "ibPmaPortVlXmitFCUpErr2"),
        ("PMA-MIB", "ibPmaPortVlXmitFCUpErr3"),
        ("PMA-MIB", "ibPmaPortVlXmitFCUpErr4"),
        ("PMA-MIB", "ibPmaPortVlXmitFCUpErr5"),
        ("PMA-MIB", "ibPmaPortVlXmitFCUpErr6"),
        ("PMA-MIB", "ibPmaPortVlXmitFCUpErr7"),
        ("PMA-MIB", "ibPmaPortVlXmitFCUpErr8"),
        ("PMA-MIB", "ibPmaPortVlXmitFCUpErr9"),
        ("PMA-MIB", "ibPmaPortVlXmitFCUpErr10"),
        ("PMA-MIB", "ibPmaPortVlXmitFCUpErr11"),
        ("PMA-MIB", "ibPmaPortVlXmitFCUpErr12"),
        ("PMA-MIB", "ibPmaPortVlXmitFCUpErr13"),
        ("PMA-MIB", "ibPmaPortVlXmitFCUpErr14"),
        ("PMA-MIB", "ibPmaPortVlXmitFCUpErr15"))
)
if mibBuilder.loadTexts:
    ibPmaPortVlXmitFCUpErrGroup.setStatus("current")

ibPmaPortVlXmitWaitGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 6, 2, 2, 10)
)
ibPmaPortVlXmitWaitGroup.setObjects(
      *(("PMA-MIB", "ibPmaPortVlXmitWait0"),
        ("PMA-MIB", "ibPmaPortVlXmitWait1"),
        ("PMA-MIB", "ibPmaPortVlXmitWait2"),
        ("PMA-MIB", "ibPmaPortVlXmitWait3"),
        ("PMA-MIB", "ibPmaPortVlXmitWait4"),
        ("PMA-MIB", "ibPmaPortVlXmitWait5"),
        ("PMA-MIB", "ibPmaPortVlXmitWait6"),
        ("PMA-MIB", "ibPmaPortVlXmitWait7"),
        ("PMA-MIB", "ibPmaPortVlXmitWait8"),
        ("PMA-MIB", "ibPmaPortVlXmitWait9"),
        ("PMA-MIB", "ibPmaPortVlXmitWait10"),
        ("PMA-MIB", "ibPmaPortVlXmitWait11"),
        ("PMA-MIB", "ibPmaPortVlXmitWait12"),
        ("PMA-MIB", "ibPmaPortVlXmitWait13"),
        ("PMA-MIB", "ibPmaPortVlXmitWait14"),
        ("PMA-MIB", "ibPmaPortVlXmitWait15"))
)
if mibBuilder.loadTexts:
    ibPmaPortVlXmitWaitGroup.setStatus("current")

ibPmaPortVlSwCongestionGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 6, 2, 2, 11)
)
ibPmaPortVlSwCongestionGroup.setObjects(
      *(("PMA-MIB", "ibPmaPortVlSwCongestion0"),
        ("PMA-MIB", "ibPmaPortVlSwCongestion1"),
        ("PMA-MIB", "ibPmaPortVlSwCongestion2"),
        ("PMA-MIB", "ibPmaPortVlSwCongestion3"),
        ("PMA-MIB", "ibPmaPortVlSwCongestion4"),
        ("PMA-MIB", "ibPmaPortVlSwCongestion5"),
        ("PMA-MIB", "ibPmaPortVlSwCongestion6"),
        ("PMA-MIB", "ibPmaPortVlSwCongestion7"),
        ("PMA-MIB", "ibPmaPortVlSwCongestion8"),
        ("PMA-MIB", "ibPmaPortVlSwCongestion9"),
        ("PMA-MIB", "ibPmaPortVlSwCongestion10"),
        ("PMA-MIB", "ibPmaPortVlSwCongestion11"),
        ("PMA-MIB", "ibPmaPortVlSwCongestion12"),
        ("PMA-MIB", "ibPmaPortVlSwCongestion13"),
        ("PMA-MIB", "ibPmaPortVlSwCongestion14"),
        ("PMA-MIB", "ibPmaPortVlSwCongestion15"))
)
if mibBuilder.loadTexts:
    ibPmaPortVlSwCongestionGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ibPmaBasicNodeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 117, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ibPmaBasicNodeCompliance.setStatus(
        "current"
    )

ibPmaFullNodeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 117, 6, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ibPmaFullNodeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PMA-MIB",
    **{"ibPmaMIB": ibPmaMIB,
       "ibPmaObjects": ibPmaObjects,
       "ibPmaPortCntrsInfo": ibPmaPortCntrsInfo,
       "ibPmaPortCntrsTable": ibPmaPortCntrsTable,
       "ibPmaPortCntrsEntry": ibPmaPortCntrsEntry,
       "ibPmaPortCntrsIndex": ibPmaPortCntrsIndex,
       "ibPmaSymbolErrCounter": ibPmaSymbolErrCounter,
       "ibPmaLinkErrRecoveryCntr": ibPmaLinkErrRecoveryCntr,
       "ibPmaLinkDownedCntr": ibPmaLinkDownedCntr,
       "ibPmaPortRcvErr": ibPmaPortRcvErr,
       "ibPmaPortRcvRemPhysErr": ibPmaPortRcvRemPhysErr,
       "ibPmaPortRcvSwitchRelayErr": ibPmaPortRcvSwitchRelayErr,
       "ibPmaPortXmitDiscard": ibPmaPortXmitDiscard,
       "ibPmaPortXmitConstraintErr": ibPmaPortXmitConstraintErr,
       "ibPmaPortRcvConstraintErr": ibPmaPortRcvConstraintErr,
       "ibPmaLocalLinkIntegrityErr": ibPmaLocalLinkIntegrityErr,
       "ibPmaExcessBufOverrunErr": ibPmaExcessBufOverrunErr,
       "ibPmaVl15Dropped": ibPmaVl15Dropped,
       "ibPmaPortCntrsOptTable": ibPmaPortCntrsOptTable,
       "ibPmaPortCntrsOptEntry": ibPmaPortCntrsOptEntry,
       "ibPmaPortCntrsOptIndex": ibPmaPortCntrsOptIndex,
       "ibPmaPortXmitData": ibPmaPortXmitData,
       "ibPmaPortRcvData": ibPmaPortRcvData,
       "ibPmaPortXmitPkts": ibPmaPortXmitPkts,
       "ibPmaPortRcvPkts": ibPmaPortRcvPkts,
       "ibPmaPortXmitRecvInfo": ibPmaPortXmitRecvInfo,
       "ibPmaPortRcvErrTable": ibPmaPortRcvErrTable,
       "ibPmaPortRcvErrEntry": ibPmaPortRcvErrEntry,
       "ibPmaPortRcvErrIndex": ibPmaPortRcvErrIndex,
       "ibPmaPortRcvErrLocalPhysErrs": ibPmaPortRcvErrLocalPhysErrs,
       "ibPmaPortMalformedPacketErrs": ibPmaPortMalformedPacketErrs,
       "ibPmaPortBufferOverrunErrs": ibPmaPortBufferOverrunErrs,
       "ibPmaPortDLIDMappingErrs": ibPmaPortDLIDMappingErrs,
       "ibPmaPortVLMappingErrs": ibPmaPortVLMappingErrs,
       "ibPmaPortLoopingErrs": ibPmaPortLoopingErrs,
       "ibPmaPortXmitDiscardTable": ibPmaPortXmitDiscardTable,
       "ibPmaPortXmitDiscardEntry": ibPmaPortXmitDiscardEntry,
       "ibPmaPortXmitDiscardIndex": ibPmaPortXmitDiscardIndex,
       "ibPmaPortInactiveDiscards": ibPmaPortInactiveDiscards,
       "ibPmaPortNeighborMtuDiscards": ibPmaPortNeighborMtuDiscards,
       "ibPmaPortSwLifetimeLimitDiscards": ibPmaPortSwLifetimeLimitDiscards,
       "ibPmaPortSwHoqLimitDiscards": ibPmaPortSwHoqLimitDiscards,
       "ibPmaPortFlowCtlCntrsTable": ibPmaPortFlowCtlCntrsTable,
       "ibPmaPortFlowCtlCntrsEntry": ibPmaPortFlowCtlCntrsEntry,
       "ibPmaPortFlowCtlCntrsIndex": ibPmaPortFlowCtlCntrsIndex,
       "ibPmaPortFlowCtlXmitFlowPkts": ibPmaPortFlowCtlXmitFlowPkts,
       "ibPmaPortFlowCtlRcvFlowPkts": ibPmaPortFlowCtlRcvFlowPkts,
       "ibPmaPortOpCodeInfo": ibPmaPortOpCodeInfo,
       "ibPmaPortOpCodeRcvCntrsTable": ibPmaPortOpCodeRcvCntrsTable,
       "ibPmaPortOpCodeRcvCntrsEntry": ibPmaPortOpCodeRcvCntrsEntry,
       "ibPmaPortOpCodeRcvCntrsPortIndex": ibPmaPortOpCodeRcvCntrsPortIndex,
       "ibPmaPortOpCodeRcvCntrsIndex": ibPmaPortOpCodeRcvCntrsIndex,
       "ibPmaPortOpCodeRcvCntrsRcvPkts": ibPmaPortOpCodeRcvCntrsRcvPkts,
       "ibPmaPortOpCodeRcvCntrsRcvData": ibPmaPortOpCodeRcvCntrsRcvData,
       "ibPmaPortOpCodeVlCntrsTable": ibPmaPortOpCodeVlCntrsTable,
       "ibPmaPortOpCodeVlCntrsEntry": ibPmaPortOpCodeVlCntrsEntry,
       "ibPmaPortOpCodeVlCntrsPortIndex": ibPmaPortOpCodeVlCntrsPortIndex,
       "ibPmaPortOpCodeVlCntrsIndex": ibPmaPortOpCodeVlCntrsIndex,
       "ibPmaPortVlOpPkt0": ibPmaPortVlOpPkt0,
       "ibPmaPortVlOpPkt1": ibPmaPortVlOpPkt1,
       "ibPmaPortVlOpPkt2": ibPmaPortVlOpPkt2,
       "ibPmaPortVlOpPkt3": ibPmaPortVlOpPkt3,
       "ibPmaPortVlOpPkt4": ibPmaPortVlOpPkt4,
       "ibPmaPortVlOpPkt5": ibPmaPortVlOpPkt5,
       "ibPmaPortVlOpPkt6": ibPmaPortVlOpPkt6,
       "ibPmaPortVlOpPkt7": ibPmaPortVlOpPkt7,
       "ibPmaPortVlOpPkt8": ibPmaPortVlOpPkt8,
       "ibPmaPortVlOpPkt9": ibPmaPortVlOpPkt9,
       "ibPmaPortVlOpPkt10": ibPmaPortVlOpPkt10,
       "ibPmaPortVlOpPkt11": ibPmaPortVlOpPkt11,
       "ibPmaPortVlOpPkt12": ibPmaPortVlOpPkt12,
       "ibPmaPortVlOpPkt13": ibPmaPortVlOpPkt13,
       "ibPmaPortVlOpPkt14": ibPmaPortVlOpPkt14,
       "ibPmaPortVlOpPkt15": ibPmaPortVlOpPkt15,
       "ibPmaPortOpCodeVlDataCntrsTable": ibPmaPortOpCodeVlDataCntrsTable,
       "ibPmaPortOpCodeVlDataCntrsEntry": ibPmaPortOpCodeVlDataCntrsEntry,
       "ibPmaPortOpCodeVlDataPortIndex": ibPmaPortOpCodeVlDataPortIndex,
       "ibPmaPortOpCodeVlDataIndex": ibPmaPortOpCodeVlDataIndex,
       "ibPmaPortVlOpData0": ibPmaPortVlOpData0,
       "ibPmaPortVlOpData1": ibPmaPortVlOpData1,
       "ibPmaPortVlOpData2": ibPmaPortVlOpData2,
       "ibPmaPortVlOpData3": ibPmaPortVlOpData3,
       "ibPmaPortVlOpData4": ibPmaPortVlOpData4,
       "ibPmaPortVlOpData5": ibPmaPortVlOpData5,
       "ibPmaPortVlOpData6": ibPmaPortVlOpData6,
       "ibPmaPortVlOpData7": ibPmaPortVlOpData7,
       "ibPmaPortVlOpData8": ibPmaPortVlOpData8,
       "ibPmaPortVlOpData9": ibPmaPortVlOpData9,
       "ibPmaPortVlOpData10": ibPmaPortVlOpData10,
       "ibPmaPortVlOpData11": ibPmaPortVlOpData11,
       "ibPmaPortVlOpData12": ibPmaPortVlOpData12,
       "ibPmaPortVlOpData13": ibPmaPortVlOpData13,
       "ibPmaPortVlOpData14": ibPmaPortVlOpData14,
       "ibPmaPortVlOpData15": ibPmaPortVlOpData15,
       "ibPmaPortVlInfo": ibPmaPortVlInfo,
       "ibPmaPortVlXmitFCUpErrTable": ibPmaPortVlXmitFCUpErrTable,
       "ibPmaPortVlXmitFCUpErrEntry": ibPmaPortVlXmitFCUpErrEntry,
       "ibPmaPortVlXmitFCUpErrPortIndex": ibPmaPortVlXmitFCUpErrPortIndex,
       "ibPmaPortVlXmitFCUpErr0": ibPmaPortVlXmitFCUpErr0,
       "ibPmaPortVlXmitFCUpErr1": ibPmaPortVlXmitFCUpErr1,
       "ibPmaPortVlXmitFCUpErr2": ibPmaPortVlXmitFCUpErr2,
       "ibPmaPortVlXmitFCUpErr3": ibPmaPortVlXmitFCUpErr3,
       "ibPmaPortVlXmitFCUpErr4": ibPmaPortVlXmitFCUpErr4,
       "ibPmaPortVlXmitFCUpErr5": ibPmaPortVlXmitFCUpErr5,
       "ibPmaPortVlXmitFCUpErr6": ibPmaPortVlXmitFCUpErr6,
       "ibPmaPortVlXmitFCUpErr7": ibPmaPortVlXmitFCUpErr7,
       "ibPmaPortVlXmitFCUpErr8": ibPmaPortVlXmitFCUpErr8,
       "ibPmaPortVlXmitFCUpErr9": ibPmaPortVlXmitFCUpErr9,
       "ibPmaPortVlXmitFCUpErr10": ibPmaPortVlXmitFCUpErr10,
       "ibPmaPortVlXmitFCUpErr11": ibPmaPortVlXmitFCUpErr11,
       "ibPmaPortVlXmitFCUpErr12": ibPmaPortVlXmitFCUpErr12,
       "ibPmaPortVlXmitFCUpErr13": ibPmaPortVlXmitFCUpErr13,
       "ibPmaPortVlXmitFCUpErr14": ibPmaPortVlXmitFCUpErr14,
       "ibPmaPortVlXmitFCUpErr15": ibPmaPortVlXmitFCUpErr15,
       "ibPmaPortVlXmitWaitCntrsTable": ibPmaPortVlXmitWaitCntrsTable,
       "ibPmaPortVlXmitWaitCntrsEntry": ibPmaPortVlXmitWaitCntrsEntry,
       "ibPmaPortVlXmitWaitCntrsIndex": ibPmaPortVlXmitWaitCntrsIndex,
       "ibPmaPortVlXmitWait0": ibPmaPortVlXmitWait0,
       "ibPmaPortVlXmitWait1": ibPmaPortVlXmitWait1,
       "ibPmaPortVlXmitWait2": ibPmaPortVlXmitWait2,
       "ibPmaPortVlXmitWait3": ibPmaPortVlXmitWait3,
       "ibPmaPortVlXmitWait4": ibPmaPortVlXmitWait4,
       "ibPmaPortVlXmitWait5": ibPmaPortVlXmitWait5,
       "ibPmaPortVlXmitWait6": ibPmaPortVlXmitWait6,
       "ibPmaPortVlXmitWait7": ibPmaPortVlXmitWait7,
       "ibPmaPortVlXmitWait8": ibPmaPortVlXmitWait8,
       "ibPmaPortVlXmitWait9": ibPmaPortVlXmitWait9,
       "ibPmaPortVlXmitWait10": ibPmaPortVlXmitWait10,
       "ibPmaPortVlXmitWait11": ibPmaPortVlXmitWait11,
       "ibPmaPortVlXmitWait12": ibPmaPortVlXmitWait12,
       "ibPmaPortVlXmitWait13": ibPmaPortVlXmitWait13,
       "ibPmaPortVlXmitWait14": ibPmaPortVlXmitWait14,
       "ibPmaPortVlXmitWait15": ibPmaPortVlXmitWait15,
       "ibPmaPortVlSwCongestionTable": ibPmaPortVlSwCongestionTable,
       "ibPmaPortVlSwCongestionEntry": ibPmaPortVlSwCongestionEntry,
       "ibPmaPortVlSwCongestionIndex": ibPmaPortVlSwCongestionIndex,
       "ibPmaPortVlSwCongestion0": ibPmaPortVlSwCongestion0,
       "ibPmaPortVlSwCongestion1": ibPmaPortVlSwCongestion1,
       "ibPmaPortVlSwCongestion2": ibPmaPortVlSwCongestion2,
       "ibPmaPortVlSwCongestion3": ibPmaPortVlSwCongestion3,
       "ibPmaPortVlSwCongestion4": ibPmaPortVlSwCongestion4,
       "ibPmaPortVlSwCongestion5": ibPmaPortVlSwCongestion5,
       "ibPmaPortVlSwCongestion6": ibPmaPortVlSwCongestion6,
       "ibPmaPortVlSwCongestion7": ibPmaPortVlSwCongestion7,
       "ibPmaPortVlSwCongestion8": ibPmaPortVlSwCongestion8,
       "ibPmaPortVlSwCongestion9": ibPmaPortVlSwCongestion9,
       "ibPmaPortVlSwCongestion10": ibPmaPortVlSwCongestion10,
       "ibPmaPortVlSwCongestion11": ibPmaPortVlSwCongestion11,
       "ibPmaPortVlSwCongestion12": ibPmaPortVlSwCongestion12,
       "ibPmaPortVlSwCongestion13": ibPmaPortVlSwCongestion13,
       "ibPmaPortVlSwCongestion14": ibPmaPortVlSwCongestion14,
       "ibPmaPortVlSwCongestion15": ibPmaPortVlSwCongestion15,
       "ibPmaConformance": ibPmaConformance,
       "ibPmaCompliances": ibPmaCompliances,
       "ibPmaBasicNodeCompliance": ibPmaBasicNodeCompliance,
       "ibPmaFullNodeCompliance": ibPmaFullNodeCompliance,
       "ibPmaGroups": ibPmaGroups,
       "ibPmaPortCntrsMandatoryGroup": ibPmaPortCntrsMandatoryGroup,
       "ibPmaPortCntrsOptionalGroup": ibPmaPortCntrsOptionalGroup,
       "ibPmaPortRcvErrGroup": ibPmaPortRcvErrGroup,
       "ibPmaPortXmitDiscardGroup": ibPmaPortXmitDiscardGroup,
       "ibPmaPortFlowCtlCntrsGroup": ibPmaPortFlowCtlCntrsGroup,
       "ibPmaPortOpCodeRcvCntrsGroup": ibPmaPortOpCodeRcvCntrsGroup,
       "ibPmaPortOpCodeVlCntrsGroup": ibPmaPortOpCodeVlCntrsGroup,
       "ibPmaPortOpCodeVlDataCntrsGroup": ibPmaPortOpCodeVlDataCntrsGroup,
       "ibPmaPortVlXmitFCUpErrGroup": ibPmaPortVlXmitFCUpErrGroup,
       "ibPmaPortVlXmitWaitGroup": ibPmaPortVlXmitWaitGroup,
       "ibPmaPortVlSwCongestionGroup": ibPmaPortVlSwCongestionGroup}
)
