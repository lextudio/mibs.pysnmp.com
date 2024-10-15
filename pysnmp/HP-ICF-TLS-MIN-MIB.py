# SNMP MIB module (HP-ICF-TLS-MIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-TLS-MIN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:18 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfTlsMinMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112)
)
hpicfTlsMinMIB.setRevisions(
        ("2017-05-11 09:00",
         "2017-04-05 09:00",
         "2016-06-22 09:00",
         "2014-10-01 09:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfTlsMinObjects_ObjectIdentity = ObjectIdentity
hpicfTlsMinObjects = _HpicfTlsMinObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0)
)
_HpicfTlsMinConfigObjects_ObjectIdentity = ObjectIdentity
hpicfTlsMinConfigObjects = _HpicfTlsMinConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1)
)
_HpicfTlsMinTable_Object = MibTable
hpicfTlsMinTable = _HpicfTlsMinTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfTlsMinTable.setStatus("current")
_HpicfTlsMinEntry_Object = MibTableRow
hpicfTlsMinEntry = _HpicfTlsMinEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1)
)
hpicfTlsMinEntry.setIndexNames(
    (0, "HP-ICF-TLS-MIN-MIB", "hpicfTlsMinApp"),
)
if mibBuilder.loadTexts:
    hpicfTlsMinEntry.setStatus("current")


class _HpicfTlsMinApp_Type(Integer32):
    """Custom type hpicfTlsMinApp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cloud", 5),
          ("openflow", 2),
          ("syslog", 3),
          ("tr69", 4),
          ("webSsl", 1))
    )


_HpicfTlsMinApp_Type.__name__ = "Integer32"
_HpicfTlsMinApp_Object = MibTableColumn
hpicfTlsMinApp = _HpicfTlsMinApp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1, 1),
    _HpicfTlsMinApp_Type()
)
hpicfTlsMinApp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfTlsMinApp.setStatus("current")


class _HpicfTlsMinVersion_Type(Integer32):
    """Custom type hpicfTlsMinVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tls1dot0", 1),
          ("tls1dot1", 2),
          ("tls1dot2", 3))
    )


_HpicfTlsMinVersion_Type.__name__ = "Integer32"
_HpicfTlsMinVersion_Object = MibTableColumn
hpicfTlsMinVersion = _HpicfTlsMinVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1, 2),
    _HpicfTlsMinVersion_Type()
)
hpicfTlsMinVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTlsMinVersion.setStatus("current")
_HpicfTlsMinCloseSSLSess_Type = TruthValue
_HpicfTlsMinCloseSSLSess_Object = MibTableColumn
hpicfTlsMinCloseSSLSess = _HpicfTlsMinCloseSSLSess_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1, 3),
    _HpicfTlsMinCloseSSLSess_Type()
)
hpicfTlsMinCloseSSLSess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTlsMinCloseSSLSess.setStatus("current")
_HpicfTlsMinRowStatus_Type = RowStatus
_HpicfTlsMinRowStatus_Object = MibTableColumn
hpicfTlsMinRowStatus = _HpicfTlsMinRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1, 4),
    _HpicfTlsMinRowStatus_Type()
)
hpicfTlsMinRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTlsMinRowStatus.setStatus("current")
_HpicfTlsMinCipherTable_Object = MibTable
hpicfTlsMinCipherTable = _HpicfTlsMinCipherTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfTlsMinCipherTable.setStatus("current")
_HpicfTlsMinCipherEntry_Object = MibTableRow
hpicfTlsMinCipherEntry = _HpicfTlsMinCipherEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 2, 1)
)
hpicfTlsMinCipherEntry.setIndexNames(
    (0, "HP-ICF-TLS-MIN-MIB", "hpicfTlsMinApp"),
    (0, "HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipher"),
)
if mibBuilder.loadTexts:
    hpicfTlsMinCipherEntry.setStatus("current")


class _HpicfTlsMinCipher_Type(Integer32):
    """Custom type hpicfTlsMinCipher based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("aes128GcmSha256", 7),
          ("aes128Sha", 4),
          ("aes128Sha256", 3),
          ("aes256GcmSha384", 6),
          ("aes256Sha", 2),
          ("aes256Sha256", 1),
          ("all", 36),
          ("des3CbcSha", 5),
          ("ecdhEcdsaAes128GcmSha256", 10),
          ("ecdhEcdsaAes128Sha", 18),
          ("ecdhEcdsaAes128Sha256", 16),
          ("ecdhEcdsaAes256GcmSha384", 8),
          ("ecdhEcdsaAes256Sha", 14),
          ("ecdhEcdsaAes256Sha384", 12),
          ("ecdhEcdsaDesCbc3Sha", 20),
          ("ecdhRsaAaes256GcmSha384", 9),
          ("ecdhRsaAes128GcmSha256", 11),
          ("ecdhRsaAes128Sha", 19),
          ("ecdhRsaAes128Sha256", 17),
          ("ecdhRsaAes256Sha", 15),
          ("ecdhRsaAes256Sha384", 13),
          ("ecdhRsaDesCbc3Sha", 21),
          ("ecdheEcdsaAes128GcmSha256", 22),
          ("ecdheEcdsaAes128Sha", 26),
          ("ecdheEcdsaAes128Sha256", 24),
          ("ecdheEcdsaAes256GcmSha384", 28),
          ("ecdheEcdsaAes256Sha", 32),
          ("ecdheEcdsaAes256Sha384", 30),
          ("ecdheEcdsaDesCbc3Sha", 34),
          ("ecdheRsaAes128GcmSha256", 23),
          ("ecdheRsaAes128Sha", 27),
          ("ecdheRsaAes128Sha256", 25),
          ("ecdheRsaAes256GcmSha384", 29),
          ("ecdheRsaAes256Sha", 33),
          ("ecdheRsaAes256Sha384", 31),
          ("ecdheRsaDesCbc3Sha", 35))
    )


_HpicfTlsMinCipher_Type.__name__ = "Integer32"
_HpicfTlsMinCipher_Object = MibTableColumn
hpicfTlsMinCipher = _HpicfTlsMinCipher_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 2, 1, 1),
    _HpicfTlsMinCipher_Type()
)
hpicfTlsMinCipher.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfTlsMinCipher.setStatus("current")
_HpicfTlsMinCipherRowStatus_Type = RowStatus
_HpicfTlsMinCipherRowStatus_Object = MibTableColumn
hpicfTlsMinCipherRowStatus = _HpicfTlsMinCipherRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 2, 1, 2),
    _HpicfTlsMinCipherRowStatus_Type()
)
hpicfTlsMinCipherRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTlsMinCipherRowStatus.setStatus("current")


class _HpicfTlsMinCipherConfig_Type(Integer32):
    """Custom type hpicfTlsMinCipherConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enforce", 1))
    )


_HpicfTlsMinCipherConfig_Type.__name__ = "Integer32"
_HpicfTlsMinCipherConfig_Object = MibTableColumn
hpicfTlsMinCipherConfig = _HpicfTlsMinCipherConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 2, 1, 3),
    _HpicfTlsMinCipherConfig_Type()
)
hpicfTlsMinCipherConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTlsMinCipherConfig.setStatus("current")
_HpicfTlsMinConformance_ObjectIdentity = ObjectIdentity
hpicfTlsMinConformance = _HpicfTlsMinConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1)
)
_HpicfTlsMinCompliances_ObjectIdentity = ObjectIdentity
hpicfTlsMinCompliances = _HpicfTlsMinCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 1)
)
_HpicfTlsMinGroups_ObjectIdentity = ObjectIdentity
hpicfTlsMinGroups = _HpicfTlsMinGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 2)
)

# Managed Objects groups

hpicfTlsMinConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 2, 1)
)
hpicfTlsMinConfigGroup.setObjects(
      *(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinVersion"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCloseSSLSess"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinRowStatus"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfTlsMinConfigGroup.setStatus("deprecated")

hpicfTlsMinConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 2, 2)
)
hpicfTlsMinConfigGroup1.setObjects(
      *(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinVersion"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCloseSSLSess"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinRowStatus"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherRowStatus"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherConfig"))
)
if mibBuilder.loadTexts:
    hpicfTlsMinConfigGroup1.setStatus("deprecated")

hpicfTlsMinConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 2, 3)
)
hpicfTlsMinConfigGroup2.setObjects(
      *(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinVersion"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCloseSSLSess"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinRowStatus"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherRowStatus"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherConfig"))
)
if mibBuilder.loadTexts:
    hpicfTlsMinConfigGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfTlsMinCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfTlsMinCompliance1.setStatus(
        "deprecated"
    )

hpicfTlsMinCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfTlsMinCompliance2.setStatus(
        "deprecated"
    )

hpicfTlsMinCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfTlsMinCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-TLS-MIN-MIB",
    **{"hpicfTlsMinMIB": hpicfTlsMinMIB,
       "hpicfTlsMinObjects": hpicfTlsMinObjects,
       "hpicfTlsMinConfigObjects": hpicfTlsMinConfigObjects,
       "hpicfTlsMinTable": hpicfTlsMinTable,
       "hpicfTlsMinEntry": hpicfTlsMinEntry,
       "hpicfTlsMinApp": hpicfTlsMinApp,
       "hpicfTlsMinVersion": hpicfTlsMinVersion,
       "hpicfTlsMinCloseSSLSess": hpicfTlsMinCloseSSLSess,
       "hpicfTlsMinRowStatus": hpicfTlsMinRowStatus,
       "hpicfTlsMinCipherTable": hpicfTlsMinCipherTable,
       "hpicfTlsMinCipherEntry": hpicfTlsMinCipherEntry,
       "hpicfTlsMinCipher": hpicfTlsMinCipher,
       "hpicfTlsMinCipherRowStatus": hpicfTlsMinCipherRowStatus,
       "hpicfTlsMinCipherConfig": hpicfTlsMinCipherConfig,
       "hpicfTlsMinConformance": hpicfTlsMinConformance,
       "hpicfTlsMinCompliances": hpicfTlsMinCompliances,
       "hpicfTlsMinCompliance1": hpicfTlsMinCompliance1,
       "hpicfTlsMinCompliance2": hpicfTlsMinCompliance2,
       "hpicfTlsMinCompliance3": hpicfTlsMinCompliance3,
       "hpicfTlsMinGroups": hpicfTlsMinGroups,
       "hpicfTlsMinConfigGroup": hpicfTlsMinConfigGroup,
       "hpicfTlsMinConfigGroup1": hpicfTlsMinConfigGroup1,
       "hpicfTlsMinConfigGroup2": hpicfTlsMinConfigGroup2}
)
