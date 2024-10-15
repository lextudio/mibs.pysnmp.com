# SNMP MIB module (HUAWEI-BRAS-SRVCFGINTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BRAS-SRVCFGINTERFACE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:12 2024
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

(hwBRASMib,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwBRASMib")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwBRASSrvcfgInterface = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwSrvcfgInterfaceMibObjects_ObjectIdentity = ObjectIdentity
hwSrvcfgInterfaceMibObjects = _HwSrvcfgInterfaceMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1)
)
_HwBRASIfCfgTable_Object = MibTable
hwBRASIfCfgTable = _HwBRASIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hwBRASIfCfgTable.setStatus("current")
_HwBRASIfCfgEntry_Object = MibTableRow
hwBRASIfCfgEntry = _HwBRASIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1)
)
hwBRASIfCfgEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgIfIndex"),
)
if mibBuilder.loadTexts:
    hwBRASIfCfgEntry.setStatus("current")
_HwBRASIfCfgIfIndex_Type = InterfaceIndex
_HwBRASIfCfgIfIndex_Object = MibTableColumn
hwBRASIfCfgIfIndex = _HwBRASIfCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 1),
    _HwBRASIfCfgIfIndex_Type()
)
hwBRASIfCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASIfCfgIfIndex.setStatus("current")


class _HwBRASIfCfgAccessType_Type(Integer32):
    """Custom type hwBRASIfCfgAccessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              6)
        )
    )
    namedValues = NamedValues(
        *(("interface", 0),
          ("l2leasedline", 2),
          ("l2subscriber", 1),
          ("l3leasedline", 3),
          ("l3subscriber", 6))
    )


_HwBRASIfCfgAccessType_Type.__name__ = "Integer32"
_HwBRASIfCfgAccessType_Object = MibTableColumn
hwBRASIfCfgAccessType = _HwBRASIfCfgAccessType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 2),
    _HwBRASIfCfgAccessType_Type()
)
hwBRASIfCfgAccessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgAccessType.setStatus("current")


class _HwBRASIfCfgBRASIfName_Type(DisplayString):
    """Custom type hwBRASIfCfgBRASIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASIfCfgBRASIfName_Type.__name__ = "DisplayString"
_HwBRASIfCfgBRASIfName_Object = MibTableColumn
hwBRASIfCfgBRASIfName = _HwBRASIfCfgBRASIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 3),
    _HwBRASIfCfgBRASIfName_Type()
)
hwBRASIfCfgBRASIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgBRASIfName.setStatus("current")


class _HwBRASIfCfgPreAuthDomain_Type(DisplayString):
    """Custom type hwBRASIfCfgPreAuthDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwBRASIfCfgPreAuthDomain_Type.__name__ = "DisplayString"
_HwBRASIfCfgPreAuthDomain_Object = MibTableColumn
hwBRASIfCfgPreAuthDomain = _HwBRASIfCfgPreAuthDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 4),
    _HwBRASIfCfgPreAuthDomain_Type()
)
hwBRASIfCfgPreAuthDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgPreAuthDomain.setStatus("current")


class _HwBRASIfCfgAuthDomain_Type(DisplayString):
    """Custom type hwBRASIfCfgAuthDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwBRASIfCfgAuthDomain_Type.__name__ = "DisplayString"
_HwBRASIfCfgAuthDomain_Object = MibTableColumn
hwBRASIfCfgAuthDomain = _HwBRASIfCfgAuthDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 5),
    _HwBRASIfCfgAuthDomain_Type()
)
hwBRASIfCfgAuthDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgAuthDomain.setStatus("current")


class _HwBRASIfCfgForceAuthDomain_Type(Integer32):
    """Custom type hwBRASIfCfgForceAuthDomain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("force", 1),
          ("none", 0),
          ("replace", 2))
    )


_HwBRASIfCfgForceAuthDomain_Type.__name__ = "Integer32"
_HwBRASIfCfgForceAuthDomain_Object = MibTableColumn
hwBRASIfCfgForceAuthDomain = _HwBRASIfCfgForceAuthDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 6),
    _HwBRASIfCfgForceAuthDomain_Type()
)
hwBRASIfCfgForceAuthDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgForceAuthDomain.setStatus("current")


class _HwBRASIfCfgAcctCpyRdSvr_Type(DisplayString):
    """Custom type hwBRASIfCfgAcctCpyRdSvr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASIfCfgAcctCpyRdSvr_Type.__name__ = "DisplayString"
_HwBRASIfCfgAcctCpyRdSvr_Object = MibTableColumn
hwBRASIfCfgAcctCpyRdSvr = _HwBRASIfCfgAcctCpyRdSvr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 7),
    _HwBRASIfCfgAcctCpyRdSvr_Type()
)
hwBRASIfCfgAcctCpyRdSvr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgAcctCpyRdSvr.setStatus("current")


class _HwBRASIfCfgAuthMethod_Type(Integer32):
    """Custom type hwBRASIfCfgAuthMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwBRASIfCfgAuthMethod_Type.__name__ = "Integer32"
_HwBRASIfCfgAuthMethod_Object = MibTableColumn
hwBRASIfCfgAuthMethod = _HwBRASIfCfgAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 8),
    _HwBRASIfCfgAuthMethod_Type()
)
hwBRASIfCfgAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgAuthMethod.setStatus("current")


class _HwBRASIfCfgNasPortType_Type(Integer32):
    """Custom type hwBRASIfCfgNasPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_HwBRASIfCfgNasPortType_Type.__name__ = "Integer32"
_HwBRASIfCfgNasPortType_Object = MibTableColumn
hwBRASIfCfgNasPortType = _HwBRASIfCfgNasPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 9),
    _HwBRASIfCfgNasPortType_Type()
)
hwBRASIfCfgNasPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgNasPortType.setStatus("current")


class _HwBRASIfCfgLeaseName_Type(DisplayString):
    """Custom type hwBRASIfCfgLeaseName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_HwBRASIfCfgLeaseName_Type.__name__ = "DisplayString"
_HwBRASIfCfgLeaseName_Object = MibTableColumn
hwBRASIfCfgLeaseName = _HwBRASIfCfgLeaseName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 10),
    _HwBRASIfCfgLeaseName_Type()
)
hwBRASIfCfgLeaseName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgLeaseName.setStatus("current")


class _HwBRASIfCfgLeasePwd_Type(DisplayString):
    """Custom type hwBRASIfCfgLeasePwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwBRASIfCfgLeasePwd_Type.__name__ = "DisplayString"
_HwBRASIfCfgLeasePwd_Object = MibTableColumn
hwBRASIfCfgLeasePwd = _HwBRASIfCfgLeasePwd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 11),
    _HwBRASIfCfgLeasePwd_Type()
)
hwBRASIfCfgLeasePwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgLeasePwd.setStatus("current")


class _HwBRASIfCfgArpInterval_Type(Integer32):
    """Custom type hwBRASIfCfgArpInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 121),
    )


_HwBRASIfCfgArpInterval_Type.__name__ = "Integer32"
_HwBRASIfCfgArpInterval_Object = MibTableColumn
hwBRASIfCfgArpInterval = _HwBRASIfCfgArpInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 12),
    _HwBRASIfCfgArpInterval_Type()
)
hwBRASIfCfgArpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgArpInterval.setStatus("current")


class _HwBRASIfCfgArpFailTimes_Type(Integer32):
    """Custom type hwBRASIfCfgArpFailTimes based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 11),
    )


_HwBRASIfCfgArpFailTimes_Type.__name__ = "Integer32"
_HwBRASIfCfgArpFailTimes_Object = MibTableColumn
hwBRASIfCfgArpFailTimes = _HwBRASIfCfgArpFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 13),
    _HwBRASIfCfgArpFailTimes_Type()
)
hwBRASIfCfgArpFailTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgArpFailTimes.setStatus("current")


class _HwBRASIfCfgArpProxy_Type(TruthValue):
    """Custom type hwBRASIfCfgArpProxy based on TruthValue"""


_HwBRASIfCfgArpProxy_Object = MibTableColumn
hwBRASIfCfgArpProxy = _HwBRASIfCfgArpProxy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 14),
    _HwBRASIfCfgArpProxy_Type()
)
hwBRASIfCfgArpProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgArpProxy.setStatus("current")


class _HwBRASIfCfgRoamIsp_Type(TruthValue):
    """Custom type hwBRASIfCfgRoamIsp based on TruthValue"""


_HwBRASIfCfgRoamIsp_Object = MibTableColumn
hwBRASIfCfgRoamIsp = _HwBRASIfCfgRoamIsp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 15),
    _HwBRASIfCfgRoamIsp_Type()
)
hwBRASIfCfgRoamIsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgRoamIsp.setStatus("current")


class _HwBRASIfCfgDhcpBroadCast_Type(TruthValue):
    """Custom type hwBRASIfCfgDhcpBroadCast based on TruthValue"""


_HwBRASIfCfgDhcpBroadCast_Object = MibTableColumn
hwBRASIfCfgDhcpBroadCast = _HwBRASIfCfgDhcpBroadCast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 16),
    _HwBRASIfCfgDhcpBroadCast_Type()
)
hwBRASIfCfgDhcpBroadCast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgDhcpBroadCast.setStatus("current")


class _HwBRASIfCfgHostCar_Type(Integer32):
    """Custom type hwBRASIfCfgHostCar based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HwBRASIfCfgHostCar_Type.__name__ = "Integer32"
_HwBRASIfCfgHostCar_Object = MibTableColumn
hwBRASIfCfgHostCar = _HwBRASIfCfgHostCar_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 17),
    _HwBRASIfCfgHostCar_Type()
)
hwBRASIfCfgHostCar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgHostCar.setStatus("current")
_HwBRASIfCfgRowStatus_Type = RowStatus
_HwBRASIfCfgRowStatus_Object = MibTableColumn
hwBRASIfCfgRowStatus = _HwBRASIfCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 18),
    _HwBRASIfCfgRowStatus_Type()
)
hwBRASIfCfgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgRowStatus.setStatus("current")


class _HwBRASIfCfgEapTrigger_Type(TruthValue):
    """Custom type hwBRASIfCfgEapTrigger based on TruthValue"""


_HwBRASIfCfgEapTrigger_Object = MibTableColumn
hwBRASIfCfgEapTrigger = _HwBRASIfCfgEapTrigger_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 19),
    _HwBRASIfCfgEapTrigger_Type()
)
hwBRASIfCfgEapTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgEapTrigger.setStatus("current")


class _HwBRASIfCfgWlanSwitch_Type(Integer32):
    """Custom type hwBRASIfCfgWlanSwitch based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwBRASIfCfgWlanSwitch_Type.__name__ = "Integer32"
_HwBRASIfCfgWlanSwitch_Object = MibTableColumn
hwBRASIfCfgWlanSwitch = _HwBRASIfCfgWlanSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 20),
    _HwBRASIfCfgWlanSwitch_Type()
)
hwBRASIfCfgWlanSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgWlanSwitch.setStatus("current")


class _HwBRASIfCfgWlanAuthorization_Type(TruthValue):
    """Custom type hwBRASIfCfgWlanAuthorization based on TruthValue"""


_HwBRASIfCfgWlanAuthorization_Object = MibTableColumn
hwBRASIfCfgWlanAuthorization = _HwBRASIfCfgWlanAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 21),
    _HwBRASIfCfgWlanAuthorization_Type()
)
hwBRASIfCfgWlanAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgWlanAuthorization.setStatus("current")


class _HwBRASIfCfgDhcpShortLease_Type(Integer32):
    """Custom type hwBRASIfCfgDhcpShortLease based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 240),
    )


_HwBRASIfCfgDhcpShortLease_Type.__name__ = "Integer32"
_HwBRASIfCfgDhcpShortLease_Object = MibTableColumn
hwBRASIfCfgDhcpShortLease = _HwBRASIfCfgDhcpShortLease_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 22),
    _HwBRASIfCfgDhcpShortLease_Type()
)
hwBRASIfCfgDhcpShortLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgDhcpShortLease.setStatus("current")


class _HwBRASIfCfgRoamDomain_Type(DisplayString):
    """Custom type hwBRASIfCfgRoamDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwBRASIfCfgRoamDomain_Type.__name__ = "DisplayString"
_HwBRASIfCfgRoamDomain_Object = MibTableColumn
hwBRASIfCfgRoamDomain = _HwBRASIfCfgRoamDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 23),
    _HwBRASIfCfgRoamDomain_Type()
)
hwBRASIfCfgRoamDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgRoamDomain.setStatus("current")


class _HwBRASIfVsiName_Type(DisplayString):
    """Custom type hwBRASIfVsiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_HwBRASIfVsiName_Type.__name__ = "DisplayString"
_HwBRASIfVsiName_Object = MibTableColumn
hwBRASIfVsiName = _HwBRASIfVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 24),
    _HwBRASIfVsiName_Type()
)
hwBRASIfVsiName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfVsiName.setStatus("current")


class _HwBRASIfCfgOption82_Type(TruthValue):
    """Custom type hwBRASIfCfgOption82 based on TruthValue"""


_HwBRASIfCfgOption82_Object = MibTableColumn
hwBRASIfCfgOption82 = _HwBRASIfCfgOption82_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 25),
    _HwBRASIfCfgOption82_Type()
)
hwBRASIfCfgOption82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgOption82.setStatus("current")


class _HwBRASIfVpnInstance_Type(DisplayString):
    """Custom type hwBRASIfVpnInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwBRASIfVpnInstance_Type.__name__ = "DisplayString"
_HwBRASIfVpnInstance_Object = MibTableColumn
hwBRASIfVpnInstance = _HwBRASIfVpnInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 26),
    _HwBRASIfVpnInstance_Type()
)
hwBRASIfVpnInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfVpnInstance.setStatus("current")


class _HwBRASIfCopyMulticasePerUser_Type(TruthValue):
    """Custom type hwBRASIfCopyMulticasePerUser based on TruthValue"""


_HwBRASIfCopyMulticasePerUser_Object = MibTableColumn
hwBRASIfCopyMulticasePerUser = _HwBRASIfCopyMulticasePerUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 27),
    _HwBRASIfCopyMulticasePerUser_Type()
)
hwBRASIfCopyMulticasePerUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCopyMulticasePerUser.setStatus("current")


class _HwBRASIfCfgNDProxy_Type(TruthValue):
    """Custom type hwBRASIfCfgNDProxy based on TruthValue"""


_HwBRASIfCfgNDProxy_Object = MibTableColumn
hwBRASIfCfgNDProxy = _HwBRASIfCfgNDProxy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 28),
    _HwBRASIfCfgNDProxy_Type()
)
hwBRASIfCfgNDProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgNDProxy.setStatus("current")
_HwBRASIfCfgVBasMAC_Type = MacAddress
_HwBRASIfCfgVBasMAC_Object = MibTableColumn
hwBRASIfCfgVBasMAC = _HwBRASIfCfgVBasMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 29),
    _HwBRASIfCfgVBasMAC_Type()
)
hwBRASIfCfgVBasMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgVBasMAC.setStatus("current")


class _HwBRASIfCfgVBasAuthMode_Type(Integer32):
    """Custom type hwBRASIfCfgVBasAuthMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 0),
          ("reject", 1))
    )


_HwBRASIfCfgVBasAuthMode_Type.__name__ = "Integer32"
_HwBRASIfCfgVBasAuthMode_Object = MibTableColumn
hwBRASIfCfgVBasAuthMode = _HwBRASIfCfgVBasAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 30),
    _HwBRASIfCfgVBasAuthMode_Type()
)
hwBRASIfCfgVBasAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgVBasAuthMode.setStatus("current")


class _HwBRASIfCfgPermitDomain1_Type(DisplayString):
    """Custom type hwBRASIfCfgPermitDomain1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwBRASIfCfgPermitDomain1_Type.__name__ = "DisplayString"
_HwBRASIfCfgPermitDomain1_Object = MibTableColumn
hwBRASIfCfgPermitDomain1 = _HwBRASIfCfgPermitDomain1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 31),
    _HwBRASIfCfgPermitDomain1_Type()
)
hwBRASIfCfgPermitDomain1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgPermitDomain1.setStatus("current")


class _HwBRASIfCfgPermitDomain2_Type(DisplayString):
    """Custom type hwBRASIfCfgPermitDomain2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwBRASIfCfgPermitDomain2_Type.__name__ = "DisplayString"
_HwBRASIfCfgPermitDomain2_Object = MibTableColumn
hwBRASIfCfgPermitDomain2 = _HwBRASIfCfgPermitDomain2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 32),
    _HwBRASIfCfgPermitDomain2_Type()
)
hwBRASIfCfgPermitDomain2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgPermitDomain2.setStatus("current")


class _HwBRASIfCfgPermitDomain3_Type(DisplayString):
    """Custom type hwBRASIfCfgPermitDomain3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwBRASIfCfgPermitDomain3_Type.__name__ = "DisplayString"
_HwBRASIfCfgPermitDomain3_Object = MibTableColumn
hwBRASIfCfgPermitDomain3 = _HwBRASIfCfgPermitDomain3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 33),
    _HwBRASIfCfgPermitDomain3_Type()
)
hwBRASIfCfgPermitDomain3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgPermitDomain3.setStatus("current")


class _HwBRASIfCfgPermitDomain4_Type(DisplayString):
    """Custom type hwBRASIfCfgPermitDomain4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwBRASIfCfgPermitDomain4_Type.__name__ = "DisplayString"
_HwBRASIfCfgPermitDomain4_Object = MibTableColumn
hwBRASIfCfgPermitDomain4 = _HwBRASIfCfgPermitDomain4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 34),
    _HwBRASIfCfgPermitDomain4_Type()
)
hwBRASIfCfgPermitDomain4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgPermitDomain4.setStatus("current")


class _HwBRASIfCfgAccessDelayType_Type(Integer32):
    """Custom type hwBRASIfCfgAccessDelayType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("according-ani", 2),
          ("according-mac", 3),
          ("none", 0),
          ("termless", 1))
    )


_HwBRASIfCfgAccessDelayType_Type.__name__ = "Integer32"
_HwBRASIfCfgAccessDelayType_Object = MibTableColumn
hwBRASIfCfgAccessDelayType = _HwBRASIfCfgAccessDelayType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 35),
    _HwBRASIfCfgAccessDelayType_Type()
)
hwBRASIfCfgAccessDelayType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgAccessDelayType.setStatus("current")


class _HwBRASIfCfgTermlessDelayTime_Type(Integer32):
    """Custom type hwBRASIfCfgTermlessDelayTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwBRASIfCfgTermlessDelayTime_Type.__name__ = "Integer32"
_HwBRASIfCfgTermlessDelayTime_Object = MibTableColumn
hwBRASIfCfgTermlessDelayTime = _HwBRASIfCfgTermlessDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 36),
    _HwBRASIfCfgTermlessDelayTime_Type()
)
hwBRASIfCfgTermlessDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgTermlessDelayTime.setStatus("current")


class _HwBRASIfCfgOddMacDelayTime_Type(Integer32):
    """Custom type hwBRASIfCfgOddMacDelayTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwBRASIfCfgOddMacDelayTime_Type.__name__ = "Integer32"
_HwBRASIfCfgOddMacDelayTime_Object = MibTableColumn
hwBRASIfCfgOddMacDelayTime = _HwBRASIfCfgOddMacDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 37),
    _HwBRASIfCfgOddMacDelayTime_Type()
)
hwBRASIfCfgOddMacDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgOddMacDelayTime.setStatus("current")


class _HwBRASIfCfgEvenMacDelayTime_Type(Integer32):
    """Custom type hwBRASIfCfgEvenMacDelayTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwBRASIfCfgEvenMacDelayTime_Type.__name__ = "Integer32"
_HwBRASIfCfgEvenMacDelayTime_Object = MibTableColumn
hwBRASIfCfgEvenMacDelayTime = _HwBRASIfCfgEvenMacDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 38),
    _HwBRASIfCfgEvenMacDelayTime_Type()
)
hwBRASIfCfgEvenMacDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgEvenMacDelayTime.setStatus("current")


class _HwBRASIfCfgAccessNodeIdentify_Type(DisplayString):
    """Custom type hwBRASIfCfgAccessNodeIdentify based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASIfCfgAccessNodeIdentify_Type.__name__ = "DisplayString"
_HwBRASIfCfgAccessNodeIdentify_Object = MibTableColumn
hwBRASIfCfgAccessNodeIdentify = _HwBRASIfCfgAccessNodeIdentify_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 39),
    _HwBRASIfCfgAccessNodeIdentify_Type()
)
hwBRASIfCfgAccessNodeIdentify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgAccessNodeIdentify.setStatus("current")


class _HwBRASIfCfgAniDelayTime_Type(Integer32):
    """Custom type hwBRASIfCfgAniDelayTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwBRASIfCfgAniDelayTime_Type.__name__ = "Integer32"
_HwBRASIfCfgAniDelayTime_Object = MibTableColumn
hwBRASIfCfgAniDelayTime = _HwBRASIfCfgAniDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 40),
    _HwBRASIfCfgAniDelayTime_Type()
)
hwBRASIfCfgAniDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgAniDelayTime.setStatus("current")


class _HwBRASIfCfgRemoteBackupProfile_Type(DisplayString):
    """Custom type hwBRASIfCfgRemoteBackupProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBRASIfCfgRemoteBackupProfile_Type.__name__ = "DisplayString"
_HwBRASIfCfgRemoteBackupProfile_Object = MibTableColumn
hwBRASIfCfgRemoteBackupProfile = _HwBRASIfCfgRemoteBackupProfile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 1, 1, 42),
    _HwBRASIfCfgRemoteBackupProfile_Type()
)
hwBRASIfCfgRemoteBackupProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfCfgRemoteBackupProfile.setStatus("current")
_HwBRASIfVlanTable_Object = MibTable
hwBRASIfVlanTable = _HwBRASIfVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hwBRASIfVlanTable.setStatus("current")
_HwBRASIfVlanEntry_Object = MibTableRow
hwBRASIfVlanEntry = _HwBRASIfVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 2, 1)
)
hwBRASIfVlanEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfVlanIfIndex"),
    (0, "HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfVlanVlanId"),
    (0, "HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfQinQVlanID"),
)
if mibBuilder.loadTexts:
    hwBRASIfVlanEntry.setStatus("current")
_HwBRASIfVlanIfIndex_Type = InterfaceIndex
_HwBRASIfVlanIfIndex_Object = MibTableColumn
hwBRASIfVlanIfIndex = _HwBRASIfVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 2, 1, 1),
    _HwBRASIfVlanIfIndex_Type()
)
hwBRASIfVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASIfVlanIfIndex.setStatus("current")


class _HwBRASIfVlanVlanId_Type(Integer32):
    """Custom type hwBRASIfVlanVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwBRASIfVlanVlanId_Type.__name__ = "Integer32"
_HwBRASIfVlanVlanId_Object = MibTableColumn
hwBRASIfVlanVlanId = _HwBRASIfVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 2, 1, 2),
    _HwBRASIfVlanVlanId_Type()
)
hwBRASIfVlanVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASIfVlanVlanId.setStatus("current")


class _HwBRASIfVlanVlanNumber_Type(Integer32):
    """Custom type hwBRASIfVlanVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwBRASIfVlanVlanNumber_Type.__name__ = "Integer32"
_HwBRASIfVlanVlanNumber_Object = MibTableColumn
hwBRASIfVlanVlanNumber = _HwBRASIfVlanVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 2, 1, 3),
    _HwBRASIfVlanVlanNumber_Type()
)
hwBRASIfVlanVlanNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfVlanVlanNumber.setStatus("current")


class _HwBRASIfVlanAccessLimit_Type(Integer32):
    """Custom type hwBRASIfVlanAccessLimit based on Integer32"""
    defaultValue = 49152

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49153),
    )


_HwBRASIfVlanAccessLimit_Type.__name__ = "Integer32"
_HwBRASIfVlanAccessLimit_Object = MibTableColumn
hwBRASIfVlanAccessLimit = _HwBRASIfVlanAccessLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 2, 1, 4),
    _HwBRASIfVlanAccessLimit_Type()
)
hwBRASIfVlanAccessLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfVlanAccessLimit.setStatus("current")


class _HwBRASIfVlanAccessNumber_Type(Integer32):
    """Custom type hwBRASIfVlanAccessNumber based on Integer32"""
    defaultValue = 49152

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49152),
    )


_HwBRASIfVlanAccessNumber_Type.__name__ = "Integer32"
_HwBRASIfVlanAccessNumber_Object = MibTableColumn
hwBRASIfVlanAccessNumber = _HwBRASIfVlanAccessNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 2, 1, 5),
    _HwBRASIfVlanAccessNumber_Type()
)
hwBRASIfVlanAccessNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASIfVlanAccessNumber.setStatus("current")


class _HwBRASIfVlanBlock_Type(TruthValue):
    """Custom type hwBRASIfVlanBlock based on TruthValue"""


_HwBRASIfVlanBlock_Object = MibTableColumn
hwBRASIfVlanBlock = _HwBRASIfVlanBlock_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 2, 1, 6),
    _HwBRASIfVlanBlock_Type()
)
hwBRASIfVlanBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfVlanBlock.setStatus("current")


class _HwBRASIfVlanDevAccessNumber_Type(Integer32):
    """Custom type hwBRASIfVlanDevAccessNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_HwBRASIfVlanDevAccessNumber_Type.__name__ = "Integer32"
_HwBRASIfVlanDevAccessNumber_Object = MibTableColumn
hwBRASIfVlanDevAccessNumber = _HwBRASIfVlanDevAccessNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 2, 1, 7),
    _HwBRASIfVlanDevAccessNumber_Type()
)
hwBRASIfVlanDevAccessNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASIfVlanDevAccessNumber.setStatus("current")


class _HwBRASIfVlanSchedulerVcName_Type(DisplayString):
    """Custom type hwBRASIfVlanSchedulerVcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwBRASIfVlanSchedulerVcName_Type.__name__ = "DisplayString"
_HwBRASIfVlanSchedulerVcName_Object = MibTableColumn
hwBRASIfVlanSchedulerVcName = _HwBRASIfVlanSchedulerVcName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 2, 1, 8),
    _HwBRASIfVlanSchedulerVcName_Type()
)
hwBRASIfVlanSchedulerVcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfVlanSchedulerVcName.setStatus("current")


class _HwBRASIfVlanSchedulerVcGroupName_Type(DisplayString):
    """Custom type hwBRASIfVlanSchedulerVcGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwBRASIfVlanSchedulerVcGroupName_Type.__name__ = "DisplayString"
_HwBRASIfVlanSchedulerVcGroupName_Object = MibTableColumn
hwBRASIfVlanSchedulerVcGroupName = _HwBRASIfVlanSchedulerVcGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 2, 1, 9),
    _HwBRASIfVlanSchedulerVcGroupName_Type()
)
hwBRASIfVlanSchedulerVcGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfVlanSchedulerVcGroupName.setStatus("current")


class _HwBRASIfVlanSchedulerVpGroupName_Type(DisplayString):
    """Custom type hwBRASIfVlanSchedulerVpGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwBRASIfVlanSchedulerVpGroupName_Type.__name__ = "DisplayString"
_HwBRASIfVlanSchedulerVpGroupName_Object = MibTableColumn
hwBRASIfVlanSchedulerVpGroupName = _HwBRASIfVlanSchedulerVpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 2, 1, 10),
    _HwBRASIfVlanSchedulerVpGroupName_Type()
)
hwBRASIfVlanSchedulerVpGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfVlanSchedulerVpGroupName.setStatus("current")


class _HwBRASIfQinQVlanID_Type(Integer32):
    """Custom type hwBRASIfQinQVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwBRASIfQinQVlanID_Type.__name__ = "Integer32"
_HwBRASIfQinQVlanID_Object = MibTableColumn
hwBRASIfQinQVlanID = _HwBRASIfQinQVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 2, 1, 11),
    _HwBRASIfQinQVlanID_Type()
)
hwBRASIfQinQVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASIfQinQVlanID.setStatus("current")
_HwBRASIfPvcTable_Object = MibTable
hwBRASIfPvcTable = _HwBRASIfPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hwBRASIfPvcTable.setStatus("current")
_HwBRASIfPvcEntry_Object = MibTableRow
hwBRASIfPvcEntry = _HwBRASIfPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 3, 1)
)
hwBRASIfPvcEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfPvcIfIndex"),
    (0, "HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfPvcVpi"),
    (0, "HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfPvcVci"),
)
if mibBuilder.loadTexts:
    hwBRASIfPvcEntry.setStatus("current")
_HwBRASIfPvcIfIndex_Type = InterfaceIndex
_HwBRASIfPvcIfIndex_Object = MibTableColumn
hwBRASIfPvcIfIndex = _HwBRASIfPvcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 3, 1, 1),
    _HwBRASIfPvcIfIndex_Type()
)
hwBRASIfPvcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASIfPvcIfIndex.setStatus("current")


class _HwBRASIfPvcVpi_Type(Integer32):
    """Custom type hwBRASIfPvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwBRASIfPvcVpi_Type.__name__ = "Integer32"
_HwBRASIfPvcVpi_Object = MibTableColumn
hwBRASIfPvcVpi = _HwBRASIfPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 3, 1, 2),
    _HwBRASIfPvcVpi_Type()
)
hwBRASIfPvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASIfPvcVpi.setStatus("current")


class _HwBRASIfPvcVci_Type(Integer32):
    """Custom type hwBRASIfPvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_HwBRASIfPvcVci_Type.__name__ = "Integer32"
_HwBRASIfPvcVci_Object = MibTableColumn
hwBRASIfPvcVci = _HwBRASIfPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 3, 1, 3),
    _HwBRASIfPvcVci_Type()
)
hwBRASIfPvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASIfPvcVci.setStatus("current")


class _HwBRASIfPvcPvcNumber_Type(Integer32):
    """Custom type hwBRASIfPvcPvcNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwBRASIfPvcPvcNumber_Type.__name__ = "Integer32"
_HwBRASIfPvcPvcNumber_Object = MibTableColumn
hwBRASIfPvcPvcNumber = _HwBRASIfPvcPvcNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 3, 1, 4),
    _HwBRASIfPvcPvcNumber_Type()
)
hwBRASIfPvcPvcNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfPvcPvcNumber.setStatus("current")


class _HwBRASIfPvcAccessLimit_Type(Integer32):
    """Custom type hwBRASIfPvcAccessLimit based on Integer32"""
    defaultValue = 49152

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49153),
    )


_HwBRASIfPvcAccessLimit_Type.__name__ = "Integer32"
_HwBRASIfPvcAccessLimit_Object = MibTableColumn
hwBRASIfPvcAccessLimit = _HwBRASIfPvcAccessLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 3, 1, 5),
    _HwBRASIfPvcAccessLimit_Type()
)
hwBRASIfPvcAccessLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfPvcAccessLimit.setStatus("current")


class _HwBRASIfPvcAccessNumber_Type(Integer32):
    """Custom type hwBRASIfPvcAccessNumber based on Integer32"""
    defaultValue = 49152

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49152),
    )


_HwBRASIfPvcAccessNumber_Type.__name__ = "Integer32"
_HwBRASIfPvcAccessNumber_Object = MibTableColumn
hwBRASIfPvcAccessNumber = _HwBRASIfPvcAccessNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 3, 1, 6),
    _HwBRASIfPvcAccessNumber_Type()
)
hwBRASIfPvcAccessNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASIfPvcAccessNumber.setStatus("current")


class _HwBRASIfPvcBlock_Type(TruthValue):
    """Custom type hwBRASIfPvcBlock based on TruthValue"""


_HwBRASIfPvcBlock_Object = MibTableColumn
hwBRASIfPvcBlock = _HwBRASIfPvcBlock_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 3, 1, 7),
    _HwBRASIfPvcBlock_Type()
)
hwBRASIfPvcBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfPvcBlock.setStatus("current")


class _HwBRASIfPvcDevAccessNumber_Type(Integer32):
    """Custom type hwBRASIfPvcDevAccessNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_HwBRASIfPvcDevAccessNumber_Type.__name__ = "Integer32"
_HwBRASIfPvcDevAccessNumber_Object = MibTableColumn
hwBRASIfPvcDevAccessNumber = _HwBRASIfPvcDevAccessNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 3, 1, 8),
    _HwBRASIfPvcDevAccessNumber_Type()
)
hwBRASIfPvcDevAccessNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASIfPvcDevAccessNumber.setStatus("current")


class _HwBRASIfPvcSchedulerVcGroupName_Type(DisplayString):
    """Custom type hwBRASIfPvcSchedulerVcGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwBRASIfPvcSchedulerVcGroupName_Type.__name__ = "DisplayString"
_HwBRASIfPvcSchedulerVcGroupName_Object = MibTableColumn
hwBRASIfPvcSchedulerVcGroupName = _HwBRASIfPvcSchedulerVcGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 3, 1, 9),
    _HwBRASIfPvcSchedulerVcGroupName_Type()
)
hwBRASIfPvcSchedulerVcGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfPvcSchedulerVcGroupName.setStatus("current")


class _HwBRASIfPvcSchedulerVpGroupName_Type(DisplayString):
    """Custom type hwBRASIfPvcSchedulerVpGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwBRASIfPvcSchedulerVpGroupName_Type.__name__ = "DisplayString"
_HwBRASIfPvcSchedulerVpGroupName_Object = MibTableColumn
hwBRASIfPvcSchedulerVpGroupName = _HwBRASIfPvcSchedulerVpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 3, 1, 10),
    _HwBRASIfPvcSchedulerVpGroupName_Type()
)
hwBRASIfPvcSchedulerVpGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBRASIfPvcSchedulerVpGroupName.setStatus("current")
_HwSTPRelayTable_Object = MibTable
hwSTPRelayTable = _HwSTPRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hwSTPRelayTable.setStatus("current")
_HwSTPRelayEntry_Object = MibTableRow
hwSTPRelayEntry = _HwSTPRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 4, 1)
)
hwSTPRelayEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwSTPRelayIndex"),
)
if mibBuilder.loadTexts:
    hwSTPRelayEntry.setStatus("current")


class _HwSTPRelayIndex_Type(Integer32):
    """Custom type hwSTPRelayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_HwSTPRelayIndex_Type.__name__ = "Integer32"
_HwSTPRelayIndex_Object = MibTableColumn
hwSTPRelayIndex = _HwSTPRelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 4, 1, 1),
    _HwSTPRelayIndex_Type()
)
hwSTPRelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSTPRelayIndex.setStatus("current")
_HwSTPRelayInIfIndex_Type = InterfaceIndex
_HwSTPRelayInIfIndex_Object = MibTableColumn
hwSTPRelayInIfIndex = _HwSTPRelayInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 4, 1, 2),
    _HwSTPRelayInIfIndex_Type()
)
hwSTPRelayInIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSTPRelayInIfIndex.setStatus("current")
_HwSTPRelayOutIfIndex_Type = InterfaceIndex
_HwSTPRelayOutIfIndex_Object = MibTableColumn
hwSTPRelayOutIfIndex = _HwSTPRelayOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 4, 1, 3),
    _HwSTPRelayOutIfIndex_Type()
)
hwSTPRelayOutIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSTPRelayOutIfIndex.setStatus("current")
_HwSTPRelayRowStatus_Type = RowStatus
_HwSTPRelayRowStatus_Object = MibTableColumn
hwSTPRelayRowStatus = _HwSTPRelayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 4, 1, 4),
    _HwSTPRelayRowStatus_Type()
)
hwSTPRelayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSTPRelayRowStatus.setStatus("current")


class _HwSTPRelayInIfName_Type(DisplayString):
    """Custom type hwSTPRelayInIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_HwSTPRelayInIfName_Type.__name__ = "DisplayString"
_HwSTPRelayInIfName_Object = MibTableColumn
hwSTPRelayInIfName = _HwSTPRelayInIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 4, 1, 5),
    _HwSTPRelayInIfName_Type()
)
hwSTPRelayInIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSTPRelayInIfName.setStatus("current")


class _HwSTPRelayOutIfName_Type(DisplayString):
    """Custom type hwSTPRelayOutIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_HwSTPRelayOutIfName_Type.__name__ = "DisplayString"
_HwSTPRelayOutIfName_Object = MibTableColumn
hwSTPRelayOutIfName = _HwSTPRelayOutIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 4, 1, 6),
    _HwSTPRelayOutIfName_Type()
)
hwSTPRelayOutIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSTPRelayOutIfName.setStatus("current")
_HwSTPRelayInMac_Type = MacAddress
_HwSTPRelayInMac_Object = MibTableColumn
hwSTPRelayInMac = _HwSTPRelayInMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 4, 1, 7),
    _HwSTPRelayInMac_Type()
)
hwSTPRelayInMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSTPRelayInMac.setStatus("current")
_HwSTPRelayOutMac_Type = MacAddress
_HwSTPRelayOutMac_Object = MibTableColumn
hwSTPRelayOutMac = _HwSTPRelayOutMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 4, 1, 8),
    _HwSTPRelayOutMac_Type()
)
hwSTPRelayOutMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSTPRelayOutMac.setStatus("current")
_HwPortAccessLimitTable_Object = MibTable
hwPortAccessLimitTable = _HwPortAccessLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hwPortAccessLimitTable.setStatus("current")
_HwPortAccessLimitEntry_Object = MibTableRow
hwPortAccessLimitEntry = _HwPortAccessLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 5, 1)
)
hwPortAccessLimitEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwPortAccessLimitIfIndex"),
)
if mibBuilder.loadTexts:
    hwPortAccessLimitEntry.setStatus("current")
_HwPortAccessLimitIfIndex_Type = InterfaceIndex
_HwPortAccessLimitIfIndex_Object = MibTableColumn
hwPortAccessLimitIfIndex = _HwPortAccessLimitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 5, 1, 1),
    _HwPortAccessLimitIfIndex_Type()
)
hwPortAccessLimitIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortAccessLimitIfIndex.setStatus("current")


class _HwPortAccessLimitLimit_Type(Integer32):
    """Custom type hwPortAccessLimitLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49153),
    )


_HwPortAccessLimitLimit_Type.__name__ = "Integer32"
_HwPortAccessLimitLimit_Object = MibTableColumn
hwPortAccessLimitLimit = _HwPortAccessLimitLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 5, 1, 2),
    _HwPortAccessLimitLimit_Type()
)
hwPortAccessLimitLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortAccessLimitLimit.setStatus("current")


class _HwPortAccessLimitNumber_Type(Integer32):
    """Custom type hwPortAccessLimitNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49152),
    )


_HwPortAccessLimitNumber_Type.__name__ = "Integer32"
_HwPortAccessLimitNumber_Object = MibTableColumn
hwPortAccessLimitNumber = _HwPortAccessLimitNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 5, 1, 3),
    _HwPortAccessLimitNumber_Type()
)
hwPortAccessLimitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortAccessLimitNumber.setStatus("current")


class _HwPortAccessLimitDevNumber_Type(Integer32):
    """Custom type hwPortAccessLimitDevNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_HwPortAccessLimitDevNumber_Type.__name__ = "Integer32"
_HwPortAccessLimitDevNumber_Object = MibTableColumn
hwPortAccessLimitDevNumber = _HwPortAccessLimitDevNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 5, 1, 4),
    _HwPortAccessLimitDevNumber_Type()
)
hwPortAccessLimitDevNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortAccessLimitDevNumber.setStatus("current")
_HwL3SubscriberIspTable_Object = MibTable
hwL3SubscriberIspTable = _HwL3SubscriberIspTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hwL3SubscriberIspTable.setStatus("current")
_HwL3SubscriberIspEntry_Object = MibTableRow
hwL3SubscriberIspEntry = _HwL3SubscriberIspEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 6, 1)
)
hwL3SubscriberIspEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwL3SubscriberIspStartIp"),
    (0, "HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwL3SubscriberIspVpnId"),
)
if mibBuilder.loadTexts:
    hwL3SubscriberIspEntry.setStatus("current")
_HwL3SubscriberIspStartIp_Type = IpAddress
_HwL3SubscriberIspStartIp_Object = MibTableColumn
hwL3SubscriberIspStartIp = _HwL3SubscriberIspStartIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 6, 1, 1),
    _HwL3SubscriberIspStartIp_Type()
)
hwL3SubscriberIspStartIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3SubscriberIspStartIp.setStatus("current")


class _HwL3SubscriberIspVpnId_Type(DisplayString):
    """Custom type hwL3SubscriberIspVpnId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_HwL3SubscriberIspVpnId_Type.__name__ = "DisplayString"
_HwL3SubscriberIspVpnId_Object = MibTableColumn
hwL3SubscriberIspVpnId = _HwL3SubscriberIspVpnId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 6, 1, 2),
    _HwL3SubscriberIspVpnId_Type()
)
hwL3SubscriberIspVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3SubscriberIspVpnId.setStatus("current")
_HwL3SubscriberIspEndIp_Type = IpAddress
_HwL3SubscriberIspEndIp_Object = MibTableColumn
hwL3SubscriberIspEndIp = _HwL3SubscriberIspEndIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 6, 1, 3),
    _HwL3SubscriberIspEndIp_Type()
)
hwL3SubscriberIspEndIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL3SubscriberIspEndIp.setStatus("current")


class _HwL3SubscriberIspDomainName_Type(DisplayString):
    """Custom type hwL3SubscriberIspDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwL3SubscriberIspDomainName_Type.__name__ = "DisplayString"
_HwL3SubscriberIspDomainName_Object = MibTableColumn
hwL3SubscriberIspDomainName = _HwL3SubscriberIspDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 6, 1, 4),
    _HwL3SubscriberIspDomainName_Type()
)
hwL3SubscriberIspDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL3SubscriberIspDomainName.setStatus("current")
_HwL3SubscriberIspRowStatus_Type = RowStatus
_HwL3SubscriberIspRowStatus_Object = MibTableColumn
hwL3SubscriberIspRowStatus = _HwL3SubscriberIspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 6, 1, 5),
    _HwL3SubscriberIspRowStatus_Type()
)
hwL3SubscriberIspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL3SubscriberIspRowStatus.setStatus("current")
_SrvcfgScalar_ObjectIdentity = ObjectIdentity
srvcfgScalar = _SrvcfgScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 8)
)
_HwDhcpOption60DomainInclude_Type = TruthValue
_HwDhcpOption60DomainInclude_Object = MibScalar
hwDhcpOption60DomainInclude = _HwDhcpOption60DomainInclude_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 8, 1),
    _HwDhcpOption60DomainInclude_Type()
)
hwDhcpOption60DomainInclude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpOption60DomainInclude.setStatus("current")
_HwDhcpOption60PartialMatch_Type = TruthValue
_HwDhcpOption60PartialMatch_Object = MibScalar
hwDhcpOption60PartialMatch = _HwDhcpOption60PartialMatch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 8, 2),
    _HwDhcpOption60PartialMatch_Type()
)
hwDhcpOption60PartialMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpOption60PartialMatch.setStatus("current")
_HwConnTimeOutTable_ObjectIdentity = ObjectIdentity
hwConnTimeOutTable = _HwConnTimeOutTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 9)
)


class _HwConnTimeOutTcp_Type(Integer32):
    """Custom type hwConnTimeOutTcp based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwConnTimeOutTcp_Type.__name__ = "Integer32"
_HwConnTimeOutTcp_Object = MibScalar
hwConnTimeOutTcp = _HwConnTimeOutTcp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 9, 1),
    _HwConnTimeOutTcp_Type()
)
hwConnTimeOutTcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwConnTimeOutTcp.setStatus("current")


class _HwConnTimeOutUdp_Type(Integer32):
    """Custom type hwConnTimeOutUdp based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwConnTimeOutUdp_Type.__name__ = "Integer32"
_HwConnTimeOutUdp_Object = MibScalar
hwConnTimeOutUdp = _HwConnTimeOutUdp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 9, 2),
    _HwConnTimeOutUdp_Type()
)
hwConnTimeOutUdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwConnTimeOutUdp.setStatus("current")
_HwBRASIfVlanNumTable_Object = MibTable
hwBRASIfVlanNumTable = _HwBRASIfVlanNumTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 10)
)
if mibBuilder.loadTexts:
    hwBRASIfVlanNumTable.setStatus("current")
_HwBRASIfVlanNumEntry_Object = MibTableRow
hwBRASIfVlanNumEntry = _HwBRASIfVlanNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 10, 1)
)
hwBRASIfVlanNumEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfSlot"),
)
if mibBuilder.loadTexts:
    hwBRASIfVlanNumEntry.setStatus("current")


class _HwBRASIfSlot_Type(Integer32):
    """Custom type hwBRASIfSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HwBRASIfSlot_Type.__name__ = "Integer32"
_HwBRASIfSlot_Object = MibTableColumn
hwBRASIfSlot = _HwBRASIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 10, 1, 1),
    _HwBRASIfSlot_Type()
)
hwBRASIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASIfSlot.setStatus("current")


class _HwBRASSlotVlanNum_Type(Integer32):
    """Custom type hwBRASSlotVlanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_HwBRASSlotVlanNum_Type.__name__ = "Integer32"
_HwBRASSlotVlanNum_Object = MibTableColumn
hwBRASSlotVlanNum = _HwBRASSlotVlanNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 10, 1, 2),
    _HwBRASSlotVlanNum_Type()
)
hwBRASSlotVlanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASSlotVlanNum.setStatus("current")


class _HwBRASSLotStaticVlanNum_Type(Integer32):
    """Custom type hwBRASSLotStaticVlanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_HwBRASSLotStaticVlanNum_Type.__name__ = "Integer32"
_HwBRASSLotStaticVlanNum_Object = MibTableColumn
hwBRASSLotStaticVlanNum = _HwBRASSLotStaticVlanNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 10, 1, 3),
    _HwBRASSLotStaticVlanNum_Type()
)
hwBRASSLotStaticVlanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBRASSLotStaticVlanNum.setStatus("current")
_HwServiceIfCfgTable_Object = MibTable
hwServiceIfCfgTable = _HwServiceIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 11)
)
if mibBuilder.loadTexts:
    hwServiceIfCfgTable.setStatus("current")
_HwServiceIfCfgEntry_Object = MibTableRow
hwServiceIfCfgEntry = _HwServiceIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 11, 1)
)
hwServiceIfCfgEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwServiceIfCfgIfIndex"),
)
if mibBuilder.loadTexts:
    hwServiceIfCfgEntry.setStatus("current")
_HwServiceIfCfgIfIndex_Type = InterfaceIndex
_HwServiceIfCfgIfIndex_Object = MibTableColumn
hwServiceIfCfgIfIndex = _HwServiceIfCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 11, 1, 1),
    _HwServiceIfCfgIfIndex_Type()
)
hwServiceIfCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwServiceIfCfgIfIndex.setStatus("current")


class _HwServiceIfCfgIdentificationMode_Type(Integer32):
    """Custom type hwServiceIfCfgIdentificationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ceVlan", 3),
          ("host", 1),
          ("location", 2))
    )


_HwServiceIfCfgIdentificationMode_Type.__name__ = "Integer32"
_HwServiceIfCfgIdentificationMode_Object = MibTableColumn
hwServiceIfCfgIdentificationMode = _HwServiceIfCfgIdentificationMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 11, 1, 2),
    _HwServiceIfCfgIdentificationMode_Type()
)
hwServiceIfCfgIdentificationMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwServiceIfCfgIdentificationMode.setStatus("current")


class _HwServiceIfCfgDomain_Type(DisplayString):
    """Custom type hwServiceIfCfgDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_HwServiceIfCfgDomain_Type.__name__ = "DisplayString"
_HwServiceIfCfgDomain_Object = MibTableColumn
hwServiceIfCfgDomain = _HwServiceIfCfgDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 11, 1, 3),
    _HwServiceIfCfgDomain_Type()
)
hwServiceIfCfgDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwServiceIfCfgDomain.setStatus("current")


class _HwServiceIfCfgUserName_Type(DisplayString):
    """Custom type hwServiceIfCfgUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwServiceIfCfgUserName_Type.__name__ = "DisplayString"
_HwServiceIfCfgUserName_Object = MibTableColumn
hwServiceIfCfgUserName = _HwServiceIfCfgUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 11, 1, 4),
    _HwServiceIfCfgUserName_Type()
)
hwServiceIfCfgUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwServiceIfCfgUserName.setStatus("current")


class _HwServiceIfCfgPassword_Type(DisplayString):
    """Custom type hwServiceIfCfgPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwServiceIfCfgPassword_Type.__name__ = "DisplayString"
_HwServiceIfCfgPassword_Object = MibTableColumn
hwServiceIfCfgPassword = _HwServiceIfCfgPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 11, 1, 5),
    _HwServiceIfCfgPassword_Type()
)
hwServiceIfCfgPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwServiceIfCfgPassword.setStatus("current")


class _HwServiceIfCfgDetectNum_Type(Integer32):
    """Custom type hwServiceIfCfgDetectNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_HwServiceIfCfgDetectNum_Type.__name__ = "Integer32"
_HwServiceIfCfgDetectNum_Object = MibTableColumn
hwServiceIfCfgDetectNum = _HwServiceIfCfgDetectNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 11, 1, 6),
    _HwServiceIfCfgDetectNum_Type()
)
hwServiceIfCfgDetectNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwServiceIfCfgDetectNum.setStatus("current")


class _HwServiceIfCfgDetectInterval_Type(Integer32):
    """Custom type hwServiceIfCfgDetectInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_HwServiceIfCfgDetectInterval_Type.__name__ = "Integer32"
_HwServiceIfCfgDetectInterval_Object = MibTableColumn
hwServiceIfCfgDetectInterval = _HwServiceIfCfgDetectInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 11, 1, 7),
    _HwServiceIfCfgDetectInterval_Type()
)
hwServiceIfCfgDetectInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwServiceIfCfgDetectInterval.setStatus("current")
_HwServiceIfCfgOption82_Type = TruthValue
_HwServiceIfCfgOption82_Object = MibTableColumn
hwServiceIfCfgOption82 = _HwServiceIfCfgOption82_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 11, 1, 8),
    _HwServiceIfCfgOption82_Type()
)
hwServiceIfCfgOption82.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwServiceIfCfgOption82.setStatus("current")


class _HwServiceIfCfgAccessLimit_Type(Integer32):
    """Custom type hwServiceIfCfgAccessLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_HwServiceIfCfgAccessLimit_Type.__name__ = "Integer32"
_HwServiceIfCfgAccessLimit_Object = MibTableColumn
hwServiceIfCfgAccessLimit = _HwServiceIfCfgAccessLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 11, 1, 9),
    _HwServiceIfCfgAccessLimit_Type()
)
hwServiceIfCfgAccessLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwServiceIfCfgAccessLimit.setStatus("current")
_HwServiceIfCfgOption60_Type = TruthValue
_HwServiceIfCfgOption60_Object = MibTableColumn
hwServiceIfCfgOption60 = _HwServiceIfCfgOption60_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 11, 1, 10),
    _HwServiceIfCfgOption60_Type()
)
hwServiceIfCfgOption60.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwServiceIfCfgOption60.setStatus("current")


class _HwServiceIfCfgIpTriggerEnable_Type(EnabledStatus):
    """Custom type hwServiceIfCfgIpTriggerEnable based on EnabledStatus"""


_HwServiceIfCfgIpTriggerEnable_Object = MibTableColumn
hwServiceIfCfgIpTriggerEnable = _HwServiceIfCfgIpTriggerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 11, 1, 11),
    _HwServiceIfCfgIpTriggerEnable_Type()
)
hwServiceIfCfgIpTriggerEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwServiceIfCfgIpTriggerEnable.setStatus("current")


class _HwServiceIfCfgArpTriggerEnable_Type(EnabledStatus):
    """Custom type hwServiceIfCfgArpTriggerEnable based on EnabledStatus"""


_HwServiceIfCfgArpTriggerEnable_Object = MibTableColumn
hwServiceIfCfgArpTriggerEnable = _HwServiceIfCfgArpTriggerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 11, 1, 12),
    _HwServiceIfCfgArpTriggerEnable_Type()
)
hwServiceIfCfgArpTriggerEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwServiceIfCfgArpTriggerEnable.setStatus("current")
_HwServiceIfCfgIfBlock_Type = TruthValue
_HwServiceIfCfgIfBlock_Object = MibTableColumn
hwServiceIfCfgIfBlock = _HwServiceIfCfgIfBlock_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 11, 1, 13),
    _HwServiceIfCfgIfBlock_Type()
)
hwServiceIfCfgIfBlock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwServiceIfCfgIfBlock.setStatus("current")


class _HwServiceIfCfgQosProfile_Type(DisplayString):
    """Custom type hwServiceIfCfgQosProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwServiceIfCfgQosProfile_Type.__name__ = "DisplayString"
_HwServiceIfCfgQosProfile_Object = MibTableColumn
hwServiceIfCfgQosProfile = _HwServiceIfCfgQosProfile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 11, 1, 14),
    _HwServiceIfCfgQosProfile_Type()
)
hwServiceIfCfgQosProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwServiceIfCfgQosProfile.setStatus("current")


class _HwServiceIfCfgBindingUserPasswordMode_Type(Integer32):
    """Custom type hwServiceIfCfgBindingUserPasswordMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cipher", 2),
          ("simple", 1))
    )


_HwServiceIfCfgBindingUserPasswordMode_Type.__name__ = "Integer32"
_HwServiceIfCfgBindingUserPasswordMode_Object = MibTableColumn
hwServiceIfCfgBindingUserPasswordMode = _HwServiceIfCfgBindingUserPasswordMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 11, 1, 15),
    _HwServiceIfCfgBindingUserPasswordMode_Type()
)
hwServiceIfCfgBindingUserPasswordMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwServiceIfCfgBindingUserPasswordMode.setStatus("current")


class _HwServiceIfCfgBindingUserNameFormat_Type(Integer32):
    """Custom type hwServiceIfCfgBindingUserNameFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_HwServiceIfCfgBindingUserNameFormat_Type.__name__ = "Integer32"
_HwServiceIfCfgBindingUserNameFormat_Object = MibTableColumn
hwServiceIfCfgBindingUserNameFormat = _HwServiceIfCfgBindingUserNameFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 11, 1, 16),
    _HwServiceIfCfgBindingUserNameFormat_Type()
)
hwServiceIfCfgBindingUserNameFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwServiceIfCfgBindingUserNameFormat.setStatus("current")


class _HwServiceIfCfgBindingUserPassword_Type(DisplayString):
    """Custom type hwServiceIfCfgBindingUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HwServiceIfCfgBindingUserPassword_Type.__name__ = "DisplayString"
_HwServiceIfCfgBindingUserPassword_Object = MibTableColumn
hwServiceIfCfgBindingUserPassword = _HwServiceIfCfgBindingUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 11, 1, 17),
    _HwServiceIfCfgBindingUserPassword_Type()
)
hwServiceIfCfgBindingUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwServiceIfCfgBindingUserPassword.setStatus("current")
_HwServiceIfCfgRowStatus_Type = RowStatus
_HwServiceIfCfgRowStatus_Object = MibTableColumn
hwServiceIfCfgRowStatus = _HwServiceIfCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 1, 11, 1, 18),
    _HwServiceIfCfgRowStatus_Type()
)
hwServiceIfCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwServiceIfCfgRowStatus.setStatus("current")
_HwSrvcfgInterfaceConformance_ObjectIdentity = ObjectIdentity
hwSrvcfgInterfaceConformance = _HwSrvcfgInterfaceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 2)
)
_HwSrvcfgInterfaceCompliances_ObjectIdentity = ObjectIdentity
hwSrvcfgInterfaceCompliances = _HwSrvcfgInterfaceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 2, 1)
)
_HwSrvcfgInterfaceGroups_ObjectIdentity = ObjectIdentity
hwSrvcfgInterfaceGroups = _HwSrvcfgInterfaceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 2, 2)
)

# Managed Objects groups

hwBRASIfCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 2, 2, 1)
)
hwBRASIfCfgGroup.setObjects(
      *(("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgAccessType"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgBRASIfName"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgPreAuthDomain"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgAuthDomain"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgForceAuthDomain"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgAcctCpyRdSvr"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgAuthMethod"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgNasPortType"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgLeaseName"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgLeasePwd"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgArpInterval"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgArpFailTimes"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgArpProxy"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgRoamIsp"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgDhcpBroadCast"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgHostCar"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgRowStatus"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgEapTrigger"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgWlanSwitch"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgWlanAuthorization"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgDhcpShortLease"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgRoamDomain"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfVsiName"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgOption82"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfVpnInstance"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCopyMulticasePerUser"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgNDProxy"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgVBasMAC"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgVBasAuthMode"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgPermitDomain1"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgPermitDomain2"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgPermitDomain3"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgPermitDomain4"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgAccessDelayType"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgTermlessDelayTime"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgOddMacDelayTime"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgEvenMacDelayTime"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgAccessNodeIdentify"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgAniDelayTime"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfCfgRemoteBackupProfile"))
)
if mibBuilder.loadTexts:
    hwBRASIfCfgGroup.setStatus("current")

hwBRASIfVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 2, 2, 2)
)
hwBRASIfVlanGroup.setObjects(
      *(("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfVlanVlanNumber"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfVlanAccessLimit"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfVlanAccessNumber"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfVlanBlock"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfVlanDevAccessNumber"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfVlanSchedulerVcName"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfVlanSchedulerVcGroupName"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfVlanSchedulerVpGroupName"))
)
if mibBuilder.loadTexts:
    hwBRASIfVlanGroup.setStatus("current")

hwBRASIfPvcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 2, 2, 3)
)
hwBRASIfPvcGroup.setObjects(
      *(("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfPvcPvcNumber"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfPvcAccessLimit"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfPvcAccessNumber"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfPvcBlock"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfPvcDevAccessNumber"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfPvcSchedulerVcGroupName"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASIfPvcSchedulerVpGroupName"))
)
if mibBuilder.loadTexts:
    hwBRASIfPvcGroup.setStatus("current")

hwSTPRelayServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 2, 2, 4)
)
hwSTPRelayServerGroup.setObjects(
      *(("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwSTPRelayInIfIndex"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwSTPRelayOutIfIndex"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwSTPRelayRowStatus"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwSTPRelayInIfName"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwSTPRelayOutIfName"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwSTPRelayInMac"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwSTPRelayOutMac"))
)
if mibBuilder.loadTexts:
    hwSTPRelayServerGroup.setStatus("current")

hwPortAccessLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 2, 2, 5)
)
hwPortAccessLimitGroup.setObjects(
      *(("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwPortAccessLimitLimit"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwPortAccessLimitNumber"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwPortAccessLimitDevNumber"))
)
if mibBuilder.loadTexts:
    hwPortAccessLimitGroup.setStatus("current")

hwL3SubscriberIspGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 2, 2, 6)
)
hwL3SubscriberIspGroup.setObjects(
      *(("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwL3SubscriberIspEndIp"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwL3SubscriberIspDomainName"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwL3SubscriberIspRowStatus"))
)
if mibBuilder.loadTexts:
    hwL3SubscriberIspGroup.setStatus("current")

hwConnTimeOutGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 2, 2, 7)
)
hwConnTimeOutGroup.setObjects(
      *(("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwConnTimeOutTcp"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwConnTimeOutUdp"))
)
if mibBuilder.loadTexts:
    hwConnTimeOutGroup.setStatus("current")

hwSrvcfgScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 2, 2, 8)
)
hwSrvcfgScalarGroup.setObjects(
      *(("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwDhcpOption60DomainInclude"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwDhcpOption60PartialMatch"))
)
if mibBuilder.loadTexts:
    hwSrvcfgScalarGroup.setStatus("current")

hwBRASIfVlanNumGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 2, 2, 9)
)
hwBRASIfVlanNumGroup.setObjects(
      *(("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASSlotVlanNum"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwBRASSLotStaticVlanNum"))
)
if mibBuilder.loadTexts:
    hwBRASIfVlanNumGroup.setStatus("current")

hwServiceIfCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 2, 2, 10)
)
hwServiceIfCfgGroup.setObjects(
      *(("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwServiceIfCfgIdentificationMode"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwServiceIfCfgDomain"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwServiceIfCfgUserName"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwServiceIfCfgPassword"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwServiceIfCfgDetectNum"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwServiceIfCfgDetectInterval"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwServiceIfCfgOption82"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwServiceIfCfgAccessLimit"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwServiceIfCfgOption60"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwServiceIfCfgIpTriggerEnable"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwServiceIfCfgArpTriggerEnable"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwServiceIfCfgIfBlock"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwServiceIfCfgQosProfile"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwServiceIfCfgBindingUserPasswordMode"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwServiceIfCfgBindingUserNameFormat"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwServiceIfCfgBindingUserPassword"),
        ("HUAWEI-BRAS-SRVCFGINTERFACE-MIB", "hwServiceIfCfgRowStatus"))
)
if mibBuilder.loadTexts:
    hwServiceIfCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwSrvcfgInterfaceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwSrvcfgInterfaceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BRAS-SRVCFGINTERFACE-MIB",
    **{"hwBRASSrvcfgInterface": hwBRASSrvcfgInterface,
       "hwSrvcfgInterfaceMibObjects": hwSrvcfgInterfaceMibObjects,
       "hwBRASIfCfgTable": hwBRASIfCfgTable,
       "hwBRASIfCfgEntry": hwBRASIfCfgEntry,
       "hwBRASIfCfgIfIndex": hwBRASIfCfgIfIndex,
       "hwBRASIfCfgAccessType": hwBRASIfCfgAccessType,
       "hwBRASIfCfgBRASIfName": hwBRASIfCfgBRASIfName,
       "hwBRASIfCfgPreAuthDomain": hwBRASIfCfgPreAuthDomain,
       "hwBRASIfCfgAuthDomain": hwBRASIfCfgAuthDomain,
       "hwBRASIfCfgForceAuthDomain": hwBRASIfCfgForceAuthDomain,
       "hwBRASIfCfgAcctCpyRdSvr": hwBRASIfCfgAcctCpyRdSvr,
       "hwBRASIfCfgAuthMethod": hwBRASIfCfgAuthMethod,
       "hwBRASIfCfgNasPortType": hwBRASIfCfgNasPortType,
       "hwBRASIfCfgLeaseName": hwBRASIfCfgLeaseName,
       "hwBRASIfCfgLeasePwd": hwBRASIfCfgLeasePwd,
       "hwBRASIfCfgArpInterval": hwBRASIfCfgArpInterval,
       "hwBRASIfCfgArpFailTimes": hwBRASIfCfgArpFailTimes,
       "hwBRASIfCfgArpProxy": hwBRASIfCfgArpProxy,
       "hwBRASIfCfgRoamIsp": hwBRASIfCfgRoamIsp,
       "hwBRASIfCfgDhcpBroadCast": hwBRASIfCfgDhcpBroadCast,
       "hwBRASIfCfgHostCar": hwBRASIfCfgHostCar,
       "hwBRASIfCfgRowStatus": hwBRASIfCfgRowStatus,
       "hwBRASIfCfgEapTrigger": hwBRASIfCfgEapTrigger,
       "hwBRASIfCfgWlanSwitch": hwBRASIfCfgWlanSwitch,
       "hwBRASIfCfgWlanAuthorization": hwBRASIfCfgWlanAuthorization,
       "hwBRASIfCfgDhcpShortLease": hwBRASIfCfgDhcpShortLease,
       "hwBRASIfCfgRoamDomain": hwBRASIfCfgRoamDomain,
       "hwBRASIfVsiName": hwBRASIfVsiName,
       "hwBRASIfCfgOption82": hwBRASIfCfgOption82,
       "hwBRASIfVpnInstance": hwBRASIfVpnInstance,
       "hwBRASIfCopyMulticasePerUser": hwBRASIfCopyMulticasePerUser,
       "hwBRASIfCfgNDProxy": hwBRASIfCfgNDProxy,
       "hwBRASIfCfgVBasMAC": hwBRASIfCfgVBasMAC,
       "hwBRASIfCfgVBasAuthMode": hwBRASIfCfgVBasAuthMode,
       "hwBRASIfCfgPermitDomain1": hwBRASIfCfgPermitDomain1,
       "hwBRASIfCfgPermitDomain2": hwBRASIfCfgPermitDomain2,
       "hwBRASIfCfgPermitDomain3": hwBRASIfCfgPermitDomain3,
       "hwBRASIfCfgPermitDomain4": hwBRASIfCfgPermitDomain4,
       "hwBRASIfCfgAccessDelayType": hwBRASIfCfgAccessDelayType,
       "hwBRASIfCfgTermlessDelayTime": hwBRASIfCfgTermlessDelayTime,
       "hwBRASIfCfgOddMacDelayTime": hwBRASIfCfgOddMacDelayTime,
       "hwBRASIfCfgEvenMacDelayTime": hwBRASIfCfgEvenMacDelayTime,
       "hwBRASIfCfgAccessNodeIdentify": hwBRASIfCfgAccessNodeIdentify,
       "hwBRASIfCfgAniDelayTime": hwBRASIfCfgAniDelayTime,
       "hwBRASIfCfgRemoteBackupProfile": hwBRASIfCfgRemoteBackupProfile,
       "hwBRASIfVlanTable": hwBRASIfVlanTable,
       "hwBRASIfVlanEntry": hwBRASIfVlanEntry,
       "hwBRASIfVlanIfIndex": hwBRASIfVlanIfIndex,
       "hwBRASIfVlanVlanId": hwBRASIfVlanVlanId,
       "hwBRASIfVlanVlanNumber": hwBRASIfVlanVlanNumber,
       "hwBRASIfVlanAccessLimit": hwBRASIfVlanAccessLimit,
       "hwBRASIfVlanAccessNumber": hwBRASIfVlanAccessNumber,
       "hwBRASIfVlanBlock": hwBRASIfVlanBlock,
       "hwBRASIfVlanDevAccessNumber": hwBRASIfVlanDevAccessNumber,
       "hwBRASIfVlanSchedulerVcName": hwBRASIfVlanSchedulerVcName,
       "hwBRASIfVlanSchedulerVcGroupName": hwBRASIfVlanSchedulerVcGroupName,
       "hwBRASIfVlanSchedulerVpGroupName": hwBRASIfVlanSchedulerVpGroupName,
       "hwBRASIfQinQVlanID": hwBRASIfQinQVlanID,
       "hwBRASIfPvcTable": hwBRASIfPvcTable,
       "hwBRASIfPvcEntry": hwBRASIfPvcEntry,
       "hwBRASIfPvcIfIndex": hwBRASIfPvcIfIndex,
       "hwBRASIfPvcVpi": hwBRASIfPvcVpi,
       "hwBRASIfPvcVci": hwBRASIfPvcVci,
       "hwBRASIfPvcPvcNumber": hwBRASIfPvcPvcNumber,
       "hwBRASIfPvcAccessLimit": hwBRASIfPvcAccessLimit,
       "hwBRASIfPvcAccessNumber": hwBRASIfPvcAccessNumber,
       "hwBRASIfPvcBlock": hwBRASIfPvcBlock,
       "hwBRASIfPvcDevAccessNumber": hwBRASIfPvcDevAccessNumber,
       "hwBRASIfPvcSchedulerVcGroupName": hwBRASIfPvcSchedulerVcGroupName,
       "hwBRASIfPvcSchedulerVpGroupName": hwBRASIfPvcSchedulerVpGroupName,
       "hwSTPRelayTable": hwSTPRelayTable,
       "hwSTPRelayEntry": hwSTPRelayEntry,
       "hwSTPRelayIndex": hwSTPRelayIndex,
       "hwSTPRelayInIfIndex": hwSTPRelayInIfIndex,
       "hwSTPRelayOutIfIndex": hwSTPRelayOutIfIndex,
       "hwSTPRelayRowStatus": hwSTPRelayRowStatus,
       "hwSTPRelayInIfName": hwSTPRelayInIfName,
       "hwSTPRelayOutIfName": hwSTPRelayOutIfName,
       "hwSTPRelayInMac": hwSTPRelayInMac,
       "hwSTPRelayOutMac": hwSTPRelayOutMac,
       "hwPortAccessLimitTable": hwPortAccessLimitTable,
       "hwPortAccessLimitEntry": hwPortAccessLimitEntry,
       "hwPortAccessLimitIfIndex": hwPortAccessLimitIfIndex,
       "hwPortAccessLimitLimit": hwPortAccessLimitLimit,
       "hwPortAccessLimitNumber": hwPortAccessLimitNumber,
       "hwPortAccessLimitDevNumber": hwPortAccessLimitDevNumber,
       "hwL3SubscriberIspTable": hwL3SubscriberIspTable,
       "hwL3SubscriberIspEntry": hwL3SubscriberIspEntry,
       "hwL3SubscriberIspStartIp": hwL3SubscriberIspStartIp,
       "hwL3SubscriberIspVpnId": hwL3SubscriberIspVpnId,
       "hwL3SubscriberIspEndIp": hwL3SubscriberIspEndIp,
       "hwL3SubscriberIspDomainName": hwL3SubscriberIspDomainName,
       "hwL3SubscriberIspRowStatus": hwL3SubscriberIspRowStatus,
       "srvcfgScalar": srvcfgScalar,
       "hwDhcpOption60DomainInclude": hwDhcpOption60DomainInclude,
       "hwDhcpOption60PartialMatch": hwDhcpOption60PartialMatch,
       "hwConnTimeOutTable": hwConnTimeOutTable,
       "hwConnTimeOutTcp": hwConnTimeOutTcp,
       "hwConnTimeOutUdp": hwConnTimeOutUdp,
       "hwBRASIfVlanNumTable": hwBRASIfVlanNumTable,
       "hwBRASIfVlanNumEntry": hwBRASIfVlanNumEntry,
       "hwBRASIfSlot": hwBRASIfSlot,
       "hwBRASSlotVlanNum": hwBRASSlotVlanNum,
       "hwBRASSLotStaticVlanNum": hwBRASSLotStaticVlanNum,
       "hwServiceIfCfgTable": hwServiceIfCfgTable,
       "hwServiceIfCfgEntry": hwServiceIfCfgEntry,
       "hwServiceIfCfgIfIndex": hwServiceIfCfgIfIndex,
       "hwServiceIfCfgIdentificationMode": hwServiceIfCfgIdentificationMode,
       "hwServiceIfCfgDomain": hwServiceIfCfgDomain,
       "hwServiceIfCfgUserName": hwServiceIfCfgUserName,
       "hwServiceIfCfgPassword": hwServiceIfCfgPassword,
       "hwServiceIfCfgDetectNum": hwServiceIfCfgDetectNum,
       "hwServiceIfCfgDetectInterval": hwServiceIfCfgDetectInterval,
       "hwServiceIfCfgOption82": hwServiceIfCfgOption82,
       "hwServiceIfCfgAccessLimit": hwServiceIfCfgAccessLimit,
       "hwServiceIfCfgOption60": hwServiceIfCfgOption60,
       "hwServiceIfCfgIpTriggerEnable": hwServiceIfCfgIpTriggerEnable,
       "hwServiceIfCfgArpTriggerEnable": hwServiceIfCfgArpTriggerEnable,
       "hwServiceIfCfgIfBlock": hwServiceIfCfgIfBlock,
       "hwServiceIfCfgQosProfile": hwServiceIfCfgQosProfile,
       "hwServiceIfCfgBindingUserPasswordMode": hwServiceIfCfgBindingUserPasswordMode,
       "hwServiceIfCfgBindingUserNameFormat": hwServiceIfCfgBindingUserNameFormat,
       "hwServiceIfCfgBindingUserPassword": hwServiceIfCfgBindingUserPassword,
       "hwServiceIfCfgRowStatus": hwServiceIfCfgRowStatus,
       "hwSrvcfgInterfaceConformance": hwSrvcfgInterfaceConformance,
       "hwSrvcfgInterfaceCompliances": hwSrvcfgInterfaceCompliances,
       "hwSrvcfgInterfaceCompliance": hwSrvcfgInterfaceCompliance,
       "hwSrvcfgInterfaceGroups": hwSrvcfgInterfaceGroups,
       "hwBRASIfCfgGroup": hwBRASIfCfgGroup,
       "hwBRASIfVlanGroup": hwBRASIfVlanGroup,
       "hwBRASIfPvcGroup": hwBRASIfPvcGroup,
       "hwSTPRelayServerGroup": hwSTPRelayServerGroup,
       "hwPortAccessLimitGroup": hwPortAccessLimitGroup,
       "hwL3SubscriberIspGroup": hwL3SubscriberIspGroup,
       "hwConnTimeOutGroup": hwConnTimeOutGroup,
       "hwSrvcfgScalarGroup": hwSrvcfgScalarGroup,
       "hwBRASIfVlanNumGroup": hwBRASIfVlanNumGroup,
       "hwServiceIfCfgGroup": hwServiceIfCfgGroup}
)
