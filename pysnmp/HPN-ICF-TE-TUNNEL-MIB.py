# SNMP MIB module (HPN-ICF-TE-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-TE-TUNNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:59 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(MplsExtendedTunnelId,
 MplsLabel,
 MplsTunnelIndex,
 MplsTunnelInstanceIndex) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsExtendedTunnelId",
    "MplsLabel",
    "MplsTunnelIndex",
    "MplsTunnelInstanceIndex")

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
 RowPointer,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfTeTunnel = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfTeTunnelScalars_ObjectIdentity = ObjectIdentity
hpnicfTeTunnelScalars = _HpnicfTeTunnelScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 1)
)
_HpnicfTeTunnelMaxTunnelIndex_Type = MplsTunnelIndex
_HpnicfTeTunnelMaxTunnelIndex_Object = MibScalar
hpnicfTeTunnelMaxTunnelIndex = _HpnicfTeTunnelMaxTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 1, 1),
    _HpnicfTeTunnelMaxTunnelIndex_Type()
)
hpnicfTeTunnelMaxTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTeTunnelMaxTunnelIndex.setStatus("current")
_HpnicfTeTunnelObjects_ObjectIdentity = ObjectIdentity
hpnicfTeTunnelObjects = _HpnicfTeTunnelObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2)
)
_HpnicfTeTunnelStaticCrlspTable_Object = MibTable
hpnicfTeTunnelStaticCrlspTable = _HpnicfTeTunnelStaticCrlspTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfTeTunnelStaticCrlspTable.setStatus("current")
_HpnicfTeTunnelStaticCrlspEntry_Object = MibTableRow
hpnicfTeTunnelStaticCrlspEntry = _HpnicfTeTunnelStaticCrlspEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 1, 1)
)
hpnicfTeTunnelStaticCrlspEntry.setIndexNames(
    (0, "HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelStaticCrlspInLabel"),
)
if mibBuilder.loadTexts:
    hpnicfTeTunnelStaticCrlspEntry.setStatus("current")
_HpnicfTeTunnelStaticCrlspInLabel_Type = MplsLabel
_HpnicfTeTunnelStaticCrlspInLabel_Object = MibTableColumn
hpnicfTeTunnelStaticCrlspInLabel = _HpnicfTeTunnelStaticCrlspInLabel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 1, 1, 1),
    _HpnicfTeTunnelStaticCrlspInLabel_Type()
)
hpnicfTeTunnelStaticCrlspInLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTeTunnelStaticCrlspInLabel.setStatus("current")


class _HpnicfTeTunnelStaticCrlspName_Type(OctetString):
    """Custom type hpnicfTeTunnelStaticCrlspName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_HpnicfTeTunnelStaticCrlspName_Type.__name__ = "OctetString"
_HpnicfTeTunnelStaticCrlspName_Object = MibTableColumn
hpnicfTeTunnelStaticCrlspName = _HpnicfTeTunnelStaticCrlspName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 1, 1, 2),
    _HpnicfTeTunnelStaticCrlspName_Type()
)
hpnicfTeTunnelStaticCrlspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTeTunnelStaticCrlspName.setStatus("current")


class _HpnicfTeTunnelStaticCrlspStatus_Type(Integer32):
    """Custom type hpnicfTeTunnelStaticCrlspStatus based on Integer32"""
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


_HpnicfTeTunnelStaticCrlspStatus_Type.__name__ = "Integer32"
_HpnicfTeTunnelStaticCrlspStatus_Object = MibTableColumn
hpnicfTeTunnelStaticCrlspStatus = _HpnicfTeTunnelStaticCrlspStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 1, 1, 3),
    _HpnicfTeTunnelStaticCrlspStatus_Type()
)
hpnicfTeTunnelStaticCrlspStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTeTunnelStaticCrlspStatus.setStatus("current")


class _HpnicfTeTunnelStaticCrlspRole_Type(Integer32):
    """Custom type hpnicfTeTunnelStaticCrlspRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tail", 2),
          ("transit", 1))
    )


_HpnicfTeTunnelStaticCrlspRole_Type.__name__ = "Integer32"
_HpnicfTeTunnelStaticCrlspRole_Object = MibTableColumn
hpnicfTeTunnelStaticCrlspRole = _HpnicfTeTunnelStaticCrlspRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 1, 1, 4),
    _HpnicfTeTunnelStaticCrlspRole_Type()
)
hpnicfTeTunnelStaticCrlspRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTeTunnelStaticCrlspRole.setStatus("current")
_HpnicfTeTunnelStaticCrlspXCPointer_Type = RowPointer
_HpnicfTeTunnelStaticCrlspXCPointer_Object = MibTableColumn
hpnicfTeTunnelStaticCrlspXCPointer = _HpnicfTeTunnelStaticCrlspXCPointer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 1, 1, 5),
    _HpnicfTeTunnelStaticCrlspXCPointer_Type()
)
hpnicfTeTunnelStaticCrlspXCPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTeTunnelStaticCrlspXCPointer.setStatus("current")
_HpnicfTeTunnelCoTable_Object = MibTable
hpnicfTeTunnelCoTable = _HpnicfTeTunnelCoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfTeTunnelCoTable.setStatus("current")
_HpnicfTeTunnelCoEntry_Object = MibTableRow
hpnicfTeTunnelCoEntry = _HpnicfTeTunnelCoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2, 1)
)
hpnicfTeTunnelCoEntry.setIndexNames(
    (0, "HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelCoIndex"),
    (0, "HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelCoLspInstance"),
    (0, "HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelCoIngressLSRId"),
    (0, "HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelCoEgressLSRId"),
)
if mibBuilder.loadTexts:
    hpnicfTeTunnelCoEntry.setStatus("current")
_HpnicfTeTunnelCoIndex_Type = MplsTunnelIndex
_HpnicfTeTunnelCoIndex_Object = MibTableColumn
hpnicfTeTunnelCoIndex = _HpnicfTeTunnelCoIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2, 1, 1),
    _HpnicfTeTunnelCoIndex_Type()
)
hpnicfTeTunnelCoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTeTunnelCoIndex.setStatus("current")
_HpnicfTeTunnelCoLspInstance_Type = MplsTunnelInstanceIndex
_HpnicfTeTunnelCoLspInstance_Object = MibTableColumn
hpnicfTeTunnelCoLspInstance = _HpnicfTeTunnelCoLspInstance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2, 1, 2),
    _HpnicfTeTunnelCoLspInstance_Type()
)
hpnicfTeTunnelCoLspInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTeTunnelCoLspInstance.setStatus("current")
_HpnicfTeTunnelCoIngressLSRId_Type = MplsExtendedTunnelId
_HpnicfTeTunnelCoIngressLSRId_Object = MibTableColumn
hpnicfTeTunnelCoIngressLSRId = _HpnicfTeTunnelCoIngressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2, 1, 3),
    _HpnicfTeTunnelCoIngressLSRId_Type()
)
hpnicfTeTunnelCoIngressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTeTunnelCoIngressLSRId.setStatus("current")
_HpnicfTeTunnelCoEgressLSRId_Type = MplsExtendedTunnelId
_HpnicfTeTunnelCoEgressLSRId_Object = MibTableColumn
hpnicfTeTunnelCoEgressLSRId = _HpnicfTeTunnelCoEgressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2, 1, 4),
    _HpnicfTeTunnelCoEgressLSRId_Type()
)
hpnicfTeTunnelCoEgressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTeTunnelCoEgressLSRId.setStatus("current")


class _HpnicfTeTunnelCoBiMode_Type(Integer32):
    """Custom type hpnicfTeTunnelCoBiMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("coroutedActive", 1),
          ("coroutedPassive", 2))
    )


_HpnicfTeTunnelCoBiMode_Type.__name__ = "Integer32"
_HpnicfTeTunnelCoBiMode_Object = MibTableColumn
hpnicfTeTunnelCoBiMode = _HpnicfTeTunnelCoBiMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2, 1, 5),
    _HpnicfTeTunnelCoBiMode_Type()
)
hpnicfTeTunnelCoBiMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTeTunnelCoBiMode.setStatus("current")
_HpnicfTeTunnelCoReverseLspInstance_Type = MplsTunnelInstanceIndex
_HpnicfTeTunnelCoReverseLspInstance_Object = MibTableColumn
hpnicfTeTunnelCoReverseLspInstance = _HpnicfTeTunnelCoReverseLspInstance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2, 1, 6),
    _HpnicfTeTunnelCoReverseLspInstance_Type()
)
hpnicfTeTunnelCoReverseLspInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTeTunnelCoReverseLspInstance.setStatus("current")
_HpnicfTeTunnelCoReverseLspXCPointer_Type = RowPointer
_HpnicfTeTunnelCoReverseLspXCPointer_Object = MibTableColumn
hpnicfTeTunnelCoReverseLspXCPointer = _HpnicfTeTunnelCoReverseLspXCPointer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2, 1, 7),
    _HpnicfTeTunnelCoReverseLspXCPointer_Type()
)
hpnicfTeTunnelCoReverseLspXCPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTeTunnelCoReverseLspXCPointer.setStatus("current")
_HpnicfTeTunnelPsTable_Object = MibTable
hpnicfTeTunnelPsTable = _HpnicfTeTunnelPsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfTeTunnelPsTable.setStatus("current")
_HpnicfTeTunnelPsEntry_Object = MibTableRow
hpnicfTeTunnelPsEntry = _HpnicfTeTunnelPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1)
)
hpnicfTeTunnelPsEntry.setIndexNames(
    (0, "HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsIndex"),
    (0, "HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsIngressLSRId"),
    (0, "HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsEgressLSRId"),
)
if mibBuilder.loadTexts:
    hpnicfTeTunnelPsEntry.setStatus("current")
_HpnicfTeTunnelPsIndex_Type = MplsTunnelIndex
_HpnicfTeTunnelPsIndex_Object = MibTableColumn
hpnicfTeTunnelPsIndex = _HpnicfTeTunnelPsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 1),
    _HpnicfTeTunnelPsIndex_Type()
)
hpnicfTeTunnelPsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTeTunnelPsIndex.setStatus("current")
_HpnicfTeTunnelPsIngressLSRId_Type = MplsExtendedTunnelId
_HpnicfTeTunnelPsIngressLSRId_Object = MibTableColumn
hpnicfTeTunnelPsIngressLSRId = _HpnicfTeTunnelPsIngressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 2),
    _HpnicfTeTunnelPsIngressLSRId_Type()
)
hpnicfTeTunnelPsIngressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTeTunnelPsIngressLSRId.setStatus("current")
_HpnicfTeTunnelPsEgressLSRId_Type = MplsExtendedTunnelId
_HpnicfTeTunnelPsEgressLSRId_Object = MibTableColumn
hpnicfTeTunnelPsEgressLSRId = _HpnicfTeTunnelPsEgressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 3),
    _HpnicfTeTunnelPsEgressLSRId_Type()
)
hpnicfTeTunnelPsEgressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTeTunnelPsEgressLSRId.setStatus("current")
_HpnicfTeTunnelPsProtectIndex_Type = MplsTunnelIndex
_HpnicfTeTunnelPsProtectIndex_Object = MibTableColumn
hpnicfTeTunnelPsProtectIndex = _HpnicfTeTunnelPsProtectIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 4),
    _HpnicfTeTunnelPsProtectIndex_Type()
)
hpnicfTeTunnelPsProtectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTeTunnelPsProtectIndex.setStatus("current")
_HpnicfTeTunnelPsProtectIngressLSRId_Type = MplsExtendedTunnelId
_HpnicfTeTunnelPsProtectIngressLSRId_Object = MibTableColumn
hpnicfTeTunnelPsProtectIngressLSRId = _HpnicfTeTunnelPsProtectIngressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 5),
    _HpnicfTeTunnelPsProtectIngressLSRId_Type()
)
hpnicfTeTunnelPsProtectIngressLSRId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTeTunnelPsProtectIngressLSRId.setStatus("current")
_HpnicfTeTunnelPsProtectEgressLSRId_Type = MplsExtendedTunnelId
_HpnicfTeTunnelPsProtectEgressLSRId_Object = MibTableColumn
hpnicfTeTunnelPsProtectEgressLSRId = _HpnicfTeTunnelPsProtectEgressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 6),
    _HpnicfTeTunnelPsProtectEgressLSRId_Type()
)
hpnicfTeTunnelPsProtectEgressLSRId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTeTunnelPsProtectEgressLSRId.setStatus("current")


class _HpnicfTeTunnelPsProtectType_Type(Integer32):
    """Custom type hpnicfTeTunnelPsProtectType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onePlusOne", 2),
          ("oneToOne", 1))
    )


_HpnicfTeTunnelPsProtectType_Type.__name__ = "Integer32"
_HpnicfTeTunnelPsProtectType_Object = MibTableColumn
hpnicfTeTunnelPsProtectType = _HpnicfTeTunnelPsProtectType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 7),
    _HpnicfTeTunnelPsProtectType_Type()
)
hpnicfTeTunnelPsProtectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTeTunnelPsProtectType.setStatus("current")


class _HpnicfTeTunnelPsRevertiveMode_Type(Integer32):
    """Custom type hpnicfTeTunnelPsRevertiveMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRevertive", 2),
          ("revertive", 1))
    )


_HpnicfTeTunnelPsRevertiveMode_Type.__name__ = "Integer32"
_HpnicfTeTunnelPsRevertiveMode_Object = MibTableColumn
hpnicfTeTunnelPsRevertiveMode = _HpnicfTeTunnelPsRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 8),
    _HpnicfTeTunnelPsRevertiveMode_Type()
)
hpnicfTeTunnelPsRevertiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTeTunnelPsRevertiveMode.setStatus("current")


class _HpnicfTeTunnelPsWtrTime_Type(Unsigned32):
    """Custom type hpnicfTeTunnelPsWtrTime based on Unsigned32"""
    defaultValue = 24

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_HpnicfTeTunnelPsWtrTime_Type.__name__ = "Unsigned32"
_HpnicfTeTunnelPsWtrTime_Object = MibTableColumn
hpnicfTeTunnelPsWtrTime = _HpnicfTeTunnelPsWtrTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 9),
    _HpnicfTeTunnelPsWtrTime_Type()
)
hpnicfTeTunnelPsWtrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTeTunnelPsWtrTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfTeTunnelPsWtrTime.setUnits("30 seconds")


class _HpnicfTeTunnelPsHoldOffTime_Type(Unsigned32):
    """Custom type hpnicfTeTunnelPsHoldOffTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_HpnicfTeTunnelPsHoldOffTime_Type.__name__ = "Unsigned32"
_HpnicfTeTunnelPsHoldOffTime_Object = MibTableColumn
hpnicfTeTunnelPsHoldOffTime = _HpnicfTeTunnelPsHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 10),
    _HpnicfTeTunnelPsHoldOffTime_Type()
)
hpnicfTeTunnelPsHoldOffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTeTunnelPsHoldOffTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfTeTunnelPsHoldOffTime.setUnits("500ms")


class _HpnicfTeTunnelPsSwitchMode_Type(Integer32):
    """Custom type hpnicfTeTunnelPsSwitchMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("biDirectional", 2),
          ("uniDirectional", 1))
    )


_HpnicfTeTunnelPsSwitchMode_Type.__name__ = "Integer32"
_HpnicfTeTunnelPsSwitchMode_Object = MibTableColumn
hpnicfTeTunnelPsSwitchMode = _HpnicfTeTunnelPsSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 11),
    _HpnicfTeTunnelPsSwitchMode_Type()
)
hpnicfTeTunnelPsSwitchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTeTunnelPsSwitchMode.setStatus("current")


class _HpnicfTeTunnelPsWorkPathStatus_Type(Integer32):
    """Custom type hpnicfTeTunnelPsWorkPathStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inDefect", 3),
          ("noDefect", 2),
          ("none", 1))
    )


_HpnicfTeTunnelPsWorkPathStatus_Type.__name__ = "Integer32"
_HpnicfTeTunnelPsWorkPathStatus_Object = MibTableColumn
hpnicfTeTunnelPsWorkPathStatus = _HpnicfTeTunnelPsWorkPathStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 12),
    _HpnicfTeTunnelPsWorkPathStatus_Type()
)
hpnicfTeTunnelPsWorkPathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTeTunnelPsWorkPathStatus.setStatus("current")


class _HpnicfTeTunnelPsProtectPathStatus_Type(Integer32):
    """Custom type hpnicfTeTunnelPsProtectPathStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inDefect", 3),
          ("noDefect", 2),
          ("none", 1))
    )


_HpnicfTeTunnelPsProtectPathStatus_Type.__name__ = "Integer32"
_HpnicfTeTunnelPsProtectPathStatus_Object = MibTableColumn
hpnicfTeTunnelPsProtectPathStatus = _HpnicfTeTunnelPsProtectPathStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 13),
    _HpnicfTeTunnelPsProtectPathStatus_Type()
)
hpnicfTeTunnelPsProtectPathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTeTunnelPsProtectPathStatus.setStatus("current")


class _HpnicfTeTunnelPsSwitchResult_Type(Integer32):
    """Custom type hpnicfTeTunnelPsSwitchResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protectPath", 2),
          ("workPath", 1))
    )


_HpnicfTeTunnelPsSwitchResult_Type.__name__ = "Integer32"
_HpnicfTeTunnelPsSwitchResult_Object = MibTableColumn
hpnicfTeTunnelPsSwitchResult = _HpnicfTeTunnelPsSwitchResult_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 14),
    _HpnicfTeTunnelPsSwitchResult_Type()
)
hpnicfTeTunnelPsSwitchResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTeTunnelPsSwitchResult.setStatus("current")
_HpnicfTeTunnelNotifications_ObjectIdentity = ObjectIdentity
hpnicfTeTunnelNotifications = _HpnicfTeTunnelNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 3)
)
_HpnicfTeTunnelNotificationsPrefix_ObjectIdentity = ObjectIdentity
hpnicfTeTunnelNotificationsPrefix = _HpnicfTeTunnelNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 3, 0)
)
_HpnicfTeTunnelConformance_ObjectIdentity = ObjectIdentity
hpnicfTeTunnelConformance = _HpnicfTeTunnelConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4)
)
_HpnicfTeTunnelCompliances_ObjectIdentity = ObjectIdentity
hpnicfTeTunnelCompliances = _HpnicfTeTunnelCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4, 1)
)
_HpnicfTeTunnelGroups_ObjectIdentity = ObjectIdentity
hpnicfTeTunnelGroups = _HpnicfTeTunnelGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4, 2)
)

# Managed Objects groups

hpnicfTeTunnelScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4, 2, 2)
)
hpnicfTeTunnelScalarsGroup.setObjects(
    ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelMaxTunnelIndex")
)
if mibBuilder.loadTexts:
    hpnicfTeTunnelScalarsGroup.setStatus("current")

hpnicfTeTunnelStaticCrlspGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4, 2, 3)
)
hpnicfTeTunnelStaticCrlspGroup.setObjects(
      *(("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelStaticCrlspName"),
        ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelStaticCrlspStatus"),
        ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelStaticCrlspRole"),
        ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelStaticCrlspXCPointer"))
)
if mibBuilder.loadTexts:
    hpnicfTeTunnelStaticCrlspGroup.setStatus("current")

hpnicfTeTunnelCorouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4, 2, 4)
)
hpnicfTeTunnelCorouteGroup.setObjects(
      *(("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelCoBiMode"),
        ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelCoReverseLspInstance"),
        ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelCoReverseLspXCPointer"))
)
if mibBuilder.loadTexts:
    hpnicfTeTunnelCorouteGroup.setStatus("current")

hpnicfTeTunnelPsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4, 2, 5)
)
hpnicfTeTunnelPsGroup.setObjects(
      *(("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsProtectIndex"),
        ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsProtectIngressLSRId"),
        ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsProtectEgressLSRId"),
        ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsProtectType"),
        ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsRevertiveMode"),
        ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsWtrTime"),
        ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsHoldOffTime"),
        ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsSwitchMode"),
        ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsWorkPathStatus"),
        ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsProtectPathStatus"),
        ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsSwitchResult"))
)
if mibBuilder.loadTexts:
    hpnicfTeTunnelPsGroup.setStatus("current")


# Notification objects

hpnicfTeTunnelPsSwitchWtoP = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 3, 0, 1)
)
hpnicfTeTunnelPsSwitchWtoP.setObjects(
      *(("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsWorkPathStatus"),
        ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsProtectPathStatus"))
)
if mibBuilder.loadTexts:
    hpnicfTeTunnelPsSwitchWtoP.setStatus(
        "current"
    )

hpnicfTeTunnelPsSwitchPtoW = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 3, 0, 2)
)
hpnicfTeTunnelPsSwitchPtoW.setObjects(
      *(("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsWorkPathStatus"),
        ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsProtectPathStatus"))
)
if mibBuilder.loadTexts:
    hpnicfTeTunnelPsSwitchPtoW.setStatus(
        "current"
    )


# Notifications groups

hpnicfTeTunnelNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4, 2, 1)
)
hpnicfTeTunnelNotificationsGroup.setObjects(
      *(("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsSwitchPtoW"),
        ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsSwitchWtoP"))
)
if mibBuilder.loadTexts:
    hpnicfTeTunnelNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpnicfTeTunnelCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfTeTunnelCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-TE-TUNNEL-MIB",
    **{"hpnicfTeTunnel": hpnicfTeTunnel,
       "hpnicfTeTunnelScalars": hpnicfTeTunnelScalars,
       "hpnicfTeTunnelMaxTunnelIndex": hpnicfTeTunnelMaxTunnelIndex,
       "hpnicfTeTunnelObjects": hpnicfTeTunnelObjects,
       "hpnicfTeTunnelStaticCrlspTable": hpnicfTeTunnelStaticCrlspTable,
       "hpnicfTeTunnelStaticCrlspEntry": hpnicfTeTunnelStaticCrlspEntry,
       "hpnicfTeTunnelStaticCrlspInLabel": hpnicfTeTunnelStaticCrlspInLabel,
       "hpnicfTeTunnelStaticCrlspName": hpnicfTeTunnelStaticCrlspName,
       "hpnicfTeTunnelStaticCrlspStatus": hpnicfTeTunnelStaticCrlspStatus,
       "hpnicfTeTunnelStaticCrlspRole": hpnicfTeTunnelStaticCrlspRole,
       "hpnicfTeTunnelStaticCrlspXCPointer": hpnicfTeTunnelStaticCrlspXCPointer,
       "hpnicfTeTunnelCoTable": hpnicfTeTunnelCoTable,
       "hpnicfTeTunnelCoEntry": hpnicfTeTunnelCoEntry,
       "hpnicfTeTunnelCoIndex": hpnicfTeTunnelCoIndex,
       "hpnicfTeTunnelCoLspInstance": hpnicfTeTunnelCoLspInstance,
       "hpnicfTeTunnelCoIngressLSRId": hpnicfTeTunnelCoIngressLSRId,
       "hpnicfTeTunnelCoEgressLSRId": hpnicfTeTunnelCoEgressLSRId,
       "hpnicfTeTunnelCoBiMode": hpnicfTeTunnelCoBiMode,
       "hpnicfTeTunnelCoReverseLspInstance": hpnicfTeTunnelCoReverseLspInstance,
       "hpnicfTeTunnelCoReverseLspXCPointer": hpnicfTeTunnelCoReverseLspXCPointer,
       "hpnicfTeTunnelPsTable": hpnicfTeTunnelPsTable,
       "hpnicfTeTunnelPsEntry": hpnicfTeTunnelPsEntry,
       "hpnicfTeTunnelPsIndex": hpnicfTeTunnelPsIndex,
       "hpnicfTeTunnelPsIngressLSRId": hpnicfTeTunnelPsIngressLSRId,
       "hpnicfTeTunnelPsEgressLSRId": hpnicfTeTunnelPsEgressLSRId,
       "hpnicfTeTunnelPsProtectIndex": hpnicfTeTunnelPsProtectIndex,
       "hpnicfTeTunnelPsProtectIngressLSRId": hpnicfTeTunnelPsProtectIngressLSRId,
       "hpnicfTeTunnelPsProtectEgressLSRId": hpnicfTeTunnelPsProtectEgressLSRId,
       "hpnicfTeTunnelPsProtectType": hpnicfTeTunnelPsProtectType,
       "hpnicfTeTunnelPsRevertiveMode": hpnicfTeTunnelPsRevertiveMode,
       "hpnicfTeTunnelPsWtrTime": hpnicfTeTunnelPsWtrTime,
       "hpnicfTeTunnelPsHoldOffTime": hpnicfTeTunnelPsHoldOffTime,
       "hpnicfTeTunnelPsSwitchMode": hpnicfTeTunnelPsSwitchMode,
       "hpnicfTeTunnelPsWorkPathStatus": hpnicfTeTunnelPsWorkPathStatus,
       "hpnicfTeTunnelPsProtectPathStatus": hpnicfTeTunnelPsProtectPathStatus,
       "hpnicfTeTunnelPsSwitchResult": hpnicfTeTunnelPsSwitchResult,
       "hpnicfTeTunnelNotifications": hpnicfTeTunnelNotifications,
       "hpnicfTeTunnelNotificationsPrefix": hpnicfTeTunnelNotificationsPrefix,
       "hpnicfTeTunnelPsSwitchWtoP": hpnicfTeTunnelPsSwitchWtoP,
       "hpnicfTeTunnelPsSwitchPtoW": hpnicfTeTunnelPsSwitchPtoW,
       "hpnicfTeTunnelConformance": hpnicfTeTunnelConformance,
       "hpnicfTeTunnelCompliances": hpnicfTeTunnelCompliances,
       "hpnicfTeTunnelCompliance": hpnicfTeTunnelCompliance,
       "hpnicfTeTunnelGroups": hpnicfTeTunnelGroups,
       "hpnicfTeTunnelNotificationsGroup": hpnicfTeTunnelNotificationsGroup,
       "hpnicfTeTunnelScalarsGroup": hpnicfTeTunnelScalarsGroup,
       "hpnicfTeTunnelStaticCrlspGroup": hpnicfTeTunnelStaticCrlspGroup,
       "hpnicfTeTunnelCorouteGroup": hpnicfTeTunnelCorouteGroup,
       "hpnicfTeTunnelPsGroup": hpnicfTeTunnelPsGroup}
)
