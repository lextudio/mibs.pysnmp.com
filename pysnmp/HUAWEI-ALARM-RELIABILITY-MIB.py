# SNMP MIB module (HUAWEI-ALARM-RELIABILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-ALARM-RELIABILITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:44 2024
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
 RowStatus,
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

hwARModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 141)
)
hwARModule.setRevisions(
        ("2006-12-14 20:10",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwAR_ObjectIdentity = ObjectIdentity
hwAR = _HwAR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 1)
)


class _HwARInformPendings_Type(Integer32):
    """Custom type hwARInformPendings based on Integer32"""
    defaultValue = 39

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_HwARInformPendings_Type.__name__ = "Integer32"
_HwARInformPendings_Object = MibScalar
hwARInformPendings = _HwARInformPendings_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 1, 1),
    _HwARInformPendings_Type()
)
hwARInformPendings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwARInformPendings.setStatus("current")


class _HwARRetryCount_Type(Integer32):
    """Custom type hwARRetryCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_HwARRetryCount_Type.__name__ = "Integer32"
_HwARRetryCount_Object = MibScalar
hwARRetryCount = _HwARRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 1, 2),
    _HwARRetryCount_Type()
)
hwARRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwARRetryCount.setStatus("current")


class _HwARTimeout_Type(TimeInterval):
    """Custom type hwARTimeout based on TimeInterval"""
    defaultValue = 1500

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 180000),
    )


_HwARTimeout_Type.__name__ = "TimeInterval"
_HwARTimeout_Object = MibScalar
hwARTimeout = _HwARTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 1, 3),
    _HwARTimeout_Type()
)
hwARTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwARTimeout.setStatus("current")
_HwARConformance_ObjectIdentity = ObjectIdentity
hwARConformance = _HwARConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 2)
)
_HwARCompliances_ObjectIdentity = ObjectIdentity
hwARCompliances = _HwARCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 2, 1)
)
_HwARGroups_ObjectIdentity = ObjectIdentity
hwARGroups = _HwARGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 2, 2)
)

# Managed Objects groups

hwARInformPacketsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 2, 2, 1)
)
hwARInformPacketsGroup.setObjects(
      *(("HUAWEI-ALARM-RELIABILITY-MIB", "hwARInformPendings"),
        ("HUAWEI-ALARM-RELIABILITY-MIB", "hwARRetryCount"),
        ("HUAWEI-ALARM-RELIABILITY-MIB", "hwARTimeout"))
)
if mibBuilder.loadTexts:
    hwARInformPacketsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwARCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwARCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-ALARM-RELIABILITY-MIB",
    **{"hwARModule": hwARModule,
       "hwAR": hwAR,
       "hwARInformPendings": hwARInformPendings,
       "hwARRetryCount": hwARRetryCount,
       "hwARTimeout": hwARTimeout,
       "hwARConformance": hwARConformance,
       "hwARCompliances": hwARCompliances,
       "hwARCompliance": hwARCompliance,
       "hwARGroups": hwARGroups,
       "hwARInformPacketsGroup": hwARInformPacketsGroup}
)
