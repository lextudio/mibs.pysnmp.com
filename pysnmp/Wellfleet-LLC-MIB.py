# SNMP MIB module (Wellfleet-LLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-LLC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:36 2024
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

(wfLlcGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfLlcGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfLlc_ObjectIdentity = ObjectIdentity
wfLlc = _WfLlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 1)
)


class _WfLlcBaseDelete_Type(Integer32):
    """Custom type wfLlcBaseDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfLlcBaseDelete_Type.__name__ = "Integer32"
_WfLlcBaseDelete_Object = MibScalar
wfLlcBaseDelete = _WfLlcBaseDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 1, 1),
    _WfLlcBaseDelete_Type()
)
wfLlcBaseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlcBaseDelete.setStatus("mandatory")


class _WfLlcBaseDisable_Type(Integer32):
    """Custom type wfLlcBaseDisable based on Integer32"""
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


_WfLlcBaseDisable_Type.__name__ = "Integer32"
_WfLlcBaseDisable_Object = MibScalar
wfLlcBaseDisable = _WfLlcBaseDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 1, 2),
    _WfLlcBaseDisable_Type()
)
wfLlcBaseDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlcBaseDisable.setStatus("mandatory")


class _WfLlcBaseState_Type(Integer32):
    """Custom type wfLlcBaseState based on Integer32"""
    defaultValue = 2

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfLlcBaseState_Type.__name__ = "Integer32"
_WfLlcBaseState_Object = MibScalar
wfLlcBaseState = _WfLlcBaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 1, 3),
    _WfLlcBaseState_Type()
)
wfLlcBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcBaseState.setStatus("mandatory")
_WfLlcInterfaceTable_Object = MibTable
wfLlcInterfaceTable = _WfLlcInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2)
)
if mibBuilder.loadTexts:
    wfLlcInterfaceTable.setStatus("mandatory")
_WfLlcInterfaceEntry_Object = MibTableRow
wfLlcInterfaceEntry = _WfLlcInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1)
)
wfLlcInterfaceEntry.setIndexNames(
    (0, "Wellfleet-LLC-MIB", "wfLlcInterfaceCircuit"),
)
if mibBuilder.loadTexts:
    wfLlcInterfaceEntry.setStatus("mandatory")


class _WfLlcInterfaceDelete_Type(Integer32):
    """Custom type wfLlcInterfaceDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfLlcInterfaceDelete_Type.__name__ = "Integer32"
_WfLlcInterfaceDelete_Object = MibTableColumn
wfLlcInterfaceDelete = _WfLlcInterfaceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 1),
    _WfLlcInterfaceDelete_Type()
)
wfLlcInterfaceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlcInterfaceDelete.setStatus("mandatory")


class _WfLlcInterfaceDisable_Type(Integer32):
    """Custom type wfLlcInterfaceDisable based on Integer32"""
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


_WfLlcInterfaceDisable_Type.__name__ = "Integer32"
_WfLlcInterfaceDisable_Object = MibTableColumn
wfLlcInterfaceDisable = _WfLlcInterfaceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 2),
    _WfLlcInterfaceDisable_Type()
)
wfLlcInterfaceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlcInterfaceDisable.setStatus("mandatory")


class _WfLlcInterfaceState_Type(Integer32):
    """Custom type wfLlcInterfaceState based on Integer32"""
    defaultValue = 2

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfLlcInterfaceState_Type.__name__ = "Integer32"
_WfLlcInterfaceState_Object = MibTableColumn
wfLlcInterfaceState = _WfLlcInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 3),
    _WfLlcInterfaceState_Type()
)
wfLlcInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcInterfaceState.setStatus("mandatory")
_WfLlcInterfaceCircuit_Type = Integer32
_WfLlcInterfaceCircuit_Object = MibTableColumn
wfLlcInterfaceCircuit = _WfLlcInterfaceCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 4),
    _WfLlcInterfaceCircuit_Type()
)
wfLlcInterfaceCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcInterfaceCircuit.setStatus("mandatory")
_WfLlcInterfaceLlc2CctId_Type = Integer32
_WfLlcInterfaceLlc2CctId_Object = MibTableColumn
wfLlcInterfaceLlc2CctId = _WfLlcInterfaceLlc2CctId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 5),
    _WfLlcInterfaceLlc2CctId_Type()
)
wfLlcInterfaceLlc2CctId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlcInterfaceLlc2CctId.setStatus("mandatory")


class _WfLlc1InterfaceMaxUinfoSize_Type(Integer32):
    """Custom type wfLlc1InterfaceMaxUinfoSize based on Integer32"""
    defaultValue = 5128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5128),
    )


_WfLlc1InterfaceMaxUinfoSize_Type.__name__ = "Integer32"
_WfLlc1InterfaceMaxUinfoSize_Object = MibTableColumn
wfLlc1InterfaceMaxUinfoSize = _WfLlc1InterfaceMaxUinfoSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 6),
    _WfLlc1InterfaceMaxUinfoSize_Type()
)
wfLlc1InterfaceMaxUinfoSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlc1InterfaceMaxUinfoSize.setStatus("mandatory")


class _WfLlc1InterfaceMaxRetry_Type(Integer32):
    """Custom type wfLlc1InterfaceMaxRetry based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WfLlc1InterfaceMaxRetry_Type.__name__ = "Integer32"
_WfLlc1InterfaceMaxRetry_Object = MibTableColumn
wfLlc1InterfaceMaxRetry = _WfLlc1InterfaceMaxRetry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 7),
    _WfLlc1InterfaceMaxRetry_Type()
)
wfLlc1InterfaceMaxRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlc1InterfaceMaxRetry.setStatus("mandatory")


class _WfLlc1InterfaceTAckWait_Type(Integer32):
    """Custom type wfLlc1InterfaceTAckWait based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_WfLlc1InterfaceTAckWait_Type.__name__ = "Integer32"
_WfLlc1InterfaceTAckWait_Object = MibTableColumn
wfLlc1InterfaceTAckWait = _WfLlc1InterfaceTAckWait_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 8),
    _WfLlc1InterfaceTAckWait_Type()
)
wfLlc1InterfaceTAckWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlc1InterfaceTAckWait.setStatus("mandatory")


class _WfLlc2InterfaceMaxInfoSize_Type(Integer32):
    """Custom type wfLlc2InterfaceMaxInfoSize based on Integer32"""
    defaultValue = 5128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5128),
    )


_WfLlc2InterfaceMaxInfoSize_Type.__name__ = "Integer32"
_WfLlc2InterfaceMaxInfoSize_Object = MibTableColumn
wfLlc2InterfaceMaxInfoSize = _WfLlc2InterfaceMaxInfoSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 9),
    _WfLlc2InterfaceMaxInfoSize_Type()
)
wfLlc2InterfaceMaxInfoSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlc2InterfaceMaxInfoSize.setStatus("mandatory")


class _WfLlc2InterfaceK_Type(Integer32):
    """Custom type wfLlc2InterfaceK based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_WfLlc2InterfaceK_Type.__name__ = "Integer32"
_WfLlc2InterfaceK_Object = MibTableColumn
wfLlc2InterfaceK = _WfLlc2InterfaceK_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 10),
    _WfLlc2InterfaceK_Type()
)
wfLlc2InterfaceK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlc2InterfaceK.setStatus("mandatory")


class _WfLlc2InterfaceN2_Type(Integer32):
    """Custom type wfLlc2InterfaceN2 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfLlc2InterfaceN2_Type.__name__ = "Integer32"
_WfLlc2InterfaceN2_Object = MibTableColumn
wfLlc2InterfaceN2 = _WfLlc2InterfaceN2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 11),
    _WfLlc2InterfaceN2_Type()
)
wfLlc2InterfaceN2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlc2InterfaceN2.setStatus("mandatory")


class _WfLlc2InterfaceN3_Type(Integer32):
    """Custom type wfLlc2InterfaceN3 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WfLlc2InterfaceN3_Type.__name__ = "Integer32"
_WfLlc2InterfaceN3_Object = MibTableColumn
wfLlc2InterfaceN3 = _WfLlc2InterfaceN3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 12),
    _WfLlc2InterfaceN3_Type()
)
wfLlc2InterfaceN3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlc2InterfaceN3.setStatus("mandatory")


class _WfLlc2InterfaceTAckWait_Type(Integer32):
    """Custom type wfLlc2InterfaceTAckWait based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_WfLlc2InterfaceTAckWait_Type.__name__ = "Integer32"
_WfLlc2InterfaceTAckWait_Object = MibTableColumn
wfLlc2InterfaceTAckWait = _WfLlc2InterfaceTAckWait_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 13),
    _WfLlc2InterfaceTAckWait_Type()
)
wfLlc2InterfaceTAckWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlc2InterfaceTAckWait.setStatus("mandatory")


class _WfLlc2InterfaceTReject_Type(Integer32):
    """Custom type wfLlc2InterfaceTReject based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_WfLlc2InterfaceTReject_Type.__name__ = "Integer32"
_WfLlc2InterfaceTReject_Object = MibTableColumn
wfLlc2InterfaceTReject = _WfLlc2InterfaceTReject_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 14),
    _WfLlc2InterfaceTReject_Type()
)
wfLlc2InterfaceTReject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlc2InterfaceTReject.setStatus("mandatory")


class _WfLlc2InterfaceTRemoteBusy_Type(Integer32):
    """Custom type wfLlc2InterfaceTRemoteBusy based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfLlc2InterfaceTRemoteBusy_Type.__name__ = "Integer32"
_WfLlc2InterfaceTRemoteBusy_Object = MibTableColumn
wfLlc2InterfaceTRemoteBusy = _WfLlc2InterfaceTRemoteBusy_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 15),
    _WfLlc2InterfaceTRemoteBusy_Type()
)
wfLlc2InterfaceTRemoteBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlc2InterfaceTRemoteBusy.setStatus("mandatory")


class _WfLlc2InterfaceTRspAck_Type(Integer32):
    """Custom type wfLlc2InterfaceTRspAck based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfLlc2InterfaceTRspAck_Type.__name__ = "Integer32"
_WfLlc2InterfaceTRspAck_Object = MibTableColumn
wfLlc2InterfaceTRspAck = _WfLlc2InterfaceTRspAck_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 16),
    _WfLlc2InterfaceTRspAck_Type()
)
wfLlc2InterfaceTRspAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlc2InterfaceTRspAck.setStatus("mandatory")


class _WfLlc2InterfaceTIdle_Type(Integer32):
    """Custom type wfLlc2InterfaceTIdle based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_WfLlc2InterfaceTIdle_Type.__name__ = "Integer32"
_WfLlc2InterfaceTIdle_Object = MibTableColumn
wfLlc2InterfaceTIdle = _WfLlc2InterfaceTIdle_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 17),
    _WfLlc2InterfaceTIdle_Type()
)
wfLlc2InterfaceTIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlc2InterfaceTIdle.setStatus("mandatory")


class _WfLlc2InterfaceTPollCycle_Type(Integer32):
    """Custom type wfLlc2InterfaceTPollCycle based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_WfLlc2InterfaceTPollCycle_Type.__name__ = "Integer32"
_WfLlc2InterfaceTPollCycle_Object = MibTableColumn
wfLlc2InterfaceTPollCycle = _WfLlc2InterfaceTPollCycle_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 18),
    _WfLlc2InterfaceTPollCycle_Type()
)
wfLlc2InterfaceTPollCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlc2InterfaceTPollCycle.setStatus("mandatory")


class _WfLlcInterfaceMaxNumOfSap_Type(Integer32):
    """Custom type wfLlcInterfaceMaxNumOfSap based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 255),
    )


_WfLlcInterfaceMaxNumOfSap_Type.__name__ = "Integer32"
_WfLlcInterfaceMaxNumOfSap_Object = MibTableColumn
wfLlcInterfaceMaxNumOfSap = _WfLlcInterfaceMaxNumOfSap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 19),
    _WfLlcInterfaceMaxNumOfSap_Type()
)
wfLlcInterfaceMaxNumOfSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlcInterfaceMaxNumOfSap.setStatus("mandatory")


class _WfLlcInterfaceMaxNumOfLink_Type(Integer32):
    """Custom type wfLlcInterfaceMaxNumOfLink based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 5000),
    )


_WfLlcInterfaceMaxNumOfLink_Type.__name__ = "Integer32"
_WfLlcInterfaceMaxNumOfLink_Object = MibTableColumn
wfLlcInterfaceMaxNumOfLink = _WfLlcInterfaceMaxNumOfLink_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 20),
    _WfLlcInterfaceMaxNumOfLink_Type()
)
wfLlcInterfaceMaxNumOfLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlcInterfaceMaxNumOfLink.setStatus("mandatory")


class _WfLlcInterfaceDupAddrCheck_Type(Integer32):
    """Custom type wfLlcInterfaceDupAddrCheck based on Integer32"""
    defaultValue = 2

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


_WfLlcInterfaceDupAddrCheck_Type.__name__ = "Integer32"
_WfLlcInterfaceDupAddrCheck_Object = MibTableColumn
wfLlcInterfaceDupAddrCheck = _WfLlcInterfaceDupAddrCheck_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 21),
    _WfLlcInterfaceDupAddrCheck_Type()
)
wfLlcInterfaceDupAddrCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlcInterfaceDupAddrCheck.setStatus("mandatory")


class _WfLlc2InterfaceRW_Type(Integer32):
    """Custom type wfLlc2InterfaceRW based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_WfLlc2InterfaceRW_Type.__name__ = "Integer32"
_WfLlc2InterfaceRW_Object = MibTableColumn
wfLlc2InterfaceRW = _WfLlc2InterfaceRW_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 22),
    _WfLlc2InterfaceRW_Type()
)
wfLlc2InterfaceRW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlc2InterfaceRW.setStatus("mandatory")


class _WfLlc2InterfaceTW_Type(Integer32):
    """Custom type wfLlc2InterfaceTW based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_WfLlc2InterfaceTW_Type.__name__ = "Integer32"
_WfLlc2InterfaceTW_Object = MibTableColumn
wfLlc2InterfaceTW = _WfLlc2InterfaceTW_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 23),
    _WfLlc2InterfaceTW_Type()
)
wfLlc2InterfaceTW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlc2InterfaceTW.setStatus("mandatory")


class _WfLlcInterfaceEncapsType_Type(Integer32):
    """Custom type wfLlcInterfaceEncapsType based on Integer32"""
    defaultValue = 1

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
        *(("csmacd", 3),
          ("default", 1),
          ("fr", 5),
          ("srb", 4),
          ("tring", 2))
    )


_WfLlcInterfaceEncapsType_Type.__name__ = "Integer32"
_WfLlcInterfaceEncapsType_Object = MibTableColumn
wfLlcInterfaceEncapsType = _WfLlcInterfaceEncapsType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 24),
    _WfLlcInterfaceEncapsType_Type()
)
wfLlcInterfaceEncapsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlcInterfaceEncapsType.setStatus("mandatory")


class _WfLlcInterfaceSrbRingId_Type(Integer32):
    """Custom type wfLlcInterfaceSrbRingId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_WfLlcInterfaceSrbRingId_Type.__name__ = "Integer32"
_WfLlcInterfaceSrbRingId_Object = MibTableColumn
wfLlcInterfaceSrbRingId = _WfLlcInterfaceSrbRingId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 25),
    _WfLlcInterfaceSrbRingId_Type()
)
wfLlcInterfaceSrbRingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlcInterfaceSrbRingId.setStatus("mandatory")
_WfLlcInterfaceFrVMask_Type = OctetString
_WfLlcInterfaceFrVMask_Object = MibTableColumn
wfLlcInterfaceFrVMask = _WfLlcInterfaceFrVMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 26),
    _WfLlcInterfaceFrVMask_Type()
)
wfLlcInterfaceFrVMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlcInterfaceFrVMask.setStatus("mandatory")


class _WfLlc2InterfaceDynWin_Type(Integer32):
    """Custom type wfLlc2InterfaceDynWin based on Integer32"""
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


_WfLlc2InterfaceDynWin_Type.__name__ = "Integer32"
_WfLlc2InterfaceDynWin_Object = MibTableColumn
wfLlc2InterfaceDynWin = _WfLlc2InterfaceDynWin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 27),
    _WfLlc2InterfaceDynWin_Type()
)
wfLlc2InterfaceDynWin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlc2InterfaceDynWin.setStatus("mandatory")


class _WfLlcInterfaceCurrentLinks_Type(Integer32):
    """Custom type wfLlcInterfaceCurrentLinks based on Integer32"""
    defaultValue = 0


_WfLlcInterfaceCurrentLinks_Object = MibTableColumn
wfLlcInterfaceCurrentLinks = _WfLlcInterfaceCurrentLinks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 28),
    _WfLlcInterfaceCurrentLinks_Type()
)
wfLlcInterfaceCurrentLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcInterfaceCurrentLinks.setStatus("mandatory")


class _WfLlcInterfaceHiWaterLinks_Type(Integer32):
    """Custom type wfLlcInterfaceHiWaterLinks based on Integer32"""
    defaultValue = 0


_WfLlcInterfaceHiWaterLinks_Object = MibTableColumn
wfLlcInterfaceHiWaterLinks = _WfLlcInterfaceHiWaterLinks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 29),
    _WfLlcInterfaceHiWaterLinks_Type()
)
wfLlcInterfaceHiWaterLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcInterfaceHiWaterLinks.setStatus("mandatory")


class _WfLlcInterfaceHiWaterReset_Type(Integer32):
    """Custom type wfLlcInterfaceHiWaterReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_WfLlcInterfaceHiWaterReset_Type.__name__ = "Integer32"
_WfLlcInterfaceHiWaterReset_Object = MibTableColumn
wfLlcInterfaceHiWaterReset = _WfLlcInterfaceHiWaterReset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 30),
    _WfLlcInterfaceHiWaterReset_Type()
)
wfLlcInterfaceHiWaterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlcInterfaceHiWaterReset.setStatus("mandatory")


class _WfLlcInterfaceFrSapTranslation_Type(Integer32):
    """Custom type wfLlcInterfaceFrSapTranslation based on Integer32"""
    defaultValue = 2

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


_WfLlcInterfaceFrSapTranslation_Type.__name__ = "Integer32"
_WfLlcInterfaceFrSapTranslation_Object = MibTableColumn
wfLlcInterfaceFrSapTranslation = _WfLlcInterfaceFrSapTranslation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 2, 1, 31),
    _WfLlcInterfaceFrSapTranslation_Type()
)
wfLlcInterfaceFrSapTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlcInterfaceFrSapTranslation.setStatus("mandatory")
_WfLlcSapTable_Object = MibTable
wfLlcSapTable = _WfLlcSapTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 3)
)
if mibBuilder.loadTexts:
    wfLlcSapTable.setStatus("mandatory")
_WfLlcSapEntry_Object = MibTableRow
wfLlcSapEntry = _WfLlcSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 3, 1)
)
wfLlcSapEntry.setIndexNames(
    (0, "Wellfleet-LLC-MIB", "wfLlcSapCircuit"),
    (0, "Wellfleet-LLC-MIB", "wfLlcSapValue"),
)
if mibBuilder.loadTexts:
    wfLlcSapEntry.setStatus("mandatory")
_WfLlcSapCircuit_Type = Integer32
_WfLlcSapCircuit_Object = MibTableColumn
wfLlcSapCircuit = _WfLlcSapCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 3, 1, 1),
    _WfLlcSapCircuit_Type()
)
wfLlcSapCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcSapCircuit.setStatus("mandatory")
_WfLlcSapValue_Type = Integer32
_WfLlcSapValue_Object = MibTableColumn
wfLlcSapValue = _WfLlcSapValue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 3, 1, 2),
    _WfLlcSapValue_Type()
)
wfLlcSapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcSapValue.setStatus("mandatory")
_WfLlcLinkTable_Object = MibTable
wfLlcLinkTable = _WfLlcLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4)
)
if mibBuilder.loadTexts:
    wfLlcLinkTable.setStatus("mandatory")
_WfLlcLinkEntry_Object = MibTableRow
wfLlcLinkEntry = _WfLlcLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1)
)
wfLlcLinkEntry.setIndexNames(
    (0, "Wellfleet-LLC-MIB", "wfLlcLinkCircuit"),
    (0, "Wellfleet-LLC-MIB", "wfLlcLinkDestMadr"),
    (0, "Wellfleet-LLC-MIB", "wfLlcLinkSrcMadr"),
    (0, "Wellfleet-LLC-MIB", "wfLlcLinkDsap"),
    (0, "Wellfleet-LLC-MIB", "wfLlcLinkSsap"),
)
if mibBuilder.loadTexts:
    wfLlcLinkEntry.setStatus("mandatory")
_WfLlcLinkCircuit_Type = Integer32
_WfLlcLinkCircuit_Object = MibTableColumn
wfLlcLinkCircuit = _WfLlcLinkCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1, 1),
    _WfLlcLinkCircuit_Type()
)
wfLlcLinkCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcLinkCircuit.setStatus("mandatory")


class _WfLlcLinkDestMadr_Type(OctetString):
    """Custom type wfLlcLinkDestMadr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfLlcLinkDestMadr_Type.__name__ = "OctetString"
_WfLlcLinkDestMadr_Object = MibTableColumn
wfLlcLinkDestMadr = _WfLlcLinkDestMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1, 2),
    _WfLlcLinkDestMadr_Type()
)
wfLlcLinkDestMadr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcLinkDestMadr.setStatus("mandatory")


class _WfLlcLinkSrcMadr_Type(OctetString):
    """Custom type wfLlcLinkSrcMadr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfLlcLinkSrcMadr_Type.__name__ = "OctetString"
_WfLlcLinkSrcMadr_Object = MibTableColumn
wfLlcLinkSrcMadr = _WfLlcLinkSrcMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1, 3),
    _WfLlcLinkSrcMadr_Type()
)
wfLlcLinkSrcMadr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcLinkSrcMadr.setStatus("mandatory")
_WfLlcLinkDsap_Type = Integer32
_WfLlcLinkDsap_Object = MibTableColumn
wfLlcLinkDsap = _WfLlcLinkDsap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1, 4),
    _WfLlcLinkDsap_Type()
)
wfLlcLinkDsap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcLinkDsap.setStatus("mandatory")
_WfLlcLinkSsap_Type = Integer32
_WfLlcLinkSsap_Object = MibTableColumn
wfLlcLinkSsap = _WfLlcLinkSsap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1, 5),
    _WfLlcLinkSsap_Type()
)
wfLlcLinkSsap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcLinkSsap.setStatus("mandatory")
_WfLlcInfoRxCnt_Type = Counter32
_WfLlcInfoRxCnt_Object = MibTableColumn
wfLlcInfoRxCnt = _WfLlcInfoRxCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1, 6),
    _WfLlcInfoRxCnt_Type()
)
wfLlcInfoRxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcInfoRxCnt.setStatus("mandatory")
_WfLlcInfoTxCnt_Type = Counter32
_WfLlcInfoTxCnt_Object = MibTableColumn
wfLlcInfoTxCnt = _WfLlcInfoTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1, 7),
    _WfLlcInfoTxCnt_Type()
)
wfLlcInfoTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcInfoTxCnt.setStatus("mandatory")
_WfLlcInfoReXmitCnt_Type = Counter32
_WfLlcInfoReXmitCnt_Object = MibTableColumn
wfLlcInfoReXmitCnt = _WfLlcInfoReXmitCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1, 8),
    _WfLlcInfoReXmitCnt_Type()
)
wfLlcInfoReXmitCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcInfoReXmitCnt.setStatus("mandatory")
_WfLlcByteInfoRxCnt_Type = Counter32
_WfLlcByteInfoRxCnt_Object = MibTableColumn
wfLlcByteInfoRxCnt = _WfLlcByteInfoRxCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1, 9),
    _WfLlcByteInfoRxCnt_Type()
)
wfLlcByteInfoRxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcByteInfoRxCnt.setStatus("mandatory")
_WfLlcByteInfoTxCnt_Type = Counter32
_WfLlcByteInfoTxCnt_Object = MibTableColumn
wfLlcByteInfoTxCnt = _WfLlcByteInfoTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1, 10),
    _WfLlcByteInfoTxCnt_Type()
)
wfLlcByteInfoTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcByteInfoTxCnt.setStatus("mandatory")
_WfLlcRrRxCnt_Type = Counter32
_WfLlcRrRxCnt_Object = MibTableColumn
wfLlcRrRxCnt = _WfLlcRrRxCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1, 11),
    _WfLlcRrRxCnt_Type()
)
wfLlcRrRxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcRrRxCnt.setStatus("mandatory")
_WfLlcRrTxCnt_Type = Counter32
_WfLlcRrTxCnt_Object = MibTableColumn
wfLlcRrTxCnt = _WfLlcRrTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1, 12),
    _WfLlcRrTxCnt_Type()
)
wfLlcRrTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcRrTxCnt.setStatus("mandatory")
_WfLlcRnrRxCnt_Type = Counter32
_WfLlcRnrRxCnt_Object = MibTableColumn
wfLlcRnrRxCnt = _WfLlcRnrRxCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1, 13),
    _WfLlcRnrRxCnt_Type()
)
wfLlcRnrRxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcRnrRxCnt.setStatus("mandatory")
_WfLlcRnrTxCnt_Type = Counter32
_WfLlcRnrTxCnt_Object = MibTableColumn
wfLlcRnrTxCnt = _WfLlcRnrTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1, 14),
    _WfLlcRnrTxCnt_Type()
)
wfLlcRnrTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcRnrTxCnt.setStatus("mandatory")
_WfLlcRejRxCnt_Type = Counter32
_WfLlcRejRxCnt_Object = MibTableColumn
wfLlcRejRxCnt = _WfLlcRejRxCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1, 15),
    _WfLlcRejRxCnt_Type()
)
wfLlcRejRxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcRejRxCnt.setStatus("mandatory")
_WfLlcRejTxCnt_Type = Counter32
_WfLlcRejTxCnt_Object = MibTableColumn
wfLlcRejTxCnt = _WfLlcRejTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1, 16),
    _WfLlcRejTxCnt_Type()
)
wfLlcRejTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcRejTxCnt.setStatus("mandatory")
_WfLlcFrmrRxCnt_Type = Counter32
_WfLlcFrmrRxCnt_Object = MibTableColumn
wfLlcFrmrRxCnt = _WfLlcFrmrRxCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1, 17),
    _WfLlcFrmrRxCnt_Type()
)
wfLlcFrmrRxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcFrmrRxCnt.setStatus("mandatory")
_WfLlcFrmrTxCnt_Type = Counter32
_WfLlcFrmrTxCnt_Object = MibTableColumn
wfLlcFrmrTxCnt = _WfLlcFrmrTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1, 18),
    _WfLlcFrmrTxCnt_Type()
)
wfLlcFrmrTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcFrmrTxCnt.setStatus("mandatory")
_WfLlcFlowDefersCnt_Type = Counter32
_WfLlcFlowDefersCnt_Object = MibTableColumn
wfLlcFlowDefersCnt = _WfLlcFlowDefersCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1, 19),
    _WfLlcFlowDefersCnt_Type()
)
wfLlcFlowDefersCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcFlowDefersCnt.setStatus("mandatory")
_WfLlcWaitAckTimeouts_Type = Counter32
_WfLlcWaitAckTimeouts_Object = MibTableColumn
wfLlcWaitAckTimeouts = _WfLlcWaitAckTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1, 20),
    _WfLlcWaitAckTimeouts_Type()
)
wfLlcWaitAckTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcWaitAckTimeouts.setStatus("mandatory")
_WfLlcRejectTimeouts_Type = Counter32
_WfLlcRejectTimeouts_Object = MibTableColumn
wfLlcRejectTimeouts = _WfLlcRejectTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1, 21),
    _WfLlcRejectTimeouts_Type()
)
wfLlcRejectTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcRejectTimeouts.setStatus("mandatory")
_WfLlcPollCycleTimeouts_Type = Counter32
_WfLlcPollCycleTimeouts_Object = MibTableColumn
wfLlcPollCycleTimeouts = _WfLlcPollCycleTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1, 22),
    _WfLlcPollCycleTimeouts_Type()
)
wfLlcPollCycleTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcPollCycleTimeouts.setStatus("mandatory")
_WfLlcStateChangeCnt_Type = Counter32
_WfLlcStateChangeCnt_Object = MibTableColumn
wfLlcStateChangeCnt = _WfLlcStateChangeCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1, 23),
    _WfLlcStateChangeCnt_Type()
)
wfLlcStateChangeCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcStateChangeCnt.setStatus("mandatory")
_WfLlcLastChangeReason_Type = Counter32
_WfLlcLastChangeReason_Object = MibTableColumn
wfLlcLastChangeReason = _WfLlcLastChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1, 24),
    _WfLlcLastChangeReason_Type()
)
wfLlcLastChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcLastChangeReason.setStatus("mandatory")
_WfLlcCurrentState_Type = Counter32
_WfLlcCurrentState_Object = MibTableColumn
wfLlcCurrentState = _WfLlcCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 4, 1, 25),
    _WfLlcCurrentState_Type()
)
wfLlcCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcCurrentState.setStatus("mandatory")
_WfLlc2TrafficFilterTable_Object = MibTable
wfLlc2TrafficFilterTable = _WfLlc2TrafficFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 8)
)
if mibBuilder.loadTexts:
    wfLlc2TrafficFilterTable.setStatus("mandatory")
_WfLlc2TrafficFilterEntry_Object = MibTableRow
wfLlc2TrafficFilterEntry = _WfLlc2TrafficFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 8, 1)
)
wfLlc2TrafficFilterEntry.setIndexNames(
    (0, "Wellfleet-LLC-MIB", "wfLlc2TrafficFilterCircuit"),
    (0, "Wellfleet-LLC-MIB", "wfLlc2TrafficFilterRuleNumber"),
    (0, "Wellfleet-LLC-MIB", "wfLlc2TrafficFilterFragment"),
)
if mibBuilder.loadTexts:
    wfLlc2TrafficFilterEntry.setStatus("mandatory")


class _WfLlc2TrafficFilterCreate_Type(Integer32):
    """Custom type wfLlc2TrafficFilterCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfLlc2TrafficFilterCreate_Type.__name__ = "Integer32"
_WfLlc2TrafficFilterCreate_Object = MibTableColumn
wfLlc2TrafficFilterCreate = _WfLlc2TrafficFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 8, 1, 1),
    _WfLlc2TrafficFilterCreate_Type()
)
wfLlc2TrafficFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlc2TrafficFilterCreate.setStatus("mandatory")


class _WfLlc2TrafficFilterEnable_Type(Integer32):
    """Custom type wfLlc2TrafficFilterEnable based on Integer32"""
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


_WfLlc2TrafficFilterEnable_Type.__name__ = "Integer32"
_WfLlc2TrafficFilterEnable_Object = MibTableColumn
wfLlc2TrafficFilterEnable = _WfLlc2TrafficFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 8, 1, 2),
    _WfLlc2TrafficFilterEnable_Type()
)
wfLlc2TrafficFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlc2TrafficFilterEnable.setStatus("mandatory")


class _WfLlc2TrafficFilterStatus_Type(Integer32):
    """Custom type wfLlc2TrafficFilterStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("error", 2),
          ("inactive", 3))
    )


_WfLlc2TrafficFilterStatus_Type.__name__ = "Integer32"
_WfLlc2TrafficFilterStatus_Object = MibTableColumn
wfLlc2TrafficFilterStatus = _WfLlc2TrafficFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 8, 1, 3),
    _WfLlc2TrafficFilterStatus_Type()
)
wfLlc2TrafficFilterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlc2TrafficFilterStatus.setStatus("mandatory")
_WfLlc2TrafficFilterCounter_Type = Counter32
_WfLlc2TrafficFilterCounter_Object = MibTableColumn
wfLlc2TrafficFilterCounter = _WfLlc2TrafficFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 8, 1, 4),
    _WfLlc2TrafficFilterCounter_Type()
)
wfLlc2TrafficFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlc2TrafficFilterCounter.setStatus("mandatory")
_WfLlc2TrafficFilterDefinition_Type = OctetString
_WfLlc2TrafficFilterDefinition_Object = MibTableColumn
wfLlc2TrafficFilterDefinition = _WfLlc2TrafficFilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 8, 1, 5),
    _WfLlc2TrafficFilterDefinition_Type()
)
wfLlc2TrafficFilterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlc2TrafficFilterDefinition.setStatus("mandatory")
_WfLlc2TrafficFilterReserved_Type = Integer32
_WfLlc2TrafficFilterReserved_Object = MibTableColumn
wfLlc2TrafficFilterReserved = _WfLlc2TrafficFilterReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 8, 1, 6),
    _WfLlc2TrafficFilterReserved_Type()
)
wfLlc2TrafficFilterReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlc2TrafficFilterReserved.setStatus("mandatory")
_WfLlc2TrafficFilterCircuit_Type = Integer32
_WfLlc2TrafficFilterCircuit_Object = MibTableColumn
wfLlc2TrafficFilterCircuit = _WfLlc2TrafficFilterCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 8, 1, 7),
    _WfLlc2TrafficFilterCircuit_Type()
)
wfLlc2TrafficFilterCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlc2TrafficFilterCircuit.setStatus("mandatory")
_WfLlc2TrafficFilterRuleNumber_Type = Integer32
_WfLlc2TrafficFilterRuleNumber_Object = MibTableColumn
wfLlc2TrafficFilterRuleNumber = _WfLlc2TrafficFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 8, 1, 8),
    _WfLlc2TrafficFilterRuleNumber_Type()
)
wfLlc2TrafficFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlc2TrafficFilterRuleNumber.setStatus("mandatory")
_WfLlc2TrafficFilterFragment_Type = Integer32
_WfLlc2TrafficFilterFragment_Object = MibTableColumn
wfLlc2TrafficFilterFragment = _WfLlc2TrafficFilterFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 8, 1, 9),
    _WfLlc2TrafficFilterFragment_Type()
)
wfLlc2TrafficFilterFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlc2TrafficFilterFragment.setStatus("mandatory")
_WfLlc2TrafficFilterName_Type = DisplayString
_WfLlc2TrafficFilterName_Object = MibTableColumn
wfLlc2TrafficFilterName = _WfLlc2TrafficFilterName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 8, 1, 10),
    _WfLlc2TrafficFilterName_Type()
)
wfLlc2TrafficFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlc2TrafficFilterName.setStatus("mandatory")
_WfLlcDlciTable_Object = MibTable
wfLlcDlciTable = _WfLlcDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 9)
)
if mibBuilder.loadTexts:
    wfLlcDlciTable.setStatus("mandatory")
_WfLlcDlciEntry_Object = MibTableRow
wfLlcDlciEntry = _WfLlcDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 9, 1)
)
wfLlcDlciEntry.setIndexNames(
    (0, "Wellfleet-LLC-MIB", "wfLlcDlciCct"),
    (0, "Wellfleet-LLC-MIB", "wfLlcDlciNum"),
)
if mibBuilder.loadTexts:
    wfLlcDlciEntry.setStatus("mandatory")


class _WfLlcDlciDelete_Type(Integer32):
    """Custom type wfLlcDlciDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfLlcDlciDelete_Type.__name__ = "Integer32"
_WfLlcDlciDelete_Object = MibTableColumn
wfLlcDlciDelete = _WfLlcDlciDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 9, 1, 1),
    _WfLlcDlciDelete_Type()
)
wfLlcDlciDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlcDlciDelete.setStatus("mandatory")
_WfLlcDlciCct_Type = Integer32
_WfLlcDlciCct_Object = MibTableColumn
wfLlcDlciCct = _WfLlcDlciCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 9, 1, 2),
    _WfLlcDlciCct_Type()
)
wfLlcDlciCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcDlciCct.setStatus("mandatory")
_WfLlcDlciNum_Type = Integer32
_WfLlcDlciNum_Object = MibTableColumn
wfLlcDlciNum = _WfLlcDlciNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 9, 1, 3),
    _WfLlcDlciNum_Type()
)
wfLlcDlciNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcDlciNum.setStatus("mandatory")
_WfLlcDlciLocalMac_Type = OctetString
_WfLlcDlciLocalMac_Object = MibTableColumn
wfLlcDlciLocalMac = _WfLlcDlciLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 9, 1, 4),
    _WfLlcDlciLocalMac_Type()
)
wfLlcDlciLocalMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlcDlciLocalMac.setStatus("mandatory")
_WfLlcDlciRemoteMac_Type = OctetString
_WfLlcDlciRemoteMac_Object = MibTableColumn
wfLlcDlciRemoteMac = _WfLlcDlciRemoteMac_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 9, 1, 5),
    _WfLlcDlciRemoteMac_Type()
)
wfLlcDlciRemoteMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlcDlciRemoteMac.setStatus("mandatory")
_WfLlcFrSvcTable_Object = MibTable
wfLlcFrSvcTable = _WfLlcFrSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 10)
)
if mibBuilder.loadTexts:
    wfLlcFrSvcTable.setStatus("mandatory")
_WfLlcFrSvcEntry_Object = MibTableRow
wfLlcFrSvcEntry = _WfLlcFrSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 10, 1)
)
wfLlcFrSvcEntry.setIndexNames(
    (0, "Wellfleet-LLC-MIB", "wfLlcFrSvcCct"),
    (0, "Wellfleet-LLC-MIB", "wfLlcFrSvcMac"),
)
if mibBuilder.loadTexts:
    wfLlcFrSvcEntry.setStatus("mandatory")


class _WfLlcFrSvcDelete_Type(Integer32):
    """Custom type wfLlcFrSvcDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfLlcFrSvcDelete_Type.__name__ = "Integer32"
_WfLlcFrSvcDelete_Object = MibTableColumn
wfLlcFrSvcDelete = _WfLlcFrSvcDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 10, 1, 1),
    _WfLlcFrSvcDelete_Type()
)
wfLlcFrSvcDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlcFrSvcDelete.setStatus("mandatory")
_WfLlcFrSvcCct_Type = Integer32
_WfLlcFrSvcCct_Object = MibTableColumn
wfLlcFrSvcCct = _WfLlcFrSvcCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 10, 1, 2),
    _WfLlcFrSvcCct_Type()
)
wfLlcFrSvcCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcFrSvcCct.setStatus("mandatory")


class _WfLlcFrSvcMac_Type(OctetString):
    """Custom type wfLlcFrSvcMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfLlcFrSvcMac_Type.__name__ = "OctetString"
_WfLlcFrSvcMac_Object = MibTableColumn
wfLlcFrSvcMac = _WfLlcFrSvcMac_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 10, 1, 3),
    _WfLlcFrSvcMac_Type()
)
wfLlcFrSvcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLlcFrSvcMac.setStatus("mandatory")


class _WfLlcFrSvcMappingType_Type(Integer32):
    """Custom type wfLlcFrSvcMappingType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_WfLlcFrSvcMappingType_Type.__name__ = "Integer32"
_WfLlcFrSvcMappingType_Object = MibTableColumn
wfLlcFrSvcMappingType = _WfLlcFrSvcMappingType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 10, 1, 4),
    _WfLlcFrSvcMappingType_Type()
)
wfLlcFrSvcMappingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlcFrSvcMappingType.setStatus("mandatory")
_WfLlcFrSvcX121Addr_Type = DisplayString
_WfLlcFrSvcX121Addr_Object = MibTableColumn
wfLlcFrSvcX121Addr = _WfLlcFrSvcX121Addr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 10, 1, 5),
    _WfLlcFrSvcX121Addr_Type()
)
wfLlcFrSvcX121Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlcFrSvcX121Addr.setStatus("mandatory")
_WfLlcFrSvcSubAddr_Type = DisplayString
_WfLlcFrSvcSubAddr_Object = MibTableColumn
wfLlcFrSvcSubAddr = _WfLlcFrSvcSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 10, 1, 6),
    _WfLlcFrSvcSubAddr_Type()
)
wfLlcFrSvcSubAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlcFrSvcSubAddr.setStatus("mandatory")


class _WfLlcFrSvcPlan_Type(Integer32):
    """Custom type wfLlcFrSvcPlan based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 3))
    )


_WfLlcFrSvcPlan_Type.__name__ = "Integer32"
_WfLlcFrSvcPlan_Object = MibTableColumn
wfLlcFrSvcPlan = _WfLlcFrSvcPlan_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 10, 1, 7),
    _WfLlcFrSvcPlan_Type()
)
wfLlcFrSvcPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlcFrSvcPlan.setStatus("mandatory")


class _WfLlcFrSvcTypeOfNumber_Type(Integer32):
    """Custom type wfLlcFrSvcTypeOfNumber based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("international", 2),
          ("unknown", 1))
    )


_WfLlcFrSvcTypeOfNumber_Type.__name__ = "Integer32"
_WfLlcFrSvcTypeOfNumber_Object = MibTableColumn
wfLlcFrSvcTypeOfNumber = _WfLlcFrSvcTypeOfNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6, 10, 1, 8),
    _WfLlcFrSvcTypeOfNumber_Type()
)
wfLlcFrSvcTypeOfNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLlcFrSvcTypeOfNumber.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-LLC-MIB",
    **{"wfLlc": wfLlc,
       "wfLlcBaseDelete": wfLlcBaseDelete,
       "wfLlcBaseDisable": wfLlcBaseDisable,
       "wfLlcBaseState": wfLlcBaseState,
       "wfLlcInterfaceTable": wfLlcInterfaceTable,
       "wfLlcInterfaceEntry": wfLlcInterfaceEntry,
       "wfLlcInterfaceDelete": wfLlcInterfaceDelete,
       "wfLlcInterfaceDisable": wfLlcInterfaceDisable,
       "wfLlcInterfaceState": wfLlcInterfaceState,
       "wfLlcInterfaceCircuit": wfLlcInterfaceCircuit,
       "wfLlcInterfaceLlc2CctId": wfLlcInterfaceLlc2CctId,
       "wfLlc1InterfaceMaxUinfoSize": wfLlc1InterfaceMaxUinfoSize,
       "wfLlc1InterfaceMaxRetry": wfLlc1InterfaceMaxRetry,
       "wfLlc1InterfaceTAckWait": wfLlc1InterfaceTAckWait,
       "wfLlc2InterfaceMaxInfoSize": wfLlc2InterfaceMaxInfoSize,
       "wfLlc2InterfaceK": wfLlc2InterfaceK,
       "wfLlc2InterfaceN2": wfLlc2InterfaceN2,
       "wfLlc2InterfaceN3": wfLlc2InterfaceN3,
       "wfLlc2InterfaceTAckWait": wfLlc2InterfaceTAckWait,
       "wfLlc2InterfaceTReject": wfLlc2InterfaceTReject,
       "wfLlc2InterfaceTRemoteBusy": wfLlc2InterfaceTRemoteBusy,
       "wfLlc2InterfaceTRspAck": wfLlc2InterfaceTRspAck,
       "wfLlc2InterfaceTIdle": wfLlc2InterfaceTIdle,
       "wfLlc2InterfaceTPollCycle": wfLlc2InterfaceTPollCycle,
       "wfLlcInterfaceMaxNumOfSap": wfLlcInterfaceMaxNumOfSap,
       "wfLlcInterfaceMaxNumOfLink": wfLlcInterfaceMaxNumOfLink,
       "wfLlcInterfaceDupAddrCheck": wfLlcInterfaceDupAddrCheck,
       "wfLlc2InterfaceRW": wfLlc2InterfaceRW,
       "wfLlc2InterfaceTW": wfLlc2InterfaceTW,
       "wfLlcInterfaceEncapsType": wfLlcInterfaceEncapsType,
       "wfLlcInterfaceSrbRingId": wfLlcInterfaceSrbRingId,
       "wfLlcInterfaceFrVMask": wfLlcInterfaceFrVMask,
       "wfLlc2InterfaceDynWin": wfLlc2InterfaceDynWin,
       "wfLlcInterfaceCurrentLinks": wfLlcInterfaceCurrentLinks,
       "wfLlcInterfaceHiWaterLinks": wfLlcInterfaceHiWaterLinks,
       "wfLlcInterfaceHiWaterReset": wfLlcInterfaceHiWaterReset,
       "wfLlcInterfaceFrSapTranslation": wfLlcInterfaceFrSapTranslation,
       "wfLlcSapTable": wfLlcSapTable,
       "wfLlcSapEntry": wfLlcSapEntry,
       "wfLlcSapCircuit": wfLlcSapCircuit,
       "wfLlcSapValue": wfLlcSapValue,
       "wfLlcLinkTable": wfLlcLinkTable,
       "wfLlcLinkEntry": wfLlcLinkEntry,
       "wfLlcLinkCircuit": wfLlcLinkCircuit,
       "wfLlcLinkDestMadr": wfLlcLinkDestMadr,
       "wfLlcLinkSrcMadr": wfLlcLinkSrcMadr,
       "wfLlcLinkDsap": wfLlcLinkDsap,
       "wfLlcLinkSsap": wfLlcLinkSsap,
       "wfLlcInfoRxCnt": wfLlcInfoRxCnt,
       "wfLlcInfoTxCnt": wfLlcInfoTxCnt,
       "wfLlcInfoReXmitCnt": wfLlcInfoReXmitCnt,
       "wfLlcByteInfoRxCnt": wfLlcByteInfoRxCnt,
       "wfLlcByteInfoTxCnt": wfLlcByteInfoTxCnt,
       "wfLlcRrRxCnt": wfLlcRrRxCnt,
       "wfLlcRrTxCnt": wfLlcRrTxCnt,
       "wfLlcRnrRxCnt": wfLlcRnrRxCnt,
       "wfLlcRnrTxCnt": wfLlcRnrTxCnt,
       "wfLlcRejRxCnt": wfLlcRejRxCnt,
       "wfLlcRejTxCnt": wfLlcRejTxCnt,
       "wfLlcFrmrRxCnt": wfLlcFrmrRxCnt,
       "wfLlcFrmrTxCnt": wfLlcFrmrTxCnt,
       "wfLlcFlowDefersCnt": wfLlcFlowDefersCnt,
       "wfLlcWaitAckTimeouts": wfLlcWaitAckTimeouts,
       "wfLlcRejectTimeouts": wfLlcRejectTimeouts,
       "wfLlcPollCycleTimeouts": wfLlcPollCycleTimeouts,
       "wfLlcStateChangeCnt": wfLlcStateChangeCnt,
       "wfLlcLastChangeReason": wfLlcLastChangeReason,
       "wfLlcCurrentState": wfLlcCurrentState,
       "wfLlc2TrafficFilterTable": wfLlc2TrafficFilterTable,
       "wfLlc2TrafficFilterEntry": wfLlc2TrafficFilterEntry,
       "wfLlc2TrafficFilterCreate": wfLlc2TrafficFilterCreate,
       "wfLlc2TrafficFilterEnable": wfLlc2TrafficFilterEnable,
       "wfLlc2TrafficFilterStatus": wfLlc2TrafficFilterStatus,
       "wfLlc2TrafficFilterCounter": wfLlc2TrafficFilterCounter,
       "wfLlc2TrafficFilterDefinition": wfLlc2TrafficFilterDefinition,
       "wfLlc2TrafficFilterReserved": wfLlc2TrafficFilterReserved,
       "wfLlc2TrafficFilterCircuit": wfLlc2TrafficFilterCircuit,
       "wfLlc2TrafficFilterRuleNumber": wfLlc2TrafficFilterRuleNumber,
       "wfLlc2TrafficFilterFragment": wfLlc2TrafficFilterFragment,
       "wfLlc2TrafficFilterName": wfLlc2TrafficFilterName,
       "wfLlcDlciTable": wfLlcDlciTable,
       "wfLlcDlciEntry": wfLlcDlciEntry,
       "wfLlcDlciDelete": wfLlcDlciDelete,
       "wfLlcDlciCct": wfLlcDlciCct,
       "wfLlcDlciNum": wfLlcDlciNum,
       "wfLlcDlciLocalMac": wfLlcDlciLocalMac,
       "wfLlcDlciRemoteMac": wfLlcDlciRemoteMac,
       "wfLlcFrSvcTable": wfLlcFrSvcTable,
       "wfLlcFrSvcEntry": wfLlcFrSvcEntry,
       "wfLlcFrSvcDelete": wfLlcFrSvcDelete,
       "wfLlcFrSvcCct": wfLlcFrSvcCct,
       "wfLlcFrSvcMac": wfLlcFrSvcMac,
       "wfLlcFrSvcMappingType": wfLlcFrSvcMappingType,
       "wfLlcFrSvcX121Addr": wfLlcFrSvcX121Addr,
       "wfLlcFrSvcSubAddr": wfLlcFrSvcSubAddr,
       "wfLlcFrSvcPlan": wfLlcFrSvcPlan,
       "wfLlcFrSvcTypeOfNumber": wfLlcFrSvcTypeOfNumber}
)
