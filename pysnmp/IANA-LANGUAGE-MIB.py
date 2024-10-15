# SNMP MIB module (IANA-LANGUAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IANA-LANGUAGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:04 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ianaLanguages = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 73)
)
ianaLanguages.setRevisions(
        ("2014-05-22 00:00",
         "2000-05-10 00:00",
         "1999-09-09 09:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IanaLangJavaByteCode_ObjectIdentity = ObjectIdentity
ianaLangJavaByteCode = _IanaLangJavaByteCode_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 73, 1)
)
if mibBuilder.loadTexts:
    ianaLangJavaByteCode.setStatus("current")
_IanaLangTcl_ObjectIdentity = ObjectIdentity
ianaLangTcl = _IanaLangTcl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 73, 2)
)
if mibBuilder.loadTexts:
    ianaLangTcl.setStatus("current")
_IanaLangPerl_ObjectIdentity = ObjectIdentity
ianaLangPerl = _IanaLangPerl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 73, 3)
)
if mibBuilder.loadTexts:
    ianaLangPerl.setStatus("current")
_IanaLangScheme_ObjectIdentity = ObjectIdentity
ianaLangScheme = _IanaLangScheme_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 73, 4)
)
if mibBuilder.loadTexts:
    ianaLangScheme.setStatus("current")
_IanaLangSRSL_ObjectIdentity = ObjectIdentity
ianaLangSRSL = _IanaLangSRSL_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 73, 5)
)
if mibBuilder.loadTexts:
    ianaLangSRSL.setStatus("current")
_IanaLangPSL_ObjectIdentity = ObjectIdentity
ianaLangPSL = _IanaLangPSL_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 73, 6)
)
if mibBuilder.loadTexts:
    ianaLangPSL.setStatus("current")
_IanaLangSMSL_ObjectIdentity = ObjectIdentity
ianaLangSMSL = _IanaLangSMSL_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 73, 7)
)
if mibBuilder.loadTexts:
    ianaLangSMSL.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IANA-LANGUAGE-MIB",
    **{"ianaLanguages": ianaLanguages,
       "ianaLangJavaByteCode": ianaLangJavaByteCode,
       "ianaLangTcl": ianaLangTcl,
       "ianaLangPerl": ianaLangPerl,
       "ianaLangScheme": ianaLangScheme,
       "ianaLangSRSL": ianaLangSRSL,
       "ianaLangPSL": ianaLangPSL,
       "ianaLangSMSL": ianaLangSMSL}
)
