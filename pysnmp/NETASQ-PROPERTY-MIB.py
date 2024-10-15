# SNMP MIB module (NETASQ-PROPERTY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETASQ-PROPERTY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:32 2024
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

(ntqProductProperty,) = mibBuilder.importSymbols(
    "NETASQ-SMI-MIB",
    "ntqProductProperty")

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



class _NtqModel_Type(DisplayString):
    """Custom type ntqModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtqModel_Type.__name__ = "DisplayString"
_NtqModel_Object = MibScalar
ntqModel = _NtqModel_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 1),
    _NtqModel_Type()
)
ntqModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqModel.setStatus("current")


class _NtqVersion_Type(DisplayString):
    """Custom type ntqVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtqVersion_Type.__name__ = "DisplayString"
_NtqVersion_Object = MibScalar
ntqVersion = _NtqVersion_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 2),
    _NtqVersion_Type()
)
ntqVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqVersion.setStatus("current")


class _NtqSerialNumber_Type(DisplayString):
    """Custom type ntqSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtqSerialNumber_Type.__name__ = "DisplayString"
_NtqSerialNumber_Object = MibScalar
ntqSerialNumber = _NtqSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 3),
    _NtqSerialNumber_Type()
)
ntqSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqSerialNumber.setStatus("current")


class _NtqSystemName_Type(DisplayString):
    """Custom type ntqSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtqSystemName_Type.__name__ = "DisplayString"
_NtqSystemName_Object = MibScalar
ntqSystemName = _NtqSystemName_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 4),
    _NtqSystemName_Type()
)
ntqSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqSystemName.setStatus("current")


class _NtqSystemLanguage_Type(DisplayString):
    """Custom type ntqSystemLanguage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtqSystemLanguage_Type.__name__ = "DisplayString"
_NtqSystemLanguage_Object = MibScalar
ntqSystemLanguage = _NtqSystemLanguage_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 5),
    _NtqSystemLanguage_Type()
)
ntqSystemLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqSystemLanguage.setStatus("current")
_NtqNbEther_Type = Integer32
_NtqNbEther_Object = MibScalar
ntqNbEther = _NtqNbEther_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 6),
    _NtqNbEther_Type()
)
ntqNbEther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqNbEther.setStatus("current")
_NtqNbVlan_Type = Integer32
_NtqNbVlan_Object = MibScalar
ntqNbVlan = _NtqNbVlan_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 7),
    _NtqNbVlan_Type()
)
ntqNbVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqNbVlan.setStatus("current")
_NtqNbDialup_Type = Integer32
_NtqNbDialup_Object = MibScalar
ntqNbDialup = _NtqNbDialup_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 8),
    _NtqNbDialup_Type()
)
ntqNbDialup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqNbDialup.setStatus("current")
_NtqNbPPTP_Type = Integer32
_NtqNbPPTP_Object = MibScalar
ntqNbPPTP = _NtqNbPPTP_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 9),
    _NtqNbPPTP_Type()
)
ntqNbPPTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqNbPPTP.setStatus("current")
_NtqNbSerial_Type = Integer32
_NtqNbSerial_Object = MibScalar
ntqNbSerial = _NtqNbSerial_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 10),
    _NtqNbSerial_Type()
)
ntqNbSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqNbSerial.setStatus("current")
_NtqNbLoopback_Type = Integer32
_NtqNbLoopback_Object = MibScalar
ntqNbLoopback = _NtqNbLoopback_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 11),
    _NtqNbLoopback_Type()
)
ntqNbLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqNbLoopback.setStatus("current")
_NtqWatchdog_Type = Integer32
_NtqWatchdog_Object = MibScalar
ntqWatchdog = _NtqWatchdog_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 12),
    _NtqWatchdog_Type()
)
ntqWatchdog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqWatchdog.setStatus("current")
_NtqLed_Type = Integer32
_NtqLed_Object = MibScalar
ntqLed = _NtqLed_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 13),
    _NtqLed_Type()
)
ntqLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqLed.setStatus("current")
_NtqClone_Type = Integer32
_NtqClone_Object = MibScalar
ntqClone = _NtqClone_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 14),
    _NtqClone_Type()
)
ntqClone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqClone.setStatus("current")
_NtqHADialup_Type = Integer32
_NtqHADialup_Object = MibScalar
ntqHADialup = _NtqHADialup_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0, 15),
    _NtqHADialup_Type()
)
ntqHADialup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqHADialup.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETASQ-PROPERTY-MIB",
    **{"ntqModel": ntqModel,
       "ntqVersion": ntqVersion,
       "ntqSerialNumber": ntqSerialNumber,
       "ntqSystemName": ntqSystemName,
       "ntqSystemLanguage": ntqSystemLanguage,
       "ntqNbEther": ntqNbEther,
       "ntqNbVlan": ntqNbVlan,
       "ntqNbDialup": ntqNbDialup,
       "ntqNbPPTP": ntqNbPPTP,
       "ntqNbSerial": ntqNbSerial,
       "ntqNbLoopback": ntqNbLoopback,
       "ntqWatchdog": ntqWatchdog,
       "ntqLed": ntqLed,
       "ntqClone": ntqClone,
       "ntqHADialup": ntqHADialup}
)
