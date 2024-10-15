# SNMP MIB module (DVB-MGSYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DVB-MGSYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:54 2024
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

mgSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dvb_ObjectIdentity = ObjectIdentity
dvb = _Dvb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696)
)
_Mg_ObjectIdentity = ObjectIdentity
mg = _Mg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3)
)
_MgSysDescr_Type = DisplayString
_MgSysDescr_Object = MibScalar
mgSysDescr = _MgSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 1, 1),
    _MgSysDescr_Type()
)
mgSysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgSysDescr.setStatus("current")
_MgSysObjectID_Type = ObjectIdentifier
_MgSysObjectID_Object = MibScalar
mgSysObjectID = _MgSysObjectID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 1, 2),
    _MgSysObjectID_Type()
)
mgSysObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgSysObjectID.setStatus("current")
_MgSysUpTime_Type = TimeTicks
_MgSysUpTime_Object = MibScalar
mgSysUpTime = _MgSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 1, 3),
    _MgSysUpTime_Type()
)
mgSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgSysUpTime.setStatus("current")
_MgSysContact_Type = DisplayString
_MgSysContact_Object = MibScalar
mgSysContact = _MgSysContact_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 1, 4),
    _MgSysContact_Type()
)
mgSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgSysContact.setStatus("current")
_MgSysName_Type = DisplayString
_MgSysName_Object = MibScalar
mgSysName = _MgSysName_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 1, 5),
    _MgSysName_Type()
)
mgSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgSysName.setStatus("current")
_MgSysLocation_Type = DisplayString
_MgSysLocation_Object = MibScalar
mgSysLocation = _MgSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 1, 6),
    _MgSysLocation_Type()
)
mgSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgSysLocation.setStatus("current")


class _MgSysServices_Type(Integer32):
    """Custom type mgSysServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MgSysServices_Type.__name__ = "Integer32"
_MgSysServices_Object = MibScalar
mgSysServices = _MgSysServices_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 1, 7),
    _MgSysServices_Type()
)
mgSysServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgSysServices.setStatus("current")


class _MgSysSerialNumber_Type(DisplayString):
    """Custom type mgSysSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_MgSysSerialNumber_Type.__name__ = "DisplayString"
_MgSysSerialNumber_Object = MibScalar
mgSysSerialNumber = _MgSysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 1, 8),
    _MgSysSerialNumber_Type()
)
mgSysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgSysSerialNumber.setStatus("current")


class _MgSysVersion_Type(DisplayString):
    """Custom type mgSysVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_MgSysVersion_Type.__name__ = "DisplayString"
_MgSysVersion_Object = MibScalar
mgSysVersion = _MgSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 1, 9),
    _MgSysVersion_Type()
)
mgSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgSysVersion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DVB-MGSYSTEM-MIB",
    **{"dvb": dvb,
       "mg": mg,
       "mgSystem": mgSystem,
       "mgSysDescr": mgSysDescr,
       "mgSysObjectID": mgSysObjectID,
       "mgSysUpTime": mgSysUpTime,
       "mgSysContact": mgSysContact,
       "mgSysName": mgSysName,
       "mgSysLocation": mgSysLocation,
       "mgSysServices": mgSysServices,
       "mgSysSerialNumber": mgSysSerialNumber,
       "mgSysVersion": mgSysVersion}
)
