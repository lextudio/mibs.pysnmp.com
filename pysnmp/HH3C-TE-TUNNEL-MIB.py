# SNMP MIB module (HH3C-TE-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-TE-TUNNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:05 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cTeTunnel = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cTeTunnelScalars_ObjectIdentity = ObjectIdentity
hh3cTeTunnelScalars = _Hh3cTeTunnelScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 1)
)
_Hh3cTeTunnelMaxTunnelIndex_Type = MplsTunnelIndex
_Hh3cTeTunnelMaxTunnelIndex_Object = MibScalar
hh3cTeTunnelMaxTunnelIndex = _Hh3cTeTunnelMaxTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 1, 1),
    _Hh3cTeTunnelMaxTunnelIndex_Type()
)
hh3cTeTunnelMaxTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTeTunnelMaxTunnelIndex.setStatus("current")
_Hh3cTeTunnelObjects_ObjectIdentity = ObjectIdentity
hh3cTeTunnelObjects = _Hh3cTeTunnelObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2)
)
_Hh3cTeTunnelStaticCrlspTable_Object = MibTable
hh3cTeTunnelStaticCrlspTable = _Hh3cTeTunnelStaticCrlspTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cTeTunnelStaticCrlspTable.setStatus("current")
_Hh3cTeTunnelStaticCrlspEntry_Object = MibTableRow
hh3cTeTunnelStaticCrlspEntry = _Hh3cTeTunnelStaticCrlspEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 1, 1)
)
hh3cTeTunnelStaticCrlspEntry.setIndexNames(
    (0, "HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelStaticCrlspInLabel"),
)
if mibBuilder.loadTexts:
    hh3cTeTunnelStaticCrlspEntry.setStatus("current")
_Hh3cTeTunnelStaticCrlspInLabel_Type = MplsLabel
_Hh3cTeTunnelStaticCrlspInLabel_Object = MibTableColumn
hh3cTeTunnelStaticCrlspInLabel = _Hh3cTeTunnelStaticCrlspInLabel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 1, 1, 1),
    _Hh3cTeTunnelStaticCrlspInLabel_Type()
)
hh3cTeTunnelStaticCrlspInLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTeTunnelStaticCrlspInLabel.setStatus("current")


class _Hh3cTeTunnelStaticCrlspName_Type(OctetString):
    """Custom type hh3cTeTunnelStaticCrlspName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Hh3cTeTunnelStaticCrlspName_Type.__name__ = "OctetString"
_Hh3cTeTunnelStaticCrlspName_Object = MibTableColumn
hh3cTeTunnelStaticCrlspName = _Hh3cTeTunnelStaticCrlspName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 1, 1, 2),
    _Hh3cTeTunnelStaticCrlspName_Type()
)
hh3cTeTunnelStaticCrlspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTeTunnelStaticCrlspName.setStatus("current")


class _Hh3cTeTunnelStaticCrlspStatus_Type(Integer32):
    """Custom type hh3cTeTunnelStaticCrlspStatus based on Integer32"""
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


_Hh3cTeTunnelStaticCrlspStatus_Type.__name__ = "Integer32"
_Hh3cTeTunnelStaticCrlspStatus_Object = MibTableColumn
hh3cTeTunnelStaticCrlspStatus = _Hh3cTeTunnelStaticCrlspStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 1, 1, 3),
    _Hh3cTeTunnelStaticCrlspStatus_Type()
)
hh3cTeTunnelStaticCrlspStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTeTunnelStaticCrlspStatus.setStatus("current")


class _Hh3cTeTunnelStaticCrlspRole_Type(Integer32):
    """Custom type hh3cTeTunnelStaticCrlspRole based on Integer32"""
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


_Hh3cTeTunnelStaticCrlspRole_Type.__name__ = "Integer32"
_Hh3cTeTunnelStaticCrlspRole_Object = MibTableColumn
hh3cTeTunnelStaticCrlspRole = _Hh3cTeTunnelStaticCrlspRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 1, 1, 4),
    _Hh3cTeTunnelStaticCrlspRole_Type()
)
hh3cTeTunnelStaticCrlspRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTeTunnelStaticCrlspRole.setStatus("current")
_Hh3cTeTunnelStaticCrlspXCPointer_Type = RowPointer
_Hh3cTeTunnelStaticCrlspXCPointer_Object = MibTableColumn
hh3cTeTunnelStaticCrlspXCPointer = _Hh3cTeTunnelStaticCrlspXCPointer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 1, 1, 5),
    _Hh3cTeTunnelStaticCrlspXCPointer_Type()
)
hh3cTeTunnelStaticCrlspXCPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTeTunnelStaticCrlspXCPointer.setStatus("current")
_Hh3cTeTunnelCoTable_Object = MibTable
hh3cTeTunnelCoTable = _Hh3cTeTunnelCoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cTeTunnelCoTable.setStatus("current")
_Hh3cTeTunnelCoEntry_Object = MibTableRow
hh3cTeTunnelCoEntry = _Hh3cTeTunnelCoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 2, 1)
)
hh3cTeTunnelCoEntry.setIndexNames(
    (0, "HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelCoIndex"),
    (0, "HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelCoLspInstance"),
    (0, "HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelCoIngressLSRId"),
    (0, "HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelCoEgressLSRId"),
)
if mibBuilder.loadTexts:
    hh3cTeTunnelCoEntry.setStatus("current")
_Hh3cTeTunnelCoIndex_Type = MplsTunnelIndex
_Hh3cTeTunnelCoIndex_Object = MibTableColumn
hh3cTeTunnelCoIndex = _Hh3cTeTunnelCoIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 2, 1, 1),
    _Hh3cTeTunnelCoIndex_Type()
)
hh3cTeTunnelCoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTeTunnelCoIndex.setStatus("current")
_Hh3cTeTunnelCoLspInstance_Type = MplsTunnelInstanceIndex
_Hh3cTeTunnelCoLspInstance_Object = MibTableColumn
hh3cTeTunnelCoLspInstance = _Hh3cTeTunnelCoLspInstance_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 2, 1, 2),
    _Hh3cTeTunnelCoLspInstance_Type()
)
hh3cTeTunnelCoLspInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTeTunnelCoLspInstance.setStatus("current")
_Hh3cTeTunnelCoIngressLSRId_Type = MplsExtendedTunnelId
_Hh3cTeTunnelCoIngressLSRId_Object = MibTableColumn
hh3cTeTunnelCoIngressLSRId = _Hh3cTeTunnelCoIngressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 2, 1, 3),
    _Hh3cTeTunnelCoIngressLSRId_Type()
)
hh3cTeTunnelCoIngressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTeTunnelCoIngressLSRId.setStatus("current")
_Hh3cTeTunnelCoEgressLSRId_Type = MplsExtendedTunnelId
_Hh3cTeTunnelCoEgressLSRId_Object = MibTableColumn
hh3cTeTunnelCoEgressLSRId = _Hh3cTeTunnelCoEgressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 2, 1, 4),
    _Hh3cTeTunnelCoEgressLSRId_Type()
)
hh3cTeTunnelCoEgressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTeTunnelCoEgressLSRId.setStatus("current")


class _Hh3cTeTunnelCoBiMode_Type(Integer32):
    """Custom type hh3cTeTunnelCoBiMode based on Integer32"""
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


_Hh3cTeTunnelCoBiMode_Type.__name__ = "Integer32"
_Hh3cTeTunnelCoBiMode_Object = MibTableColumn
hh3cTeTunnelCoBiMode = _Hh3cTeTunnelCoBiMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 2, 1, 5),
    _Hh3cTeTunnelCoBiMode_Type()
)
hh3cTeTunnelCoBiMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTeTunnelCoBiMode.setStatus("current")
_Hh3cTeTunnelCoReverseLspInstance_Type = MplsTunnelInstanceIndex
_Hh3cTeTunnelCoReverseLspInstance_Object = MibTableColumn
hh3cTeTunnelCoReverseLspInstance = _Hh3cTeTunnelCoReverseLspInstance_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 2, 1, 6),
    _Hh3cTeTunnelCoReverseLspInstance_Type()
)
hh3cTeTunnelCoReverseLspInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTeTunnelCoReverseLspInstance.setStatus("current")
_Hh3cTeTunnelCoReverseLspXCPointer_Type = RowPointer
_Hh3cTeTunnelCoReverseLspXCPointer_Object = MibTableColumn
hh3cTeTunnelCoReverseLspXCPointer = _Hh3cTeTunnelCoReverseLspXCPointer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 2, 1, 7),
    _Hh3cTeTunnelCoReverseLspXCPointer_Type()
)
hh3cTeTunnelCoReverseLspXCPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTeTunnelCoReverseLspXCPointer.setStatus("current")
_Hh3cTeTunnelPsTable_Object = MibTable
hh3cTeTunnelPsTable = _Hh3cTeTunnelPsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cTeTunnelPsTable.setStatus("current")
_Hh3cTeTunnelPsEntry_Object = MibTableRow
hh3cTeTunnelPsEntry = _Hh3cTeTunnelPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 3, 1)
)
hh3cTeTunnelPsEntry.setIndexNames(
    (0, "HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelPsIndex"),
    (0, "HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelPsIngressLSRId"),
    (0, "HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelPsEgressLSRId"),
)
if mibBuilder.loadTexts:
    hh3cTeTunnelPsEntry.setStatus("current")
_Hh3cTeTunnelPsIndex_Type = MplsTunnelIndex
_Hh3cTeTunnelPsIndex_Object = MibTableColumn
hh3cTeTunnelPsIndex = _Hh3cTeTunnelPsIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 3, 1, 1),
    _Hh3cTeTunnelPsIndex_Type()
)
hh3cTeTunnelPsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTeTunnelPsIndex.setStatus("current")
_Hh3cTeTunnelPsIngressLSRId_Type = MplsExtendedTunnelId
_Hh3cTeTunnelPsIngressLSRId_Object = MibTableColumn
hh3cTeTunnelPsIngressLSRId = _Hh3cTeTunnelPsIngressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 3, 1, 2),
    _Hh3cTeTunnelPsIngressLSRId_Type()
)
hh3cTeTunnelPsIngressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTeTunnelPsIngressLSRId.setStatus("current")
_Hh3cTeTunnelPsEgressLSRId_Type = MplsExtendedTunnelId
_Hh3cTeTunnelPsEgressLSRId_Object = MibTableColumn
hh3cTeTunnelPsEgressLSRId = _Hh3cTeTunnelPsEgressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 3, 1, 3),
    _Hh3cTeTunnelPsEgressLSRId_Type()
)
hh3cTeTunnelPsEgressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTeTunnelPsEgressLSRId.setStatus("current")
_Hh3cTeTunnelPsProtectIndex_Type = MplsTunnelIndex
_Hh3cTeTunnelPsProtectIndex_Object = MibTableColumn
hh3cTeTunnelPsProtectIndex = _Hh3cTeTunnelPsProtectIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 3, 1, 4),
    _Hh3cTeTunnelPsProtectIndex_Type()
)
hh3cTeTunnelPsProtectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTeTunnelPsProtectIndex.setStatus("current")
_Hh3cTeTunnelPsProtectIngressLSRId_Type = MplsExtendedTunnelId
_Hh3cTeTunnelPsProtectIngressLSRId_Object = MibTableColumn
hh3cTeTunnelPsProtectIngressLSRId = _Hh3cTeTunnelPsProtectIngressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 3, 1, 5),
    _Hh3cTeTunnelPsProtectIngressLSRId_Type()
)
hh3cTeTunnelPsProtectIngressLSRId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTeTunnelPsProtectIngressLSRId.setStatus("current")
_Hh3cTeTunnelPsProtectEgressLSRId_Type = MplsExtendedTunnelId
_Hh3cTeTunnelPsProtectEgressLSRId_Object = MibTableColumn
hh3cTeTunnelPsProtectEgressLSRId = _Hh3cTeTunnelPsProtectEgressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 3, 1, 6),
    _Hh3cTeTunnelPsProtectEgressLSRId_Type()
)
hh3cTeTunnelPsProtectEgressLSRId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTeTunnelPsProtectEgressLSRId.setStatus("current")


class _Hh3cTeTunnelPsProtectType_Type(Integer32):
    """Custom type hh3cTeTunnelPsProtectType based on Integer32"""
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


_Hh3cTeTunnelPsProtectType_Type.__name__ = "Integer32"
_Hh3cTeTunnelPsProtectType_Object = MibTableColumn
hh3cTeTunnelPsProtectType = _Hh3cTeTunnelPsProtectType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 3, 1, 7),
    _Hh3cTeTunnelPsProtectType_Type()
)
hh3cTeTunnelPsProtectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTeTunnelPsProtectType.setStatus("current")


class _Hh3cTeTunnelPsRevertiveMode_Type(Integer32):
    """Custom type hh3cTeTunnelPsRevertiveMode based on Integer32"""
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


_Hh3cTeTunnelPsRevertiveMode_Type.__name__ = "Integer32"
_Hh3cTeTunnelPsRevertiveMode_Object = MibTableColumn
hh3cTeTunnelPsRevertiveMode = _Hh3cTeTunnelPsRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 3, 1, 8),
    _Hh3cTeTunnelPsRevertiveMode_Type()
)
hh3cTeTunnelPsRevertiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTeTunnelPsRevertiveMode.setStatus("current")


class _Hh3cTeTunnelPsWtrTime_Type(Unsigned32):
    """Custom type hh3cTeTunnelPsWtrTime based on Unsigned32"""
    defaultValue = 24

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_Hh3cTeTunnelPsWtrTime_Type.__name__ = "Unsigned32"
_Hh3cTeTunnelPsWtrTime_Object = MibTableColumn
hh3cTeTunnelPsWtrTime = _Hh3cTeTunnelPsWtrTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 3, 1, 9),
    _Hh3cTeTunnelPsWtrTime_Type()
)
hh3cTeTunnelPsWtrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTeTunnelPsWtrTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cTeTunnelPsWtrTime.setUnits("30 seconds")


class _Hh3cTeTunnelPsHoldOffTime_Type(Unsigned32):
    """Custom type hh3cTeTunnelPsHoldOffTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_Hh3cTeTunnelPsHoldOffTime_Type.__name__ = "Unsigned32"
_Hh3cTeTunnelPsHoldOffTime_Object = MibTableColumn
hh3cTeTunnelPsHoldOffTime = _Hh3cTeTunnelPsHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 3, 1, 10),
    _Hh3cTeTunnelPsHoldOffTime_Type()
)
hh3cTeTunnelPsHoldOffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTeTunnelPsHoldOffTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cTeTunnelPsHoldOffTime.setUnits("500ms")


class _Hh3cTeTunnelPsSwitchMode_Type(Integer32):
    """Custom type hh3cTeTunnelPsSwitchMode based on Integer32"""
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


_Hh3cTeTunnelPsSwitchMode_Type.__name__ = "Integer32"
_Hh3cTeTunnelPsSwitchMode_Object = MibTableColumn
hh3cTeTunnelPsSwitchMode = _Hh3cTeTunnelPsSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 3, 1, 11),
    _Hh3cTeTunnelPsSwitchMode_Type()
)
hh3cTeTunnelPsSwitchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTeTunnelPsSwitchMode.setStatus("current")


class _Hh3cTeTunnelPsWorkPathStatus_Type(Integer32):
    """Custom type hh3cTeTunnelPsWorkPathStatus based on Integer32"""
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


_Hh3cTeTunnelPsWorkPathStatus_Type.__name__ = "Integer32"
_Hh3cTeTunnelPsWorkPathStatus_Object = MibTableColumn
hh3cTeTunnelPsWorkPathStatus = _Hh3cTeTunnelPsWorkPathStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 3, 1, 12),
    _Hh3cTeTunnelPsWorkPathStatus_Type()
)
hh3cTeTunnelPsWorkPathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTeTunnelPsWorkPathStatus.setStatus("current")


class _Hh3cTeTunnelPsProtectPathStatus_Type(Integer32):
    """Custom type hh3cTeTunnelPsProtectPathStatus based on Integer32"""
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


_Hh3cTeTunnelPsProtectPathStatus_Type.__name__ = "Integer32"
_Hh3cTeTunnelPsProtectPathStatus_Object = MibTableColumn
hh3cTeTunnelPsProtectPathStatus = _Hh3cTeTunnelPsProtectPathStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 3, 1, 13),
    _Hh3cTeTunnelPsProtectPathStatus_Type()
)
hh3cTeTunnelPsProtectPathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTeTunnelPsProtectPathStatus.setStatus("current")


class _Hh3cTeTunnelPsSwitchResult_Type(Integer32):
    """Custom type hh3cTeTunnelPsSwitchResult based on Integer32"""
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


_Hh3cTeTunnelPsSwitchResult_Type.__name__ = "Integer32"
_Hh3cTeTunnelPsSwitchResult_Object = MibTableColumn
hh3cTeTunnelPsSwitchResult = _Hh3cTeTunnelPsSwitchResult_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 2, 3, 1, 14),
    _Hh3cTeTunnelPsSwitchResult_Type()
)
hh3cTeTunnelPsSwitchResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTeTunnelPsSwitchResult.setStatus("current")
_Hh3cTeTunnelNotifications_ObjectIdentity = ObjectIdentity
hh3cTeTunnelNotifications = _Hh3cTeTunnelNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 3)
)
_Hh3cTeTunnelNotificationsPrefix_ObjectIdentity = ObjectIdentity
hh3cTeTunnelNotificationsPrefix = _Hh3cTeTunnelNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 3, 0)
)
_Hh3cTeTunnelConformance_ObjectIdentity = ObjectIdentity
hh3cTeTunnelConformance = _Hh3cTeTunnelConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 4)
)
_Hh3cTeTunnelCompliances_ObjectIdentity = ObjectIdentity
hh3cTeTunnelCompliances = _Hh3cTeTunnelCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 4, 1)
)
_Hh3cTeTunnelGroups_ObjectIdentity = ObjectIdentity
hh3cTeTunnelGroups = _Hh3cTeTunnelGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 4, 2)
)

# Managed Objects groups

hh3cTeTunnelScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 4, 2, 2)
)
hh3cTeTunnelScalarsGroup.setObjects(
    ("HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelMaxTunnelIndex")
)
if mibBuilder.loadTexts:
    hh3cTeTunnelScalarsGroup.setStatus("current")

hh3cTeTunnelStaticCrlspGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 4, 2, 3)
)
hh3cTeTunnelStaticCrlspGroup.setObjects(
      *(("HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelStaticCrlspName"),
        ("HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelStaticCrlspStatus"),
        ("HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelStaticCrlspRole"),
        ("HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelStaticCrlspXCPointer"))
)
if mibBuilder.loadTexts:
    hh3cTeTunnelStaticCrlspGroup.setStatus("current")

hh3cTeTunnelCorouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 4, 2, 4)
)
hh3cTeTunnelCorouteGroup.setObjects(
      *(("HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelCoBiMode"),
        ("HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelCoReverseLspInstance"),
        ("HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelCoReverseLspXCPointer"))
)
if mibBuilder.loadTexts:
    hh3cTeTunnelCorouteGroup.setStatus("current")

hh3cTeTunnelPsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 4, 2, 5)
)
hh3cTeTunnelPsGroup.setObjects(
      *(("HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelPsProtectIndex"),
        ("HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelPsProtectIngressLSRId"),
        ("HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelPsProtectEgressLSRId"),
        ("HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelPsProtectType"),
        ("HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelPsRevertiveMode"),
        ("HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelPsWtrTime"),
        ("HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelPsHoldOffTime"),
        ("HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelPsSwitchMode"),
        ("HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelPsWorkPathStatus"),
        ("HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelPsProtectPathStatus"),
        ("HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelPsSwitchResult"))
)
if mibBuilder.loadTexts:
    hh3cTeTunnelPsGroup.setStatus("current")


# Notification objects

hh3cTeTunnelPsSwitchWtoP = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 3, 0, 1)
)
hh3cTeTunnelPsSwitchWtoP.setObjects(
      *(("HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelPsWorkPathStatus"),
        ("HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelPsProtectPathStatus"))
)
if mibBuilder.loadTexts:
    hh3cTeTunnelPsSwitchWtoP.setStatus(
        "current"
    )

hh3cTeTunnelPsSwitchPtoW = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 3, 0, 2)
)
hh3cTeTunnelPsSwitchPtoW.setObjects(
      *(("HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelPsWorkPathStatus"),
        ("HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelPsProtectPathStatus"))
)
if mibBuilder.loadTexts:
    hh3cTeTunnelPsSwitchPtoW.setStatus(
        "current"
    )


# Notifications groups

hh3cTeTunnelNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 4, 2, 1)
)
hh3cTeTunnelNotificationsGroup.setObjects(
      *(("HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelPsSwitchPtoW"),
        ("HH3C-TE-TUNNEL-MIB", "hh3cTeTunnelPsSwitchWtoP"))
)
if mibBuilder.loadTexts:
    hh3cTeTunnelNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hh3cTeTunnelCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cTeTunnelCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-TE-TUNNEL-MIB",
    **{"hh3cTeTunnel": hh3cTeTunnel,
       "hh3cTeTunnelScalars": hh3cTeTunnelScalars,
       "hh3cTeTunnelMaxTunnelIndex": hh3cTeTunnelMaxTunnelIndex,
       "hh3cTeTunnelObjects": hh3cTeTunnelObjects,
       "hh3cTeTunnelStaticCrlspTable": hh3cTeTunnelStaticCrlspTable,
       "hh3cTeTunnelStaticCrlspEntry": hh3cTeTunnelStaticCrlspEntry,
       "hh3cTeTunnelStaticCrlspInLabel": hh3cTeTunnelStaticCrlspInLabel,
       "hh3cTeTunnelStaticCrlspName": hh3cTeTunnelStaticCrlspName,
       "hh3cTeTunnelStaticCrlspStatus": hh3cTeTunnelStaticCrlspStatus,
       "hh3cTeTunnelStaticCrlspRole": hh3cTeTunnelStaticCrlspRole,
       "hh3cTeTunnelStaticCrlspXCPointer": hh3cTeTunnelStaticCrlspXCPointer,
       "hh3cTeTunnelCoTable": hh3cTeTunnelCoTable,
       "hh3cTeTunnelCoEntry": hh3cTeTunnelCoEntry,
       "hh3cTeTunnelCoIndex": hh3cTeTunnelCoIndex,
       "hh3cTeTunnelCoLspInstance": hh3cTeTunnelCoLspInstance,
       "hh3cTeTunnelCoIngressLSRId": hh3cTeTunnelCoIngressLSRId,
       "hh3cTeTunnelCoEgressLSRId": hh3cTeTunnelCoEgressLSRId,
       "hh3cTeTunnelCoBiMode": hh3cTeTunnelCoBiMode,
       "hh3cTeTunnelCoReverseLspInstance": hh3cTeTunnelCoReverseLspInstance,
       "hh3cTeTunnelCoReverseLspXCPointer": hh3cTeTunnelCoReverseLspXCPointer,
       "hh3cTeTunnelPsTable": hh3cTeTunnelPsTable,
       "hh3cTeTunnelPsEntry": hh3cTeTunnelPsEntry,
       "hh3cTeTunnelPsIndex": hh3cTeTunnelPsIndex,
       "hh3cTeTunnelPsIngressLSRId": hh3cTeTunnelPsIngressLSRId,
       "hh3cTeTunnelPsEgressLSRId": hh3cTeTunnelPsEgressLSRId,
       "hh3cTeTunnelPsProtectIndex": hh3cTeTunnelPsProtectIndex,
       "hh3cTeTunnelPsProtectIngressLSRId": hh3cTeTunnelPsProtectIngressLSRId,
       "hh3cTeTunnelPsProtectEgressLSRId": hh3cTeTunnelPsProtectEgressLSRId,
       "hh3cTeTunnelPsProtectType": hh3cTeTunnelPsProtectType,
       "hh3cTeTunnelPsRevertiveMode": hh3cTeTunnelPsRevertiveMode,
       "hh3cTeTunnelPsWtrTime": hh3cTeTunnelPsWtrTime,
       "hh3cTeTunnelPsHoldOffTime": hh3cTeTunnelPsHoldOffTime,
       "hh3cTeTunnelPsSwitchMode": hh3cTeTunnelPsSwitchMode,
       "hh3cTeTunnelPsWorkPathStatus": hh3cTeTunnelPsWorkPathStatus,
       "hh3cTeTunnelPsProtectPathStatus": hh3cTeTunnelPsProtectPathStatus,
       "hh3cTeTunnelPsSwitchResult": hh3cTeTunnelPsSwitchResult,
       "hh3cTeTunnelNotifications": hh3cTeTunnelNotifications,
       "hh3cTeTunnelNotificationsPrefix": hh3cTeTunnelNotificationsPrefix,
       "hh3cTeTunnelPsSwitchWtoP": hh3cTeTunnelPsSwitchWtoP,
       "hh3cTeTunnelPsSwitchPtoW": hh3cTeTunnelPsSwitchPtoW,
       "hh3cTeTunnelConformance": hh3cTeTunnelConformance,
       "hh3cTeTunnelCompliances": hh3cTeTunnelCompliances,
       "hh3cTeTunnelCompliance": hh3cTeTunnelCompliance,
       "hh3cTeTunnelGroups": hh3cTeTunnelGroups,
       "hh3cTeTunnelNotificationsGroup": hh3cTeTunnelNotificationsGroup,
       "hh3cTeTunnelScalarsGroup": hh3cTeTunnelScalarsGroup,
       "hh3cTeTunnelStaticCrlspGroup": hh3cTeTunnelStaticCrlspGroup,
       "hh3cTeTunnelCorouteGroup": hh3cTeTunnelCorouteGroup,
       "hh3cTeTunnelPsGroup": hh3cTeTunnelPsGroup}
)
