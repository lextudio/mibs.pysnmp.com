# SNMP MIB module (WATCHGUARD-INFO-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WATCHGUARD-INFO-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:32 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")

(watchguard,) = mibBuilder.importSymbols(
    "WATCHGUARD-SMI",
    "watchguard")


# MODULE-IDENTITY

wgInfoModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 6)
)
wgInfoModule.setRevisions(
        ("2007-01-25 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WgInfoSystem_ObjectIdentity = ObjectIdentity
wgInfoSystem = _WgInfoSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 6, 1)
)
if mibBuilder.loadTexts:
    wgInfoSystem.setStatus("current")
_WgInfoSystemCurrentTime_Type = DateAndTime
_WgInfoSystemCurrentTime_Object = MibScalar
wgInfoSystemCurrentTime = _WgInfoSystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 1, 1),
    _WgInfoSystemCurrentTime_Type()
)
wgInfoSystemCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgInfoSystemCurrentTime.setStatus("current")


class _WgInfoGavService_Type(OctetString):
    """Custom type wgInfoGavService based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WgInfoGavService_Type.__name__ = "OctetString"
_WgInfoGavService_Object = MibScalar
wgInfoGavService = _WgInfoGavService_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 1, 3),
    _WgInfoGavService_Type()
)
wgInfoGavService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgInfoGavService.setStatus("current")


class _WgInfoIpsService_Type(OctetString):
    """Custom type wgInfoIpsService based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WgInfoIpsService_Type.__name__ = "OctetString"
_WgInfoIpsService_Object = MibScalar
wgInfoIpsService = _WgInfoIpsService_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 1, 4),
    _WgInfoIpsService_Type()
)
wgInfoIpsService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgInfoIpsService.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WATCHGUARD-INFO-SYSTEM-MIB",
    **{"wgInfoModule": wgInfoModule,
       "wgInfoSystem": wgInfoSystem,
       "wgInfoSystemCurrentTime": wgInfoSystemCurrentTime,
       "wgInfoGavService": wgInfoGavService,
       "wgInfoIpsService": wgInfoIpsService}
)
