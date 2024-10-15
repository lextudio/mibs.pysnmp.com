# SNMP MIB module (Wellfleet-IPSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-IPSEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:29 2024
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfIpsecGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfIpsecGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfIpsecBase_ObjectIdentity = ObjectIdentity
wfIpsecBase = _WfIpsecBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 1)
)


class _WfIpsecBaseCreate_Type(Integer32):
    """Custom type wfIpsecBaseCreate based on Integer32"""
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


_WfIpsecBaseCreate_Type.__name__ = "Integer32"
_WfIpsecBaseCreate_Object = MibScalar
wfIpsecBaseCreate = _WfIpsecBaseCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 1, 1),
    _WfIpsecBaseCreate_Type()
)
wfIpsecBaseCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecBaseCreate.setStatus("mandatory")


class _WfIpsecBaseEnable_Type(Integer32):
    """Custom type wfIpsecBaseEnable based on Integer32"""
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


_WfIpsecBaseEnable_Type.__name__ = "Integer32"
_WfIpsecBaseEnable_Object = MibScalar
wfIpsecBaseEnable = _WfIpsecBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 1, 2),
    _WfIpsecBaseEnable_Type()
)
wfIpsecBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecBaseEnable.setStatus("mandatory")


class _WfIpsecBaseState_Type(Integer32):
    """Custom type wfIpsecBaseState based on Integer32"""
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
        *(("down", 2),
          ("notpresent", 3),
          ("up", 1))
    )


_WfIpsecBaseState_Type.__name__ = "Integer32"
_WfIpsecBaseState_Object = MibScalar
wfIpsecBaseState = _WfIpsecBaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 1, 3),
    _WfIpsecBaseState_Type()
)
wfIpsecBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecBaseState.setStatus("mandatory")


class _WfIpsecBaseEspEncipherEnable_Type(Integer32):
    """Custom type wfIpsecBaseEspEncipherEnable based on Integer32"""
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


_WfIpsecBaseEspEncipherEnable_Type.__name__ = "Integer32"
_WfIpsecBaseEspEncipherEnable_Object = MibScalar
wfIpsecBaseEspEncipherEnable = _WfIpsecBaseEspEncipherEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 1, 4),
    _WfIpsecBaseEspEncipherEnable_Type()
)
wfIpsecBaseEspEncipherEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecBaseEspEncipherEnable.setStatus("mandatory")


class _WfIpsecBaseMaxManualSpi_Type(Integer32):
    """Custom type wfIpsecBaseMaxManualSpi based on Integer32"""
    defaultValue = 384

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 65535),
    )


_WfIpsecBaseMaxManualSpi_Type.__name__ = "Integer32"
_WfIpsecBaseMaxManualSpi_Object = MibScalar
wfIpsecBaseMaxManualSpi = _WfIpsecBaseMaxManualSpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 1, 5),
    _WfIpsecBaseMaxManualSpi_Type()
)
wfIpsecBaseMaxManualSpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecBaseMaxManualSpi.setStatus("mandatory")
_WfIpsecSelectorInTable_Object = MibTable
wfIpsecSelectorInTable = _WfIpsecSelectorInTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 2)
)
if mibBuilder.loadTexts:
    wfIpsecSelectorInTable.setStatus("mandatory")
_WfIpsecSelectorInEntry_Object = MibTableRow
wfIpsecSelectorInEntry = _WfIpsecSelectorInEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 2, 1)
)
wfIpsecSelectorInEntry.setIndexNames(
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecSelectorInInterface"),
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecSelectorInCircuit"),
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecSelectorInPolicyNumber"),
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecSelectorInFragment"),
)
if mibBuilder.loadTexts:
    wfIpsecSelectorInEntry.setStatus("mandatory")


class _WfIpsecSelectorInCreate_Type(Integer32):
    """Custom type wfIpsecSelectorInCreate based on Integer32"""
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


_WfIpsecSelectorInCreate_Type.__name__ = "Integer32"
_WfIpsecSelectorInCreate_Object = MibTableColumn
wfIpsecSelectorInCreate = _WfIpsecSelectorInCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 2, 1, 1),
    _WfIpsecSelectorInCreate_Type()
)
wfIpsecSelectorInCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecSelectorInCreate.setStatus("mandatory")


class _WfIpsecSelectorInEnable_Type(Integer32):
    """Custom type wfIpsecSelectorInEnable based on Integer32"""
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


_WfIpsecSelectorInEnable_Type.__name__ = "Integer32"
_WfIpsecSelectorInEnable_Object = MibTableColumn
wfIpsecSelectorInEnable = _WfIpsecSelectorInEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 2, 1, 2),
    _WfIpsecSelectorInEnable_Type()
)
wfIpsecSelectorInEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecSelectorInEnable.setStatus("mandatory")


class _WfIpsecSelectorInStatus_Type(Integer32):
    """Custom type wfIpsecSelectorInStatus based on Integer32"""
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
          ("inactive", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfIpsecSelectorInStatus_Type.__name__ = "Integer32"
_WfIpsecSelectorInStatus_Object = MibTableColumn
wfIpsecSelectorInStatus = _WfIpsecSelectorInStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 2, 1, 3),
    _WfIpsecSelectorInStatus_Type()
)
wfIpsecSelectorInStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSelectorInStatus.setStatus("mandatory")
_WfIpsecSelectorInCounter_Type = Counter32
_WfIpsecSelectorInCounter_Object = MibTableColumn
wfIpsecSelectorInCounter = _WfIpsecSelectorInCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 2, 1, 4),
    _WfIpsecSelectorInCounter_Type()
)
wfIpsecSelectorInCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSelectorInCounter.setStatus("mandatory")
_WfIpsecSelectorInDefinition_Type = Opaque
_WfIpsecSelectorInDefinition_Object = MibTableColumn
wfIpsecSelectorInDefinition = _WfIpsecSelectorInDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 2, 1, 5),
    _WfIpsecSelectorInDefinition_Type()
)
wfIpsecSelectorInDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecSelectorInDefinition.setStatus("mandatory")
_WfIpsecSelectorInReserved_Type = Integer32
_WfIpsecSelectorInReserved_Object = MibTableColumn
wfIpsecSelectorInReserved = _WfIpsecSelectorInReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 2, 1, 6),
    _WfIpsecSelectorInReserved_Type()
)
wfIpsecSelectorInReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSelectorInReserved.setStatus("mandatory")
_WfIpsecSelectorInInterface_Type = IpAddress
_WfIpsecSelectorInInterface_Object = MibTableColumn
wfIpsecSelectorInInterface = _WfIpsecSelectorInInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 2, 1, 7),
    _WfIpsecSelectorInInterface_Type()
)
wfIpsecSelectorInInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSelectorInInterface.setStatus("mandatory")
_WfIpsecSelectorInCircuit_Type = Integer32
_WfIpsecSelectorInCircuit_Object = MibTableColumn
wfIpsecSelectorInCircuit = _WfIpsecSelectorInCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 2, 1, 8),
    _WfIpsecSelectorInCircuit_Type()
)
wfIpsecSelectorInCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSelectorInCircuit.setStatus("mandatory")
_WfIpsecSelectorInPolicyNumber_Type = Integer32
_WfIpsecSelectorInPolicyNumber_Object = MibTableColumn
wfIpsecSelectorInPolicyNumber = _WfIpsecSelectorInPolicyNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 2, 1, 9),
    _WfIpsecSelectorInPolicyNumber_Type()
)
wfIpsecSelectorInPolicyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSelectorInPolicyNumber.setStatus("mandatory")
_WfIpsecSelectorInFragment_Type = Integer32
_WfIpsecSelectorInFragment_Object = MibTableColumn
wfIpsecSelectorInFragment = _WfIpsecSelectorInFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 2, 1, 10),
    _WfIpsecSelectorInFragment_Type()
)
wfIpsecSelectorInFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSelectorInFragment.setStatus("mandatory")
_WfIpsecSelectorInName_Type = DisplayString
_WfIpsecSelectorInName_Object = MibTableColumn
wfIpsecSelectorInName = _WfIpsecSelectorInName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 2, 1, 11),
    _WfIpsecSelectorInName_Type()
)
wfIpsecSelectorInName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecSelectorInName.setStatus("mandatory")
_WfIpsecSelectorOutTable_Object = MibTable
wfIpsecSelectorOutTable = _WfIpsecSelectorOutTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 3)
)
if mibBuilder.loadTexts:
    wfIpsecSelectorOutTable.setStatus("mandatory")
_WfIpsecSelectorOutEntry_Object = MibTableRow
wfIpsecSelectorOutEntry = _WfIpsecSelectorOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 3, 1)
)
wfIpsecSelectorOutEntry.setIndexNames(
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecSelectorOutInterface"),
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecSelectorOutCircuit"),
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecSelectorOutPolicyNumber"),
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecSelectorOutFragment"),
)
if mibBuilder.loadTexts:
    wfIpsecSelectorOutEntry.setStatus("mandatory")


class _WfIpsecSelectorOutCreate_Type(Integer32):
    """Custom type wfIpsecSelectorOutCreate based on Integer32"""
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


_WfIpsecSelectorOutCreate_Type.__name__ = "Integer32"
_WfIpsecSelectorOutCreate_Object = MibTableColumn
wfIpsecSelectorOutCreate = _WfIpsecSelectorOutCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 3, 1, 1),
    _WfIpsecSelectorOutCreate_Type()
)
wfIpsecSelectorOutCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecSelectorOutCreate.setStatus("mandatory")


class _WfIpsecSelectorOutEnable_Type(Integer32):
    """Custom type wfIpsecSelectorOutEnable based on Integer32"""
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


_WfIpsecSelectorOutEnable_Type.__name__ = "Integer32"
_WfIpsecSelectorOutEnable_Object = MibTableColumn
wfIpsecSelectorOutEnable = _WfIpsecSelectorOutEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 3, 1, 2),
    _WfIpsecSelectorOutEnable_Type()
)
wfIpsecSelectorOutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecSelectorOutEnable.setStatus("mandatory")


class _WfIpsecSelectorOutStatus_Type(Integer32):
    """Custom type wfIpsecSelectorOutStatus based on Integer32"""
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
          ("inactive", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfIpsecSelectorOutStatus_Type.__name__ = "Integer32"
_WfIpsecSelectorOutStatus_Object = MibTableColumn
wfIpsecSelectorOutStatus = _WfIpsecSelectorOutStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 3, 1, 3),
    _WfIpsecSelectorOutStatus_Type()
)
wfIpsecSelectorOutStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSelectorOutStatus.setStatus("mandatory")
_WfIpsecSelectorOutCounter_Type = Counter32
_WfIpsecSelectorOutCounter_Object = MibTableColumn
wfIpsecSelectorOutCounter = _WfIpsecSelectorOutCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 3, 1, 4),
    _WfIpsecSelectorOutCounter_Type()
)
wfIpsecSelectorOutCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSelectorOutCounter.setStatus("mandatory")
_WfIpsecSelectorOutDefinition_Type = Opaque
_WfIpsecSelectorOutDefinition_Object = MibTableColumn
wfIpsecSelectorOutDefinition = _WfIpsecSelectorOutDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 3, 1, 5),
    _WfIpsecSelectorOutDefinition_Type()
)
wfIpsecSelectorOutDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecSelectorOutDefinition.setStatus("mandatory")
_WfIpsecSelectorOutReserved_Type = Integer32
_WfIpsecSelectorOutReserved_Object = MibTableColumn
wfIpsecSelectorOutReserved = _WfIpsecSelectorOutReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 3, 1, 6),
    _WfIpsecSelectorOutReserved_Type()
)
wfIpsecSelectorOutReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSelectorOutReserved.setStatus("mandatory")
_WfIpsecSelectorOutInterface_Type = IpAddress
_WfIpsecSelectorOutInterface_Object = MibTableColumn
wfIpsecSelectorOutInterface = _WfIpsecSelectorOutInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 3, 1, 7),
    _WfIpsecSelectorOutInterface_Type()
)
wfIpsecSelectorOutInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSelectorOutInterface.setStatus("mandatory")
_WfIpsecSelectorOutCircuit_Type = Integer32
_WfIpsecSelectorOutCircuit_Object = MibTableColumn
wfIpsecSelectorOutCircuit = _WfIpsecSelectorOutCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 3, 1, 8),
    _WfIpsecSelectorOutCircuit_Type()
)
wfIpsecSelectorOutCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSelectorOutCircuit.setStatus("mandatory")
_WfIpsecSelectorOutPolicyNumber_Type = Integer32
_WfIpsecSelectorOutPolicyNumber_Object = MibTableColumn
wfIpsecSelectorOutPolicyNumber = _WfIpsecSelectorOutPolicyNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 3, 1, 9),
    _WfIpsecSelectorOutPolicyNumber_Type()
)
wfIpsecSelectorOutPolicyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSelectorOutPolicyNumber.setStatus("mandatory")
_WfIpsecSelectorOutFragment_Type = Integer32
_WfIpsecSelectorOutFragment_Object = MibTableColumn
wfIpsecSelectorOutFragment = _WfIpsecSelectorOutFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 3, 1, 10),
    _WfIpsecSelectorOutFragment_Type()
)
wfIpsecSelectorOutFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSelectorOutFragment.setStatus("mandatory")
_WfIpsecSelectorOutName_Type = DisplayString
_WfIpsecSelectorOutName_Object = MibTableColumn
wfIpsecSelectorOutName = _WfIpsecSelectorOutName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 3, 1, 11),
    _WfIpsecSelectorOutName_Type()
)
wfIpsecSelectorOutName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecSelectorOutName.setStatus("mandatory")
_WfIpsecDescriptorTable_Object = MibTable
wfIpsecDescriptorTable = _WfIpsecDescriptorTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 4)
)
if mibBuilder.loadTexts:
    wfIpsecDescriptorTable.setStatus("mandatory")
_WfIpsecDescriptorEntry_Object = MibTableRow
wfIpsecDescriptorEntry = _WfIpsecDescriptorEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 4, 1)
)
wfIpsecDescriptorEntry.setIndexNames(
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecDescriptorInterface"),
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecDescriptorCircuit"),
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecDescriptorPolicyNumber"),
)
if mibBuilder.loadTexts:
    wfIpsecDescriptorEntry.setStatus("mandatory")


class _WfIpsecDescriptorCreate_Type(Integer32):
    """Custom type wfIpsecDescriptorCreate based on Integer32"""
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


_WfIpsecDescriptorCreate_Type.__name__ = "Integer32"
_WfIpsecDescriptorCreate_Object = MibTableColumn
wfIpsecDescriptorCreate = _WfIpsecDescriptorCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 4, 1, 1),
    _WfIpsecDescriptorCreate_Type()
)
wfIpsecDescriptorCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecDescriptorCreate.setStatus("mandatory")


class _WfIpsecDescriptorStatus_Type(Integer32):
    """Custom type wfIpsecDescriptorStatus based on Integer32"""
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
          ("inactive", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfIpsecDescriptorStatus_Type.__name__ = "Integer32"
_WfIpsecDescriptorStatus_Object = MibTableColumn
wfIpsecDescriptorStatus = _WfIpsecDescriptorStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 4, 1, 2),
    _WfIpsecDescriptorStatus_Type()
)
wfIpsecDescriptorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecDescriptorStatus.setStatus("mandatory")
_WfIpsecDescriptorPolicyNumber_Type = Integer32
_WfIpsecDescriptorPolicyNumber_Object = MibTableColumn
wfIpsecDescriptorPolicyNumber = _WfIpsecDescriptorPolicyNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 4, 1, 3),
    _WfIpsecDescriptorPolicyNumber_Type()
)
wfIpsecDescriptorPolicyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecDescriptorPolicyNumber.setStatus("mandatory")
_WfIpsecDescriptorInterface_Type = IpAddress
_WfIpsecDescriptorInterface_Object = MibTableColumn
wfIpsecDescriptorInterface = _WfIpsecDescriptorInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 4, 1, 4),
    _WfIpsecDescriptorInterface_Type()
)
wfIpsecDescriptorInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecDescriptorInterface.setStatus("mandatory")
_WfIpsecDescriptorCircuit_Type = Integer32
_WfIpsecDescriptorCircuit_Object = MibTableColumn
wfIpsecDescriptorCircuit = _WfIpsecDescriptorCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 4, 1, 5),
    _WfIpsecDescriptorCircuit_Type()
)
wfIpsecDescriptorCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecDescriptorCircuit.setStatus("mandatory")
_WfIpsecDescriptorManualSaList_Type = Opaque
_WfIpsecDescriptorManualSaList_Object = MibTableColumn
wfIpsecDescriptorManualSaList = _WfIpsecDescriptorManualSaList_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 4, 1, 6),
    _WfIpsecDescriptorManualSaList_Type()
)
wfIpsecDescriptorManualSaList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecDescriptorManualSaList.setStatus("mandatory")


class _WfIpsecDescriptorSaMode_Type(Integer32):
    """Custom type wfIpsecDescriptorSaMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transport", 2),
          ("tunnel", 1))
    )


_WfIpsecDescriptorSaMode_Type.__name__ = "Integer32"
_WfIpsecDescriptorSaMode_Object = MibTableColumn
wfIpsecDescriptorSaMode = _WfIpsecDescriptorSaMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 4, 1, 7),
    _WfIpsecDescriptorSaMode_Type()
)
wfIpsecDescriptorSaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecDescriptorSaMode.setStatus("mandatory")


class _WfIpsecDescriptorPfs_Type(Integer32):
    """Custom type wfIpsecDescriptorPfs based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_WfIpsecDescriptorPfs_Type.__name__ = "Integer32"
_WfIpsecDescriptorPfs_Object = MibTableColumn
wfIpsecDescriptorPfs = _WfIpsecDescriptorPfs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 4, 1, 8),
    _WfIpsecDescriptorPfs_Type()
)
wfIpsecDescriptorPfs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecDescriptorPfs.setStatus("mandatory")
_WfIpsecDescriptorProposals_Type = Opaque
_WfIpsecDescriptorProposals_Object = MibTableColumn
wfIpsecDescriptorProposals = _WfIpsecDescriptorProposals_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 4, 1, 9),
    _WfIpsecDescriptorProposals_Type()
)
wfIpsecDescriptorProposals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecDescriptorProposals.setStatus("mandatory")


class _WfIpsecDescriptorSourceForDestAddr_Type(Integer32):
    """Custom type wfIpsecDescriptorSourceForDestAddr based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packet", 1),
          ("policy", 2))
    )


_WfIpsecDescriptorSourceForDestAddr_Type.__name__ = "Integer32"
_WfIpsecDescriptorSourceForDestAddr_Object = MibTableColumn
wfIpsecDescriptorSourceForDestAddr = _WfIpsecDescriptorSourceForDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 4, 1, 10),
    _WfIpsecDescriptorSourceForDestAddr_Type()
)
wfIpsecDescriptorSourceForDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecDescriptorSourceForDestAddr.setStatus("mandatory")


class _WfIpsecDescriptorSourceForSrcAddr_Type(Integer32):
    """Custom type wfIpsecDescriptorSourceForSrcAddr based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packet", 1),
          ("policy", 2))
    )


_WfIpsecDescriptorSourceForSrcAddr_Type.__name__ = "Integer32"
_WfIpsecDescriptorSourceForSrcAddr_Object = MibTableColumn
wfIpsecDescriptorSourceForSrcAddr = _WfIpsecDescriptorSourceForSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 4, 1, 11),
    _WfIpsecDescriptorSourceForSrcAddr_Type()
)
wfIpsecDescriptorSourceForSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecDescriptorSourceForSrcAddr.setStatus("mandatory")


class _WfIpsecDescriptorSourceForProtocol_Type(Integer32):
    """Custom type wfIpsecDescriptorSourceForProtocol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packet", 1),
          ("policy", 2))
    )


_WfIpsecDescriptorSourceForProtocol_Type.__name__ = "Integer32"
_WfIpsecDescriptorSourceForProtocol_Object = MibTableColumn
wfIpsecDescriptorSourceForProtocol = _WfIpsecDescriptorSourceForProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 4, 1, 12),
    _WfIpsecDescriptorSourceForProtocol_Type()
)
wfIpsecDescriptorSourceForProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecDescriptorSourceForProtocol.setStatus("mandatory")
_WfIpsecDescriptorStartSourceAddr_Type = IpAddress
_WfIpsecDescriptorStartSourceAddr_Object = MibTableColumn
wfIpsecDescriptorStartSourceAddr = _WfIpsecDescriptorStartSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 4, 1, 13),
    _WfIpsecDescriptorStartSourceAddr_Type()
)
wfIpsecDescriptorStartSourceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecDescriptorStartSourceAddr.setStatus("mandatory")
_WfIpsecDescriptorEndSourceAddr_Type = IpAddress
_WfIpsecDescriptorEndSourceAddr_Object = MibTableColumn
wfIpsecDescriptorEndSourceAddr = _WfIpsecDescriptorEndSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 4, 1, 14),
    _WfIpsecDescriptorEndSourceAddr_Type()
)
wfIpsecDescriptorEndSourceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecDescriptorEndSourceAddr.setStatus("mandatory")
_WfIpsecDescriptorStartDestAddr_Type = IpAddress
_WfIpsecDescriptorStartDestAddr_Object = MibTableColumn
wfIpsecDescriptorStartDestAddr = _WfIpsecDescriptorStartDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 4, 1, 15),
    _WfIpsecDescriptorStartDestAddr_Type()
)
wfIpsecDescriptorStartDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecDescriptorStartDestAddr.setStatus("mandatory")
_WfIpsecDescriptorEndDestAddr_Type = IpAddress
_WfIpsecDescriptorEndDestAddr_Object = MibTableColumn
wfIpsecDescriptorEndDestAddr = _WfIpsecDescriptorEndDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 4, 1, 16),
    _WfIpsecDescriptorEndDestAddr_Type()
)
wfIpsecDescriptorEndDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecDescriptorEndDestAddr.setStatus("mandatory")
_WfIpsecDescriptorSourcePort_Type = Integer32
_WfIpsecDescriptorSourcePort_Object = MibTableColumn
wfIpsecDescriptorSourcePort = _WfIpsecDescriptorSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 4, 1, 17),
    _WfIpsecDescriptorSourcePort_Type()
)
wfIpsecDescriptorSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecDescriptorSourcePort.setStatus("mandatory")
_WfIpsecDescriptorProtocol_Type = Integer32
_WfIpsecDescriptorProtocol_Object = MibTableColumn
wfIpsecDescriptorProtocol = _WfIpsecDescriptorProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 4, 1, 18),
    _WfIpsecDescriptorProtocol_Type()
)
wfIpsecDescriptorProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecDescriptorProtocol.setStatus("mandatory")
_WfIpsecDescriptorPrimarySG_Type = IpAddress
_WfIpsecDescriptorPrimarySG_Object = MibTableColumn
wfIpsecDescriptorPrimarySG = _WfIpsecDescriptorPrimarySG_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 4, 1, 19),
    _WfIpsecDescriptorPrimarySG_Type()
)
wfIpsecDescriptorPrimarySG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecDescriptorPrimarySG.setStatus("mandatory")


class _WfIpsecDescriptorInboundIdleTimer_Type(Integer32):
    """Custom type wfIpsecDescriptorInboundIdleTimer based on Integer32"""
    defaultValue = 15


_WfIpsecDescriptorInboundIdleTimer_Object = MibTableColumn
wfIpsecDescriptorInboundIdleTimer = _WfIpsecDescriptorInboundIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 4, 1, 20),
    _WfIpsecDescriptorInboundIdleTimer_Type()
)
wfIpsecDescriptorInboundIdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecDescriptorInboundIdleTimer.setStatus("mandatory")


class _WfIpsecDescriptorAntiReplayWindow_Type(Integer32):
    """Custom type wfIpsecDescriptorAntiReplayWindow based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("pkts128", 128),
          ("pkts32", 32),
          ("pkts64", 64))
    )


_WfIpsecDescriptorAntiReplayWindow_Type.__name__ = "Integer32"
_WfIpsecDescriptorAntiReplayWindow_Object = MibTableColumn
wfIpsecDescriptorAntiReplayWindow = _WfIpsecDescriptorAntiReplayWindow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 4, 1, 21),
    _WfIpsecDescriptorAntiReplayWindow_Type()
)
wfIpsecDescriptorAntiReplayWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecDescriptorAntiReplayWindow.setStatus("mandatory")
_WfIpsecDescriptorDestPort_Type = Integer32
_WfIpsecDescriptorDestPort_Object = MibTableColumn
wfIpsecDescriptorDestPort = _WfIpsecDescriptorDestPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 4, 1, 22),
    _WfIpsecDescriptorDestPort_Type()
)
wfIpsecDescriptorDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecDescriptorDestPort.setStatus("mandatory")
_WfIpsecEspSaTable_Object = MibTable
wfIpsecEspSaTable = _WfIpsecEspSaTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 5)
)
if mibBuilder.loadTexts:
    wfIpsecEspSaTable.setStatus("mandatory")
_WfIpsecEspSaEntry_Object = MibTableRow
wfIpsecEspSaEntry = _WfIpsecEspSaEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 5, 1)
)
wfIpsecEspSaEntry.setIndexNames(
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecEspSaSrc"),
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecEspSaDest"),
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecEspSaSpi"),
)
if mibBuilder.loadTexts:
    wfIpsecEspSaEntry.setStatus("mandatory")


class _WfIpsecEspSaCreate_Type(Integer32):
    """Custom type wfIpsecEspSaCreate based on Integer32"""
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


_WfIpsecEspSaCreate_Type.__name__ = "Integer32"
_WfIpsecEspSaCreate_Object = MibTableColumn
wfIpsecEspSaCreate = _WfIpsecEspSaCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 5, 1, 1),
    _WfIpsecEspSaCreate_Type()
)
wfIpsecEspSaCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecEspSaCreate.setStatus("mandatory")


class _WfIpsecEspSaStatus_Type(Integer32):
    """Custom type wfIpsecEspSaStatus based on Integer32"""
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
          ("inactive", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfIpsecEspSaStatus_Type.__name__ = "Integer32"
_WfIpsecEspSaStatus_Object = MibTableColumn
wfIpsecEspSaStatus = _WfIpsecEspSaStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 5, 1, 2),
    _WfIpsecEspSaStatus_Type()
)
wfIpsecEspSaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecEspSaStatus.setStatus("mandatory")
_WfIpsecEspSaSrc_Type = IpAddress
_WfIpsecEspSaSrc_Object = MibTableColumn
wfIpsecEspSaSrc = _WfIpsecEspSaSrc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 5, 1, 3),
    _WfIpsecEspSaSrc_Type()
)
wfIpsecEspSaSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecEspSaSrc.setStatus("mandatory")
_WfIpsecEspSaDest_Type = IpAddress
_WfIpsecEspSaDest_Object = MibTableColumn
wfIpsecEspSaDest = _WfIpsecEspSaDest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 5, 1, 4),
    _WfIpsecEspSaDest_Type()
)
wfIpsecEspSaDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecEspSaDest.setStatus("mandatory")
_WfIpsecEspSaSpi_Type = Integer32
_WfIpsecEspSaSpi_Object = MibTableColumn
wfIpsecEspSaSpi = _WfIpsecEspSaSpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 5, 1, 5),
    _WfIpsecEspSaSpi_Type()
)
wfIpsecEspSaSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecEspSaSpi.setStatus("mandatory")


class _WfIpsecEspSaCipherAlg_Type(Integer32):
    """Custom type wfIpsecEspSaCipherAlg based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("des", 2),
          ("desede", 3),
          ("none", 1))
    )


_WfIpsecEspSaCipherAlg_Type.__name__ = "Integer32"
_WfIpsecEspSaCipherAlg_Object = MibTableColumn
wfIpsecEspSaCipherAlg = _WfIpsecEspSaCipherAlg_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 5, 1, 6),
    _WfIpsecEspSaCipherAlg_Type()
)
wfIpsecEspSaCipherAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecEspSaCipherAlg.setStatus("mandatory")
_WfIpsecEspSaManualCipherKey_Type = OctetString
_WfIpsecEspSaManualCipherKey_Object = MibTableColumn
wfIpsecEspSaManualCipherKey = _WfIpsecEspSaManualCipherKey_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 5, 1, 7),
    _WfIpsecEspSaManualCipherKey_Type()
)
wfIpsecEspSaManualCipherKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecEspSaManualCipherKey.setStatus("mandatory")


class _WfIpsecEspSaDesKeyStrength_Type(Integer32):
    """Custom type wfIpsecEspSaDesKeyStrength based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fiftysixbit", 2),
          ("fortybit", 1))
    )


_WfIpsecEspSaDesKeyStrength_Type.__name__ = "Integer32"
_WfIpsecEspSaDesKeyStrength_Object = MibTableColumn
wfIpsecEspSaDesKeyStrength = _WfIpsecEspSaDesKeyStrength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 5, 1, 8),
    _WfIpsecEspSaDesKeyStrength_Type()
)
wfIpsecEspSaDesKeyStrength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecEspSaDesKeyStrength.setStatus("mandatory")


class _WfIpsecEspSaIntegrityAlg_Type(Integer32):
    """Custom type wfIpsecEspSaIntegrityAlg based on Integer32"""
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
        *(("hmacMd5", 2),
          ("hmacSha1", 3),
          ("none", 1))
    )


_WfIpsecEspSaIntegrityAlg_Type.__name__ = "Integer32"
_WfIpsecEspSaIntegrityAlg_Object = MibTableColumn
wfIpsecEspSaIntegrityAlg = _WfIpsecEspSaIntegrityAlg_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 5, 1, 9),
    _WfIpsecEspSaIntegrityAlg_Type()
)
wfIpsecEspSaIntegrityAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecEspSaIntegrityAlg.setStatus("mandatory")
_WfIpsecEspSaManualIntegrityKey_Type = OctetString
_WfIpsecEspSaManualIntegrityKey_Object = MibTableColumn
wfIpsecEspSaManualIntegrityKey = _WfIpsecEspSaManualIntegrityKey_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 5, 1, 10),
    _WfIpsecEspSaManualIntegrityKey_Type()
)
wfIpsecEspSaManualIntegrityKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecEspSaManualIntegrityKey.setStatus("mandatory")


class _WfIpsecEspSaVerifyPad_Type(Integer32):
    """Custom type wfIpsecEspSaVerifyPad based on Integer32"""
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


_WfIpsecEspSaVerifyPad_Type.__name__ = "Integer32"
_WfIpsecEspSaVerifyPad_Object = MibTableColumn
wfIpsecEspSaVerifyPad = _WfIpsecEspSaVerifyPad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 5, 1, 11),
    _WfIpsecEspSaVerifyPad_Type()
)
wfIpsecEspSaVerifyPad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecEspSaVerifyPad.setStatus("mandatory")
_WfIpsecEspSaReset_Type = Integer32
_WfIpsecEspSaReset_Object = MibTableColumn
wfIpsecEspSaReset = _WfIpsecEspSaReset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 5, 1, 12),
    _WfIpsecEspSaReset_Type()
)
wfIpsecEspSaReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecEspSaReset.setStatus("mandatory")
_WfIpsecEspSaBadAuthen_Type = Counter32
_WfIpsecEspSaBadAuthen_Object = MibTableColumn
wfIpsecEspSaBadAuthen = _WfIpsecEspSaBadAuthen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 5, 1, 13),
    _WfIpsecEspSaBadAuthen_Type()
)
wfIpsecEspSaBadAuthen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecEspSaBadAuthen.setStatus("mandatory")
_WfIpsecEspSaBadDecrypt_Type = Counter32
_WfIpsecEspSaBadDecrypt_Object = MibTableColumn
wfIpsecEspSaBadDecrypt = _WfIpsecEspSaBadDecrypt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 5, 1, 14),
    _WfIpsecEspSaBadDecrypt_Type()
)
wfIpsecEspSaBadDecrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecEspSaBadDecrypt.setStatus("mandatory")
_WfIpsecEspSaBadPad_Type = Counter32
_WfIpsecEspSaBadPad_Object = MibTableColumn
wfIpsecEspSaBadPad = _WfIpsecEspSaBadPad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 5, 1, 15),
    _WfIpsecEspSaBadPad_Type()
)
wfIpsecEspSaBadPad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecEspSaBadPad.setStatus("mandatory")
_WfIpsecEspSaProtectPkt_Type = Counter32
_WfIpsecEspSaProtectPkt_Object = MibTableColumn
wfIpsecEspSaProtectPkt = _WfIpsecEspSaProtectPkt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 5, 1, 16),
    _WfIpsecEspSaProtectPkt_Type()
)
wfIpsecEspSaProtectPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecEspSaProtectPkt.setStatus("mandatory")
_WfIpsecEspSaUnprotectPkt_Type = Counter32
_WfIpsecEspSaUnprotectPkt_Object = MibTableColumn
wfIpsecEspSaUnprotectPkt = _WfIpsecEspSaUnprotectPkt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 5, 1, 17),
    _WfIpsecEspSaUnprotectPkt_Type()
)
wfIpsecEspSaUnprotectPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecEspSaUnprotectPkt.setStatus("mandatory")
_WfIpsecEspSaEncryptByte_Type = Counter32
_WfIpsecEspSaEncryptByte_Object = MibTableColumn
wfIpsecEspSaEncryptByte = _WfIpsecEspSaEncryptByte_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 5, 1, 18),
    _WfIpsecEspSaEncryptByte_Type()
)
wfIpsecEspSaEncryptByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecEspSaEncryptByte.setStatus("mandatory")
_WfIpsecEspSaDecryptByte_Type = Counter32
_WfIpsecEspSaDecryptByte_Object = MibTableColumn
wfIpsecEspSaDecryptByte = _WfIpsecEspSaDecryptByte_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 5, 1, 19),
    _WfIpsecEspSaDecryptByte_Type()
)
wfIpsecEspSaDecryptByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecEspSaDecryptByte.setStatus("mandatory")


class _WfIpsecEspSaMode_Type(Integer32):
    """Custom type wfIpsecEspSaMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transport", 2),
          ("tunnel", 1))
    )


_WfIpsecEspSaMode_Type.__name__ = "Integer32"
_WfIpsecEspSaMode_Object = MibTableColumn
wfIpsecEspSaMode = _WfIpsecEspSaMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 5, 1, 20),
    _WfIpsecEspSaMode_Type()
)
wfIpsecEspSaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecEspSaMode.setStatus("mandatory")


class _WfIpsecEspSaPfs_Type(Integer32):
    """Custom type wfIpsecEspSaPfs based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_WfIpsecEspSaPfs_Type.__name__ = "Integer32"
_WfIpsecEspSaPfs_Object = MibTableColumn
wfIpsecEspSaPfs = _WfIpsecEspSaPfs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 5, 1, 21),
    _WfIpsecEspSaPfs_Type()
)
wfIpsecEspSaPfs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecEspSaPfs.setStatus("mandatory")


class _WfIpsecEspSaExpiryType_Type(Integer32):
    """Custom type wfIpsecEspSaExpiryType based on Integer32"""
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
        *(("kilobytes", 2),
          ("none", 3),
          ("seconds", 1))
    )


_WfIpsecEspSaExpiryType_Type.__name__ = "Integer32"
_WfIpsecEspSaExpiryType_Object = MibTableColumn
wfIpsecEspSaExpiryType = _WfIpsecEspSaExpiryType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 5, 1, 22),
    _WfIpsecEspSaExpiryType_Type()
)
wfIpsecEspSaExpiryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecEspSaExpiryType.setStatus("mandatory")
_WfIpsecEspSaExpiryValue_Type = Integer32
_WfIpsecEspSaExpiryValue_Object = MibTableColumn
wfIpsecEspSaExpiryValue = _WfIpsecEspSaExpiryValue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 5, 1, 23),
    _WfIpsecEspSaExpiryValue_Type()
)
wfIpsecEspSaExpiryValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecEspSaExpiryValue.setStatus("mandatory")
_WfIpsecStatsTable_Object = MibTable
wfIpsecStatsTable = _WfIpsecStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 6)
)
if mibBuilder.loadTexts:
    wfIpsecStatsTable.setStatus("mandatory")
_WfIpsecStatsEntry_Object = MibTableRow
wfIpsecStatsEntry = _WfIpsecStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 6, 1)
)
wfIpsecStatsEntry.setIndexNames(
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecStatsInterface"),
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecStatsCircuit"),
)
if mibBuilder.loadTexts:
    wfIpsecStatsEntry.setStatus("mandatory")


class _WfIpsecStatsCreate_Type(Integer32):
    """Custom type wfIpsecStatsCreate based on Integer32"""
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


_WfIpsecStatsCreate_Type.__name__ = "Integer32"
_WfIpsecStatsCreate_Object = MibTableColumn
wfIpsecStatsCreate = _WfIpsecStatsCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 6, 1, 1),
    _WfIpsecStatsCreate_Type()
)
wfIpsecStatsCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecStatsCreate.setStatus("mandatory")
_WfIpsecStatsInterface_Type = IpAddress
_WfIpsecStatsInterface_Object = MibTableColumn
wfIpsecStatsInterface = _WfIpsecStatsInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 6, 1, 2),
    _WfIpsecStatsInterface_Type()
)
wfIpsecStatsInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecStatsInterface.setStatus("mandatory")
_WfIpsecStatsCircuit_Type = Integer32
_WfIpsecStatsCircuit_Object = MibTableColumn
wfIpsecStatsCircuit = _WfIpsecStatsCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 6, 1, 3),
    _WfIpsecStatsCircuit_Type()
)
wfIpsecStatsCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecStatsCircuit.setStatus("mandatory")
_WfIpsecStatsReset_Type = Integer32
_WfIpsecStatsReset_Object = MibTableColumn
wfIpsecStatsReset = _WfIpsecStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 6, 1, 4),
    _WfIpsecStatsReset_Type()
)
wfIpsecStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecStatsReset.setStatus("mandatory")
_WfIpsecStatsUnprotectPkt_Type = Counter32
_WfIpsecStatsUnprotectPkt_Object = MibTableColumn
wfIpsecStatsUnprotectPkt = _WfIpsecStatsUnprotectPkt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 6, 1, 5),
    _WfIpsecStatsUnprotectPkt_Type()
)
wfIpsecStatsUnprotectPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecStatsUnprotectPkt.setStatus("mandatory")
_WfIpsecStatsProtectPkt_Type = Counter32
_WfIpsecStatsProtectPkt_Object = MibTableColumn
wfIpsecStatsProtectPkt = _WfIpsecStatsProtectPkt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 6, 1, 6),
    _WfIpsecStatsProtectPkt_Type()
)
wfIpsecStatsProtectPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecStatsProtectPkt.setStatus("mandatory")
_WfIpsecStatsBypassPkt_Type = Counter32
_WfIpsecStatsBypassPkt_Object = MibTableColumn
wfIpsecStatsBypassPkt = _WfIpsecStatsBypassPkt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 6, 1, 7),
    _WfIpsecStatsBypassPkt_Type()
)
wfIpsecStatsBypassPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecStatsBypassPkt.setStatus("mandatory")
_WfIpsecStatsDropPkt_Type = Counter32
_WfIpsecStatsDropPkt_Object = MibTableColumn
wfIpsecStatsDropPkt = _WfIpsecStatsDropPkt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 6, 1, 8),
    _WfIpsecStatsDropPkt_Type()
)
wfIpsecStatsDropPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecStatsDropPkt.setStatus("mandatory")
_WfIpsecStatsNoSa_Type = Counter32
_WfIpsecStatsNoSa_Object = MibTableColumn
wfIpsecStatsNoSa = _WfIpsecStatsNoSa_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 6, 1, 9),
    _WfIpsecStatsNoSa_Type()
)
wfIpsecStatsNoSa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecStatsNoSa.setStatus("mandatory")
_WfIpsecStatsLastBadSpi_Type = Integer32
_WfIpsecStatsLastBadSpi_Object = MibTableColumn
wfIpsecStatsLastBadSpi = _WfIpsecStatsLastBadSpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 6, 1, 10),
    _WfIpsecStatsLastBadSpi_Type()
)
wfIpsecStatsLastBadSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecStatsLastBadSpi.setStatus("mandatory")
_WfIpsecStatsNoPolicyMatch_Type = Counter32
_WfIpsecStatsNoPolicyMatch_Object = MibTableColumn
wfIpsecStatsNoPolicyMatch = _WfIpsecStatsNoPolicyMatch_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 6, 1, 11),
    _WfIpsecStatsNoPolicyMatch_Type()
)
wfIpsecStatsNoPolicyMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecStatsNoPolicyMatch.setStatus("mandatory")
_WfIpsecStatsSaExpDropBytes_Type = Counter32
_WfIpsecStatsSaExpDropBytes_Object = MibTableColumn
wfIpsecStatsSaExpDropBytes = _WfIpsecStatsSaExpDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 6, 1, 12),
    _WfIpsecStatsSaExpDropBytes_Type()
)
wfIpsecStatsSaExpDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecStatsSaExpDropBytes.setStatus("mandatory")
_WfIpsecStatsOutClips_Type = Counter32
_WfIpsecStatsOutClips_Object = MibTableColumn
wfIpsecStatsOutClips = _WfIpsecStatsOutClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 6, 1, 13),
    _WfIpsecStatsOutClips_Type()
)
wfIpsecStatsOutClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecStatsOutClips.setStatus("mandatory")
_WfIpsecStatsInClips_Type = Counter32
_WfIpsecStatsInClips_Object = MibTableColumn
wfIpsecStatsInClips = _WfIpsecStatsInClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 6, 1, 14),
    _WfIpsecStatsInClips_Type()
)
wfIpsecStatsInClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecStatsInClips.setStatus("mandatory")
_WfIpsecRemoteGatewayTable_Object = MibTable
wfIpsecRemoteGatewayTable = _WfIpsecRemoteGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 7)
)
if mibBuilder.loadTexts:
    wfIpsecRemoteGatewayTable.setStatus("mandatory")
_WfIpsecRemoteGatewayEntry_Object = MibTableRow
wfIpsecRemoteGatewayEntry = _WfIpsecRemoteGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 7, 1)
)
wfIpsecRemoteGatewayEntry.setIndexNames(
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecRemoteGatewayInterface"),
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecRemoteGatewayCircuit"),
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecRemoteGatewayIndex"),
)
if mibBuilder.loadTexts:
    wfIpsecRemoteGatewayEntry.setStatus("mandatory")


class _WfIpsecRemoteGatewayCreate_Type(Integer32):
    """Custom type wfIpsecRemoteGatewayCreate based on Integer32"""
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


_WfIpsecRemoteGatewayCreate_Type.__name__ = "Integer32"
_WfIpsecRemoteGatewayCreate_Object = MibTableColumn
wfIpsecRemoteGatewayCreate = _WfIpsecRemoteGatewayCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 7, 1, 1),
    _WfIpsecRemoteGatewayCreate_Type()
)
wfIpsecRemoteGatewayCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecRemoteGatewayCreate.setStatus("mandatory")


class _WfIpsecRemoteGatewayEnable_Type(Integer32):
    """Custom type wfIpsecRemoteGatewayEnable based on Integer32"""
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


_WfIpsecRemoteGatewayEnable_Type.__name__ = "Integer32"
_WfIpsecRemoteGatewayEnable_Object = MibTableColumn
wfIpsecRemoteGatewayEnable = _WfIpsecRemoteGatewayEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 7, 1, 2),
    _WfIpsecRemoteGatewayEnable_Type()
)
wfIpsecRemoteGatewayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecRemoteGatewayEnable.setStatus("mandatory")


class _WfIpsecRemoteGatewayStatus_Type(Integer32):
    """Custom type wfIpsecRemoteGatewayStatus based on Integer32"""
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
        *(("active", 1),
          ("error", 2),
          ("inactive", 3),
          ("notpresent", 4))
    )


_WfIpsecRemoteGatewayStatus_Type.__name__ = "Integer32"
_WfIpsecRemoteGatewayStatus_Object = MibTableColumn
wfIpsecRemoteGatewayStatus = _WfIpsecRemoteGatewayStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 7, 1, 3),
    _WfIpsecRemoteGatewayStatus_Type()
)
wfIpsecRemoteGatewayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecRemoteGatewayStatus.setStatus("mandatory")
_WfIpsecRemoteGatewayInterface_Type = IpAddress
_WfIpsecRemoteGatewayInterface_Object = MibTableColumn
wfIpsecRemoteGatewayInterface = _WfIpsecRemoteGatewayInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 7, 1, 4),
    _WfIpsecRemoteGatewayInterface_Type()
)
wfIpsecRemoteGatewayInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecRemoteGatewayInterface.setStatus("mandatory")
_WfIpsecRemoteGatewayCircuit_Type = Integer32
_WfIpsecRemoteGatewayCircuit_Object = MibTableColumn
wfIpsecRemoteGatewayCircuit = _WfIpsecRemoteGatewayCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 7, 1, 5),
    _WfIpsecRemoteGatewayCircuit_Type()
)
wfIpsecRemoteGatewayCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecRemoteGatewayCircuit.setStatus("mandatory")
_WfIpsecRemoteGatewayIndex_Type = Integer32
_WfIpsecRemoteGatewayIndex_Object = MibTableColumn
wfIpsecRemoteGatewayIndex = _WfIpsecRemoteGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 7, 1, 6),
    _WfIpsecRemoteGatewayIndex_Type()
)
wfIpsecRemoteGatewayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecRemoteGatewayIndex.setStatus("mandatory")
_WfIpsecRemoteGatewayIpAddr_Type = IpAddress
_WfIpsecRemoteGatewayIpAddr_Object = MibTableColumn
wfIpsecRemoteGatewayIpAddr = _WfIpsecRemoteGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 7, 1, 7),
    _WfIpsecRemoteGatewayIpAddr_Type()
)
wfIpsecRemoteGatewayIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecRemoteGatewayIpAddr.setStatus("mandatory")
_WfIpsecRemoteGatewayRange_Type = OctetString
_WfIpsecRemoteGatewayRange_Object = MibTableColumn
wfIpsecRemoteGatewayRange = _WfIpsecRemoteGatewayRange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 7, 1, 8),
    _WfIpsecRemoteGatewayRange_Type()
)
wfIpsecRemoteGatewayRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecRemoteGatewayRange.setStatus("mandatory")
_WfIpsecRemoteGatewayName_Type = DisplayString
_WfIpsecRemoteGatewayName_Object = MibTableColumn
wfIpsecRemoteGatewayName = _WfIpsecRemoteGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 7, 1, 9),
    _WfIpsecRemoteGatewayName_Type()
)
wfIpsecRemoteGatewayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecRemoteGatewayName.setStatus("mandatory")
_WfIpsecProposalTable_Object = MibTable
wfIpsecProposalTable = _WfIpsecProposalTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 8)
)
if mibBuilder.loadTexts:
    wfIpsecProposalTable.setStatus("mandatory")
_WfIpsecProposalEntry_Object = MibTableRow
wfIpsecProposalEntry = _WfIpsecProposalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 8, 1)
)
wfIpsecProposalEntry.setIndexNames(
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecProposalNumber"),
)
if mibBuilder.loadTexts:
    wfIpsecProposalEntry.setStatus("mandatory")


class _WfIpsecProposalCreate_Type(Integer32):
    """Custom type wfIpsecProposalCreate based on Integer32"""
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


_WfIpsecProposalCreate_Type.__name__ = "Integer32"
_WfIpsecProposalCreate_Object = MibTableColumn
wfIpsecProposalCreate = _WfIpsecProposalCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 8, 1, 1),
    _WfIpsecProposalCreate_Type()
)
wfIpsecProposalCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecProposalCreate.setStatus("mandatory")


class _WfIpsecProposalStatus_Type(Integer32):
    """Custom type wfIpsecProposalStatus based on Integer32"""
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
        *(("active", 1),
          ("error", 2),
          ("inactive", 3),
          ("notpresent", 4))
    )


_WfIpsecProposalStatus_Type.__name__ = "Integer32"
_WfIpsecProposalStatus_Object = MibTableColumn
wfIpsecProposalStatus = _WfIpsecProposalStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 8, 1, 2),
    _WfIpsecProposalStatus_Type()
)
wfIpsecProposalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecProposalStatus.setStatus("mandatory")
_WfIpsecProposalName_Type = DisplayString
_WfIpsecProposalName_Object = MibTableColumn
wfIpsecProposalName = _WfIpsecProposalName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 8, 1, 3),
    _WfIpsecProposalName_Type()
)
wfIpsecProposalName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecProposalName.setStatus("mandatory")
_WfIpsecProposalNumber_Type = Integer32
_WfIpsecProposalNumber_Object = MibTableColumn
wfIpsecProposalNumber = _WfIpsecProposalNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 8, 1, 4),
    _WfIpsecProposalNumber_Type()
)
wfIpsecProposalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecProposalNumber.setStatus("mandatory")
_WfIpsecProposalSuites_Type = Opaque
_WfIpsecProposalSuites_Object = MibTableColumn
wfIpsecProposalSuites = _WfIpsecProposalSuites_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 8, 1, 5),
    _WfIpsecProposalSuites_Type()
)
wfIpsecProposalSuites.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecProposalSuites.setStatus("mandatory")
_WfIpsecSuiteTable_Object = MibTable
wfIpsecSuiteTable = _WfIpsecSuiteTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 9)
)
if mibBuilder.loadTexts:
    wfIpsecSuiteTable.setStatus("mandatory")
_WfIpsecSuiteEntry_Object = MibTableRow
wfIpsecSuiteEntry = _WfIpsecSuiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 9, 1)
)
wfIpsecSuiteEntry.setIndexNames(
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecSuiteNumber"),
)
if mibBuilder.loadTexts:
    wfIpsecSuiteEntry.setStatus("mandatory")


class _WfIpsecSuiteCreate_Type(Integer32):
    """Custom type wfIpsecSuiteCreate based on Integer32"""
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


_WfIpsecSuiteCreate_Type.__name__ = "Integer32"
_WfIpsecSuiteCreate_Object = MibTableColumn
wfIpsecSuiteCreate = _WfIpsecSuiteCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 9, 1, 1),
    _WfIpsecSuiteCreate_Type()
)
wfIpsecSuiteCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecSuiteCreate.setStatus("mandatory")


class _WfIpsecSuiteStatus_Type(Integer32):
    """Custom type wfIpsecSuiteStatus based on Integer32"""
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
        *(("active", 1),
          ("error", 2),
          ("inactive", 3),
          ("notpresent", 4))
    )


_WfIpsecSuiteStatus_Type.__name__ = "Integer32"
_WfIpsecSuiteStatus_Object = MibTableColumn
wfIpsecSuiteStatus = _WfIpsecSuiteStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 9, 1, 2),
    _WfIpsecSuiteStatus_Type()
)
wfIpsecSuiteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSuiteStatus.setStatus("mandatory")
_WfIpsecSuiteName_Type = DisplayString
_WfIpsecSuiteName_Object = MibTableColumn
wfIpsecSuiteName = _WfIpsecSuiteName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 9, 1, 3),
    _WfIpsecSuiteName_Type()
)
wfIpsecSuiteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecSuiteName.setStatus("mandatory")
_WfIpsecSuiteNumber_Type = Integer32
_WfIpsecSuiteNumber_Object = MibTableColumn
wfIpsecSuiteNumber = _WfIpsecSuiteNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 9, 1, 4),
    _WfIpsecSuiteNumber_Type()
)
wfIpsecSuiteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSuiteNumber.setStatus("mandatory")
_WfIpsecSuiteEspProtocol_Type = Opaque
_WfIpsecSuiteEspProtocol_Object = MibTableColumn
wfIpsecSuiteEspProtocol = _WfIpsecSuiteEspProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 9, 1, 5),
    _WfIpsecSuiteEspProtocol_Type()
)
wfIpsecSuiteEspProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecSuiteEspProtocol.setStatus("mandatory")
_WfIpsecSuiteAhProtocol_Type = Opaque
_WfIpsecSuiteAhProtocol_Object = MibTableColumn
wfIpsecSuiteAhProtocol = _WfIpsecSuiteAhProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 9, 1, 6),
    _WfIpsecSuiteAhProtocol_Type()
)
wfIpsecSuiteAhProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecSuiteAhProtocol.setStatus("mandatory")
_WfIpsecEspTransformTable_Object = MibTable
wfIpsecEspTransformTable = _WfIpsecEspTransformTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 10)
)
if mibBuilder.loadTexts:
    wfIpsecEspTransformTable.setStatus("mandatory")
_WfIpsecEspTransformEntry_Object = MibTableRow
wfIpsecEspTransformEntry = _WfIpsecEspTransformEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 10, 1)
)
wfIpsecEspTransformEntry.setIndexNames(
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecEspTransformNumber"),
)
if mibBuilder.loadTexts:
    wfIpsecEspTransformEntry.setStatus("mandatory")


class _WfIpsecEspTransformCreate_Type(Integer32):
    """Custom type wfIpsecEspTransformCreate based on Integer32"""
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


_WfIpsecEspTransformCreate_Type.__name__ = "Integer32"
_WfIpsecEspTransformCreate_Object = MibTableColumn
wfIpsecEspTransformCreate = _WfIpsecEspTransformCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 10, 1, 1),
    _WfIpsecEspTransformCreate_Type()
)
wfIpsecEspTransformCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecEspTransformCreate.setStatus("mandatory")


class _WfIpsecEspTransformStatus_Type(Integer32):
    """Custom type wfIpsecEspTransformStatus based on Integer32"""
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
        *(("active", 1),
          ("error", 2),
          ("inactive", 3),
          ("notpresent", 4))
    )


_WfIpsecEspTransformStatus_Type.__name__ = "Integer32"
_WfIpsecEspTransformStatus_Object = MibTableColumn
wfIpsecEspTransformStatus = _WfIpsecEspTransformStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 10, 1, 2),
    _WfIpsecEspTransformStatus_Type()
)
wfIpsecEspTransformStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecEspTransformStatus.setStatus("mandatory")
_WfIpsecEspTransformName_Type = DisplayString
_WfIpsecEspTransformName_Object = MibTableColumn
wfIpsecEspTransformName = _WfIpsecEspTransformName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 10, 1, 3),
    _WfIpsecEspTransformName_Type()
)
wfIpsecEspTransformName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecEspTransformName.setStatus("mandatory")
_WfIpsecEspTransformNumber_Type = Integer32
_WfIpsecEspTransformNumber_Object = MibTableColumn
wfIpsecEspTransformNumber = _WfIpsecEspTransformNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 10, 1, 4),
    _WfIpsecEspTransformNumber_Type()
)
wfIpsecEspTransformNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecEspTransformNumber.setStatus("mandatory")


class _WfIpsecEspTransformCipherAlg_Type(Integer32):
    """Custom type wfIpsecEspTransformCipherAlg based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("des", 2),
          ("desede", 3),
          ("none", 1))
    )


_WfIpsecEspTransformCipherAlg_Type.__name__ = "Integer32"
_WfIpsecEspTransformCipherAlg_Object = MibTableColumn
wfIpsecEspTransformCipherAlg = _WfIpsecEspTransformCipherAlg_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 10, 1, 5),
    _WfIpsecEspTransformCipherAlg_Type()
)
wfIpsecEspTransformCipherAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecEspTransformCipherAlg.setStatus("mandatory")
_WfIpsecEspTransformKeyLength_Type = Integer32
_WfIpsecEspTransformKeyLength_Object = MibTableColumn
wfIpsecEspTransformKeyLength = _WfIpsecEspTransformKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 10, 1, 6),
    _WfIpsecEspTransformKeyLength_Type()
)
wfIpsecEspTransformKeyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecEspTransformKeyLength.setStatus("mandatory")


class _WfIpsecEspTransformIntegrityAlg_Type(Integer32):
    """Custom type wfIpsecEspTransformIntegrityAlg based on Integer32"""
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
        *(("hmacMd5", 2),
          ("hmacSha1", 3),
          ("none", 1))
    )


_WfIpsecEspTransformIntegrityAlg_Type.__name__ = "Integer32"
_WfIpsecEspTransformIntegrityAlg_Object = MibTableColumn
wfIpsecEspTransformIntegrityAlg = _WfIpsecEspTransformIntegrityAlg_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 10, 1, 7),
    _WfIpsecEspTransformIntegrityAlg_Type()
)
wfIpsecEspTransformIntegrityAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecEspTransformIntegrityAlg.setStatus("mandatory")


class _WfIpsecEspTransformExpiryTime_Type(Integer32):
    """Custom type wfIpsecEspTransformExpiryTime based on Integer32"""
    defaultValue = 480


_WfIpsecEspTransformExpiryTime_Object = MibTableColumn
wfIpsecEspTransformExpiryTime = _WfIpsecEspTransformExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 10, 1, 8),
    _WfIpsecEspTransformExpiryTime_Type()
)
wfIpsecEspTransformExpiryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecEspTransformExpiryTime.setStatus("mandatory")


class _WfIpsecEspTransformExpiryMBytes_Type(Integer32):
    """Custom type wfIpsecEspTransformExpiryMBytes based on Integer32"""
    defaultValue = 1024


_WfIpsecEspTransformExpiryMBytes_Object = MibTableColumn
wfIpsecEspTransformExpiryMBytes = _WfIpsecEspTransformExpiryMBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 10, 1, 9),
    _WfIpsecEspTransformExpiryMBytes_Type()
)
wfIpsecEspTransformExpiryMBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecEspTransformExpiryMBytes.setStatus("mandatory")


class _WfIpsecEspTransformExpiryPref_Type(Integer32):
    """Custom type wfIpsecEspTransformExpiryPref based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mbytes", 2),
          ("minutes", 1))
    )


_WfIpsecEspTransformExpiryPref_Type.__name__ = "Integer32"
_WfIpsecEspTransformExpiryPref_Object = MibTableColumn
wfIpsecEspTransformExpiryPref = _WfIpsecEspTransformExpiryPref_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 10, 1, 10),
    _WfIpsecEspTransformExpiryPref_Type()
)
wfIpsecEspTransformExpiryPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecEspTransformExpiryPref.setStatus("mandatory")
_WfIpsecAhTransformTable_Object = MibTable
wfIpsecAhTransformTable = _WfIpsecAhTransformTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 11)
)
if mibBuilder.loadTexts:
    wfIpsecAhTransformTable.setStatus("mandatory")
_WfIpsecAhTransformEntry_Object = MibTableRow
wfIpsecAhTransformEntry = _WfIpsecAhTransformEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 11, 1)
)
wfIpsecAhTransformEntry.setIndexNames(
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecAhTransformNumber"),
)
if mibBuilder.loadTexts:
    wfIpsecAhTransformEntry.setStatus("mandatory")


class _WfIpsecAhTransformCreate_Type(Integer32):
    """Custom type wfIpsecAhTransformCreate based on Integer32"""
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


_WfIpsecAhTransformCreate_Type.__name__ = "Integer32"
_WfIpsecAhTransformCreate_Object = MibTableColumn
wfIpsecAhTransformCreate = _WfIpsecAhTransformCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 11, 1, 1),
    _WfIpsecAhTransformCreate_Type()
)
wfIpsecAhTransformCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecAhTransformCreate.setStatus("mandatory")


class _WfIpsecAhTransformStatus_Type(Integer32):
    """Custom type wfIpsecAhTransformStatus based on Integer32"""
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
        *(("active", 1),
          ("error", 2),
          ("inactive", 3),
          ("notpresent", 4))
    )


_WfIpsecAhTransformStatus_Type.__name__ = "Integer32"
_WfIpsecAhTransformStatus_Object = MibTableColumn
wfIpsecAhTransformStatus = _WfIpsecAhTransformStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 11, 1, 2),
    _WfIpsecAhTransformStatus_Type()
)
wfIpsecAhTransformStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecAhTransformStatus.setStatus("mandatory")
_WfIpsecAhTransformName_Type = DisplayString
_WfIpsecAhTransformName_Object = MibTableColumn
wfIpsecAhTransformName = _WfIpsecAhTransformName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 11, 1, 3),
    _WfIpsecAhTransformName_Type()
)
wfIpsecAhTransformName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecAhTransformName.setStatus("mandatory")
_WfIpsecAhTransformNumber_Type = Integer32
_WfIpsecAhTransformNumber_Object = MibTableColumn
wfIpsecAhTransformNumber = _WfIpsecAhTransformNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 11, 1, 4),
    _WfIpsecAhTransformNumber_Type()
)
wfIpsecAhTransformNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecAhTransformNumber.setStatus("mandatory")


class _WfIpsecAhTransformIntegrityAlg_Type(Integer32):
    """Custom type wfIpsecAhTransformIntegrityAlg based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hmacMd5", 2),
          ("hmacSha1", 3),
          ("none", 1))
    )


_WfIpsecAhTransformIntegrityAlg_Type.__name__ = "Integer32"
_WfIpsecAhTransformIntegrityAlg_Object = MibTableColumn
wfIpsecAhTransformIntegrityAlg = _WfIpsecAhTransformIntegrityAlg_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 11, 1, 5),
    _WfIpsecAhTransformIntegrityAlg_Type()
)
wfIpsecAhTransformIntegrityAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecAhTransformIntegrityAlg.setStatus("mandatory")


class _WfIpsecAhTransformGroup_Type(Integer32):
    """Custom type wfIpsecAhTransformGroup based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("one", 1)
    )


_WfIpsecAhTransformGroup_Type.__name__ = "Integer32"
_WfIpsecAhTransformGroup_Object = MibTableColumn
wfIpsecAhTransformGroup = _WfIpsecAhTransformGroup_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 11, 1, 6),
    _WfIpsecAhTransformGroup_Type()
)
wfIpsecAhTransformGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecAhTransformGroup.setStatus("mandatory")


class _WfIpsecAhTransformExpiryType_Type(Integer32):
    """Custom type wfIpsecAhTransformExpiryType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("kilobytes", 2),
          ("none", 3),
          ("seconds", 1))
    )


_WfIpsecAhTransformExpiryType_Type.__name__ = "Integer32"
_WfIpsecAhTransformExpiryType_Object = MibTableColumn
wfIpsecAhTransformExpiryType = _WfIpsecAhTransformExpiryType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 11, 1, 7),
    _WfIpsecAhTransformExpiryType_Type()
)
wfIpsecAhTransformExpiryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecAhTransformExpiryType.setStatus("mandatory")


class _WfIpsecAhTransformExpiryValue_Type(Integer32):
    """Custom type wfIpsecAhTransformExpiryValue based on Integer32"""
    defaultValue = 1024


_WfIpsecAhTransformExpiryValue_Object = MibTableColumn
wfIpsecAhTransformExpiryValue = _WfIpsecAhTransformExpiryValue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 11, 1, 8),
    _WfIpsecAhTransformExpiryValue_Type()
)
wfIpsecAhTransformExpiryValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpsecAhTransformExpiryValue.setStatus("mandatory")
_WfIpsecSaStatsTable_Object = MibTable
wfIpsecSaStatsTable = _WfIpsecSaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 12)
)
if mibBuilder.loadTexts:
    wfIpsecSaStatsTable.setStatus("mandatory")
_WfIpsecSaStatsEntry_Object = MibTableRow
wfIpsecSaStatsEntry = _WfIpsecSaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 12, 1)
)
wfIpsecSaStatsEntry.setIndexNames(
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecSaStatsSrc"),
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecSaStatsDest"),
    (0, "Wellfleet-IPSEC-MIB", "wfIpsecSaStatsSpi"),
)
if mibBuilder.loadTexts:
    wfIpsecSaStatsEntry.setStatus("mandatory")


class _WfIpsecSaStatsStatus_Type(Integer32):
    """Custom type wfIpsecSaStatsStatus based on Integer32"""
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
          ("inactive", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfIpsecSaStatsStatus_Type.__name__ = "Integer32"
_WfIpsecSaStatsStatus_Object = MibTableColumn
wfIpsecSaStatsStatus = _WfIpsecSaStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 12, 1, 1),
    _WfIpsecSaStatsStatus_Type()
)
wfIpsecSaStatsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSaStatsStatus.setStatus("mandatory")
_WfIpsecSaStatsSrc_Type = IpAddress
_WfIpsecSaStatsSrc_Object = MibTableColumn
wfIpsecSaStatsSrc = _WfIpsecSaStatsSrc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 12, 1, 2),
    _WfIpsecSaStatsSrc_Type()
)
wfIpsecSaStatsSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSaStatsSrc.setStatus("mandatory")
_WfIpsecSaStatsDest_Type = IpAddress
_WfIpsecSaStatsDest_Object = MibTableColumn
wfIpsecSaStatsDest = _WfIpsecSaStatsDest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 12, 1, 3),
    _WfIpsecSaStatsDest_Type()
)
wfIpsecSaStatsDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSaStatsDest.setStatus("mandatory")
_WfIpsecSaStatsSpi_Type = Gauge32
_WfIpsecSaStatsSpi_Object = MibTableColumn
wfIpsecSaStatsSpi = _WfIpsecSaStatsSpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 12, 1, 4),
    _WfIpsecSaStatsSpi_Type()
)
wfIpsecSaStatsSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSaStatsSpi.setStatus("mandatory")


class _WfIpsecSaStatsProto_Type(Integer32):
    """Custom type wfIpsecSaStatsProto based on Integer32"""
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
        *(("ah", 3),
          ("esp", 2),
          ("none", 1))
    )


_WfIpsecSaStatsProto_Type.__name__ = "Integer32"
_WfIpsecSaStatsProto_Object = MibTableColumn
wfIpsecSaStatsProto = _WfIpsecSaStatsProto_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 12, 1, 5),
    _WfIpsecSaStatsProto_Type()
)
wfIpsecSaStatsProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSaStatsProto.setStatus("mandatory")


class _WfIpsecSaStatsCipherAlg_Type(Integer32):
    """Custom type wfIpsecSaStatsCipherAlg based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("des", 2),
          ("desede", 3),
          ("none", 1))
    )


_WfIpsecSaStatsCipherAlg_Type.__name__ = "Integer32"
_WfIpsecSaStatsCipherAlg_Object = MibTableColumn
wfIpsecSaStatsCipherAlg = _WfIpsecSaStatsCipherAlg_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 12, 1, 6),
    _WfIpsecSaStatsCipherAlg_Type()
)
wfIpsecSaStatsCipherAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSaStatsCipherAlg.setStatus("mandatory")


class _WfIpsecSaStatsIntegrityAlg_Type(Integer32):
    """Custom type wfIpsecSaStatsIntegrityAlg based on Integer32"""
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
        *(("hmacMd5", 2),
          ("hmacSha1", 3),
          ("none", 1))
    )


_WfIpsecSaStatsIntegrityAlg_Type.__name__ = "Integer32"
_WfIpsecSaStatsIntegrityAlg_Object = MibTableColumn
wfIpsecSaStatsIntegrityAlg = _WfIpsecSaStatsIntegrityAlg_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 12, 1, 7),
    _WfIpsecSaStatsIntegrityAlg_Type()
)
wfIpsecSaStatsIntegrityAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSaStatsIntegrityAlg.setStatus("mandatory")
_WfIpsecSaStatsBadAuthen_Type = Counter32
_WfIpsecSaStatsBadAuthen_Object = MibTableColumn
wfIpsecSaStatsBadAuthen = _WfIpsecSaStatsBadAuthen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 12, 1, 8),
    _WfIpsecSaStatsBadAuthen_Type()
)
wfIpsecSaStatsBadAuthen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSaStatsBadAuthen.setStatus("mandatory")
_WfIpsecSaStatsBadDecrypt_Type = Counter32
_WfIpsecSaStatsBadDecrypt_Object = MibTableColumn
wfIpsecSaStatsBadDecrypt = _WfIpsecSaStatsBadDecrypt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 12, 1, 9),
    _WfIpsecSaStatsBadDecrypt_Type()
)
wfIpsecSaStatsBadDecrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSaStatsBadDecrypt.setStatus("mandatory")
_WfIpsecSaStatsBadPad_Type = Counter32
_WfIpsecSaStatsBadPad_Object = MibTableColumn
wfIpsecSaStatsBadPad = _WfIpsecSaStatsBadPad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 12, 1, 10),
    _WfIpsecSaStatsBadPad_Type()
)
wfIpsecSaStatsBadPad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSaStatsBadPad.setStatus("mandatory")
_WfIpsecSaStatsProtectPkt_Type = Counter32
_WfIpsecSaStatsProtectPkt_Object = MibTableColumn
wfIpsecSaStatsProtectPkt = _WfIpsecSaStatsProtectPkt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 12, 1, 11),
    _WfIpsecSaStatsProtectPkt_Type()
)
wfIpsecSaStatsProtectPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSaStatsProtectPkt.setStatus("mandatory")
_WfIpsecSaStatsUnprotectPkt_Type = Counter32
_WfIpsecSaStatsUnprotectPkt_Object = MibTableColumn
wfIpsecSaStatsUnprotectPkt = _WfIpsecSaStatsUnprotectPkt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 12, 1, 12),
    _WfIpsecSaStatsUnprotectPkt_Type()
)
wfIpsecSaStatsUnprotectPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSaStatsUnprotectPkt.setStatus("mandatory")
_WfIpsecSaStatsEncryptByte_Type = Counter32
_WfIpsecSaStatsEncryptByte_Object = MibTableColumn
wfIpsecSaStatsEncryptByte = _WfIpsecSaStatsEncryptByte_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 12, 1, 13),
    _WfIpsecSaStatsEncryptByte_Type()
)
wfIpsecSaStatsEncryptByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSaStatsEncryptByte.setStatus("mandatory")
_WfIpsecSaStatsDecryptByte_Type = Counter32
_WfIpsecSaStatsDecryptByte_Object = MibTableColumn
wfIpsecSaStatsDecryptByte = _WfIpsecSaStatsDecryptByte_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 12, 1, 14),
    _WfIpsecSaStatsDecryptByte_Type()
)
wfIpsecSaStatsDecryptByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSaStatsDecryptByte.setStatus("mandatory")


class _WfIpsecSaStatsMode_Type(Integer32):
    """Custom type wfIpsecSaStatsMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transport", 2),
          ("tunnel", 1))
    )


_WfIpsecSaStatsMode_Type.__name__ = "Integer32"
_WfIpsecSaStatsMode_Object = MibTableColumn
wfIpsecSaStatsMode = _WfIpsecSaStatsMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 12, 1, 15),
    _WfIpsecSaStatsMode_Type()
)
wfIpsecSaStatsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSaStatsMode.setStatus("mandatory")


class _WfIpsecSaStatsPfs_Type(Integer32):
    """Custom type wfIpsecSaStatsPfs based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_WfIpsecSaStatsPfs_Type.__name__ = "Integer32"
_WfIpsecSaStatsPfs_Object = MibTableColumn
wfIpsecSaStatsPfs = _WfIpsecSaStatsPfs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 12, 1, 16),
    _WfIpsecSaStatsPfs_Type()
)
wfIpsecSaStatsPfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSaStatsPfs.setStatus("mandatory")


class _WfIpsecSaStatsExpiryType_Type(Integer32):
    """Custom type wfIpsecSaStatsExpiryType based on Integer32"""
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
        *(("kilobytes", 2),
          ("none", 3),
          ("seconds", 1))
    )


_WfIpsecSaStatsExpiryType_Type.__name__ = "Integer32"
_WfIpsecSaStatsExpiryType_Object = MibTableColumn
wfIpsecSaStatsExpiryType = _WfIpsecSaStatsExpiryType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 12, 1, 17),
    _WfIpsecSaStatsExpiryType_Type()
)
wfIpsecSaStatsExpiryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSaStatsExpiryType.setStatus("mandatory")
_WfIpsecSaStatsExpiryValue_Type = Integer32
_WfIpsecSaStatsExpiryValue_Object = MibTableColumn
wfIpsecSaStatsExpiryValue = _WfIpsecSaStatsExpiryValue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26, 12, 1, 18),
    _WfIpsecSaStatsExpiryValue_Type()
)
wfIpsecSaStatsExpiryValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpsecSaStatsExpiryValue.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-IPSEC-MIB",
    **{"wfIpsecBase": wfIpsecBase,
       "wfIpsecBaseCreate": wfIpsecBaseCreate,
       "wfIpsecBaseEnable": wfIpsecBaseEnable,
       "wfIpsecBaseState": wfIpsecBaseState,
       "wfIpsecBaseEspEncipherEnable": wfIpsecBaseEspEncipherEnable,
       "wfIpsecBaseMaxManualSpi": wfIpsecBaseMaxManualSpi,
       "wfIpsecSelectorInTable": wfIpsecSelectorInTable,
       "wfIpsecSelectorInEntry": wfIpsecSelectorInEntry,
       "wfIpsecSelectorInCreate": wfIpsecSelectorInCreate,
       "wfIpsecSelectorInEnable": wfIpsecSelectorInEnable,
       "wfIpsecSelectorInStatus": wfIpsecSelectorInStatus,
       "wfIpsecSelectorInCounter": wfIpsecSelectorInCounter,
       "wfIpsecSelectorInDefinition": wfIpsecSelectorInDefinition,
       "wfIpsecSelectorInReserved": wfIpsecSelectorInReserved,
       "wfIpsecSelectorInInterface": wfIpsecSelectorInInterface,
       "wfIpsecSelectorInCircuit": wfIpsecSelectorInCircuit,
       "wfIpsecSelectorInPolicyNumber": wfIpsecSelectorInPolicyNumber,
       "wfIpsecSelectorInFragment": wfIpsecSelectorInFragment,
       "wfIpsecSelectorInName": wfIpsecSelectorInName,
       "wfIpsecSelectorOutTable": wfIpsecSelectorOutTable,
       "wfIpsecSelectorOutEntry": wfIpsecSelectorOutEntry,
       "wfIpsecSelectorOutCreate": wfIpsecSelectorOutCreate,
       "wfIpsecSelectorOutEnable": wfIpsecSelectorOutEnable,
       "wfIpsecSelectorOutStatus": wfIpsecSelectorOutStatus,
       "wfIpsecSelectorOutCounter": wfIpsecSelectorOutCounter,
       "wfIpsecSelectorOutDefinition": wfIpsecSelectorOutDefinition,
       "wfIpsecSelectorOutReserved": wfIpsecSelectorOutReserved,
       "wfIpsecSelectorOutInterface": wfIpsecSelectorOutInterface,
       "wfIpsecSelectorOutCircuit": wfIpsecSelectorOutCircuit,
       "wfIpsecSelectorOutPolicyNumber": wfIpsecSelectorOutPolicyNumber,
       "wfIpsecSelectorOutFragment": wfIpsecSelectorOutFragment,
       "wfIpsecSelectorOutName": wfIpsecSelectorOutName,
       "wfIpsecDescriptorTable": wfIpsecDescriptorTable,
       "wfIpsecDescriptorEntry": wfIpsecDescriptorEntry,
       "wfIpsecDescriptorCreate": wfIpsecDescriptorCreate,
       "wfIpsecDescriptorStatus": wfIpsecDescriptorStatus,
       "wfIpsecDescriptorPolicyNumber": wfIpsecDescriptorPolicyNumber,
       "wfIpsecDescriptorInterface": wfIpsecDescriptorInterface,
       "wfIpsecDescriptorCircuit": wfIpsecDescriptorCircuit,
       "wfIpsecDescriptorManualSaList": wfIpsecDescriptorManualSaList,
       "wfIpsecDescriptorSaMode": wfIpsecDescriptorSaMode,
       "wfIpsecDescriptorPfs": wfIpsecDescriptorPfs,
       "wfIpsecDescriptorProposals": wfIpsecDescriptorProposals,
       "wfIpsecDescriptorSourceForDestAddr": wfIpsecDescriptorSourceForDestAddr,
       "wfIpsecDescriptorSourceForSrcAddr": wfIpsecDescriptorSourceForSrcAddr,
       "wfIpsecDescriptorSourceForProtocol": wfIpsecDescriptorSourceForProtocol,
       "wfIpsecDescriptorStartSourceAddr": wfIpsecDescriptorStartSourceAddr,
       "wfIpsecDescriptorEndSourceAddr": wfIpsecDescriptorEndSourceAddr,
       "wfIpsecDescriptorStartDestAddr": wfIpsecDescriptorStartDestAddr,
       "wfIpsecDescriptorEndDestAddr": wfIpsecDescriptorEndDestAddr,
       "wfIpsecDescriptorSourcePort": wfIpsecDescriptorSourcePort,
       "wfIpsecDescriptorProtocol": wfIpsecDescriptorProtocol,
       "wfIpsecDescriptorPrimarySG": wfIpsecDescriptorPrimarySG,
       "wfIpsecDescriptorInboundIdleTimer": wfIpsecDescriptorInboundIdleTimer,
       "wfIpsecDescriptorAntiReplayWindow": wfIpsecDescriptorAntiReplayWindow,
       "wfIpsecDescriptorDestPort": wfIpsecDescriptorDestPort,
       "wfIpsecEspSaTable": wfIpsecEspSaTable,
       "wfIpsecEspSaEntry": wfIpsecEspSaEntry,
       "wfIpsecEspSaCreate": wfIpsecEspSaCreate,
       "wfIpsecEspSaStatus": wfIpsecEspSaStatus,
       "wfIpsecEspSaSrc": wfIpsecEspSaSrc,
       "wfIpsecEspSaDest": wfIpsecEspSaDest,
       "wfIpsecEspSaSpi": wfIpsecEspSaSpi,
       "wfIpsecEspSaCipherAlg": wfIpsecEspSaCipherAlg,
       "wfIpsecEspSaManualCipherKey": wfIpsecEspSaManualCipherKey,
       "wfIpsecEspSaDesKeyStrength": wfIpsecEspSaDesKeyStrength,
       "wfIpsecEspSaIntegrityAlg": wfIpsecEspSaIntegrityAlg,
       "wfIpsecEspSaManualIntegrityKey": wfIpsecEspSaManualIntegrityKey,
       "wfIpsecEspSaVerifyPad": wfIpsecEspSaVerifyPad,
       "wfIpsecEspSaReset": wfIpsecEspSaReset,
       "wfIpsecEspSaBadAuthen": wfIpsecEspSaBadAuthen,
       "wfIpsecEspSaBadDecrypt": wfIpsecEspSaBadDecrypt,
       "wfIpsecEspSaBadPad": wfIpsecEspSaBadPad,
       "wfIpsecEspSaProtectPkt": wfIpsecEspSaProtectPkt,
       "wfIpsecEspSaUnprotectPkt": wfIpsecEspSaUnprotectPkt,
       "wfIpsecEspSaEncryptByte": wfIpsecEspSaEncryptByte,
       "wfIpsecEspSaDecryptByte": wfIpsecEspSaDecryptByte,
       "wfIpsecEspSaMode": wfIpsecEspSaMode,
       "wfIpsecEspSaPfs": wfIpsecEspSaPfs,
       "wfIpsecEspSaExpiryType": wfIpsecEspSaExpiryType,
       "wfIpsecEspSaExpiryValue": wfIpsecEspSaExpiryValue,
       "wfIpsecStatsTable": wfIpsecStatsTable,
       "wfIpsecStatsEntry": wfIpsecStatsEntry,
       "wfIpsecStatsCreate": wfIpsecStatsCreate,
       "wfIpsecStatsInterface": wfIpsecStatsInterface,
       "wfIpsecStatsCircuit": wfIpsecStatsCircuit,
       "wfIpsecStatsReset": wfIpsecStatsReset,
       "wfIpsecStatsUnprotectPkt": wfIpsecStatsUnprotectPkt,
       "wfIpsecStatsProtectPkt": wfIpsecStatsProtectPkt,
       "wfIpsecStatsBypassPkt": wfIpsecStatsBypassPkt,
       "wfIpsecStatsDropPkt": wfIpsecStatsDropPkt,
       "wfIpsecStatsNoSa": wfIpsecStatsNoSa,
       "wfIpsecStatsLastBadSpi": wfIpsecStatsLastBadSpi,
       "wfIpsecStatsNoPolicyMatch": wfIpsecStatsNoPolicyMatch,
       "wfIpsecStatsSaExpDropBytes": wfIpsecStatsSaExpDropBytes,
       "wfIpsecStatsOutClips": wfIpsecStatsOutClips,
       "wfIpsecStatsInClips": wfIpsecStatsInClips,
       "wfIpsecRemoteGatewayTable": wfIpsecRemoteGatewayTable,
       "wfIpsecRemoteGatewayEntry": wfIpsecRemoteGatewayEntry,
       "wfIpsecRemoteGatewayCreate": wfIpsecRemoteGatewayCreate,
       "wfIpsecRemoteGatewayEnable": wfIpsecRemoteGatewayEnable,
       "wfIpsecRemoteGatewayStatus": wfIpsecRemoteGatewayStatus,
       "wfIpsecRemoteGatewayInterface": wfIpsecRemoteGatewayInterface,
       "wfIpsecRemoteGatewayCircuit": wfIpsecRemoteGatewayCircuit,
       "wfIpsecRemoteGatewayIndex": wfIpsecRemoteGatewayIndex,
       "wfIpsecRemoteGatewayIpAddr": wfIpsecRemoteGatewayIpAddr,
       "wfIpsecRemoteGatewayRange": wfIpsecRemoteGatewayRange,
       "wfIpsecRemoteGatewayName": wfIpsecRemoteGatewayName,
       "wfIpsecProposalTable": wfIpsecProposalTable,
       "wfIpsecProposalEntry": wfIpsecProposalEntry,
       "wfIpsecProposalCreate": wfIpsecProposalCreate,
       "wfIpsecProposalStatus": wfIpsecProposalStatus,
       "wfIpsecProposalName": wfIpsecProposalName,
       "wfIpsecProposalNumber": wfIpsecProposalNumber,
       "wfIpsecProposalSuites": wfIpsecProposalSuites,
       "wfIpsecSuiteTable": wfIpsecSuiteTable,
       "wfIpsecSuiteEntry": wfIpsecSuiteEntry,
       "wfIpsecSuiteCreate": wfIpsecSuiteCreate,
       "wfIpsecSuiteStatus": wfIpsecSuiteStatus,
       "wfIpsecSuiteName": wfIpsecSuiteName,
       "wfIpsecSuiteNumber": wfIpsecSuiteNumber,
       "wfIpsecSuiteEspProtocol": wfIpsecSuiteEspProtocol,
       "wfIpsecSuiteAhProtocol": wfIpsecSuiteAhProtocol,
       "wfIpsecEspTransformTable": wfIpsecEspTransformTable,
       "wfIpsecEspTransformEntry": wfIpsecEspTransformEntry,
       "wfIpsecEspTransformCreate": wfIpsecEspTransformCreate,
       "wfIpsecEspTransformStatus": wfIpsecEspTransformStatus,
       "wfIpsecEspTransformName": wfIpsecEspTransformName,
       "wfIpsecEspTransformNumber": wfIpsecEspTransformNumber,
       "wfIpsecEspTransformCipherAlg": wfIpsecEspTransformCipherAlg,
       "wfIpsecEspTransformKeyLength": wfIpsecEspTransformKeyLength,
       "wfIpsecEspTransformIntegrityAlg": wfIpsecEspTransformIntegrityAlg,
       "wfIpsecEspTransformExpiryTime": wfIpsecEspTransformExpiryTime,
       "wfIpsecEspTransformExpiryMBytes": wfIpsecEspTransformExpiryMBytes,
       "wfIpsecEspTransformExpiryPref": wfIpsecEspTransformExpiryPref,
       "wfIpsecAhTransformTable": wfIpsecAhTransformTable,
       "wfIpsecAhTransformEntry": wfIpsecAhTransformEntry,
       "wfIpsecAhTransformCreate": wfIpsecAhTransformCreate,
       "wfIpsecAhTransformStatus": wfIpsecAhTransformStatus,
       "wfIpsecAhTransformName": wfIpsecAhTransformName,
       "wfIpsecAhTransformNumber": wfIpsecAhTransformNumber,
       "wfIpsecAhTransformIntegrityAlg": wfIpsecAhTransformIntegrityAlg,
       "wfIpsecAhTransformGroup": wfIpsecAhTransformGroup,
       "wfIpsecAhTransformExpiryType": wfIpsecAhTransformExpiryType,
       "wfIpsecAhTransformExpiryValue": wfIpsecAhTransformExpiryValue,
       "wfIpsecSaStatsTable": wfIpsecSaStatsTable,
       "wfIpsecSaStatsEntry": wfIpsecSaStatsEntry,
       "wfIpsecSaStatsStatus": wfIpsecSaStatsStatus,
       "wfIpsecSaStatsSrc": wfIpsecSaStatsSrc,
       "wfIpsecSaStatsDest": wfIpsecSaStatsDest,
       "wfIpsecSaStatsSpi": wfIpsecSaStatsSpi,
       "wfIpsecSaStatsProto": wfIpsecSaStatsProto,
       "wfIpsecSaStatsCipherAlg": wfIpsecSaStatsCipherAlg,
       "wfIpsecSaStatsIntegrityAlg": wfIpsecSaStatsIntegrityAlg,
       "wfIpsecSaStatsBadAuthen": wfIpsecSaStatsBadAuthen,
       "wfIpsecSaStatsBadDecrypt": wfIpsecSaStatsBadDecrypt,
       "wfIpsecSaStatsBadPad": wfIpsecSaStatsBadPad,
       "wfIpsecSaStatsProtectPkt": wfIpsecSaStatsProtectPkt,
       "wfIpsecSaStatsUnprotectPkt": wfIpsecSaStatsUnprotectPkt,
       "wfIpsecSaStatsEncryptByte": wfIpsecSaStatsEncryptByte,
       "wfIpsecSaStatsDecryptByte": wfIpsecSaStatsDecryptByte,
       "wfIpsecSaStatsMode": wfIpsecSaStatsMode,
       "wfIpsecSaStatsPfs": wfIpsecSaStatsPfs,
       "wfIpsecSaStatsExpiryType": wfIpsecSaStatsExpiryType,
       "wfIpsecSaStatsExpiryValue": wfIpsecSaStatsExpiryValue}
)
