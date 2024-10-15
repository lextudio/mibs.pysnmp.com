# SNMP MIB module (ELTEX-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:15 2024
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

(eltexLtd,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "eltexLtd")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

eltQos = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 20)
)
eltQos.setRevisions(
        ("2015-04-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltQosPolicyStats_ObjectIdentity = ObjectIdentity
eltQosPolicyStats = _EltQosPolicyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 20, 1)
)
_EltQosPolicyStatsTable_Object = MibTable
eltQosPolicyStatsTable = _EltQosPolicyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 20, 1, 1)
)
if mibBuilder.loadTexts:
    eltQosPolicyStatsTable.setStatus("current")
_EltQosPolicyStatsEntry_Object = MibTableRow
eltQosPolicyStatsEntry = _EltQosPolicyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 20, 1, 1, 1)
)
eltQosPolicyStatsEntry.setIndexNames(
    (0, "ELTEX-QOS-MIB", "eltQosPolicyStatsPolicyIndex"),
)
if mibBuilder.loadTexts:
    eltQosPolicyStatsEntry.setStatus("current")


class _EltQosPolicyStatsPolicyIndex_Type(Integer32):
    """Custom type eltQosPolicyStatsPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EltQosPolicyStatsPolicyIndex_Type.__name__ = "Integer32"
_EltQosPolicyStatsPolicyIndex_Object = MibTableColumn
eltQosPolicyStatsPolicyIndex = _EltQosPolicyStatsPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 20, 1, 1, 1, 1),
    _EltQosPolicyStatsPolicyIndex_Type()
)
eltQosPolicyStatsPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosPolicyStatsPolicyIndex.setStatus("current")


class _EltQosPolicyStatsifDescr_Type(DisplayString):
    """Custom type eltQosPolicyStatsifDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EltQosPolicyStatsifDescr_Type.__name__ = "DisplayString"
_EltQosPolicyStatsifDescr_Object = MibTableColumn
eltQosPolicyStatsifDescr = _EltQosPolicyStatsifDescr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 20, 1, 1, 1, 2),
    _EltQosPolicyStatsifDescr_Type()
)
eltQosPolicyStatsifDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosPolicyStatsifDescr.setStatus("current")


class _EltQosPolicyStatsPolicy_Type(DisplayString):
    """Custom type eltQosPolicyStatsPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EltQosPolicyStatsPolicy_Type.__name__ = "DisplayString"
_EltQosPolicyStatsPolicy_Object = MibTableColumn
eltQosPolicyStatsPolicy = _EltQosPolicyStatsPolicy_Object(
    (1, 3, 6, 1, 4, 1, 35265, 20, 1, 1, 1, 3),
    _EltQosPolicyStatsPolicy_Type()
)
eltQosPolicyStatsPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosPolicyStatsPolicy.setStatus("current")
_EltQosPolicyStatsBytes_Type = Counter64
_EltQosPolicyStatsBytes_Object = MibTableColumn
eltQosPolicyStatsBytes = _EltQosPolicyStatsBytes_Object(
    (1, 3, 6, 1, 4, 1, 35265, 20, 1, 1, 1, 4),
    _EltQosPolicyStatsBytes_Type()
)
eltQosPolicyStatsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosPolicyStatsBytes.setStatus("current")
_EltQosPolicyStatsPkts_Type = Counter64
_EltQosPolicyStatsPkts_Object = MibTableColumn
eltQosPolicyStatsPkts = _EltQosPolicyStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 20, 1, 1, 1, 5),
    _EltQosPolicyStatsPkts_Type()
)
eltQosPolicyStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosPolicyStatsPkts.setStatus("current")
_EltQosPolicyStatsDrops_Type = Counter64
_EltQosPolicyStatsDrops_Object = MibTableColumn
eltQosPolicyStatsDrops = _EltQosPolicyStatsDrops_Object(
    (1, 3, 6, 1, 4, 1, 35265, 20, 1, 1, 1, 6),
    _EltQosPolicyStatsDrops_Type()
)
eltQosPolicyStatsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosPolicyStatsDrops.setStatus("current")
_EltQosClassStats_ObjectIdentity = ObjectIdentity
eltQosClassStats = _EltQosClassStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 20, 2)
)
_EltQosClassStatsTable_Object = MibTable
eltQosClassStatsTable = _EltQosClassStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 20, 2, 1)
)
if mibBuilder.loadTexts:
    eltQosClassStatsTable.setStatus("current")
_EltQosClassStatsEntry_Object = MibTableRow
eltQosClassStatsEntry = _EltQosClassStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 20, 2, 1, 1)
)
eltQosClassStatsEntry.setIndexNames(
    (0, "ELTEX-QOS-MIB", "eltQosClassStatsClassIndex"),
)
if mibBuilder.loadTexts:
    eltQosClassStatsEntry.setStatus("current")


class _EltQosClassStatsClassIndex_Type(Integer32):
    """Custom type eltQosClassStatsClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EltQosClassStatsClassIndex_Type.__name__ = "Integer32"
_EltQosClassStatsClassIndex_Object = MibTableColumn
eltQosClassStatsClassIndex = _EltQosClassStatsClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 20, 2, 1, 1, 1),
    _EltQosClassStatsClassIndex_Type()
)
eltQosClassStatsClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosClassStatsClassIndex.setStatus("current")


class _EltQosClassStatsifDescr_Type(DisplayString):
    """Custom type eltQosClassStatsifDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EltQosClassStatsifDescr_Type.__name__ = "DisplayString"
_EltQosClassStatsifDescr_Object = MibTableColumn
eltQosClassStatsifDescr = _EltQosClassStatsifDescr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 20, 2, 1, 1, 2),
    _EltQosClassStatsifDescr_Type()
)
eltQosClassStatsifDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosClassStatsifDescr.setStatus("current")


class _EltQosClassStatsClass_Type(DisplayString):
    """Custom type eltQosClassStatsClass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EltQosClassStatsClass_Type.__name__ = "DisplayString"
_EltQosClassStatsClass_Object = MibTableColumn
eltQosClassStatsClass = _EltQosClassStatsClass_Object(
    (1, 3, 6, 1, 4, 1, 35265, 20, 2, 1, 1, 3),
    _EltQosClassStatsClass_Type()
)
eltQosClassStatsClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosClassStatsClass.setStatus("current")


class _EltQosClassStatsPolicy_Type(DisplayString):
    """Custom type eltQosClassStatsPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EltQosClassStatsPolicy_Type.__name__ = "DisplayString"
_EltQosClassStatsPolicy_Object = MibTableColumn
eltQosClassStatsPolicy = _EltQosClassStatsPolicy_Object(
    (1, 3, 6, 1, 4, 1, 35265, 20, 2, 1, 1, 4),
    _EltQosClassStatsPolicy_Type()
)
eltQosClassStatsPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosClassStatsPolicy.setStatus("current")
_EltQosClassStatsBytes_Type = Counter64
_EltQosClassStatsBytes_Object = MibTableColumn
eltQosClassStatsBytes = _EltQosClassStatsBytes_Object(
    (1, 3, 6, 1, 4, 1, 35265, 20, 2, 1, 1, 5),
    _EltQosClassStatsBytes_Type()
)
eltQosClassStatsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosClassStatsBytes.setStatus("current")
_EltQosClassStatsPkts_Type = Counter64
_EltQosClassStatsPkts_Object = MibTableColumn
eltQosClassStatsPkts = _EltQosClassStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 20, 2, 1, 1, 6),
    _EltQosClassStatsPkts_Type()
)
eltQosClassStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosClassStatsPkts.setStatus("current")
_EltQosClassStatsDrops_Type = Counter64
_EltQosClassStatsDrops_Object = MibTableColumn
eltQosClassStatsDrops = _EltQosClassStatsDrops_Object(
    (1, 3, 6, 1, 4, 1, 35265, 20, 2, 1, 1, 7),
    _EltQosClassStatsDrops_Type()
)
eltQosClassStatsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosClassStatsDrops.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-QOS-MIB",
    **{"eltQos": eltQos,
       "eltQosPolicyStats": eltQosPolicyStats,
       "eltQosPolicyStatsTable": eltQosPolicyStatsTable,
       "eltQosPolicyStatsEntry": eltQosPolicyStatsEntry,
       "eltQosPolicyStatsPolicyIndex": eltQosPolicyStatsPolicyIndex,
       "eltQosPolicyStatsifDescr": eltQosPolicyStatsifDescr,
       "eltQosPolicyStatsPolicy": eltQosPolicyStatsPolicy,
       "eltQosPolicyStatsBytes": eltQosPolicyStatsBytes,
       "eltQosPolicyStatsPkts": eltQosPolicyStatsPkts,
       "eltQosPolicyStatsDrops": eltQosPolicyStatsDrops,
       "eltQosClassStats": eltQosClassStats,
       "eltQosClassStatsTable": eltQosClassStatsTable,
       "eltQosClassStatsEntry": eltQosClassStatsEntry,
       "eltQosClassStatsClassIndex": eltQosClassStatsClassIndex,
       "eltQosClassStatsifDescr": eltQosClassStatsifDescr,
       "eltQosClassStatsClass": eltQosClassStatsClass,
       "eltQosClassStatsPolicy": eltQosClassStatsPolicy,
       "eltQosClassStatsBytes": eltQosClassStatsBytes,
       "eltQosClassStatsPkts": eltQosClassStatsPkts,
       "eltQosClassStatsDrops": eltQosClassStatsDrops}
)
