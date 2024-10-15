# SNMP MIB module (XEDIA-DRIVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEDIA-DRIVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:47 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(xediaMibs,) = mibBuilder.importSymbols(
    "XEDIA-REG",
    "xediaMibs")


# MODULE-IDENTITY

xediaDriverMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XdriverObjects_ObjectIdentity = ObjectIdentity
xdriverObjects = _XdriverObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 6, 1)
)
_XdriverStatsTable_Object = MibTable
xdriverStatsTable = _XdriverStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1)
)
if mibBuilder.loadTexts:
    xdriverStatsTable.setStatus("current")
_XdriverStatsEntry_Object = MibTableRow
xdriverStatsEntry = _XdriverStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1, 1)
)
xdriverStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xdriverStatsEntry.setStatus("current")
_XdriverStatsInternalQOverflows_Type = Counter32
_XdriverStatsInternalQOverflows_Object = MibTableColumn
xdriverStatsInternalQOverflows = _XdriverStatsInternalQOverflows_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1, 1, 1),
    _XdriverStatsInternalQOverflows_Type()
)
xdriverStatsInternalQOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdriverStatsInternalQOverflows.setStatus("current")
_XdriverStatsOutGoodFrames_Type = Counter32
_XdriverStatsOutGoodFrames_Object = MibTableColumn
xdriverStatsOutGoodFrames = _XdriverStatsOutGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1, 1, 2),
    _XdriverStatsOutGoodFrames_Type()
)
xdriverStatsOutGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdriverStatsOutGoodFrames.setStatus("current")


class _XdriverStatsOutPercentGood_Type(Gauge32):
    """Custom type xdriverStatsOutPercentGood based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XdriverStatsOutPercentGood_Type.__name__ = "Gauge32"
_XdriverStatsOutPercentGood_Object = MibTableColumn
xdriverStatsOutPercentGood = _XdriverStatsOutPercentGood_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1, 1, 3),
    _XdriverStatsOutPercentGood_Type()
)
xdriverStatsOutPercentGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdriverStatsOutPercentGood.setStatus("current")
if mibBuilder.loadTexts:
    xdriverStatsOutPercentGood.setUnits("%")


class _XdriverStatsOutPercentBad_Type(Gauge32):
    """Custom type xdriverStatsOutPercentBad based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XdriverStatsOutPercentBad_Type.__name__ = "Gauge32"
_XdriverStatsOutPercentBad_Object = MibTableColumn
xdriverStatsOutPercentBad = _XdriverStatsOutPercentBad_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1, 1, 4),
    _XdriverStatsOutPercentBad_Type()
)
xdriverStatsOutPercentBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdriverStatsOutPercentBad.setStatus("current")
if mibBuilder.loadTexts:
    xdriverStatsOutPercentBad.setUnits("%")
_XdriverStatsOutAvgFrameLen_Type = Gauge32
_XdriverStatsOutAvgFrameLen_Object = MibTableColumn
xdriverStatsOutAvgFrameLen = _XdriverStatsOutAvgFrameLen_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1, 1, 5),
    _XdriverStatsOutAvgFrameLen_Type()
)
xdriverStatsOutAvgFrameLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdriverStatsOutAvgFrameLen.setStatus("current")
_XdriverStatsInCRCErrors_Type = Gauge32
_XdriverStatsInCRCErrors_Object = MibTableColumn
xdriverStatsInCRCErrors = _XdriverStatsInCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1, 1, 6),
    _XdriverStatsInCRCErrors_Type()
)
xdriverStatsInCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdriverStatsInCRCErrors.setStatus("current")
_XdriverStatsInGoodFrames_Type = Counter32
_XdriverStatsInGoodFrames_Object = MibTableColumn
xdriverStatsInGoodFrames = _XdriverStatsInGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1, 1, 7),
    _XdriverStatsInGoodFrames_Type()
)
xdriverStatsInGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdriverStatsInGoodFrames.setStatus("current")
_XdriverStatsInNoResources_Type = Counter32
_XdriverStatsInNoResources_Object = MibTableColumn
xdriverStatsInNoResources = _XdriverStatsInNoResources_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1, 1, 8),
    _XdriverStatsInNoResources_Type()
)
xdriverStatsInNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdriverStatsInNoResources.setStatus("current")


class _XdriverStatsInPercentGood_Type(Gauge32):
    """Custom type xdriverStatsInPercentGood based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XdriverStatsInPercentGood_Type.__name__ = "Gauge32"
_XdriverStatsInPercentGood_Object = MibTableColumn
xdriverStatsInPercentGood = _XdriverStatsInPercentGood_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1, 1, 9),
    _XdriverStatsInPercentGood_Type()
)
xdriverStatsInPercentGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdriverStatsInPercentGood.setStatus("current")
if mibBuilder.loadTexts:
    xdriverStatsInPercentGood.setUnits("%")


class _XdriverStatsInPercentBad_Type(Gauge32):
    """Custom type xdriverStatsInPercentBad based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XdriverStatsInPercentBad_Type.__name__ = "Gauge32"
_XdriverStatsInPercentBad_Object = MibTableColumn
xdriverStatsInPercentBad = _XdriverStatsInPercentBad_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1, 1, 10),
    _XdriverStatsInPercentBad_Type()
)
xdriverStatsInPercentBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdriverStatsInPercentBad.setStatus("current")
if mibBuilder.loadTexts:
    xdriverStatsInPercentBad.setUnits("%")
_XdriverStatsInAvgFrameLen_Type = Gauge32
_XdriverStatsInAvgFrameLen_Object = MibTableColumn
xdriverStatsInAvgFrameLen = _XdriverStatsInAvgFrameLen_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1, 1, 11),
    _XdriverStatsInAvgFrameLen_Type()
)
xdriverStatsInAvgFrameLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdriverStatsInAvgFrameLen.setStatus("current")
_XdriverConformance_ObjectIdentity = ObjectIdentity
xdriverConformance = _XdriverConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 6, 2)
)
_XdriverCompliances_ObjectIdentity = ObjectIdentity
xdriverCompliances = _XdriverCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 6, 2, 1)
)
_XdriverGroups_ObjectIdentity = ObjectIdentity
xdriverGroups = _XdriverGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 6, 2, 2)
)

# Managed Objects groups

xdriverGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 6, 2, 2, 1)
)
xdriverGroup.setObjects(
      *(("XEDIA-DRIVER-MIB", "xdriverStatsInternalQOverflows"),
        ("XEDIA-DRIVER-MIB", "xdriverStatsOutGoodFrames"),
        ("XEDIA-DRIVER-MIB", "xdriverStatsOutPercentGood"),
        ("XEDIA-DRIVER-MIB", "xdriverStatsOutPercentBad"),
        ("XEDIA-DRIVER-MIB", "xdriverStatsOutAvgFrameLen"),
        ("XEDIA-DRIVER-MIB", "xdriverStatsInCRCErrors"),
        ("XEDIA-DRIVER-MIB", "xdriverStatsInGoodFrames"),
        ("XEDIA-DRIVER-MIB", "xdriverStatsInNoResources"),
        ("XEDIA-DRIVER-MIB", "xdriverStatsInPercentGood"),
        ("XEDIA-DRIVER-MIB", "xdriverStatsInPercentBad"),
        ("XEDIA-DRIVER-MIB", "xdriverStatsInAvgFrameLen"))
)
if mibBuilder.loadTexts:
    xdriverGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xdriverCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 838, 3, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xdriverCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-DRIVER-MIB",
    **{"xediaDriverMIB": xediaDriverMIB,
       "xdriverObjects": xdriverObjects,
       "xdriverStatsTable": xdriverStatsTable,
       "xdriverStatsEntry": xdriverStatsEntry,
       "xdriverStatsInternalQOverflows": xdriverStatsInternalQOverflows,
       "xdriverStatsOutGoodFrames": xdriverStatsOutGoodFrames,
       "xdriverStatsOutPercentGood": xdriverStatsOutPercentGood,
       "xdriverStatsOutPercentBad": xdriverStatsOutPercentBad,
       "xdriverStatsOutAvgFrameLen": xdriverStatsOutAvgFrameLen,
       "xdriverStatsInCRCErrors": xdriverStatsInCRCErrors,
       "xdriverStatsInGoodFrames": xdriverStatsInGoodFrames,
       "xdriverStatsInNoResources": xdriverStatsInNoResources,
       "xdriverStatsInPercentGood": xdriverStatsInPercentGood,
       "xdriverStatsInPercentBad": xdriverStatsInPercentBad,
       "xdriverStatsInAvgFrameLen": xdriverStatsInAvgFrameLen,
       "xdriverConformance": xdriverConformance,
       "xdriverCompliances": xdriverCompliances,
       "xdriverCompliance": xdriverCompliance,
       "xdriverGroups": xdriverGroups,
       "xdriverGroup": xdriverGroup}
)
