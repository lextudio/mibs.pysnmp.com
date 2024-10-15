# SNMP MIB module (ZYXEL-LOAD-SHARING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-LOAD-SHARING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:14 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelLoadSharing = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelLoadSharingSetup_ObjectIdentity = ObjectIdentity
zyxelLoadSharingSetup = _ZyxelLoadSharingSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1)
)
_ZyLoadSharingState_Type = EnabledStatus
_ZyLoadSharingState_Object = MibScalar
zyLoadSharingState = _ZyLoadSharingState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1, 1),
    _ZyLoadSharingState_Type()
)
zyLoadSharingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLoadSharingState.setStatus("current")


class _ZyLoadSharingCriteria_Type(Integer32):
    """Custom type zyLoadSharingCriteria based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("srcDstIp", 2),
          ("srcIp", 1))
    )


_ZyLoadSharingCriteria_Type.__name__ = "Integer32"
_ZyLoadSharingCriteria_Object = MibScalar
zyLoadSharingCriteria = _ZyLoadSharingCriteria_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1, 2),
    _ZyLoadSharingCriteria_Type()
)
zyLoadSharingCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLoadSharingCriteria.setStatus("current")
_ZyLoadSharingAgingTime_Type = Integer32
_ZyLoadSharingAgingTime_Object = MibScalar
zyLoadSharingAgingTime = _ZyLoadSharingAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1, 3),
    _ZyLoadSharingAgingTime_Type()
)
zyLoadSharingAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLoadSharingAgingTime.setStatus("current")
_ZyLoadSharingDiscoverTime_Type = Integer32
_ZyLoadSharingDiscoverTime_Object = MibScalar
zyLoadSharingDiscoverTime = _ZyLoadSharingDiscoverTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1, 4),
    _ZyLoadSharingDiscoverTime_Type()
)
zyLoadSharingDiscoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLoadSharingDiscoverTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-LOAD-SHARING-MIB",
    **{"zyxelLoadSharing": zyxelLoadSharing,
       "zyxelLoadSharingSetup": zyxelLoadSharingSetup,
       "zyLoadSharingState": zyLoadSharingState,
       "zyLoadSharingCriteria": zyLoadSharingCriteria,
       "zyLoadSharingAgingTime": zyLoadSharingAgingTime,
       "zyLoadSharingDiscoverTime": zyLoadSharingDiscoverTime}
)
