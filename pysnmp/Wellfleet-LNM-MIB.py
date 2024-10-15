# SNMP MIB module (Wellfleet-LNM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-LNM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:37 2024
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
 Opaque,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mgmt,
 mib_2) = mibBuilder.importSymbols(
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
    "Opaque",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mgmt",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfLanManagerGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfLanManagerGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfLnm_ObjectIdentity = ObjectIdentity
wfLnm = _WfLnm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 1)
)


class _WfLnmDelete_Type(Integer32):
    """Custom type wfLnmDelete based on Integer32"""
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


_WfLnmDelete_Type.__name__ = "Integer32"
_WfLnmDelete_Object = MibScalar
wfLnmDelete = _WfLnmDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 1, 1),
    _WfLnmDelete_Type()
)
wfLnmDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLnmDelete.setStatus("mandatory")


class _WfLnmDisable_Type(Integer32):
    """Custom type wfLnmDisable based on Integer32"""
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


_WfLnmDisable_Type.__name__ = "Integer32"
_WfLnmDisable_Object = MibScalar
wfLnmDisable = _WfLnmDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 1, 2),
    _WfLnmDisable_Type()
)
wfLnmDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLnmDisable.setStatus("mandatory")


class _WfLnmState_Type(Integer32):
    """Custom type wfLnmState based on Integer32"""
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


_WfLnmState_Type.__name__ = "Integer32"
_WfLnmState_Object = MibScalar
wfLnmState = _WfLnmState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 1, 3),
    _WfLnmState_Type()
)
wfLnmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLnmState.setStatus("mandatory")


class _WfLnmLnmSetsDisable_Type(Integer32):
    """Custom type wfLnmLnmSetsDisable based on Integer32"""
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


_WfLnmLnmSetsDisable_Type.__name__ = "Integer32"
_WfLnmLnmSetsDisable_Object = MibScalar
wfLnmLnmSetsDisable = _WfLnmLnmSetsDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 1, 4),
    _WfLnmLnmSetsDisable_Type()
)
wfLnmLnmSetsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLnmLnmSetsDisable.setStatus("mandatory")
_WfLnmInternalLanId_Type = Integer32
_WfLnmInternalLanId_Object = MibScalar
wfLnmInternalLanId = _WfLnmInternalLanId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 1, 5),
    _WfLnmInternalLanId_Type()
)
wfLnmInternalLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLnmInternalLanId.setStatus("mandatory")
_WfLnmBridgeId_Type = Integer32
_WfLnmBridgeId_Object = MibScalar
wfLnmBridgeId = _WfLnmBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 1, 6),
    _WfLnmBridgeId_Type()
)
wfLnmBridgeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLnmBridgeId.setStatus("mandatory")
_WfLnmInterfaceTable_Object = MibTable
wfLnmInterfaceTable = _WfLnmInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2)
)
if mibBuilder.loadTexts:
    wfLnmInterfaceTable.setStatus("mandatory")
_WfLnmInterfaceEntry_Object = MibTableRow
wfLnmInterfaceEntry = _WfLnmInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1)
)
wfLnmInterfaceEntry.setIndexNames(
    (0, "Wellfleet-LNM-MIB", "wfLnmInterfaceMacCircuit"),
)
if mibBuilder.loadTexts:
    wfLnmInterfaceEntry.setStatus("mandatory")


class _WfLnmInterfaceDelete_Type(Integer32):
    """Custom type wfLnmInterfaceDelete based on Integer32"""
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


_WfLnmInterfaceDelete_Type.__name__ = "Integer32"
_WfLnmInterfaceDelete_Object = MibTableColumn
wfLnmInterfaceDelete = _WfLnmInterfaceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 1),
    _WfLnmInterfaceDelete_Type()
)
wfLnmInterfaceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLnmInterfaceDelete.setStatus("mandatory")


class _WfLnmInterfaceDisable_Type(Integer32):
    """Custom type wfLnmInterfaceDisable based on Integer32"""
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


_WfLnmInterfaceDisable_Type.__name__ = "Integer32"
_WfLnmInterfaceDisable_Object = MibTableColumn
wfLnmInterfaceDisable = _WfLnmInterfaceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 2),
    _WfLnmInterfaceDisable_Type()
)
wfLnmInterfaceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLnmInterfaceDisable.setStatus("mandatory")
_WfLnmInterfaceCircuit_Type = Integer32
_WfLnmInterfaceCircuit_Object = MibTableColumn
wfLnmInterfaceCircuit = _WfLnmInterfaceCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 3),
    _WfLnmInterfaceCircuit_Type()
)
wfLnmInterfaceCircuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLnmInterfaceCircuit.setStatus("mandatory")
_WfLnmInterfaceMacCircuit_Type = Integer32
_WfLnmInterfaceMacCircuit_Object = MibTableColumn
wfLnmInterfaceMacCircuit = _WfLnmInterfaceMacCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 4),
    _WfLnmInterfaceMacCircuit_Type()
)
wfLnmInterfaceMacCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLnmInterfaceMacCircuit.setStatus("mandatory")
_WfLnmInterfaceRemoteMac_Type = OctetString
_WfLnmInterfaceRemoteMac_Object = MibTableColumn
wfLnmInterfaceRemoteMac = _WfLnmInterfaceRemoteMac_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 5),
    _WfLnmInterfaceRemoteMac_Type()
)
wfLnmInterfaceRemoteMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLnmInterfaceRemoteMac.setStatus("mandatory")


class _WfLnmInterfaceLrmDisable_Type(Integer32):
    """Custom type wfLnmInterfaceLrmDisable based on Integer32"""
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


_WfLnmInterfaceLrmDisable_Type.__name__ = "Integer32"
_WfLnmInterfaceLrmDisable_Object = MibTableColumn
wfLnmInterfaceLrmDisable = _WfLnmInterfaceLrmDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 6),
    _WfLnmInterfaceLrmDisable_Type()
)
wfLnmInterfaceLrmDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLnmInterfaceLrmDisable.setStatus("mandatory")


class _WfLnmInterfaceLrmState_Type(Integer32):
    """Custom type wfLnmInterfaceLrmState based on Integer32"""
    defaultValue = 4

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


_WfLnmInterfaceLrmState_Type.__name__ = "Integer32"
_WfLnmInterfaceLrmState_Object = MibTableColumn
wfLnmInterfaceLrmState = _WfLnmInterfaceLrmState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 7),
    _WfLnmInterfaceLrmState_Type()
)
wfLnmInterfaceLrmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLnmInterfaceLrmState.setStatus("mandatory")


class _WfLnmInterfaceLbsState_Type(Integer32):
    """Custom type wfLnmInterfaceLbsState based on Integer32"""
    defaultValue = 4

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


_WfLnmInterfaceLbsState_Type.__name__ = "Integer32"
_WfLnmInterfaceLbsState_Object = MibTableColumn
wfLnmInterfaceLbsState = _WfLnmInterfaceLbsState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 8),
    _WfLnmInterfaceLbsState_Type()
)
wfLnmInterfaceLbsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLnmInterfaceLbsState.setStatus("mandatory")


class _WfLnmInterfaceRemDisable_Type(Integer32):
    """Custom type wfLnmInterfaceRemDisable based on Integer32"""
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


_WfLnmInterfaceRemDisable_Type.__name__ = "Integer32"
_WfLnmInterfaceRemDisable_Object = MibTableColumn
wfLnmInterfaceRemDisable = _WfLnmInterfaceRemDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 9),
    _WfLnmInterfaceRemDisable_Type()
)
wfLnmInterfaceRemDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLnmInterfaceRemDisable.setStatus("mandatory")


class _WfLnmInterfaceRemState_Type(Integer32):
    """Custom type wfLnmInterfaceRemState based on Integer32"""
    defaultValue = 4

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


_WfLnmInterfaceRemState_Type.__name__ = "Integer32"
_WfLnmInterfaceRemState_Object = MibTableColumn
wfLnmInterfaceRemState = _WfLnmInterfaceRemState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 10),
    _WfLnmInterfaceRemState_Type()
)
wfLnmInterfaceRemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLnmInterfaceRemState.setStatus("mandatory")


class _WfLnmInterfaceRpsDisable_Type(Integer32):
    """Custom type wfLnmInterfaceRpsDisable based on Integer32"""
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


_WfLnmInterfaceRpsDisable_Type.__name__ = "Integer32"
_WfLnmInterfaceRpsDisable_Object = MibTableColumn
wfLnmInterfaceRpsDisable = _WfLnmInterfaceRpsDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 11),
    _WfLnmInterfaceRpsDisable_Type()
)
wfLnmInterfaceRpsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLnmInterfaceRpsDisable.setStatus("mandatory")


class _WfLnmInterfaceRpsState_Type(Integer32):
    """Custom type wfLnmInterfaceRpsState based on Integer32"""
    defaultValue = 4

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


_WfLnmInterfaceRpsState_Type.__name__ = "Integer32"
_WfLnmInterfaceRpsState_Object = MibTableColumn
wfLnmInterfaceRpsState = _WfLnmInterfaceRpsState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 12),
    _WfLnmInterfaceRpsState_Type()
)
wfLnmInterfaceRpsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLnmInterfaceRpsState.setStatus("mandatory")


class _WfLnmInterfaceCrsDisable_Type(Integer32):
    """Custom type wfLnmInterfaceCrsDisable based on Integer32"""
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


_WfLnmInterfaceCrsDisable_Type.__name__ = "Integer32"
_WfLnmInterfaceCrsDisable_Object = MibTableColumn
wfLnmInterfaceCrsDisable = _WfLnmInterfaceCrsDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 13),
    _WfLnmInterfaceCrsDisable_Type()
)
wfLnmInterfaceCrsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLnmInterfaceCrsDisable.setStatus("mandatory")


class _WfLnmInterfaceCrsState_Type(Integer32):
    """Custom type wfLnmInterfaceCrsState based on Integer32"""
    defaultValue = 4

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


_WfLnmInterfaceCrsState_Type.__name__ = "Integer32"
_WfLnmInterfaceCrsState_Object = MibTableColumn
wfLnmInterfaceCrsState = _WfLnmInterfaceCrsState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 14),
    _WfLnmInterfaceCrsState_Type()
)
wfLnmInterfaceCrsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLnmInterfaceCrsState.setStatus("mandatory")
_WfLnmInterfaceCtrlMgrPswd_Type = DisplayString
_WfLnmInterfaceCtrlMgrPswd_Object = MibTableColumn
wfLnmInterfaceCtrlMgrPswd = _WfLnmInterfaceCtrlMgrPswd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 15),
    _WfLnmInterfaceCtrlMgrPswd_Type()
)
wfLnmInterfaceCtrlMgrPswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLnmInterfaceCtrlMgrPswd.setStatus("mandatory")
_WfLnmInterfaceOb1MgrPswd_Type = DisplayString
_WfLnmInterfaceOb1MgrPswd_Object = MibTableColumn
wfLnmInterfaceOb1MgrPswd = _WfLnmInterfaceOb1MgrPswd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 16),
    _WfLnmInterfaceOb1MgrPswd_Type()
)
wfLnmInterfaceOb1MgrPswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLnmInterfaceOb1MgrPswd.setStatus("mandatory")
_WfLnmInterfaceOb2MgrPswd_Type = DisplayString
_WfLnmInterfaceOb2MgrPswd_Object = MibTableColumn
wfLnmInterfaceOb2MgrPswd = _WfLnmInterfaceOb2MgrPswd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 17),
    _WfLnmInterfaceOb2MgrPswd_Type()
)
wfLnmInterfaceOb2MgrPswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLnmInterfaceOb2MgrPswd.setStatus("mandatory")
_WfLnmInterfaceOb3MgrPswd_Type = DisplayString
_WfLnmInterfaceOb3MgrPswd_Object = MibTableColumn
wfLnmInterfaceOb3MgrPswd = _WfLnmInterfaceOb3MgrPswd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 18),
    _WfLnmInterfaceOb3MgrPswd_Type()
)
wfLnmInterfaceOb3MgrPswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLnmInterfaceOb3MgrPswd.setStatus("mandatory")
_WfLnmInterfaceCtrlMgrMac_Type = OctetString
_WfLnmInterfaceCtrlMgrMac_Object = MibTableColumn
wfLnmInterfaceCtrlMgrMac = _WfLnmInterfaceCtrlMgrMac_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 19),
    _WfLnmInterfaceCtrlMgrMac_Type()
)
wfLnmInterfaceCtrlMgrMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLnmInterfaceCtrlMgrMac.setStatus("mandatory")
_WfLnmInterfaceOb1MgrMac_Type = OctetString
_WfLnmInterfaceOb1MgrMac_Object = MibTableColumn
wfLnmInterfaceOb1MgrMac = _WfLnmInterfaceOb1MgrMac_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 20),
    _WfLnmInterfaceOb1MgrMac_Type()
)
wfLnmInterfaceOb1MgrMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLnmInterfaceOb1MgrMac.setStatus("mandatory")
_WfLnmInterfaceOb2MgrMac_Type = OctetString
_WfLnmInterfaceOb2MgrMac_Object = MibTableColumn
wfLnmInterfaceOb2MgrMac = _WfLnmInterfaceOb2MgrMac_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 21),
    _WfLnmInterfaceOb2MgrMac_Type()
)
wfLnmInterfaceOb2MgrMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLnmInterfaceOb2MgrMac.setStatus("mandatory")
_WfLnmInterfaceOb3MgrMac_Type = OctetString
_WfLnmInterfaceOb3MgrMac_Object = MibTableColumn
wfLnmInterfaceOb3MgrMac = _WfLnmInterfaceOb3MgrMac_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 22),
    _WfLnmInterfaceOb3MgrMac_Type()
)
wfLnmInterfaceOb3MgrMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLnmInterfaceOb3MgrMac.setStatus("mandatory")


class _WfLnmInterfaceWghtTrshld_Type(Integer32):
    """Custom type wfLnmInterfaceWghtTrshld based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 256),
    )


_WfLnmInterfaceWghtTrshld_Type.__name__ = "Integer32"
_WfLnmInterfaceWghtTrshld_Object = MibTableColumn
wfLnmInterfaceWghtTrshld = _WfLnmInterfaceWghtTrshld_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 23),
    _WfLnmInterfaceWghtTrshld_Type()
)
wfLnmInterfaceWghtTrshld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLnmInterfaceWghtTrshld.setStatus("mandatory")
_WfLnmInterfaceLrmCngstnErrs_Type = Counter32
_WfLnmInterfaceLrmCngstnErrs_Object = MibTableColumn
wfLnmInterfaceLrmCngstnErrs = _WfLnmInterfaceLrmCngstnErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 24),
    _WfLnmInterfaceLrmCngstnErrs_Type()
)
wfLnmInterfaceLrmCngstnErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLnmInterfaceLrmCngstnErrs.setStatus("mandatory")
_WfLnmInterfaceLrmRxErrors_Type = Counter32
_WfLnmInterfaceLrmRxErrors_Object = MibTableColumn
wfLnmInterfaceLrmRxErrors = _WfLnmInterfaceLrmRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 25),
    _WfLnmInterfaceLrmRxErrors_Type()
)
wfLnmInterfaceLrmRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLnmInterfaceLrmRxErrors.setStatus("mandatory")
_WfLnmInterfaceRemRxErrors_Type = Counter32
_WfLnmInterfaceRemRxErrors_Object = MibTableColumn
wfLnmInterfaceRemRxErrors = _WfLnmInterfaceRemRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 26),
    _WfLnmInterfaceRemRxErrors_Type()
)
wfLnmInterfaceRemRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLnmInterfaceRemRxErrors.setStatus("mandatory")
_WfLnmInterfaceRpsRxErrors_Type = Counter32
_WfLnmInterfaceRpsRxErrors_Object = MibTableColumn
wfLnmInterfaceRpsRxErrors = _WfLnmInterfaceRpsRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 27),
    _WfLnmInterfaceRpsRxErrors_Type()
)
wfLnmInterfaceRpsRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLnmInterfaceRpsRxErrors.setStatus("mandatory")
_WfLnmInterfaceCrsRxErrors_Type = Counter32
_WfLnmInterfaceCrsRxErrors_Object = MibTableColumn
wfLnmInterfaceCrsRxErrors = _WfLnmInterfaceCrsRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 28),
    _WfLnmInterfaceCrsRxErrors_Type()
)
wfLnmInterfaceCrsRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLnmInterfaceCrsRxErrors.setStatus("mandatory")
_WfLnmInterfaceLbsRxErrors_Type = Counter32
_WfLnmInterfaceLbsRxErrors_Object = MibTableColumn
wfLnmInterfaceLbsRxErrors = _WfLnmInterfaceLbsRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 29),
    _WfLnmInterfaceLbsRxErrors_Type()
)
wfLnmInterfaceLbsRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLnmInterfaceLbsRxErrors.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-LNM-MIB",
    **{"wfLnm": wfLnm,
       "wfLnmDelete": wfLnmDelete,
       "wfLnmDisable": wfLnmDisable,
       "wfLnmState": wfLnmState,
       "wfLnmLnmSetsDisable": wfLnmLnmSetsDisable,
       "wfLnmInternalLanId": wfLnmInternalLanId,
       "wfLnmBridgeId": wfLnmBridgeId,
       "wfLnmInterfaceTable": wfLnmInterfaceTable,
       "wfLnmInterfaceEntry": wfLnmInterfaceEntry,
       "wfLnmInterfaceDelete": wfLnmInterfaceDelete,
       "wfLnmInterfaceDisable": wfLnmInterfaceDisable,
       "wfLnmInterfaceCircuit": wfLnmInterfaceCircuit,
       "wfLnmInterfaceMacCircuit": wfLnmInterfaceMacCircuit,
       "wfLnmInterfaceRemoteMac": wfLnmInterfaceRemoteMac,
       "wfLnmInterfaceLrmDisable": wfLnmInterfaceLrmDisable,
       "wfLnmInterfaceLrmState": wfLnmInterfaceLrmState,
       "wfLnmInterfaceLbsState": wfLnmInterfaceLbsState,
       "wfLnmInterfaceRemDisable": wfLnmInterfaceRemDisable,
       "wfLnmInterfaceRemState": wfLnmInterfaceRemState,
       "wfLnmInterfaceRpsDisable": wfLnmInterfaceRpsDisable,
       "wfLnmInterfaceRpsState": wfLnmInterfaceRpsState,
       "wfLnmInterfaceCrsDisable": wfLnmInterfaceCrsDisable,
       "wfLnmInterfaceCrsState": wfLnmInterfaceCrsState,
       "wfLnmInterfaceCtrlMgrPswd": wfLnmInterfaceCtrlMgrPswd,
       "wfLnmInterfaceOb1MgrPswd": wfLnmInterfaceOb1MgrPswd,
       "wfLnmInterfaceOb2MgrPswd": wfLnmInterfaceOb2MgrPswd,
       "wfLnmInterfaceOb3MgrPswd": wfLnmInterfaceOb3MgrPswd,
       "wfLnmInterfaceCtrlMgrMac": wfLnmInterfaceCtrlMgrMac,
       "wfLnmInterfaceOb1MgrMac": wfLnmInterfaceOb1MgrMac,
       "wfLnmInterfaceOb2MgrMac": wfLnmInterfaceOb2MgrMac,
       "wfLnmInterfaceOb3MgrMac": wfLnmInterfaceOb3MgrMac,
       "wfLnmInterfaceWghtTrshld": wfLnmInterfaceWghtTrshld,
       "wfLnmInterfaceLrmCngstnErrs": wfLnmInterfaceLrmCngstnErrs,
       "wfLnmInterfaceLrmRxErrors": wfLnmInterfaceLrmRxErrors,
       "wfLnmInterfaceRemRxErrors": wfLnmInterfaceRemRxErrors,
       "wfLnmInterfaceRpsRxErrors": wfLnmInterfaceRpsRxErrors,
       "wfLnmInterfaceCrsRxErrors": wfLnmInterfaceCrsRxErrors,
       "wfLnmInterfaceLbsRxErrors": wfLnmInterfaceLbsRxErrors}
)
