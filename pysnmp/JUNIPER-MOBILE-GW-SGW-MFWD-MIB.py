# SNMP MIB module (JUNIPER-MOBILE-GW-SGW-MFWD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-MOBILE-GW-SGW-MFWD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:53 2024
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

(jnxMobileGatewaySgw,) = mibBuilder.importSymbols(
    "JUNIPER-MBG-SMI",
    "jnxMobileGatewaySgw")

(EnabledStatus,) = mibBuilder.importSymbols(
    "JUNIPER-MIMSTP-MIB",
    "EnabledStatus")

(jnxMbgGwName,) = mibBuilder.importSymbols(
    "JUNIPER-MOBILE-GATEWAYS",
    "jnxMbgGwName")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

jnxMbgSgwMfwdMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxMbgSgwMfwdNotifications_ObjectIdentity = ObjectIdentity
jnxMbgSgwMfwdNotifications = _JnxMbgSgwMfwdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7, 0)
)
_JnxMbgSgwMfwdNotificationVars_ObjectIdentity = ObjectIdentity
jnxMbgSgwMfwdNotificationVars = _JnxMbgSgwMfwdNotificationVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7, 1)
)


class _JnxMbgSgwMfwdServicePicName_Type(DisplayString):
    """Custom type jnxMbgSgwMfwdServicePicName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 15),
    )


_JnxMbgSgwMfwdServicePicName_Type.__name__ = "DisplayString"
_JnxMbgSgwMfwdServicePicName_Object = MibScalar
jnxMbgSgwMfwdServicePicName = _JnxMbgSgwMfwdServicePicName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7, 1, 1),
    _JnxMbgSgwMfwdServicePicName_Type()
)
jnxMbgSgwMfwdServicePicName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwMfwdServicePicName.setStatus("current")
_JnxMbgSgwMfwdBufMemLimit_Type = Gauge32
_JnxMbgSgwMfwdBufMemLimit_Object = MibScalar
jnxMbgSgwMfwdBufMemLimit = _JnxMbgSgwMfwdBufMemLimit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7, 1, 2),
    _JnxMbgSgwMfwdBufMemLimit_Type()
)
jnxMbgSgwMfwdBufMemLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwMfwdBufMemLimit.setStatus("current")
if mibBuilder.loadTexts:
    jnxMbgSgwMfwdBufMemLimit.setUnits("percent")

# Managed Objects groups


# Notification objects

jnxMbgSgwMfwdBufMemThresRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7, 0, 1)
)
jnxMbgSgwMfwdBufMemThresRaise.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILE-GW-SGW-MFWD-MIB", "jnxMbgSgwMfwdServicePicName"),
        ("JUNIPER-MOBILE-GW-SGW-MFWD-MIB", "jnxMbgSgwMfwdBufMemLimit"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwMfwdBufMemThresRaise.setStatus(
        "current"
    )

jnxMbgSgwMfwdBufMemThresClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7, 0, 2)
)
jnxMbgSgwMfwdBufMemThresClear.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILE-GW-SGW-MFWD-MIB", "jnxMbgSgwMfwdServicePicName"),
        ("JUNIPER-MOBILE-GW-SGW-MFWD-MIB", "jnxMbgSgwMfwdBufMemLimit"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwMfwdBufMemThresClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-MOBILE-GW-SGW-MFWD-MIB",
    **{"jnxMbgSgwMfwdMib": jnxMbgSgwMfwdMib,
       "jnxMbgSgwMfwdNotifications": jnxMbgSgwMfwdNotifications,
       "jnxMbgSgwMfwdBufMemThresRaise": jnxMbgSgwMfwdBufMemThresRaise,
       "jnxMbgSgwMfwdBufMemThresClear": jnxMbgSgwMfwdBufMemThresClear,
       "jnxMbgSgwMfwdNotificationVars": jnxMbgSgwMfwdNotificationVars,
       "jnxMbgSgwMfwdServicePicName": jnxMbgSgwMfwdServicePicName,
       "jnxMbgSgwMfwdBufMemLimit": jnxMbgSgwMfwdBufMemLimit}
)
