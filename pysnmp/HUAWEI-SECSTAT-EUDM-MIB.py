# SNMP MIB module (HUAWEI-SECSTAT-EUDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-SECSTAT-EUDM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:50 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(mplsVpnVrfName,) = mibBuilder.importSymbols(
    "MPLS-VPN-MIB",
    "mplsVpnVrfName")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwSECSTATEudm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwSECSTAT_ObjectIdentity = ObjectIdentity
hwSECSTAT = _HwSECSTAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11)
)
_HwSecStatEudmCfgObjects_ObjectIdentity = ObjectIdentity
hwSecStatEudmCfgObjects = _HwSecStatEudmCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1)
)
_HwSecStatEudmSessCfgTable_Object = MibTable
hwSecStatEudmSessCfgTable = _HwSecStatEudmSessCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwSecStatEudmSessCfgTable.setStatus("current")
_HwSecStatEudmSessCfgEntry_Object = MibTableRow
hwSecStatEudmSessCfgEntry = _HwSecStatEudmSessCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1)
)
hwSecStatEudmSessCfgEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessCfgZoneID"),
)
if mibBuilder.loadTexts:
    hwSecStatEudmSessCfgEntry.setStatus("current")


class _HwSecStatEudmSessCfgZoneID_Type(Integer32):
    """Custom type hwSecStatEudmSessCfgZoneID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwSecStatEudmSessCfgZoneID_Type.__name__ = "Integer32"
_HwSecStatEudmSessCfgZoneID_Object = MibTableColumn
hwSecStatEudmSessCfgZoneID = _HwSecStatEudmSessCfgZoneID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 1),
    _HwSecStatEudmSessCfgZoneID_Type()
)
hwSecStatEudmSessCfgZoneID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSecStatEudmSessCfgZoneID.setStatus("current")


class _HwSecStatEudmSessTcpInZoneNumMax_Type(Integer32):
    """Custom type hwSecStatEudmSessTcpInZoneNumMax based on Integer32"""
    defaultValue = 500000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500000),
    )


_HwSecStatEudmSessTcpInZoneNumMax_Type.__name__ = "Integer32"
_HwSecStatEudmSessTcpInZoneNumMax_Object = MibTableColumn
hwSecStatEudmSessTcpInZoneNumMax = _HwSecStatEudmSessTcpInZoneNumMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 2),
    _HwSecStatEudmSessTcpInZoneNumMax_Type()
)
hwSecStatEudmSessTcpInZoneNumMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSecStatEudmSessTcpInZoneNumMax.setStatus("current")


class _HwSecStatEudmSessTcpInZoneNumMin_Type(Integer32):
    """Custom type hwSecStatEudmSessTcpInZoneNumMin based on Integer32"""
    defaultValue = 500000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500000),
    )


_HwSecStatEudmSessTcpInZoneNumMin_Type.__name__ = "Integer32"
_HwSecStatEudmSessTcpInZoneNumMin_Object = MibTableColumn
hwSecStatEudmSessTcpInZoneNumMin = _HwSecStatEudmSessTcpInZoneNumMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 3),
    _HwSecStatEudmSessTcpInZoneNumMin_Type()
)
hwSecStatEudmSessTcpInZoneNumMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessTcpInZoneNumMin.setStatus("current")
_HwSecStatEudmSessTcpInIPNumMax_Type = Integer32
_HwSecStatEudmSessTcpInIPNumMax_Object = MibTableColumn
hwSecStatEudmSessTcpInIPNumMax = _HwSecStatEudmSessTcpInIPNumMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 4),
    _HwSecStatEudmSessTcpInIPNumMax_Type()
)
hwSecStatEudmSessTcpInIPNumMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessTcpInIPNumMax.setStatus("current")
_HwSecStatEudmSessTcpInIPNumMin_Type = Integer32
_HwSecStatEudmSessTcpInIPNumMin_Object = MibTableColumn
hwSecStatEudmSessTcpInIPNumMin = _HwSecStatEudmSessTcpInIPNumMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 5),
    _HwSecStatEudmSessTcpInIPNumMin_Type()
)
hwSecStatEudmSessTcpInIPNumMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessTcpInIPNumMin.setStatus("current")


class _HwSecStatEudmSessTcpOutZoneNumMax_Type(Integer32):
    """Custom type hwSecStatEudmSessTcpOutZoneNumMax based on Integer32"""
    defaultValue = 500000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500000),
    )


_HwSecStatEudmSessTcpOutZoneNumMax_Type.__name__ = "Integer32"
_HwSecStatEudmSessTcpOutZoneNumMax_Object = MibTableColumn
hwSecStatEudmSessTcpOutZoneNumMax = _HwSecStatEudmSessTcpOutZoneNumMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 6),
    _HwSecStatEudmSessTcpOutZoneNumMax_Type()
)
hwSecStatEudmSessTcpOutZoneNumMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessTcpOutZoneNumMax.setStatus("current")


class _HwSecStatEudmSessTcpOutZoneNumMin_Type(Integer32):
    """Custom type hwSecStatEudmSessTcpOutZoneNumMin based on Integer32"""
    defaultValue = 500000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500000),
    )


_HwSecStatEudmSessTcpOutZoneNumMin_Type.__name__ = "Integer32"
_HwSecStatEudmSessTcpOutZoneNumMin_Object = MibTableColumn
hwSecStatEudmSessTcpOutZoneNumMin = _HwSecStatEudmSessTcpOutZoneNumMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 7),
    _HwSecStatEudmSessTcpOutZoneNumMin_Type()
)
hwSecStatEudmSessTcpOutZoneNumMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessTcpOutZoneNumMin.setStatus("current")
_HwSecStatEudmSessTcpOutIPNumMax_Type = Integer32
_HwSecStatEudmSessTcpOutIPNumMax_Object = MibTableColumn
hwSecStatEudmSessTcpOutIPNumMax = _HwSecStatEudmSessTcpOutIPNumMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 8),
    _HwSecStatEudmSessTcpOutIPNumMax_Type()
)
hwSecStatEudmSessTcpOutIPNumMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessTcpOutIPNumMax.setStatus("current")
_HwSecStatEudmSessTcpOutIPNumMin_Type = Integer32
_HwSecStatEudmSessTcpOutIPNumMin_Object = MibTableColumn
hwSecStatEudmSessTcpOutIPNumMin = _HwSecStatEudmSessTcpOutIPNumMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 9),
    _HwSecStatEudmSessTcpOutIPNumMin_Type()
)
hwSecStatEudmSessTcpOutIPNumMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessTcpOutIPNumMin.setStatus("current")


class _HwSecStatEudmSessUdpInZoneNumMax_Type(Integer32):
    """Custom type hwSecStatEudmSessUdpInZoneNumMax based on Integer32"""
    defaultValue = 500000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500000),
    )


_HwSecStatEudmSessUdpInZoneNumMax_Type.__name__ = "Integer32"
_HwSecStatEudmSessUdpInZoneNumMax_Object = MibTableColumn
hwSecStatEudmSessUdpInZoneNumMax = _HwSecStatEudmSessUdpInZoneNumMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 10),
    _HwSecStatEudmSessUdpInZoneNumMax_Type()
)
hwSecStatEudmSessUdpInZoneNumMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessUdpInZoneNumMax.setStatus("current")


class _HwSecStatEudmSessUdpInZoneNumMin_Type(Integer32):
    """Custom type hwSecStatEudmSessUdpInZoneNumMin based on Integer32"""
    defaultValue = 500000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500000),
    )


_HwSecStatEudmSessUdpInZoneNumMin_Type.__name__ = "Integer32"
_HwSecStatEudmSessUdpInZoneNumMin_Object = MibTableColumn
hwSecStatEudmSessUdpInZoneNumMin = _HwSecStatEudmSessUdpInZoneNumMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 11),
    _HwSecStatEudmSessUdpInZoneNumMin_Type()
)
hwSecStatEudmSessUdpInZoneNumMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessUdpInZoneNumMin.setStatus("current")
_HwSecStatEudmSessUdpInIPNumMax_Type = Integer32
_HwSecStatEudmSessUdpInIPNumMax_Object = MibTableColumn
hwSecStatEudmSessUdpInIPNumMax = _HwSecStatEudmSessUdpInIPNumMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 12),
    _HwSecStatEudmSessUdpInIPNumMax_Type()
)
hwSecStatEudmSessUdpInIPNumMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessUdpInIPNumMax.setStatus("current")
_HwSecStatEudmSessUdpInIPNumMin_Type = Integer32
_HwSecStatEudmSessUdpInIPNumMin_Object = MibTableColumn
hwSecStatEudmSessUdpInIPNumMin = _HwSecStatEudmSessUdpInIPNumMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 13),
    _HwSecStatEudmSessUdpInIPNumMin_Type()
)
hwSecStatEudmSessUdpInIPNumMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessUdpInIPNumMin.setStatus("current")


class _HwSecStatEudmSessUdpOutZoneNumMax_Type(Integer32):
    """Custom type hwSecStatEudmSessUdpOutZoneNumMax based on Integer32"""
    defaultValue = 500000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500000),
    )


_HwSecStatEudmSessUdpOutZoneNumMax_Type.__name__ = "Integer32"
_HwSecStatEudmSessUdpOutZoneNumMax_Object = MibTableColumn
hwSecStatEudmSessUdpOutZoneNumMax = _HwSecStatEudmSessUdpOutZoneNumMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 14),
    _HwSecStatEudmSessUdpOutZoneNumMax_Type()
)
hwSecStatEudmSessUdpOutZoneNumMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessUdpOutZoneNumMax.setStatus("current")


class _HwSecStatEudmSessUdpOutZoneNumMin_Type(Integer32):
    """Custom type hwSecStatEudmSessUdpOutZoneNumMin based on Integer32"""
    defaultValue = 500000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500000),
    )


_HwSecStatEudmSessUdpOutZoneNumMin_Type.__name__ = "Integer32"
_HwSecStatEudmSessUdpOutZoneNumMin_Object = MibTableColumn
hwSecStatEudmSessUdpOutZoneNumMin = _HwSecStatEudmSessUdpOutZoneNumMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 15),
    _HwSecStatEudmSessUdpOutZoneNumMin_Type()
)
hwSecStatEudmSessUdpOutZoneNumMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessUdpOutZoneNumMin.setStatus("current")
_HwSecStatEudmSessUdpOutIPNumMax_Type = Integer32
_HwSecStatEudmSessUdpOutIPNumMax_Object = MibTableColumn
hwSecStatEudmSessUdpOutIPNumMax = _HwSecStatEudmSessUdpOutIPNumMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 16),
    _HwSecStatEudmSessUdpOutIPNumMax_Type()
)
hwSecStatEudmSessUdpOutIPNumMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessUdpOutIPNumMax.setStatus("current")
_HwSecStatEudmSessUdpOutIPNumMin_Type = Integer32
_HwSecStatEudmSessUdpOutIPNumMin_Object = MibTableColumn
hwSecStatEudmSessUdpOutIPNumMin = _HwSecStatEudmSessUdpOutIPNumMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 17),
    _HwSecStatEudmSessUdpOutIPNumMin_Type()
)
hwSecStatEudmSessUdpOutIPNumMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessUdpOutIPNumMin.setStatus("current")
_HwSecStatEudmSessTcpInZoneSpeedMax_Type = Integer32
_HwSecStatEudmSessTcpInZoneSpeedMax_Object = MibTableColumn
hwSecStatEudmSessTcpInZoneSpeedMax = _HwSecStatEudmSessTcpInZoneSpeedMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 18),
    _HwSecStatEudmSessTcpInZoneSpeedMax_Type()
)
hwSecStatEudmSessTcpInZoneSpeedMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessTcpInZoneSpeedMax.setStatus("current")
_HwSecStatEudmSessTcpInZoneSpeedMin_Type = Integer32
_HwSecStatEudmSessTcpInZoneSpeedMin_Object = MibTableColumn
hwSecStatEudmSessTcpInZoneSpeedMin = _HwSecStatEudmSessTcpInZoneSpeedMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 19),
    _HwSecStatEudmSessTcpInZoneSpeedMin_Type()
)
hwSecStatEudmSessTcpInZoneSpeedMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessTcpInZoneSpeedMin.setStatus("current")
_HwSecStatEudmSessTcpInIPSpeedMax_Type = Integer32
_HwSecStatEudmSessTcpInIPSpeedMax_Object = MibTableColumn
hwSecStatEudmSessTcpInIPSpeedMax = _HwSecStatEudmSessTcpInIPSpeedMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 20),
    _HwSecStatEudmSessTcpInIPSpeedMax_Type()
)
hwSecStatEudmSessTcpInIPSpeedMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessTcpInIPSpeedMax.setStatus("current")
_HwSecStatEudmSessTcpInIPSpeedMin_Type = Integer32
_HwSecStatEudmSessTcpInIPSpeedMin_Object = MibTableColumn
hwSecStatEudmSessTcpInIPSpeedMin = _HwSecStatEudmSessTcpInIPSpeedMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 21),
    _HwSecStatEudmSessTcpInIPSpeedMin_Type()
)
hwSecStatEudmSessTcpInIPSpeedMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessTcpInIPSpeedMin.setStatus("current")
_HwSecStatEudmSessTcpOutZoneSpeedMax_Type = Integer32
_HwSecStatEudmSessTcpOutZoneSpeedMax_Object = MibTableColumn
hwSecStatEudmSessTcpOutZoneSpeedMax = _HwSecStatEudmSessTcpOutZoneSpeedMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 22),
    _HwSecStatEudmSessTcpOutZoneSpeedMax_Type()
)
hwSecStatEudmSessTcpOutZoneSpeedMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessTcpOutZoneSpeedMax.setStatus("current")
_HwSecStatEudmSessTcpOutZoneSpeedMin_Type = Integer32
_HwSecStatEudmSessTcpOutZoneSpeedMin_Object = MibTableColumn
hwSecStatEudmSessTcpOutZoneSpeedMin = _HwSecStatEudmSessTcpOutZoneSpeedMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 23),
    _HwSecStatEudmSessTcpOutZoneSpeedMin_Type()
)
hwSecStatEudmSessTcpOutZoneSpeedMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessTcpOutZoneSpeedMin.setStatus("current")
_HwSecStatEudmSessTcpOutIPSpeedMax_Type = Integer32
_HwSecStatEudmSessTcpOutIPSpeedMax_Object = MibTableColumn
hwSecStatEudmSessTcpOutIPSpeedMax = _HwSecStatEudmSessTcpOutIPSpeedMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 24),
    _HwSecStatEudmSessTcpOutIPSpeedMax_Type()
)
hwSecStatEudmSessTcpOutIPSpeedMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessTcpOutIPSpeedMax.setStatus("current")
_HwSecStatEudmSessTcpOutIPSpeedMin_Type = Integer32
_HwSecStatEudmSessTcpOutIPSpeedMin_Object = MibTableColumn
hwSecStatEudmSessTcpOutIPSpeedMin = _HwSecStatEudmSessTcpOutIPSpeedMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 25),
    _HwSecStatEudmSessTcpOutIPSpeedMin_Type()
)
hwSecStatEudmSessTcpOutIPSpeedMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessTcpOutIPSpeedMin.setStatus("current")
_HwSecStatEudmSessUdpInZoneSpeedMax_Type = Integer32
_HwSecStatEudmSessUdpInZoneSpeedMax_Object = MibTableColumn
hwSecStatEudmSessUdpInZoneSpeedMax = _HwSecStatEudmSessUdpInZoneSpeedMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 26),
    _HwSecStatEudmSessUdpInZoneSpeedMax_Type()
)
hwSecStatEudmSessUdpInZoneSpeedMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessUdpInZoneSpeedMax.setStatus("current")
_HwSecStatEudmSessUdpInZoneSpeedMin_Type = Integer32
_HwSecStatEudmSessUdpInZoneSpeedMin_Object = MibTableColumn
hwSecStatEudmSessUdpInZoneSpeedMin = _HwSecStatEudmSessUdpInZoneSpeedMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 27),
    _HwSecStatEudmSessUdpInZoneSpeedMin_Type()
)
hwSecStatEudmSessUdpInZoneSpeedMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessUdpInZoneSpeedMin.setStatus("current")
_HwSecStatEudmSessUdpInIPSpeedMax_Type = Integer32
_HwSecStatEudmSessUdpInIPSpeedMax_Object = MibTableColumn
hwSecStatEudmSessUdpInIPSpeedMax = _HwSecStatEudmSessUdpInIPSpeedMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 28),
    _HwSecStatEudmSessUdpInIPSpeedMax_Type()
)
hwSecStatEudmSessUdpInIPSpeedMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessUdpInIPSpeedMax.setStatus("current")
_HwSecStatEudmSessUdpInIPSpeedMin_Type = Integer32
_HwSecStatEudmSessUdpInIPSpeedMin_Object = MibTableColumn
hwSecStatEudmSessUdpInIPSpeedMin = _HwSecStatEudmSessUdpInIPSpeedMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 29),
    _HwSecStatEudmSessUdpInIPSpeedMin_Type()
)
hwSecStatEudmSessUdpInIPSpeedMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessUdpInIPSpeedMin.setStatus("current")
_HwSecStatEudmSessUdpOutZoneSpeedMax_Type = Integer32
_HwSecStatEudmSessUdpOutZoneSpeedMax_Object = MibTableColumn
hwSecStatEudmSessUdpOutZoneSpeedMax = _HwSecStatEudmSessUdpOutZoneSpeedMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 30),
    _HwSecStatEudmSessUdpOutZoneSpeedMax_Type()
)
hwSecStatEudmSessUdpOutZoneSpeedMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessUdpOutZoneSpeedMax.setStatus("current")
_HwSecStatEudmSessUdpOutZoneSpeedMin_Type = Integer32
_HwSecStatEudmSessUdpOutZoneSpeedMin_Object = MibTableColumn
hwSecStatEudmSessUdpOutZoneSpeedMin = _HwSecStatEudmSessUdpOutZoneSpeedMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 31),
    _HwSecStatEudmSessUdpOutZoneSpeedMin_Type()
)
hwSecStatEudmSessUdpOutZoneSpeedMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessUdpOutZoneSpeedMin.setStatus("current")
_HwSecStatEudmSessUdpOutIPSpeedMax_Type = Integer32
_HwSecStatEudmSessUdpOutIPSpeedMax_Object = MibTableColumn
hwSecStatEudmSessUdpOutIPSpeedMax = _HwSecStatEudmSessUdpOutIPSpeedMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 32),
    _HwSecStatEudmSessUdpOutIPSpeedMax_Type()
)
hwSecStatEudmSessUdpOutIPSpeedMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessUdpOutIPSpeedMax.setStatus("current")
_HwSecStatEudmSessUdpOutIPSpeedMin_Type = Integer32
_HwSecStatEudmSessUdpOutIPSpeedMin_Object = MibTableColumn
hwSecStatEudmSessUdpOutIPSpeedMin = _HwSecStatEudmSessUdpOutIPSpeedMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 33),
    _HwSecStatEudmSessUdpOutIPSpeedMin_Type()
)
hwSecStatEudmSessUdpOutIPSpeedMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessUdpOutIPSpeedMin.setStatus("current")


class _HwSecStatEudmSessCfgSetDefault_Type(Integer32):
    """Custom type hwSecStatEudmSessCfgSetDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwSecStatEudmSessCfgSetDefault_Type.__name__ = "Integer32"
_HwSecStatEudmSessCfgSetDefault_Object = MibTableColumn
hwSecStatEudmSessCfgSetDefault = _HwSecStatEudmSessCfgSetDefault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 1, 1, 34),
    _HwSecStatEudmSessCfgSetDefault_Type()
)
hwSecStatEudmSessCfgSetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmSessCfgSetDefault.setStatus("current")
_HwSecStatEudmCfgEnableTable_Object = MibTable
hwSecStatEudmCfgEnableTable = _HwSecStatEudmCfgEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hwSecStatEudmCfgEnableTable.setStatus("current")
_HwSecStatEudmCfgEnableEntry_Object = MibTableRow
hwSecStatEudmCfgEnableEntry = _HwSecStatEudmCfgEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 2, 1)
)
hwSecStatEudmCfgEnableEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmCfgEnableZoneID"),
)
if mibBuilder.loadTexts:
    hwSecStatEudmCfgEnableEntry.setStatus("current")


class _HwSecStatEudmCfgEnableZoneID_Type(Integer32):
    """Custom type hwSecStatEudmCfgEnableZoneID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwSecStatEudmCfgEnableZoneID_Type.__name__ = "Integer32"
_HwSecStatEudmCfgEnableZoneID_Object = MibTableColumn
hwSecStatEudmCfgEnableZoneID = _HwSecStatEudmCfgEnableZoneID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 2, 1, 1),
    _HwSecStatEudmCfgEnableZoneID_Type()
)
hwSecStatEudmCfgEnableZoneID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSecStatEudmCfgEnableZoneID.setStatus("current")


class _HwSecStatEudmCfgEnbaleZoneIn_Type(TruthValue):
    """Custom type hwSecStatEudmCfgEnbaleZoneIn based on TruthValue"""


_HwSecStatEudmCfgEnbaleZoneIn_Object = MibTableColumn
hwSecStatEudmCfgEnbaleZoneIn = _HwSecStatEudmCfgEnbaleZoneIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 2, 1, 2),
    _HwSecStatEudmCfgEnbaleZoneIn_Type()
)
hwSecStatEudmCfgEnbaleZoneIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmCfgEnbaleZoneIn.setStatus("current")


class _HwSecStatEudmCfgEnbaleZoneOut_Type(TruthValue):
    """Custom type hwSecStatEudmCfgEnbaleZoneOut based on TruthValue"""


_HwSecStatEudmCfgEnbaleZoneOut_Object = MibTableColumn
hwSecStatEudmCfgEnbaleZoneOut = _HwSecStatEudmCfgEnbaleZoneOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 2, 1, 3),
    _HwSecStatEudmCfgEnbaleZoneOut_Type()
)
hwSecStatEudmCfgEnbaleZoneOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmCfgEnbaleZoneOut.setStatus("current")
_HwSecStatEudmCfgEnbaleIpIn_Type = TruthValue
_HwSecStatEudmCfgEnbaleIpIn_Object = MibTableColumn
hwSecStatEudmCfgEnbaleIpIn = _HwSecStatEudmCfgEnbaleIpIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 2, 1, 4),
    _HwSecStatEudmCfgEnbaleIpIn_Type()
)
hwSecStatEudmCfgEnbaleIpIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmCfgEnbaleIpIn.setStatus("current")
_HwSecStatEudmCfgEnbaleIPOut_Type = TruthValue
_HwSecStatEudmCfgEnbaleIPOut_Object = MibTableColumn
hwSecStatEudmCfgEnbaleIPOut = _HwSecStatEudmCfgEnbaleIPOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 2, 1, 5),
    _HwSecStatEudmCfgEnbaleIPOut_Type()
)
hwSecStatEudmCfgEnbaleIPOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmCfgEnbaleIPOut.setStatus("current")


class _HwSecStatEudmCfgEnableSetDefault_Type(Integer32):
    """Custom type hwSecStatEudmCfgEnableSetDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwSecStatEudmCfgEnableSetDefault_Type.__name__ = "Integer32"
_HwSecStatEudmCfgEnableSetDefault_Object = MibTableColumn
hwSecStatEudmCfgEnableSetDefault = _HwSecStatEudmCfgEnableSetDefault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 1, 2, 1, 6),
    _HwSecStatEudmCfgEnableSetDefault_Type()
)
hwSecStatEudmCfgEnableSetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatEudmCfgEnableSetDefault.setStatus("current")
_HwSecStatEudmMonitorObjects_ObjectIdentity = ObjectIdentity
hwSecStatEudmMonitorObjects = _HwSecStatEudmMonitorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2)
)
_HwSecStatZoneInfoTable_Object = MibTable
hwSecStatZoneInfoTable = _HwSecStatZoneInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hwSecStatZoneInfoTable.setStatus("current")
_HwSecStatZoneInfoEntry_Object = MibTableRow
hwSecStatZoneInfoEntry = _HwSecStatZoneInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1)
)
hwSecStatZoneInfoEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneInfoZoneID"),
)
if mibBuilder.loadTexts:
    hwSecStatZoneInfoEntry.setStatus("current")


class _HwSecStatZoneInfoZoneID_Type(Integer32):
    """Custom type hwSecStatZoneInfoZoneID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwSecStatZoneInfoZoneID_Type.__name__ = "Integer32"
_HwSecStatZoneInfoZoneID_Object = MibTableColumn
hwSecStatZoneInfoZoneID = _HwSecStatZoneInfoZoneID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 1),
    _HwSecStatZoneInfoZoneID_Type()
)
hwSecStatZoneInfoZoneID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSecStatZoneInfoZoneID.setStatus("current")
_HwSecStatZoneInTcpSess_Type = Counter64
_HwSecStatZoneInTcpSess_Object = MibTableColumn
hwSecStatZoneInTcpSess = _HwSecStatZoneInTcpSess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 2),
    _HwSecStatZoneInTcpSess_Type()
)
hwSecStatZoneInTcpSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneInTcpSess.setStatus("current")
_HwSecStatZoneInUdpSess_Type = Counter64
_HwSecStatZoneInUdpSess_Object = MibTableColumn
hwSecStatZoneInUdpSess = _HwSecStatZoneInUdpSess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 3),
    _HwSecStatZoneInUdpSess_Type()
)
hwSecStatZoneInUdpSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneInUdpSess.setStatus("current")
_HwSecStatZoneInIcmpSess_Type = Counter64
_HwSecStatZoneInIcmpSess_Object = MibTableColumn
hwSecStatZoneInIcmpSess = _HwSecStatZoneInIcmpSess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 4),
    _HwSecStatZoneInIcmpSess_Type()
)
hwSecStatZoneInIcmpSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneInIcmpSess.setStatus("current")
_HwSecStatZoneInConn_Type = Counter64
_HwSecStatZoneInConn_Object = MibTableColumn
hwSecStatZoneInConn = _HwSecStatZoneInConn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 5),
    _HwSecStatZoneInConn_Type()
)
hwSecStatZoneInConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneInConn.setStatus("current")
_HwSecStatZoneInHalfConn_Type = Counter64
_HwSecStatZoneInHalfConn_Object = MibTableColumn
hwSecStatZoneInHalfConn = _HwSecStatZoneInHalfConn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 6),
    _HwSecStatZoneInHalfConn_Type()
)
hwSecStatZoneInHalfConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneInHalfConn.setStatus("current")
_HwSecStatZoneInTcpSessSpeed_Type = Counter64
_HwSecStatZoneInTcpSessSpeed_Object = MibTableColumn
hwSecStatZoneInTcpSessSpeed = _HwSecStatZoneInTcpSessSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 7),
    _HwSecStatZoneInTcpSessSpeed_Type()
)
hwSecStatZoneInTcpSessSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneInTcpSessSpeed.setStatus("current")
_HwSecStatZoneInUdpSessSpeed_Type = Counter64
_HwSecStatZoneInUdpSessSpeed_Object = MibTableColumn
hwSecStatZoneInUdpSessSpeed = _HwSecStatZoneInUdpSessSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 8),
    _HwSecStatZoneInUdpSessSpeed_Type()
)
hwSecStatZoneInUdpSessSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneInUdpSessSpeed.setStatus("current")
_HwSecStatZoneInIcmpSessSpeed_Type = Counter64
_HwSecStatZoneInIcmpSessSpeed_Object = MibTableColumn
hwSecStatZoneInIcmpSessSpeed = _HwSecStatZoneInIcmpSessSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 9),
    _HwSecStatZoneInIcmpSessSpeed_Type()
)
hwSecStatZoneInIcmpSessSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneInIcmpSessSpeed.setStatus("current")
_HwSecStatZoneInConnSpeed_Type = Counter64
_HwSecStatZoneInConnSpeed_Object = MibTableColumn
hwSecStatZoneInConnSpeed = _HwSecStatZoneInConnSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 10),
    _HwSecStatZoneInConnSpeed_Type()
)
hwSecStatZoneInConnSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneInConnSpeed.setStatus("current")
_HwSecStatZoneInHalfConnSpeed_Type = Counter64
_HwSecStatZoneInHalfConnSpeed_Object = MibTableColumn
hwSecStatZoneInHalfConnSpeed = _HwSecStatZoneInHalfConnSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 11),
    _HwSecStatZoneInHalfConnSpeed_Type()
)
hwSecStatZoneInHalfConnSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneInHalfConnSpeed.setStatus("current")
_HwSecStatZoneInAclDenyIcmpPkts_Type = Counter64
_HwSecStatZoneInAclDenyIcmpPkts_Object = MibTableColumn
hwSecStatZoneInAclDenyIcmpPkts = _HwSecStatZoneInAclDenyIcmpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 12),
    _HwSecStatZoneInAclDenyIcmpPkts_Type()
)
hwSecStatZoneInAclDenyIcmpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneInAclDenyIcmpPkts.setStatus("current")
_HwSecStatZoneInAclDenyIcmpOcts_Type = Counter64
_HwSecStatZoneInAclDenyIcmpOcts_Object = MibTableColumn
hwSecStatZoneInAclDenyIcmpOcts = _HwSecStatZoneInAclDenyIcmpOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 13),
    _HwSecStatZoneInAclDenyIcmpOcts_Type()
)
hwSecStatZoneInAclDenyIcmpOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneInAclDenyIcmpOcts.setStatus("current")
_HwSecStatZoneInAclDenyNonIcmpPkts_Type = Counter64
_HwSecStatZoneInAclDenyNonIcmpPkts_Object = MibTableColumn
hwSecStatZoneInAclDenyNonIcmpPkts = _HwSecStatZoneInAclDenyNonIcmpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 14),
    _HwSecStatZoneInAclDenyNonIcmpPkts_Type()
)
hwSecStatZoneInAclDenyNonIcmpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneInAclDenyNonIcmpPkts.setStatus("current")
_HwSecStatZoneInAclDenyNonIcmpOcts_Type = Counter64
_HwSecStatZoneInAclDenyNonIcmpOcts_Object = MibTableColumn
hwSecStatZoneInAclDenyNonIcmpOcts = _HwSecStatZoneInAclDenyNonIcmpOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 15),
    _HwSecStatZoneInAclDenyNonIcmpOcts_Type()
)
hwSecStatZoneInAclDenyNonIcmpOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneInAclDenyNonIcmpOcts.setStatus("current")
_HwSecStatZoneInBlsDenyPkts_Type = Counter64
_HwSecStatZoneInBlsDenyPkts_Object = MibTableColumn
hwSecStatZoneInBlsDenyPkts = _HwSecStatZoneInBlsDenyPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 16),
    _HwSecStatZoneInBlsDenyPkts_Type()
)
hwSecStatZoneInBlsDenyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneInBlsDenyPkts.setStatus("current")
_HwSecStatZoneInDftAclDenyPkts_Type = Counter64
_HwSecStatZoneInDftAclDenyPkts_Object = MibTableColumn
hwSecStatZoneInDftAclDenyPkts = _HwSecStatZoneInDftAclDenyPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 17),
    _HwSecStatZoneInDftAclDenyPkts_Type()
)
hwSecStatZoneInDftAclDenyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneInDftAclDenyPkts.setStatus("current")
_HwSecStatZoneInDftAclDenyIcmpPkts_Type = Counter64
_HwSecStatZoneInDftAclDenyIcmpPkts_Object = MibTableColumn
hwSecStatZoneInDftAclDenyIcmpPkts = _HwSecStatZoneInDftAclDenyIcmpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 18),
    _HwSecStatZoneInDftAclDenyIcmpPkts_Type()
)
hwSecStatZoneInDftAclDenyIcmpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneInDftAclDenyIcmpPkts.setStatus("current")
_HwSecStatZoneInIcmpFloodDropPkts_Type = Counter64
_HwSecStatZoneInIcmpFloodDropPkts_Object = MibTableColumn
hwSecStatZoneInIcmpFloodDropPkts = _HwSecStatZoneInIcmpFloodDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 19),
    _HwSecStatZoneInIcmpFloodDropPkts_Type()
)
hwSecStatZoneInIcmpFloodDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneInIcmpFloodDropPkts.setStatus("current")
_HwSecStatZoneInUdpFloodDropPkts_Type = Counter64
_HwSecStatZoneInUdpFloodDropPkts_Object = MibTableColumn
hwSecStatZoneInUdpFloodDropPkts = _HwSecStatZoneInUdpFloodDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 20),
    _HwSecStatZoneInUdpFloodDropPkts_Type()
)
hwSecStatZoneInUdpFloodDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneInUdpFloodDropPkts.setStatus("current")
_HwSecStatZoneInFtpPkts_Type = Counter64
_HwSecStatZoneInFtpPkts_Object = MibTableColumn
hwSecStatZoneInFtpPkts = _HwSecStatZoneInFtpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 21),
    _HwSecStatZoneInFtpPkts_Type()
)
hwSecStatZoneInFtpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneInFtpPkts.setStatus("current")
_HwSecStatZoneInSmtpPkts_Type = Counter64
_HwSecStatZoneInSmtpPkts_Object = MibTableColumn
hwSecStatZoneInSmtpPkts = _HwSecStatZoneInSmtpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 22),
    _HwSecStatZoneInSmtpPkts_Type()
)
hwSecStatZoneInSmtpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneInSmtpPkts.setStatus("current")
_HwSecStatZoneInHttpPkts_Type = Counter64
_HwSecStatZoneInHttpPkts_Object = MibTableColumn
hwSecStatZoneInHttpPkts = _HwSecStatZoneInHttpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 23),
    _HwSecStatZoneInHttpPkts_Type()
)
hwSecStatZoneInHttpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneInHttpPkts.setStatus("current")
_HwSecStatZoneInH323Pkts_Type = Counter64
_HwSecStatZoneInH323Pkts_Object = MibTableColumn
hwSecStatZoneInH323Pkts = _HwSecStatZoneInH323Pkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 24),
    _HwSecStatZoneInH323Pkts_Type()
)
hwSecStatZoneInH323Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneInH323Pkts.setStatus("current")
_HwSecStatZoneInRtspPkts_Type = Counter64
_HwSecStatZoneInRtspPkts_Object = MibTableColumn
hwSecStatZoneInRtspPkts = _HwSecStatZoneInRtspPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 25),
    _HwSecStatZoneInRtspPkts_Type()
)
hwSecStatZoneInRtspPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneInRtspPkts.setStatus("current")
_HwSecStatZoneOutTcpSess_Type = Counter64
_HwSecStatZoneOutTcpSess_Object = MibTableColumn
hwSecStatZoneOutTcpSess = _HwSecStatZoneOutTcpSess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 26),
    _HwSecStatZoneOutTcpSess_Type()
)
hwSecStatZoneOutTcpSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneOutTcpSess.setStatus("current")
_HwSecStatZoneOutUdpSess_Type = Counter64
_HwSecStatZoneOutUdpSess_Object = MibTableColumn
hwSecStatZoneOutUdpSess = _HwSecStatZoneOutUdpSess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 27),
    _HwSecStatZoneOutUdpSess_Type()
)
hwSecStatZoneOutUdpSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneOutUdpSess.setStatus("current")
_HwSecStatZoneOutIcmpSess_Type = Counter64
_HwSecStatZoneOutIcmpSess_Object = MibTableColumn
hwSecStatZoneOutIcmpSess = _HwSecStatZoneOutIcmpSess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 28),
    _HwSecStatZoneOutIcmpSess_Type()
)
hwSecStatZoneOutIcmpSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneOutIcmpSess.setStatus("current")
_HwSecStatZoneOutConn_Type = Counter64
_HwSecStatZoneOutConn_Object = MibTableColumn
hwSecStatZoneOutConn = _HwSecStatZoneOutConn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 29),
    _HwSecStatZoneOutConn_Type()
)
hwSecStatZoneOutConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneOutConn.setStatus("current")
_HwSecStatZoneOutHalfConn_Type = Counter64
_HwSecStatZoneOutHalfConn_Object = MibTableColumn
hwSecStatZoneOutHalfConn = _HwSecStatZoneOutHalfConn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 30),
    _HwSecStatZoneOutHalfConn_Type()
)
hwSecStatZoneOutHalfConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneOutHalfConn.setStatus("current")
_HwSecStatZoneOutTcpSessSpeed_Type = Counter64
_HwSecStatZoneOutTcpSessSpeed_Object = MibTableColumn
hwSecStatZoneOutTcpSessSpeed = _HwSecStatZoneOutTcpSessSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 31),
    _HwSecStatZoneOutTcpSessSpeed_Type()
)
hwSecStatZoneOutTcpSessSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneOutTcpSessSpeed.setStatus("current")
_HwSecStatZoneOutUdpSessSpeed_Type = Counter64
_HwSecStatZoneOutUdpSessSpeed_Object = MibTableColumn
hwSecStatZoneOutUdpSessSpeed = _HwSecStatZoneOutUdpSessSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 32),
    _HwSecStatZoneOutUdpSessSpeed_Type()
)
hwSecStatZoneOutUdpSessSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneOutUdpSessSpeed.setStatus("current")
_HwSecStatZoneOutIcmpSessSpeed_Type = Counter64
_HwSecStatZoneOutIcmpSessSpeed_Object = MibTableColumn
hwSecStatZoneOutIcmpSessSpeed = _HwSecStatZoneOutIcmpSessSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 33),
    _HwSecStatZoneOutIcmpSessSpeed_Type()
)
hwSecStatZoneOutIcmpSessSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneOutIcmpSessSpeed.setStatus("current")
_HwSecStatZoneOutConnSpeed_Type = Counter64
_HwSecStatZoneOutConnSpeed_Object = MibTableColumn
hwSecStatZoneOutConnSpeed = _HwSecStatZoneOutConnSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 34),
    _HwSecStatZoneOutConnSpeed_Type()
)
hwSecStatZoneOutConnSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneOutConnSpeed.setStatus("current")
_HwSecStatZoneOutHalfConnSpeed_Type = Counter64
_HwSecStatZoneOutHalfConnSpeed_Object = MibTableColumn
hwSecStatZoneOutHalfConnSpeed = _HwSecStatZoneOutHalfConnSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 35),
    _HwSecStatZoneOutHalfConnSpeed_Type()
)
hwSecStatZoneOutHalfConnSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneOutHalfConnSpeed.setStatus("current")
_HwSecStatZoneOutAclDenyIcmpPkts_Type = Counter64
_HwSecStatZoneOutAclDenyIcmpPkts_Object = MibTableColumn
hwSecStatZoneOutAclDenyIcmpPkts = _HwSecStatZoneOutAclDenyIcmpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 36),
    _HwSecStatZoneOutAclDenyIcmpPkts_Type()
)
hwSecStatZoneOutAclDenyIcmpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneOutAclDenyIcmpPkts.setStatus("current")
_HwSecStatZoneOutAclDenyIcmpOcts_Type = Counter64
_HwSecStatZoneOutAclDenyIcmpOcts_Object = MibTableColumn
hwSecStatZoneOutAclDenyIcmpOcts = _HwSecStatZoneOutAclDenyIcmpOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 37),
    _HwSecStatZoneOutAclDenyIcmpOcts_Type()
)
hwSecStatZoneOutAclDenyIcmpOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneOutAclDenyIcmpOcts.setStatus("current")
_HwSecStatZoneOutAclDenyNonIcmpPkts_Type = Counter64
_HwSecStatZoneOutAclDenyNonIcmpPkts_Object = MibTableColumn
hwSecStatZoneOutAclDenyNonIcmpPkts = _HwSecStatZoneOutAclDenyNonIcmpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 38),
    _HwSecStatZoneOutAclDenyNonIcmpPkts_Type()
)
hwSecStatZoneOutAclDenyNonIcmpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneOutAclDenyNonIcmpPkts.setStatus("current")
_HwSecStatZoneOutAclDenyNonIcmpOcts_Type = Counter64
_HwSecStatZoneOutAclDenyNonIcmpOcts_Object = MibTableColumn
hwSecStatZoneOutAclDenyNonIcmpOcts = _HwSecStatZoneOutAclDenyNonIcmpOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 39),
    _HwSecStatZoneOutAclDenyNonIcmpOcts_Type()
)
hwSecStatZoneOutAclDenyNonIcmpOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneOutAclDenyNonIcmpOcts.setStatus("current")
_HwSecStatZoneOutBlsDenyPkts_Type = Counter64
_HwSecStatZoneOutBlsDenyPkts_Object = MibTableColumn
hwSecStatZoneOutBlsDenyPkts = _HwSecStatZoneOutBlsDenyPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 40),
    _HwSecStatZoneOutBlsDenyPkts_Type()
)
hwSecStatZoneOutBlsDenyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneOutBlsDenyPkts.setStatus("current")
_HwSecStatZoneOutDftAclDenyPkts_Type = Counter64
_HwSecStatZoneOutDftAclDenyPkts_Object = MibTableColumn
hwSecStatZoneOutDftAclDenyPkts = _HwSecStatZoneOutDftAclDenyPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 41),
    _HwSecStatZoneOutDftAclDenyPkts_Type()
)
hwSecStatZoneOutDftAclDenyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneOutDftAclDenyPkts.setStatus("current")
_HwSecStatZoneOutDftAclDenyIcmpPkts_Type = Counter64
_HwSecStatZoneOutDftAclDenyIcmpPkts_Object = MibTableColumn
hwSecStatZoneOutDftAclDenyIcmpPkts = _HwSecStatZoneOutDftAclDenyIcmpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 42),
    _HwSecStatZoneOutDftAclDenyIcmpPkts_Type()
)
hwSecStatZoneOutDftAclDenyIcmpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneOutDftAclDenyIcmpPkts.setStatus("current")
_HwSecStatZoneOutFtpPkts_Type = Counter64
_HwSecStatZoneOutFtpPkts_Object = MibTableColumn
hwSecStatZoneOutFtpPkts = _HwSecStatZoneOutFtpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 43),
    _HwSecStatZoneOutFtpPkts_Type()
)
hwSecStatZoneOutFtpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneOutFtpPkts.setStatus("current")
_HwSecStatZoneOutSmtpPkts_Type = Counter64
_HwSecStatZoneOutSmtpPkts_Object = MibTableColumn
hwSecStatZoneOutSmtpPkts = _HwSecStatZoneOutSmtpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 44),
    _HwSecStatZoneOutSmtpPkts_Type()
)
hwSecStatZoneOutSmtpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneOutSmtpPkts.setStatus("current")
_HwSecStatZoneOutHttpPkts_Type = Counter64
_HwSecStatZoneOutHttpPkts_Object = MibTableColumn
hwSecStatZoneOutHttpPkts = _HwSecStatZoneOutHttpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 45),
    _HwSecStatZoneOutHttpPkts_Type()
)
hwSecStatZoneOutHttpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneOutHttpPkts.setStatus("current")
_HwSecStatZoneOutH323Pkts_Type = Counter64
_HwSecStatZoneOutH323Pkts_Object = MibTableColumn
hwSecStatZoneOutH323Pkts = _HwSecStatZoneOutH323Pkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 46),
    _HwSecStatZoneOutH323Pkts_Type()
)
hwSecStatZoneOutH323Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneOutH323Pkts.setStatus("current")
_HwSecStatZoneOutRtspPkts_Type = Counter64
_HwSecStatZoneOutRtspPkts_Object = MibTableColumn
hwSecStatZoneOutRtspPkts = _HwSecStatZoneOutRtspPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 47),
    _HwSecStatZoneOutRtspPkts_Type()
)
hwSecStatZoneOutRtspPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatZoneOutRtspPkts.setStatus("current")


class _HwSecStatClearZoneInfo_Type(Integer32):
    """Custom type hwSecStatClearZoneInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwSecStatClearZoneInfo_Type.__name__ = "Integer32"
_HwSecStatClearZoneInfo_Object = MibTableColumn
hwSecStatClearZoneInfo = _HwSecStatClearZoneInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 2, 1, 1, 48),
    _HwSecStatClearZoneInfo_Type()
)
hwSecStatClearZoneInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatClearZoneInfo.setStatus("current")
_HwSECSTATEudmConformance_ObjectIdentity = ObjectIdentity
hwSECSTATEudmConformance = _HwSECSTATEudmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 3)
)
_HwSECSTATEudmCompliance_ObjectIdentity = ObjectIdentity
hwSECSTATEudmCompliance = _HwSECSTATEudmCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 3, 1)
)
_HwSECSTATEudmMibGroups_ObjectIdentity = ObjectIdentity
hwSECSTATEudmMibGroups = _HwSECSTATEudmMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 3, 2)
)

# Managed Objects groups

hwSECSTATEudmZoneCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 3, 2, 2)
)
hwSECSTATEudmZoneCfgGroup.setObjects(
      *(("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessTcpInZoneNumMax"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessTcpInZoneNumMin"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessTcpInIPNumMax"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessTcpInIPNumMin"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessTcpOutZoneNumMax"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessTcpOutZoneNumMin"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessTcpOutIPNumMax"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessTcpOutIPNumMin"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessUdpInZoneNumMax"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessUdpInZoneNumMin"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessUdpInIPNumMax"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessUdpInIPNumMin"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessUdpOutZoneNumMax"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessUdpOutZoneNumMin"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessUdpOutIPNumMax"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessUdpOutIPNumMin"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessTcpInZoneSpeedMax"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessTcpInZoneSpeedMin"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessTcpInIPSpeedMax"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessTcpInIPSpeedMin"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessTcpOutZoneSpeedMax"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessTcpOutZoneSpeedMin"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessTcpOutIPSpeedMax"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessTcpOutIPSpeedMin"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessUdpInZoneSpeedMax"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessUdpInZoneSpeedMin"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessUdpInIPSpeedMax"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessUdpInIPSpeedMin"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessUdpOutZoneSpeedMax"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessUdpOutZoneSpeedMin"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessUdpOutIPSpeedMax"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessUdpOutIPSpeedMin"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmCfgEnbaleZoneIn"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmCfgEnbaleZoneOut"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmCfgEnbaleIpIn"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmCfgEnbaleIPOut"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmSessCfgSetDefault"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatEudmCfgEnableSetDefault"))
)
if mibBuilder.loadTexts:
    hwSECSTATEudmZoneCfgGroup.setStatus("current")

hwSECSTATEudmZoneMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 2, 3, 2, 4)
)
hwSECSTATEudmZoneMonitorGroup.setObjects(
      *(("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneInTcpSess"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneInUdpSess"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneInIcmpSess"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneInConn"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneInHalfConn"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneInTcpSessSpeed"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneInUdpSessSpeed"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneInIcmpSessSpeed"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneInConnSpeed"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneInHalfConnSpeed"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneInAclDenyIcmpPkts"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneInAclDenyIcmpOcts"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneInAclDenyNonIcmpPkts"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneInAclDenyNonIcmpOcts"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneInIcmpFloodDropPkts"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneInUdpFloodDropPkts"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneInFtpPkts"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneInSmtpPkts"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneInHttpPkts"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneInH323Pkts"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneInRtspPkts"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneOutTcpSess"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneOutUdpSess"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneOutIcmpSess"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneOutConn"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneOutHalfConn"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneOutTcpSessSpeed"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneOutUdpSessSpeed"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneOutIcmpSessSpeed"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneOutConnSpeed"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneOutHalfConnSpeed"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneOutAclDenyIcmpPkts"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneOutAclDenyIcmpOcts"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneOutAclDenyNonIcmpPkts"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneOutAclDenyNonIcmpOcts"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneOutDftAclDenyIcmpPkts"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneOutFtpPkts"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneOutSmtpPkts"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneOutHttpPkts"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneOutH323Pkts"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneOutRtspPkts"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneInDftAclDenyIcmpPkts"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneInBlsDenyPkts"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneInDftAclDenyPkts"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatClearZoneInfo"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneOutDftAclDenyPkts"),
        ("HUAWEI-SECSTAT-EUDM-MIB", "hwSecStatZoneOutBlsDenyPkts"))
)
if mibBuilder.loadTexts:
    hwSECSTATEudmZoneMonitorGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SECSTAT-EUDM-MIB",
    **{"hwSECSTAT": hwSECSTAT,
       "hwSECSTATEudm": hwSECSTATEudm,
       "hwSecStatEudmCfgObjects": hwSecStatEudmCfgObjects,
       "hwSecStatEudmSessCfgTable": hwSecStatEudmSessCfgTable,
       "hwSecStatEudmSessCfgEntry": hwSecStatEudmSessCfgEntry,
       "hwSecStatEudmSessCfgZoneID": hwSecStatEudmSessCfgZoneID,
       "hwSecStatEudmSessTcpInZoneNumMax": hwSecStatEudmSessTcpInZoneNumMax,
       "hwSecStatEudmSessTcpInZoneNumMin": hwSecStatEudmSessTcpInZoneNumMin,
       "hwSecStatEudmSessTcpInIPNumMax": hwSecStatEudmSessTcpInIPNumMax,
       "hwSecStatEudmSessTcpInIPNumMin": hwSecStatEudmSessTcpInIPNumMin,
       "hwSecStatEudmSessTcpOutZoneNumMax": hwSecStatEudmSessTcpOutZoneNumMax,
       "hwSecStatEudmSessTcpOutZoneNumMin": hwSecStatEudmSessTcpOutZoneNumMin,
       "hwSecStatEudmSessTcpOutIPNumMax": hwSecStatEudmSessTcpOutIPNumMax,
       "hwSecStatEudmSessTcpOutIPNumMin": hwSecStatEudmSessTcpOutIPNumMin,
       "hwSecStatEudmSessUdpInZoneNumMax": hwSecStatEudmSessUdpInZoneNumMax,
       "hwSecStatEudmSessUdpInZoneNumMin": hwSecStatEudmSessUdpInZoneNumMin,
       "hwSecStatEudmSessUdpInIPNumMax": hwSecStatEudmSessUdpInIPNumMax,
       "hwSecStatEudmSessUdpInIPNumMin": hwSecStatEudmSessUdpInIPNumMin,
       "hwSecStatEudmSessUdpOutZoneNumMax": hwSecStatEudmSessUdpOutZoneNumMax,
       "hwSecStatEudmSessUdpOutZoneNumMin": hwSecStatEudmSessUdpOutZoneNumMin,
       "hwSecStatEudmSessUdpOutIPNumMax": hwSecStatEudmSessUdpOutIPNumMax,
       "hwSecStatEudmSessUdpOutIPNumMin": hwSecStatEudmSessUdpOutIPNumMin,
       "hwSecStatEudmSessTcpInZoneSpeedMax": hwSecStatEudmSessTcpInZoneSpeedMax,
       "hwSecStatEudmSessTcpInZoneSpeedMin": hwSecStatEudmSessTcpInZoneSpeedMin,
       "hwSecStatEudmSessTcpInIPSpeedMax": hwSecStatEudmSessTcpInIPSpeedMax,
       "hwSecStatEudmSessTcpInIPSpeedMin": hwSecStatEudmSessTcpInIPSpeedMin,
       "hwSecStatEudmSessTcpOutZoneSpeedMax": hwSecStatEudmSessTcpOutZoneSpeedMax,
       "hwSecStatEudmSessTcpOutZoneSpeedMin": hwSecStatEudmSessTcpOutZoneSpeedMin,
       "hwSecStatEudmSessTcpOutIPSpeedMax": hwSecStatEudmSessTcpOutIPSpeedMax,
       "hwSecStatEudmSessTcpOutIPSpeedMin": hwSecStatEudmSessTcpOutIPSpeedMin,
       "hwSecStatEudmSessUdpInZoneSpeedMax": hwSecStatEudmSessUdpInZoneSpeedMax,
       "hwSecStatEudmSessUdpInZoneSpeedMin": hwSecStatEudmSessUdpInZoneSpeedMin,
       "hwSecStatEudmSessUdpInIPSpeedMax": hwSecStatEudmSessUdpInIPSpeedMax,
       "hwSecStatEudmSessUdpInIPSpeedMin": hwSecStatEudmSessUdpInIPSpeedMin,
       "hwSecStatEudmSessUdpOutZoneSpeedMax": hwSecStatEudmSessUdpOutZoneSpeedMax,
       "hwSecStatEudmSessUdpOutZoneSpeedMin": hwSecStatEudmSessUdpOutZoneSpeedMin,
       "hwSecStatEudmSessUdpOutIPSpeedMax": hwSecStatEudmSessUdpOutIPSpeedMax,
       "hwSecStatEudmSessUdpOutIPSpeedMin": hwSecStatEudmSessUdpOutIPSpeedMin,
       "hwSecStatEudmSessCfgSetDefault": hwSecStatEudmSessCfgSetDefault,
       "hwSecStatEudmCfgEnableTable": hwSecStatEudmCfgEnableTable,
       "hwSecStatEudmCfgEnableEntry": hwSecStatEudmCfgEnableEntry,
       "hwSecStatEudmCfgEnableZoneID": hwSecStatEudmCfgEnableZoneID,
       "hwSecStatEudmCfgEnbaleZoneIn": hwSecStatEudmCfgEnbaleZoneIn,
       "hwSecStatEudmCfgEnbaleZoneOut": hwSecStatEudmCfgEnbaleZoneOut,
       "hwSecStatEudmCfgEnbaleIpIn": hwSecStatEudmCfgEnbaleIpIn,
       "hwSecStatEudmCfgEnbaleIPOut": hwSecStatEudmCfgEnbaleIPOut,
       "hwSecStatEudmCfgEnableSetDefault": hwSecStatEudmCfgEnableSetDefault,
       "hwSecStatEudmMonitorObjects": hwSecStatEudmMonitorObjects,
       "hwSecStatZoneInfoTable": hwSecStatZoneInfoTable,
       "hwSecStatZoneInfoEntry": hwSecStatZoneInfoEntry,
       "hwSecStatZoneInfoZoneID": hwSecStatZoneInfoZoneID,
       "hwSecStatZoneInTcpSess": hwSecStatZoneInTcpSess,
       "hwSecStatZoneInUdpSess": hwSecStatZoneInUdpSess,
       "hwSecStatZoneInIcmpSess": hwSecStatZoneInIcmpSess,
       "hwSecStatZoneInConn": hwSecStatZoneInConn,
       "hwSecStatZoneInHalfConn": hwSecStatZoneInHalfConn,
       "hwSecStatZoneInTcpSessSpeed": hwSecStatZoneInTcpSessSpeed,
       "hwSecStatZoneInUdpSessSpeed": hwSecStatZoneInUdpSessSpeed,
       "hwSecStatZoneInIcmpSessSpeed": hwSecStatZoneInIcmpSessSpeed,
       "hwSecStatZoneInConnSpeed": hwSecStatZoneInConnSpeed,
       "hwSecStatZoneInHalfConnSpeed": hwSecStatZoneInHalfConnSpeed,
       "hwSecStatZoneInAclDenyIcmpPkts": hwSecStatZoneInAclDenyIcmpPkts,
       "hwSecStatZoneInAclDenyIcmpOcts": hwSecStatZoneInAclDenyIcmpOcts,
       "hwSecStatZoneInAclDenyNonIcmpPkts": hwSecStatZoneInAclDenyNonIcmpPkts,
       "hwSecStatZoneInAclDenyNonIcmpOcts": hwSecStatZoneInAclDenyNonIcmpOcts,
       "hwSecStatZoneInBlsDenyPkts": hwSecStatZoneInBlsDenyPkts,
       "hwSecStatZoneInDftAclDenyPkts": hwSecStatZoneInDftAclDenyPkts,
       "hwSecStatZoneInDftAclDenyIcmpPkts": hwSecStatZoneInDftAclDenyIcmpPkts,
       "hwSecStatZoneInIcmpFloodDropPkts": hwSecStatZoneInIcmpFloodDropPkts,
       "hwSecStatZoneInUdpFloodDropPkts": hwSecStatZoneInUdpFloodDropPkts,
       "hwSecStatZoneInFtpPkts": hwSecStatZoneInFtpPkts,
       "hwSecStatZoneInSmtpPkts": hwSecStatZoneInSmtpPkts,
       "hwSecStatZoneInHttpPkts": hwSecStatZoneInHttpPkts,
       "hwSecStatZoneInH323Pkts": hwSecStatZoneInH323Pkts,
       "hwSecStatZoneInRtspPkts": hwSecStatZoneInRtspPkts,
       "hwSecStatZoneOutTcpSess": hwSecStatZoneOutTcpSess,
       "hwSecStatZoneOutUdpSess": hwSecStatZoneOutUdpSess,
       "hwSecStatZoneOutIcmpSess": hwSecStatZoneOutIcmpSess,
       "hwSecStatZoneOutConn": hwSecStatZoneOutConn,
       "hwSecStatZoneOutHalfConn": hwSecStatZoneOutHalfConn,
       "hwSecStatZoneOutTcpSessSpeed": hwSecStatZoneOutTcpSessSpeed,
       "hwSecStatZoneOutUdpSessSpeed": hwSecStatZoneOutUdpSessSpeed,
       "hwSecStatZoneOutIcmpSessSpeed": hwSecStatZoneOutIcmpSessSpeed,
       "hwSecStatZoneOutConnSpeed": hwSecStatZoneOutConnSpeed,
       "hwSecStatZoneOutHalfConnSpeed": hwSecStatZoneOutHalfConnSpeed,
       "hwSecStatZoneOutAclDenyIcmpPkts": hwSecStatZoneOutAclDenyIcmpPkts,
       "hwSecStatZoneOutAclDenyIcmpOcts": hwSecStatZoneOutAclDenyIcmpOcts,
       "hwSecStatZoneOutAclDenyNonIcmpPkts": hwSecStatZoneOutAclDenyNonIcmpPkts,
       "hwSecStatZoneOutAclDenyNonIcmpOcts": hwSecStatZoneOutAclDenyNonIcmpOcts,
       "hwSecStatZoneOutBlsDenyPkts": hwSecStatZoneOutBlsDenyPkts,
       "hwSecStatZoneOutDftAclDenyPkts": hwSecStatZoneOutDftAclDenyPkts,
       "hwSecStatZoneOutDftAclDenyIcmpPkts": hwSecStatZoneOutDftAclDenyIcmpPkts,
       "hwSecStatZoneOutFtpPkts": hwSecStatZoneOutFtpPkts,
       "hwSecStatZoneOutSmtpPkts": hwSecStatZoneOutSmtpPkts,
       "hwSecStatZoneOutHttpPkts": hwSecStatZoneOutHttpPkts,
       "hwSecStatZoneOutH323Pkts": hwSecStatZoneOutH323Pkts,
       "hwSecStatZoneOutRtspPkts": hwSecStatZoneOutRtspPkts,
       "hwSecStatClearZoneInfo": hwSecStatClearZoneInfo,
       "hwSECSTATEudmConformance": hwSECSTATEudmConformance,
       "hwSECSTATEudmCompliance": hwSECSTATEudmCompliance,
       "hwSECSTATEudmMibGroups": hwSECSTATEudmMibGroups,
       "hwSECSTATEudmZoneCfgGroup": hwSECSTATEudmZoneCfgGroup,
       "hwSECSTATEudmZoneMonitorGroup": hwSECSTATEudmZoneMonitorGroup}
)
