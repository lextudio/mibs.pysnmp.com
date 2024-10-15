# SNMP MIB module (TPDIN2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPDIN2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:43 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

tpdin2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45621, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Tenths(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )



# MIB Managed Objects in the order of their OIDs

_Tycon_ObjectIdentity = ObjectIdentity
tycon = _Tycon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45621)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45621, 2, 1)
)
_Name_Type = DisplayString
_Name_Object = MibScalar
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 1, 1),
    _Name_Type()
)
name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    name.setStatus("current")
_Version_Type = DisplayString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 1, 2),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")
_Builddate_Type = DisplayString
_Builddate_Object = MibScalar
builddate = _Builddate_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 1, 3),
    _Builddate_Type()
)
builddate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    builddate.setStatus("current")
_Monitor_ObjectIdentity = ObjectIdentity
monitor = _Monitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2)
)
_Relay1_Type = Integer32
_Relay1_Object = MibScalar
relay1 = _Relay1_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 1),
    _Relay1_Type()
)
relay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay1.setStatus("current")
_Relay2_Type = Integer32
_Relay2_Object = MibScalar
relay2 = _Relay2_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 2),
    _Relay2_Type()
)
relay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay2.setStatus("current")
_Relay3_Type = Integer32
_Relay3_Object = MibScalar
relay3 = _Relay3_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 3),
    _Relay3_Type()
)
relay3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay3.setStatus("current")
_Relay4_Type = Integer32
_Relay4_Object = MibScalar
relay4 = _Relay4_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 4),
    _Relay4_Type()
)
relay4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay4.setStatus("current")
_Voltage1_Type = Tenths
_Voltage1_Object = MibScalar
voltage1 = _Voltage1_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 5),
    _Voltage1_Type()
)
voltage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage1.setStatus("current")
_Voltage2_Type = Tenths
_Voltage2_Object = MibScalar
voltage2 = _Voltage2_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 6),
    _Voltage2_Type()
)
voltage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage2.setStatus("current")
_Voltage3_Type = Tenths
_Voltage3_Object = MibScalar
voltage3 = _Voltage3_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 7),
    _Voltage3_Type()
)
voltage3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage3.setStatus("current")
_Voltage4_Type = Tenths
_Voltage4_Object = MibScalar
voltage4 = _Voltage4_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 8),
    _Voltage4_Type()
)
voltage4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage4.setStatus("current")
_Current1_Type = Tenths
_Current1_Object = MibScalar
current1 = _Current1_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 9),
    _Current1_Type()
)
current1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    current1.setStatus("current")
_Current2_Type = Tenths
_Current2_Object = MibScalar
current2 = _Current2_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 10),
    _Current2_Type()
)
current2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    current2.setStatus("current")
_Current3_Type = Tenths
_Current3_Object = MibScalar
current3 = _Current3_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 11),
    _Current3_Type()
)
current3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    current3.setStatus("current")
_Current4_Type = Tenths
_Current4_Object = MibScalar
current4 = _Current4_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 12),
    _Current4_Type()
)
current4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    current4.setStatus("current")
_Temperature1_Type = Tenths
_Temperature1_Object = MibScalar
temperature1 = _Temperature1_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 13),
    _Temperature1_Type()
)
temperature1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature1.setStatus("current")
_Temperature2_Type = Tenths
_Temperature2_Object = MibScalar
temperature2 = _Temperature2_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 14),
    _Temperature2_Type()
)
temperature2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature2.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPDIN2-MIB",
    **{"Tenths": Tenths,
       "tycon": tycon,
       "tpdin2": tpdin2,
       "product": product,
       "name": name,
       "version": version,
       "builddate": builddate,
       "monitor": monitor,
       "relay1": relay1,
       "relay2": relay2,
       "relay3": relay3,
       "relay4": relay4,
       "voltage1": voltage1,
       "voltage2": voltage2,
       "voltage3": voltage3,
       "voltage4": voltage4,
       "current1": current1,
       "current2": current2,
       "current3": current3,
       "current4": current4,
       "temperature1": temperature1,
       "temperature2": temperature2}
)
