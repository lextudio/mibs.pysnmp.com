# SNMP MIB module (STN-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STN-ATM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:02 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(stnNotification,
 stnSystems) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-SMI",
    "stnNotification",
    "stnSystems")

(NSAPAddress,) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-TC",
    "NSAPAddress")

(stnRouterIndex,) = mibBuilder.importSymbols(
    "STN-ROUTER-MIB",
    "stnRouterIndex")


# MODULE-IDENTITY

stnAtm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VcLinkOperStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("create-and-go", 4),
          ("create-and-wait", 5),
          ("destroy", 6),
          ("not-in-service", 2),
          ("not-ready", 3))
    )



class VcCrossConnOperStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("create-and-go", 4),
          ("create-and-wait", 5),
          ("destroy", 6),
          ("not-in-service", 2),
          ("not-ready", 3))
    )



class TrafficDescrOperStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("create-and-go", 4),
          ("create-and-wait", 5),
          ("destroy", 6),
          ("not-in-service", 2),
          ("not-ready", 3))
    )



class AtmPortOperStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )



# MIB Managed Objects in the order of their OIDs

_StnAtmObjects_ObjectIdentity = ObjectIdentity
stnAtmObjects = _StnAtmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1)
)
_StnAtmLinks_ObjectIdentity = ObjectIdentity
stnAtmLinks = _StnAtmLinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 1)
)
_StnVcLinks_ObjectIdentity = ObjectIdentity
stnVcLinks = _StnVcLinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 1, 1)
)
_StnVcLinkTable_Object = MibTable
stnVcLinkTable = _StnVcLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    stnVcLinkTable.setStatus("current")
_StnVcLinkEntry_Object = MibTableRow
stnVcLinkEntry = _StnVcLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 1, 1, 1, 1)
)
stnVcLinkEntry.setIndexNames(
    (0, "STN-ATM-MIB", "stnVcLinkIfIndex"),
    (0, "STN-ATM-MIB", "stnVcLinkVpi"),
    (0, "STN-ATM-MIB", "stnVcLinkVci"),
)
if mibBuilder.loadTexts:
    stnVcLinkEntry.setStatus("current")
_StnVcLinkIfIndex_Type = InterfaceIndex
_StnVcLinkIfIndex_Object = MibTableColumn
stnVcLinkIfIndex = _StnVcLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 1, 1, 1, 1, 1),
    _StnVcLinkIfIndex_Type()
)
stnVcLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcLinkIfIndex.setStatus("current")
_StnVcLinkVpi_Type = Integer32
_StnVcLinkVpi_Object = MibTableColumn
stnVcLinkVpi = _StnVcLinkVpi_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 1, 1, 1, 1, 2),
    _StnVcLinkVpi_Type()
)
stnVcLinkVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcLinkVpi.setStatus("current")
_StnVcLinkVci_Type = Integer32
_StnVcLinkVci_Object = MibTableColumn
stnVcLinkVci = _StnVcLinkVci_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 1, 1, 1, 1, 3),
    _StnVcLinkVci_Type()
)
stnVcLinkVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcLinkVci.setStatus("current")
_StnVcLinkRcvTrafDescr_Type = Integer32
_StnVcLinkRcvTrafDescr_Object = MibTableColumn
stnVcLinkRcvTrafDescr = _StnVcLinkRcvTrafDescr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 1, 1, 1, 1, 4),
    _StnVcLinkRcvTrafDescr_Type()
)
stnVcLinkRcvTrafDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcLinkRcvTrafDescr.setStatus("current")
_StnVcLinkXmtTrafDescr_Type = Integer32
_StnVcLinkXmtTrafDescr_Object = MibTableColumn
stnVcLinkXmtTrafDescr = _StnVcLinkXmtTrafDescr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 1, 1, 1, 1, 5),
    _StnVcLinkXmtTrafDescr_Type()
)
stnVcLinkXmtTrafDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcLinkXmtTrafDescr.setStatus("current")
_StnVcLinkAalObjectsValid_Type = Integer32
_StnVcLinkAalObjectsValid_Object = MibTableColumn
stnVcLinkAalObjectsValid = _StnVcLinkAalObjectsValid_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 1, 1, 1, 1, 6),
    _StnVcLinkAalObjectsValid_Type()
)
stnVcLinkAalObjectsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcLinkAalObjectsValid.setStatus("current")


class _StnVcLinkAalType_Type(Integer32):
    """Custom type stnVcLinkAalType based on Integer32"""
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
        *(("aal1", 1),
          ("aal3-4", 2),
          ("aal5", 3),
          ("other", 4))
    )


_StnVcLinkAalType_Type.__name__ = "Integer32"
_StnVcLinkAalType_Object = MibTableColumn
stnVcLinkAalType = _StnVcLinkAalType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 1, 1, 1, 1, 7),
    _StnVcLinkAalType_Type()
)
stnVcLinkAalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcLinkAalType.setStatus("current")


class _StnVcLinkAal5XmtSDUSize_Type(Integer32):
    """Custom type stnVcLinkAal5XmtSDUSize based on Integer32"""
    defaultValue = 4096


_StnVcLinkAal5XmtSDUSize_Object = MibTableColumn
stnVcLinkAal5XmtSDUSize = _StnVcLinkAal5XmtSDUSize_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 1, 1, 1, 1, 8),
    _StnVcLinkAal5XmtSDUSize_Type()
)
stnVcLinkAal5XmtSDUSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcLinkAal5XmtSDUSize.setStatus("current")


class _StnVcLinkAal5RcvSDUSize_Type(Integer32):
    """Custom type stnVcLinkAal5RcvSDUSize based on Integer32"""
    defaultValue = 4096


_StnVcLinkAal5RcvSDUSize_Object = MibTableColumn
stnVcLinkAal5RcvSDUSize = _StnVcLinkAal5RcvSDUSize_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 1, 1, 1, 1, 9),
    _StnVcLinkAal5RcvSDUSize_Type()
)
stnVcLinkAal5RcvSDUSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcLinkAal5RcvSDUSize.setStatus("current")
_StnVcLinkAal5EncapsType_Type = Integer32
_StnVcLinkAal5EncapsType_Object = MibTableColumn
stnVcLinkAal5EncapsType = _StnVcLinkAal5EncapsType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 1, 1, 1, 1, 10),
    _StnVcLinkAal5EncapsType_Type()
)
stnVcLinkAal5EncapsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcLinkAal5EncapsType.setStatus("current")


class _StnVcLinkCastType_Type(Integer32):
    """Custom type stnVcLinkCastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("p2mpLeaf", 2),
          ("p2mpRoot", 1))
    )


_StnVcLinkCastType_Type.__name__ = "Integer32"
_StnVcLinkCastType_Object = MibTableColumn
stnVcLinkCastType = _StnVcLinkCastType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 1, 1, 1, 1, 11),
    _StnVcLinkCastType_Type()
)
stnVcLinkCastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcLinkCastType.setStatus("current")


class _StnVcLinkConnKind_Type(Integer32):
    """Custom type stnVcLinkConnKind based on Integer32"""
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
        *(("pvc", 1),
          ("spvc-initiator", 4),
          ("spvc-target", 5),
          ("svc-incomming", 2),
          ("svc-outgoing", 3))
    )


_StnVcLinkConnKind_Type.__name__ = "Integer32"
_StnVcLinkConnKind_Object = MibTableColumn
stnVcLinkConnKind = _StnVcLinkConnKind_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 1, 1, 1, 1, 12),
    _StnVcLinkConnKind_Type()
)
stnVcLinkConnKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcLinkConnKind.setStatus("current")


class _StnVcLinkAccEnabled_Type(TruthValue):
    """Custom type stnVcLinkAccEnabled based on TruthValue"""


_StnVcLinkAccEnabled_Object = MibTableColumn
stnVcLinkAccEnabled = _StnVcLinkAccEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 1, 1, 1, 1, 13),
    _StnVcLinkAccEnabled_Type()
)
stnVcLinkAccEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcLinkAccEnabled.setStatus("current")


class _StnVcLinkOAMMgmtEnabled_Type(TruthValue):
    """Custom type stnVcLinkOAMMgmtEnabled based on TruthValue"""


_StnVcLinkOAMMgmtEnabled_Object = MibTableColumn
stnVcLinkOAMMgmtEnabled = _StnVcLinkOAMMgmtEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 1, 1, 1, 1, 14),
    _StnVcLinkOAMMgmtEnabled_Type()
)
stnVcLinkOAMMgmtEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcLinkOAMMgmtEnabled.setStatus("current")


class _StnVcLinkOAMXmtFrequency_Type(Integer32):
    """Custom type stnVcLinkOAMXmtFrequency based on Integer32"""
    defaultValue = 5


_StnVcLinkOAMXmtFrequency_Object = MibTableColumn
stnVcLinkOAMXmtFrequency = _StnVcLinkOAMXmtFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 1, 1, 1, 1, 15),
    _StnVcLinkOAMXmtFrequency_Type()
)
stnVcLinkOAMXmtFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcLinkOAMXmtFrequency.setStatus("current")


class _StnVcLinkOAMRetryUpCount_Type(Integer32):
    """Custom type stnVcLinkOAMRetryUpCount based on Integer32"""
    defaultValue = 3


_StnVcLinkOAMRetryUpCount_Object = MibTableColumn
stnVcLinkOAMRetryUpCount = _StnVcLinkOAMRetryUpCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 1, 1, 1, 1, 16),
    _StnVcLinkOAMRetryUpCount_Type()
)
stnVcLinkOAMRetryUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcLinkOAMRetryUpCount.setStatus("current")


class _StnVcLinkOAMRetryDownCount_Type(Integer32):
    """Custom type stnVcLinkOAMRetryDownCount based on Integer32"""
    defaultValue = 5


_StnVcLinkOAMRetryDownCount_Object = MibTableColumn
stnVcLinkOAMRetryDownCount = _StnVcLinkOAMRetryDownCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 1, 1, 1, 1, 17),
    _StnVcLinkOAMRetryDownCount_Type()
)
stnVcLinkOAMRetryDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcLinkOAMRetryDownCount.setStatus("current")


class _StnVcLinkOAMRetryFrequency_Type(Integer32):
    """Custom type stnVcLinkOAMRetryFrequency based on Integer32"""
    defaultValue = 5


_StnVcLinkOAMRetryFrequency_Object = MibTableColumn
stnVcLinkOAMRetryFrequency = _StnVcLinkOAMRetryFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 1, 1, 1, 1, 18),
    _StnVcLinkOAMRetryFrequency_Type()
)
stnVcLinkOAMRetryFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcLinkOAMRetryFrequency.setStatus("current")
_StnVcLinkPppId_Type = Integer32
_StnVcLinkPppId_Object = MibTableColumn
stnVcLinkPppId = _StnVcLinkPppId_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 1, 1, 1, 1, 19),
    _StnVcLinkPppId_Type()
)
stnVcLinkPppId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcLinkPppId.setStatus("current")
_StnVcLinkOperStatus_Type = VcLinkOperStatus
_StnVcLinkOperStatus_Object = MibTableColumn
stnVcLinkOperStatus = _StnVcLinkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 1, 1, 1, 1, 20),
    _StnVcLinkOperStatus_Type()
)
stnVcLinkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcLinkOperStatus.setStatus("current")
_StnAtmCrossConns_ObjectIdentity = ObjectIdentity
stnAtmCrossConns = _StnAtmCrossConns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 2)
)
_StnVcCrossConns_ObjectIdentity = ObjectIdentity
stnVcCrossConns = _StnVcCrossConns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 2, 1)
)
_StnVcCrossConnTable_Object = MibTable
stnVcCrossConnTable = _StnVcCrossConnTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    stnVcCrossConnTable.setStatus("current")
_StnVcCrossConnEntry_Object = MibTableRow
stnVcCrossConnEntry = _StnVcCrossConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 2, 1, 1, 1)
)
stnVcCrossConnEntry.setIndexNames(
    (0, "STN-ATM-MIB", "stnVcCrossConnLowIfIndex"),
    (0, "STN-ATM-MIB", "stnVcCrossConnLowVpi"),
    (0, "STN-ATM-MIB", "stnVcCrossConnLowVci"),
    (0, "STN-ATM-MIB", "stnVcCrossConnHighIfIndex"),
    (0, "STN-ATM-MIB", "stnVcCrossConnHighVpi"),
    (0, "STN-ATM-MIB", "stnVcCrossConnHighVci"),
)
if mibBuilder.loadTexts:
    stnVcCrossConnEntry.setStatus("current")
_StnVcCrossConnLowIfIndex_Type = InterfaceIndex
_StnVcCrossConnLowIfIndex_Object = MibTableColumn
stnVcCrossConnLowIfIndex = _StnVcCrossConnLowIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 2, 1, 1, 1, 1),
    _StnVcCrossConnLowIfIndex_Type()
)
stnVcCrossConnLowIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcCrossConnLowIfIndex.setStatus("current")
_StnVcCrossConnLowVpi_Type = Integer32
_StnVcCrossConnLowVpi_Object = MibTableColumn
stnVcCrossConnLowVpi = _StnVcCrossConnLowVpi_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 2, 1, 1, 1, 2),
    _StnVcCrossConnLowVpi_Type()
)
stnVcCrossConnLowVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcCrossConnLowVpi.setStatus("current")
_StnVcCrossConnLowVci_Type = Integer32
_StnVcCrossConnLowVci_Object = MibTableColumn
stnVcCrossConnLowVci = _StnVcCrossConnLowVci_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 2, 1, 1, 1, 3),
    _StnVcCrossConnLowVci_Type()
)
stnVcCrossConnLowVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcCrossConnLowVci.setStatus("current")
_StnVcCrossConnHighIfIndex_Type = InterfaceIndex
_StnVcCrossConnHighIfIndex_Object = MibTableColumn
stnVcCrossConnHighIfIndex = _StnVcCrossConnHighIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 2, 1, 1, 1, 4),
    _StnVcCrossConnHighIfIndex_Type()
)
stnVcCrossConnHighIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcCrossConnHighIfIndex.setStatus("current")
_StnVcCrossConnHighVpi_Type = Integer32
_StnVcCrossConnHighVpi_Object = MibTableColumn
stnVcCrossConnHighVpi = _StnVcCrossConnHighVpi_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 2, 1, 1, 1, 5),
    _StnVcCrossConnHighVpi_Type()
)
stnVcCrossConnHighVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcCrossConnHighVpi.setStatus("current")
_StnVcCrossConnHighVci_Type = Integer32
_StnVcCrossConnHighVci_Object = MibTableColumn
stnVcCrossConnHighVci = _StnVcCrossConnHighVci_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 2, 1, 1, 1, 6),
    _StnVcCrossConnHighVci_Type()
)
stnVcCrossConnHighVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcCrossConnHighVci.setStatus("current")


class _StnVcCrossConnLowAutoAssign_Type(TruthValue):
    """Custom type stnVcCrossConnLowAutoAssign based on TruthValue"""


_StnVcCrossConnLowAutoAssign_Object = MibTableColumn
stnVcCrossConnLowAutoAssign = _StnVcCrossConnLowAutoAssign_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 2, 1, 1, 1, 7),
    _StnVcCrossConnLowAutoAssign_Type()
)
stnVcCrossConnLowAutoAssign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcCrossConnLowAutoAssign.setStatus("current")


class _StnVcCrossConnHighAutoAssign_Type(TruthValue):
    """Custom type stnVcCrossConnHighAutoAssign based on TruthValue"""


_StnVcCrossConnHighAutoAssign_Object = MibTableColumn
stnVcCrossConnHighAutoAssign = _StnVcCrossConnHighAutoAssign_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 2, 1, 1, 1, 8),
    _StnVcCrossConnHighAutoAssign_Type()
)
stnVcCrossConnHighAutoAssign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcCrossConnHighAutoAssign.setStatus("current")
_StnVcCrossConnOperStatus_Type = VcCrossConnOperStatus
_StnVcCrossConnOperStatus_Object = MibTableColumn
stnVcCrossConnOperStatus = _StnVcCrossConnOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 2, 1, 1, 1, 9),
    _StnVcCrossConnOperStatus_Type()
)
stnVcCrossConnOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVcCrossConnOperStatus.setStatus("current")
_StnVpCrossConns_ObjectIdentity = ObjectIdentity
stnVpCrossConns = _StnVpCrossConns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 2, 2)
)
_StnAtmTrafficDescrs_ObjectIdentity = ObjectIdentity
stnAtmTrafficDescrs = _StnAtmTrafficDescrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 3)
)
_StnTrafficDescrTable_Object = MibTable
stnTrafficDescrTable = _StnTrafficDescrTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    stnTrafficDescrTable.setStatus("current")
_StnTrafficDescrEntry_Object = MibTableRow
stnTrafficDescrEntry = _StnTrafficDescrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 3, 1, 1)
)
stnTrafficDescrEntry.setIndexNames(
    (0, "STN-ATM-MIB", "stnTrafDescrIndex"),
)
if mibBuilder.loadTexts:
    stnTrafficDescrEntry.setStatus("current")
_StnTrafDescrIndex_Type = Integer32
_StnTrafDescrIndex_Object = MibTableColumn
stnTrafDescrIndex = _StnTrafDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 3, 1, 1, 1),
    _StnTrafDescrIndex_Type()
)
stnTrafDescrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnTrafDescrIndex.setStatus("current")


class _StnTrafDescrName_Type(OctetString):
    """Custom type stnTrafDescrName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StnTrafDescrName_Type.__name__ = "OctetString"
_StnTrafDescrName_Object = MibTableColumn
stnTrafDescrName = _StnTrafDescrName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 3, 1, 1, 2),
    _StnTrafDescrName_Type()
)
stnTrafDescrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnTrafDescrName.setStatus("current")


class _StnTrafDescrType_Type(Integer32):
    """Custom type stnTrafDescrType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("clp-no-tag-mcr", 8),
          ("clp-no-tag-no-scr", 3),
          ("clp-no-tag-scr", 6),
          ("clp-tagging-no-scr", 4),
          ("clp-tagging-scr", 7),
          ("clp-trans-no-scr", 9),
          ("clp-trans-scr", 10),
          ("no-clp-no-scr", 2),
          ("no-clp-scr", 5),
          ("no-clp-tag-no-scr", 11),
          ("no-td", 1))
    )


_StnTrafDescrType_Type.__name__ = "Integer32"
_StnTrafDescrType_Object = MibTableColumn
stnTrafDescrType = _StnTrafDescrType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 3, 1, 1, 3),
    _StnTrafDescrType_Type()
)
stnTrafDescrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnTrafDescrType.setStatus("current")


class _StnTrafDescrParam1_Type(Integer32):
    """Custom type stnTrafDescrParam1 based on Integer32"""
    defaultValue = 0


_StnTrafDescrParam1_Object = MibTableColumn
stnTrafDescrParam1 = _StnTrafDescrParam1_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 3, 1, 1, 4),
    _StnTrafDescrParam1_Type()
)
stnTrafDescrParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnTrafDescrParam1.setStatus("current")


class _StnTrafDescrParam2_Type(Integer32):
    """Custom type stnTrafDescrParam2 based on Integer32"""
    defaultValue = 0


_StnTrafDescrParam2_Object = MibTableColumn
stnTrafDescrParam2 = _StnTrafDescrParam2_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 3, 1, 1, 5),
    _StnTrafDescrParam2_Type()
)
stnTrafDescrParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnTrafDescrParam2.setStatus("current")


class _StnTrafDescrParam3_Type(Integer32):
    """Custom type stnTrafDescrParam3 based on Integer32"""
    defaultValue = 0


_StnTrafDescrParam3_Object = MibTableColumn
stnTrafDescrParam3 = _StnTrafDescrParam3_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 3, 1, 1, 6),
    _StnTrafDescrParam3_Type()
)
stnTrafDescrParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnTrafDescrParam3.setStatus("current")


class _StnTrafDescrParam4_Type(Integer32):
    """Custom type stnTrafDescrParam4 based on Integer32"""
    defaultValue = 0


_StnTrafDescrParam4_Object = MibTableColumn
stnTrafDescrParam4 = _StnTrafDescrParam4_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 3, 1, 1, 7),
    _StnTrafDescrParam4_Type()
)
stnTrafDescrParam4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnTrafDescrParam4.setStatus("current")


class _StnTrafDescrParam5_Type(Integer32):
    """Custom type stnTrafDescrParam5 based on Integer32"""
    defaultValue = 0


_StnTrafDescrParam5_Object = MibTableColumn
stnTrafDescrParam5 = _StnTrafDescrParam5_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 3, 1, 1, 8),
    _StnTrafDescrParam5_Type()
)
stnTrafDescrParam5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnTrafDescrParam5.setStatus("current")


class _StnTrafDescrQosClass_Type(Integer32):
    """Custom type stnTrafDescrQosClass based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("best-effort", 0),
          ("service-class-a", 1),
          ("service-class-b", 2),
          ("service-class-c", 3),
          ("service-class-d", 4))
    )


_StnTrafDescrQosClass_Type.__name__ = "Integer32"
_StnTrafDescrQosClass_Object = MibTableColumn
stnTrafDescrQosClass = _StnTrafDescrQosClass_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 3, 1, 1, 9),
    _StnTrafDescrQosClass_Type()
)
stnTrafDescrQosClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnTrafDescrQosClass.setStatus("current")


class _StnTrafDescrServiceCategory_Type(Integer32):
    """Custom type stnTrafDescrServiceCategory based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("abr", 5),
          ("cbr", 2),
          ("nrt-vbr", 4),
          ("other", 1),
          ("rt-vbr", 3),
          ("ubr", 6))
    )


_StnTrafDescrServiceCategory_Type.__name__ = "Integer32"
_StnTrafDescrServiceCategory_Object = MibTableColumn
stnTrafDescrServiceCategory = _StnTrafDescrServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 3, 1, 1, 10),
    _StnTrafDescrServiceCategory_Type()
)
stnTrafDescrServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnTrafDescrServiceCategory.setStatus("current")


class _StnTrafDescrFrameDiscard_Type(TruthValue):
    """Custom type stnTrafDescrFrameDiscard based on TruthValue"""


_StnTrafDescrFrameDiscard_Object = MibTableColumn
stnTrafDescrFrameDiscard = _StnTrafDescrFrameDiscard_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 3, 1, 1, 11),
    _StnTrafDescrFrameDiscard_Type()
)
stnTrafDescrFrameDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnTrafDescrFrameDiscard.setStatus("current")
_StnTrafDescrOperStatus_Type = TrafficDescrOperStatus
_StnTrafDescrOperStatus_Object = MibTableColumn
stnTrafDescrOperStatus = _StnTrafDescrOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 3, 1, 1, 12),
    _StnTrafDescrOperStatus_Type()
)
stnTrafDescrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnTrafDescrOperStatus.setStatus("current")


class _StnTrafDescrCommittedRate_Type(Integer32):
    """Custom type stnTrafDescrCommittedRate based on Integer32"""
    defaultValue = 0


_StnTrafDescrCommittedRate_Object = MibTableColumn
stnTrafDescrCommittedRate = _StnTrafDescrCommittedRate_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 3, 1, 1, 13),
    _StnTrafDescrCommittedRate_Type()
)
stnTrafDescrCommittedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnTrafDescrCommittedRate.setStatus("current")


class _StnTrafDescrMaximumRate_Type(Integer32):
    """Custom type stnTrafDescrMaximumRate based on Integer32"""
    defaultValue = 0


_StnTrafDescrMaximumRate_Object = MibTableColumn
stnTrafDescrMaximumRate = _StnTrafDescrMaximumRate_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 3, 1, 1, 14),
    _StnTrafDescrMaximumRate_Type()
)
stnTrafDescrMaximumRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnTrafDescrMaximumRate.setStatus("current")
_StnAtmPorts_ObjectIdentity = ObjectIdentity
stnAtmPorts = _StnAtmPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4)
)
_StnAtmPortAttrs_ObjectIdentity = ObjectIdentity
stnAtmPortAttrs = _StnAtmPortAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1)
)
_StnAtmPortAttrTable_Object = MibTable
stnAtmPortAttrTable = _StnAtmPortAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    stnAtmPortAttrTable.setStatus("current")
_StnAtmPortAttrEntry_Object = MibTableRow
stnAtmPortAttrEntry = _StnAtmPortAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1)
)
stnAtmPortAttrEntry.setIndexNames(
    (0, "STN-ATM-MIB", "stnAtmPortIfIndex"),
)
if mibBuilder.loadTexts:
    stnAtmPortAttrEntry.setStatus("current")
_StnAtmPortIfIndex_Type = InterfaceIndex
_StnAtmPortIfIndex_Object = MibTableColumn
stnAtmPortIfIndex = _StnAtmPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 1),
    _StnAtmPortIfIndex_Type()
)
stnAtmPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortIfIndex.setStatus("current")
_StnAtmPortIfType_Type = Integer32
_StnAtmPortIfType_Object = MibTableColumn
stnAtmPortIfType = _StnAtmPortIfType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 2),
    _StnAtmPortIfType_Type()
)
stnAtmPortIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortIfType.setStatus("current")


class _StnAtmPortIfState_Type(Integer32):
    """Custom type stnAtmPortIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_StnAtmPortIfState_Type.__name__ = "Integer32"
_StnAtmPortIfState_Object = MibTableColumn
stnAtmPortIfState = _StnAtmPortIfState_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 3),
    _StnAtmPortIfState_Type()
)
stnAtmPortIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortIfState.setStatus("current")


class _StnAtmPortEnabled_Type(TruthValue):
    """Custom type stnAtmPortEnabled based on TruthValue"""


_StnAtmPortEnabled_Object = MibTableColumn
stnAtmPortEnabled = _StnAtmPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 4),
    _StnAtmPortEnabled_Type()
)
stnAtmPortEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortEnabled.setStatus("current")


class _StnAtmPortMinVccVpi_Type(Integer32):
    """Custom type stnAtmPortMinVccVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_StnAtmPortMinVccVpi_Type.__name__ = "Integer32"
_StnAtmPortMinVccVpi_Object = MibTableColumn
stnAtmPortMinVccVpi = _StnAtmPortMinVccVpi_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 5),
    _StnAtmPortMinVccVpi_Type()
)
stnAtmPortMinVccVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortMinVccVpi.setStatus("current")


class _StnAtmPortMaxVccVpi_Type(Integer32):
    """Custom type stnAtmPortMaxVccVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_StnAtmPortMaxVccVpi_Type.__name__ = "Integer32"
_StnAtmPortMaxVccVpi_Object = MibTableColumn
stnAtmPortMaxVccVpi = _StnAtmPortMaxVccVpi_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 6),
    _StnAtmPortMaxVccVpi_Type()
)
stnAtmPortMaxVccVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortMaxVccVpi.setStatus("current")


class _StnAtmPortMinVccVci_Type(Integer32):
    """Custom type stnAtmPortMinVccVci based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65554),
    )


_StnAtmPortMinVccVci_Type.__name__ = "Integer32"
_StnAtmPortMinVccVci_Object = MibTableColumn
stnAtmPortMinVccVci = _StnAtmPortMinVccVci_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 7),
    _StnAtmPortMinVccVci_Type()
)
stnAtmPortMinVccVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortMinVccVci.setStatus("current")


class _StnAtmPortMaxVccVci_Type(Integer32):
    """Custom type stnAtmPortMaxVccVci based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65554),
    )


_StnAtmPortMaxVccVci_Type.__name__ = "Integer32"
_StnAtmPortMaxVccVci_Object = MibTableColumn
stnAtmPortMaxVccVci = _StnAtmPortMaxVccVci_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 8),
    _StnAtmPortMaxVccVci_Type()
)
stnAtmPortMaxVccVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortMaxVccVci.setStatus("current")


class _StnAtmPortMinVpcVpi_Type(Integer32):
    """Custom type stnAtmPortMinVpcVpi based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_StnAtmPortMinVpcVpi_Type.__name__ = "Integer32"
_StnAtmPortMinVpcVpi_Object = MibTableColumn
stnAtmPortMinVpcVpi = _StnAtmPortMinVpcVpi_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 9),
    _StnAtmPortMinVpcVpi_Type()
)
stnAtmPortMinVpcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortMinVpcVpi.setStatus("current")


class _StnAtmPortMaxVpcVpi_Type(Integer32):
    """Custom type stnAtmPortMaxVpcVpi based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_StnAtmPortMaxVpcVpi_Type.__name__ = "Integer32"
_StnAtmPortMaxVpcVpi_Object = MibTableColumn
stnAtmPortMaxVpcVpi = _StnAtmPortMaxVpcVpi_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 10),
    _StnAtmPortMaxVpcVpi_Type()
)
stnAtmPortMaxVpcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortMaxVpcVpi.setStatus("current")


class _StnAtmPortMaxActivePaths_Type(Integer32):
    """Custom type stnAtmPortMaxActivePaths based on Integer32"""
    defaultValue = 127

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_StnAtmPortMaxActivePaths_Type.__name__ = "Integer32"
_StnAtmPortMaxActivePaths_Object = MibTableColumn
stnAtmPortMaxActivePaths = _StnAtmPortMaxActivePaths_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 11),
    _StnAtmPortMaxActivePaths_Type()
)
stnAtmPortMaxActivePaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortMaxActivePaths.setStatus("current")


class _StnAtmPortMaxActiveChannels_Type(Integer32):
    """Custom type stnAtmPortMaxActiveChannels based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65554),
    )


_StnAtmPortMaxActiveChannels_Type.__name__ = "Integer32"
_StnAtmPortMaxActiveChannels_Object = MibTableColumn
stnAtmPortMaxActiveChannels = _StnAtmPortMaxActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 12),
    _StnAtmPortMaxActiveChannels_Type()
)
stnAtmPortMaxActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortMaxActiveChannels.setStatus("current")
_StnAtmPortPVCAddress_Type = NSAPAddress
_StnAtmPortPVCAddress_Object = MibTableColumn
stnAtmPortPVCAddress = _StnAtmPortPVCAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 13),
    _StnAtmPortPVCAddress_Type()
)
stnAtmPortPVCAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortPVCAddress.setStatus("current")
_StnAtmPortSVCAddress_Type = NSAPAddress
_StnAtmPortSVCAddress_Object = MibTableColumn
stnAtmPortSVCAddress = _StnAtmPortSVCAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 14),
    _StnAtmPortSVCAddress_Type()
)
stnAtmPortSVCAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSVCAddress.setStatus("current")


class _StnAtmPortSigVpi_Type(Integer32):
    """Custom type stnAtmPortSigVpi based on Integer32"""
    defaultValue = 0


_StnAtmPortSigVpi_Object = MibTableColumn
stnAtmPortSigVpi = _StnAtmPortSigVpi_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 15),
    _StnAtmPortSigVpi_Type()
)
stnAtmPortSigVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigVpi.setStatus("current")


class _StnAtmPortSigVci_Type(Integer32):
    """Custom type stnAtmPortSigVci based on Integer32"""
    defaultValue = 5


_StnAtmPortSigVci_Object = MibTableColumn
stnAtmPortSigVci = _StnAtmPortSigVci_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 16),
    _StnAtmPortSigVci_Type()
)
stnAtmPortSigVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigVci.setStatus("current")


class _StnAtmPortSigEnabled_Type(TruthValue):
    """Custom type stnAtmPortSigEnabled based on TruthValue"""


_StnAtmPortSigEnabled_Object = MibTableColumn
stnAtmPortSigEnabled = _StnAtmPortSigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 17),
    _StnAtmPortSigEnabled_Type()
)
stnAtmPortSigEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigEnabled.setStatus("current")


class _StnAtmPortIlmiVpi_Type(Integer32):
    """Custom type stnAtmPortIlmiVpi based on Integer32"""
    defaultValue = 0


_StnAtmPortIlmiVpi_Object = MibTableColumn
stnAtmPortIlmiVpi = _StnAtmPortIlmiVpi_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 18),
    _StnAtmPortIlmiVpi_Type()
)
stnAtmPortIlmiVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortIlmiVpi.setStatus("current")


class _StnAtmPortIlmiVci_Type(Integer32):
    """Custom type stnAtmPortIlmiVci based on Integer32"""
    defaultValue = 16


_StnAtmPortIlmiVci_Object = MibTableColumn
stnAtmPortIlmiVci = _StnAtmPortIlmiVci_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 19),
    _StnAtmPortIlmiVci_Type()
)
stnAtmPortIlmiVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortIlmiVci.setStatus("current")


class _StnAtmPortIlmiEnabled_Type(TruthValue):
    """Custom type stnAtmPortIlmiEnabled based on TruthValue"""


_StnAtmPortIlmiEnabled_Object = MibTableColumn
stnAtmPortIlmiEnabled = _StnAtmPortIlmiEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 20),
    _StnAtmPortIlmiEnabled_Type()
)
stnAtmPortIlmiEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortIlmiEnabled.setStatus("current")


class _StnAtmPortOamManagementEnabled_Type(TruthValue):
    """Custom type stnAtmPortOamManagementEnabled based on TruthValue"""


_StnAtmPortOamManagementEnabled_Object = MibTableColumn
stnAtmPortOamManagementEnabled = _StnAtmPortOamManagementEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 21),
    _StnAtmPortOamManagementEnabled_Type()
)
stnAtmPortOamManagementEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortOamManagementEnabled.setStatus("current")
_StnAtmPortOamXmtFrequency_Type = Integer32
_StnAtmPortOamXmtFrequency_Object = MibTableColumn
stnAtmPortOamXmtFrequency = _StnAtmPortOamXmtFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 22),
    _StnAtmPortOamXmtFrequency_Type()
)
stnAtmPortOamXmtFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortOamXmtFrequency.setStatus("current")
_StnAtmPortOamRetryUpCount_Type = Integer32
_StnAtmPortOamRetryUpCount_Object = MibTableColumn
stnAtmPortOamRetryUpCount = _StnAtmPortOamRetryUpCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 23),
    _StnAtmPortOamRetryUpCount_Type()
)
stnAtmPortOamRetryUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortOamRetryUpCount.setStatus("current")
_StnAtmPortOamRetryDownCount_Type = Integer32
_StnAtmPortOamRetryDownCount_Object = MibTableColumn
stnAtmPortOamRetryDownCount = _StnAtmPortOamRetryDownCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 24),
    _StnAtmPortOamRetryDownCount_Type()
)
stnAtmPortOamRetryDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortOamRetryDownCount.setStatus("current")
_StnAtmPortOamRetryFrequency_Type = Integer32
_StnAtmPortOamRetryFrequency_Object = MibTableColumn
stnAtmPortOamRetryFrequency = _StnAtmPortOamRetryFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 25),
    _StnAtmPortOamRetryFrequency_Type()
)
stnAtmPortOamRetryFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortOamRetryFrequency.setStatus("current")
_StnAtmPortOperStatus_Type = AtmPortOperStatus
_StnAtmPortOperStatus_Object = MibTableColumn
stnAtmPortOperStatus = _StnAtmPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 1, 1, 1, 26),
    _StnAtmPortOperStatus_Type()
)
stnAtmPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortOperStatus.setStatus("current")
_StnAtmPortIlmi_ObjectIdentity = ObjectIdentity
stnAtmPortIlmi = _StnAtmPortIlmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 2)
)
_StnAtmPortIlmiTable_Object = MibTable
stnAtmPortIlmiTable = _StnAtmPortIlmiTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    stnAtmPortIlmiTable.setStatus("current")
_StnAtmPortIlmiEntry_Object = MibTableRow
stnAtmPortIlmiEntry = _StnAtmPortIlmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 2, 1, 1)
)
stnAtmPortIlmiEntry.setIndexNames(
    (0, "STN-ATM-MIB", "stnAtmPortIlmiIfIndex"),
)
if mibBuilder.loadTexts:
    stnAtmPortIlmiEntry.setStatus("current")
_StnAtmPortIlmiIfIndex_Type = InterfaceIndex
_StnAtmPortIlmiIfIndex_Object = MibTableColumn
stnAtmPortIlmiIfIndex = _StnAtmPortIlmiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 2, 1, 1, 1),
    _StnAtmPortIlmiIfIndex_Type()
)
stnAtmPortIlmiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortIlmiIfIndex.setStatus("current")


class _StnAtmPortIlmiVersion_Type(Integer32):
    """Custom type stnAtmPortIlmiVersion based on Integer32"""
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
        *(("iisp-3-dot-1", 4),
          ("uni-3-dot-0", 1),
          ("uni-3-dot-1", 2),
          ("uni-4-dot-0", 3))
    )


_StnAtmPortIlmiVersion_Type.__name__ = "Integer32"
_StnAtmPortIlmiVersion_Object = MibTableColumn
stnAtmPortIlmiVersion = _StnAtmPortIlmiVersion_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 2, 1, 1, 2),
    _StnAtmPortIlmiVersion_Type()
)
stnAtmPortIlmiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortIlmiVersion.setStatus("current")


class _StnAtmPortIlmiNetworkOrientation_Type(Integer32):
    """Custom type stnAtmPortIlmiNetworkOrientation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 2),
          ("user", 1))
    )


_StnAtmPortIlmiNetworkOrientation_Type.__name__ = "Integer32"
_StnAtmPortIlmiNetworkOrientation_Object = MibTableColumn
stnAtmPortIlmiNetworkOrientation = _StnAtmPortIlmiNetworkOrientation_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 2, 1, 1, 3),
    _StnAtmPortIlmiNetworkOrientation_Type()
)
stnAtmPortIlmiNetworkOrientation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortIlmiNetworkOrientation.setStatus("current")


class _StnAtmPortIlmiAutoNegotiate_Type(TruthValue):
    """Custom type stnAtmPortIlmiAutoNegotiate based on TruthValue"""


_StnAtmPortIlmiAutoNegotiate_Object = MibTableColumn
stnAtmPortIlmiAutoNegotiate = _StnAtmPortIlmiAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 2, 1, 1, 4),
    _StnAtmPortIlmiAutoNegotiate_Type()
)
stnAtmPortIlmiAutoNegotiate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortIlmiAutoNegotiate.setStatus("current")


class _StnAtmPortIlmiPollInterval_Type(Integer32):
    """Custom type stnAtmPortIlmiPollInterval based on Integer32"""
    defaultValue = 1


_StnAtmPortIlmiPollInterval_Object = MibTableColumn
stnAtmPortIlmiPollInterval = _StnAtmPortIlmiPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 2, 1, 1, 5),
    _StnAtmPortIlmiPollInterval_Type()
)
stnAtmPortIlmiPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortIlmiPollInterval.setStatus("current")


class _StnAtmPortIlmiCheckConnectionInt_Type(Integer32):
    """Custom type stnAtmPortIlmiCheckConnectionInt based on Integer32"""
    defaultValue = 5


_StnAtmPortIlmiCheckConnectionInt_Object = MibTableColumn
stnAtmPortIlmiCheckConnectionInt = _StnAtmPortIlmiCheckConnectionInt_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 2, 1, 1, 6),
    _StnAtmPortIlmiCheckConnectionInt_Type()
)
stnAtmPortIlmiCheckConnectionInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortIlmiCheckConnectionInt.setStatus("current")


class _StnAtmPortIlmiInactivityFactor_Type(Integer32):
    """Custom type stnAtmPortIlmiInactivityFactor based on Integer32"""
    defaultValue = 4


_StnAtmPortIlmiInactivityFactor_Object = MibTableColumn
stnAtmPortIlmiInactivityFactor = _StnAtmPortIlmiInactivityFactor_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 2, 1, 1, 7),
    _StnAtmPortIlmiInactivityFactor_Type()
)
stnAtmPortIlmiInactivityFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortIlmiInactivityFactor.setStatus("current")


class _StnAtmPortIlmiLocalConn_Type(Integer32):
    """Custom type stnAtmPortIlmiLocalConn based on Integer32"""
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
        *(("other", 1),
          ("private", 3),
          ("public", 2))
    )


_StnAtmPortIlmiLocalConn_Type.__name__ = "Integer32"
_StnAtmPortIlmiLocalConn_Object = MibTableColumn
stnAtmPortIlmiLocalConn = _StnAtmPortIlmiLocalConn_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 2, 1, 1, 8),
    _StnAtmPortIlmiLocalConn_Type()
)
stnAtmPortIlmiLocalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortIlmiLocalConn.setStatus("current")


class _StnAtmPortIlmiAdminStatus_Type(Bits):
    """Custom type stnAtmPortIlmiAdminStatus based on Bits"""
    namedValues = NamedValues(
        *(("addr-reg", 1),
          ("connect", 2),
          ("std-ilmi", 0))
    )

_StnAtmPortIlmiAdminStatus_Type.__name__ = "Bits"
_StnAtmPortIlmiAdminStatus_Object = MibTableColumn
stnAtmPortIlmiAdminStatus = _StnAtmPortIlmiAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 2, 1, 1, 9),
    _StnAtmPortIlmiAdminStatus_Type()
)
stnAtmPortIlmiAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortIlmiAdminStatus.setStatus("current")
_StnAtmPortIlmiEnterprise_Type = ObjectIdentifier
_StnAtmPortIlmiEnterprise_Object = MibTableColumn
stnAtmPortIlmiEnterprise = _StnAtmPortIlmiEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 2, 1, 1, 10),
    _StnAtmPortIlmiEnterprise_Type()
)
stnAtmPortIlmiEnterprise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortIlmiEnterprise.setStatus("current")
_StnAtmPortIlmiLocalOid_Type = ObjectIdentifier
_StnAtmPortIlmiLocalOid_Object = MibTableColumn
stnAtmPortIlmiLocalOid = _StnAtmPortIlmiLocalOid_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 2, 1, 1, 11),
    _StnAtmPortIlmiLocalOid_Type()
)
stnAtmPortIlmiLocalOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortIlmiLocalOid.setStatus("current")


class _StnAtmPortIlmiNetPrefix_Type(OctetString):
    """Custom type stnAtmPortIlmiNetPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_StnAtmPortIlmiNetPrefix_Type.__name__ = "OctetString"
_StnAtmPortIlmiNetPrefix_Object = MibTableColumn
stnAtmPortIlmiNetPrefix = _StnAtmPortIlmiNetPrefix_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 2, 1, 1, 12),
    _StnAtmPortIlmiNetPrefix_Type()
)
stnAtmPortIlmiNetPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortIlmiNetPrefix.setStatus("current")
_StnAtmPortIlmiPrefixLen_Type = Integer32
_StnAtmPortIlmiPrefixLen_Object = MibTableColumn
stnAtmPortIlmiPrefixLen = _StnAtmPortIlmiPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 2, 1, 1, 13),
    _StnAtmPortIlmiPrefixLen_Type()
)
stnAtmPortIlmiPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortIlmiPrefixLen.setStatus("current")
_StnAtmPortSignaling_ObjectIdentity = ObjectIdentity
stnAtmPortSignaling = _StnAtmPortSignaling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3)
)
_StnAtmPortSigs_ObjectIdentity = ObjectIdentity
stnAtmPortSigs = _StnAtmPortSigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 1)
)
_StnAtmPortSigTable_Object = MibTable
stnAtmPortSigTable = _StnAtmPortSigTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 1, 1)
)
if mibBuilder.loadTexts:
    stnAtmPortSigTable.setStatus("current")
_StnAtmPortSigEntry_Object = MibTableRow
stnAtmPortSigEntry = _StnAtmPortSigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 1, 1, 1)
)
stnAtmPortSigEntry.setIndexNames(
    (0, "STN-ATM-MIB", "stnAtmPortSigIfIndex"),
)
if mibBuilder.loadTexts:
    stnAtmPortSigEntry.setStatus("current")
_StnAtmPortSigIfIndex_Type = InterfaceIndex
_StnAtmPortSigIfIndex_Object = MibTableColumn
stnAtmPortSigIfIndex = _StnAtmPortSigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 1, 1, 1, 1),
    _StnAtmPortSigIfIndex_Type()
)
stnAtmPortSigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigIfIndex.setStatus("current")


class _StnAtmPortSigVersion_Type(Integer32):
    """Custom type stnAtmPortSigVersion based on Integer32"""
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
        *(("iisp-3-dot-1", 3),
          ("pnni-1-dot-0", 4),
          ("uni-3-dot-0", 1),
          ("uni-3-dot-1", 2))
    )


_StnAtmPortSigVersion_Type.__name__ = "Integer32"
_StnAtmPortSigVersion_Object = MibTableColumn
stnAtmPortSigVersion = _StnAtmPortSigVersion_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 1, 1, 1, 2),
    _StnAtmPortSigVersion_Type()
)
stnAtmPortSigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigVersion.setStatus("current")


class _StnAtmPortSigNetworkOrientation_Type(Integer32):
    """Custom type stnAtmPortSigNetworkOrientation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 2),
          ("user", 1))
    )


_StnAtmPortSigNetworkOrientation_Type.__name__ = "Integer32"
_StnAtmPortSigNetworkOrientation_Object = MibTableColumn
stnAtmPortSigNetworkOrientation = _StnAtmPortSigNetworkOrientation_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 1, 1, 1, 3),
    _StnAtmPortSigNetworkOrientation_Type()
)
stnAtmPortSigNetworkOrientation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigNetworkOrientation.setStatus("current")


class _StnAtmPortSigAssignVpiVci_Type(TruthValue):
    """Custom type stnAtmPortSigAssignVpiVci based on TruthValue"""


_StnAtmPortSigAssignVpiVci_Object = MibTableColumn
stnAtmPortSigAssignVpiVci = _StnAtmPortSigAssignVpiVci_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 1, 1, 1, 4),
    _StnAtmPortSigAssignVpiVci_Type()
)
stnAtmPortSigAssignVpiVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stnAtmPortSigAssignVpiVci.setStatus("current")


class _StnAtmPortSigVpSigType_Type(Integer32):
    """Custom type stnAtmPortSigVpSigType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("associated-signaling", 1),
          ("explicit-vpci", 2))
    )


_StnAtmPortSigVpSigType_Type.__name__ = "Integer32"
_StnAtmPortSigVpSigType_Object = MibTableColumn
stnAtmPortSigVpSigType = _StnAtmPortSigVpSigType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 1, 1, 1, 5),
    _StnAtmPortSigVpSigType_Type()
)
stnAtmPortSigVpSigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigVpSigType.setStatus("current")


class _StnAtmPortSigParseMode_Type(Integer32):
    """Custom type stnAtmPortSigParseMode based on Integer32"""
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
          ("strict", 2))
    )


_StnAtmPortSigParseMode_Type.__name__ = "Integer32"
_StnAtmPortSigParseMode_Object = MibTableColumn
stnAtmPortSigParseMode = _StnAtmPortSigParseMode_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 1, 1, 1, 6),
    _StnAtmPortSigParseMode_Type()
)
stnAtmPortSigParseMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigParseMode.setStatus("current")


class _StnAtmPortSigPrefCarrierPresent_Type(TruthValue):
    """Custom type stnAtmPortSigPrefCarrierPresent based on TruthValue"""


_StnAtmPortSigPrefCarrierPresent_Object = MibTableColumn
stnAtmPortSigPrefCarrierPresent = _StnAtmPortSigPrefCarrierPresent_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 1, 1, 1, 7),
    _StnAtmPortSigPrefCarrierPresent_Type()
)
stnAtmPortSigPrefCarrierPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigPrefCarrierPresent.setStatus("current")
_StnAtmPortSigPrefCarrier_Type = TruthValue
_StnAtmPortSigPrefCarrier_Object = MibTableColumn
stnAtmPortSigPrefCarrier = _StnAtmPortSigPrefCarrier_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 1, 1, 1, 8),
    _StnAtmPortSigPrefCarrier_Type()
)
stnAtmPortSigPrefCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigPrefCarrier.setStatus("current")
_StnAtmPortSigDurations_ObjectIdentity = ObjectIdentity
stnAtmPortSigDurations = _StnAtmPortSigDurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 2)
)
_StnAtmPortSigDurationTable_Object = MibTable
stnAtmPortSigDurationTable = _StnAtmPortSigDurationTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 2, 1)
)
if mibBuilder.loadTexts:
    stnAtmPortSigDurationTable.setStatus("current")
_StnAtmPortSigDurationEntry_Object = MibTableRow
stnAtmPortSigDurationEntry = _StnAtmPortSigDurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 2, 1, 1)
)
stnAtmPortSigDurationEntry.setIndexNames(
    (0, "STN-ATM-MIB", "stnAtmPortSigDurIfIndex"),
)
if mibBuilder.loadTexts:
    stnAtmPortSigDurationEntry.setStatus("current")
_StnAtmPortSigDurIfIndex_Type = InterfaceIndex
_StnAtmPortSigDurIfIndex_Object = MibTableColumn
stnAtmPortSigDurIfIndex = _StnAtmPortSigDurIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 2, 1, 1, 1),
    _StnAtmPortSigDurIfIndex_Type()
)
stnAtmPortSigDurIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigDurIfIndex.setStatus("current")


class _StnAtmPortSigT301Duration_Type(Integer32):
    """Custom type stnAtmPortSigT301Duration based on Integer32"""
    defaultValue = 180000


_StnAtmPortSigT301Duration_Object = MibTableColumn
stnAtmPortSigT301Duration = _StnAtmPortSigT301Duration_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 2, 1, 1, 2),
    _StnAtmPortSigT301Duration_Type()
)
stnAtmPortSigT301Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigT301Duration.setStatus("current")


class _StnAtmPortSigT303Duration_Type(Integer32):
    """Custom type stnAtmPortSigT303Duration based on Integer32"""
    defaultValue = 4000


_StnAtmPortSigT303Duration_Object = MibTableColumn
stnAtmPortSigT303Duration = _StnAtmPortSigT303Duration_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 2, 1, 1, 3),
    _StnAtmPortSigT303Duration_Type()
)
stnAtmPortSigT303Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigT303Duration.setStatus("current")


class _StnAtmPortSigT306Duration_Type(Integer32):
    """Custom type stnAtmPortSigT306Duration based on Integer32"""
    defaultValue = 30000


_StnAtmPortSigT306Duration_Object = MibTableColumn
stnAtmPortSigT306Duration = _StnAtmPortSigT306Duration_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 2, 1, 1, 4),
    _StnAtmPortSigT306Duration_Type()
)
stnAtmPortSigT306Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigT306Duration.setStatus("current")


class _StnAtmPortSigT308Duration_Type(Integer32):
    """Custom type stnAtmPortSigT308Duration based on Integer32"""
    defaultValue = 30000


_StnAtmPortSigT308Duration_Object = MibTableColumn
stnAtmPortSigT308Duration = _StnAtmPortSigT308Duration_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 2, 1, 1, 5),
    _StnAtmPortSigT308Duration_Type()
)
stnAtmPortSigT308Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigT308Duration.setStatus("current")


class _StnAtmPortSigT309Duration_Type(Integer32):
    """Custom type stnAtmPortSigT309Duration based on Integer32"""
    defaultValue = 10000


_StnAtmPortSigT309Duration_Object = MibTableColumn
stnAtmPortSigT309Duration = _StnAtmPortSigT309Duration_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 2, 1, 1, 6),
    _StnAtmPortSigT309Duration_Type()
)
stnAtmPortSigT309Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigT309Duration.setStatus("current")


class _StnAtmPortSigT310Duration_Type(Integer32):
    """Custom type stnAtmPortSigT310Duration based on Integer32"""
    defaultValue = 10000


_StnAtmPortSigT310Duration_Object = MibTableColumn
stnAtmPortSigT310Duration = _StnAtmPortSigT310Duration_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 2, 1, 1, 7),
    _StnAtmPortSigT310Duration_Type()
)
stnAtmPortSigT310Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigT310Duration.setStatus("current")


class _StnAtmPortSigT313Duration_Type(Integer32):
    """Custom type stnAtmPortSigT313Duration based on Integer32"""
    defaultValue = 30000


_StnAtmPortSigT313Duration_Object = MibTableColumn
stnAtmPortSigT313Duration = _StnAtmPortSigT313Duration_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 2, 1, 1, 8),
    _StnAtmPortSigT313Duration_Type()
)
stnAtmPortSigT313Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigT313Duration.setStatus("current")


class _StnAtmPortSigT316Duration_Type(Integer32):
    """Custom type stnAtmPortSigT316Duration based on Integer32"""
    defaultValue = 120000


_StnAtmPortSigT316Duration_Object = MibTableColumn
stnAtmPortSigT316Duration = _StnAtmPortSigT316Duration_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 2, 1, 1, 9),
    _StnAtmPortSigT316Duration_Type()
)
stnAtmPortSigT316Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigT316Duration.setStatus("current")


class _StnAtmPortSigT317Duration_Type(Integer32):
    """Custom type stnAtmPortSigT317Duration based on Integer32"""
    defaultValue = 60000


_StnAtmPortSigT317Duration_Object = MibTableColumn
stnAtmPortSigT317Duration = _StnAtmPortSigT317Duration_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 2, 1, 1, 10),
    _StnAtmPortSigT317Duration_Type()
)
stnAtmPortSigT317Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigT317Duration.setStatus("current")


class _StnAtmPortSigT322Duration_Type(Integer32):
    """Custom type stnAtmPortSigT322Duration based on Integer32"""
    defaultValue = 4000


_StnAtmPortSigT322Duration_Object = MibTableColumn
stnAtmPortSigT322Duration = _StnAtmPortSigT322Duration_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 2, 1, 1, 11),
    _StnAtmPortSigT322Duration_Type()
)
stnAtmPortSigT322Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigT322Duration.setStatus("current")


class _StnAtmPortSigT331Duration_Type(Integer32):
    """Custom type stnAtmPortSigT331Duration based on Integer32"""
    defaultValue = 60000


_StnAtmPortSigT331Duration_Object = MibTableColumn
stnAtmPortSigT331Duration = _StnAtmPortSigT331Duration_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 2, 1, 1, 12),
    _StnAtmPortSigT331Duration_Type()
)
stnAtmPortSigT331Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigT331Duration.setStatus("current")


class _StnAtmPortSigT333Duration_Type(Integer32):
    """Custom type stnAtmPortSigT333Duration based on Integer32"""
    defaultValue = 10000


_StnAtmPortSigT333Duration_Object = MibTableColumn
stnAtmPortSigT333Duration = _StnAtmPortSigT333Duration_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 2, 1, 1, 13),
    _StnAtmPortSigT333Duration_Type()
)
stnAtmPortSigT333Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigT333Duration.setStatus("current")


class _StnAtmPortSigT397Duration_Type(Integer32):
    """Custom type stnAtmPortSigT397Duration based on Integer32"""
    defaultValue = 180000


_StnAtmPortSigT397Duration_Object = MibTableColumn
stnAtmPortSigT397Duration = _StnAtmPortSigT397Duration_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 2, 1, 1, 14),
    _StnAtmPortSigT397Duration_Type()
)
stnAtmPortSigT397Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigT397Duration.setStatus("current")


class _StnAtmPortSigT398Duration_Type(Integer32):
    """Custom type stnAtmPortSigT398Duration based on Integer32"""
    defaultValue = 4000


_StnAtmPortSigT398Duration_Object = MibTableColumn
stnAtmPortSigT398Duration = _StnAtmPortSigT398Duration_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 2, 1, 1, 15),
    _StnAtmPortSigT398Duration_Type()
)
stnAtmPortSigT398Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigT398Duration.setStatus("current")


class _StnAtmPortSigT399Duration_Type(Integer32):
    """Custom type stnAtmPortSigT399Duration based on Integer32"""
    defaultValue = 14000


_StnAtmPortSigT399Duration_Object = MibTableColumn
stnAtmPortSigT399Duration = _StnAtmPortSigT399Duration_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 2, 1, 1, 16),
    _StnAtmPortSigT399Duration_Type()
)
stnAtmPortSigT399Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigT399Duration.setStatus("current")


class _StnAtmPortSigSaalRetryDuration_Type(Integer32):
    """Custom type stnAtmPortSigSaalRetryDuration based on Integer32"""
    defaultValue = 10000


_StnAtmPortSigSaalRetryDuration_Object = MibTableColumn
stnAtmPortSigSaalRetryDuration = _StnAtmPortSigSaalRetryDuration_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 2, 1, 1, 17),
    _StnAtmPortSigSaalRetryDuration_Type()
)
stnAtmPortSigSaalRetryDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigSaalRetryDuration.setStatus("current")
_StnAtmPortSigRetries_ObjectIdentity = ObjectIdentity
stnAtmPortSigRetries = _StnAtmPortSigRetries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 3)
)
_StnAtmPortSigRetryTable_Object = MibTable
stnAtmPortSigRetryTable = _StnAtmPortSigRetryTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 3, 1)
)
if mibBuilder.loadTexts:
    stnAtmPortSigRetryTable.setStatus("current")
_StnAtmPortSigRetryEntry_Object = MibTableRow
stnAtmPortSigRetryEntry = _StnAtmPortSigRetryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 3, 1, 1)
)
stnAtmPortSigRetryEntry.setIndexNames(
    (0, "STN-ATM-MIB", "stnAtmPortSigRetryIfIndex"),
)
if mibBuilder.loadTexts:
    stnAtmPortSigRetryEntry.setStatus("current")
_StnAtmPortSigRetryIfIndex_Type = InterfaceIndex
_StnAtmPortSigRetryIfIndex_Object = MibTableColumn
stnAtmPortSigRetryIfIndex = _StnAtmPortSigRetryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 3, 1, 1, 1),
    _StnAtmPortSigRetryIfIndex_Type()
)
stnAtmPortSigRetryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigRetryIfIndex.setStatus("current")


class _StnAtmPortSigT303Retries_Type(Integer32):
    """Custom type stnAtmPortSigT303Retries based on Integer32"""
    defaultValue = 1


_StnAtmPortSigT303Retries_Object = MibTableColumn
stnAtmPortSigT303Retries = _StnAtmPortSigT303Retries_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 3, 1, 1, 2),
    _StnAtmPortSigT303Retries_Type()
)
stnAtmPortSigT303Retries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigT303Retries.setStatus("current")


class _StnAtmPortSigT308Retries_Type(Integer32):
    """Custom type stnAtmPortSigT308Retries based on Integer32"""
    defaultValue = 1


_StnAtmPortSigT308Retries_Object = MibTableColumn
stnAtmPortSigT308Retries = _StnAtmPortSigT308Retries_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 3, 1, 1, 3),
    _StnAtmPortSigT308Retries_Type()
)
stnAtmPortSigT308Retries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigT308Retries.setStatus("current")


class _StnAtmPortSigT316Retries_Type(Integer32):
    """Custom type stnAtmPortSigT316Retries based on Integer32"""
    defaultValue = 1


_StnAtmPortSigT316Retries_Object = MibTableColumn
stnAtmPortSigT316Retries = _StnAtmPortSigT316Retries_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 3, 1, 1, 4),
    _StnAtmPortSigT316Retries_Type()
)
stnAtmPortSigT316Retries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigT316Retries.setStatus("current")


class _StnAtmPortSigT322Retries_Type(Integer32):
    """Custom type stnAtmPortSigT322Retries based on Integer32"""
    defaultValue = 1


_StnAtmPortSigT322Retries_Object = MibTableColumn
stnAtmPortSigT322Retries = _StnAtmPortSigT322Retries_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 3, 1, 1, 5),
    _StnAtmPortSigT322Retries_Type()
)
stnAtmPortSigT322Retries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigT322Retries.setStatus("current")


class _StnAtmPortSigT331Retries_Type(Integer32):
    """Custom type stnAtmPortSigT331Retries based on Integer32"""
    defaultValue = 1


_StnAtmPortSigT331Retries_Object = MibTableColumn
stnAtmPortSigT331Retries = _StnAtmPortSigT331Retries_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 3, 1, 1, 6),
    _StnAtmPortSigT331Retries_Type()
)
stnAtmPortSigT331Retries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigT331Retries.setStatus("current")
_StnAtmPortSigSSCSTable_Object = MibTable
stnAtmPortSigSSCSTable = _StnAtmPortSigSSCSTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 3, 2)
)
if mibBuilder.loadTexts:
    stnAtmPortSigSSCSTable.setStatus("current")
_StnAtmPortSigSSCSEntry_Object = MibTableRow
stnAtmPortSigSSCSEntry = _StnAtmPortSigSSCSEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 3, 2, 1)
)
stnAtmPortSigSSCSEntry.setIndexNames(
    (0, "STN-ATM-MIB", "stnAtmPortSigSSCSIfIndex"),
)
if mibBuilder.loadTexts:
    stnAtmPortSigSSCSEntry.setStatus("current")
_StnAtmPortSigSSCSIfIndex_Type = InterfaceIndex
_StnAtmPortSigSSCSIfIndex_Object = MibTableColumn
stnAtmPortSigSSCSIfIndex = _StnAtmPortSigSSCSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 3, 2, 1, 1),
    _StnAtmPortSigSSCSIfIndex_Type()
)
stnAtmPortSigSSCSIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigSSCSIfIndex.setStatus("current")


class _StnAtmPortSigSSCSPollDuration_Type(Integer32):
    """Custom type stnAtmPortSigSSCSPollDuration based on Integer32"""
    defaultValue = 750


_StnAtmPortSigSSCSPollDuration_Object = MibTableColumn
stnAtmPortSigSSCSPollDuration = _StnAtmPortSigSSCSPollDuration_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 3, 2, 1, 2),
    _StnAtmPortSigSSCSPollDuration_Type()
)
stnAtmPortSigSSCSPollDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigSSCSPollDuration.setStatus("current")


class _StnAtmPortSigSSCSKeepAliveDuration_Type(Integer32):
    """Custom type stnAtmPortSigSSCSKeepAliveDuration based on Integer32"""
    defaultValue = 2000


_StnAtmPortSigSSCSKeepAliveDuration_Object = MibTableColumn
stnAtmPortSigSSCSKeepAliveDuration = _StnAtmPortSigSSCSKeepAliveDuration_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 3, 2, 1, 3),
    _StnAtmPortSigSSCSKeepAliveDuration_Type()
)
stnAtmPortSigSSCSKeepAliveDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigSSCSKeepAliveDuration.setStatus("current")


class _StnAtmPortSigSSCSIdleDuration_Type(Integer32):
    """Custom type stnAtmPortSigSSCSIdleDuration based on Integer32"""
    defaultValue = 15000


_StnAtmPortSigSSCSIdleDuration_Object = MibTableColumn
stnAtmPortSigSSCSIdleDuration = _StnAtmPortSigSSCSIdleDuration_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 3, 2, 1, 4),
    _StnAtmPortSigSSCSIdleDuration_Type()
)
stnAtmPortSigSSCSIdleDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigSSCSIdleDuration.setStatus("current")


class _StnAtmPortSigSSCSNoRspDuration_Type(Integer32):
    """Custom type stnAtmPortSigSSCSNoRspDuration based on Integer32"""
    defaultValue = 7000


_StnAtmPortSigSSCSNoRspDuration_Object = MibTableColumn
stnAtmPortSigSSCSNoRspDuration = _StnAtmPortSigSSCSNoRspDuration_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 3, 2, 1, 5),
    _StnAtmPortSigSSCSNoRspDuration_Type()
)
stnAtmPortSigSSCSNoRspDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigSSCSNoRspDuration.setStatus("current")


class _StnAtmPortSigSSCSCcDuration_Type(Integer32):
    """Custom type stnAtmPortSigSSCSCcDuration based on Integer32"""
    defaultValue = 1000


_StnAtmPortSigSSCSCcDuration_Object = MibTableColumn
stnAtmPortSigSSCSCcDuration = _StnAtmPortSigSSCSCcDuration_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 3, 2, 1, 6),
    _StnAtmPortSigSSCSCcDuration_Type()
)
stnAtmPortSigSSCSCcDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigSSCSCcDuration.setStatus("current")


class _StnAtmPortSigSSCSMaxRcvWindowSize_Type(Integer32):
    """Custom type stnAtmPortSigSSCSMaxRcvWindowSize based on Integer32"""
    defaultValue = 20


_StnAtmPortSigSSCSMaxRcvWindowSize_Object = MibTableColumn
stnAtmPortSigSSCSMaxRcvWindowSize = _StnAtmPortSigSSCSMaxRcvWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 3, 2, 1, 7),
    _StnAtmPortSigSSCSMaxRcvWindowSize_Type()
)
stnAtmPortSigSSCSMaxRcvWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigSSCSMaxRcvWindowSize.setStatus("current")


class _StnAtmPortSigSSCSMaxCcRetries_Type(Integer32):
    """Custom type stnAtmPortSigSSCSMaxCcRetries based on Integer32"""
    defaultValue = 4


_StnAtmPortSigSSCSMaxCcRetries_Object = MibTableColumn
stnAtmPortSigSSCSMaxCcRetries = _StnAtmPortSigSSCSMaxCcRetries_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 3, 2, 1, 8),
    _StnAtmPortSigSSCSMaxCcRetries_Type()
)
stnAtmPortSigSSCSMaxCcRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigSSCSMaxCcRetries.setStatus("current")


class _StnAtmPortSigSSCSMaxSdBetwPolls_Type(Integer32):
    """Custom type stnAtmPortSigSSCSMaxSdBetwPolls based on Integer32"""
    defaultValue = 25


_StnAtmPortSigSSCSMaxSdBetwPolls_Object = MibTableColumn
stnAtmPortSigSSCSMaxSdBetwPolls = _StnAtmPortSigSSCSMaxSdBetwPolls_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 3, 2, 1, 9),
    _StnAtmPortSigSSCSMaxSdBetwPolls_Type()
)
stnAtmPortSigSSCSMaxSdBetwPolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigSSCSMaxSdBetwPolls.setStatus("current")


class _StnAtmPortSigSSCSMaxStatListElms_Type(Integer32):
    """Custom type stnAtmPortSigSSCSMaxStatListElms based on Integer32"""
    defaultValue = 67


_StnAtmPortSigSSCSMaxStatListElms_Object = MibTableColumn
stnAtmPortSigSSCSMaxStatListElms = _StnAtmPortSigSSCSMaxStatListElms_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 3, 2, 1, 10),
    _StnAtmPortSigSSCSMaxStatListElms_Type()
)
stnAtmPortSigSSCSMaxStatListElms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigSSCSMaxStatListElms.setStatus("current")


class _StnAtmPortSigSSCSPollAfterRetrans_Type(TruthValue):
    """Custom type stnAtmPortSigSSCSPollAfterRetrans based on TruthValue"""


_StnAtmPortSigSSCSPollAfterRetrans_Object = MibTableColumn
stnAtmPortSigSSCSPollAfterRetrans = _StnAtmPortSigSSCSPollAfterRetrans_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 3, 2, 1, 11),
    _StnAtmPortSigSSCSPollAfterRetrans_Type()
)
stnAtmPortSigSSCSPollAfterRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigSSCSPollAfterRetrans.setStatus("current")


class _StnAtmPortSigSSCSRepeatUstat_Type(TruthValue):
    """Custom type stnAtmPortSigSSCSRepeatUstat based on TruthValue"""


_StnAtmPortSigSSCSRepeatUstat_Object = MibTableColumn
stnAtmPortSigSSCSRepeatUstat = _StnAtmPortSigSSCSRepeatUstat_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 3, 2, 1, 12),
    _StnAtmPortSigSSCSRepeatUstat_Type()
)
stnAtmPortSigSSCSRepeatUstat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigSSCSRepeatUstat.setStatus("current")


class _StnAtmPortSigSSCSUstatRspToPoll_Type(TruthValue):
    """Custom type stnAtmPortSigSSCSUstatRspToPoll based on TruthValue"""


_StnAtmPortSigSSCSUstatRspToPoll_Object = MibTableColumn
stnAtmPortSigSSCSUstatRspToPoll = _StnAtmPortSigSSCSUstatRspToPoll_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 3, 3, 2, 1, 13),
    _StnAtmPortSigSSCSUstatRspToPoll_Type()
)
stnAtmPortSigSSCSUstatRspToPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortSigSSCSUstatRspToPoll.setStatus("current")
_StnAtmPortTraffic_ObjectIdentity = ObjectIdentity
stnAtmPortTraffic = _StnAtmPortTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 4)
)
_StnAtmPortTrafficTable_Object = MibTable
stnAtmPortTrafficTable = _StnAtmPortTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 4, 1)
)
if mibBuilder.loadTexts:
    stnAtmPortTrafficTable.setStatus("current")
_StnAtmPortTrafficEntry_Object = MibTableRow
stnAtmPortTrafficEntry = _StnAtmPortTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 4, 1, 1)
)
stnAtmPortTrafficEntry.setIndexNames(
    (0, "STN-ATM-MIB", "stnAtmPortTrafIndex"),
)
if mibBuilder.loadTexts:
    stnAtmPortTrafficEntry.setStatus("current")
_StnAtmPortTrafIndex_Type = InterfaceIndex
_StnAtmPortTrafIndex_Object = MibTableColumn
stnAtmPortTrafIndex = _StnAtmPortTrafIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 4, 1, 1, 1),
    _StnAtmPortTrafIndex_Type()
)
stnAtmPortTrafIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortTrafIndex.setStatus("current")
_StnAtmPortTrafTxCells_Type = Counter32
_StnAtmPortTrafTxCells_Object = MibTableColumn
stnAtmPortTrafTxCells = _StnAtmPortTrafTxCells_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 4, 1, 1, 2),
    _StnAtmPortTrafTxCells_Type()
)
stnAtmPortTrafTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortTrafTxCells.setStatus("current")
_StnAtmPortTrafRxCells_Type = Counter32
_StnAtmPortTrafRxCells_Object = MibTableColumn
stnAtmPortTrafRxCells = _StnAtmPortTrafRxCells_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 4, 1, 1, 3),
    _StnAtmPortTrafRxCells_Type()
)
stnAtmPortTrafRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortTrafRxCells.setStatus("current")
_StnAtmPortTrafTxParityErrors_Type = Counter32
_StnAtmPortTrafTxParityErrors_Object = MibTableColumn
stnAtmPortTrafTxParityErrors = _StnAtmPortTrafTxParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 4, 1, 1, 4),
    _StnAtmPortTrafTxParityErrors_Type()
)
stnAtmPortTrafTxParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortTrafTxParityErrors.setStatus("current")
_StnAtmPortTrafRxHdrChkSumErrors_Type = Counter32
_StnAtmPortTrafRxHdrChkSumErrors_Object = MibTableColumn
stnAtmPortTrafRxHdrChkSumErrors = _StnAtmPortTrafRxHdrChkSumErrors_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 4, 1, 1, 5),
    _StnAtmPortTrafRxHdrChkSumErrors_Type()
)
stnAtmPortTrafRxHdrChkSumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortTrafRxHdrChkSumErrors.setStatus("current")
_StnAtmPortTrafPhyParityErrors_Type = Counter32
_StnAtmPortTrafPhyParityErrors_Object = MibTableColumn
stnAtmPortTrafPhyParityErrors = _StnAtmPortTrafPhyParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 4, 1, 1, 6),
    _StnAtmPortTrafPhyParityErrors_Type()
)
stnAtmPortTrafPhyParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortTrafPhyParityErrors.setStatus("current")
_StnAtmPortTrafCrc10Errors_Type = Counter32
_StnAtmPortTrafCrc10Errors_Object = MibTableColumn
stnAtmPortTrafCrc10Errors = _StnAtmPortTrafCrc10Errors_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 4, 4, 1, 1, 7),
    _StnAtmPortTrafCrc10Errors_Type()
)
stnAtmPortTrafCrc10Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmPortTrafCrc10Errors.setStatus("current")
_StnAtmTraces_ObjectIdentity = ObjectIdentity
stnAtmTraces = _StnAtmTraces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 5)
)
_StnTraceIps_ObjectIdentity = ObjectIdentity
stnTraceIps = _StnTraceIps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 5, 1)
)


class _StnTraceIpsEnabled_Type(TruthValue):
    """Custom type stnTraceIpsEnabled based on TruthValue"""


_StnTraceIpsEnabled_Object = MibScalar
stnTraceIpsEnabled = _StnTraceIpsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 5, 1, 1),
    _StnTraceIpsEnabled_Type()
)
stnTraceIpsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnTraceIpsEnabled.setStatus("current")


class _StnTraceIpsSize_Type(Integer32):
    """Custom type stnTraceIpsSize based on Integer32"""
    defaultValue = 1000


_StnTraceIpsSize_Object = MibScalar
stnTraceIpsSize = _StnTraceIpsSize_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 5, 1, 2),
    _StnTraceIpsSize_Type()
)
stnTraceIpsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnTraceIpsSize.setStatus("current")


class _StnTraceIpsFile_Type(OctetString):
    """Custom type stnTraceIpsFile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StnTraceIpsFile_Type.__name__ = "OctetString"
_StnTraceIpsFile_Object = MibScalar
stnTraceIpsFile = _StnTraceIpsFile_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 5, 1, 3),
    _StnTraceIpsFile_Type()
)
stnTraceIpsFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnTraceIpsFile.setStatus("current")
_StnTracePd_ObjectIdentity = ObjectIdentity
stnTracePd = _StnTracePd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 5, 2)
)


class _StnTracePdProblemEnabled_Type(TruthValue):
    """Custom type stnTracePdProblemEnabled based on TruthValue"""


_StnTracePdProblemEnabled_Object = MibScalar
stnTracePdProblemEnabled = _StnTracePdProblemEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 5, 2, 1),
    _StnTracePdProblemEnabled_Type()
)
stnTracePdProblemEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnTracePdProblemEnabled.setStatus("current")


class _StnTracePdExceptionEnabled_Type(TruthValue):
    """Custom type stnTracePdExceptionEnabled based on TruthValue"""


_StnTracePdExceptionEnabled_Object = MibScalar
stnTracePdExceptionEnabled = _StnTracePdExceptionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 5, 2, 2),
    _StnTracePdExceptionEnabled_Type()
)
stnTracePdExceptionEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnTracePdExceptionEnabled.setStatus("current")


class _StnTracePdAuditEnabled_Type(TruthValue):
    """Custom type stnTracePdAuditEnabled based on TruthValue"""


_StnTracePdAuditEnabled_Object = MibScalar
stnTracePdAuditEnabled = _StnTracePdAuditEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 5, 2, 3),
    _StnTracePdAuditEnabled_Type()
)
stnTracePdAuditEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnTracePdAuditEnabled.setStatus("current")


class _StnTracePdDeveloperEnabled_Type(TruthValue):
    """Custom type stnTracePdDeveloperEnabled based on TruthValue"""


_StnTracePdDeveloperEnabled_Object = MibScalar
stnTracePdDeveloperEnabled = _StnTracePdDeveloperEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 5, 2, 4),
    _StnTracePdDeveloperEnabled_Type()
)
stnTracePdDeveloperEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnTracePdDeveloperEnabled.setStatus("current")


class _StnTracePdSize_Type(Integer32):
    """Custom type stnTracePdSize based on Integer32"""
    defaultValue = 25


_StnTracePdSize_Object = MibScalar
stnTracePdSize = _StnTracePdSize_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 5, 2, 5),
    _StnTracePdSize_Type()
)
stnTracePdSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnTracePdSize.setStatus("current")


class _StnTracePdFile_Type(OctetString):
    """Custom type stnTracePdFile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StnTracePdFile_Type.__name__ = "OctetString"
_StnTracePdFile_Object = MibScalar
stnTracePdFile = _StnTracePdFile_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 5, 2, 6),
    _StnTracePdFile_Type()
)
stnTracePdFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnTracePdFile.setStatus("current")
_StnAtmQos_ObjectIdentity = ObjectIdentity
stnAtmQos = _StnAtmQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 6)
)
_StnQosCLR_ObjectIdentity = ObjectIdentity
stnQosCLR = _StnQosCLR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 6, 1)
)
_StnQosClass1CLR_Type = Integer32
_StnQosClass1CLR_Object = MibScalar
stnQosClass1CLR = _StnQosClass1CLR_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 6, 1, 1),
    _StnQosClass1CLR_Type()
)
stnQosClass1CLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnQosClass1CLR.setStatus("current")
_StnQosClass2CLR_Type = Integer32
_StnQosClass2CLR_Object = MibScalar
stnQosClass2CLR = _StnQosClass2CLR_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 6, 1, 2),
    _StnQosClass2CLR_Type()
)
stnQosClass2CLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnQosClass2CLR.setStatus("current")
_StnQosClass3CLR_Type = Integer32
_StnQosClass3CLR_Object = MibScalar
stnQosClass3CLR = _StnQosClass3CLR_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 6, 1, 3),
    _StnQosClass3CLR_Type()
)
stnQosClass3CLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnQosClass3CLR.setStatus("current")
_StnQosClass4CLR_Type = Integer32
_StnQosClass4CLR_Object = MibScalar
stnQosClass4CLR = _StnQosClass4CLR_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 6, 1, 4),
    _StnQosClass4CLR_Type()
)
stnQosClass4CLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnQosClass4CLR.setStatus("current")
_StnQosCDV_ObjectIdentity = ObjectIdentity
stnQosCDV = _StnQosCDV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 6, 2)
)
_StnQosClass1CDV_Type = Integer32
_StnQosClass1CDV_Object = MibScalar
stnQosClass1CDV = _StnQosClass1CDV_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 6, 2, 1),
    _StnQosClass1CDV_Type()
)
stnQosClass1CDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnQosClass1CDV.setStatus("current")
_StnQosClass2CDV_Type = Integer32
_StnQosClass2CDV_Object = MibScalar
stnQosClass2CDV = _StnQosClass2CDV_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 6, 2, 2),
    _StnQosClass2CDV_Type()
)
stnQosClass2CDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnQosClass2CDV.setStatus("current")
_StnQosClass3CDV_Type = Integer32
_StnQosClass3CDV_Object = MibScalar
stnQosClass3CDV = _StnQosClass3CDV_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 6, 2, 3),
    _StnQosClass3CDV_Type()
)
stnQosClass3CDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnQosClass3CDV.setStatus("current")
_StnQosClass4CDV_Type = Integer32
_StnQosClass4CDV_Object = MibScalar
stnQosClass4CDV = _StnQosClass4CDV_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 6, 2, 4),
    _StnQosClass4CDV_Type()
)
stnQosClass4CDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnQosClass4CDV.setStatus("current")
_StnQosCTD_ObjectIdentity = ObjectIdentity
stnQosCTD = _StnQosCTD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 6, 3)
)
_StnQosClass1MaxCTD_Type = Integer32
_StnQosClass1MaxCTD_Object = MibScalar
stnQosClass1MaxCTD = _StnQosClass1MaxCTD_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 6, 3, 1),
    _StnQosClass1MaxCTD_Type()
)
stnQosClass1MaxCTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnQosClass1MaxCTD.setStatus("current")
_StnQosClass2MaxCTD_Type = Integer32
_StnQosClass2MaxCTD_Object = MibScalar
stnQosClass2MaxCTD = _StnQosClass2MaxCTD_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 6, 3, 2),
    _StnQosClass2MaxCTD_Type()
)
stnQosClass2MaxCTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnQosClass2MaxCTD.setStatus("current")
_StnQosClass3MaxCTD_Type = Integer32
_StnQosClass3MaxCTD_Object = MibScalar
stnQosClass3MaxCTD = _StnQosClass3MaxCTD_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 6, 3, 3),
    _StnQosClass3MaxCTD_Type()
)
stnQosClass3MaxCTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnQosClass3MaxCTD.setStatus("current")
_StnQosClass4MaxCTD_Type = Integer32
_StnQosClass4MaxCTD_Object = MibScalar
stnQosClass4MaxCTD = _StnQosClass4MaxCTD_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 6, 3, 4),
    _StnQosClass4MaxCTD_Type()
)
stnQosClass4MaxCTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnQosClass4MaxCTD.setStatus("current")
_StnAtmAddresses_ObjectIdentity = ObjectIdentity
stnAtmAddresses = _StnAtmAddresses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 7)
)
_StnAtmAddressTable_Object = MibTable
stnAtmAddressTable = _StnAtmAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 7, 1)
)
if mibBuilder.loadTexts:
    stnAtmAddressTable.setStatus("current")
_StnAtmAddressEntry_Object = MibTableRow
stnAtmAddressEntry = _StnAtmAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 7, 1, 1)
)
stnAtmAddressEntry.setIndexNames(
    (0, "STN-ATM-MIB", "stnAtmAddrIfIndex"),
    (0, "STN-ATM-MIB", "stnAtmAddrAddress"),
)
if mibBuilder.loadTexts:
    stnAtmAddressEntry.setStatus("current")
_StnAtmAddrIfIndex_Type = InterfaceIndex
_StnAtmAddrIfIndex_Object = MibTableColumn
stnAtmAddrIfIndex = _StnAtmAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 7, 1, 1, 1),
    _StnAtmAddrIfIndex_Type()
)
stnAtmAddrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmAddrIfIndex.setStatus("current")
_StnAtmAddrAddress_Type = NSAPAddress
_StnAtmAddrAddress_Object = MibTableColumn
stnAtmAddrAddress = _StnAtmAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 7, 1, 1, 2),
    _StnAtmAddrAddress_Type()
)
stnAtmAddrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmAddrAddress.setStatus("current")
_StnAtmAddrAddressLen_Type = Integer32
_StnAtmAddrAddressLen_Object = MibTableColumn
stnAtmAddrAddressLen = _StnAtmAddrAddressLen_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 7, 1, 1, 3),
    _StnAtmAddrAddressLen_Type()
)
stnAtmAddrAddressLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmAddrAddressLen.setStatus("current")
_StnAtmThresholds_ObjectIdentity = ObjectIdentity
stnAtmThresholds = _StnAtmThresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 8)
)
_StnAtmThresholdTable_Object = MibTable
stnAtmThresholdTable = _StnAtmThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 8, 1)
)
if mibBuilder.loadTexts:
    stnAtmThresholdTable.setStatus("current")
_StnAtmThresholdEntry_Object = MibTableRow
stnAtmThresholdEntry = _StnAtmThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 8, 1, 1)
)
stnAtmThresholdEntry.setIndexNames(
    (0, "STN-ATM-MIB", "stnAtmTholdTgrpId"),
    (0, "STN-ATM-MIB", "stnAtmTholdRegionId"),
)
if mibBuilder.loadTexts:
    stnAtmThresholdEntry.setStatus("current")


class _StnAtmTholdTgrpId_Type(Integer32):
    """Custom type stnAtmTholdTgrpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_StnAtmTholdTgrpId_Type.__name__ = "Integer32"
_StnAtmTholdTgrpId_Object = MibTableColumn
stnAtmTholdTgrpId = _StnAtmTholdTgrpId_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 8, 1, 1, 1),
    _StnAtmTholdTgrpId_Type()
)
stnAtmTholdTgrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmTholdTgrpId.setStatus("current")


class _StnAtmTholdRegionId_Type(Integer32):
    """Custom type stnAtmTholdRegionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_StnAtmTholdRegionId_Type.__name__ = "Integer32"
_StnAtmTholdRegionId_Object = MibTableColumn
stnAtmTholdRegionId = _StnAtmTholdRegionId_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 8, 1, 1, 2),
    _StnAtmTholdRegionId_Type()
)
stnAtmTholdRegionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmTholdRegionId.setStatus("current")


class _StnAtmTholdCellLowerLimit_Type(Integer32):
    """Custom type stnAtmTholdCellLowerLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StnAtmTholdCellLowerLimit_Type.__name__ = "Integer32"
_StnAtmTholdCellLowerLimit_Object = MibTableColumn
stnAtmTholdCellLowerLimit = _StnAtmTholdCellLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 8, 1, 1, 3),
    _StnAtmTholdCellLowerLimit_Type()
)
stnAtmTholdCellLowerLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmTholdCellLowerLimit.setStatus("current")


class _StnAtmTholdCellUpperLimit_Type(Integer32):
    """Custom type stnAtmTholdCellUpperLimit based on Integer32"""
    defaultValue = 1023

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StnAtmTholdCellUpperLimit_Type.__name__ = "Integer32"
_StnAtmTholdCellUpperLimit_Object = MibTableColumn
stnAtmTholdCellUpperLimit = _StnAtmTholdCellUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 8, 1, 1, 4),
    _StnAtmTholdCellUpperLimit_Type()
)
stnAtmTholdCellUpperLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmTholdCellUpperLimit.setStatus("current")


class _StnAtmTholdCellQLimitMarking_Type(Integer32):
    """Custom type stnAtmTholdCellQLimitMarking based on Integer32"""
    defaultValue = 1023

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StnAtmTholdCellQLimitMarking_Type.__name__ = "Integer32"
_StnAtmTholdCellQLimitMarking_Object = MibTableColumn
stnAtmTholdCellQLimitMarking = _StnAtmTholdCellQLimitMarking_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 8, 1, 1, 5),
    _StnAtmTholdCellQLimitMarking_Type()
)
stnAtmTholdCellQLimitMarking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmTholdCellQLimitMarking.setStatus("current")


class _StnAtmTholdQLimitDiscard_Type(Integer32):
    """Custom type stnAtmTholdQLimitDiscard based on Integer32"""
    defaultValue = 1023

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StnAtmTholdQLimitDiscard_Type.__name__ = "Integer32"
_StnAtmTholdQLimitDiscard_Object = MibTableColumn
stnAtmTholdQLimitDiscard = _StnAtmTholdQLimitDiscard_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 8, 1, 1, 6),
    _StnAtmTholdQLimitDiscard_Type()
)
stnAtmTholdQLimitDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmTholdQLimitDiscard.setStatus("current")


class _StnAtmTholdQueueLimit_Type(Integer32):
    """Custom type stnAtmTholdQueueLimit based on Integer32"""
    defaultValue = 1023

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StnAtmTholdQueueLimit_Type.__name__ = "Integer32"
_StnAtmTholdQueueLimit_Object = MibTableColumn
stnAtmTholdQueueLimit = _StnAtmTholdQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 8, 1, 1, 7),
    _StnAtmTholdQueueLimit_Type()
)
stnAtmTholdQueueLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmTholdQueueLimit.setStatus("current")
_StnAtmAcct_ObjectIdentity = ObjectIdentity
stnAtmAcct = _StnAtmAcct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 9)
)


class _StnAtmAcctEnabled_Type(TruthValue):
    """Custom type stnAtmAcctEnabled based on TruthValue"""


_StnAtmAcctEnabled_Object = MibScalar
stnAtmAcctEnabled = _StnAtmAcctEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 9, 1),
    _StnAtmAcctEnabled_Type()
)
stnAtmAcctEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmAcctEnabled.setStatus("current")


class _StnAtmAcctMaxSize_Type(Integer32):
    """Custom type stnAtmAcctMaxSize based on Integer32"""
    defaultValue = 1024


_StnAtmAcctMaxSize_Object = MibScalar
stnAtmAcctMaxSize = _StnAtmAcctMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 9, 2),
    _StnAtmAcctMaxSize_Type()
)
stnAtmAcctMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmAcctMaxSize.setStatus("current")


class _StnAtmAcctMaxFiles_Type(Integer32):
    """Custom type stnAtmAcctMaxFiles based on Integer32"""
    defaultValue = 10


_StnAtmAcctMaxFiles_Object = MibScalar
stnAtmAcctMaxFiles = _StnAtmAcctMaxFiles_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 9, 3),
    _StnAtmAcctMaxFiles_Type()
)
stnAtmAcctMaxFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmAcctMaxFiles.setStatus("current")


class _StnAtmAcctFilePath_Type(OctetString):
    """Custom type stnAtmAcctFilePath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StnAtmAcctFilePath_Type.__name__ = "OctetString"
_StnAtmAcctFilePath_Object = MibScalar
stnAtmAcctFilePath = _StnAtmAcctFilePath_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 9, 4),
    _StnAtmAcctFilePath_Type()
)
stnAtmAcctFilePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmAcctFilePath.setStatus("current")
_StnAtmAcctFtpServer1_Type = IpAddress
_StnAtmAcctFtpServer1_Object = MibScalar
stnAtmAcctFtpServer1 = _StnAtmAcctFtpServer1_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 9, 5),
    _StnAtmAcctFtpServer1_Type()
)
stnAtmAcctFtpServer1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmAcctFtpServer1.setStatus("current")


class _StnAtmAcctFtpUserName1_Type(DisplayString):
    """Custom type stnAtmAcctFtpUserName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_StnAtmAcctFtpUserName1_Type.__name__ = "DisplayString"
_StnAtmAcctFtpUserName1_Object = MibScalar
stnAtmAcctFtpUserName1 = _StnAtmAcctFtpUserName1_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 9, 6),
    _StnAtmAcctFtpUserName1_Type()
)
stnAtmAcctFtpUserName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmAcctFtpUserName1.setStatus("current")


class _StnAtmAcctFtpPassword1_Type(OctetString):
    """Custom type stnAtmAcctFtpPassword1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StnAtmAcctFtpPassword1_Type.__name__ = "OctetString"
_StnAtmAcctFtpPassword1_Object = MibScalar
stnAtmAcctFtpPassword1 = _StnAtmAcctFtpPassword1_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 9, 7),
    _StnAtmAcctFtpPassword1_Type()
)
stnAtmAcctFtpPassword1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stnAtmAcctFtpPassword1.setStatus("current")
_StnAtmAcctFtpServer2_Type = IpAddress
_StnAtmAcctFtpServer2_Object = MibScalar
stnAtmAcctFtpServer2 = _StnAtmAcctFtpServer2_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 9, 8),
    _StnAtmAcctFtpServer2_Type()
)
stnAtmAcctFtpServer2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmAcctFtpServer2.setStatus("current")


class _StnAtmAcctFtpUserName2_Type(DisplayString):
    """Custom type stnAtmAcctFtpUserName2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_StnAtmAcctFtpUserName2_Type.__name__ = "DisplayString"
_StnAtmAcctFtpUserName2_Object = MibScalar
stnAtmAcctFtpUserName2 = _StnAtmAcctFtpUserName2_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 9, 9),
    _StnAtmAcctFtpUserName2_Type()
)
stnAtmAcctFtpUserName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmAcctFtpUserName2.setStatus("current")


class _StnAtmAcctFtpPassword2_Type(OctetString):
    """Custom type stnAtmAcctFtpPassword2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StnAtmAcctFtpPassword2_Type.__name__ = "OctetString"
_StnAtmAcctFtpPassword2_Object = MibScalar
stnAtmAcctFtpPassword2 = _StnAtmAcctFtpPassword2_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 9, 10),
    _StnAtmAcctFtpPassword2_Type()
)
stnAtmAcctFtpPassword2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stnAtmAcctFtpPassword2.setStatus("current")
_StnAtmAcctFtpServer3_Type = IpAddress
_StnAtmAcctFtpServer3_Object = MibScalar
stnAtmAcctFtpServer3 = _StnAtmAcctFtpServer3_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 9, 11),
    _StnAtmAcctFtpServer3_Type()
)
stnAtmAcctFtpServer3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmAcctFtpServer3.setStatus("current")


class _StnAtmAcctFtpUserName3_Type(DisplayString):
    """Custom type stnAtmAcctFtpUserName3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_StnAtmAcctFtpUserName3_Type.__name__ = "DisplayString"
_StnAtmAcctFtpUserName3_Object = MibScalar
stnAtmAcctFtpUserName3 = _StnAtmAcctFtpUserName3_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 9, 12),
    _StnAtmAcctFtpUserName3_Type()
)
stnAtmAcctFtpUserName3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmAcctFtpUserName3.setStatus("current")


class _StnAtmAcctFtpPassword3_Type(OctetString):
    """Custom type stnAtmAcctFtpPassword3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StnAtmAcctFtpPassword3_Type.__name__ = "OctetString"
_StnAtmAcctFtpPassword3_Object = MibScalar
stnAtmAcctFtpPassword3 = _StnAtmAcctFtpPassword3_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 9, 13),
    _StnAtmAcctFtpPassword3_Type()
)
stnAtmAcctFtpPassword3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stnAtmAcctFtpPassword3.setStatus("current")
_StnAtmAcctCurrentFtpServer_Type = IpAddress
_StnAtmAcctCurrentFtpServer_Object = MibScalar
stnAtmAcctCurrentFtpServer = _StnAtmAcctCurrentFtpServer_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 9, 14),
    _StnAtmAcctCurrentFtpServer_Type()
)
stnAtmAcctCurrentFtpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmAcctCurrentFtpServer.setStatus("current")
_StnAtmAcctPreviousFtpServer_Type = IpAddress
_StnAtmAcctPreviousFtpServer_Object = MibScalar
stnAtmAcctPreviousFtpServer = _StnAtmAcctPreviousFtpServer_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 1, 9, 15),
    _StnAtmAcctPreviousFtpServer_Type()
)
stnAtmAcctPreviousFtpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmAcctPreviousFtpServer.setStatus("current")
_StnAtmMibConformance_ObjectIdentity = ObjectIdentity
stnAtmMibConformance = _StnAtmMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 6, 2)
)

# Managed Objects groups


# Notification objects

stnCdrServerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 15)
)
stnCdrServerFailure.setObjects(
      *(("STN-ATM-MIB", "stnAtmAcctCurrentFtpServer"),
        ("STN-ATM-MIB", "stnAtmAcctPreviousFtpServer"))
)
if mibBuilder.loadTexts:
    stnCdrServerFailure.setStatus(
        "current"
    )

stnCdrLogFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 16)
)
stnCdrLogFailure.setObjects(
      *(("STN-ATM-MIB", "stnAtmAcctFtpServer1"),
        ("STN-ATM-MIB", "stnAtmAcctFtpServer2"),
        ("STN-ATM-MIB", "stnAtmAcctFtpServer3"))
)
if mibBuilder.loadTexts:
    stnCdrLogFailure.setStatus(
        "current"
    )

stnConfigAuditPvcFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 31)
)
stnConfigAuditPvcFailure.setObjects(
      *(("STN-ATM-MIB", "stnVcLinkIfIndex"),
        ("STN-ATM-MIB", "stnVcLinkVpi"),
        ("STN-ATM-MIB", "stnVcLinkVci"),
        ("STN-ROUTER-MIB", "stnRouterIndex"))
)
if mibBuilder.loadTexts:
    stnConfigAuditPvcFailure.setStatus(
        "current"
    )

stnConfigAuditSpvcFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 32)
)
stnConfigAuditSpvcFailure.setObjects(
      *(("STN-ATM-MIB", "stnVcLinkIfIndex"),
        ("STN-ATM-MIB", "stnVcLinkVpi"),
        ("STN-ATM-MIB", "stnVcLinkVci"),
        ("STN-ROUTER-MIB", "stnRouterIndex"))
)
if mibBuilder.loadTexts:
    stnConfigAuditSpvcFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STN-ATM-MIB",
    **{"VcLinkOperStatus": VcLinkOperStatus,
       "VcCrossConnOperStatus": VcCrossConnOperStatus,
       "TrafficDescrOperStatus": TrafficDescrOperStatus,
       "AtmPortOperStatus": AtmPortOperStatus,
       "stnAtm": stnAtm,
       "stnAtmObjects": stnAtmObjects,
       "stnAtmLinks": stnAtmLinks,
       "stnVcLinks": stnVcLinks,
       "stnVcLinkTable": stnVcLinkTable,
       "stnVcLinkEntry": stnVcLinkEntry,
       "stnVcLinkIfIndex": stnVcLinkIfIndex,
       "stnVcLinkVpi": stnVcLinkVpi,
       "stnVcLinkVci": stnVcLinkVci,
       "stnVcLinkRcvTrafDescr": stnVcLinkRcvTrafDescr,
       "stnVcLinkXmtTrafDescr": stnVcLinkXmtTrafDescr,
       "stnVcLinkAalObjectsValid": stnVcLinkAalObjectsValid,
       "stnVcLinkAalType": stnVcLinkAalType,
       "stnVcLinkAal5XmtSDUSize": stnVcLinkAal5XmtSDUSize,
       "stnVcLinkAal5RcvSDUSize": stnVcLinkAal5RcvSDUSize,
       "stnVcLinkAal5EncapsType": stnVcLinkAal5EncapsType,
       "stnVcLinkCastType": stnVcLinkCastType,
       "stnVcLinkConnKind": stnVcLinkConnKind,
       "stnVcLinkAccEnabled": stnVcLinkAccEnabled,
       "stnVcLinkOAMMgmtEnabled": stnVcLinkOAMMgmtEnabled,
       "stnVcLinkOAMXmtFrequency": stnVcLinkOAMXmtFrequency,
       "stnVcLinkOAMRetryUpCount": stnVcLinkOAMRetryUpCount,
       "stnVcLinkOAMRetryDownCount": stnVcLinkOAMRetryDownCount,
       "stnVcLinkOAMRetryFrequency": stnVcLinkOAMRetryFrequency,
       "stnVcLinkPppId": stnVcLinkPppId,
       "stnVcLinkOperStatus": stnVcLinkOperStatus,
       "stnAtmCrossConns": stnAtmCrossConns,
       "stnVcCrossConns": stnVcCrossConns,
       "stnVcCrossConnTable": stnVcCrossConnTable,
       "stnVcCrossConnEntry": stnVcCrossConnEntry,
       "stnVcCrossConnLowIfIndex": stnVcCrossConnLowIfIndex,
       "stnVcCrossConnLowVpi": stnVcCrossConnLowVpi,
       "stnVcCrossConnLowVci": stnVcCrossConnLowVci,
       "stnVcCrossConnHighIfIndex": stnVcCrossConnHighIfIndex,
       "stnVcCrossConnHighVpi": stnVcCrossConnHighVpi,
       "stnVcCrossConnHighVci": stnVcCrossConnHighVci,
       "stnVcCrossConnLowAutoAssign": stnVcCrossConnLowAutoAssign,
       "stnVcCrossConnHighAutoAssign": stnVcCrossConnHighAutoAssign,
       "stnVcCrossConnOperStatus": stnVcCrossConnOperStatus,
       "stnVpCrossConns": stnVpCrossConns,
       "stnAtmTrafficDescrs": stnAtmTrafficDescrs,
       "stnTrafficDescrTable": stnTrafficDescrTable,
       "stnTrafficDescrEntry": stnTrafficDescrEntry,
       "stnTrafDescrIndex": stnTrafDescrIndex,
       "stnTrafDescrName": stnTrafDescrName,
       "stnTrafDescrType": stnTrafDescrType,
       "stnTrafDescrParam1": stnTrafDescrParam1,
       "stnTrafDescrParam2": stnTrafDescrParam2,
       "stnTrafDescrParam3": stnTrafDescrParam3,
       "stnTrafDescrParam4": stnTrafDescrParam4,
       "stnTrafDescrParam5": stnTrafDescrParam5,
       "stnTrafDescrQosClass": stnTrafDescrQosClass,
       "stnTrafDescrServiceCategory": stnTrafDescrServiceCategory,
       "stnTrafDescrFrameDiscard": stnTrafDescrFrameDiscard,
       "stnTrafDescrOperStatus": stnTrafDescrOperStatus,
       "stnTrafDescrCommittedRate": stnTrafDescrCommittedRate,
       "stnTrafDescrMaximumRate": stnTrafDescrMaximumRate,
       "stnAtmPorts": stnAtmPorts,
       "stnAtmPortAttrs": stnAtmPortAttrs,
       "stnAtmPortAttrTable": stnAtmPortAttrTable,
       "stnAtmPortAttrEntry": stnAtmPortAttrEntry,
       "stnAtmPortIfIndex": stnAtmPortIfIndex,
       "stnAtmPortIfType": stnAtmPortIfType,
       "stnAtmPortIfState": stnAtmPortIfState,
       "stnAtmPortEnabled": stnAtmPortEnabled,
       "stnAtmPortMinVccVpi": stnAtmPortMinVccVpi,
       "stnAtmPortMaxVccVpi": stnAtmPortMaxVccVpi,
       "stnAtmPortMinVccVci": stnAtmPortMinVccVci,
       "stnAtmPortMaxVccVci": stnAtmPortMaxVccVci,
       "stnAtmPortMinVpcVpi": stnAtmPortMinVpcVpi,
       "stnAtmPortMaxVpcVpi": stnAtmPortMaxVpcVpi,
       "stnAtmPortMaxActivePaths": stnAtmPortMaxActivePaths,
       "stnAtmPortMaxActiveChannels": stnAtmPortMaxActiveChannels,
       "stnAtmPortPVCAddress": stnAtmPortPVCAddress,
       "stnAtmPortSVCAddress": stnAtmPortSVCAddress,
       "stnAtmPortSigVpi": stnAtmPortSigVpi,
       "stnAtmPortSigVci": stnAtmPortSigVci,
       "stnAtmPortSigEnabled": stnAtmPortSigEnabled,
       "stnAtmPortIlmiVpi": stnAtmPortIlmiVpi,
       "stnAtmPortIlmiVci": stnAtmPortIlmiVci,
       "stnAtmPortIlmiEnabled": stnAtmPortIlmiEnabled,
       "stnAtmPortOamManagementEnabled": stnAtmPortOamManagementEnabled,
       "stnAtmPortOamXmtFrequency": stnAtmPortOamXmtFrequency,
       "stnAtmPortOamRetryUpCount": stnAtmPortOamRetryUpCount,
       "stnAtmPortOamRetryDownCount": stnAtmPortOamRetryDownCount,
       "stnAtmPortOamRetryFrequency": stnAtmPortOamRetryFrequency,
       "stnAtmPortOperStatus": stnAtmPortOperStatus,
       "stnAtmPortIlmi": stnAtmPortIlmi,
       "stnAtmPortIlmiTable": stnAtmPortIlmiTable,
       "stnAtmPortIlmiEntry": stnAtmPortIlmiEntry,
       "stnAtmPortIlmiIfIndex": stnAtmPortIlmiIfIndex,
       "stnAtmPortIlmiVersion": stnAtmPortIlmiVersion,
       "stnAtmPortIlmiNetworkOrientation": stnAtmPortIlmiNetworkOrientation,
       "stnAtmPortIlmiAutoNegotiate": stnAtmPortIlmiAutoNegotiate,
       "stnAtmPortIlmiPollInterval": stnAtmPortIlmiPollInterval,
       "stnAtmPortIlmiCheckConnectionInt": stnAtmPortIlmiCheckConnectionInt,
       "stnAtmPortIlmiInactivityFactor": stnAtmPortIlmiInactivityFactor,
       "stnAtmPortIlmiLocalConn": stnAtmPortIlmiLocalConn,
       "stnAtmPortIlmiAdminStatus": stnAtmPortIlmiAdminStatus,
       "stnAtmPortIlmiEnterprise": stnAtmPortIlmiEnterprise,
       "stnAtmPortIlmiLocalOid": stnAtmPortIlmiLocalOid,
       "stnAtmPortIlmiNetPrefix": stnAtmPortIlmiNetPrefix,
       "stnAtmPortIlmiPrefixLen": stnAtmPortIlmiPrefixLen,
       "stnAtmPortSignaling": stnAtmPortSignaling,
       "stnAtmPortSigs": stnAtmPortSigs,
       "stnAtmPortSigTable": stnAtmPortSigTable,
       "stnAtmPortSigEntry": stnAtmPortSigEntry,
       "stnAtmPortSigIfIndex": stnAtmPortSigIfIndex,
       "stnAtmPortSigVersion": stnAtmPortSigVersion,
       "stnAtmPortSigNetworkOrientation": stnAtmPortSigNetworkOrientation,
       "stnAtmPortSigAssignVpiVci": stnAtmPortSigAssignVpiVci,
       "stnAtmPortSigVpSigType": stnAtmPortSigVpSigType,
       "stnAtmPortSigParseMode": stnAtmPortSigParseMode,
       "stnAtmPortSigPrefCarrierPresent": stnAtmPortSigPrefCarrierPresent,
       "stnAtmPortSigPrefCarrier": stnAtmPortSigPrefCarrier,
       "stnAtmPortSigDurations": stnAtmPortSigDurations,
       "stnAtmPortSigDurationTable": stnAtmPortSigDurationTable,
       "stnAtmPortSigDurationEntry": stnAtmPortSigDurationEntry,
       "stnAtmPortSigDurIfIndex": stnAtmPortSigDurIfIndex,
       "stnAtmPortSigT301Duration": stnAtmPortSigT301Duration,
       "stnAtmPortSigT303Duration": stnAtmPortSigT303Duration,
       "stnAtmPortSigT306Duration": stnAtmPortSigT306Duration,
       "stnAtmPortSigT308Duration": stnAtmPortSigT308Duration,
       "stnAtmPortSigT309Duration": stnAtmPortSigT309Duration,
       "stnAtmPortSigT310Duration": stnAtmPortSigT310Duration,
       "stnAtmPortSigT313Duration": stnAtmPortSigT313Duration,
       "stnAtmPortSigT316Duration": stnAtmPortSigT316Duration,
       "stnAtmPortSigT317Duration": stnAtmPortSigT317Duration,
       "stnAtmPortSigT322Duration": stnAtmPortSigT322Duration,
       "stnAtmPortSigT331Duration": stnAtmPortSigT331Duration,
       "stnAtmPortSigT333Duration": stnAtmPortSigT333Duration,
       "stnAtmPortSigT397Duration": stnAtmPortSigT397Duration,
       "stnAtmPortSigT398Duration": stnAtmPortSigT398Duration,
       "stnAtmPortSigT399Duration": stnAtmPortSigT399Duration,
       "stnAtmPortSigSaalRetryDuration": stnAtmPortSigSaalRetryDuration,
       "stnAtmPortSigRetries": stnAtmPortSigRetries,
       "stnAtmPortSigRetryTable": stnAtmPortSigRetryTable,
       "stnAtmPortSigRetryEntry": stnAtmPortSigRetryEntry,
       "stnAtmPortSigRetryIfIndex": stnAtmPortSigRetryIfIndex,
       "stnAtmPortSigT303Retries": stnAtmPortSigT303Retries,
       "stnAtmPortSigT308Retries": stnAtmPortSigT308Retries,
       "stnAtmPortSigT316Retries": stnAtmPortSigT316Retries,
       "stnAtmPortSigT322Retries": stnAtmPortSigT322Retries,
       "stnAtmPortSigT331Retries": stnAtmPortSigT331Retries,
       "stnAtmPortSigSSCSTable": stnAtmPortSigSSCSTable,
       "stnAtmPortSigSSCSEntry": stnAtmPortSigSSCSEntry,
       "stnAtmPortSigSSCSIfIndex": stnAtmPortSigSSCSIfIndex,
       "stnAtmPortSigSSCSPollDuration": stnAtmPortSigSSCSPollDuration,
       "stnAtmPortSigSSCSKeepAliveDuration": stnAtmPortSigSSCSKeepAliveDuration,
       "stnAtmPortSigSSCSIdleDuration": stnAtmPortSigSSCSIdleDuration,
       "stnAtmPortSigSSCSNoRspDuration": stnAtmPortSigSSCSNoRspDuration,
       "stnAtmPortSigSSCSCcDuration": stnAtmPortSigSSCSCcDuration,
       "stnAtmPortSigSSCSMaxRcvWindowSize": stnAtmPortSigSSCSMaxRcvWindowSize,
       "stnAtmPortSigSSCSMaxCcRetries": stnAtmPortSigSSCSMaxCcRetries,
       "stnAtmPortSigSSCSMaxSdBetwPolls": stnAtmPortSigSSCSMaxSdBetwPolls,
       "stnAtmPortSigSSCSMaxStatListElms": stnAtmPortSigSSCSMaxStatListElms,
       "stnAtmPortSigSSCSPollAfterRetrans": stnAtmPortSigSSCSPollAfterRetrans,
       "stnAtmPortSigSSCSRepeatUstat": stnAtmPortSigSSCSRepeatUstat,
       "stnAtmPortSigSSCSUstatRspToPoll": stnAtmPortSigSSCSUstatRspToPoll,
       "stnAtmPortTraffic": stnAtmPortTraffic,
       "stnAtmPortTrafficTable": stnAtmPortTrafficTable,
       "stnAtmPortTrafficEntry": stnAtmPortTrafficEntry,
       "stnAtmPortTrafIndex": stnAtmPortTrafIndex,
       "stnAtmPortTrafTxCells": stnAtmPortTrafTxCells,
       "stnAtmPortTrafRxCells": stnAtmPortTrafRxCells,
       "stnAtmPortTrafTxParityErrors": stnAtmPortTrafTxParityErrors,
       "stnAtmPortTrafRxHdrChkSumErrors": stnAtmPortTrafRxHdrChkSumErrors,
       "stnAtmPortTrafPhyParityErrors": stnAtmPortTrafPhyParityErrors,
       "stnAtmPortTrafCrc10Errors": stnAtmPortTrafCrc10Errors,
       "stnAtmTraces": stnAtmTraces,
       "stnTraceIps": stnTraceIps,
       "stnTraceIpsEnabled": stnTraceIpsEnabled,
       "stnTraceIpsSize": stnTraceIpsSize,
       "stnTraceIpsFile": stnTraceIpsFile,
       "stnTracePd": stnTracePd,
       "stnTracePdProblemEnabled": stnTracePdProblemEnabled,
       "stnTracePdExceptionEnabled": stnTracePdExceptionEnabled,
       "stnTracePdAuditEnabled": stnTracePdAuditEnabled,
       "stnTracePdDeveloperEnabled": stnTracePdDeveloperEnabled,
       "stnTracePdSize": stnTracePdSize,
       "stnTracePdFile": stnTracePdFile,
       "stnAtmQos": stnAtmQos,
       "stnQosCLR": stnQosCLR,
       "stnQosClass1CLR": stnQosClass1CLR,
       "stnQosClass2CLR": stnQosClass2CLR,
       "stnQosClass3CLR": stnQosClass3CLR,
       "stnQosClass4CLR": stnQosClass4CLR,
       "stnQosCDV": stnQosCDV,
       "stnQosClass1CDV": stnQosClass1CDV,
       "stnQosClass2CDV": stnQosClass2CDV,
       "stnQosClass3CDV": stnQosClass3CDV,
       "stnQosClass4CDV": stnQosClass4CDV,
       "stnQosCTD": stnQosCTD,
       "stnQosClass1MaxCTD": stnQosClass1MaxCTD,
       "stnQosClass2MaxCTD": stnQosClass2MaxCTD,
       "stnQosClass3MaxCTD": stnQosClass3MaxCTD,
       "stnQosClass4MaxCTD": stnQosClass4MaxCTD,
       "stnAtmAddresses": stnAtmAddresses,
       "stnAtmAddressTable": stnAtmAddressTable,
       "stnAtmAddressEntry": stnAtmAddressEntry,
       "stnAtmAddrIfIndex": stnAtmAddrIfIndex,
       "stnAtmAddrAddress": stnAtmAddrAddress,
       "stnAtmAddrAddressLen": stnAtmAddrAddressLen,
       "stnAtmThresholds": stnAtmThresholds,
       "stnAtmThresholdTable": stnAtmThresholdTable,
       "stnAtmThresholdEntry": stnAtmThresholdEntry,
       "stnAtmTholdTgrpId": stnAtmTholdTgrpId,
       "stnAtmTholdRegionId": stnAtmTholdRegionId,
       "stnAtmTholdCellLowerLimit": stnAtmTholdCellLowerLimit,
       "stnAtmTholdCellUpperLimit": stnAtmTholdCellUpperLimit,
       "stnAtmTholdCellQLimitMarking": stnAtmTholdCellQLimitMarking,
       "stnAtmTholdQLimitDiscard": stnAtmTholdQLimitDiscard,
       "stnAtmTholdQueueLimit": stnAtmTholdQueueLimit,
       "stnAtmAcct": stnAtmAcct,
       "stnAtmAcctEnabled": stnAtmAcctEnabled,
       "stnAtmAcctMaxSize": stnAtmAcctMaxSize,
       "stnAtmAcctMaxFiles": stnAtmAcctMaxFiles,
       "stnAtmAcctFilePath": stnAtmAcctFilePath,
       "stnAtmAcctFtpServer1": stnAtmAcctFtpServer1,
       "stnAtmAcctFtpUserName1": stnAtmAcctFtpUserName1,
       "stnAtmAcctFtpPassword1": stnAtmAcctFtpPassword1,
       "stnAtmAcctFtpServer2": stnAtmAcctFtpServer2,
       "stnAtmAcctFtpUserName2": stnAtmAcctFtpUserName2,
       "stnAtmAcctFtpPassword2": stnAtmAcctFtpPassword2,
       "stnAtmAcctFtpServer3": stnAtmAcctFtpServer3,
       "stnAtmAcctFtpUserName3": stnAtmAcctFtpUserName3,
       "stnAtmAcctFtpPassword3": stnAtmAcctFtpPassword3,
       "stnAtmAcctCurrentFtpServer": stnAtmAcctCurrentFtpServer,
       "stnAtmAcctPreviousFtpServer": stnAtmAcctPreviousFtpServer,
       "stnAtmMibConformance": stnAtmMibConformance,
       "stnCdrServerFailure": stnCdrServerFailure,
       "stnCdrLogFailure": stnCdrLogFailure,
       "stnConfigAuditPvcFailure": stnConfigAuditPvcFailure,
       "stnConfigAuditSpvcFailure": stnConfigAuditSpvcFailure}
)
