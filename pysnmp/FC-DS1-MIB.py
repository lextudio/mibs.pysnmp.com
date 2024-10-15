# SNMP MIB module (FC-DS1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FC-DS1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:16 2024
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
 ObjectName,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "ObjectName",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "snmpModules")

(DisplayString,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

fcDS1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lucent_ObjectIdentity = ObjectIdentity
lucent = _Lucent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1)
)
_SoftSwitch_ObjectIdentity = ObjectIdentity
softSwitch = _SoftSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198)
)
_FcDeviceServer_ObjectIdentity = ObjectIdentity
fcDeviceServer = _FcDeviceServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9)
)
_FcSystem_ObjectIdentity = ObjectIdentity
fcSystem = _FcSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 1, 1)
)


class _FCServer_Type(Integer32):
    """Custom type fCServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_FCServer_Type.__name__ = "Integer32"
_FCServer_Object = MibScalar
fCServer = _FCServer_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 1, 1, 1),
    _FCServer_Type()
)
fCServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fCServer.setStatus("current")


class _FCApp_Type(Integer32):
    """Custom type fCApp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_FCApp_Type.__name__ = "Integer32"
_FCApp_Object = MibScalar
fCApp = _FCApp_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 1, 1, 2),
    _FCApp_Type()
)
fCApp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fCApp.setStatus("current")
_FCDescText_Type = DisplayString
_FCDescText_Object = MibScalar
fCDescText = _FCDescText_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 1, 1, 3),
    _FCDescText_Type()
)
fCDescText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fCDescText.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FC-DS1-MIB",
    **{"lucent": lucent,
       "products": products,
       "softSwitch": softSwitch,
       "fcDeviceServer": fcDeviceServer,
       "fcDS1": fcDS1,
       "fcSystem": fcSystem,
       "fCServer": fCServer,
       "fCApp": fCApp,
       "fCDescText": fCDescText}
)
