# SNMP MIB module (H3C-TE-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-TE-TUNNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:32 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

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

h3cTeTunnel = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cTeTunnelScalars_ObjectIdentity = ObjectIdentity
h3cTeTunnelScalars = _H3cTeTunnelScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 1)
)
_H3cTeTunnelMaxTunnelIndex_Type = MplsTunnelIndex
_H3cTeTunnelMaxTunnelIndex_Object = MibScalar
h3cTeTunnelMaxTunnelIndex = _H3cTeTunnelMaxTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 1, 1),
    _H3cTeTunnelMaxTunnelIndex_Type()
)
h3cTeTunnelMaxTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTeTunnelMaxTunnelIndex.setStatus("current")
_H3cTeTunnelObjects_ObjectIdentity = ObjectIdentity
h3cTeTunnelObjects = _H3cTeTunnelObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2)
)
_H3cTeTunnelStaticCrlspTable_Object = MibTable
h3cTeTunnelStaticCrlspTable = _H3cTeTunnelStaticCrlspTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 1)
)
if mibBuilder.loadTexts:
    h3cTeTunnelStaticCrlspTable.setStatus("current")
_H3cTeTunnelStaticCrlspEntry_Object = MibTableRow
h3cTeTunnelStaticCrlspEntry = _H3cTeTunnelStaticCrlspEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 1, 1)
)
h3cTeTunnelStaticCrlspEntry.setIndexNames(
    (0, "H3C-TE-TUNNEL-MIB", "h3cTeTunnelStaticCrlspInLabel"),
)
if mibBuilder.loadTexts:
    h3cTeTunnelStaticCrlspEntry.setStatus("current")
_H3cTeTunnelStaticCrlspInLabel_Type = MplsLabel
_H3cTeTunnelStaticCrlspInLabel_Object = MibTableColumn
h3cTeTunnelStaticCrlspInLabel = _H3cTeTunnelStaticCrlspInLabel_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 1, 1, 1),
    _H3cTeTunnelStaticCrlspInLabel_Type()
)
h3cTeTunnelStaticCrlspInLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTeTunnelStaticCrlspInLabel.setStatus("current")


class _H3cTeTunnelStaticCrlspName_Type(OctetString):
    """Custom type h3cTeTunnelStaticCrlspName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_H3cTeTunnelStaticCrlspName_Type.__name__ = "OctetString"
_H3cTeTunnelStaticCrlspName_Object = MibTableColumn
h3cTeTunnelStaticCrlspName = _H3cTeTunnelStaticCrlspName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 1, 1, 2),
    _H3cTeTunnelStaticCrlspName_Type()
)
h3cTeTunnelStaticCrlspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTeTunnelStaticCrlspName.setStatus("current")


class _H3cTeTunnelStaticCrlspStatus_Type(Integer32):
    """Custom type h3cTeTunnelStaticCrlspStatus based on Integer32"""
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


_H3cTeTunnelStaticCrlspStatus_Type.__name__ = "Integer32"
_H3cTeTunnelStaticCrlspStatus_Object = MibTableColumn
h3cTeTunnelStaticCrlspStatus = _H3cTeTunnelStaticCrlspStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 1, 1, 3),
    _H3cTeTunnelStaticCrlspStatus_Type()
)
h3cTeTunnelStaticCrlspStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTeTunnelStaticCrlspStatus.setStatus("current")


class _H3cTeTunnelStaticCrlspRole_Type(Integer32):
    """Custom type h3cTeTunnelStaticCrlspRole based on Integer32"""
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


_H3cTeTunnelStaticCrlspRole_Type.__name__ = "Integer32"
_H3cTeTunnelStaticCrlspRole_Object = MibTableColumn
h3cTeTunnelStaticCrlspRole = _H3cTeTunnelStaticCrlspRole_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 1, 1, 4),
    _H3cTeTunnelStaticCrlspRole_Type()
)
h3cTeTunnelStaticCrlspRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTeTunnelStaticCrlspRole.setStatus("current")
_H3cTeTunnelStaticCrlspXCPointer_Type = RowPointer
_H3cTeTunnelStaticCrlspXCPointer_Object = MibTableColumn
h3cTeTunnelStaticCrlspXCPointer = _H3cTeTunnelStaticCrlspXCPointer_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 1, 1, 5),
    _H3cTeTunnelStaticCrlspXCPointer_Type()
)
h3cTeTunnelStaticCrlspXCPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTeTunnelStaticCrlspXCPointer.setStatus("current")
_H3cTeTunnelCoTable_Object = MibTable
h3cTeTunnelCoTable = _H3cTeTunnelCoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 2)
)
if mibBuilder.loadTexts:
    h3cTeTunnelCoTable.setStatus("current")
_H3cTeTunnelCoEntry_Object = MibTableRow
h3cTeTunnelCoEntry = _H3cTeTunnelCoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 2, 1)
)
h3cTeTunnelCoEntry.setIndexNames(
    (0, "H3C-TE-TUNNEL-MIB", "h3cTeTunnelCoIndex"),
    (0, "H3C-TE-TUNNEL-MIB", "h3cTeTunnelCoLspInstance"),
    (0, "H3C-TE-TUNNEL-MIB", "h3cTeTunnelCoIngressLSRId"),
    (0, "H3C-TE-TUNNEL-MIB", "h3cTeTunnelCoEgressLSRId"),
)
if mibBuilder.loadTexts:
    h3cTeTunnelCoEntry.setStatus("current")
_H3cTeTunnelCoIndex_Type = MplsTunnelIndex
_H3cTeTunnelCoIndex_Object = MibTableColumn
h3cTeTunnelCoIndex = _H3cTeTunnelCoIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 2, 1, 1),
    _H3cTeTunnelCoIndex_Type()
)
h3cTeTunnelCoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTeTunnelCoIndex.setStatus("current")
_H3cTeTunnelCoLspInstance_Type = MplsTunnelInstanceIndex
_H3cTeTunnelCoLspInstance_Object = MibTableColumn
h3cTeTunnelCoLspInstance = _H3cTeTunnelCoLspInstance_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 2, 1, 2),
    _H3cTeTunnelCoLspInstance_Type()
)
h3cTeTunnelCoLspInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTeTunnelCoLspInstance.setStatus("current")
_H3cTeTunnelCoIngressLSRId_Type = MplsExtendedTunnelId
_H3cTeTunnelCoIngressLSRId_Object = MibTableColumn
h3cTeTunnelCoIngressLSRId = _H3cTeTunnelCoIngressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 2, 1, 3),
    _H3cTeTunnelCoIngressLSRId_Type()
)
h3cTeTunnelCoIngressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTeTunnelCoIngressLSRId.setStatus("current")
_H3cTeTunnelCoEgressLSRId_Type = MplsExtendedTunnelId
_H3cTeTunnelCoEgressLSRId_Object = MibTableColumn
h3cTeTunnelCoEgressLSRId = _H3cTeTunnelCoEgressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 2, 1, 4),
    _H3cTeTunnelCoEgressLSRId_Type()
)
h3cTeTunnelCoEgressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTeTunnelCoEgressLSRId.setStatus("current")


class _H3cTeTunnelCoBiMode_Type(Integer32):
    """Custom type h3cTeTunnelCoBiMode based on Integer32"""
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


_H3cTeTunnelCoBiMode_Type.__name__ = "Integer32"
_H3cTeTunnelCoBiMode_Object = MibTableColumn
h3cTeTunnelCoBiMode = _H3cTeTunnelCoBiMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 2, 1, 5),
    _H3cTeTunnelCoBiMode_Type()
)
h3cTeTunnelCoBiMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTeTunnelCoBiMode.setStatus("current")
_H3cTeTunnelCoReverseLspInstance_Type = MplsTunnelInstanceIndex
_H3cTeTunnelCoReverseLspInstance_Object = MibTableColumn
h3cTeTunnelCoReverseLspInstance = _H3cTeTunnelCoReverseLspInstance_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 2, 1, 6),
    _H3cTeTunnelCoReverseLspInstance_Type()
)
h3cTeTunnelCoReverseLspInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTeTunnelCoReverseLspInstance.setStatus("current")
_H3cTeTunnelCoReverseLspXCPointer_Type = RowPointer
_H3cTeTunnelCoReverseLspXCPointer_Object = MibTableColumn
h3cTeTunnelCoReverseLspXCPointer = _H3cTeTunnelCoReverseLspXCPointer_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 2, 1, 7),
    _H3cTeTunnelCoReverseLspXCPointer_Type()
)
h3cTeTunnelCoReverseLspXCPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTeTunnelCoReverseLspXCPointer.setStatus("current")
_H3cTeTunnelPsTable_Object = MibTable
h3cTeTunnelPsTable = _H3cTeTunnelPsTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3)
)
if mibBuilder.loadTexts:
    h3cTeTunnelPsTable.setStatus("current")
_H3cTeTunnelPsEntry_Object = MibTableRow
h3cTeTunnelPsEntry = _H3cTeTunnelPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1)
)
h3cTeTunnelPsEntry.setIndexNames(
    (0, "H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsIndex"),
    (0, "H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsIngressLSRId"),
    (0, "H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsEgressLSRId"),
)
if mibBuilder.loadTexts:
    h3cTeTunnelPsEntry.setStatus("current")
_H3cTeTunnelPsIndex_Type = MplsTunnelIndex
_H3cTeTunnelPsIndex_Object = MibTableColumn
h3cTeTunnelPsIndex = _H3cTeTunnelPsIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 1),
    _H3cTeTunnelPsIndex_Type()
)
h3cTeTunnelPsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTeTunnelPsIndex.setStatus("current")
_H3cTeTunnelPsIngressLSRId_Type = MplsExtendedTunnelId
_H3cTeTunnelPsIngressLSRId_Object = MibTableColumn
h3cTeTunnelPsIngressLSRId = _H3cTeTunnelPsIngressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 2),
    _H3cTeTunnelPsIngressLSRId_Type()
)
h3cTeTunnelPsIngressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTeTunnelPsIngressLSRId.setStatus("current")
_H3cTeTunnelPsEgressLSRId_Type = MplsExtendedTunnelId
_H3cTeTunnelPsEgressLSRId_Object = MibTableColumn
h3cTeTunnelPsEgressLSRId = _H3cTeTunnelPsEgressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 3),
    _H3cTeTunnelPsEgressLSRId_Type()
)
h3cTeTunnelPsEgressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTeTunnelPsEgressLSRId.setStatus("current")
_H3cTeTunnelPsProtectIndex_Type = MplsTunnelIndex
_H3cTeTunnelPsProtectIndex_Object = MibTableColumn
h3cTeTunnelPsProtectIndex = _H3cTeTunnelPsProtectIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 4),
    _H3cTeTunnelPsProtectIndex_Type()
)
h3cTeTunnelPsProtectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTeTunnelPsProtectIndex.setStatus("current")
_H3cTeTunnelPsProtectIngressLSRId_Type = MplsExtendedTunnelId
_H3cTeTunnelPsProtectIngressLSRId_Object = MibTableColumn
h3cTeTunnelPsProtectIngressLSRId = _H3cTeTunnelPsProtectIngressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 5),
    _H3cTeTunnelPsProtectIngressLSRId_Type()
)
h3cTeTunnelPsProtectIngressLSRId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTeTunnelPsProtectIngressLSRId.setStatus("current")
_H3cTeTunnelPsProtectEgressLSRId_Type = MplsExtendedTunnelId
_H3cTeTunnelPsProtectEgressLSRId_Object = MibTableColumn
h3cTeTunnelPsProtectEgressLSRId = _H3cTeTunnelPsProtectEgressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 6),
    _H3cTeTunnelPsProtectEgressLSRId_Type()
)
h3cTeTunnelPsProtectEgressLSRId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTeTunnelPsProtectEgressLSRId.setStatus("current")


class _H3cTeTunnelPsProtectType_Type(Integer32):
    """Custom type h3cTeTunnelPsProtectType based on Integer32"""
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


_H3cTeTunnelPsProtectType_Type.__name__ = "Integer32"
_H3cTeTunnelPsProtectType_Object = MibTableColumn
h3cTeTunnelPsProtectType = _H3cTeTunnelPsProtectType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 7),
    _H3cTeTunnelPsProtectType_Type()
)
h3cTeTunnelPsProtectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTeTunnelPsProtectType.setStatus("current")


class _H3cTeTunnelPsRevertiveMode_Type(Integer32):
    """Custom type h3cTeTunnelPsRevertiveMode based on Integer32"""
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


_H3cTeTunnelPsRevertiveMode_Type.__name__ = "Integer32"
_H3cTeTunnelPsRevertiveMode_Object = MibTableColumn
h3cTeTunnelPsRevertiveMode = _H3cTeTunnelPsRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 8),
    _H3cTeTunnelPsRevertiveMode_Type()
)
h3cTeTunnelPsRevertiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTeTunnelPsRevertiveMode.setStatus("current")


class _H3cTeTunnelPsWtrTime_Type(Unsigned32):
    """Custom type h3cTeTunnelPsWtrTime based on Unsigned32"""
    defaultValue = 24

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_H3cTeTunnelPsWtrTime_Type.__name__ = "Unsigned32"
_H3cTeTunnelPsWtrTime_Object = MibTableColumn
h3cTeTunnelPsWtrTime = _H3cTeTunnelPsWtrTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 9),
    _H3cTeTunnelPsWtrTime_Type()
)
h3cTeTunnelPsWtrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTeTunnelPsWtrTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cTeTunnelPsWtrTime.setUnits("30 seconds")


class _H3cTeTunnelPsHoldOffTime_Type(Unsigned32):
    """Custom type h3cTeTunnelPsHoldOffTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_H3cTeTunnelPsHoldOffTime_Type.__name__ = "Unsigned32"
_H3cTeTunnelPsHoldOffTime_Object = MibTableColumn
h3cTeTunnelPsHoldOffTime = _H3cTeTunnelPsHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 10),
    _H3cTeTunnelPsHoldOffTime_Type()
)
h3cTeTunnelPsHoldOffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTeTunnelPsHoldOffTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cTeTunnelPsHoldOffTime.setUnits("500ms")


class _H3cTeTunnelPsSwitchMode_Type(Integer32):
    """Custom type h3cTeTunnelPsSwitchMode based on Integer32"""
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


_H3cTeTunnelPsSwitchMode_Type.__name__ = "Integer32"
_H3cTeTunnelPsSwitchMode_Object = MibTableColumn
h3cTeTunnelPsSwitchMode = _H3cTeTunnelPsSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 11),
    _H3cTeTunnelPsSwitchMode_Type()
)
h3cTeTunnelPsSwitchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTeTunnelPsSwitchMode.setStatus("current")


class _H3cTeTunnelPsWorkPathStatus_Type(Integer32):
    """Custom type h3cTeTunnelPsWorkPathStatus based on Integer32"""
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


_H3cTeTunnelPsWorkPathStatus_Type.__name__ = "Integer32"
_H3cTeTunnelPsWorkPathStatus_Object = MibTableColumn
h3cTeTunnelPsWorkPathStatus = _H3cTeTunnelPsWorkPathStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 12),
    _H3cTeTunnelPsWorkPathStatus_Type()
)
h3cTeTunnelPsWorkPathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTeTunnelPsWorkPathStatus.setStatus("current")


class _H3cTeTunnelPsProtectPathStatus_Type(Integer32):
    """Custom type h3cTeTunnelPsProtectPathStatus based on Integer32"""
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


_H3cTeTunnelPsProtectPathStatus_Type.__name__ = "Integer32"
_H3cTeTunnelPsProtectPathStatus_Object = MibTableColumn
h3cTeTunnelPsProtectPathStatus = _H3cTeTunnelPsProtectPathStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 13),
    _H3cTeTunnelPsProtectPathStatus_Type()
)
h3cTeTunnelPsProtectPathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTeTunnelPsProtectPathStatus.setStatus("current")


class _H3cTeTunnelPsSwitchResult_Type(Integer32):
    """Custom type h3cTeTunnelPsSwitchResult based on Integer32"""
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


_H3cTeTunnelPsSwitchResult_Type.__name__ = "Integer32"
_H3cTeTunnelPsSwitchResult_Object = MibTableColumn
h3cTeTunnelPsSwitchResult = _H3cTeTunnelPsSwitchResult_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 14),
    _H3cTeTunnelPsSwitchResult_Type()
)
h3cTeTunnelPsSwitchResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTeTunnelPsSwitchResult.setStatus("current")
_H3cTeTunnelNotifications_ObjectIdentity = ObjectIdentity
h3cTeTunnelNotifications = _H3cTeTunnelNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 3)
)
_H3cTeTunnelNotificationsPrefix_ObjectIdentity = ObjectIdentity
h3cTeTunnelNotificationsPrefix = _H3cTeTunnelNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 3, 0)
)
_H3cTeTunnelConformance_ObjectIdentity = ObjectIdentity
h3cTeTunnelConformance = _H3cTeTunnelConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 4)
)
_H3cTeTunnelCompliances_ObjectIdentity = ObjectIdentity
h3cTeTunnelCompliances = _H3cTeTunnelCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 4, 1)
)
_H3cTeTunnelGroups_ObjectIdentity = ObjectIdentity
h3cTeTunnelGroups = _H3cTeTunnelGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 4, 2)
)

# Managed Objects groups

h3cTeTunnelScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 4, 2, 2)
)
h3cTeTunnelScalarsGroup.setObjects(
    ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelMaxTunnelIndex")
)
if mibBuilder.loadTexts:
    h3cTeTunnelScalarsGroup.setStatus("current")

h3cTeTunnelStaticCrlspGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 4, 2, 3)
)
h3cTeTunnelStaticCrlspGroup.setObjects(
      *(("H3C-TE-TUNNEL-MIB", "h3cTeTunnelStaticCrlspName"),
        ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelStaticCrlspStatus"),
        ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelStaticCrlspRole"),
        ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelStaticCrlspXCPointer"))
)
if mibBuilder.loadTexts:
    h3cTeTunnelStaticCrlspGroup.setStatus("current")

h3cTeTunnelCorouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 4, 2, 4)
)
h3cTeTunnelCorouteGroup.setObjects(
      *(("H3C-TE-TUNNEL-MIB", "h3cTeTunnelCoBiMode"),
        ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelCoReverseLspInstance"),
        ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelCoReverseLspXCPointer"))
)
if mibBuilder.loadTexts:
    h3cTeTunnelCorouteGroup.setStatus("current")

h3cTeTunnelPsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 4, 2, 5)
)
h3cTeTunnelPsGroup.setObjects(
      *(("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsProtectIndex"),
        ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsProtectIngressLSRId"),
        ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsProtectEgressLSRId"),
        ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsProtectType"),
        ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsRevertiveMode"),
        ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsWtrTime"),
        ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsHoldOffTime"),
        ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsSwitchMode"),
        ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsWorkPathStatus"),
        ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsProtectPathStatus"),
        ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsSwitchResult"))
)
if mibBuilder.loadTexts:
    h3cTeTunnelPsGroup.setStatus("current")


# Notification objects

h3cTeTunnelPsSwitchWtoP = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 3, 0, 1)
)
h3cTeTunnelPsSwitchWtoP.setObjects(
      *(("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsWorkPathStatus"),
        ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsProtectPathStatus"))
)
if mibBuilder.loadTexts:
    h3cTeTunnelPsSwitchWtoP.setStatus(
        "current"
    )

h3cTeTunnelPsSwitchPtoW = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 3, 0, 2)
)
h3cTeTunnelPsSwitchPtoW.setObjects(
      *(("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsWorkPathStatus"),
        ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsProtectPathStatus"))
)
if mibBuilder.loadTexts:
    h3cTeTunnelPsSwitchPtoW.setStatus(
        "current"
    )


# Notifications groups

h3cTeTunnelNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 4, 2, 1)
)
h3cTeTunnelNotificationsGroup.setObjects(
      *(("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsSwitchPtoW"),
        ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsSwitchWtoP"))
)
if mibBuilder.loadTexts:
    h3cTeTunnelNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

h3cTeTunnelCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 4, 1, 1)
)
if mibBuilder.loadTexts:
    h3cTeTunnelCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-TE-TUNNEL-MIB",
    **{"h3cTeTunnel": h3cTeTunnel,
       "h3cTeTunnelScalars": h3cTeTunnelScalars,
       "h3cTeTunnelMaxTunnelIndex": h3cTeTunnelMaxTunnelIndex,
       "h3cTeTunnelObjects": h3cTeTunnelObjects,
       "h3cTeTunnelStaticCrlspTable": h3cTeTunnelStaticCrlspTable,
       "h3cTeTunnelStaticCrlspEntry": h3cTeTunnelStaticCrlspEntry,
       "h3cTeTunnelStaticCrlspInLabel": h3cTeTunnelStaticCrlspInLabel,
       "h3cTeTunnelStaticCrlspName": h3cTeTunnelStaticCrlspName,
       "h3cTeTunnelStaticCrlspStatus": h3cTeTunnelStaticCrlspStatus,
       "h3cTeTunnelStaticCrlspRole": h3cTeTunnelStaticCrlspRole,
       "h3cTeTunnelStaticCrlspXCPointer": h3cTeTunnelStaticCrlspXCPointer,
       "h3cTeTunnelCoTable": h3cTeTunnelCoTable,
       "h3cTeTunnelCoEntry": h3cTeTunnelCoEntry,
       "h3cTeTunnelCoIndex": h3cTeTunnelCoIndex,
       "h3cTeTunnelCoLspInstance": h3cTeTunnelCoLspInstance,
       "h3cTeTunnelCoIngressLSRId": h3cTeTunnelCoIngressLSRId,
       "h3cTeTunnelCoEgressLSRId": h3cTeTunnelCoEgressLSRId,
       "h3cTeTunnelCoBiMode": h3cTeTunnelCoBiMode,
       "h3cTeTunnelCoReverseLspInstance": h3cTeTunnelCoReverseLspInstance,
       "h3cTeTunnelCoReverseLspXCPointer": h3cTeTunnelCoReverseLspXCPointer,
       "h3cTeTunnelPsTable": h3cTeTunnelPsTable,
       "h3cTeTunnelPsEntry": h3cTeTunnelPsEntry,
       "h3cTeTunnelPsIndex": h3cTeTunnelPsIndex,
       "h3cTeTunnelPsIngressLSRId": h3cTeTunnelPsIngressLSRId,
       "h3cTeTunnelPsEgressLSRId": h3cTeTunnelPsEgressLSRId,
       "h3cTeTunnelPsProtectIndex": h3cTeTunnelPsProtectIndex,
       "h3cTeTunnelPsProtectIngressLSRId": h3cTeTunnelPsProtectIngressLSRId,
       "h3cTeTunnelPsProtectEgressLSRId": h3cTeTunnelPsProtectEgressLSRId,
       "h3cTeTunnelPsProtectType": h3cTeTunnelPsProtectType,
       "h3cTeTunnelPsRevertiveMode": h3cTeTunnelPsRevertiveMode,
       "h3cTeTunnelPsWtrTime": h3cTeTunnelPsWtrTime,
       "h3cTeTunnelPsHoldOffTime": h3cTeTunnelPsHoldOffTime,
       "h3cTeTunnelPsSwitchMode": h3cTeTunnelPsSwitchMode,
       "h3cTeTunnelPsWorkPathStatus": h3cTeTunnelPsWorkPathStatus,
       "h3cTeTunnelPsProtectPathStatus": h3cTeTunnelPsProtectPathStatus,
       "h3cTeTunnelPsSwitchResult": h3cTeTunnelPsSwitchResult,
       "h3cTeTunnelNotifications": h3cTeTunnelNotifications,
       "h3cTeTunnelNotificationsPrefix": h3cTeTunnelNotificationsPrefix,
       "h3cTeTunnelPsSwitchWtoP": h3cTeTunnelPsSwitchWtoP,
       "h3cTeTunnelPsSwitchPtoW": h3cTeTunnelPsSwitchPtoW,
       "h3cTeTunnelConformance": h3cTeTunnelConformance,
       "h3cTeTunnelCompliances": h3cTeTunnelCompliances,
       "h3cTeTunnelCompliance": h3cTeTunnelCompliance,
       "h3cTeTunnelGroups": h3cTeTunnelGroups,
       "h3cTeTunnelNotificationsGroup": h3cTeTunnelNotificationsGroup,
       "h3cTeTunnelScalarsGroup": h3cTeTunnelScalarsGroup,
       "h3cTeTunnelStaticCrlspGroup": h3cTeTunnelStaticCrlspGroup,
       "h3cTeTunnelCorouteGroup": h3cTeTunnelCorouteGroup,
       "h3cTeTunnelPsGroup": h3cTeTunnelPsGroup}
)
