# SNMP MIB module (PNHRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PNHRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:06 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(xylanNHRP,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanNHRP")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PNHRPMIB_ObjectIdentity = ObjectIdentity
pNHRPMIB = _PNHRPMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 4, 1)
)
_PNHRPConfigGroup_ObjectIdentity = ObjectIdentity
pNHRPConfigGroup = _PNHRPConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 4, 1, 1)
)
_PNHRPConfigCommon_ObjectIdentity = ObjectIdentity
pNHRPConfigCommon = _PNHRPConfigCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 4, 1, 1, 1)
)


class _PNHRPResolutionCacheSize_Type(Integer32):
    """Custom type pNHRPResolutionCacheSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 65535),
    )


_PNHRPResolutionCacheSize_Type.__name__ = "Integer32"
_PNHRPResolutionCacheSize_Object = MibScalar
pNHRPResolutionCacheSize = _PNHRPResolutionCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 4, 1, 1, 1, 1),
    _PNHRPResolutionCacheSize_Type()
)
pNHRPResolutionCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNHRPResolutionCacheSize.setStatus("mandatory")
_PNHRPIPExcludeTable_Object = MibTable
pNHRPIPExcludeTable = _PNHRPIPExcludeTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 4, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pNHRPIPExcludeTable.setStatus("mandatory")
_PNHRPIPExcludeEntry_Object = MibTableRow
pNHRPIPExcludeEntry = _PNHRPIPExcludeEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 4, 1, 1, 1, 2, 1)
)
pNHRPIPExcludeEntry.setIndexNames(
    (0, "PNHRP-MIB", "pNHRPIPExcludeAddress"),
)
if mibBuilder.loadTexts:
    pNHRPIPExcludeEntry.setStatus("mandatory")
_PNHRPIPExcludeAddress_Type = IpAddress
_PNHRPIPExcludeAddress_Object = MibTableColumn
pNHRPIPExcludeAddress = _PNHRPIPExcludeAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 4, 1, 1, 1, 2, 1, 1),
    _PNHRPIPExcludeAddress_Type()
)
pNHRPIPExcludeAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pNHRPIPExcludeAddress.setStatus("mandatory")
_PNHRPIPExcludeMask_Type = IpAddress
_PNHRPIPExcludeMask_Object = MibTableColumn
pNHRPIPExcludeMask = _PNHRPIPExcludeMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 4, 1, 1, 1, 2, 1, 2),
    _PNHRPIPExcludeMask_Type()
)
pNHRPIPExcludeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNHRPIPExcludeMask.setStatus("mandatory")
_PNHRPIPExcludeRowStatus_Type = RowStatus
_PNHRPIPExcludeRowStatus_Object = MibTableColumn
pNHRPIPExcludeRowStatus = _PNHRPIPExcludeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 4, 1, 1, 1, 2, 1, 3),
    _PNHRPIPExcludeRowStatus_Type()
)
pNHRPIPExcludeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNHRPIPExcludeRowStatus.setStatus("mandatory")
_PNHRPConfigClient_ObjectIdentity = ObjectIdentity
pNHRPConfigClient = _PNHRPConfigClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 4, 1, 1, 2)
)


class _PNHRPDataRate_Type(Integer32):
    """Custom type pNHRPDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5120),
    )


_PNHRPDataRate_Type.__name__ = "Integer32"
_PNHRPDataRate_Object = MibScalar
pNHRPDataRate = _PNHRPDataRate_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 4, 1, 1, 2, 1),
    _PNHRPDataRate_Type()
)
pNHRPDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNHRPDataRate.setStatus("mandatory")
_PNHRPPortTable_Object = MibTable
pNHRPPortTable = _PNHRPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 4, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    pNHRPPortTable.setStatus("mandatory")
_PNHRPPortEntry_Object = MibTableRow
pNHRPPortEntry = _PNHRPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 4, 1, 1, 2, 2, 1)
)
pNHRPPortEntry.setIndexNames(
    (0, "PNHRP-MIB", "pNHRPPortSlot"),
    (0, "PNHRP-MIB", "pNHRPPortIf"),
)
if mibBuilder.loadTexts:
    pNHRPPortEntry.setStatus("mandatory")


class _PNHRPPortSlot_Type(Integer32):
    """Custom type pNHRPPortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_PNHRPPortSlot_Type.__name__ = "Integer32"
_PNHRPPortSlot_Object = MibTableColumn
pNHRPPortSlot = _PNHRPPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 4, 1, 1, 2, 2, 1, 1),
    _PNHRPPortSlot_Type()
)
pNHRPPortSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pNHRPPortSlot.setStatus("mandatory")


class _PNHRPPortIf_Type(Integer32):
    """Custom type pNHRPPortIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_PNHRPPortIf_Type.__name__ = "Integer32"
_PNHRPPortIf_Object = MibTableColumn
pNHRPPortIf = _PNHRPPortIf_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 4, 1, 1, 2, 2, 1, 2),
    _PNHRPPortIf_Type()
)
pNHRPPortIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pNHRPPortIf.setStatus("mandatory")


class _PNHRPPortUseBestEffort_Type(Integer32):
    """Custom type pNHRPPortUseBestEffort based on Integer32"""
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


_PNHRPPortUseBestEffort_Type.__name__ = "Integer32"
_PNHRPPortUseBestEffort_Object = MibTableColumn
pNHRPPortUseBestEffort = _PNHRPPortUseBestEffort_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 4, 1, 1, 2, 2, 1, 3),
    _PNHRPPortUseBestEffort_Type()
)
pNHRPPortUseBestEffort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNHRPPortUseBestEffort.setStatus("mandatory")


class _PNHRPPortPeakCellRate_Type(Integer32):
    """Custom type pNHRPPortPeakCellRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_PNHRPPortPeakCellRate_Type.__name__ = "Integer32"
_PNHRPPortPeakCellRate_Object = MibTableColumn
pNHRPPortPeakCellRate = _PNHRPPortPeakCellRate_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 4, 1, 1, 2, 2, 1, 4),
    _PNHRPPortPeakCellRate_Type()
)
pNHRPPortPeakCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNHRPPortPeakCellRate.setStatus("mandatory")


class _PNHRPPortSustainedCellRate_Type(Integer32):
    """Custom type pNHRPPortSustainedCellRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_PNHRPPortSustainedCellRate_Type.__name__ = "Integer32"
_PNHRPPortSustainedCellRate_Object = MibTableColumn
pNHRPPortSustainedCellRate = _PNHRPPortSustainedCellRate_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 4, 1, 1, 2, 2, 1, 5),
    _PNHRPPortSustainedCellRate_Type()
)
pNHRPPortSustainedCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNHRPPortSustainedCellRate.setStatus("mandatory")


class _PNHRPPortUseMyMAC_Type(Integer32):
    """Custom type pNHRPPortUseMyMAC based on Integer32"""
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


_PNHRPPortUseMyMAC_Type.__name__ = "Integer32"
_PNHRPPortUseMyMAC_Object = MibTableColumn
pNHRPPortUseMyMAC = _PNHRPPortUseMyMAC_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 4, 1, 1, 2, 2, 1, 6),
    _PNHRPPortUseMyMAC_Type()
)
pNHRPPortUseMyMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNHRPPortUseMyMAC.setStatus("mandatory")
_PNHRPPortRowStatus_Type = RowStatus
_PNHRPPortRowStatus_Object = MibTableColumn
pNHRPPortRowStatus = _PNHRPPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 4, 1, 1, 2, 2, 1, 7),
    _PNHRPPortRowStatus_Type()
)
pNHRPPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNHRPPortRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PNHRP-MIB",
    **{"pNHRPMIB": pNHRPMIB,
       "pNHRPConfigGroup": pNHRPConfigGroup,
       "pNHRPConfigCommon": pNHRPConfigCommon,
       "pNHRPResolutionCacheSize": pNHRPResolutionCacheSize,
       "pNHRPIPExcludeTable": pNHRPIPExcludeTable,
       "pNHRPIPExcludeEntry": pNHRPIPExcludeEntry,
       "pNHRPIPExcludeAddress": pNHRPIPExcludeAddress,
       "pNHRPIPExcludeMask": pNHRPIPExcludeMask,
       "pNHRPIPExcludeRowStatus": pNHRPIPExcludeRowStatus,
       "pNHRPConfigClient": pNHRPConfigClient,
       "pNHRPDataRate": pNHRPDataRate,
       "pNHRPPortTable": pNHRPPortTable,
       "pNHRPPortEntry": pNHRPPortEntry,
       "pNHRPPortSlot": pNHRPPortSlot,
       "pNHRPPortIf": pNHRPPortIf,
       "pNHRPPortUseBestEffort": pNHRPPortUseBestEffort,
       "pNHRPPortPeakCellRate": pNHRPPortPeakCellRate,
       "pNHRPPortSustainedCellRate": pNHRPPortSustainedCellRate,
       "pNHRPPortUseMyMAC": pNHRPPortUseMyMAC,
       "pNHRPPortRowStatus": pNHRPPortRowStatus}
)
