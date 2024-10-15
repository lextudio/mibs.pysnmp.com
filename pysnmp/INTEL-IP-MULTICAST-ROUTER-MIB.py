# SNMP MIB module (INTEL-IP-MULTICAST-ROUTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-IP-MULTICAST-ROUTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:46 2024
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

(mib2ext,) = mibBuilder.importSymbols(
    "INTEL-GEN-MIB",
    "mib2ext")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ipmrouter_ObjectIdentity = ObjectIdentity
ipmrouter = _Ipmrouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 32)
)
_Conf_ObjectIdentity = ObjectIdentity
conf = _Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 32, 1)
)


class _ConfMaxDvmrpRoutes_Type(Integer32):
    """Custom type confMaxDvmrpRoutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_ConfMaxDvmrpRoutes_Type.__name__ = "Integer32"
_ConfMaxDvmrpRoutes_Object = MibScalar
confMaxDvmrpRoutes = _ConfMaxDvmrpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 32, 1, 1),
    _ConfMaxDvmrpRoutes_Type()
)
confMaxDvmrpRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confMaxDvmrpRoutes.setStatus("mandatory")
_ConfIfTable_Object = MibTable
confIfTable = _ConfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 32, 1, 2)
)
if mibBuilder.loadTexts:
    confIfTable.setStatus("mandatory")
_ConfIfEntry_Object = MibTableRow
confIfEntry = _ConfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 32, 1, 2, 1)
)
confIfEntry.setIndexNames(
    (0, "INTEL-IP-MULTICAST-ROUTER-MIB", "confIfIndex"),
)
if mibBuilder.loadTexts:
    confIfEntry.setStatus("mandatory")
_ConfIfIndex_Type = Integer32
_ConfIfIndex_Object = MibTableColumn
confIfIndex = _ConfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 32, 1, 2, 1, 1),
    _ConfIfIndex_Type()
)
confIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confIfIndex.setStatus("mandatory")


class _ConfIfMCRouteProto_Type(Integer32):
    """Custom type confIfMCRouteProto based on Integer32"""
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


_ConfIfMCRouteProto_Type.__name__ = "Integer32"
_ConfIfMCRouteProto_Object = MibTableColumn
confIfMCRouteProto = _ConfIfMCRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 32, 1, 2, 1, 2),
    _ConfIfMCRouteProto_Type()
)
confIfMCRouteProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfMCRouteProto.setStatus("mandatory")
_ConfIfIgmpQueryInterval_Type = Integer32
_ConfIfIgmpQueryInterval_Object = MibTableColumn
confIfIgmpQueryInterval = _ConfIfIgmpQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 32, 1, 2, 1, 3),
    _ConfIfIgmpQueryInterval_Type()
)
confIfIgmpQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfIgmpQueryInterval.setStatus("mandatory")
_ConfIfIgmpRobustness_Type = Integer32
_ConfIfIgmpRobustness_Object = MibTableColumn
confIfIgmpRobustness = _ConfIfIgmpRobustness_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 32, 1, 2, 1, 4),
    _ConfIfIgmpRobustness_Type()
)
confIfIgmpRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfIgmpRobustness.setStatus("mandatory")


class _ConfIfDvmrpMetric_Type(Integer32):
    """Custom type confIfDvmrpMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_ConfIfDvmrpMetric_Type.__name__ = "Integer32"
_ConfIfDvmrpMetric_Object = MibTableColumn
confIfDvmrpMetric = _ConfIfDvmrpMetric_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 32, 1, 2, 1, 5),
    _ConfIfDvmrpMetric_Type()
)
confIfDvmrpMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfDvmrpMetric.setStatus("mandatory")


class _ConfIfDvmrpUnreachableMetric_Type(Integer32):
    """Custom type confIfDvmrpUnreachableMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_ConfIfDvmrpUnreachableMetric_Type.__name__ = "Integer32"
_ConfIfDvmrpUnreachableMetric_Object = MibTableColumn
confIfDvmrpUnreachableMetric = _ConfIfDvmrpUnreachableMetric_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 32, 1, 2, 1, 6),
    _ConfIfDvmrpUnreachableMetric_Type()
)
confIfDvmrpUnreachableMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfDvmrpUnreachableMetric.setStatus("mandatory")


class _ConfIfCreateObj_Type(OctetString):
    """Custom type confIfCreateObj based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_ConfIfCreateObj_Type.__name__ = "OctetString"
_ConfIfCreateObj_Object = MibTableColumn
confIfCreateObj = _ConfIfCreateObj_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 32, 1, 2, 1, 7),
    _ConfIfCreateObj_Type()
)
confIfCreateObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfCreateObj.setStatus("mandatory")


class _ConfIfDeleteObj_Type(Integer32):
    """Custom type confIfDeleteObj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete", 1)
    )


_ConfIfDeleteObj_Type.__name__ = "Integer32"
_ConfIfDeleteObj_Object = MibTableColumn
confIfDeleteObj = _ConfIfDeleteObj_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 32, 1, 2, 1, 8),
    _ConfIfDeleteObj_Type()
)
confIfDeleteObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfDeleteObj.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-IP-MULTICAST-ROUTER-MIB",
    **{"ipmrouter": ipmrouter,
       "conf": conf,
       "confMaxDvmrpRoutes": confMaxDvmrpRoutes,
       "confIfTable": confIfTable,
       "confIfEntry": confIfEntry,
       "confIfIndex": confIfIndex,
       "confIfMCRouteProto": confIfMCRouteProto,
       "confIfIgmpQueryInterval": confIfIgmpQueryInterval,
       "confIfIgmpRobustness": confIfIgmpRobustness,
       "confIfDvmrpMetric": confIfDvmrpMetric,
       "confIfDvmrpUnreachableMetric": confIfDvmrpUnreachableMetric,
       "confIfCreateObj": confIfCreateObj,
       "confIfDeleteObj": confIfDeleteObj}
)
