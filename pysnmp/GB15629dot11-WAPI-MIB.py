# SNMP MIB module (GB15629dot11-WAPI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GB15629dot11-WAPI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:42 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

gb15629dot11wapiMIB = ModuleIdentity(
    (1, 2, 156, 11235, 15629, 11, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Member_body_ObjectIdentity = ObjectIdentity
member_body = _Member_body_ObjectIdentity(
    (1, 2)
)
_Cn_ObjectIdentity = ObjectIdentity
cn = _Cn_ObjectIdentity(
    (1, 2, 156)
)
_Bwips_ObjectIdentity = ObjectIdentity
bwips = _Bwips_ObjectIdentity(
    (1, 2, 156, 11235)
)
_Gb15629_ObjectIdentity = ObjectIdentity
gb15629 = _Gb15629_ObjectIdentity(
    (1, 2, 156, 11235, 15629)
)
_Gb15629_11_ObjectIdentity = ObjectIdentity
gb15629_11 = _Gb15629_11_ObjectIdentity(
    (1, 2, 156, 11235, 15629, 11)
)
_Gb15629_11_mibs_ObjectIdentity = ObjectIdentity
gb15629_11_mibs = _Gb15629_11_mibs_ObjectIdentity(
    (1, 2, 156, 11235, 15629, 11, 1)
)
_WapiMIBObjects_ObjectIdentity = ObjectIdentity
wapiMIBObjects = _WapiMIBObjects_ObjectIdentity(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1)
)
_Gb15629dot11wapiConfigTable_Object = MibTable
gb15629dot11wapiConfigTable = _Gb15629dot11wapiConfigTable_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigTable.setStatus("current")
_Gb15629dot11wapiConfigEntry_Object = MibTableRow
gb15629dot11wapiConfigEntry = _Gb15629dot11wapiConfigEntry_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1)
)
gb15629dot11wapiConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigEntry.setStatus("current")
_Gb15629dot11wapiConfigVersion_Type = Integer32
_Gb15629dot11wapiConfigVersion_Object = MibTableColumn
gb15629dot11wapiConfigVersion = _Gb15629dot11wapiConfigVersion_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 1),
    _Gb15629dot11wapiConfigVersion_Type()
)
gb15629dot11wapiConfigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigVersion.setStatus("current")
_Gb15629dot11wapiControlledAuthControl_Type = TruthValue
_Gb15629dot11wapiControlledAuthControl_Object = MibTableColumn
gb15629dot11wapiControlledAuthControl = _Gb15629dot11wapiControlledAuthControl_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 2),
    _Gb15629dot11wapiControlledAuthControl_Type()
)
gb15629dot11wapiControlledAuthControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiControlledAuthControl.setStatus("current")
_Gb15629dot11wapiControlledPortControl_Type = Integer32
_Gb15629dot11wapiControlledPortControl_Object = MibTableColumn
gb15629dot11wapiControlledPortControl = _Gb15629dot11wapiControlledPortControl_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 3),
    _Gb15629dot11wapiControlledPortControl_Type()
)
gb15629dot11wapiControlledPortControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiControlledPortControl.setStatus("current")
_Gb15629dot11wapiOptionImplemented_Type = TruthValue
_Gb15629dot11wapiOptionImplemented_Object = MibTableColumn
gb15629dot11wapiOptionImplemented = _Gb15629dot11wapiOptionImplemented_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 4),
    _Gb15629dot11wapiOptionImplemented_Type()
)
gb15629dot11wapiOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiOptionImplemented.setStatus("current")
_Gb15629dot11wapiPreauthenticationImplemented_Type = TruthValue
_Gb15629dot11wapiPreauthenticationImplemented_Object = MibTableColumn
gb15629dot11wapiPreauthenticationImplemented = _Gb15629dot11wapiPreauthenticationImplemented_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 5),
    _Gb15629dot11wapiPreauthenticationImplemented_Type()
)
gb15629dot11wapiPreauthenticationImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiPreauthenticationImplemented.setStatus("current")
_Gb15629dot11wapiEnabled_Type = TruthValue
_Gb15629dot11wapiEnabled_Object = MibTableColumn
gb15629dot11wapiEnabled = _Gb15629dot11wapiEnabled_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 6),
    _Gb15629dot11wapiEnabled_Type()
)
gb15629dot11wapiEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gb15629dot11wapiEnabled.setStatus("current")
_Gb15629dot11wapiPreauthenticationEnabled_Type = TruthValue
_Gb15629dot11wapiPreauthenticationEnabled_Object = MibTableColumn
gb15629dot11wapiPreauthenticationEnabled = _Gb15629dot11wapiPreauthenticationEnabled_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 7),
    _Gb15629dot11wapiPreauthenticationEnabled_Type()
)
gb15629dot11wapiPreauthenticationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gb15629dot11wapiPreauthenticationEnabled.setStatus("current")
_Gb15629dot11wapiConfigUnicastKeysSupported_Type = Unsigned32
_Gb15629dot11wapiConfigUnicastKeysSupported_Object = MibTableColumn
gb15629dot11wapiConfigUnicastKeysSupported = _Gb15629dot11wapiConfigUnicastKeysSupported_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 8),
    _Gb15629dot11wapiConfigUnicastKeysSupported_Type()
)
gb15629dot11wapiConfigUnicastKeysSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigUnicastKeysSupported.setStatus("current")


class _Gb15629dot11wapiConfigUnicastRekeyMethod_Type(Integer32):
    """Custom type gb15629dot11wapiConfigUnicastRekeyMethod based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("packetBased", 3),
          ("timeBased", 2),
          ("timepacket-Based", 4))
    )


_Gb15629dot11wapiConfigUnicastRekeyMethod_Type.__name__ = "Integer32"
_Gb15629dot11wapiConfigUnicastRekeyMethod_Object = MibTableColumn
gb15629dot11wapiConfigUnicastRekeyMethod = _Gb15629dot11wapiConfigUnicastRekeyMethod_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 9),
    _Gb15629dot11wapiConfigUnicastRekeyMethod_Type()
)
gb15629dot11wapiConfigUnicastRekeyMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigUnicastRekeyMethod.setStatus("current")


class _Gb15629dot11wapiConfigUnicastRekeyTime_Type(Unsigned32):
    """Custom type gb15629dot11wapiConfigUnicastRekeyTime based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gb15629dot11wapiConfigUnicastRekeyTime_Type.__name__ = "Unsigned32"
_Gb15629dot11wapiConfigUnicastRekeyTime_Object = MibTableColumn
gb15629dot11wapiConfigUnicastRekeyTime = _Gb15629dot11wapiConfigUnicastRekeyTime_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 10),
    _Gb15629dot11wapiConfigUnicastRekeyTime_Type()
)
gb15629dot11wapiConfigUnicastRekeyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigUnicastRekeyTime.setStatus("current")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigUnicastRekeyTime.setUnits("seconds")


class _Gb15629dot11wapiConfigUnicastRekeyPackets_Type(Unsigned32):
    """Custom type gb15629dot11wapiConfigUnicastRekeyPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gb15629dot11wapiConfigUnicastRekeyPackets_Type.__name__ = "Unsigned32"
_Gb15629dot11wapiConfigUnicastRekeyPackets_Object = MibTableColumn
gb15629dot11wapiConfigUnicastRekeyPackets = _Gb15629dot11wapiConfigUnicastRekeyPackets_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 11),
    _Gb15629dot11wapiConfigUnicastRekeyPackets_Type()
)
gb15629dot11wapiConfigUnicastRekeyPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigUnicastRekeyPackets.setStatus("current")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigUnicastRekeyPackets.setUnits("1000 packets")


class _Gb15629dot11wapiConfigMulticastCipher_Type(OctetString):
    """Custom type gb15629dot11wapiConfigMulticastCipher based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Gb15629dot11wapiConfigMulticastCipher_Type.__name__ = "OctetString"
_Gb15629dot11wapiConfigMulticastCipher_Object = MibTableColumn
gb15629dot11wapiConfigMulticastCipher = _Gb15629dot11wapiConfigMulticastCipher_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 12),
    _Gb15629dot11wapiConfigMulticastCipher_Type()
)
gb15629dot11wapiConfigMulticastCipher.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigMulticastCipher.setStatus("current")


class _Gb15629dot11wapiConfigMulticastRekeyMethod_Type(Integer32):
    """Custom type gb15629dot11wapiConfigMulticastRekeyMethod based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("packetBased", 3),
          ("timeBased", 2),
          ("timepacket-Based", 4))
    )


_Gb15629dot11wapiConfigMulticastRekeyMethod_Type.__name__ = "Integer32"
_Gb15629dot11wapiConfigMulticastRekeyMethod_Object = MibTableColumn
gb15629dot11wapiConfigMulticastRekeyMethod = _Gb15629dot11wapiConfigMulticastRekeyMethod_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 13),
    _Gb15629dot11wapiConfigMulticastRekeyMethod_Type()
)
gb15629dot11wapiConfigMulticastRekeyMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigMulticastRekeyMethod.setStatus("current")


class _Gb15629dot11wapiConfigMulticastRekeyTime_Type(Unsigned32):
    """Custom type gb15629dot11wapiConfigMulticastRekeyTime based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gb15629dot11wapiConfigMulticastRekeyTime_Type.__name__ = "Unsigned32"
_Gb15629dot11wapiConfigMulticastRekeyTime_Object = MibTableColumn
gb15629dot11wapiConfigMulticastRekeyTime = _Gb15629dot11wapiConfigMulticastRekeyTime_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 14),
    _Gb15629dot11wapiConfigMulticastRekeyTime_Type()
)
gb15629dot11wapiConfigMulticastRekeyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigMulticastRekeyTime.setStatus("current")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigMulticastRekeyTime.setUnits("seconds")


class _Gb15629dot11wapiConfigMulticastRekeyPackets_Type(Unsigned32):
    """Custom type gb15629dot11wapiConfigMulticastRekeyPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gb15629dot11wapiConfigMulticastRekeyPackets_Type.__name__ = "Unsigned32"
_Gb15629dot11wapiConfigMulticastRekeyPackets_Object = MibTableColumn
gb15629dot11wapiConfigMulticastRekeyPackets = _Gb15629dot11wapiConfigMulticastRekeyPackets_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 15),
    _Gb15629dot11wapiConfigMulticastRekeyPackets_Type()
)
gb15629dot11wapiConfigMulticastRekeyPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigMulticastRekeyPackets.setStatus("current")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigMulticastRekeyPackets.setUnits("1000 packets")
_Gb15629dot11wapiConfigMulticastRekeyStrict_Type = TruthValue
_Gb15629dot11wapiConfigMulticastRekeyStrict_Object = MibTableColumn
gb15629dot11wapiConfigMulticastRekeyStrict = _Gb15629dot11wapiConfigMulticastRekeyStrict_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 16),
    _Gb15629dot11wapiConfigMulticastRekeyStrict_Type()
)
gb15629dot11wapiConfigMulticastRekeyStrict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigMulticastRekeyStrict.setStatus("current")


class _Gb15629dot11wapiConfigPSKValue_Type(OctetString):
    """Custom type gb15629dot11wapiConfigPSKValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_Gb15629dot11wapiConfigPSKValue_Type.__name__ = "OctetString"
_Gb15629dot11wapiConfigPSKValue_Object = MibTableColumn
gb15629dot11wapiConfigPSKValue = _Gb15629dot11wapiConfigPSKValue_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 17),
    _Gb15629dot11wapiConfigPSKValue_Type()
)
gb15629dot11wapiConfigPSKValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigPSKValue.setStatus("current")
_Gb15629dot11wapiConfigPSKPassPhrase_Type = DisplayString
_Gb15629dot11wapiConfigPSKPassPhrase_Object = MibTableColumn
gb15629dot11wapiConfigPSKPassPhrase = _Gb15629dot11wapiConfigPSKPassPhrase_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 18),
    _Gb15629dot11wapiConfigPSKPassPhrase_Type()
)
gb15629dot11wapiConfigPSKPassPhrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigPSKPassPhrase.setStatus("current")


class _Gb15629dot11wapiConfigCertificateUpdateCount_Type(Unsigned32):
    """Custom type gb15629dot11wapiConfigCertificateUpdateCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gb15629dot11wapiConfigCertificateUpdateCount_Type.__name__ = "Unsigned32"
_Gb15629dot11wapiConfigCertificateUpdateCount_Object = MibTableColumn
gb15629dot11wapiConfigCertificateUpdateCount = _Gb15629dot11wapiConfigCertificateUpdateCount_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 19),
    _Gb15629dot11wapiConfigCertificateUpdateCount_Type()
)
gb15629dot11wapiConfigCertificateUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigCertificateUpdateCount.setStatus("current")


class _Gb15629dot11wapiConfigMulticastUpdateCount_Type(Unsigned32):
    """Custom type gb15629dot11wapiConfigMulticastUpdateCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gb15629dot11wapiConfigMulticastUpdateCount_Type.__name__ = "Unsigned32"
_Gb15629dot11wapiConfigMulticastUpdateCount_Object = MibTableColumn
gb15629dot11wapiConfigMulticastUpdateCount = _Gb15629dot11wapiConfigMulticastUpdateCount_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 20),
    _Gb15629dot11wapiConfigMulticastUpdateCount_Type()
)
gb15629dot11wapiConfigMulticastUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigMulticastUpdateCount.setStatus("current")


class _Gb15629dot11wapiConfigUnicastUpdateCount_Type(Unsigned32):
    """Custom type gb15629dot11wapiConfigUnicastUpdateCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gb15629dot11wapiConfigUnicastUpdateCount_Type.__name__ = "Unsigned32"
_Gb15629dot11wapiConfigUnicastUpdateCount_Object = MibTableColumn
gb15629dot11wapiConfigUnicastUpdateCount = _Gb15629dot11wapiConfigUnicastUpdateCount_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 21),
    _Gb15629dot11wapiConfigUnicastUpdateCount_Type()
)
gb15629dot11wapiConfigUnicastUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigUnicastUpdateCount.setStatus("current")


class _Gb15629dot11wapiConfigMulticastCipherSize_Type(Unsigned32):
    """Custom type gb15629dot11wapiConfigMulticastCipherSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Gb15629dot11wapiConfigMulticastCipherSize_Type.__name__ = "Unsigned32"
_Gb15629dot11wapiConfigMulticastCipherSize_Object = MibTableColumn
gb15629dot11wapiConfigMulticastCipherSize = _Gb15629dot11wapiConfigMulticastCipherSize_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 22),
    _Gb15629dot11wapiConfigMulticastCipherSize_Type()
)
gb15629dot11wapiConfigMulticastCipherSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigMulticastCipherSize.setStatus("current")


class _Gb15629dot11wapiConfigBKLifetime_Type(Unsigned32):
    """Custom type gb15629dot11wapiConfigBKLifetime based on Unsigned32"""
    defaultValue = 43200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gb15629dot11wapiConfigBKLifetime_Type.__name__ = "Unsigned32"
_Gb15629dot11wapiConfigBKLifetime_Object = MibTableColumn
gb15629dot11wapiConfigBKLifetime = _Gb15629dot11wapiConfigBKLifetime_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 23),
    _Gb15629dot11wapiConfigBKLifetime_Type()
)
gb15629dot11wapiConfigBKLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigBKLifetime.setStatus("current")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigBKLifetime.setUnits("seconds")


class _Gb15629dot11wapiConfigBKReauthThreshold_Type(Unsigned32):
    """Custom type gb15629dot11wapiConfigBKReauthThreshold based on Unsigned32"""
    defaultValue = 70

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Gb15629dot11wapiConfigBKReauthThreshold_Type.__name__ = "Unsigned32"
_Gb15629dot11wapiConfigBKReauthThreshold_Object = MibTableColumn
gb15629dot11wapiConfigBKReauthThreshold = _Gb15629dot11wapiConfigBKReauthThreshold_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 24),
    _Gb15629dot11wapiConfigBKReauthThreshold_Type()
)
gb15629dot11wapiConfigBKReauthThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigBKReauthThreshold.setStatus("current")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigBKReauthThreshold.setUnits("percentage")


class _Gb15629dot11wapiConfigSATimeout_Type(Unsigned32):
    """Custom type gb15629dot11wapiConfigSATimeout based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gb15629dot11wapiConfigSATimeout_Type.__name__ = "Unsigned32"
_Gb15629dot11wapiConfigSATimeout_Object = MibTableColumn
gb15629dot11wapiConfigSATimeout = _Gb15629dot11wapiConfigSATimeout_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 25),
    _Gb15629dot11wapiConfigSATimeout_Type()
)
gb15629dot11wapiConfigSATimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigSATimeout.setStatus("current")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigSATimeout.setUnits("seconds")


class _Gb15629dot11wapiAuthenticationSuiteSelected_Type(OctetString):
    """Custom type gb15629dot11wapiAuthenticationSuiteSelected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Gb15629dot11wapiAuthenticationSuiteSelected_Type.__name__ = "OctetString"
_Gb15629dot11wapiAuthenticationSuiteSelected_Object = MibTableColumn
gb15629dot11wapiAuthenticationSuiteSelected = _Gb15629dot11wapiAuthenticationSuiteSelected_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 26),
    _Gb15629dot11wapiAuthenticationSuiteSelected_Type()
)
gb15629dot11wapiAuthenticationSuiteSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiAuthenticationSuiteSelected.setStatus("current")


class _Gb15629dot11wapiUnicastCipherSelected_Type(OctetString):
    """Custom type gb15629dot11wapiUnicastCipherSelected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Gb15629dot11wapiUnicastCipherSelected_Type.__name__ = "OctetString"
_Gb15629dot11wapiUnicastCipherSelected_Object = MibTableColumn
gb15629dot11wapiUnicastCipherSelected = _Gb15629dot11wapiUnicastCipherSelected_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 27),
    _Gb15629dot11wapiUnicastCipherSelected_Type()
)
gb15629dot11wapiUnicastCipherSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiUnicastCipherSelected.setStatus("current")


class _Gb15629dot11wapiMulticastCipherSelected_Type(OctetString):
    """Custom type gb15629dot11wapiMulticastCipherSelected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Gb15629dot11wapiMulticastCipherSelected_Type.__name__ = "OctetString"
_Gb15629dot11wapiMulticastCipherSelected_Object = MibTableColumn
gb15629dot11wapiMulticastCipherSelected = _Gb15629dot11wapiMulticastCipherSelected_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 28),
    _Gb15629dot11wapiMulticastCipherSelected_Type()
)
gb15629dot11wapiMulticastCipherSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiMulticastCipherSelected.setStatus("current")


class _Gb15629dot11wapiBKIDUsed_Type(OctetString):
    """Custom type gb15629dot11wapiBKIDUsed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Gb15629dot11wapiBKIDUsed_Type.__name__ = "OctetString"
_Gb15629dot11wapiBKIDUsed_Object = MibTableColumn
gb15629dot11wapiBKIDUsed = _Gb15629dot11wapiBKIDUsed_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 29),
    _Gb15629dot11wapiBKIDUsed_Type()
)
gb15629dot11wapiBKIDUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiBKIDUsed.setStatus("current")


class _Gb15629dot11wapiAuthenticationSuiteRequested_Type(OctetString):
    """Custom type gb15629dot11wapiAuthenticationSuiteRequested based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Gb15629dot11wapiAuthenticationSuiteRequested_Type.__name__ = "OctetString"
_Gb15629dot11wapiAuthenticationSuiteRequested_Object = MibTableColumn
gb15629dot11wapiAuthenticationSuiteRequested = _Gb15629dot11wapiAuthenticationSuiteRequested_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 30),
    _Gb15629dot11wapiAuthenticationSuiteRequested_Type()
)
gb15629dot11wapiAuthenticationSuiteRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiAuthenticationSuiteRequested.setStatus("current")


class _Gb15629dot11wapiUnicastCipherRequested_Type(OctetString):
    """Custom type gb15629dot11wapiUnicastCipherRequested based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Gb15629dot11wapiUnicastCipherRequested_Type.__name__ = "OctetString"
_Gb15629dot11wapiUnicastCipherRequested_Object = MibTableColumn
gb15629dot11wapiUnicastCipherRequested = _Gb15629dot11wapiUnicastCipherRequested_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 31),
    _Gb15629dot11wapiUnicastCipherRequested_Type()
)
gb15629dot11wapiUnicastCipherRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiUnicastCipherRequested.setStatus("current")


class _Gb15629dot11wapiMulticastCipherRequested_Type(OctetString):
    """Custom type gb15629dot11wapiMulticastCipherRequested based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Gb15629dot11wapiMulticastCipherRequested_Type.__name__ = "OctetString"
_Gb15629dot11wapiMulticastCipherRequested_Object = MibTableColumn
gb15629dot11wapiMulticastCipherRequested = _Gb15629dot11wapiMulticastCipherRequested_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 32),
    _Gb15629dot11wapiMulticastCipherRequested_Type()
)
gb15629dot11wapiMulticastCipherRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiMulticastCipherRequested.setStatus("current")
_Gb15629dot11wapiConfigUnicastCiphersTable_Object = MibTable
gb15629dot11wapiConfigUnicastCiphersTable = _Gb15629dot11wapiConfigUnicastCiphersTable_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigUnicastCiphersTable.setStatus("current")
_Gb15629dot11wapiConfigUnicastCiphersEntry_Object = MibTableRow
gb15629dot11wapiConfigUnicastCiphersEntry = _Gb15629dot11wapiConfigUnicastCiphersEntry_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 2, 1)
)
gb15629dot11wapiConfigUnicastCiphersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigUnicastCipherIndex"),
)
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigUnicastCiphersEntry.setStatus("current")


class _Gb15629dot11wapiConfigUnicastCipherIndex_Type(Unsigned32):
    """Custom type gb15629dot11wapiConfigUnicastCipherIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gb15629dot11wapiConfigUnicastCipherIndex_Type.__name__ = "Unsigned32"
_Gb15629dot11wapiConfigUnicastCipherIndex_Object = MibTableColumn
gb15629dot11wapiConfigUnicastCipherIndex = _Gb15629dot11wapiConfigUnicastCipherIndex_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 2, 1, 1),
    _Gb15629dot11wapiConfigUnicastCipherIndex_Type()
)
gb15629dot11wapiConfigUnicastCipherIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigUnicastCipherIndex.setStatus("current")


class _Gb15629dot11wapiConfigUnicastCipher_Type(OctetString):
    """Custom type gb15629dot11wapiConfigUnicastCipher based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Gb15629dot11wapiConfigUnicastCipher_Type.__name__ = "OctetString"
_Gb15629dot11wapiConfigUnicastCipher_Object = MibTableColumn
gb15629dot11wapiConfigUnicastCipher = _Gb15629dot11wapiConfigUnicastCipher_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 2, 1, 2),
    _Gb15629dot11wapiConfigUnicastCipher_Type()
)
gb15629dot11wapiConfigUnicastCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigUnicastCipher.setStatus("current")
_Gb15629dot11wapiConfigUnicastCipherEnabled_Type = TruthValue
_Gb15629dot11wapiConfigUnicastCipherEnabled_Object = MibTableColumn
gb15629dot11wapiConfigUnicastCipherEnabled = _Gb15629dot11wapiConfigUnicastCipherEnabled_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 2, 1, 3),
    _Gb15629dot11wapiConfigUnicastCipherEnabled_Type()
)
gb15629dot11wapiConfigUnicastCipherEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigUnicastCipherEnabled.setStatus("current")


class _Gb15629dot11wapiConfigUnicastCipherSize_Type(Unsigned32):
    """Custom type gb15629dot11wapiConfigUnicastCipherSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Gb15629dot11wapiConfigUnicastCipherSize_Type.__name__ = "Unsigned32"
_Gb15629dot11wapiConfigUnicastCipherSize_Object = MibTableColumn
gb15629dot11wapiConfigUnicastCipherSize = _Gb15629dot11wapiConfigUnicastCipherSize_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 2, 1, 4),
    _Gb15629dot11wapiConfigUnicastCipherSize_Type()
)
gb15629dot11wapiConfigUnicastCipherSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigUnicastCipherSize.setStatus("current")
_Gb15629dot11wapiConfigAuthenticationSuitesTable_Object = MibTable
gb15629dot11wapiConfigAuthenticationSuitesTable = _Gb15629dot11wapiConfigAuthenticationSuitesTable_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigAuthenticationSuitesTable.setStatus("current")
_Gb15629dot11wapiConfigAuthenticationSuitesEntry_Object = MibTableRow
gb15629dot11wapiConfigAuthenticationSuitesEntry = _Gb15629dot11wapiConfigAuthenticationSuitesEntry_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 3, 1)
)
gb15629dot11wapiConfigAuthenticationSuitesEntry.setIndexNames(
    (0, "GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigAuthenticationSuiteIndex"),
)
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigAuthenticationSuitesEntry.setStatus("current")


class _Gb15629dot11wapiConfigAuthenticationSuiteIndex_Type(Unsigned32):
    """Custom type gb15629dot11wapiConfigAuthenticationSuiteIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gb15629dot11wapiConfigAuthenticationSuiteIndex_Type.__name__ = "Unsigned32"
_Gb15629dot11wapiConfigAuthenticationSuiteIndex_Object = MibTableColumn
gb15629dot11wapiConfigAuthenticationSuiteIndex = _Gb15629dot11wapiConfigAuthenticationSuiteIndex_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 3, 1, 1),
    _Gb15629dot11wapiConfigAuthenticationSuiteIndex_Type()
)
gb15629dot11wapiConfigAuthenticationSuiteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigAuthenticationSuiteIndex.setStatus("current")


class _Gb15629dot11wapiConfigAuthenticationSuite_Type(OctetString):
    """Custom type gb15629dot11wapiConfigAuthenticationSuite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Gb15629dot11wapiConfigAuthenticationSuite_Type.__name__ = "OctetString"
_Gb15629dot11wapiConfigAuthenticationSuite_Object = MibTableColumn
gb15629dot11wapiConfigAuthenticationSuite = _Gb15629dot11wapiConfigAuthenticationSuite_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 3, 1, 2),
    _Gb15629dot11wapiConfigAuthenticationSuite_Type()
)
gb15629dot11wapiConfigAuthenticationSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigAuthenticationSuite.setStatus("current")
_Gb15629dot11wapiConfigAuthenticationSuiteEnabled_Type = TruthValue
_Gb15629dot11wapiConfigAuthenticationSuiteEnabled_Object = MibTableColumn
gb15629dot11wapiConfigAuthenticationSuiteEnabled = _Gb15629dot11wapiConfigAuthenticationSuiteEnabled_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 3, 1, 3),
    _Gb15629dot11wapiConfigAuthenticationSuiteEnabled_Type()
)
gb15629dot11wapiConfigAuthenticationSuiteEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gb15629dot11wapiConfigAuthenticationSuiteEnabled.setStatus("current")
_Gb15629dot11wapiStatsTable_Object = MibTable
gb15629dot11wapiStatsTable = _Gb15629dot11wapiStatsTable_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    gb15629dot11wapiStatsTable.setStatus("current")
_Gb15629dot11wapiStatsEntry_Object = MibTableRow
gb15629dot11wapiStatsEntry = _Gb15629dot11wapiStatsEntry_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1)
)
gb15629dot11wapiStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsIndex"),
)
if mibBuilder.loadTexts:
    gb15629dot11wapiStatsEntry.setStatus("current")


class _Gb15629dot11wapiStatsIndex_Type(Unsigned32):
    """Custom type gb15629dot11wapiStatsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gb15629dot11wapiStatsIndex_Type.__name__ = "Unsigned32"
_Gb15629dot11wapiStatsIndex_Object = MibTableColumn
gb15629dot11wapiStatsIndex = _Gb15629dot11wapiStatsIndex_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 1),
    _Gb15629dot11wapiStatsIndex_Type()
)
gb15629dot11wapiStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gb15629dot11wapiStatsIndex.setStatus("current")
_Gb15629dot11wapiStatsSTAAddress_Type = MacAddress
_Gb15629dot11wapiStatsSTAAddress_Object = MibTableColumn
gb15629dot11wapiStatsSTAAddress = _Gb15629dot11wapiStatsSTAAddress_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 2),
    _Gb15629dot11wapiStatsSTAAddress_Type()
)
gb15629dot11wapiStatsSTAAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiStatsSTAAddress.setStatus("current")


class _Gb15629dot11wapiStatsVersion_Type(Unsigned32):
    """Custom type gb15629dot11wapiStatsVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gb15629dot11wapiStatsVersion_Type.__name__ = "Unsigned32"
_Gb15629dot11wapiStatsVersion_Object = MibTableColumn
gb15629dot11wapiStatsVersion = _Gb15629dot11wapiStatsVersion_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 3),
    _Gb15629dot11wapiStatsVersion_Type()
)
gb15629dot11wapiStatsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiStatsVersion.setStatus("current")
_Gb15629dot11wapiStatsControlledPortStatus_Type = TruthValue
_Gb15629dot11wapiStatsControlledPortStatus_Object = MibTableColumn
gb15629dot11wapiStatsControlledPortStatus = _Gb15629dot11wapiStatsControlledPortStatus_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 4),
    _Gb15629dot11wapiStatsControlledPortStatus_Type()
)
gb15629dot11wapiStatsControlledPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiStatsControlledPortStatus.setStatus("current")


class _Gb15629dot11wapiStatsSelectedUnicastCipher_Type(OctetString):
    """Custom type gb15629dot11wapiStatsSelectedUnicastCipher based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Gb15629dot11wapiStatsSelectedUnicastCipher_Type.__name__ = "OctetString"
_Gb15629dot11wapiStatsSelectedUnicastCipher_Object = MibTableColumn
gb15629dot11wapiStatsSelectedUnicastCipher = _Gb15629dot11wapiStatsSelectedUnicastCipher_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 5),
    _Gb15629dot11wapiStatsSelectedUnicastCipher_Type()
)
gb15629dot11wapiStatsSelectedUnicastCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiStatsSelectedUnicastCipher.setStatus("current")
_Gb15629dot11wapiStatsWPIReplayCounters_Type = Counter32
_Gb15629dot11wapiStatsWPIReplayCounters_Object = MibTableColumn
gb15629dot11wapiStatsWPIReplayCounters = _Gb15629dot11wapiStatsWPIReplayCounters_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 6),
    _Gb15629dot11wapiStatsWPIReplayCounters_Type()
)
gb15629dot11wapiStatsWPIReplayCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiStatsWPIReplayCounters.setStatus("current")
_Gb15629dot11wapiStatsWPIDecryptableErrors_Type = Counter32
_Gb15629dot11wapiStatsWPIDecryptableErrors_Object = MibTableColumn
gb15629dot11wapiStatsWPIDecryptableErrors = _Gb15629dot11wapiStatsWPIDecryptableErrors_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 7),
    _Gb15629dot11wapiStatsWPIDecryptableErrors_Type()
)
gb15629dot11wapiStatsWPIDecryptableErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiStatsWPIDecryptableErrors.setStatus("current")
_Gb15629dot11wapiStatsWPIMICErrors_Type = Counter32
_Gb15629dot11wapiStatsWPIMICErrors_Object = MibTableColumn
gb15629dot11wapiStatsWPIMICErrors = _Gb15629dot11wapiStatsWPIMICErrors_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 8),
    _Gb15629dot11wapiStatsWPIMICErrors_Type()
)
gb15629dot11wapiStatsWPIMICErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiStatsWPIMICErrors.setStatus("current")
_Gb15629dot11wapiStatsWAISignatureErrors_Type = Counter32
_Gb15629dot11wapiStatsWAISignatureErrors_Object = MibTableColumn
gb15629dot11wapiStatsWAISignatureErrors = _Gb15629dot11wapiStatsWAISignatureErrors_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 9),
    _Gb15629dot11wapiStatsWAISignatureErrors_Type()
)
gb15629dot11wapiStatsWAISignatureErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiStatsWAISignatureErrors.setStatus("current")
_Gb15629dot11wapiStatsWAIHMACErrors_Type = Counter32
_Gb15629dot11wapiStatsWAIHMACErrors_Object = MibTableColumn
gb15629dot11wapiStatsWAIHMACErrors = _Gb15629dot11wapiStatsWAIHMACErrors_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 10),
    _Gb15629dot11wapiStatsWAIHMACErrors_Type()
)
gb15629dot11wapiStatsWAIHMACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiStatsWAIHMACErrors.setStatus("current")
_Gb15629dot11wapiStatsWAIAuthenticationResultFailures_Type = Counter32
_Gb15629dot11wapiStatsWAIAuthenticationResultFailures_Object = MibTableColumn
gb15629dot11wapiStatsWAIAuthenticationResultFailures = _Gb15629dot11wapiStatsWAIAuthenticationResultFailures_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 11),
    _Gb15629dot11wapiStatsWAIAuthenticationResultFailures_Type()
)
gb15629dot11wapiStatsWAIAuthenticationResultFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiStatsWAIAuthenticationResultFailures.setStatus("current")
_Gb15629dot11wapiStatsWAIDiscardCounters_Type = Counter32
_Gb15629dot11wapiStatsWAIDiscardCounters_Object = MibTableColumn
gb15629dot11wapiStatsWAIDiscardCounters = _Gb15629dot11wapiStatsWAIDiscardCounters_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 12),
    _Gb15629dot11wapiStatsWAIDiscardCounters_Type()
)
gb15629dot11wapiStatsWAIDiscardCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiStatsWAIDiscardCounters.setStatus("current")
_Gb15629dot11wapiStatsWAITimeoutCounters_Type = Counter32
_Gb15629dot11wapiStatsWAITimeoutCounters_Object = MibTableColumn
gb15629dot11wapiStatsWAITimeoutCounters = _Gb15629dot11wapiStatsWAITimeoutCounters_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 13),
    _Gb15629dot11wapiStatsWAITimeoutCounters_Type()
)
gb15629dot11wapiStatsWAITimeoutCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiStatsWAITimeoutCounters.setStatus("current")
_Gb15629dot11wapiStatsWAIFormatErrors_Type = Counter32
_Gb15629dot11wapiStatsWAIFormatErrors_Object = MibTableColumn
gb15629dot11wapiStatsWAIFormatErrors = _Gb15629dot11wapiStatsWAIFormatErrors_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 14),
    _Gb15629dot11wapiStatsWAIFormatErrors_Type()
)
gb15629dot11wapiStatsWAIFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiStatsWAIFormatErrors.setStatus("current")
_Gb15629dot11wapiStatsWAICertificateHandshakeFailures_Type = Counter32
_Gb15629dot11wapiStatsWAICertificateHandshakeFailures_Object = MibTableColumn
gb15629dot11wapiStatsWAICertificateHandshakeFailures = _Gb15629dot11wapiStatsWAICertificateHandshakeFailures_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 15),
    _Gb15629dot11wapiStatsWAICertificateHandshakeFailures_Type()
)
gb15629dot11wapiStatsWAICertificateHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiStatsWAICertificateHandshakeFailures.setStatus("current")
_Gb15629dot11wapiStatsWAIUnicastHandshakeFailures_Type = Counter32
_Gb15629dot11wapiStatsWAIUnicastHandshakeFailures_Object = MibTableColumn
gb15629dot11wapiStatsWAIUnicastHandshakeFailures = _Gb15629dot11wapiStatsWAIUnicastHandshakeFailures_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 16),
    _Gb15629dot11wapiStatsWAIUnicastHandshakeFailures_Type()
)
gb15629dot11wapiStatsWAIUnicastHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiStatsWAIUnicastHandshakeFailures.setStatus("current")
_Gb15629dot11wapiStatsWAIMulticastHandshakeFailures_Type = Counter32
_Gb15629dot11wapiStatsWAIMulticastHandshakeFailures_Object = MibTableColumn
gb15629dot11wapiStatsWAIMulticastHandshakeFailures = _Gb15629dot11wapiStatsWAIMulticastHandshakeFailures_Object(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 17),
    _Gb15629dot11wapiStatsWAIMulticastHandshakeFailures_Type()
)
gb15629dot11wapiStatsWAIMulticastHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gb15629dot11wapiStatsWAIMulticastHandshakeFailures.setStatus("current")
_WapiMIBConformance_ObjectIdentity = ObjectIdentity
wapiMIBConformance = _WapiMIBConformance_ObjectIdentity(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 2)
)
_Gb15629dot11wapiGroups_ObjectIdentity = ObjectIdentity
gb15629dot11wapiGroups = _Gb15629dot11wapiGroups_ObjectIdentity(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 2, 1)
)
_Gb15629wapiCompliances_ObjectIdentity = ObjectIdentity
gb15629wapiCompliances = _Gb15629wapiCompliances_ObjectIdentity(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 2, 2)
)

# Managed Objects groups

gb15629dot11wapiBase = ObjectGroup(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 2, 1, 1)
)
gb15629dot11wapiBase.setObjects(
      *(("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigVersion"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiControlledAuthControl"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiControlledPortControl"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiOptionImplemented"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiPreauthenticationImplemented"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiEnabled"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiPreauthenticationEnabled"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigUnicastKeysSupported"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigUnicastRekeyMethod"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigUnicastRekeyTime"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigUnicastRekeyPackets"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigMulticastCipher"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigMulticastRekeyMethod"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigMulticastRekeyTime"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigMulticastRekeyPackets"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigMulticastRekeyStrict"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigPSKValue"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigPSKPassPhrase"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigCertificateUpdateCount"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigMulticastUpdateCount"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigUnicastUpdateCount"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigMulticastCipherSize"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigUnicastCipher"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigUnicastCipherEnabled"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigUnicastCipherSize"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigAuthenticationSuite"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigAuthenticationSuiteEnabled"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigSATimeout"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiAuthenticationSuiteSelected"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiUnicastCipherSelected"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiMulticastCipherSelected"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiBKIDUsed"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiAuthenticationSuiteRequested"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiUnicastCipherRequested"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiMulticastCipherRequested"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsSTAAddress"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsVersion"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsControlledPortStatus"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsSelectedUnicastCipher"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsWPIReplayCounters"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsWPIDecryptableErrors"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsWPIMICErrors"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsWAISignatureErrors"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsWAIHMACErrors"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsWAIAuthenticationResultFailures"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsWAIDiscardCounters"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsWAITimeoutCounters"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsWAIFormatErrors"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsWAICertificateHandshakeFailures"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsWAIUnicastHandshakeFailures"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsWAIMulticastHandshakeFailures"))
)
if mibBuilder.loadTexts:
    gb15629dot11wapiBase.setStatus("current")

gb15629dot11wapiBKcachingGroup = ObjectGroup(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 2, 1, 2)
)
gb15629dot11wapiBKcachingGroup.setObjects(
      *(("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigBKLifetime"),
        ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigBKReauthThreshold"))
)
if mibBuilder.loadTexts:
    gb15629dot11wapiBKcachingGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

gb15629dot11wapiCompliance = ModuleCompliance(
    (1, 2, 156, 11235, 15629, 11, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    gb15629dot11wapiCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GB15629dot11-WAPI-MIB",
    **{"member-body": member_body,
       "cn": cn,
       "bwips": bwips,
       "gb15629": gb15629,
       "gb15629-11": gb15629_11,
       "gb15629-11-mibs": gb15629_11_mibs,
       "gb15629dot11wapiMIB": gb15629dot11wapiMIB,
       "wapiMIBObjects": wapiMIBObjects,
       "gb15629dot11wapiConfigTable": gb15629dot11wapiConfigTable,
       "gb15629dot11wapiConfigEntry": gb15629dot11wapiConfigEntry,
       "gb15629dot11wapiConfigVersion": gb15629dot11wapiConfigVersion,
       "gb15629dot11wapiControlledAuthControl": gb15629dot11wapiControlledAuthControl,
       "gb15629dot11wapiControlledPortControl": gb15629dot11wapiControlledPortControl,
       "gb15629dot11wapiOptionImplemented": gb15629dot11wapiOptionImplemented,
       "gb15629dot11wapiPreauthenticationImplemented": gb15629dot11wapiPreauthenticationImplemented,
       "gb15629dot11wapiEnabled": gb15629dot11wapiEnabled,
       "gb15629dot11wapiPreauthenticationEnabled": gb15629dot11wapiPreauthenticationEnabled,
       "gb15629dot11wapiConfigUnicastKeysSupported": gb15629dot11wapiConfigUnicastKeysSupported,
       "gb15629dot11wapiConfigUnicastRekeyMethod": gb15629dot11wapiConfigUnicastRekeyMethod,
       "gb15629dot11wapiConfigUnicastRekeyTime": gb15629dot11wapiConfigUnicastRekeyTime,
       "gb15629dot11wapiConfigUnicastRekeyPackets": gb15629dot11wapiConfigUnicastRekeyPackets,
       "gb15629dot11wapiConfigMulticastCipher": gb15629dot11wapiConfigMulticastCipher,
       "gb15629dot11wapiConfigMulticastRekeyMethod": gb15629dot11wapiConfigMulticastRekeyMethod,
       "gb15629dot11wapiConfigMulticastRekeyTime": gb15629dot11wapiConfigMulticastRekeyTime,
       "gb15629dot11wapiConfigMulticastRekeyPackets": gb15629dot11wapiConfigMulticastRekeyPackets,
       "gb15629dot11wapiConfigMulticastRekeyStrict": gb15629dot11wapiConfigMulticastRekeyStrict,
       "gb15629dot11wapiConfigPSKValue": gb15629dot11wapiConfigPSKValue,
       "gb15629dot11wapiConfigPSKPassPhrase": gb15629dot11wapiConfigPSKPassPhrase,
       "gb15629dot11wapiConfigCertificateUpdateCount": gb15629dot11wapiConfigCertificateUpdateCount,
       "gb15629dot11wapiConfigMulticastUpdateCount": gb15629dot11wapiConfigMulticastUpdateCount,
       "gb15629dot11wapiConfigUnicastUpdateCount": gb15629dot11wapiConfigUnicastUpdateCount,
       "gb15629dot11wapiConfigMulticastCipherSize": gb15629dot11wapiConfigMulticastCipherSize,
       "gb15629dot11wapiConfigBKLifetime": gb15629dot11wapiConfigBKLifetime,
       "gb15629dot11wapiConfigBKReauthThreshold": gb15629dot11wapiConfigBKReauthThreshold,
       "gb15629dot11wapiConfigSATimeout": gb15629dot11wapiConfigSATimeout,
       "gb15629dot11wapiAuthenticationSuiteSelected": gb15629dot11wapiAuthenticationSuiteSelected,
       "gb15629dot11wapiUnicastCipherSelected": gb15629dot11wapiUnicastCipherSelected,
       "gb15629dot11wapiMulticastCipherSelected": gb15629dot11wapiMulticastCipherSelected,
       "gb15629dot11wapiBKIDUsed": gb15629dot11wapiBKIDUsed,
       "gb15629dot11wapiAuthenticationSuiteRequested": gb15629dot11wapiAuthenticationSuiteRequested,
       "gb15629dot11wapiUnicastCipherRequested": gb15629dot11wapiUnicastCipherRequested,
       "gb15629dot11wapiMulticastCipherRequested": gb15629dot11wapiMulticastCipherRequested,
       "gb15629dot11wapiConfigUnicastCiphersTable": gb15629dot11wapiConfigUnicastCiphersTable,
       "gb15629dot11wapiConfigUnicastCiphersEntry": gb15629dot11wapiConfigUnicastCiphersEntry,
       "gb15629dot11wapiConfigUnicastCipherIndex": gb15629dot11wapiConfigUnicastCipherIndex,
       "gb15629dot11wapiConfigUnicastCipher": gb15629dot11wapiConfigUnicastCipher,
       "gb15629dot11wapiConfigUnicastCipherEnabled": gb15629dot11wapiConfigUnicastCipherEnabled,
       "gb15629dot11wapiConfigUnicastCipherSize": gb15629dot11wapiConfigUnicastCipherSize,
       "gb15629dot11wapiConfigAuthenticationSuitesTable": gb15629dot11wapiConfigAuthenticationSuitesTable,
       "gb15629dot11wapiConfigAuthenticationSuitesEntry": gb15629dot11wapiConfigAuthenticationSuitesEntry,
       "gb15629dot11wapiConfigAuthenticationSuiteIndex": gb15629dot11wapiConfigAuthenticationSuiteIndex,
       "gb15629dot11wapiConfigAuthenticationSuite": gb15629dot11wapiConfigAuthenticationSuite,
       "gb15629dot11wapiConfigAuthenticationSuiteEnabled": gb15629dot11wapiConfigAuthenticationSuiteEnabled,
       "gb15629dot11wapiStatsTable": gb15629dot11wapiStatsTable,
       "gb15629dot11wapiStatsEntry": gb15629dot11wapiStatsEntry,
       "gb15629dot11wapiStatsIndex": gb15629dot11wapiStatsIndex,
       "gb15629dot11wapiStatsSTAAddress": gb15629dot11wapiStatsSTAAddress,
       "gb15629dot11wapiStatsVersion": gb15629dot11wapiStatsVersion,
       "gb15629dot11wapiStatsControlledPortStatus": gb15629dot11wapiStatsControlledPortStatus,
       "gb15629dot11wapiStatsSelectedUnicastCipher": gb15629dot11wapiStatsSelectedUnicastCipher,
       "gb15629dot11wapiStatsWPIReplayCounters": gb15629dot11wapiStatsWPIReplayCounters,
       "gb15629dot11wapiStatsWPIDecryptableErrors": gb15629dot11wapiStatsWPIDecryptableErrors,
       "gb15629dot11wapiStatsWPIMICErrors": gb15629dot11wapiStatsWPIMICErrors,
       "gb15629dot11wapiStatsWAISignatureErrors": gb15629dot11wapiStatsWAISignatureErrors,
       "gb15629dot11wapiStatsWAIHMACErrors": gb15629dot11wapiStatsWAIHMACErrors,
       "gb15629dot11wapiStatsWAIAuthenticationResultFailures": gb15629dot11wapiStatsWAIAuthenticationResultFailures,
       "gb15629dot11wapiStatsWAIDiscardCounters": gb15629dot11wapiStatsWAIDiscardCounters,
       "gb15629dot11wapiStatsWAITimeoutCounters": gb15629dot11wapiStatsWAITimeoutCounters,
       "gb15629dot11wapiStatsWAIFormatErrors": gb15629dot11wapiStatsWAIFormatErrors,
       "gb15629dot11wapiStatsWAICertificateHandshakeFailures": gb15629dot11wapiStatsWAICertificateHandshakeFailures,
       "gb15629dot11wapiStatsWAIUnicastHandshakeFailures": gb15629dot11wapiStatsWAIUnicastHandshakeFailures,
       "gb15629dot11wapiStatsWAIMulticastHandshakeFailures": gb15629dot11wapiStatsWAIMulticastHandshakeFailures,
       "wapiMIBConformance": wapiMIBConformance,
       "gb15629dot11wapiGroups": gb15629dot11wapiGroups,
       "gb15629dot11wapiBase": gb15629dot11wapiBase,
       "gb15629dot11wapiBKcachingGroup": gb15629dot11wapiBKcachingGroup,
       "gb15629wapiCompliances": gb15629wapiCompliances,
       "gb15629dot11wapiCompliance": gb15629dot11wapiCompliance}
)
