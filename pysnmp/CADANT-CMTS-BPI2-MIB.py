# SNMP MIB module (CADANT-CMTS-BPI2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-CMTS-BPI2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:23 2024
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

(cadSystem,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadSystem")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cadBpi2Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 5)
)
cadBpi2Mib.setRevisions(
        ("2014-07-30 00:00",
         "2006-12-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CadBpi2CmtsBaseTable_Object = MibTable
cadBpi2CmtsBaseTable = _CadBpi2CmtsBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 5, 1)
)
if mibBuilder.loadTexts:
    cadBpi2CmtsBaseTable.setStatus("current")
_CadBpi2CmtsBaseEntry_Object = MibTableRow
cadBpi2CmtsBaseEntry = _CadBpi2CmtsBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 5, 1, 1)
)
cadBpi2CmtsBaseEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cadBpi2CmtsBaseEntry.setStatus("current")


class _CadBpi2CmtsDefaultAuthLifetime_Type(Integer32):
    """Custom type cadBpi2CmtsDefaultAuthLifetime based on Integer32"""
    defaultValue = 604800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6048000),
    )


_CadBpi2CmtsDefaultAuthLifetime_Type.__name__ = "Integer32"
_CadBpi2CmtsDefaultAuthLifetime_Object = MibTableColumn
cadBpi2CmtsDefaultAuthLifetime = _CadBpi2CmtsDefaultAuthLifetime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 5, 1, 1, 1),
    _CadBpi2CmtsDefaultAuthLifetime_Type()
)
cadBpi2CmtsDefaultAuthLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadBpi2CmtsDefaultAuthLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cadBpi2CmtsDefaultAuthLifetime.setUnits("seconds")


class _CadBpi2CmtsDefaultTEKLifetime_Type(Integer32):
    """Custom type cadBpi2CmtsDefaultTEKLifetime based on Integer32"""
    defaultValue = 43200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_CadBpi2CmtsDefaultTEKLifetime_Type.__name__ = "Integer32"
_CadBpi2CmtsDefaultTEKLifetime_Object = MibTableColumn
cadBpi2CmtsDefaultTEKLifetime = _CadBpi2CmtsDefaultTEKLifetime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 5, 1, 1, 2),
    _CadBpi2CmtsDefaultTEKLifetime_Type()
)
cadBpi2CmtsDefaultTEKLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadBpi2CmtsDefaultTEKLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cadBpi2CmtsDefaultTEKLifetime.setUnits("seconds")


class _CadBpi2CmtsDefaultSelfSignedManufCertTrust_Type(Integer32):
    """Custom type cadBpi2CmtsDefaultSelfSignedManufCertTrust based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trusted", 1),
          ("untrusted", 2))
    )


_CadBpi2CmtsDefaultSelfSignedManufCertTrust_Type.__name__ = "Integer32"
_CadBpi2CmtsDefaultSelfSignedManufCertTrust_Object = MibTableColumn
cadBpi2CmtsDefaultSelfSignedManufCertTrust = _CadBpi2CmtsDefaultSelfSignedManufCertTrust_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 5, 1, 1, 3),
    _CadBpi2CmtsDefaultSelfSignedManufCertTrust_Type()
)
cadBpi2CmtsDefaultSelfSignedManufCertTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadBpi2CmtsDefaultSelfSignedManufCertTrust.setStatus("current")


class _CadBpi2CmtsCheckCertValidityPeriods_Type(TruthValue):
    """Custom type cadBpi2CmtsCheckCertValidityPeriods based on TruthValue"""


_CadBpi2CmtsCheckCertValidityPeriods_Object = MibTableColumn
cadBpi2CmtsCheckCertValidityPeriods = _CadBpi2CmtsCheckCertValidityPeriods_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 5, 1, 1, 4),
    _CadBpi2CmtsCheckCertValidityPeriods_Type()
)
cadBpi2CmtsCheckCertValidityPeriods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadBpi2CmtsCheckCertValidityPeriods.setStatus("current")
_CadBpi2CmtsConfig_ObjectIdentity = ObjectIdentity
cadBpi2CmtsConfig = _CadBpi2CmtsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 5, 2)
)


class _CadBpi2CmtsAES128Enable_Type(TruthValue):
    """Custom type cadBpi2CmtsAES128Enable based on TruthValue"""


_CadBpi2CmtsAES128Enable_Object = MibScalar
cadBpi2CmtsAES128Enable = _CadBpi2CmtsAES128Enable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 5, 2, 1),
    _CadBpi2CmtsAES128Enable_Type()
)
cadBpi2CmtsAES128Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadBpi2CmtsAES128Enable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-CMTS-BPI2-MIB",
    **{"cadBpi2Mib": cadBpi2Mib,
       "cadBpi2CmtsBaseTable": cadBpi2CmtsBaseTable,
       "cadBpi2CmtsBaseEntry": cadBpi2CmtsBaseEntry,
       "cadBpi2CmtsDefaultAuthLifetime": cadBpi2CmtsDefaultAuthLifetime,
       "cadBpi2CmtsDefaultTEKLifetime": cadBpi2CmtsDefaultTEKLifetime,
       "cadBpi2CmtsDefaultSelfSignedManufCertTrust": cadBpi2CmtsDefaultSelfSignedManufCertTrust,
       "cadBpi2CmtsCheckCertValidityPeriods": cadBpi2CmtsCheckCertValidityPeriods,
       "cadBpi2CmtsConfig": cadBpi2CmtsConfig,
       "cadBpi2CmtsAES128Enable": cadBpi2CmtsAES128Enable}
)
