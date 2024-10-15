# SNMP MIB module (HUAWEI-NTPV3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-NTPV3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:24 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwNtpV3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 234)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwNtpV3MibObjects_ObjectIdentity = ObjectIdentity
hwNtpV3MibObjects = _HwNtpV3MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 1)
)
_HwNtpV3ServerIPAdd_Type = IpAddress
_HwNtpV3ServerIPAdd_Object = MibScalar
hwNtpV3ServerIPAdd = _HwNtpV3ServerIPAdd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 1, 1),
    _HwNtpV3ServerIPAdd_Type()
)
hwNtpV3ServerIPAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNtpV3ServerIPAdd.setStatus("current")
_HwNtpV3TimeSyncPeriod_Type = Integer32
_HwNtpV3TimeSyncPeriod_Object = MibScalar
hwNtpV3TimeSyncPeriod = _HwNtpV3TimeSyncPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 1, 2),
    _HwNtpV3TimeSyncPeriod_Type()
)
hwNtpV3TimeSyncPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNtpV3TimeSyncPeriod.setStatus("current")
_HwNtpV3TimeAfterNTPCal_Type = DisplayString
_HwNtpV3TimeAfterNTPCal_Object = MibScalar
hwNtpV3TimeAfterNTPCal = _HwNtpV3TimeAfterNTPCal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 1, 3),
    _HwNtpV3TimeAfterNTPCal_Type()
)
hwNtpV3TimeAfterNTPCal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNtpV3TimeAfterNTPCal.setStatus("current")
_HwNtpV3Conformance_ObjectIdentity = ObjectIdentity
hwNtpV3Conformance = _HwNtpV3Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 2)
)
_HwNtpV3Compliances_ObjectIdentity = ObjectIdentity
hwNtpV3Compliances = _HwNtpV3Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 2, 1)
)
_HwNtpV3Groups_ObjectIdentity = ObjectIdentity
hwNtpV3Groups = _HwNtpV3Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 2, 2)
)

# Managed Objects groups

hwNtpV3ObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 2, 2, 1)
)
hwNtpV3ObjectGroup.setObjects(
      *(("HUAWEI-NTPV3-MIB", "hwNtpV3ServerIPAdd"),
        ("HUAWEI-NTPV3-MIB", "hwNtpV3TimeSyncPeriod"),
        ("HUAWEI-NTPV3-MIB", "hwNtpV3TimeAfterNTPCal"))
)
if mibBuilder.loadTexts:
    hwNtpV3ObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwNtpV3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwNtpV3Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-NTPV3-MIB",
    **{"hwNtpV3": hwNtpV3,
       "hwNtpV3MibObjects": hwNtpV3MibObjects,
       "hwNtpV3ServerIPAdd": hwNtpV3ServerIPAdd,
       "hwNtpV3TimeSyncPeriod": hwNtpV3TimeSyncPeriod,
       "hwNtpV3TimeAfterNTPCal": hwNtpV3TimeAfterNTPCal,
       "hwNtpV3Conformance": hwNtpV3Conformance,
       "hwNtpV3Compliances": hwNtpV3Compliances,
       "hwNtpV3Compliance": hwNtpV3Compliance,
       "hwNtpV3Groups": hwNtpV3Groups,
       "hwNtpV3ObjectGroup": hwNtpV3ObjectGroup}
)
