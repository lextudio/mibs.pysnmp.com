# SNMP MIB module (WWP-LEOS-RSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-RSTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:07 2024
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

(dot1dStpPort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dStpPort")

(dot1dStpPortOperEdgePort,) = mibBuilder.importSymbols(
    "RSTP-MIB",
    "dot1dStpPortOperEdgePort")

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

(wwpModules,
 wwpModulesLeos) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosRstpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13)
)
wwpLeosRstpMIB.setRevisions(
        ("2011-08-02 00:00",
         "2001-04-03 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpLeosRstpMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosRstpMIBObjects = _WwpLeosRstpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1)
)
_WwpLeosRstpDomain_ObjectIdentity = ObjectIdentity
wwpLeosRstpDomain = _WwpLeosRstpDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1)
)


class _WwpLeosRstpMode_Type(Integer32):
    """Custom type wwpLeosRstpMode based on Integer32"""
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
        *(("domain", 3),
          ("mstp", 4),
          ("rstp", 2),
          ("unknown", 1))
    )


_WwpLeosRstpMode_Type.__name__ = "Integer32"
_WwpLeosRstpMode_Object = MibScalar
wwpLeosRstpMode = _WwpLeosRstpMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 1),
    _WwpLeosRstpMode_Type()
)
wwpLeosRstpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRstpMode.setStatus("current")
_WwpLeosRstpDomainTable_Object = MibTable
wwpLeosRstpDomainTable = _WwpLeosRstpDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wwpLeosRstpDomainTable.setStatus("current")
_WwpLeosRstpDomainEntry_Object = MibTableRow
wwpLeosRstpDomainEntry = _WwpLeosRstpDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 2, 1)
)
wwpLeosRstpDomainEntry.setIndexNames(
    (0, "WWP-LEOS-RSTP-MIB", "wwpLeosRstpDomainId"),
)
if mibBuilder.loadTexts:
    wwpLeosRstpDomainEntry.setStatus("current")


class _WwpLeosRstpDomainId_Type(Integer32):
    """Custom type wwpLeosRstpDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosRstpDomainId_Type.__name__ = "Integer32"
_WwpLeosRstpDomainId_Object = MibTableColumn
wwpLeosRstpDomainId = _WwpLeosRstpDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 2, 1, 1),
    _WwpLeosRstpDomainId_Type()
)
wwpLeosRstpDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRstpDomainId.setStatus("current")
_WwpLeosRstpDomainName_Type = DisplayString
_WwpLeosRstpDomainName_Object = MibTableColumn
wwpLeosRstpDomainName = _WwpLeosRstpDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 2, 1, 2),
    _WwpLeosRstpDomainName_Type()
)
wwpLeosRstpDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosRstpDomainName.setStatus("current")
_WwpLeosRstpDomainStatus_Type = RowStatus
_WwpLeosRstpDomainStatus_Object = MibTableColumn
wwpLeosRstpDomainStatus = _WwpLeosRstpDomainStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 2, 1, 3),
    _WwpLeosRstpDomainStatus_Type()
)
wwpLeosRstpDomainStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosRstpDomainStatus.setStatus("current")
_WwpLeosRstpDomainMemTable_Object = MibTable
wwpLeosRstpDomainMemTable = _WwpLeosRstpDomainMemTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wwpLeosRstpDomainMemTable.setStatus("current")
_WwpLeosRstpDomainMemEntry_Object = MibTableRow
wwpLeosRstpDomainMemEntry = _WwpLeosRstpDomainMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 3, 1)
)
wwpLeosRstpDomainMemEntry.setIndexNames(
    (0, "WWP-LEOS-RSTP-MIB", "wwpLeosRstpDomainId"),
    (0, "WWP-LEOS-RSTP-MIB", "wwpLeosRstpDomainPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosRstpDomainMemEntry.setStatus("current")


class _WwpLeosRstpDomainPortId_Type(Integer32):
    """Custom type wwpLeosRstpDomainPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosRstpDomainPortId_Type.__name__ = "Integer32"
_WwpLeosRstpDomainPortId_Object = MibTableColumn
wwpLeosRstpDomainPortId = _WwpLeosRstpDomainPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 3, 1, 1),
    _WwpLeosRstpDomainPortId_Type()
)
wwpLeosRstpDomainPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRstpDomainPortId.setStatus("current")
_WwpLeosRstpDomainMemStatus_Type = RowStatus
_WwpLeosRstpDomainMemStatus_Object = MibTableColumn
wwpLeosRstpDomainMemStatus = _WwpLeosRstpDomainMemStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 3, 1, 2),
    _WwpLeosRstpDomainMemStatus_Type()
)
wwpLeosRstpDomainMemStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosRstpDomainMemStatus.setStatus("current")
_WwpLeosRstpBridgeDomainAttrs_ObjectIdentity = ObjectIdentity
wwpLeosRstpBridgeDomainAttrs = _WwpLeosRstpBridgeDomainAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 4)
)


class _WwpLeosRstpDomainAttrsForceVer_Type(Integer32):
    """Custom type wwpLeosRstpDomainAttrsForceVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notDefined", 1),
          ("rstp", 2),
          ("stp", 0))
    )


_WwpLeosRstpDomainAttrsForceVer_Type.__name__ = "Integer32"
_WwpLeosRstpDomainAttrsForceVer_Object = MibScalar
wwpLeosRstpDomainAttrsForceVer = _WwpLeosRstpDomainAttrsForceVer_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 4, 1),
    _WwpLeosRstpDomainAttrsForceVer_Type()
)
wwpLeosRstpDomainAttrsForceVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRstpDomainAttrsForceVer.setStatus("current")


class _WwpLeosRstpDomainAttrsForwardDelay_Type(Integer32):
    """Custom type wwpLeosRstpDomainAttrsForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_WwpLeosRstpDomainAttrsForwardDelay_Type.__name__ = "Integer32"
_WwpLeosRstpDomainAttrsForwardDelay_Object = MibScalar
wwpLeosRstpDomainAttrsForwardDelay = _WwpLeosRstpDomainAttrsForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 4, 2),
    _WwpLeosRstpDomainAttrsForwardDelay_Type()
)
wwpLeosRstpDomainAttrsForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRstpDomainAttrsForwardDelay.setStatus("current")


class _WwpLeosRstpDomainAttrsHelloTime_Type(Integer32):
    """Custom type wwpLeosRstpDomainAttrsHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WwpLeosRstpDomainAttrsHelloTime_Type.__name__ = "Integer32"
_WwpLeosRstpDomainAttrsHelloTime_Object = MibScalar
wwpLeosRstpDomainAttrsHelloTime = _WwpLeosRstpDomainAttrsHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 4, 3),
    _WwpLeosRstpDomainAttrsHelloTime_Type()
)
wwpLeosRstpDomainAttrsHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRstpDomainAttrsHelloTime.setStatus("current")


class _WwpLeosRstpDomainAttrsLoopBackBlock_Type(Integer32):
    """Custom type wwpLeosRstpDomainAttrsLoopBackBlock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_WwpLeosRstpDomainAttrsLoopBackBlock_Type.__name__ = "Integer32"
_WwpLeosRstpDomainAttrsLoopBackBlock_Object = MibScalar
wwpLeosRstpDomainAttrsLoopBackBlock = _WwpLeosRstpDomainAttrsLoopBackBlock_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 4, 4),
    _WwpLeosRstpDomainAttrsLoopBackBlock_Type()
)
wwpLeosRstpDomainAttrsLoopBackBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRstpDomainAttrsLoopBackBlock.setStatus("current")


class _WwpLeosRstpDomainAttrsMaxAge_Type(Integer32):
    """Custom type wwpLeosRstpDomainAttrsMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_WwpLeosRstpDomainAttrsMaxAge_Type.__name__ = "Integer32"
_WwpLeosRstpDomainAttrsMaxAge_Object = MibScalar
wwpLeosRstpDomainAttrsMaxAge = _WwpLeosRstpDomainAttrsMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 4, 5),
    _WwpLeosRstpDomainAttrsMaxAge_Type()
)
wwpLeosRstpDomainAttrsMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRstpDomainAttrsMaxAge.setStatus("current")


class _WwpLeosRstpDomainAttrsPathCostDef_Type(Integer32):
    """Custom type wwpLeosRstpDomainAttrsPathCostDef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WwpLeosRstpDomainAttrsPathCostDef_Type.__name__ = "Integer32"
_WwpLeosRstpDomainAttrsPathCostDef_Object = MibScalar
wwpLeosRstpDomainAttrsPathCostDef = _WwpLeosRstpDomainAttrsPathCostDef_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 4, 6),
    _WwpLeosRstpDomainAttrsPathCostDef_Type()
)
wwpLeosRstpDomainAttrsPathCostDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRstpDomainAttrsPathCostDef.setStatus("current")


class _WwpLeosRstpDomainAttrsPriority_Type(Integer32):
    """Custom type wwpLeosRstpDomainAttrsPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WwpLeosRstpDomainAttrsPriority_Type.__name__ = "Integer32"
_WwpLeosRstpDomainAttrsPriority_Object = MibScalar
wwpLeosRstpDomainAttrsPriority = _WwpLeosRstpDomainAttrsPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 4, 7),
    _WwpLeosRstpDomainAttrsPriority_Type()
)
wwpLeosRstpDomainAttrsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRstpDomainAttrsPriority.setStatus("current")


class _WwpLeosRstpDomainAttrsTxHoldCount_Type(Integer32):
    """Custom type wwpLeosRstpDomainAttrsTxHoldCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WwpLeosRstpDomainAttrsTxHoldCount_Type.__name__ = "Integer32"
_WwpLeosRstpDomainAttrsTxHoldCount_Object = MibScalar
wwpLeosRstpDomainAttrsTxHoldCount = _WwpLeosRstpDomainAttrsTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 4, 8),
    _WwpLeosRstpDomainAttrsTxHoldCount_Type()
)
wwpLeosRstpDomainAttrsTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRstpDomainAttrsTxHoldCount.setStatus("current")
_WwpLeosRstpDomainAttrTable_Object = MibTable
wwpLeosRstpDomainAttrTable = _WwpLeosRstpDomainAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 5)
)
if mibBuilder.loadTexts:
    wwpLeosRstpDomainAttrTable.setStatus("current")
_WwpLeosRstpDomainAttrEntry_Object = MibTableRow
wwpLeosRstpDomainAttrEntry = _WwpLeosRstpDomainAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 5, 1)
)
wwpLeosRstpDomainAttrEntry.setIndexNames(
    (0, "WWP-LEOS-RSTP-MIB", "wwpLeosRstpDomainId"),
)
if mibBuilder.loadTexts:
    wwpLeosRstpDomainAttrEntry.setStatus("current")


class _WwpLeosRstpDomainAttrDesignatedBridgePri_Type(Integer32):
    """Custom type wwpLeosRstpDomainAttrDesignatedBridgePri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosRstpDomainAttrDesignatedBridgePri_Type.__name__ = "Integer32"
_WwpLeosRstpDomainAttrDesignatedBridgePri_Object = MibTableColumn
wwpLeosRstpDomainAttrDesignatedBridgePri = _WwpLeosRstpDomainAttrDesignatedBridgePri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 5, 1, 1),
    _WwpLeosRstpDomainAttrDesignatedBridgePri_Type()
)
wwpLeosRstpDomainAttrDesignatedBridgePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRstpDomainAttrDesignatedBridgePri.setStatus("current")
_WwpLeosRstpDomainAttrDesignatedBridgeMac_Type = MacAddress
_WwpLeosRstpDomainAttrDesignatedBridgeMac_Object = MibTableColumn
wwpLeosRstpDomainAttrDesignatedBridgeMac = _WwpLeosRstpDomainAttrDesignatedBridgeMac_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 5, 1, 2),
    _WwpLeosRstpDomainAttrDesignatedBridgeMac_Type()
)
wwpLeosRstpDomainAttrDesignatedBridgeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRstpDomainAttrDesignatedBridgeMac.setStatus("current")


class _WwpLeosRstpDomainAttrDesignatedRootPri_Type(Integer32):
    """Custom type wwpLeosRstpDomainAttrDesignatedRootPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosRstpDomainAttrDesignatedRootPri_Type.__name__ = "Integer32"
_WwpLeosRstpDomainAttrDesignatedRootPri_Object = MibTableColumn
wwpLeosRstpDomainAttrDesignatedRootPri = _WwpLeosRstpDomainAttrDesignatedRootPri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 5, 1, 3),
    _WwpLeosRstpDomainAttrDesignatedRootPri_Type()
)
wwpLeosRstpDomainAttrDesignatedRootPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRstpDomainAttrDesignatedRootPri.setStatus("current")
_WwpLeosRstpDomainAttrDesignatedRootMac_Type = MacAddress
_WwpLeosRstpDomainAttrDesignatedRootMac_Object = MibTableColumn
wwpLeosRstpDomainAttrDesignatedRootMac = _WwpLeosRstpDomainAttrDesignatedRootMac_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 5, 1, 4),
    _WwpLeosRstpDomainAttrDesignatedRootMac_Type()
)
wwpLeosRstpDomainAttrDesignatedRootMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRstpDomainAttrDesignatedRootMac.setStatus("current")


class _WwpLeosRstpDomainAttrRootCost_Type(Integer32):
    """Custom type wwpLeosRstpDomainAttrRootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosRstpDomainAttrRootCost_Type.__name__ = "Integer32"
_WwpLeosRstpDomainAttrRootCost_Object = MibTableColumn
wwpLeosRstpDomainAttrRootCost = _WwpLeosRstpDomainAttrRootCost_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 5, 1, 5),
    _WwpLeosRstpDomainAttrRootCost_Type()
)
wwpLeosRstpDomainAttrRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRstpDomainAttrRootCost.setStatus("current")


class _WwpLeosRstpDomainAttrRootPort_Type(Integer32):
    """Custom type wwpLeosRstpDomainAttrRootPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosRstpDomainAttrRootPort_Type.__name__ = "Integer32"
_WwpLeosRstpDomainAttrRootPort_Object = MibTableColumn
wwpLeosRstpDomainAttrRootPort = _WwpLeosRstpDomainAttrRootPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 5, 1, 6),
    _WwpLeosRstpDomainAttrRootPort_Type()
)
wwpLeosRstpDomainAttrRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRstpDomainAttrRootPort.setStatus("current")


class _WwpLeosRstpDomainAttrMaxAge_Type(Integer32):
    """Custom type wwpLeosRstpDomainAttrMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_WwpLeosRstpDomainAttrMaxAge_Type.__name__ = "Integer32"
_WwpLeosRstpDomainAttrMaxAge_Object = MibTableColumn
wwpLeosRstpDomainAttrMaxAge = _WwpLeosRstpDomainAttrMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 5, 1, 7),
    _WwpLeosRstpDomainAttrMaxAge_Type()
)
wwpLeosRstpDomainAttrMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRstpDomainAttrMaxAge.setStatus("current")


class _WwpLeosRstpDomainAttrHelloTime_Type(Integer32):
    """Custom type wwpLeosRstpDomainAttrHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WwpLeosRstpDomainAttrHelloTime_Type.__name__ = "Integer32"
_WwpLeosRstpDomainAttrHelloTime_Object = MibTableColumn
wwpLeosRstpDomainAttrHelloTime = _WwpLeosRstpDomainAttrHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 5, 1, 8),
    _WwpLeosRstpDomainAttrHelloTime_Type()
)
wwpLeosRstpDomainAttrHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRstpDomainAttrHelloTime.setStatus("current")


class _WwpLeosRstpDomainAttrHoldTime_Type(Integer32):
    """Custom type wwpLeosRstpDomainAttrHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosRstpDomainAttrHoldTime_Type.__name__ = "Integer32"
_WwpLeosRstpDomainAttrHoldTime_Object = MibTableColumn
wwpLeosRstpDomainAttrHoldTime = _WwpLeosRstpDomainAttrHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 5, 1, 9),
    _WwpLeosRstpDomainAttrHoldTime_Type()
)
wwpLeosRstpDomainAttrHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRstpDomainAttrHoldTime.setStatus("current")


class _WwpLeosRstpDomainAttrForwardDelay_Type(Integer32):
    """Custom type wwpLeosRstpDomainAttrForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_WwpLeosRstpDomainAttrForwardDelay_Type.__name__ = "Integer32"
_WwpLeosRstpDomainAttrForwardDelay_Object = MibTableColumn
wwpLeosRstpDomainAttrForwardDelay = _WwpLeosRstpDomainAttrForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 5, 1, 10),
    _WwpLeosRstpDomainAttrForwardDelay_Type()
)
wwpLeosRstpDomainAttrForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRstpDomainAttrForwardDelay.setStatus("current")


class _WwpLeosRstpDomainAttrPriority_Type(Integer32):
    """Custom type wwpLeosRstpDomainAttrPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WwpLeosRstpDomainAttrPriority_Type.__name__ = "Integer32"
_WwpLeosRstpDomainAttrPriority_Object = MibTableColumn
wwpLeosRstpDomainAttrPriority = _WwpLeosRstpDomainAttrPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 5, 1, 11),
    _WwpLeosRstpDomainAttrPriority_Type()
)
wwpLeosRstpDomainAttrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRstpDomainAttrPriority.setStatus("current")


class _WwpLeosRstpMaxAgeEventInterval_Type(Integer32):
    """Custom type wwpLeosRstpMaxAgeEventInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_WwpLeosRstpMaxAgeEventInterval_Type.__name__ = "Integer32"
_WwpLeosRstpMaxAgeEventInterval_Object = MibScalar
wwpLeosRstpMaxAgeEventInterval = _WwpLeosRstpMaxAgeEventInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 1, 6),
    _WwpLeosRstpMaxAgeEventInterval_Type()
)
wwpLeosRstpMaxAgeEventInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRstpMaxAgeEventInterval.setStatus("current")
_WwpLeosRstpPortExt_ObjectIdentity = ObjectIdentity
wwpLeosRstpPortExt = _WwpLeosRstpPortExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 2)
)
_WwpLeosRstpPortInfoTable_Object = MibTable
wwpLeosRstpPortInfoTable = _WwpLeosRstpPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wwpLeosRstpPortInfoTable.setStatus("current")
_WwpLeosRstpPortInfoEntry_Object = MibTableRow
wwpLeosRstpPortInfoEntry = _WwpLeosRstpPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 2, 1, 1)
)
wwpLeosRstpPortInfoEntry.setIndexNames(
    (0, "WWP-LEOS-RSTP-MIB", "wwpLeosRstpPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosRstpPortInfoEntry.setStatus("current")


class _WwpLeosRstpPortId_Type(Integer32):
    """Custom type wwpLeosRstpPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosRstpPortId_Type.__name__ = "Integer32"
_WwpLeosRstpPortId_Object = MibTableColumn
wwpLeosRstpPortId = _WwpLeosRstpPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 2, 1, 1, 1),
    _WwpLeosRstpPortId_Type()
)
wwpLeosRstpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRstpPortId.setStatus("current")
_WwpLeosRstpPortDesiginatedId_Type = MacAddress
_WwpLeosRstpPortDesiginatedId_Object = MibTableColumn
wwpLeosRstpPortDesiginatedId = _WwpLeosRstpPortDesiginatedId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 2, 1, 1, 2),
    _WwpLeosRstpPortDesiginatedId_Type()
)
wwpLeosRstpPortDesiginatedId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRstpPortDesiginatedId.setStatus("current")


class _WwpLeosRstpPortDesiginatedPid_Type(OctetString):
    """Custom type wwpLeosRstpPortDesiginatedPid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WwpLeosRstpPortDesiginatedPid_Type.__name__ = "OctetString"
_WwpLeosRstpPortDesiginatedPid_Object = MibTableColumn
wwpLeosRstpPortDesiginatedPid = _WwpLeosRstpPortDesiginatedPid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 2, 1, 1, 3),
    _WwpLeosRstpPortDesiginatedPid_Type()
)
wwpLeosRstpPortDesiginatedPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRstpPortDesiginatedPid.setStatus("current")
_WwpLeosRstpLocalPortExt_ObjectIdentity = ObjectIdentity
wwpLeosRstpLocalPortExt = _WwpLeosRstpLocalPortExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 3)
)
_WwpLeosRstpLocalPortInfoTable_Object = MibTable
wwpLeosRstpLocalPortInfoTable = _WwpLeosRstpLocalPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wwpLeosRstpLocalPortInfoTable.setStatus("current")
_WwpLeosRstpLocalPortInfoEntry_Object = MibTableRow
wwpLeosRstpLocalPortInfoEntry = _WwpLeosRstpLocalPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 3, 1, 1)
)
wwpLeosRstpLocalPortInfoEntry.setIndexNames(
    (0, "WWP-LEOS-RSTP-MIB", "wwpLeosRstpPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosRstpLocalPortInfoEntry.setStatus("current")


class _WwpLeosRstpPortDynPathCostState_Type(Integer32):
    """Custom type wwpLeosRstpPortDynPathCostState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosRstpPortDynPathCostState_Type.__name__ = "Integer32"
_WwpLeosRstpPortDynPathCostState_Object = MibTableColumn
wwpLeosRstpPortDynPathCostState = _WwpLeosRstpPortDynPathCostState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 1, 3, 1, 1, 1),
    _WwpLeosRstpPortDynPathCostState_Type()
)
wwpLeosRstpPortDynPathCostState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRstpPortDynPathCostState.setStatus("current")
_WwpLeosRstpMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosRstpMIBNotificationPrefix = _WwpLeosRstpMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 2)
)
_WwpLeosRstpMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosRstpMIBNotifications = _WwpLeosRstpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 2, 0)
)
_WwpLeosRstpMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosRstpMIBConformance = _WwpLeosRstpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 3)
)
_WwpLeosRstpMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosRstpMIBCompliances = _WwpLeosRstpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 3, 1)
)
_WwpLeosRstpMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosRstpMIBGroups = _WwpLeosRstpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 3, 2)
)

# Managed Objects groups


# Notification objects

wwpLeosRstpPortBackupNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 2, 0, 1)
)
wwpLeosRstpPortBackupNotification.setObjects(
    ("BRIDGE-MIB", "dot1dStpPort")
)
if mibBuilder.loadTexts:
    wwpLeosRstpPortBackupNotification.setStatus(
        "current"
    )

wwpLeosRstpPvstBpduReceivedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 2, 0, 2)
)
wwpLeosRstpPvstBpduReceivedNotification.setObjects(
    ("BRIDGE-MIB", "dot1dStpPort")
)
if mibBuilder.loadTexts:
    wwpLeosRstpPvstBpduReceivedNotification.setStatus(
        "deprecated"
    )

wwpLeosRstpSelfLoopNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 2, 0, 3)
)
wwpLeosRstpSelfLoopNotification.setObjects(
    ("BRIDGE-MIB", "dot1dStpPort")
)
if mibBuilder.loadTexts:
    wwpLeosRstpSelfLoopNotification.setStatus(
        "current"
    )

wwpLeosRstpPortOperEdgeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 2, 0, 4)
)
wwpLeosRstpPortOperEdgeNotification.setObjects(
      *(("BRIDGE-MIB", "dot1dStpPort"),
        ("RSTP-MIB", "dot1dStpPortOperEdgePort"))
)
if mibBuilder.loadTexts:
    wwpLeosRstpPortOperEdgeNotification.setStatus(
        "current"
    )

wwpLeosRstpPortFlapNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 2, 0, 5)
)
wwpLeosRstpPortFlapNotification.setObjects(
    ("BRIDGE-MIB", "dot1dStpPort")
)
if mibBuilder.loadTexts:
    wwpLeosRstpPortFlapNotification.setStatus(
        "current"
    )

wwpLeosRstpBridgeRootPortLostNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 13, 2, 0, 6)
)
wwpLeosRstpBridgeRootPortLostNotification.setObjects(
    ("BRIDGE-MIB", "dot1dStpPort")
)
if mibBuilder.loadTexts:
    wwpLeosRstpBridgeRootPortLostNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-RSTP-MIB",
    **{"wwpLeosRstpMIB": wwpLeosRstpMIB,
       "wwpLeosRstpMIBObjects": wwpLeosRstpMIBObjects,
       "wwpLeosRstpDomain": wwpLeosRstpDomain,
       "wwpLeosRstpMode": wwpLeosRstpMode,
       "wwpLeosRstpDomainTable": wwpLeosRstpDomainTable,
       "wwpLeosRstpDomainEntry": wwpLeosRstpDomainEntry,
       "wwpLeosRstpDomainId": wwpLeosRstpDomainId,
       "wwpLeosRstpDomainName": wwpLeosRstpDomainName,
       "wwpLeosRstpDomainStatus": wwpLeosRstpDomainStatus,
       "wwpLeosRstpDomainMemTable": wwpLeosRstpDomainMemTable,
       "wwpLeosRstpDomainMemEntry": wwpLeosRstpDomainMemEntry,
       "wwpLeosRstpDomainPortId": wwpLeosRstpDomainPortId,
       "wwpLeosRstpDomainMemStatus": wwpLeosRstpDomainMemStatus,
       "wwpLeosRstpBridgeDomainAttrs": wwpLeosRstpBridgeDomainAttrs,
       "wwpLeosRstpDomainAttrsForceVer": wwpLeosRstpDomainAttrsForceVer,
       "wwpLeosRstpDomainAttrsForwardDelay": wwpLeosRstpDomainAttrsForwardDelay,
       "wwpLeosRstpDomainAttrsHelloTime": wwpLeosRstpDomainAttrsHelloTime,
       "wwpLeosRstpDomainAttrsLoopBackBlock": wwpLeosRstpDomainAttrsLoopBackBlock,
       "wwpLeosRstpDomainAttrsMaxAge": wwpLeosRstpDomainAttrsMaxAge,
       "wwpLeosRstpDomainAttrsPathCostDef": wwpLeosRstpDomainAttrsPathCostDef,
       "wwpLeosRstpDomainAttrsPriority": wwpLeosRstpDomainAttrsPriority,
       "wwpLeosRstpDomainAttrsTxHoldCount": wwpLeosRstpDomainAttrsTxHoldCount,
       "wwpLeosRstpDomainAttrTable": wwpLeosRstpDomainAttrTable,
       "wwpLeosRstpDomainAttrEntry": wwpLeosRstpDomainAttrEntry,
       "wwpLeosRstpDomainAttrDesignatedBridgePri": wwpLeosRstpDomainAttrDesignatedBridgePri,
       "wwpLeosRstpDomainAttrDesignatedBridgeMac": wwpLeosRstpDomainAttrDesignatedBridgeMac,
       "wwpLeosRstpDomainAttrDesignatedRootPri": wwpLeosRstpDomainAttrDesignatedRootPri,
       "wwpLeosRstpDomainAttrDesignatedRootMac": wwpLeosRstpDomainAttrDesignatedRootMac,
       "wwpLeosRstpDomainAttrRootCost": wwpLeosRstpDomainAttrRootCost,
       "wwpLeosRstpDomainAttrRootPort": wwpLeosRstpDomainAttrRootPort,
       "wwpLeosRstpDomainAttrMaxAge": wwpLeosRstpDomainAttrMaxAge,
       "wwpLeosRstpDomainAttrHelloTime": wwpLeosRstpDomainAttrHelloTime,
       "wwpLeosRstpDomainAttrHoldTime": wwpLeosRstpDomainAttrHoldTime,
       "wwpLeosRstpDomainAttrForwardDelay": wwpLeosRstpDomainAttrForwardDelay,
       "wwpLeosRstpDomainAttrPriority": wwpLeosRstpDomainAttrPriority,
       "wwpLeosRstpMaxAgeEventInterval": wwpLeosRstpMaxAgeEventInterval,
       "wwpLeosRstpPortExt": wwpLeosRstpPortExt,
       "wwpLeosRstpPortInfoTable": wwpLeosRstpPortInfoTable,
       "wwpLeosRstpPortInfoEntry": wwpLeosRstpPortInfoEntry,
       "wwpLeosRstpPortId": wwpLeosRstpPortId,
       "wwpLeosRstpPortDesiginatedId": wwpLeosRstpPortDesiginatedId,
       "wwpLeosRstpPortDesiginatedPid": wwpLeosRstpPortDesiginatedPid,
       "wwpLeosRstpLocalPortExt": wwpLeosRstpLocalPortExt,
       "wwpLeosRstpLocalPortInfoTable": wwpLeosRstpLocalPortInfoTable,
       "wwpLeosRstpLocalPortInfoEntry": wwpLeosRstpLocalPortInfoEntry,
       "wwpLeosRstpPortDynPathCostState": wwpLeosRstpPortDynPathCostState,
       "wwpLeosRstpMIBNotificationPrefix": wwpLeosRstpMIBNotificationPrefix,
       "wwpLeosRstpMIBNotifications": wwpLeosRstpMIBNotifications,
       "wwpLeosRstpPortBackupNotification": wwpLeosRstpPortBackupNotification,
       "wwpLeosRstpPvstBpduReceivedNotification": wwpLeosRstpPvstBpduReceivedNotification,
       "wwpLeosRstpSelfLoopNotification": wwpLeosRstpSelfLoopNotification,
       "wwpLeosRstpPortOperEdgeNotification": wwpLeosRstpPortOperEdgeNotification,
       "wwpLeosRstpPortFlapNotification": wwpLeosRstpPortFlapNotification,
       "wwpLeosRstpBridgeRootPortLostNotification": wwpLeosRstpBridgeRootPortLostNotification,
       "wwpLeosRstpMIBConformance": wwpLeosRstpMIBConformance,
       "wwpLeosRstpMIBCompliances": wwpLeosRstpMIBCompliances,
       "wwpLeosRstpMIBGroups": wwpLeosRstpMIBGroups}
)
