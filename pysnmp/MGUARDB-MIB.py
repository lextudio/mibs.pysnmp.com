# SNMP MIB module (MGUARDB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MGUARDB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:24 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Innominate_ObjectIdentity = ObjectIdentity
innominate = _Innominate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450)
)
_MGuardb_ObjectIdentity = ObjectIdentity
mGuardb = _MGuardb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2)
)
_MGuardVPN_ObjectIdentity = ObjectIdentity
mGuardVPN = _MGuardVPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1)
)
_MGuardVPNMachine_ObjectIdentity = ObjectIdentity
mGuardVPNMachine = _MGuardVPNMachine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 1)
)
_MGuardVPNMachineCert_Type = DisplayString
_MGuardVPNMachineCert_Object = MibScalar
mGuardVPNMachineCert = _MGuardVPNMachineCert_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 1, 1),
    _MGuardVPNMachineCert_Type()
)
mGuardVPNMachineCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNMachineCert.setStatus("mandatory")
_MGuardVPNMachinePrivate_Type = DisplayString
_MGuardVPNMachinePrivate_Object = MibScalar
mGuardVPNMachinePrivate = _MGuardVPNMachinePrivate_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 1, 2),
    _MGuardVPNMachinePrivate_Type()
)
mGuardVPNMachinePrivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNMachinePrivate.setStatus("mandatory")
_MGuardVPNConnectionTable_Object = MibTable
mGuardVPNConnectionTable = _MGuardVPNConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2)
)
if mibBuilder.loadTexts:
    mGuardVPNConnectionTable.setStatus("mandatory")
_MGuardVPNConnectionEntry_Object = MibTableRow
mGuardVPNConnectionEntry = _MGuardVPNConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1)
)
mGuardVPNConnectionEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardVPNconIndex"),
)
if mibBuilder.loadTexts:
    mGuardVPNConnectionEntry.setStatus("mandatory")


class _MGuardVPNconIndex_Type(Integer32):
    """Custom type mGuardVPNconIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_MGuardVPNconIndex_Type.__name__ = "Integer32"
_MGuardVPNconIndex_Object = MibTableColumn
mGuardVPNconIndex = _MGuardVPNconIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 1),
    _MGuardVPNconIndex_Type()
)
mGuardVPNconIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardVPNconIndex.setStatus("mandatory")
_MGuardVPNconName_Type = DisplayString
_MGuardVPNconName_Object = MibTableColumn
mGuardVPNconName = _MGuardVPNconName_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 2),
    _MGuardVPNconName_Type()
)
mGuardVPNconName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNconName.setStatus("mandatory")


class _MGuardVPNconEnabled_Type(Integer32):
    """Custom type mGuardVPNconEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MGuardVPNconEnabled_Type.__name__ = "Integer32"
_MGuardVPNconEnabled_Object = MibTableColumn
mGuardVPNconEnabled = _MGuardVPNconEnabled_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 3),
    _MGuardVPNconEnabled_Type()
)
mGuardVPNconEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNconEnabled.setStatus("mandatory")
_MGuardVPNremGW_Type = DisplayString
_MGuardVPNremGW_Object = MibTableColumn
mGuardVPNremGW = _MGuardVPNremGW_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 4),
    _MGuardVPNremGW_Type()
)
mGuardVPNremGW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNremGW.setStatus("mandatory")


class _MGuardVPNconType_Type(Integer32):
    """Custom type mGuardVPNconType based on Integer32"""
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
        *(("l2tp-ssh", 4),
          ("l2tp-w2k", 3),
          ("transport", 1),
          ("tunnel", 2))
    )


_MGuardVPNconType_Type.__name__ = "Integer32"
_MGuardVPNconType_Object = MibTableColumn
mGuardVPNconType = _MGuardVPNconType_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 5),
    _MGuardVPNconType_Type()
)
mGuardVPNconType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNconType.setStatus("mandatory")
_MGuardVPNlocalNet_Type = IpAddress
_MGuardVPNlocalNet_Object = MibTableColumn
mGuardVPNlocalNet = _MGuardVPNlocalNet_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 6),
    _MGuardVPNlocalNet_Type()
)
mGuardVPNlocalNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNlocalNet.setStatus("deprecated")
_MGuardVPNlocalMask_Type = IpAddress
_MGuardVPNlocalMask_Object = MibTableColumn
mGuardVPNlocalMask = _MGuardVPNlocalMask_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 7),
    _MGuardVPNlocalMask_Type()
)
mGuardVPNlocalMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNlocalMask.setStatus("deprecated")
_MGuardVPNremoteNet_Type = IpAddress
_MGuardVPNremoteNet_Object = MibTableColumn
mGuardVPNremoteNet = _MGuardVPNremoteNet_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 8),
    _MGuardVPNremoteNet_Type()
)
mGuardVPNremoteNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNremoteNet.setStatus("deprecated")
_MGuardVPNremoteMask_Type = IpAddress
_MGuardVPNremoteMask_Object = MibTableColumn
mGuardVPNremoteMask = _MGuardVPNremoteMask_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 9),
    _MGuardVPNremoteMask_Type()
)
mGuardVPNremoteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNremoteMask.setStatus("deprecated")


class _MGuardVPNauthType_Type(Integer32):
    """Custom type mGuardVPNauthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("psk", 1),
          ("x509", 2))
    )


_MGuardVPNauthType_Type.__name__ = "Integer32"
_MGuardVPNauthType_Object = MibTableColumn
mGuardVPNauthType = _MGuardVPNauthType_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 10),
    _MGuardVPNauthType_Type()
)
mGuardVPNauthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNauthType.setStatus("mandatory")
_MGuardVPNpsk_Type = DisplayString
_MGuardVPNpsk_Object = MibTableColumn
mGuardVPNpsk = _MGuardVPNpsk_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 11),
    _MGuardVPNpsk_Type()
)
mGuardVPNpsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNpsk.setStatus("mandatory")
_MGuardVPNx509_Type = DisplayString
_MGuardVPNx509_Object = MibTableColumn
mGuardVPNx509 = _MGuardVPNx509_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 12),
    _MGuardVPNx509_Type()
)
mGuardVPNx509.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNx509.setStatus("mandatory")


class _MGuardVPNikeDH_Type(Integer32):
    """Custom type mGuardVPNikeDH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("modp1024", 2),
          ("modp1536", 3),
          ("modp2048", 4),
          ("modp3072", 5),
          ("modp4096", 6))
    )


_MGuardVPNikeDH_Type.__name__ = "Integer32"
_MGuardVPNikeDH_Object = MibTableColumn
mGuardVPNikeDH = _MGuardVPNikeDH_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 13),
    _MGuardVPNikeDH_Type()
)
mGuardVPNikeDH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNikeDH.setStatus("mandatory")


class _MGuardVPNikeHash_Type(Integer32):
    """Custom type mGuardVPNikeHash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("md5", 2),
          ("sha1", 3))
    )


_MGuardVPNikeHash_Type.__name__ = "Integer32"
_MGuardVPNikeHash_Object = MibTableColumn
mGuardVPNikeHash = _MGuardVPNikeHash_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 14),
    _MGuardVPNikeHash_Type()
)
mGuardVPNikeHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNikeHash.setStatus("mandatory")


class _MGuardVPNipsecHash_Type(Integer32):
    """Custom type mGuardVPNipsecHash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("md5", 2),
          ("sha1", 3))
    )


_MGuardVPNipsecHash_Type.__name__ = "Integer32"
_MGuardVPNipsecHash_Object = MibTableColumn
mGuardVPNipsecHash = _MGuardVPNipsecHash_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 15),
    _MGuardVPNipsecHash_Type()
)
mGuardVPNipsecHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNipsecHash.setStatus("mandatory")


class _MGuardVPNikeAlg_Type(Integer32):
    """Custom type mGuardVPNikeAlg based on Integer32"""
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
        *(("aes128", 3),
          ("aes192", 4),
          ("aes256", 5),
          ("des", 1),
          ("tripledes168", 2))
    )


_MGuardVPNikeAlg_Type.__name__ = "Integer32"
_MGuardVPNikeAlg_Object = MibTableColumn
mGuardVPNikeAlg = _MGuardVPNikeAlg_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 16),
    _MGuardVPNikeAlg_Type()
)
mGuardVPNikeAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNikeAlg.setStatus("mandatory")


class _MGuardVPNipsecAlg_Type(Integer32):
    """Custom type mGuardVPNipsecAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("aes128", 3),
          ("aes192", 4),
          ("aes256", 5),
          ("des", 1),
          ("null", 6),
          ("tripledes168", 2))
    )


_MGuardVPNipsecAlg_Type.__name__ = "Integer32"
_MGuardVPNipsecAlg_Object = MibTableColumn
mGuardVPNipsecAlg = _MGuardVPNipsecAlg_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 17),
    _MGuardVPNipsecAlg_Type()
)
mGuardVPNipsecAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNipsecAlg.setStatus("mandatory")


class _MGuardVPNpfs_Type(Integer32):
    """Custom type mGuardVPNpfs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("modp1024", 3),
          ("modp1536", 4),
          ("modp2048", 5),
          ("modp3072", 6),
          ("modp4096", 7),
          ("no", 1))
    )


_MGuardVPNpfs_Type.__name__ = "Integer32"
_MGuardVPNpfs_Object = MibTableColumn
mGuardVPNpfs = _MGuardVPNpfs_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 18),
    _MGuardVPNpfs_Type()
)
mGuardVPNpfs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNpfs.setStatus("mandatory")


class _MGuardVPNconStartUp_Type(Integer32):
    """Custom type mGuardVPNconStartUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initiate", 1),
          ("waitForRemote", 2))
    )


_MGuardVPNconStartUp_Type.__name__ = "Integer32"
_MGuardVPNconStartUp_Object = MibTableColumn
mGuardVPNconStartUp = _MGuardVPNconStartUp_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 19),
    _MGuardVPNconStartUp_Type()
)
mGuardVPNconStartUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNconStartUp.setStatus("mandatory")


class _MGuardVPNvirtIPMethod_Type(Integer32):
    """Custom type mGuardVPNvirtIPMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp-over-ipsec", 2),
          ("static", 1))
    )


_MGuardVPNvirtIPMethod_Type.__name__ = "Integer32"
_MGuardVPNvirtIPMethod_Object = MibTableColumn
mGuardVPNvirtIPMethod = _MGuardVPNvirtIPMethod_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 20),
    _MGuardVPNvirtIPMethod_Type()
)
mGuardVPNvirtIPMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNvirtIPMethod.setStatus("mandatory")
_MGuardVPNvirtIP_Type = IpAddress
_MGuardVPNvirtIP_Object = MibTableColumn
mGuardVPNvirtIP = _MGuardVPNvirtIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 21),
    _MGuardVPNvirtIP_Type()
)
mGuardVPNvirtIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNvirtIP.setStatus("mandatory")


class _MGuardVPNFWLogDefIn_Type(Integer32):
    """Custom type mGuardVPNFWLogDefIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardVPNFWLogDefIn_Type.__name__ = "Integer32"
_MGuardVPNFWLogDefIn_Object = MibTableColumn
mGuardVPNFWLogDefIn = _MGuardVPNFWLogDefIn_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 22),
    _MGuardVPNFWLogDefIn_Type()
)
mGuardVPNFWLogDefIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNFWLogDefIn.setStatus("mandatory")


class _MGuardVPNFWLogDefOut_Type(Integer32):
    """Custom type mGuardVPNFWLogDefOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardVPNFWLogDefOut_Type.__name__ = "Integer32"
_MGuardVPNFWLogDefOut_Object = MibTableColumn
mGuardVPNFWLogDefOut = _MGuardVPNFWLogDefOut_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 23),
    _MGuardVPNFWLogDefOut_Type()
)
mGuardVPNFWLogDefOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNFWLogDefOut.setStatus("mandatory")


class _MGuardVPNProtoAH_Type(Integer32):
    """Custom type mGuardVPNProtoAH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardVPNProtoAH_Type.__name__ = "Integer32"
_MGuardVPNProtoAH_Object = MibTableColumn
mGuardVPNProtoAH = _MGuardVPNProtoAH_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 26),
    _MGuardVPNProtoAH_Type()
)
mGuardVPNProtoAH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNProtoAH.setStatus("mandatory")


class _MGuardVPNProtoESP_Type(Integer32):
    """Custom type mGuardVPNProtoESP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardVPNProtoESP_Type.__name__ = "Integer32"
_MGuardVPNProtoESP_Object = MibTableColumn
mGuardVPNProtoESP = _MGuardVPNProtoESP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 27),
    _MGuardVPNProtoESP_Type()
)
mGuardVPNProtoESP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNProtoESP.setStatus("mandatory")


class _MGuardVPNComp_Type(Integer32):
    """Custom type mGuardVPNComp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardVPNComp_Type.__name__ = "Integer32"
_MGuardVPNComp_Object = MibTableColumn
mGuardVPNComp = _MGuardVPNComp_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 28),
    _MGuardVPNComp_Type()
)
mGuardVPNComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNComp.setStatus("mandatory")


class _MGuardVPNLocalIDMode_Type(Integer32):
    """Custom type mGuardVPNLocalIDMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("freeswan", 2))
    )


_MGuardVPNLocalIDMode_Type.__name__ = "Integer32"
_MGuardVPNLocalIDMode_Object = MibTableColumn
mGuardVPNLocalIDMode = _MGuardVPNLocalIDMode_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 29),
    _MGuardVPNLocalIDMode_Type()
)
mGuardVPNLocalIDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNLocalIDMode.setStatus("mandatory")
_MGuardVPNLocalID_Type = DisplayString
_MGuardVPNLocalID_Object = MibTableColumn
mGuardVPNLocalID = _MGuardVPNLocalID_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 30),
    _MGuardVPNLocalID_Type()
)
mGuardVPNLocalID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNLocalID.setStatus("mandatory")


class _MGuardVPNRemoteIDMode_Type(Integer32):
    """Custom type mGuardVPNRemoteIDMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("freeswan", 2))
    )


_MGuardVPNRemoteIDMode_Type.__name__ = "Integer32"
_MGuardVPNRemoteIDMode_Object = MibTableColumn
mGuardVPNRemoteIDMode = _MGuardVPNRemoteIDMode_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 31),
    _MGuardVPNRemoteIDMode_Type()
)
mGuardVPNRemoteIDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNRemoteIDMode.setStatus("mandatory")
_MGuardVPNRemoteID_Type = DisplayString
_MGuardVPNRemoteID_Object = MibTableColumn
mGuardVPNRemoteID = _MGuardVPNRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 32),
    _MGuardVPNRemoteID_Type()
)
mGuardVPNRemoteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNRemoteID.setStatus("mandatory")
_MGuardVPNIkeLifetime_Type = Integer32
_MGuardVPNIkeLifetime_Object = MibTableColumn
mGuardVPNIkeLifetime = _MGuardVPNIkeLifetime_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 33),
    _MGuardVPNIkeLifetime_Type()
)
mGuardVPNIkeLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNIkeLifetime.setStatus("mandatory")
_MGuardVPNIpsecLifetime_Type = Integer32
_MGuardVPNIpsecLifetime_Object = MibTableColumn
mGuardVPNIpsecLifetime = _MGuardVPNIpsecLifetime_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 34),
    _MGuardVPNIpsecLifetime_Type()
)
mGuardVPNIpsecLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNIpsecLifetime.setStatus("mandatory")
_MGuardVPNRekeyMargin_Type = Integer32
_MGuardVPNRekeyMargin_Object = MibTableColumn
mGuardVPNRekeyMargin = _MGuardVPNRekeyMargin_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 35),
    _MGuardVPNRekeyMargin_Type()
)
mGuardVPNRekeyMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNRekeyMargin.setStatus("mandatory")
_MGuardVPNRekeyFuzz_Type = Integer32
_MGuardVPNRekeyFuzz_Object = MibTableColumn
mGuardVPNRekeyFuzz = _MGuardVPNRekeyFuzz_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 36),
    _MGuardVPNRekeyFuzz_Type()
)
mGuardVPNRekeyFuzz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNRekeyFuzz.setStatus("mandatory")
_MGuardVPNKeyingTries_Type = Integer32
_MGuardVPNKeyingTries_Object = MibTableColumn
mGuardVPNKeyingTries = _MGuardVPNKeyingTries_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 37),
    _MGuardVPNKeyingTries_Type()
)
mGuardVPNKeyingTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNKeyingTries.setStatus("mandatory")


class _MGuardVPNRekey_Type(Integer32):
    """Custom type mGuardVPNRekey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardVPNRekey_Type.__name__ = "Integer32"
_MGuardVPNRekey_Object = MibTableColumn
mGuardVPNRekey = _MGuardVPNRekey_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 38),
    _MGuardVPNRekey_Type()
)
mGuardVPNRekey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNRekey.setStatus("mandatory")


class _MGuardVPNDPDAction_Type(Integer32):
    """Custom type mGuardVPNDPDAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("hold", 1))
    )


_MGuardVPNDPDAction_Type.__name__ = "Integer32"
_MGuardVPNDPDAction_Object = MibTableColumn
mGuardVPNDPDAction = _MGuardVPNDPDAction_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 39),
    _MGuardVPNDPDAction_Type()
)
mGuardVPNDPDAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNDPDAction.setStatus("mandatory")
_MGuardVPNDPDDelay_Type = Integer32
_MGuardVPNDPDDelay_Object = MibTableColumn
mGuardVPNDPDDelay = _MGuardVPNDPDDelay_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 40),
    _MGuardVPNDPDDelay_Type()
)
mGuardVPNDPDDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNDPDDelay.setStatus("mandatory")
_MGuardVPNDPDTimeout_Type = Integer32
_MGuardVPNDPDTimeout_Object = MibTableColumn
mGuardVPNDPDTimeout = _MGuardVPNDPDTimeout_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 41),
    _MGuardVPNDPDTimeout_Type()
)
mGuardVPNDPDTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNDPDTimeout.setStatus("mandatory")
_MGuardVPNRowStatus_Type = RowStatus
_MGuardVPNRowStatus_Object = MibTableColumn
mGuardVPNRowStatus = _MGuardVPNRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 42),
    _MGuardVPNRowStatus_Type()
)
mGuardVPNRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNRowStatus.setStatus("mandatory")


class _MGuardVPNAggressive_Type(Integer32):
    """Custom type mGuardVPNAggressive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MGuardVPNAggressive_Type.__name__ = "Integer32"
_MGuardVPNAggressive_Object = MibTableColumn
mGuardVPNAggressive = _MGuardVPNAggressive_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 43),
    _MGuardVPNAggressive_Type()
)
mGuardVPNAggressive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNAggressive.setStatus("mandatory")
_MGuardVPNlocal_Type = DisplayString
_MGuardVPNlocal_Object = MibTableColumn
mGuardVPNlocal = _MGuardVPNlocal_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 44),
    _MGuardVPNlocal_Type()
)
mGuardVPNlocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNlocal.setStatus("mandatory")
_MGuardVPNremote_Type = DisplayString
_MGuardVPNremote_Object = MibTableColumn
mGuardVPNremote = _MGuardVPNremote_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 2, 1, 45),
    _MGuardVPNremote_Type()
)
mGuardVPNremote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNremote.setStatus("mandatory")
_MGuardVPNFW_ObjectIdentity = ObjectIdentity
mGuardVPNFW = _MGuardVPNFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3)
)
_MGuardVPNFWINTable_Object = MibTable
mGuardVPNFWINTable = _MGuardVPNFWINTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mGuardVPNFWINTable.setStatus("mandatory")
_MGuardVPNFWINEntry_Object = MibTableRow
mGuardVPNFWINEntry = _MGuardVPNFWINEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 1, 1)
)
mGuardVPNFWINEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardVPNFWINconIndex"),
    (0, "MGUARDB-MIB", "mGuardVPNFWINruleIndex"),
)
if mibBuilder.loadTexts:
    mGuardVPNFWINEntry.setStatus("mandatory")


class _MGuardVPNFWINconIndex_Type(Integer32):
    """Custom type mGuardVPNFWINconIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_MGuardVPNFWINconIndex_Type.__name__ = "Integer32"
_MGuardVPNFWINconIndex_Object = MibTableColumn
mGuardVPNFWINconIndex = _MGuardVPNFWINconIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 1, 1, 1),
    _MGuardVPNFWINconIndex_Type()
)
mGuardVPNFWINconIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardVPNFWINconIndex.setStatus("mandatory")


class _MGuardVPNFWINruleIndex_Type(Integer32):
    """Custom type mGuardVPNFWINruleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_MGuardVPNFWINruleIndex_Type.__name__ = "Integer32"
_MGuardVPNFWINruleIndex_Object = MibTableColumn
mGuardVPNFWINruleIndex = _MGuardVPNFWINruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 1, 1, 2),
    _MGuardVPNFWINruleIndex_Type()
)
mGuardVPNFWINruleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardVPNFWINruleIndex.setStatus("mandatory")
_MGuardVPNFWINsourceIP_Type = DisplayString
_MGuardVPNFWINsourceIP_Object = MibTableColumn
mGuardVPNFWINsourceIP = _MGuardVPNFWINsourceIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 1, 1, 3),
    _MGuardVPNFWINsourceIP_Type()
)
mGuardVPNFWINsourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNFWINsourceIP.setStatus("mandatory")
_MGuardVPNFWINdestinationIP_Type = DisplayString
_MGuardVPNFWINdestinationIP_Object = MibTableColumn
mGuardVPNFWINdestinationIP = _MGuardVPNFWINdestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 1, 1, 4),
    _MGuardVPNFWINdestinationIP_Type()
)
mGuardVPNFWINdestinationIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNFWINdestinationIP.setStatus("mandatory")
_MGuardVPNFWINsport_Type = DisplayString
_MGuardVPNFWINsport_Object = MibTableColumn
mGuardVPNFWINsport = _MGuardVPNFWINsport_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 1, 1, 5),
    _MGuardVPNFWINsport_Type()
)
mGuardVPNFWINsport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNFWINsport.setStatus("mandatory")
_MGuardVPNFWINdport_Type = DisplayString
_MGuardVPNFWINdport_Object = MibTableColumn
mGuardVPNFWINdport = _MGuardVPNFWINdport_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 1, 1, 6),
    _MGuardVPNFWINdport_Type()
)
mGuardVPNFWINdport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNFWINdport.setStatus("mandatory")


class _MGuardVPNFWINtarget_Type(Integer32):
    """Custom type mGuardVPNFWINtarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 3),
          ("reject", 2))
    )


_MGuardVPNFWINtarget_Type.__name__ = "Integer32"
_MGuardVPNFWINtarget_Object = MibTableColumn
mGuardVPNFWINtarget = _MGuardVPNFWINtarget_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 1, 1, 7),
    _MGuardVPNFWINtarget_Type()
)
mGuardVPNFWINtarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNFWINtarget.setStatus("mandatory")


class _MGuardVPNFWINproto_Type(Integer32):
    """Custom type mGuardVPNFWINproto based on Integer32"""
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
        *(("all", 4),
          ("icmp", 3),
          ("tcp", 1),
          ("udp", 2))
    )


_MGuardVPNFWINproto_Type.__name__ = "Integer32"
_MGuardVPNFWINproto_Object = MibTableColumn
mGuardVPNFWINproto = _MGuardVPNFWINproto_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 1, 1, 8),
    _MGuardVPNFWINproto_Type()
)
mGuardVPNFWINproto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNFWINproto.setStatus("mandatory")


class _MGuardVPNFWINlog_Type(Integer32):
    """Custom type mGuardVPNFWINlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardVPNFWINlog_Type.__name__ = "Integer32"
_MGuardVPNFWINlog_Object = MibTableColumn
mGuardVPNFWINlog = _MGuardVPNFWINlog_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 1, 1, 9),
    _MGuardVPNFWINlog_Type()
)
mGuardVPNFWINlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNFWINlog.setStatus("mandatory")
_MGuardVPNFWINRowStatus_Type = RowStatus
_MGuardVPNFWINRowStatus_Object = MibTableColumn
mGuardVPNFWINRowStatus = _MGuardVPNFWINRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 1, 1, 10),
    _MGuardVPNFWINRowStatus_Type()
)
mGuardVPNFWINRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNFWINRowStatus.setStatus("mandatory")
_MGuardVPNFWINcomment_Type = DisplayString
_MGuardVPNFWINcomment_Object = MibTableColumn
mGuardVPNFWINcomment = _MGuardVPNFWINcomment_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 1, 1, 11),
    _MGuardVPNFWINcomment_Type()
)
mGuardVPNFWINcomment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNFWINcomment.setStatus("mandatory")
_MGuardVPNFWOUTTable_Object = MibTable
mGuardVPNFWOUTTable = _MGuardVPNFWOUTTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    mGuardVPNFWOUTTable.setStatus("mandatory")
_MGuardVPNFWOUTEntry_Object = MibTableRow
mGuardVPNFWOUTEntry = _MGuardVPNFWOUTEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 2, 1)
)
mGuardVPNFWOUTEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardVPNFWOUTconIndex"),
    (0, "MGUARDB-MIB", "mGuardVPNFWOUTruleIndex"),
)
if mibBuilder.loadTexts:
    mGuardVPNFWOUTEntry.setStatus("mandatory")


class _MGuardVPNFWOUTconIndex_Type(Integer32):
    """Custom type mGuardVPNFWOUTconIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_MGuardVPNFWOUTconIndex_Type.__name__ = "Integer32"
_MGuardVPNFWOUTconIndex_Object = MibTableColumn
mGuardVPNFWOUTconIndex = _MGuardVPNFWOUTconIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 2, 1, 1),
    _MGuardVPNFWOUTconIndex_Type()
)
mGuardVPNFWOUTconIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardVPNFWOUTconIndex.setStatus("mandatory")


class _MGuardVPNFWOUTruleIndex_Type(Integer32):
    """Custom type mGuardVPNFWOUTruleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_MGuardVPNFWOUTruleIndex_Type.__name__ = "Integer32"
_MGuardVPNFWOUTruleIndex_Object = MibTableColumn
mGuardVPNFWOUTruleIndex = _MGuardVPNFWOUTruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 2, 1, 2),
    _MGuardVPNFWOUTruleIndex_Type()
)
mGuardVPNFWOUTruleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardVPNFWOUTruleIndex.setStatus("mandatory")
_MGuardVPNFWOUTsourceIP_Type = DisplayString
_MGuardVPNFWOUTsourceIP_Object = MibTableColumn
mGuardVPNFWOUTsourceIP = _MGuardVPNFWOUTsourceIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 2, 1, 3),
    _MGuardVPNFWOUTsourceIP_Type()
)
mGuardVPNFWOUTsourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNFWOUTsourceIP.setStatus("mandatory")
_MGuardVPNFWOUTdestinationIP_Type = DisplayString
_MGuardVPNFWOUTdestinationIP_Object = MibTableColumn
mGuardVPNFWOUTdestinationIP = _MGuardVPNFWOUTdestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 2, 1, 4),
    _MGuardVPNFWOUTdestinationIP_Type()
)
mGuardVPNFWOUTdestinationIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNFWOUTdestinationIP.setStatus("mandatory")
_MGuardVPNFWOUTsport_Type = DisplayString
_MGuardVPNFWOUTsport_Object = MibTableColumn
mGuardVPNFWOUTsport = _MGuardVPNFWOUTsport_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 2, 1, 5),
    _MGuardVPNFWOUTsport_Type()
)
mGuardVPNFWOUTsport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNFWOUTsport.setStatus("mandatory")
_MGuardVPNFWOUTdport_Type = DisplayString
_MGuardVPNFWOUTdport_Object = MibTableColumn
mGuardVPNFWOUTdport = _MGuardVPNFWOUTdport_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 2, 1, 6),
    _MGuardVPNFWOUTdport_Type()
)
mGuardVPNFWOUTdport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNFWOUTdport.setStatus("mandatory")


class _MGuardVPNFWOUTtarget_Type(Integer32):
    """Custom type mGuardVPNFWOUTtarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 3),
          ("reject", 2))
    )


_MGuardVPNFWOUTtarget_Type.__name__ = "Integer32"
_MGuardVPNFWOUTtarget_Object = MibTableColumn
mGuardVPNFWOUTtarget = _MGuardVPNFWOUTtarget_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 2, 1, 7),
    _MGuardVPNFWOUTtarget_Type()
)
mGuardVPNFWOUTtarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNFWOUTtarget.setStatus("mandatory")


class _MGuardVPNFWOUTproto_Type(Integer32):
    """Custom type mGuardVPNFWOUTproto based on Integer32"""
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
        *(("all", 4),
          ("icmp", 3),
          ("tcp", 1),
          ("udp", 2))
    )


_MGuardVPNFWOUTproto_Type.__name__ = "Integer32"
_MGuardVPNFWOUTproto_Object = MibTableColumn
mGuardVPNFWOUTproto = _MGuardVPNFWOUTproto_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 2, 1, 8),
    _MGuardVPNFWOUTproto_Type()
)
mGuardVPNFWOUTproto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNFWOUTproto.setStatus("mandatory")


class _MGuardVPNFWOUTlog_Type(Integer32):
    """Custom type mGuardVPNFWOUTlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardVPNFWOUTlog_Type.__name__ = "Integer32"
_MGuardVPNFWOUTlog_Object = MibTableColumn
mGuardVPNFWOUTlog = _MGuardVPNFWOUTlog_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 2, 1, 9),
    _MGuardVPNFWOUTlog_Type()
)
mGuardVPNFWOUTlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNFWOUTlog.setStatus("mandatory")
_MGuardVPNFWOUTRowStatus_Type = RowStatus
_MGuardVPNFWOUTRowStatus_Object = MibTableColumn
mGuardVPNFWOUTRowStatus = _MGuardVPNFWOUTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 2, 1, 10),
    _MGuardVPNFWOUTRowStatus_Type()
)
mGuardVPNFWOUTRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNFWOUTRowStatus.setStatus("mandatory")
_MGuardVPNFWOUTcomment_Type = DisplayString
_MGuardVPNFWOUTcomment_Object = MibTableColumn
mGuardVPNFWOUTcomment = _MGuardVPNFWOUTcomment_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 3, 2, 1, 11),
    _MGuardVPNFWOUTcomment_Type()
)
mGuardVPNFWOUTcomment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNFWOUTcomment.setStatus("mandatory")
_MGuardVPNDynDNS_ObjectIdentity = ObjectIdentity
mGuardVPNDynDNS = _MGuardVPNDynDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 4)
)
_MGuardVPNDynDNSRegister_ObjectIdentity = ObjectIdentity
mGuardVPNDynDNSRegister = _MGuardVPNDynDNSRegister_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 4, 1)
)
_MGuardVPNDynDNSReg_Type = TruthValue
_MGuardVPNDynDNSReg_Object = MibScalar
mGuardVPNDynDNSReg = _MGuardVPNDynDNSReg_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 4, 1, 1),
    _MGuardVPNDynDNSReg_Type()
)
mGuardVPNDynDNSReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNDynDNSReg.setStatus("mandatory")
_MGuardVPNDynDNSRegInterval_Type = Integer32
_MGuardVPNDynDNSRegInterval_Object = MibScalar
mGuardVPNDynDNSRegInterval = _MGuardVPNDynDNSRegInterval_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 4, 1, 2),
    _MGuardVPNDynDNSRegInterval_Type()
)
mGuardVPNDynDNSRegInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNDynDNSRegInterval.setStatus("mandatory")
_MGuardVPNDynDNSRegServer_Type = DisplayString
_MGuardVPNDynDNSRegServer_Object = MibScalar
mGuardVPNDynDNSRegServer = _MGuardVPNDynDNSRegServer_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 4, 1, 3),
    _MGuardVPNDynDNSRegServer_Type()
)
mGuardVPNDynDNSRegServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNDynDNSRegServer.setStatus("mandatory")
_MGuardVPNDynDNSRegLogin_Type = DisplayString
_MGuardVPNDynDNSRegLogin_Object = MibScalar
mGuardVPNDynDNSRegLogin = _MGuardVPNDynDNSRegLogin_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 4, 1, 4),
    _MGuardVPNDynDNSRegLogin_Type()
)
mGuardVPNDynDNSRegLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNDynDNSRegLogin.setStatus("mandatory")
_MGuardVPNDynDNSRegPasswd_Type = DisplayString
_MGuardVPNDynDNSRegPasswd_Object = MibScalar
mGuardVPNDynDNSRegPasswd = _MGuardVPNDynDNSRegPasswd_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 4, 1, 5),
    _MGuardVPNDynDNSRegPasswd_Type()
)
mGuardVPNDynDNSRegPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNDynDNSRegPasswd.setStatus("mandatory")


class _MGuardVPNDynDNSRegProvider_Type(Integer32):
    """Custom type mGuardVPNDynDNSRegProvider based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dns4biz", 3),
          ("dyndns", 2),
          ("inominate", 1))
    )


_MGuardVPNDynDNSRegProvider_Type.__name__ = "Integer32"
_MGuardVPNDynDNSRegProvider_Object = MibScalar
mGuardVPNDynDNSRegProvider = _MGuardVPNDynDNSRegProvider_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 4, 1, 6),
    _MGuardVPNDynDNSRegProvider_Type()
)
mGuardVPNDynDNSRegProvider.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNDynDNSRegProvider.setStatus("mandatory")
_MGuardVPNDynDNSRegHostname_Type = DisplayString
_MGuardVPNDynDNSRegHostname_Object = MibScalar
mGuardVPNDynDNSRegHostname = _MGuardVPNDynDNSRegHostname_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 4, 1, 7),
    _MGuardVPNDynDNSRegHostname_Type()
)
mGuardVPNDynDNSRegHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNDynDNSRegHostname.setStatus("mandatory")
_MGuardVPNDynDNSCheck_ObjectIdentity = ObjectIdentity
mGuardVPNDynDNSCheck = _MGuardVPNDynDNSCheck_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 4, 2)
)
_MGuardVPNDynDNSCheckDo_Type = TruthValue
_MGuardVPNDynDNSCheckDo_Object = MibScalar
mGuardVPNDynDNSCheckDo = _MGuardVPNDynDNSCheckDo_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 4, 2, 1),
    _MGuardVPNDynDNSCheckDo_Type()
)
mGuardVPNDynDNSCheckDo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNDynDNSCheckDo.setStatus("mandatory")
_MGuardVPNDynDNSCheckRefresh_Type = Integer32
_MGuardVPNDynDNSCheckRefresh_Object = MibScalar
mGuardVPNDynDNSCheckRefresh = _MGuardVPNDynDNSCheckRefresh_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 4, 2, 2),
    _MGuardVPNDynDNSCheckRefresh_Type()
)
mGuardVPNDynDNSCheckRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNDynDNSCheckRefresh.setStatus("mandatory")
_MGuardVPNL2TP_ObjectIdentity = ObjectIdentity
mGuardVPNL2TP = _MGuardVPNL2TP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 5)
)


class _MGuardVPNL2TPStart_Type(Integer32):
    """Custom type mGuardVPNL2TPStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MGuardVPNL2TPStart_Type.__name__ = "Integer32"
_MGuardVPNL2TPStart_Object = MibScalar
mGuardVPNL2TPStart = _MGuardVPNL2TPStart_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 5, 1),
    _MGuardVPNL2TPStart_Type()
)
mGuardVPNL2TPStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNL2TPStart.setStatus("mandatory")
_MGuardVPNL2TPLocalIP_Type = IpAddress
_MGuardVPNL2TPLocalIP_Object = MibScalar
mGuardVPNL2TPLocalIP = _MGuardVPNL2TPLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 5, 2),
    _MGuardVPNL2TPLocalIP_Type()
)
mGuardVPNL2TPLocalIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNL2TPLocalIP.setStatus("mandatory")
_MGuardVPNL2TPRemoteIPRangeStart_Type = IpAddress
_MGuardVPNL2TPRemoteIPRangeStart_Object = MibScalar
mGuardVPNL2TPRemoteIPRangeStart = _MGuardVPNL2TPRemoteIPRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 5, 3),
    _MGuardVPNL2TPRemoteIPRangeStart_Type()
)
mGuardVPNL2TPRemoteIPRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNL2TPRemoteIPRangeStart.setStatus("mandatory")
_MGuardVPNL2TPRemoteIPRangeEnd_Type = IpAddress
_MGuardVPNL2TPRemoteIPRangeEnd_Object = MibScalar
mGuardVPNL2TPRemoteIPRangeEnd = _MGuardVPNL2TPRemoteIPRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 5, 4),
    _MGuardVPNL2TPRemoteIPRangeEnd_Type()
)
mGuardVPNL2TPRemoteIPRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNL2TPRemoteIPRangeEnd.setStatus("mandatory")
_MGuardVPNL2TPpppdOptTable_Object = MibTable
mGuardVPNL2TPpppdOptTable = _MGuardVPNL2TPpppdOptTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 5, 5)
)
if mibBuilder.loadTexts:
    mGuardVPNL2TPpppdOptTable.setStatus("mandatory")
_MGuardVPNL2TPpppdOptEntry_Object = MibTableRow
mGuardVPNL2TPpppdOptEntry = _MGuardVPNL2TPpppdOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 5, 5, 1)
)
mGuardVPNL2TPpppdOptEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardVPNL2TPpppdOptIndex"),
)
if mibBuilder.loadTexts:
    mGuardVPNL2TPpppdOptEntry.setStatus("mandatory")


class _MGuardVPNL2TPpppdOptIndex_Type(Integer32):
    """Custom type mGuardVPNL2TPpppdOptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardVPNL2TPpppdOptIndex_Type.__name__ = "Integer32"
_MGuardVPNL2TPpppdOptIndex_Object = MibTableColumn
mGuardVPNL2TPpppdOptIndex = _MGuardVPNL2TPpppdOptIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 5, 5, 1, 1),
    _MGuardVPNL2TPpppdOptIndex_Type()
)
mGuardVPNL2TPpppdOptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardVPNL2TPpppdOptIndex.setStatus("mandatory")
_MGuardVPNL2TPpppdOptValue_Type = DisplayString
_MGuardVPNL2TPpppdOptValue_Object = MibTableColumn
mGuardVPNL2TPpppdOptValue = _MGuardVPNL2TPpppdOptValue_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 5, 5, 1, 2),
    _MGuardVPNL2TPpppdOptValue_Type()
)
mGuardVPNL2TPpppdOptValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNL2TPpppdOptValue.setStatus("mandatory")
_MGuardVPNL2TPpppdOptRowStatus_Type = RowStatus
_MGuardVPNL2TPpppdOptRowStatus_Object = MibTableColumn
mGuardVPNL2TPpppdOptRowStatus = _MGuardVPNL2TPpppdOptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 5, 5, 1, 3),
    _MGuardVPNL2TPpppdOptRowStatus_Type()
)
mGuardVPNL2TPpppdOptRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNL2TPpppdOptRowStatus.setStatus("mandatory")
_MGuardVPNSettings_ObjectIdentity = ObjectIdentity
mGuardVPNSettings = _MGuardVPNSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 6)
)


class _MGuardVPNRequireUniqueIDs_Type(Integer32):
    """Custom type mGuardVPNRequireUniqueIDs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardVPNRequireUniqueIDs_Type.__name__ = "Integer32"
_MGuardVPNRequireUniqueIDs_Object = MibScalar
mGuardVPNRequireUniqueIDs = _MGuardVPNRequireUniqueIDs_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 6, 1),
    _MGuardVPNRequireUniqueIDs_Type()
)
mGuardVPNRequireUniqueIDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNRequireUniqueIDs.setStatus("mandatory")


class _MGuardVPNNatTraversal_Type(Integer32):
    """Custom type mGuardVPNNatTraversal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_MGuardVPNNatTraversal_Type.__name__ = "Integer32"
_MGuardVPNNatTraversal_Object = MibScalar
mGuardVPNNatTraversal = _MGuardVPNNatTraversal_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 6, 2),
    _MGuardVPNNatTraversal_Type()
)
mGuardVPNNatTraversal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNNatTraversal.setStatus("mandatory")


class _MGuardVPNNatTPortfloating_Type(Integer32):
    """Custom type mGuardVPNNatTPortfloating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_MGuardVPNNatTPortfloating_Type.__name__ = "Integer32"
_MGuardVPNNatTPortfloating_Object = MibScalar
mGuardVPNNatTPortfloating = _MGuardVPNNatTPortfloating_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 6, 3),
    _MGuardVPNNatTPortfloating_Type()
)
mGuardVPNNatTPortfloating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNNatTPortfloating.setStatus("mandatory")
_MGuardVPNNatTKeepAliveInterval_Type = Integer32
_MGuardVPNNatTKeepAliveInterval_Object = MibScalar
mGuardVPNNatTKeepAliveInterval = _MGuardVPNNatTKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 6, 4),
    _MGuardVPNNatTKeepAliveInterval_Type()
)
mGuardVPNNatTKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNNatTKeepAliveInterval.setStatus("mandatory")


class _MGuardVPNNatTKeepAliveForce_Type(Integer32):
    """Custom type mGuardVPNNatTKeepAliveForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardVPNNatTKeepAliveForce_Type.__name__ = "Integer32"
_MGuardVPNNatTKeepAliveForce_Object = MibScalar
mGuardVPNNatTKeepAliveForce = _MGuardVPNNatTKeepAliveForce_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 6, 5),
    _MGuardVPNNatTKeepAliveForce_Type()
)
mGuardVPNNatTKeepAliveForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNNatTKeepAliveForce.setStatus("mandatory")


class _MGuardVPNIkeLog_Type(Integer32):
    """Custom type mGuardVPNIkeLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardVPNIkeLog_Type.__name__ = "Integer32"
_MGuardVPNIkeLog_Object = MibScalar
mGuardVPNIkeLog = _MGuardVPNIkeLog_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 6, 6),
    _MGuardVPNIkeLog_Type()
)
mGuardVPNIkeLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNIkeLog.setStatus("mandatory")


class _MGuardVPNHideTos_Type(Integer32):
    """Custom type mGuardVPNHideTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardVPNHideTos_Type.__name__ = "Integer32"
_MGuardVPNHideTos_Object = MibScalar
mGuardVPNHideTos = _MGuardVPNHideTos_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 6, 7),
    _MGuardVPNHideTos_Type()
)
mGuardVPNHideTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNHideTos.setStatus("mandatory")
_MGuardVPNmtu_Type = Integer32
_MGuardVPNmtu_Object = MibScalar
mGuardVPNmtu = _MGuardVPNmtu_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 6, 8),
    _MGuardVPNmtu_Type()
)
mGuardVPNmtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNmtu.setStatus("mandatory")


class _MGuardVPNStrictCRLPolicy_Type(Integer32):
    """Custom type mGuardVPNStrictCRLPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardVPNStrictCRLPolicy_Type.__name__ = "Integer32"
_MGuardVPNStrictCRLPolicy_Object = MibScalar
mGuardVPNStrictCRLPolicy = _MGuardVPNStrictCRLPolicy_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 6, 9),
    _MGuardVPNStrictCRLPolicy_Type()
)
mGuardVPNStrictCRLPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNStrictCRLPolicy.setStatus("mandatory")


class _MGuardVPNNoCertReqSend_Type(Integer32):
    """Custom type mGuardVPNNoCertReqSend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardVPNNoCertReqSend_Type.__name__ = "Integer32"
_MGuardVPNNoCertReqSend_Object = MibScalar
mGuardVPNNoCertReqSend = _MGuardVPNNoCertReqSend_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 1, 6, 10),
    _MGuardVPNNoCertReqSend_Type()
)
mGuardVPNNoCertReqSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardVPNNoCertReqSend.setStatus("mandatory")
_MGuardFirewall_ObjectIdentity = ObjectIdentity
mGuardFirewall = _MGuardFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2)
)
_MGuardFirewallIncoming_ObjectIdentity = ObjectIdentity
mGuardFirewallIncoming = _MGuardFirewallIncoming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 1)
)
_MGuardFirewallIncomingTable_Object = MibTable
mGuardFirewallIncomingTable = _MGuardFirewallIncomingTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mGuardFirewallIncomingTable.setStatus("mandatory")
_MGuardFirewallIncomingEntry_Object = MibTableRow
mGuardFirewallIncomingEntry = _MGuardFirewallIncomingEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 1, 1, 1)
)
mGuardFirewallIncomingEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardFWINruleIndex"),
)
if mibBuilder.loadTexts:
    mGuardFirewallIncomingEntry.setStatus("mandatory")


class _MGuardFWINruleIndex_Type(Integer32):
    """Custom type mGuardFWINruleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_MGuardFWINruleIndex_Type.__name__ = "Integer32"
_MGuardFWINruleIndex_Object = MibTableColumn
mGuardFWINruleIndex = _MGuardFWINruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 1, 1, 1, 1),
    _MGuardFWINruleIndex_Type()
)
mGuardFWINruleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardFWINruleIndex.setStatus("mandatory")
_MGuardFWINsourceIP_Type = DisplayString
_MGuardFWINsourceIP_Object = MibTableColumn
mGuardFWINsourceIP = _MGuardFWINsourceIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 1, 1, 1, 2),
    _MGuardFWINsourceIP_Type()
)
mGuardFWINsourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWINsourceIP.setStatus("mandatory")
_MGuardFWINdestinationIP_Type = DisplayString
_MGuardFWINdestinationIP_Object = MibTableColumn
mGuardFWINdestinationIP = _MGuardFWINdestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 1, 1, 1, 3),
    _MGuardFWINdestinationIP_Type()
)
mGuardFWINdestinationIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWINdestinationIP.setStatus("mandatory")
_MGuardFWINsport_Type = DisplayString
_MGuardFWINsport_Object = MibTableColumn
mGuardFWINsport = _MGuardFWINsport_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 1, 1, 1, 4),
    _MGuardFWINsport_Type()
)
mGuardFWINsport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWINsport.setStatus("mandatory")
_MGuardFWINdport_Type = DisplayString
_MGuardFWINdport_Object = MibTableColumn
mGuardFWINdport = _MGuardFWINdport_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 1, 1, 1, 5),
    _MGuardFWINdport_Type()
)
mGuardFWINdport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWINdport.setStatus("mandatory")


class _MGuardFWINtarget_Type(Integer32):
    """Custom type mGuardFWINtarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 3),
          ("reject", 2))
    )


_MGuardFWINtarget_Type.__name__ = "Integer32"
_MGuardFWINtarget_Object = MibTableColumn
mGuardFWINtarget = _MGuardFWINtarget_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 1, 1, 1, 6),
    _MGuardFWINtarget_Type()
)
mGuardFWINtarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWINtarget.setStatus("mandatory")


class _MGuardFWINproto_Type(Integer32):
    """Custom type mGuardFWINproto based on Integer32"""
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
        *(("all", 4),
          ("icmp", 3),
          ("tcp", 1),
          ("udp", 2))
    )


_MGuardFWINproto_Type.__name__ = "Integer32"
_MGuardFWINproto_Object = MibTableColumn
mGuardFWINproto = _MGuardFWINproto_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 1, 1, 1, 7),
    _MGuardFWINproto_Type()
)
mGuardFWINproto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWINproto.setStatus("mandatory")


class _MGuardFWINlog_Type(Integer32):
    """Custom type mGuardFWINlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardFWINlog_Type.__name__ = "Integer32"
_MGuardFWINlog_Object = MibTableColumn
mGuardFWINlog = _MGuardFWINlog_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 1, 1, 1, 8),
    _MGuardFWINlog_Type()
)
mGuardFWINlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWINlog.setStatus("mandatory")
_MGuardFWINRowStatus_Type = RowStatus
_MGuardFWINRowStatus_Object = MibTableColumn
mGuardFWINRowStatus = _MGuardFWINRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 1, 1, 1, 9),
    _MGuardFWINRowStatus_Type()
)
mGuardFWINRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWINRowStatus.setStatus("mandatory")
_MGuardFWINcomment_Type = DisplayString
_MGuardFWINcomment_Object = MibTableColumn
mGuardFWINcomment = _MGuardFWINcomment_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 1, 1, 1, 10),
    _MGuardFWINcomment_Type()
)
mGuardFWINcomment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWINcomment.setStatus("mandatory")


class _MGuardFirewallINLogDefault_Type(Integer32):
    """Custom type mGuardFirewallINLogDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardFirewallINLogDefault_Type.__name__ = "Integer32"
_MGuardFirewallINLogDefault_Object = MibScalar
mGuardFirewallINLogDefault = _MGuardFirewallINLogDefault_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 1, 2),
    _MGuardFirewallINLogDefault_Type()
)
mGuardFirewallINLogDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallINLogDefault.setStatus("mandatory")
_MGuardFirewallOutgoing_ObjectIdentity = ObjectIdentity
mGuardFirewallOutgoing = _MGuardFirewallOutgoing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 2)
)
_MGuardFirewallOutgoingTable_Object = MibTable
mGuardFirewallOutgoingTable = _MGuardFirewallOutgoingTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mGuardFirewallOutgoingTable.setStatus("mandatory")
_MGuardFirewallOutgoingEntry_Object = MibTableRow
mGuardFirewallOutgoingEntry = _MGuardFirewallOutgoingEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 2, 1, 1)
)
mGuardFirewallOutgoingEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardFWOUTruleIndex"),
)
if mibBuilder.loadTexts:
    mGuardFirewallOutgoingEntry.setStatus("mandatory")


class _MGuardFWOUTruleIndex_Type(Integer32):
    """Custom type mGuardFWOUTruleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_MGuardFWOUTruleIndex_Type.__name__ = "Integer32"
_MGuardFWOUTruleIndex_Object = MibTableColumn
mGuardFWOUTruleIndex = _MGuardFWOUTruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 2, 1, 1, 1),
    _MGuardFWOUTruleIndex_Type()
)
mGuardFWOUTruleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardFWOUTruleIndex.setStatus("mandatory")
_MGuardFWOUTsourceIP_Type = DisplayString
_MGuardFWOUTsourceIP_Object = MibTableColumn
mGuardFWOUTsourceIP = _MGuardFWOUTsourceIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 2, 1, 1, 2),
    _MGuardFWOUTsourceIP_Type()
)
mGuardFWOUTsourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWOUTsourceIP.setStatus("mandatory")
_MGuardFWOUTdestinationIP_Type = DisplayString
_MGuardFWOUTdestinationIP_Object = MibTableColumn
mGuardFWOUTdestinationIP = _MGuardFWOUTdestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 2, 1, 1, 3),
    _MGuardFWOUTdestinationIP_Type()
)
mGuardFWOUTdestinationIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWOUTdestinationIP.setStatus("mandatory")
_MGuardFWOUTsport_Type = DisplayString
_MGuardFWOUTsport_Object = MibTableColumn
mGuardFWOUTsport = _MGuardFWOUTsport_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 2, 1, 1, 4),
    _MGuardFWOUTsport_Type()
)
mGuardFWOUTsport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWOUTsport.setStatus("mandatory")
_MGuardFWOUTdport_Type = DisplayString
_MGuardFWOUTdport_Object = MibTableColumn
mGuardFWOUTdport = _MGuardFWOUTdport_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 2, 1, 1, 5),
    _MGuardFWOUTdport_Type()
)
mGuardFWOUTdport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWOUTdport.setStatus("mandatory")


class _MGuardFWOUTtarget_Type(Integer32):
    """Custom type mGuardFWOUTtarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 3),
          ("reject", 2))
    )


_MGuardFWOUTtarget_Type.__name__ = "Integer32"
_MGuardFWOUTtarget_Object = MibTableColumn
mGuardFWOUTtarget = _MGuardFWOUTtarget_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 2, 1, 1, 6),
    _MGuardFWOUTtarget_Type()
)
mGuardFWOUTtarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWOUTtarget.setStatus("mandatory")


class _MGuardFWOUTproto_Type(Integer32):
    """Custom type mGuardFWOUTproto based on Integer32"""
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
        *(("all", 4),
          ("icmp", 3),
          ("tcp", 1),
          ("udp", 2))
    )


_MGuardFWOUTproto_Type.__name__ = "Integer32"
_MGuardFWOUTproto_Object = MibTableColumn
mGuardFWOUTproto = _MGuardFWOUTproto_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 2, 1, 1, 7),
    _MGuardFWOUTproto_Type()
)
mGuardFWOUTproto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWOUTproto.setStatus("mandatory")


class _MGuardFWOUTlog_Type(Integer32):
    """Custom type mGuardFWOUTlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardFWOUTlog_Type.__name__ = "Integer32"
_MGuardFWOUTlog_Object = MibTableColumn
mGuardFWOUTlog = _MGuardFWOUTlog_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 2, 1, 1, 8),
    _MGuardFWOUTlog_Type()
)
mGuardFWOUTlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWOUTlog.setStatus("mandatory")
_MGuardFWOUTRowStatus_Type = RowStatus
_MGuardFWOUTRowStatus_Object = MibTableColumn
mGuardFWOUTRowStatus = _MGuardFWOUTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 2, 1, 1, 9),
    _MGuardFWOUTRowStatus_Type()
)
mGuardFWOUTRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWOUTRowStatus.setStatus("mandatory")
_MGuardFWOUTcomment_Type = DisplayString
_MGuardFWOUTcomment_Object = MibTableColumn
mGuardFWOUTcomment = _MGuardFWOUTcomment_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 2, 1, 1, 10),
    _MGuardFWOUTcomment_Type()
)
mGuardFWOUTcomment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWOUTcomment.setStatus("mandatory")


class _MGuardFirewallOUTLogDefault_Type(Integer32):
    """Custom type mGuardFirewallOUTLogDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardFirewallOUTLogDefault_Type.__name__ = "Integer32"
_MGuardFirewallOUTLogDefault_Object = MibScalar
mGuardFirewallOUTLogDefault = _MGuardFirewallOUTLogDefault_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 2, 2),
    _MGuardFirewallOUTLogDefault_Type()
)
mGuardFirewallOUTLogDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallOUTLogDefault.setStatus("mandatory")
_MGuardFirewallPortforwarding_ObjectIdentity = ObjectIdentity
mGuardFirewallPortforwarding = _MGuardFirewallPortforwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 3)
)
_MGuardFirewallPortforwardTable_Object = MibTable
mGuardFirewallPortforwardTable = _MGuardFirewallPortforwardTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mGuardFirewallPortforwardTable.setStatus("mandatory")
_MGuardFirewallPortforwardEntry_Object = MibTableRow
mGuardFirewallPortforwardEntry = _MGuardFirewallPortforwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 3, 1, 1)
)
mGuardFirewallPortforwardEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardFWPORTFORWruleIndex"),
)
if mibBuilder.loadTexts:
    mGuardFirewallPortforwardEntry.setStatus("mandatory")


class _MGuardFWPORTFORWruleIndex_Type(Integer32):
    """Custom type mGuardFWPORTFORWruleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_MGuardFWPORTFORWruleIndex_Type.__name__ = "Integer32"
_MGuardFWPORTFORWruleIndex_Object = MibTableColumn
mGuardFWPORTFORWruleIndex = _MGuardFWPORTFORWruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 3, 1, 1, 1),
    _MGuardFWPORTFORWruleIndex_Type()
)
mGuardFWPORTFORWruleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardFWPORTFORWruleIndex.setStatus("mandatory")
_MGuardFWPORTFORWinIP_Type = DisplayString
_MGuardFWPORTFORWinIP_Object = MibTableColumn
mGuardFWPORTFORWinIP = _MGuardFWPORTFORWinIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 3, 1, 1, 2),
    _MGuardFWPORTFORWinIP_Type()
)
mGuardFWPORTFORWinIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWPORTFORWinIP.setStatus("mandatory")
_MGuardFWPORTFORWoutIP_Type = DisplayString
_MGuardFWPORTFORWoutIP_Object = MibTableColumn
mGuardFWPORTFORWoutIP = _MGuardFWPORTFORWoutIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 3, 1, 1, 3),
    _MGuardFWPORTFORWoutIP_Type()
)
mGuardFWPORTFORWoutIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWPORTFORWoutIP.setStatus("mandatory")
_MGuardFWPORTFORWinport_Type = DisplayString
_MGuardFWPORTFORWinport_Object = MibTableColumn
mGuardFWPORTFORWinport = _MGuardFWPORTFORWinport_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 3, 1, 1, 4),
    _MGuardFWPORTFORWinport_Type()
)
mGuardFWPORTFORWinport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWPORTFORWinport.setStatus("mandatory")
_MGuardFWPORTFORWoutport_Type = DisplayString
_MGuardFWPORTFORWoutport_Object = MibTableColumn
mGuardFWPORTFORWoutport = _MGuardFWPORTFORWoutport_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 3, 1, 1, 5),
    _MGuardFWPORTFORWoutport_Type()
)
mGuardFWPORTFORWoutport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWPORTFORWoutport.setStatus("mandatory")


class _MGuardFWPORTFORWproto_Type(Integer32):
    """Custom type mGuardFWPORTFORWproto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_MGuardFWPORTFORWproto_Type.__name__ = "Integer32"
_MGuardFWPORTFORWproto_Object = MibTableColumn
mGuardFWPORTFORWproto = _MGuardFWPORTFORWproto_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 3, 1, 1, 6),
    _MGuardFWPORTFORWproto_Type()
)
mGuardFWPORTFORWproto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWPORTFORWproto.setStatus("mandatory")


class _MGuardFWPORTFORWlog_Type(Integer32):
    """Custom type mGuardFWPORTFORWlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardFWPORTFORWlog_Type.__name__ = "Integer32"
_MGuardFWPORTFORWlog_Object = MibTableColumn
mGuardFWPORTFORWlog = _MGuardFWPORTFORWlog_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 3, 1, 1, 7),
    _MGuardFWPORTFORWlog_Type()
)
mGuardFWPORTFORWlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWPORTFORWlog.setStatus("mandatory")
_MGuardFWPORTFORWRowStatus_Type = RowStatus
_MGuardFWPORTFORWRowStatus_Object = MibTableColumn
mGuardFWPORTFORWRowStatus = _MGuardFWPORTFORWRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 3, 1, 1, 8),
    _MGuardFWPORTFORWRowStatus_Type()
)
mGuardFWPORTFORWRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWPORTFORWRowStatus.setStatus("mandatory")
_MGuardFWPORTFORWsrcIP_Type = DisplayString
_MGuardFWPORTFORWsrcIP_Object = MibTableColumn
mGuardFWPORTFORWsrcIP = _MGuardFWPORTFORWsrcIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 3, 1, 1, 9),
    _MGuardFWPORTFORWsrcIP_Type()
)
mGuardFWPORTFORWsrcIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWPORTFORWsrcIP.setStatus("mandatory")
_MGuardFWPORTFORWsrcport_Type = DisplayString
_MGuardFWPORTFORWsrcport_Object = MibTableColumn
mGuardFWPORTFORWsrcport = _MGuardFWPORTFORWsrcport_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 3, 1, 1, 10),
    _MGuardFWPORTFORWsrcport_Type()
)
mGuardFWPORTFORWsrcport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWPORTFORWsrcport.setStatus("mandatory")
_MGuardFWPORTFORWcomment_Type = DisplayString
_MGuardFWPORTFORWcomment_Object = MibTableColumn
mGuardFWPORTFORWcomment = _MGuardFWPORTFORWcomment_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 3, 1, 1, 11),
    _MGuardFWPORTFORWcomment_Type()
)
mGuardFWPORTFORWcomment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWPORTFORWcomment.setStatus("mandatory")
_MGuardFirewallNAT_ObjectIdentity = ObjectIdentity
mGuardFirewallNAT = _MGuardFirewallNAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 4)
)
_MGuardFirewallNATRuleTable_Object = MibTable
mGuardFirewallNATRuleTable = _MGuardFirewallNATRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    mGuardFirewallNATRuleTable.setStatus("mandatory")
_MGuardFirewallNATRuleEntry_Object = MibTableRow
mGuardFirewallNATRuleEntry = _MGuardFirewallNATRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 4, 1, 1)
)
mGuardFirewallNATRuleEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardFWNATruleIndex"),
)
if mibBuilder.loadTexts:
    mGuardFirewallNATRuleEntry.setStatus("mandatory")


class _MGuardFWNATruleIndex_Type(Integer32):
    """Custom type mGuardFWNATruleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_MGuardFWNATruleIndex_Type.__name__ = "Integer32"
_MGuardFWNATruleIndex_Object = MibTableColumn
mGuardFWNATruleIndex = _MGuardFWNATruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 4, 1, 1, 1),
    _MGuardFWNATruleIndex_Type()
)
mGuardFWNATruleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardFWNATruleIndex.setStatus("mandatory")
_MGuardFWNATIP_Type = DisplayString
_MGuardFWNATIP_Object = MibTableColumn
mGuardFWNATIP = _MGuardFWNATIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 4, 1, 1, 2),
    _MGuardFWNATIP_Type()
)
mGuardFWNATIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWNATIP.setStatus("mandatory")
_MGuardFWNATRowStatus_Type = RowStatus
_MGuardFWNATRowStatus_Object = MibTableColumn
mGuardFWNATRowStatus = _MGuardFWNATRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 4, 1, 1, 3),
    _MGuardFWNATRowStatus_Type()
)
mGuardFWNATRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWNATRowStatus.setStatus("mandatory")
_MGuardFWNATOutIP_Type = DisplayString
_MGuardFWNATOutIP_Object = MibTableColumn
mGuardFWNATOutIP = _MGuardFWNATOutIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 4, 1, 1, 4),
    _MGuardFWNATOutIP_Type()
)
mGuardFWNATOutIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFWNATOutIP.setStatus("mandatory")
_MGuardFirewallExtended_ObjectIdentity = ObjectIdentity
mGuardFirewallExtended = _MGuardFirewallExtended_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 5)
)
_MGuardFirewallIPConntrackMax_Type = Integer32
_MGuardFirewallIPConntrackMax_Object = MibScalar
mGuardFirewallIPConntrackMax = _MGuardFirewallIPConntrackMax_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 5, 1),
    _MGuardFirewallIPConntrackMax_Type()
)
mGuardFirewallIPConntrackMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallIPConntrackMax.setStatus("mandatory")
_MGuardFirewallIPSynfloodLimitInt_Type = Integer32
_MGuardFirewallIPSynfloodLimitInt_Object = MibScalar
mGuardFirewallIPSynfloodLimitInt = _MGuardFirewallIPSynfloodLimitInt_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 5, 2),
    _MGuardFirewallIPSynfloodLimitInt_Type()
)
mGuardFirewallIPSynfloodLimitInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallIPSynfloodLimitInt.setStatus("mandatory")
_MGuardFirewallIPSynfloodLimitExt_Type = Integer32
_MGuardFirewallIPSynfloodLimitExt_Object = MibScalar
mGuardFirewallIPSynfloodLimitExt = _MGuardFirewallIPSynfloodLimitExt_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 5, 3),
    _MGuardFirewallIPSynfloodLimitExt_Type()
)
mGuardFirewallIPSynfloodLimitExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallIPSynfloodLimitExt.setStatus("mandatory")
_MGuardFirewallICMPLimitInt_Type = Integer32
_MGuardFirewallICMPLimitInt_Object = MibScalar
mGuardFirewallICMPLimitInt = _MGuardFirewallICMPLimitInt_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 5, 4),
    _MGuardFirewallICMPLimitInt_Type()
)
mGuardFirewallICMPLimitInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallICMPLimitInt.setStatus("mandatory")
_MGuardFirewallICMPLimitExt_Type = Integer32
_MGuardFirewallICMPLimitExt_Object = MibScalar
mGuardFirewallICMPLimitExt = _MGuardFirewallICMPLimitExt_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 5, 5),
    _MGuardFirewallICMPLimitExt_Type()
)
mGuardFirewallICMPLimitExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallICMPLimitExt.setStatus("mandatory")


class _MGuardFirewallEnableConntrackFTP_Type(Integer32):
    """Custom type mGuardFirewallEnableConntrackFTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardFirewallEnableConntrackFTP_Type.__name__ = "Integer32"
_MGuardFirewallEnableConntrackFTP_Object = MibScalar
mGuardFirewallEnableConntrackFTP = _MGuardFirewallEnableConntrackFTP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 5, 6),
    _MGuardFirewallEnableConntrackFTP_Type()
)
mGuardFirewallEnableConntrackFTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallEnableConntrackFTP.setStatus("mandatory")


class _MGuardFirewallConntrackIRC_Type(Integer32):
    """Custom type mGuardFirewallConntrackIRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardFirewallConntrackIRC_Type.__name__ = "Integer32"
_MGuardFirewallConntrackIRC_Object = MibScalar
mGuardFirewallConntrackIRC = _MGuardFirewallConntrackIRC_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 5, 7),
    _MGuardFirewallConntrackIRC_Type()
)
mGuardFirewallConntrackIRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallConntrackIRC.setStatus("mandatory")


class _MGuardFirewallConntrackPPTP_Type(Integer32):
    """Custom type mGuardFirewallConntrackPPTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardFirewallConntrackPPTP_Type.__name__ = "Integer32"
_MGuardFirewallConntrackPPTP_Object = MibScalar
mGuardFirewallConntrackPPTP = _MGuardFirewallConntrackPPTP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 5, 8),
    _MGuardFirewallConntrackPPTP_Type()
)
mGuardFirewallConntrackPPTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallConntrackPPTP.setStatus("mandatory")
_MGuardFirewallARPLimitInt_Type = Integer32
_MGuardFirewallARPLimitInt_Object = MibScalar
mGuardFirewallARPLimitInt = _MGuardFirewallARPLimitInt_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 5, 9),
    _MGuardFirewallARPLimitInt_Type()
)
mGuardFirewallARPLimitInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallARPLimitInt.setStatus("mandatory")
_MGuardFirewallARPLimitExt_Type = Integer32
_MGuardFirewallARPLimitExt_Object = MibScalar
mGuardFirewallARPLimitExt = _MGuardFirewallARPLimitExt_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 5, 10),
    _MGuardFirewallARPLimitExt_Type()
)
mGuardFirewallARPLimitExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallARPLimitExt.setStatus("mandatory")


class _MGuardFirewallICMPPolicy_Type(Integer32):
    """Custom type mGuardFirewallICMPPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("drop", 1),
          ("ping", 2))
    )


_MGuardFirewallICMPPolicy_Type.__name__ = "Integer32"
_MGuardFirewallICMPPolicy_Object = MibScalar
mGuardFirewallICMPPolicy = _MGuardFirewallICMPPolicy_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 5, 11),
    _MGuardFirewallICMPPolicy_Type()
)
mGuardFirewallICMPPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallICMPPolicy.setStatus("mandatory")


class _MGuardFirewallConntrackH323_Type(Integer32):
    """Custom type mGuardFirewallConntrackH323 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardFirewallConntrackH323_Type.__name__ = "Integer32"
_MGuardFirewallConntrackH323_Object = MibScalar
mGuardFirewallConntrackH323 = _MGuardFirewallConntrackH323_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 5, 12),
    _MGuardFirewallConntrackH323_Type()
)
mGuardFirewallConntrackH323.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallConntrackH323.setStatus("mandatory")


class _MGuardFirewallIpUncleanMatch_Type(Integer32):
    """Custom type mGuardFirewallIpUncleanMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardFirewallIpUncleanMatch_Type.__name__ = "Integer32"
_MGuardFirewallIpUncleanMatch_Object = MibScalar
mGuardFirewallIpUncleanMatch = _MGuardFirewallIpUncleanMatch_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 5, 13),
    _MGuardFirewallIpUncleanMatch_Type()
)
mGuardFirewallIpUncleanMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallIpUncleanMatch.setStatus("mandatory")
_MGuardFirewall11NAT_ObjectIdentity = ObjectIdentity
mGuardFirewall11NAT = _MGuardFirewall11NAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 6)
)
_MGuardFirewall11NATRuleTable_Object = MibTable
mGuardFirewall11NATRuleTable = _MGuardFirewall11NATRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 6, 1)
)
if mibBuilder.loadTexts:
    mGuardFirewall11NATRuleTable.setStatus("mandatory")
_MGuardFirewall11NATRuleEntry_Object = MibTableRow
mGuardFirewall11NATRuleEntry = _MGuardFirewall11NATRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 6, 1, 1)
)
mGuardFirewall11NATRuleEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardFW11NATruleIndex"),
)
if mibBuilder.loadTexts:
    mGuardFirewall11NATRuleEntry.setStatus("mandatory")


class _MGuardFW11NATruleIndex_Type(Integer32):
    """Custom type mGuardFW11NATruleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_MGuardFW11NATruleIndex_Type.__name__ = "Integer32"
_MGuardFW11NATruleIndex_Object = MibTableColumn
mGuardFW11NATruleIndex = _MGuardFW11NATruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 6, 1, 1, 1),
    _MGuardFW11NATruleIndex_Type()
)
mGuardFW11NATruleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardFW11NATruleIndex.setStatus("mandatory")
_MGuardFW11NATLocal_Type = IpAddress
_MGuardFW11NATLocal_Object = MibTableColumn
mGuardFW11NATLocal = _MGuardFW11NATLocal_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 6, 1, 1, 2),
    _MGuardFW11NATLocal_Type()
)
mGuardFW11NATLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFW11NATLocal.setStatus("mandatory")
_MGuardFW11NATRemote_Type = IpAddress
_MGuardFW11NATRemote_Object = MibTableColumn
mGuardFW11NATRemote = _MGuardFW11NATRemote_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 6, 1, 1, 3),
    _MGuardFW11NATRemote_Type()
)
mGuardFW11NATRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFW11NATRemote.setStatus("mandatory")
_MGuardFW11NATMask_Type = Integer32
_MGuardFW11NATMask_Object = MibTableColumn
mGuardFW11NATMask = _MGuardFW11NATMask_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 6, 1, 1, 4),
    _MGuardFW11NATMask_Type()
)
mGuardFW11NATMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFW11NATMask.setStatus("mandatory")


class _MGuardFW11NATLog_Type(Integer32):
    """Custom type mGuardFW11NATLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardFW11NATLog_Type.__name__ = "Integer32"
_MGuardFW11NATLog_Object = MibTableColumn
mGuardFW11NATLog = _MGuardFW11NATLog_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 6, 1, 1, 5),
    _MGuardFW11NATLog_Type()
)
mGuardFW11NATLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFW11NATLog.setStatus("mandatory")
_MGuardFW11NATRowStatus_Type = RowStatus
_MGuardFW11NATRowStatus_Object = MibTableColumn
mGuardFW11NATRowStatus = _MGuardFW11NATRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 6, 1, 1, 10),
    _MGuardFW11NATRowStatus_Type()
)
mGuardFW11NATRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFW11NATRowStatus.setStatus("mandatory")
_MGuardFirewallUserFW_ObjectIdentity = ObjectIdentity
mGuardFirewallUserFW = _MGuardFirewallUserFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7)
)


class _MGuardFirewallUserFWEnabled_Type(Integer32):
    """Custom type mGuardFirewallUserFWEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MGuardFirewallUserFWEnabled_Type.__name__ = "Integer32"
_MGuardFirewallUserFWEnabled_Object = MibScalar
mGuardFirewallUserFWEnabled = _MGuardFirewallUserFWEnabled_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 1),
    _MGuardFirewallUserFWEnabled_Type()
)
mGuardFirewallUserFWEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallUserFWEnabled.setStatus("mandatory")
_MGuardFirewallUserFWTemplateTable_Object = MibTable
mGuardFirewallUserFWTemplateTable = _MGuardFirewallUserFWTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 2)
)
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateTable.setStatus("mandatory")
_MGuardFirewallUserFWTemplateEntry_Object = MibTableRow
mGuardFirewallUserFWTemplateEntry = _MGuardFirewallUserFWTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 2, 1)
)
mGuardFirewallUserFWTemplateEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardFirewallUserFWTemplateIndex"),
)
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateEntry.setStatus("mandatory")


class _MGuardFirewallUserFWTemplateIndex_Type(Integer32):
    """Custom type mGuardFirewallUserFWTemplateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardFirewallUserFWTemplateIndex_Type.__name__ = "Integer32"
_MGuardFirewallUserFWTemplateIndex_Object = MibTableColumn
mGuardFirewallUserFWTemplateIndex = _MGuardFirewallUserFWTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 2, 1, 1),
    _MGuardFirewallUserFWTemplateIndex_Type()
)
mGuardFirewallUserFWTemplateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateIndex.setStatus("mandatory")


class _MGuardFirewallUserFWTemplateEnabled_Type(Integer32):
    """Custom type mGuardFirewallUserFWTemplateEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MGuardFirewallUserFWTemplateEnabled_Type.__name__ = "Integer32"
_MGuardFirewallUserFWTemplateEnabled_Object = MibTableColumn
mGuardFirewallUserFWTemplateEnabled = _MGuardFirewallUserFWTemplateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 2, 1, 2),
    _MGuardFirewallUserFWTemplateEnabled_Type()
)
mGuardFirewallUserFWTemplateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateEnabled.setStatus("mandatory")
_MGuardFirewallUserFWTemplateName_Type = DisplayString
_MGuardFirewallUserFWTemplateName_Object = MibTableColumn
mGuardFirewallUserFWTemplateName = _MGuardFirewallUserFWTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 2, 1, 3),
    _MGuardFirewallUserFWTemplateName_Type()
)
mGuardFirewallUserFWTemplateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateName.setStatus("mandatory")
_MGuardFirewallUserFWTemplateComment_Type = DisplayString
_MGuardFirewallUserFWTemplateComment_Object = MibTableColumn
mGuardFirewallUserFWTemplateComment = _MGuardFirewallUserFWTemplateComment_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 2, 1, 4),
    _MGuardFirewallUserFWTemplateComment_Type()
)
mGuardFirewallUserFWTemplateComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateComment.setStatus("mandatory")


class _MGuardFirewallUserFWTemplateTimeout_Type(Integer32):
    """Custom type mGuardFirewallUserFWTemplateTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_MGuardFirewallUserFWTemplateTimeout_Type.__name__ = "Integer32"
_MGuardFirewallUserFWTemplateTimeout_Object = MibTableColumn
mGuardFirewallUserFWTemplateTimeout = _MGuardFirewallUserFWTemplateTimeout_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 2, 1, 5),
    _MGuardFirewallUserFWTemplateTimeout_Type()
)
mGuardFirewallUserFWTemplateTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateTimeout.setStatus("mandatory")
_MGuardFirewallUserFWTemplateSrcIP_Type = DisplayString
_MGuardFirewallUserFWTemplateSrcIP_Object = MibTableColumn
mGuardFirewallUserFWTemplateSrcIP = _MGuardFirewallUserFWTemplateSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 2, 1, 6),
    _MGuardFirewallUserFWTemplateSrcIP_Type()
)
mGuardFirewallUserFWTemplateSrcIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateSrcIP.setStatus("mandatory")
_MGuardFirewallUserFWTemplateRowStatus_Type = RowStatus
_MGuardFirewallUserFWTemplateRowStatus_Object = MibTableColumn
mGuardFirewallUserFWTemplateRowStatus = _MGuardFirewallUserFWTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 2, 1, 7),
    _MGuardFirewallUserFWTemplateRowStatus_Type()
)
mGuardFirewallUserFWTemplateRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateRowStatus.setStatus("mandatory")
_MGuardFirewallUserFWTemplateUserTable_Object = MibTable
mGuardFirewallUserFWTemplateUserTable = _MGuardFirewallUserFWTemplateUserTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 3)
)
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateUserTable.setStatus("mandatory")
_MGuardFirewallUserFWTemplateUserEntry_Object = MibTableRow
mGuardFirewallUserFWTemplateUserEntry = _MGuardFirewallUserFWTemplateUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 3, 1)
)
mGuardFirewallUserFWTemplateUserEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardFirewallUserFWTemplateUserTemplateIndex"),
    (0, "MGUARDB-MIB", "mGuardFirewallUserFWTemplateUserIndex"),
)
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateUserEntry.setStatus("mandatory")


class _MGuardFirewallUserFWTemplateUserTemplateIndex_Type(Integer32):
    """Custom type mGuardFirewallUserFWTemplateUserTemplateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardFirewallUserFWTemplateUserTemplateIndex_Type.__name__ = "Integer32"
_MGuardFirewallUserFWTemplateUserTemplateIndex_Object = MibTableColumn
mGuardFirewallUserFWTemplateUserTemplateIndex = _MGuardFirewallUserFWTemplateUserTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 3, 1, 1),
    _MGuardFirewallUserFWTemplateUserTemplateIndex_Type()
)
mGuardFirewallUserFWTemplateUserTemplateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateUserTemplateIndex.setStatus("mandatory")


class _MGuardFirewallUserFWTemplateUserIndex_Type(Integer32):
    """Custom type mGuardFirewallUserFWTemplateUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardFirewallUserFWTemplateUserIndex_Type.__name__ = "Integer32"
_MGuardFirewallUserFWTemplateUserIndex_Object = MibTableColumn
mGuardFirewallUserFWTemplateUserIndex = _MGuardFirewallUserFWTemplateUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 3, 1, 2),
    _MGuardFirewallUserFWTemplateUserIndex_Type()
)
mGuardFirewallUserFWTemplateUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateUserIndex.setStatus("mandatory")
_MGuardFirewallUserFWTemplateUserName_Type = DisplayString
_MGuardFirewallUserFWTemplateUserName_Object = MibTableColumn
mGuardFirewallUserFWTemplateUserName = _MGuardFirewallUserFWTemplateUserName_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 3, 1, 3),
    _MGuardFirewallUserFWTemplateUserName_Type()
)
mGuardFirewallUserFWTemplateUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateUserName.setStatus("mandatory")
_MGuardFirewallUserFWTemplateUserRowStatus_Type = RowStatus
_MGuardFirewallUserFWTemplateUserRowStatus_Object = MibTableColumn
mGuardFirewallUserFWTemplateUserRowStatus = _MGuardFirewallUserFWTemplateUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 3, 1, 4),
    _MGuardFirewallUserFWTemplateUserRowStatus_Type()
)
mGuardFirewallUserFWTemplateUserRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateUserRowStatus.setStatus("mandatory")
_MGuardFirewallUserFWTemplateRuleTable_Object = MibTable
mGuardFirewallUserFWTemplateRuleTable = _MGuardFirewallUserFWTemplateRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 4)
)
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateRuleTable.setStatus("mandatory")
_MGuardFirewallUserFWTemplateRuleEntry_Object = MibTableRow
mGuardFirewallUserFWTemplateRuleEntry = _MGuardFirewallUserFWTemplateRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 4, 1)
)
mGuardFirewallUserFWTemplateRuleEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardFirewallUserFWTemplateRuleTemplateIndex"),
    (0, "MGUARDB-MIB", "mGuardFirewallUserFWTemplateRuleIndex"),
)
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateRuleEntry.setStatus("mandatory")


class _MGuardFirewallUserFWTemplateRuleTemplateIndex_Type(Integer32):
    """Custom type mGuardFirewallUserFWTemplateRuleTemplateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardFirewallUserFWTemplateRuleTemplateIndex_Type.__name__ = "Integer32"
_MGuardFirewallUserFWTemplateRuleTemplateIndex_Object = MibTableColumn
mGuardFirewallUserFWTemplateRuleTemplateIndex = _MGuardFirewallUserFWTemplateRuleTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 4, 1, 1),
    _MGuardFirewallUserFWTemplateRuleTemplateIndex_Type()
)
mGuardFirewallUserFWTemplateRuleTemplateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateRuleTemplateIndex.setStatus("mandatory")


class _MGuardFirewallUserFWTemplateRuleIndex_Type(Integer32):
    """Custom type mGuardFirewallUserFWTemplateRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardFirewallUserFWTemplateRuleIndex_Type.__name__ = "Integer32"
_MGuardFirewallUserFWTemplateRuleIndex_Object = MibTableColumn
mGuardFirewallUserFWTemplateRuleIndex = _MGuardFirewallUserFWTemplateRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 4, 1, 2),
    _MGuardFirewallUserFWTemplateRuleIndex_Type()
)
mGuardFirewallUserFWTemplateRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateRuleIndex.setStatus("mandatory")


class _MGuardFirewallUserFWTemplateRuleProto_Type(Integer32):
    """Custom type mGuardFirewallUserFWTemplateRuleProto based on Integer32"""
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
        *(("all", 4),
          ("icmp", 3),
          ("tcp", 1),
          ("udp", 2))
    )


_MGuardFirewallUserFWTemplateRuleProto_Type.__name__ = "Integer32"
_MGuardFirewallUserFWTemplateRuleProto_Object = MibTableColumn
mGuardFirewallUserFWTemplateRuleProto = _MGuardFirewallUserFWTemplateRuleProto_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 4, 1, 3),
    _MGuardFirewallUserFWTemplateRuleProto_Type()
)
mGuardFirewallUserFWTemplateRuleProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateRuleProto.setStatus("mandatory")
_MGuardFirewallUserFWTemplateRuleSrcPort_Type = DisplayString
_MGuardFirewallUserFWTemplateRuleSrcPort_Object = MibTableColumn
mGuardFirewallUserFWTemplateRuleSrcPort = _MGuardFirewallUserFWTemplateRuleSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 4, 1, 4),
    _MGuardFirewallUserFWTemplateRuleSrcPort_Type()
)
mGuardFirewallUserFWTemplateRuleSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateRuleSrcPort.setStatus("mandatory")
_MGuardFirewallUserFWTemplateRuleDstPort_Type = DisplayString
_MGuardFirewallUserFWTemplateRuleDstPort_Object = MibTableColumn
mGuardFirewallUserFWTemplateRuleDstPort = _MGuardFirewallUserFWTemplateRuleDstPort_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 4, 1, 5),
    _MGuardFirewallUserFWTemplateRuleDstPort_Type()
)
mGuardFirewallUserFWTemplateRuleDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateRuleDstPort.setStatus("mandatory")
_MGuardFirewallUserFWTemplateRuleDstIP_Type = DisplayString
_MGuardFirewallUserFWTemplateRuleDstIP_Object = MibTableColumn
mGuardFirewallUserFWTemplateRuleDstIP = _MGuardFirewallUserFWTemplateRuleDstIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 4, 1, 6),
    _MGuardFirewallUserFWTemplateRuleDstIP_Type()
)
mGuardFirewallUserFWTemplateRuleDstIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateRuleDstIP.setStatus("mandatory")


class _MGuardFirewallUserFWTemplateRuleLog_Type(Integer32):
    """Custom type mGuardFirewallUserFWTemplateRuleLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardFirewallUserFWTemplateRuleLog_Type.__name__ = "Integer32"
_MGuardFirewallUserFWTemplateRuleLog_Object = MibTableColumn
mGuardFirewallUserFWTemplateRuleLog = _MGuardFirewallUserFWTemplateRuleLog_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 4, 1, 7),
    _MGuardFirewallUserFWTemplateRuleLog_Type()
)
mGuardFirewallUserFWTemplateRuleLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateRuleLog.setStatus("mandatory")
_MGuardFirewallUserFWTemplateRuleComment_Type = DisplayString
_MGuardFirewallUserFWTemplateRuleComment_Object = MibTableColumn
mGuardFirewallUserFWTemplateRuleComment = _MGuardFirewallUserFWTemplateRuleComment_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 4, 1, 8),
    _MGuardFirewallUserFWTemplateRuleComment_Type()
)
mGuardFirewallUserFWTemplateRuleComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateRuleComment.setStatus("mandatory")
_MGuardFirewallUserFWTemplateRuleRowStatus_Type = RowStatus
_MGuardFirewallUserFWTemplateRuleRowStatus_Object = MibTableColumn
mGuardFirewallUserFWTemplateRuleRowStatus = _MGuardFirewallUserFWTemplateRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 2, 7, 4, 1, 9),
    _MGuardFirewallUserFWTemplateRuleRowStatus_Type()
)
mGuardFirewallUserFWTemplateRuleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardFirewallUserFWTemplateRuleRowStatus.setStatus("mandatory")
_MGuardNetwork_ObjectIdentity = ObjectIdentity
mGuardNetwork = _MGuardNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3)
)


class _MGuardNetworkMode_Type(Integer32):
    """Custom type mGuardNetworkMode based on Integer32"""
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
        *(("pppoe", 3),
          ("pptp", 4),
          ("router", 2),
          ("stealth", 1))
    )


_MGuardNetworkMode_Type.__name__ = "Integer32"
_MGuardNetworkMode_Object = MibScalar
mGuardNetworkMode = _MGuardNetworkMode_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 1),
    _MGuardNetworkMode_Type()
)
mGuardNetworkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardNetworkMode.setStatus("mandatory")
_MGuardStealth_ObjectIdentity = ObjectIdentity
mGuardStealth = _MGuardStealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2)
)


class _MGuardStealthIPConfMode_Type(Integer32):
    """Custom type mGuardStealthIPConfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoDetect", 1),
          ("multi", 3),
          ("static", 2))
    )


_MGuardStealthIPConfMode_Type.__name__ = "Integer32"
_MGuardStealthIPConfMode_Object = MibScalar
mGuardStealthIPConfMode = _MGuardStealthIPConfMode_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 1),
    _MGuardStealthIPConfMode_Type()
)
mGuardStealthIPConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardStealthIPConfMode.setStatus("mandatory")
_MGuardStealthIPConfStatic_ObjectIdentity = ObjectIdentity
mGuardStealthIPConfStatic = _MGuardStealthIPConfStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 2)
)
_MGuardStealthStaticIP_Type = IpAddress
_MGuardStealthStaticIP_Object = MibScalar
mGuardStealthStaticIP = _MGuardStealthStaticIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 2, 1),
    _MGuardStealthStaticIP_Type()
)
mGuardStealthStaticIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardStealthStaticIP.setStatus("mandatory")
_MGuardStealthStaticMAC_Type = MacAddress
_MGuardStealthStaticMAC_Object = MibScalar
mGuardStealthStaticMAC = _MGuardStealthStaticMAC_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 2, 2),
    _MGuardStealthStaticMAC_Type()
)
mGuardStealthStaticMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardStealthStaticMAC.setStatus("mandatory")


class _MGuardStealthStaticActivate_Type(Integer32):
    """Custom type mGuardStealthStaticActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("valuescached", 2))
    )


_MGuardStealthStaticActivate_Type.__name__ = "Integer32"
_MGuardStealthStaticActivate_Object = MibScalar
mGuardStealthStaticActivate = _MGuardStealthStaticActivate_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 2, 3),
    _MGuardStealthStaticActivate_Type()
)
mGuardStealthStaticActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardStealthStaticActivate.setStatus("mandatory")
_MGuardStealthManageIP_Type = IpAddress
_MGuardStealthManageIP_Object = MibScalar
mGuardStealthManageIP = _MGuardStealthManageIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 2, 4),
    _MGuardStealthManageIP_Type()
)
mGuardStealthManageIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardStealthManageIP.setStatus("mandatory")
_MGuardStealthManageNetmask_Type = IpAddress
_MGuardStealthManageNetmask_Object = MibScalar
mGuardStealthManageNetmask = _MGuardStealthManageNetmask_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 2, 5),
    _MGuardStealthManageNetmask_Type()
)
mGuardStealthManageNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardStealthManageNetmask.setStatus("mandatory")
_MGuardStealthManageGateway_Type = IpAddress
_MGuardStealthManageGateway_Object = MibScalar
mGuardStealthManageGateway = _MGuardStealthManageGateway_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 2, 6),
    _MGuardStealthManageGateway_Type()
)
mGuardStealthManageGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardStealthManageGateway.setStatus("mandatory")


class _MGuardStealthManageActivate_Type(Integer32):
    """Custom type mGuardStealthManageActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("valuescached", 2))
    )


_MGuardStealthManageActivate_Type.__name__ = "Integer32"
_MGuardStealthManageActivate_Object = MibScalar
mGuardStealthManageActivate = _MGuardStealthManageActivate_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 2, 7),
    _MGuardStealthManageActivate_Type()
)
mGuardStealthManageActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardStealthManageActivate.setStatus("mandatory")


class _MGuardStealthHiDiscoveryRelay_Type(Integer32):
    """Custom type mGuardStealthHiDiscoveryRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MGuardStealthHiDiscoveryRelay_Type.__name__ = "Integer32"
_MGuardStealthHiDiscoveryRelay_Object = MibScalar
mGuardStealthHiDiscoveryRelay = _MGuardStealthHiDiscoveryRelay_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 3),
    _MGuardStealthHiDiscoveryRelay_Type()
)
mGuardStealthHiDiscoveryRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardStealthHiDiscoveryRelay.setStatus("mandatory")


class _MGuardStealthHiDiscoveryState_Type(Integer32):
    """Custom type mGuardStealthHiDiscoveryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("readonly", 3),
          ("readwrite", 1))
    )


_MGuardStealthHiDiscoveryState_Type.__name__ = "Integer32"
_MGuardStealthHiDiscoveryState_Object = MibScalar
mGuardStealthHiDiscoveryState = _MGuardStealthHiDiscoveryState_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 4),
    _MGuardStealthHiDiscoveryState_Type()
)
mGuardStealthHiDiscoveryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardStealthHiDiscoveryState.setStatus("mandatory")
_MGuardStealthL2Filter_ObjectIdentity = ObjectIdentity
mGuardStealthL2Filter = _MGuardStealthL2Filter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 5)
)
_MGuardL2FilterInternTable_Object = MibTable
mGuardL2FilterInternTable = _MGuardL2FilterInternTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 5, 1)
)
if mibBuilder.loadTexts:
    mGuardL2FilterInternTable.setStatus("mandatory")
_MGuardL2FilterInternEntry_Object = MibTableRow
mGuardL2FilterInternEntry = _MGuardL2FilterInternEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 5, 1, 1)
)
mGuardL2FilterInternEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardL2FilterInternRuleIndex"),
)
if mibBuilder.loadTexts:
    mGuardL2FilterInternEntry.setStatus("mandatory")


class _MGuardL2FilterInternRuleIndex_Type(Integer32):
    """Custom type mGuardL2FilterInternRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardL2FilterInternRuleIndex_Type.__name__ = "Integer32"
_MGuardL2FilterInternRuleIndex_Object = MibTableColumn
mGuardL2FilterInternRuleIndex = _MGuardL2FilterInternRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 5, 1, 1, 1),
    _MGuardL2FilterInternRuleIndex_Type()
)
mGuardL2FilterInternRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardL2FilterInternRuleIndex.setStatus("mandatory")
_MGuardL2FilterInternRowStatus_Type = RowStatus
_MGuardL2FilterInternRowStatus_Object = MibTableColumn
mGuardL2FilterInternRowStatus = _MGuardL2FilterInternRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 5, 1, 1, 2),
    _MGuardL2FilterInternRowStatus_Type()
)
mGuardL2FilterInternRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardL2FilterInternRowStatus.setStatus("mandatory")
_MGuardL2FilterInternSrcMac_Type = MacAddress
_MGuardL2FilterInternSrcMac_Object = MibTableColumn
mGuardL2FilterInternSrcMac = _MGuardL2FilterInternSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 5, 1, 1, 3),
    _MGuardL2FilterInternSrcMac_Type()
)
mGuardL2FilterInternSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardL2FilterInternSrcMac.setStatus("mandatory")
_MGuardL2FilterInternDstMac_Type = MacAddress
_MGuardL2FilterInternDstMac_Object = MibTableColumn
mGuardL2FilterInternDstMac = _MGuardL2FilterInternDstMac_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 5, 1, 1, 4),
    _MGuardL2FilterInternDstMac_Type()
)
mGuardL2FilterInternDstMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardL2FilterInternDstMac.setStatus("mandatory")
_MGuardL2FilterInternEthType_Type = Integer32
_MGuardL2FilterInternEthType_Object = MibTableColumn
mGuardL2FilterInternEthType = _MGuardL2FilterInternEthType_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 5, 1, 1, 5),
    _MGuardL2FilterInternEthType_Type()
)
mGuardL2FilterInternEthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardL2FilterInternEthType.setStatus("mandatory")


class _MGuardL2FilterInternTarget_Type(Integer32):
    """Custom type mGuardL2FilterInternTarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 3),
          ("reject", 2))
    )


_MGuardL2FilterInternTarget_Type.__name__ = "Integer32"
_MGuardL2FilterInternTarget_Object = MibTableColumn
mGuardL2FilterInternTarget = _MGuardL2FilterInternTarget_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 5, 1, 1, 6),
    _MGuardL2FilterInternTarget_Type()
)
mGuardL2FilterInternTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardL2FilterInternTarget.setStatus("mandatory")
_MGuardL2FilterInternComment_Type = DisplayString
_MGuardL2FilterInternComment_Object = MibTableColumn
mGuardL2FilterInternComment = _MGuardL2FilterInternComment_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 5, 1, 1, 7),
    _MGuardL2FilterInternComment_Type()
)
mGuardL2FilterInternComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardL2FilterInternComment.setStatus("mandatory")
_MGuardL2FilterExternTable_Object = MibTable
mGuardL2FilterExternTable = _MGuardL2FilterExternTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 5, 2)
)
if mibBuilder.loadTexts:
    mGuardL2FilterExternTable.setStatus("mandatory")
_MGuardL2FilterExternEntry_Object = MibTableRow
mGuardL2FilterExternEntry = _MGuardL2FilterExternEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 5, 2, 1)
)
mGuardL2FilterExternEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardL2FilterExternRuleIndex"),
)
if mibBuilder.loadTexts:
    mGuardL2FilterExternEntry.setStatus("mandatory")


class _MGuardL2FilterExternRuleIndex_Type(Integer32):
    """Custom type mGuardL2FilterExternRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardL2FilterExternRuleIndex_Type.__name__ = "Integer32"
_MGuardL2FilterExternRuleIndex_Object = MibTableColumn
mGuardL2FilterExternRuleIndex = _MGuardL2FilterExternRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 5, 2, 1, 1),
    _MGuardL2FilterExternRuleIndex_Type()
)
mGuardL2FilterExternRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardL2FilterExternRuleIndex.setStatus("mandatory")
_MGuardL2FilterExternRowStatus_Type = RowStatus
_MGuardL2FilterExternRowStatus_Object = MibTableColumn
mGuardL2FilterExternRowStatus = _MGuardL2FilterExternRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 5, 2, 1, 2),
    _MGuardL2FilterExternRowStatus_Type()
)
mGuardL2FilterExternRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardL2FilterExternRowStatus.setStatus("mandatory")
_MGuardL2FilterExternSrcMac_Type = MacAddress
_MGuardL2FilterExternSrcMac_Object = MibTableColumn
mGuardL2FilterExternSrcMac = _MGuardL2FilterExternSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 5, 2, 1, 3),
    _MGuardL2FilterExternSrcMac_Type()
)
mGuardL2FilterExternSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardL2FilterExternSrcMac.setStatus("mandatory")
_MGuardL2FilterExternDstMac_Type = MacAddress
_MGuardL2FilterExternDstMac_Object = MibTableColumn
mGuardL2FilterExternDstMac = _MGuardL2FilterExternDstMac_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 5, 2, 1, 4),
    _MGuardL2FilterExternDstMac_Type()
)
mGuardL2FilterExternDstMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardL2FilterExternDstMac.setStatus("mandatory")
_MGuardL2FilterExternEthType_Type = Integer32
_MGuardL2FilterExternEthType_Object = MibTableColumn
mGuardL2FilterExternEthType = _MGuardL2FilterExternEthType_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 5, 2, 1, 5),
    _MGuardL2FilterExternEthType_Type()
)
mGuardL2FilterExternEthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardL2FilterExternEthType.setStatus("mandatory")


class _MGuardL2FilterExternTarget_Type(Integer32):
    """Custom type mGuardL2FilterExternTarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 3),
          ("reject", 2))
    )


_MGuardL2FilterExternTarget_Type.__name__ = "Integer32"
_MGuardL2FilterExternTarget_Object = MibTableColumn
mGuardL2FilterExternTarget = _MGuardL2FilterExternTarget_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 5, 2, 1, 6),
    _MGuardL2FilterExternTarget_Type()
)
mGuardL2FilterExternTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardL2FilterExternTarget.setStatus("mandatory")
_MGuardL2FilterExternComment_Type = DisplayString
_MGuardL2FilterExternComment_Object = MibTableColumn
mGuardL2FilterExternComment = _MGuardL2FilterExternComment_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 5, 2, 1, 7),
    _MGuardL2FilterExternComment_Type()
)
mGuardL2FilterExternComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardL2FilterExternComment.setStatus("mandatory")


class _MGuardStealthL2ForwardGVRP_Type(Integer32):
    """Custom type mGuardStealthL2ForwardGVRP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardStealthL2ForwardGVRP_Type.__name__ = "Integer32"
_MGuardStealthL2ForwardGVRP_Object = MibScalar
mGuardStealthL2ForwardGVRP = _MGuardStealthL2ForwardGVRP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 5, 3),
    _MGuardStealthL2ForwardGVRP_Type()
)
mGuardStealthL2ForwardGVRP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardStealthL2ForwardGVRP.setStatus("mandatory")


class _MGuardStealthL2ForwardSTP_Type(Integer32):
    """Custom type mGuardStealthL2ForwardSTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardStealthL2ForwardSTP_Type.__name__ = "Integer32"
_MGuardStealthL2ForwardSTP_Object = MibScalar
mGuardStealthL2ForwardSTP = _MGuardStealthL2ForwardSTP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 5, 4),
    _MGuardStealthL2ForwardSTP_Type()
)
mGuardStealthL2ForwardSTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardStealthL2ForwardSTP.setStatus("mandatory")


class _MGuardStealthL2ForwardDHCP_Type(Integer32):
    """Custom type mGuardStealthL2ForwardDHCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardStealthL2ForwardDHCP_Type.__name__ = "Integer32"
_MGuardStealthL2ForwardDHCP_Object = MibScalar
mGuardStealthL2ForwardDHCP = _MGuardStealthL2ForwardDHCP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 5, 5),
    _MGuardStealthL2ForwardDHCP_Type()
)
mGuardStealthL2ForwardDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardStealthL2ForwardDHCP.setStatus("mandatory")
_MGuardStealthInterface_ObjectIdentity = ObjectIdentity
mGuardStealthInterface = _MGuardStealthInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 6)
)
_MGuardStealthMTU_Type = Integer32
_MGuardStealthMTU_Object = MibScalar
mGuardStealthMTU = _MGuardStealthMTU_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 6, 1),
    _MGuardStealthMTU_Type()
)
mGuardStealthMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardStealthMTU.setStatus("mandatory")
_MGuardStealthVlanMTU_Type = Integer32
_MGuardStealthVlanMTU_Object = MibScalar
mGuardStealthVlanMTU = _MGuardStealthVlanMTU_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 6, 2),
    _MGuardStealthVlanMTU_Type()
)
mGuardStealthVlanMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardStealthVlanMTU.setStatus("mandatory")


class _MGuardStealthManageUseVLAN_Type(Integer32):
    """Custom type mGuardStealthManageUseVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardStealthManageUseVLAN_Type.__name__ = "Integer32"
_MGuardStealthManageUseVLAN_Object = MibScalar
mGuardStealthManageUseVLAN = _MGuardStealthManageUseVLAN_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 6, 3),
    _MGuardStealthManageUseVLAN_Type()
)
mGuardStealthManageUseVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardStealthManageUseVLAN.setStatus("mandatory")
_MGuardStealthManageVLanID_Type = Integer32
_MGuardStealthManageVLanID_Object = MibScalar
mGuardStealthManageVLanID = _MGuardStealthManageVLanID_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 2, 6, 4),
    _MGuardStealthManageVLanID_Type()
)
mGuardStealthManageVLanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardStealthManageVLanID.setStatus("mandatory")
_MGuardRouter_ObjectIdentity = ObjectIdentity
mGuardRouter = _MGuardRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3)
)
_MGuardRouterLocal_ObjectIdentity = ObjectIdentity
mGuardRouterLocal = _MGuardRouterLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 1)
)
_MGuardRouterLocalIP_Type = IpAddress
_MGuardRouterLocalIP_Object = MibScalar
mGuardRouterLocalIP = _MGuardRouterLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 1, 1),
    _MGuardRouterLocalIP_Type()
)
mGuardRouterLocalIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterLocalIP.setStatus("mandatory")
_MGuardRouterLocalNetmask_Type = IpAddress
_MGuardRouterLocalNetmask_Object = MibScalar
mGuardRouterLocalNetmask = _MGuardRouterLocalNetmask_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 1, 2),
    _MGuardRouterLocalNetmask_Type()
)
mGuardRouterLocalNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterLocalNetmask.setStatus("mandatory")


class _MGuardRouterLocalActivate_Type(Integer32):
    """Custom type mGuardRouterLocalActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("valuescached", 2))
    )


_MGuardRouterLocalActivate_Type.__name__ = "Integer32"
_MGuardRouterLocalActivate_Object = MibScalar
mGuardRouterLocalActivate = _MGuardRouterLocalActivate_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 1, 3),
    _MGuardRouterLocalActivate_Type()
)
mGuardRouterLocalActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterLocalActivate.setStatus("mandatory")
_MGuardRouterLocalAliasesTable_Object = MibTable
mGuardRouterLocalAliasesTable = _MGuardRouterLocalAliasesTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 1, 4)
)
if mibBuilder.loadTexts:
    mGuardRouterLocalAliasesTable.setStatus("mandatory")
_MGuardRouterLocalAliasesEntry_Object = MibTableRow
mGuardRouterLocalAliasesEntry = _MGuardRouterLocalAliasesEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 1, 4, 1)
)
mGuardRouterLocalAliasesEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardLocalAliasIndex"),
)
if mibBuilder.loadTexts:
    mGuardRouterLocalAliasesEntry.setStatus("mandatory")


class _MGuardLocalAliasIndex_Type(Integer32):
    """Custom type mGuardLocalAliasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardLocalAliasIndex_Type.__name__ = "Integer32"
_MGuardLocalAliasIndex_Object = MibTableColumn
mGuardLocalAliasIndex = _MGuardLocalAliasIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 1, 4, 1, 1),
    _MGuardLocalAliasIndex_Type()
)
mGuardLocalAliasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardLocalAliasIndex.setStatus("mandatory")
_MGuardLocalAliasIpAddress_Type = IpAddress
_MGuardLocalAliasIpAddress_Object = MibTableColumn
mGuardLocalAliasIpAddress = _MGuardLocalAliasIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 1, 4, 1, 2),
    _MGuardLocalAliasIpAddress_Type()
)
mGuardLocalAliasIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardLocalAliasIpAddress.setStatus("mandatory")
_MGuardLocalAliasNetmask_Type = IpAddress
_MGuardLocalAliasNetmask_Object = MibTableColumn
mGuardLocalAliasNetmask = _MGuardLocalAliasNetmask_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 1, 4, 1, 3),
    _MGuardLocalAliasNetmask_Type()
)
mGuardLocalAliasNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardLocalAliasNetmask.setStatus("mandatory")
_MGuardLocalAliasRowStatus_Type = RowStatus
_MGuardLocalAliasRowStatus_Object = MibTableColumn
mGuardLocalAliasRowStatus = _MGuardLocalAliasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 1, 4, 1, 4),
    _MGuardLocalAliasRowStatus_Type()
)
mGuardLocalAliasRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardLocalAliasRowStatus.setStatus("mandatory")


class _MGuardLocalAliasUseVLAN_Type(Integer32):
    """Custom type mGuardLocalAliasUseVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardLocalAliasUseVLAN_Type.__name__ = "Integer32"
_MGuardLocalAliasUseVLAN_Object = MibTableColumn
mGuardLocalAliasUseVLAN = _MGuardLocalAliasUseVLAN_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 1, 4, 1, 5),
    _MGuardLocalAliasUseVLAN_Type()
)
mGuardLocalAliasUseVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardLocalAliasUseVLAN.setStatus("mandatory")
_MGuardLocalAliasVLANid_Type = Integer32
_MGuardLocalAliasVLANid_Object = MibTableColumn
mGuardLocalAliasVLANid = _MGuardLocalAliasVLANid_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 1, 4, 1, 6),
    _MGuardLocalAliasVLANid_Type()
)
mGuardLocalAliasVLANid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardLocalAliasVLANid.setStatus("mandatory")
_MGuardLocalRoutesTable_Object = MibTable
mGuardLocalRoutesTable = _MGuardLocalRoutesTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 1, 5)
)
if mibBuilder.loadTexts:
    mGuardLocalRoutesTable.setStatus("mandatory")
_MGuardLocalRoutesEntry_Object = MibTableRow
mGuardLocalRoutesEntry = _MGuardLocalRoutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 1, 5, 1)
)
mGuardLocalRoutesEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardLocalRouteIndex"),
)
if mibBuilder.loadTexts:
    mGuardLocalRoutesEntry.setStatus("mandatory")


class _MGuardLocalRouteIndex_Type(Integer32):
    """Custom type mGuardLocalRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardLocalRouteIndex_Type.__name__ = "Integer32"
_MGuardLocalRouteIndex_Object = MibTableColumn
mGuardLocalRouteIndex = _MGuardLocalRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 1, 5, 1, 1),
    _MGuardLocalRouteIndex_Type()
)
mGuardLocalRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardLocalRouteIndex.setStatus("mandatory")
_MGuardLocalRouteNetwork_Type = DisplayString
_MGuardLocalRouteNetwork_Object = MibTableColumn
mGuardLocalRouteNetwork = _MGuardLocalRouteNetwork_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 1, 5, 1, 2),
    _MGuardLocalRouteNetwork_Type()
)
mGuardLocalRouteNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardLocalRouteNetwork.setStatus("mandatory")
_MGuardLocalRouteGateway_Type = IpAddress
_MGuardLocalRouteGateway_Object = MibTableColumn
mGuardLocalRouteGateway = _MGuardLocalRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 1, 5, 1, 3),
    _MGuardLocalRouteGateway_Type()
)
mGuardLocalRouteGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardLocalRouteGateway.setStatus("mandatory")
_MGuardLocalRouteRowStatus_Type = RowStatus
_MGuardLocalRouteRowStatus_Object = MibTableColumn
mGuardLocalRouteRowStatus = _MGuardLocalRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 1, 5, 1, 4),
    _MGuardLocalRouteRowStatus_Type()
)
mGuardLocalRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardLocalRouteRowStatus.setStatus("mandatory")
_MGuardRouterLocalDevMTU_Type = Integer32
_MGuardRouterLocalDevMTU_Object = MibScalar
mGuardRouterLocalDevMTU = _MGuardRouterLocalDevMTU_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 1, 6),
    _MGuardRouterLocalDevMTU_Type()
)
mGuardRouterLocalDevMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterLocalDevMTU.setStatus("mandatory")


class _MGuardRouterLocalUseVLAN_Type(Integer32):
    """Custom type mGuardRouterLocalUseVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardRouterLocalUseVLAN_Type.__name__ = "Integer32"
_MGuardRouterLocalUseVLAN_Object = MibScalar
mGuardRouterLocalUseVLAN = _MGuardRouterLocalUseVLAN_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 1, 7),
    _MGuardRouterLocalUseVLAN_Type()
)
mGuardRouterLocalUseVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterLocalUseVLAN.setStatus("mandatory")
_MGuardRouterLocalVlanId_Type = Integer32
_MGuardRouterLocalVlanId_Object = MibScalar
mGuardRouterLocalVlanId = _MGuardRouterLocalVlanId_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 1, 8),
    _MGuardRouterLocalVlanId_Type()
)
mGuardRouterLocalVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterLocalVlanId.setStatus("mandatory")
_MGuardRouterLocalDevVlanMTU_Type = Integer32
_MGuardRouterLocalDevVlanMTU_Object = MibScalar
mGuardRouterLocalDevVlanMTU = _MGuardRouterLocalDevVlanMTU_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 1, 9),
    _MGuardRouterLocalDevVlanMTU_Type()
)
mGuardRouterLocalDevVlanMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterLocalDevVlanMTU.setStatus("mandatory")
_MGuardRouterExtern_ObjectIdentity = ObjectIdentity
mGuardRouterExtern = _MGuardRouterExtern_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 2)
)


class _MGuardRouterExternDHCP_Type(Integer32):
    """Custom type mGuardRouterExternDHCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MGuardRouterExternDHCP_Type.__name__ = "Integer32"
_MGuardRouterExternDHCP_Object = MibScalar
mGuardRouterExternDHCP = _MGuardRouterExternDHCP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 2, 1),
    _MGuardRouterExternDHCP_Type()
)
mGuardRouterExternDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterExternDHCP.setStatus("mandatory")
_MGuardRouterExternStatic_ObjectIdentity = ObjectIdentity
mGuardRouterExternStatic = _MGuardRouterExternStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 2, 2)
)
_MGuardRouterExternStaticIP_Type = IpAddress
_MGuardRouterExternStaticIP_Object = MibScalar
mGuardRouterExternStaticIP = _MGuardRouterExternStaticIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 2, 2, 1),
    _MGuardRouterExternStaticIP_Type()
)
mGuardRouterExternStaticIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterExternStaticIP.setStatus("mandatory")
_MGuardRouterExternStaticNetmask_Type = IpAddress
_MGuardRouterExternStaticNetmask_Object = MibScalar
mGuardRouterExternStaticNetmask = _MGuardRouterExternStaticNetmask_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 2, 2, 2),
    _MGuardRouterExternStaticNetmask_Type()
)
mGuardRouterExternStaticNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterExternStaticNetmask.setStatus("mandatory")
_MGuardRouterExternStaticGateway_Type = IpAddress
_MGuardRouterExternStaticGateway_Object = MibScalar
mGuardRouterExternStaticGateway = _MGuardRouterExternStaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 2, 2, 3),
    _MGuardRouterExternStaticGateway_Type()
)
mGuardRouterExternStaticGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterExternStaticGateway.setStatus("mandatory")


class _MGuardRouterExternActivate_Type(Integer32):
    """Custom type mGuardRouterExternActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("valuescached", 2))
    )


_MGuardRouterExternActivate_Type.__name__ = "Integer32"
_MGuardRouterExternActivate_Object = MibScalar
mGuardRouterExternActivate = _MGuardRouterExternActivate_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 2, 2, 4),
    _MGuardRouterExternActivate_Type()
)
mGuardRouterExternActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterExternActivate.setStatus("mandatory")
_MGuardRouterExternAliasesTable_Object = MibTable
mGuardRouterExternAliasesTable = _MGuardRouterExternAliasesTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 2, 2, 5)
)
if mibBuilder.loadTexts:
    mGuardRouterExternAliasesTable.setStatus("mandatory")
_MGuardRouterExternAliasesEntry_Object = MibTableRow
mGuardRouterExternAliasesEntry = _MGuardRouterExternAliasesEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 2, 2, 5, 1)
)
mGuardRouterExternAliasesEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardExternAliasIndex"),
)
if mibBuilder.loadTexts:
    mGuardRouterExternAliasesEntry.setStatus("mandatory")


class _MGuardExternAliasIndex_Type(Integer32):
    """Custom type mGuardExternAliasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardExternAliasIndex_Type.__name__ = "Integer32"
_MGuardExternAliasIndex_Object = MibTableColumn
mGuardExternAliasIndex = _MGuardExternAliasIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 2, 2, 5, 1, 1),
    _MGuardExternAliasIndex_Type()
)
mGuardExternAliasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardExternAliasIndex.setStatus("mandatory")
_MGuardExternAliasIpAddress_Type = IpAddress
_MGuardExternAliasIpAddress_Object = MibTableColumn
mGuardExternAliasIpAddress = _MGuardExternAliasIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 2, 2, 5, 1, 2),
    _MGuardExternAliasIpAddress_Type()
)
mGuardExternAliasIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardExternAliasIpAddress.setStatus("mandatory")
_MGuardExternAliasNetmask_Type = IpAddress
_MGuardExternAliasNetmask_Object = MibTableColumn
mGuardExternAliasNetmask = _MGuardExternAliasNetmask_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 2, 2, 5, 1, 3),
    _MGuardExternAliasNetmask_Type()
)
mGuardExternAliasNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardExternAliasNetmask.setStatus("mandatory")
_MGuardExternAliasRowStatus_Type = RowStatus
_MGuardExternAliasRowStatus_Object = MibTableColumn
mGuardExternAliasRowStatus = _MGuardExternAliasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 2, 2, 5, 1, 4),
    _MGuardExternAliasRowStatus_Type()
)
mGuardExternAliasRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardExternAliasRowStatus.setStatus("mandatory")


class _MGuardExternAliasUseVLAN_Type(Integer32):
    """Custom type mGuardExternAliasUseVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardExternAliasUseVLAN_Type.__name__ = "Integer32"
_MGuardExternAliasUseVLAN_Object = MibTableColumn
mGuardExternAliasUseVLAN = _MGuardExternAliasUseVLAN_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 2, 2, 5, 1, 5),
    _MGuardExternAliasUseVLAN_Type()
)
mGuardExternAliasUseVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardExternAliasUseVLAN.setStatus("mandatory")
_MGuardExternAliasVLANid_Type = Integer32
_MGuardExternAliasVLANid_Object = MibTableColumn
mGuardExternAliasVLANid = _MGuardExternAliasVLANid_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 2, 2, 5, 1, 6),
    _MGuardExternAliasVLANid_Type()
)
mGuardExternAliasVLANid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardExternAliasVLANid.setStatus("mandatory")
_MGuardExternRoutesTable_Object = MibTable
mGuardExternRoutesTable = _MGuardExternRoutesTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 2, 2, 6)
)
if mibBuilder.loadTexts:
    mGuardExternRoutesTable.setStatus("mandatory")
_MGuardExternRoutesEntry_Object = MibTableRow
mGuardExternRoutesEntry = _MGuardExternRoutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 2, 2, 6, 1)
)
mGuardExternRoutesEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardExternRouteIndex"),
)
if mibBuilder.loadTexts:
    mGuardExternRoutesEntry.setStatus("mandatory")


class _MGuardExternRouteIndex_Type(Integer32):
    """Custom type mGuardExternRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardExternRouteIndex_Type.__name__ = "Integer32"
_MGuardExternRouteIndex_Object = MibTableColumn
mGuardExternRouteIndex = _MGuardExternRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 2, 2, 6, 1, 1),
    _MGuardExternRouteIndex_Type()
)
mGuardExternRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardExternRouteIndex.setStatus("mandatory")
_MGuardExternRouteNetwork_Type = DisplayString
_MGuardExternRouteNetwork_Object = MibTableColumn
mGuardExternRouteNetwork = _MGuardExternRouteNetwork_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 2, 2, 6, 1, 2),
    _MGuardExternRouteNetwork_Type()
)
mGuardExternRouteNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardExternRouteNetwork.setStatus("mandatory")
_MGuardExternRouteGateway_Type = IpAddress
_MGuardExternRouteGateway_Object = MibTableColumn
mGuardExternRouteGateway = _MGuardExternRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 2, 2, 6, 1, 3),
    _MGuardExternRouteGateway_Type()
)
mGuardExternRouteGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardExternRouteGateway.setStatus("mandatory")
_MGuardExternRouteRowStatus_Type = RowStatus
_MGuardExternRouteRowStatus_Object = MibTableColumn
mGuardExternRouteRowStatus = _MGuardExternRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 2, 2, 6, 1, 4),
    _MGuardExternRouteRowStatus_Type()
)
mGuardExternRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardExternRouteRowStatus.setStatus("mandatory")
_MGuardRouterExternDevMTU_Type = Integer32
_MGuardRouterExternDevMTU_Object = MibScalar
mGuardRouterExternDevMTU = _MGuardRouterExternDevMTU_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 2, 6),
    _MGuardRouterExternDevMTU_Type()
)
mGuardRouterExternDevMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterExternDevMTU.setStatus("mandatory")


class _MGuardRouterExternUseVLAN_Type(Integer32):
    """Custom type mGuardRouterExternUseVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardRouterExternUseVLAN_Type.__name__ = "Integer32"
_MGuardRouterExternUseVLAN_Object = MibScalar
mGuardRouterExternUseVLAN = _MGuardRouterExternUseVLAN_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 2, 7),
    _MGuardRouterExternUseVLAN_Type()
)
mGuardRouterExternUseVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterExternUseVLAN.setStatus("mandatory")
_MGuardRouterExternVlanId_Type = Integer32
_MGuardRouterExternVlanId_Object = MibScalar
mGuardRouterExternVlanId = _MGuardRouterExternVlanId_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 2, 8),
    _MGuardRouterExternVlanId_Type()
)
mGuardRouterExternVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterExternVlanId.setStatus("mandatory")
_MGuardRouterExternDevVlanMTU_Type = Integer32
_MGuardRouterExternDevVlanMTU_Object = MibScalar
mGuardRouterExternDevVlanMTU = _MGuardRouterExternDevVlanMTU_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 2, 9),
    _MGuardRouterExternDevVlanMTU_Type()
)
mGuardRouterExternDevVlanMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterExternDevVlanMTU.setStatus("mandatory")
_MGuardRouterHiDiscovery_ObjectIdentity = ObjectIdentity
mGuardRouterHiDiscovery = _MGuardRouterHiDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 3)
)


class _MGuardRouterHiDiscoveryIntern_Type(Integer32):
    """Custom type mGuardRouterHiDiscoveryIntern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("readonly", 3),
          ("readwrite", 1))
    )


_MGuardRouterHiDiscoveryIntern_Type.__name__ = "Integer32"
_MGuardRouterHiDiscoveryIntern_Object = MibScalar
mGuardRouterHiDiscoveryIntern = _MGuardRouterHiDiscoveryIntern_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 3, 1),
    _MGuardRouterHiDiscoveryIntern_Type()
)
mGuardRouterHiDiscoveryIntern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterHiDiscoveryIntern.setStatus("mandatory")


class _MGuardRouterHiDiscoveryExtern_Type(Integer32):
    """Custom type mGuardRouterHiDiscoveryExtern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("readonly", 3),
          ("readwrite", 1))
    )


_MGuardRouterHiDiscoveryExtern_Type.__name__ = "Integer32"
_MGuardRouterHiDiscoveryExtern_Object = MibScalar
mGuardRouterHiDiscoveryExtern = _MGuardRouterHiDiscoveryExtern_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 3, 3, 2),
    _MGuardRouterHiDiscoveryExtern_Type()
)
mGuardRouterHiDiscoveryExtern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterHiDiscoveryExtern.setStatus("mandatory")
_MGuardPPPOE_ObjectIdentity = ObjectIdentity
mGuardPPPOE = _MGuardPPPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 4)
)
_MGuardPPPOELogin_Type = DisplayString
_MGuardPPPOELogin_Object = MibScalar
mGuardPPPOELogin = _MGuardPPPOELogin_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 4, 1),
    _MGuardPPPOELogin_Type()
)
mGuardPPPOELogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardPPPOELogin.setStatus("mandatory")
_MGuardPPPOEPasswd_Type = DisplayString
_MGuardPPPOEPasswd_Object = MibScalar
mGuardPPPOEPasswd = _MGuardPPPOEPasswd_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 4, 2),
    _MGuardPPPOEPasswd_Type()
)
mGuardPPPOEPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardPPPOEPasswd.setStatus("mandatory")
_MGuardPPPOEMSS_Type = DisplayString
_MGuardPPPOEMSS_Object = MibScalar
mGuardPPPOEMSS = _MGuardPPPOEMSS_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 4, 3),
    _MGuardPPPOEMSS_Type()
)
mGuardPPPOEMSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardPPPOEMSS.setStatus("mandatory")
_MGuardPPPOEServiceName_Type = DisplayString
_MGuardPPPOEServiceName_Object = MibScalar
mGuardPPPOEServiceName = _MGuardPPPOEServiceName_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 4, 4),
    _MGuardPPPOEServiceName_Type()
)
mGuardPPPOEServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardPPPOEServiceName.setStatus("obsolete")
_MGuardPPPOEAccessConcentName_Type = DisplayString
_MGuardPPPOEAccessConcentName_Object = MibScalar
mGuardPPPOEAccessConcentName = _MGuardPPPOEAccessConcentName_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 4, 5),
    _MGuardPPPOEAccessConcentName_Type()
)
mGuardPPPOEAccessConcentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardPPPOEAccessConcentName.setStatus("obsolete")


class _MGuardPPPOEHostUnique_Type(Integer32):
    """Custom type mGuardPPPOEHostUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MGuardPPPOEHostUnique_Type.__name__ = "Integer32"
_MGuardPPPOEHostUnique_Object = MibScalar
mGuardPPPOEHostUnique = _MGuardPPPOEHostUnique_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 4, 6),
    _MGuardPPPOEHostUnique_Type()
)
mGuardPPPOEHostUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardPPPOEHostUnique.setStatus("obsolete")
_MGuardPPPOEpppdOptionsTable_Object = MibTable
mGuardPPPOEpppdOptionsTable = _MGuardPPPOEpppdOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 4, 7)
)
if mibBuilder.loadTexts:
    mGuardPPPOEpppdOptionsTable.setStatus("mandatory")
_MGuardPPPOEpppdOptionsEntry_Object = MibTableRow
mGuardPPPOEpppdOptionsEntry = _MGuardPPPOEpppdOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 4, 7, 1)
)
mGuardPPPOEpppdOptionsEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardPPPOEpppdOptionsIndex"),
)
if mibBuilder.loadTexts:
    mGuardPPPOEpppdOptionsEntry.setStatus("mandatory")


class _MGuardPPPOEpppdOptionsIndex_Type(Integer32):
    """Custom type mGuardPPPOEpppdOptionsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardPPPOEpppdOptionsIndex_Type.__name__ = "Integer32"
_MGuardPPPOEpppdOptionsIndex_Object = MibTableColumn
mGuardPPPOEpppdOptionsIndex = _MGuardPPPOEpppdOptionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 4, 7, 1, 1),
    _MGuardPPPOEpppdOptionsIndex_Type()
)
mGuardPPPOEpppdOptionsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardPPPOEpppdOptionsIndex.setStatus("mandatory")
_MGuardPPPOEpppdOptionsValue_Type = DisplayString
_MGuardPPPOEpppdOptionsValue_Object = MibTableColumn
mGuardPPPOEpppdOptionsValue = _MGuardPPPOEpppdOptionsValue_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 4, 7, 1, 2),
    _MGuardPPPOEpppdOptionsValue_Type()
)
mGuardPPPOEpppdOptionsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardPPPOEpppdOptionsValue.setStatus("mandatory")
_MGuardPPPOEpppdOptionsRowStatus_Type = RowStatus
_MGuardPPPOEpppdOptionsRowStatus_Object = MibTableColumn
mGuardPPPOEpppdOptionsRowStatus = _MGuardPPPOEpppdOptionsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 4, 7, 1, 3),
    _MGuardPPPOEpppdOptionsRowStatus_Type()
)
mGuardPPPOEpppdOptionsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardPPPOEpppdOptionsRowStatus.setStatus("mandatory")
_MGuardDHCP_ObjectIdentity = ObjectIdentity
mGuardDHCP = _MGuardDHCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5)
)
_MGuardDHCPInt_ObjectIdentity = ObjectIdentity
mGuardDHCPInt = _MGuardDHCPInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1)
)


class _MGuardDHCPIntStart_Type(Integer32):
    """Custom type mGuardDHCPIntStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("enabled-relay", 3))
    )


_MGuardDHCPIntStart_Type.__name__ = "Integer32"
_MGuardDHCPIntStart_Object = MibScalar
mGuardDHCPIntStart = _MGuardDHCPIntStart_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 1),
    _MGuardDHCPIntStart_Type()
)
mGuardDHCPIntStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPIntStart.setStatus("mandatory")


class _MGuardDHCPIntPoolEnable_Type(Integer32):
    """Custom type mGuardDHCPIntPoolEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MGuardDHCPIntPoolEnable_Type.__name__ = "Integer32"
_MGuardDHCPIntPoolEnable_Object = MibScalar
mGuardDHCPIntPoolEnable = _MGuardDHCPIntPoolEnable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 2),
    _MGuardDHCPIntPoolEnable_Type()
)
mGuardDHCPIntPoolEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPIntPoolEnable.setStatus("mandatory")
_MGuardDHCPIntRangeStart_Type = IpAddress
_MGuardDHCPIntRangeStart_Object = MibScalar
mGuardDHCPIntRangeStart = _MGuardDHCPIntRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 3),
    _MGuardDHCPIntRangeStart_Type()
)
mGuardDHCPIntRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPIntRangeStart.setStatus("mandatory")
_MGuardDHCPIntRangeEnd_Type = IpAddress
_MGuardDHCPIntRangeEnd_Object = MibScalar
mGuardDHCPIntRangeEnd = _MGuardDHCPIntRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 4),
    _MGuardDHCPIntRangeEnd_Type()
)
mGuardDHCPIntRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPIntRangeEnd.setStatus("mandatory")
_MGuardDHCPIntNetmask_Type = IpAddress
_MGuardDHCPIntNetmask_Object = MibScalar
mGuardDHCPIntNetmask = _MGuardDHCPIntNetmask_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 5),
    _MGuardDHCPIntNetmask_Type()
)
mGuardDHCPIntNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPIntNetmask.setStatus("mandatory")
_MGuardDHCPIntGateway_Type = IpAddress
_MGuardDHCPIntGateway_Object = MibScalar
mGuardDHCPIntGateway = _MGuardDHCPIntGateway_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 6),
    _MGuardDHCPIntGateway_Type()
)
mGuardDHCPIntGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPIntGateway.setStatus("mandatory")
_MGuardDHCPIntDnsServer_Type = IpAddress
_MGuardDHCPIntDnsServer_Object = MibScalar
mGuardDHCPIntDnsServer = _MGuardDHCPIntDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 7),
    _MGuardDHCPIntDnsServer_Type()
)
mGuardDHCPIntDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPIntDnsServer.setStatus("mandatory")
_MGuardDHCPIntStaticTable_Object = MibTable
mGuardDHCPIntStaticTable = _MGuardDHCPIntStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 8)
)
if mibBuilder.loadTexts:
    mGuardDHCPIntStaticTable.setStatus("mandatory")
_MGuardDHCPIntStaticEntry_Object = MibTableRow
mGuardDHCPIntStaticEntry = _MGuardDHCPIntStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 8, 1)
)
mGuardDHCPIntStaticEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardDHCPIntStaticIndex"),
)
if mibBuilder.loadTexts:
    mGuardDHCPIntStaticEntry.setStatus("mandatory")


class _MGuardDHCPIntStaticIndex_Type(Integer32):
    """Custom type mGuardDHCPIntStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_MGuardDHCPIntStaticIndex_Type.__name__ = "Integer32"
_MGuardDHCPIntStaticIndex_Object = MibTableColumn
mGuardDHCPIntStaticIndex = _MGuardDHCPIntStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 8, 1, 1),
    _MGuardDHCPIntStaticIndex_Type()
)
mGuardDHCPIntStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardDHCPIntStaticIndex.setStatus("mandatory")
_MGuardDHCPIntStaticMAC_Type = MacAddress
_MGuardDHCPIntStaticMAC_Object = MibTableColumn
mGuardDHCPIntStaticMAC = _MGuardDHCPIntStaticMAC_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 8, 1, 2),
    _MGuardDHCPIntStaticMAC_Type()
)
mGuardDHCPIntStaticMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPIntStaticMAC.setStatus("mandatory")
_MGuardDHCPIntStaticIP_Type = IpAddress
_MGuardDHCPIntStaticIP_Object = MibTableColumn
mGuardDHCPIntStaticIP = _MGuardDHCPIntStaticIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 8, 1, 3),
    _MGuardDHCPIntStaticIP_Type()
)
mGuardDHCPIntStaticIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPIntStaticIP.setStatus("mandatory")
_MGuardDHCPIntStaticRowStatus_Type = RowStatus
_MGuardDHCPIntStaticRowStatus_Object = MibTableColumn
mGuardDHCPIntStaticRowStatus = _MGuardDHCPIntStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 8, 1, 4),
    _MGuardDHCPIntStaticRowStatus_Type()
)
mGuardDHCPIntStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPIntStaticRowStatus.setStatus("mandatory")
_MGuardDHCPIntBroadcast_Type = IpAddress
_MGuardDHCPIntBroadcast_Object = MibScalar
mGuardDHCPIntBroadcast = _MGuardDHCPIntBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 9),
    _MGuardDHCPIntBroadcast_Type()
)
mGuardDHCPIntBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPIntBroadcast.setStatus("mandatory")
_MGuardDHCPIntWINS_Type = IpAddress
_MGuardDHCPIntWINS_Object = MibScalar
mGuardDHCPIntWINS = _MGuardDHCPIntWINS_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 10),
    _MGuardDHCPIntWINS_Type()
)
mGuardDHCPIntWINS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPIntWINS.setStatus("mandatory")
_MGuardDHCPIntLeaseTime_Type = Integer32
_MGuardDHCPIntLeaseTime_Object = MibScalar
mGuardDHCPIntLeaseTime = _MGuardDHCPIntLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 11),
    _MGuardDHCPIntLeaseTime_Type()
)
mGuardDHCPIntLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPIntLeaseTime.setStatus("mandatory")
_MGuardDHCPIntRelayServerTable_Object = MibTable
mGuardDHCPIntRelayServerTable = _MGuardDHCPIntRelayServerTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 50)
)
if mibBuilder.loadTexts:
    mGuardDHCPIntRelayServerTable.setStatus("mandatory")
_MGuardDHCPIntRelayServerEntry_Object = MibTableRow
mGuardDHCPIntRelayServerEntry = _MGuardDHCPIntRelayServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 50, 1)
)
mGuardDHCPIntRelayServerEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardDHCPIntRelayServerIndex"),
)
if mibBuilder.loadTexts:
    mGuardDHCPIntRelayServerEntry.setStatus("mandatory")


class _MGuardDHCPIntRelayServerIndex_Type(Integer32):
    """Custom type mGuardDHCPIntRelayServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardDHCPIntRelayServerIndex_Type.__name__ = "Integer32"
_MGuardDHCPIntRelayServerIndex_Object = MibTableColumn
mGuardDHCPIntRelayServerIndex = _MGuardDHCPIntRelayServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 50, 1, 1),
    _MGuardDHCPIntRelayServerIndex_Type()
)
mGuardDHCPIntRelayServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardDHCPIntRelayServerIndex.setStatus("mandatory")
_MGuardDHCPIntRelayServerIP_Type = IpAddress
_MGuardDHCPIntRelayServerIP_Object = MibTableColumn
mGuardDHCPIntRelayServerIP = _MGuardDHCPIntRelayServerIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 50, 1, 2),
    _MGuardDHCPIntRelayServerIP_Type()
)
mGuardDHCPIntRelayServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPIntRelayServerIP.setStatus("mandatory")
_MGuardDHCPIntRelayRowStatus_Type = RowStatus
_MGuardDHCPIntRelayRowStatus_Object = MibTableColumn
mGuardDHCPIntRelayRowStatus = _MGuardDHCPIntRelayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 50, 1, 10),
    _MGuardDHCPIntRelayRowStatus_Type()
)
mGuardDHCPIntRelayRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPIntRelayRowStatus.setStatus("mandatory")
_MGuardDHCPIntRelayMaxHop_Type = Integer32
_MGuardDHCPIntRelayMaxHop_Object = MibScalar
mGuardDHCPIntRelayMaxHop = _MGuardDHCPIntRelayMaxHop_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 51),
    _MGuardDHCPIntRelayMaxHop_Type()
)
mGuardDHCPIntRelayMaxHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPIntRelayMaxHop.setStatus("mandatory")
_MGuardDHCPIntRelayAppend_Type = TruthValue
_MGuardDHCPIntRelayAppend_Object = MibScalar
mGuardDHCPIntRelayAppend = _MGuardDHCPIntRelayAppend_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 52),
    _MGuardDHCPIntRelayAppend_Type()
)
mGuardDHCPIntRelayAppend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPIntRelayAppend.setStatus("mandatory")
_MGuardDHCPIntRelayAppendLimit_Type = Integer32
_MGuardDHCPIntRelayAppendLimit_Object = MibScalar
mGuardDHCPIntRelayAppendLimit = _MGuardDHCPIntRelayAppendLimit_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 53),
    _MGuardDHCPIntRelayAppendLimit_Type()
)
mGuardDHCPIntRelayAppendLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPIntRelayAppendLimit.setStatus("mandatory")


class _MGuardDHCPIntRelayCircuitInfo_Type(Integer32):
    """Custom type mGuardDHCPIntRelayCircuitInfo based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("if-idx", 2),
          ("if-ip", 5),
          ("if-mac", 4),
          ("if-name", 3),
          ("if-prefixed-ip", 8),
          ("none", 1),
          ("rs2", 9),
          ("sysname", 6),
          ("text", 7))
    )


_MGuardDHCPIntRelayCircuitInfo_Type.__name__ = "Integer32"
_MGuardDHCPIntRelayCircuitInfo_Object = MibScalar
mGuardDHCPIntRelayCircuitInfo = _MGuardDHCPIntRelayCircuitInfo_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 54),
    _MGuardDHCPIntRelayCircuitInfo_Type()
)
mGuardDHCPIntRelayCircuitInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPIntRelayCircuitInfo.setStatus("mandatory")
_MGuardDHCPIntRelayCircuitText_Type = DisplayString
_MGuardDHCPIntRelayCircuitText_Object = MibScalar
mGuardDHCPIntRelayCircuitText = _MGuardDHCPIntRelayCircuitText_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 55),
    _MGuardDHCPIntRelayCircuitText_Type()
)
mGuardDHCPIntRelayCircuitText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPIntRelayCircuitText.setStatus("mandatory")


class _MGuardDHCPIntRelayRemoteInfo_Type(Integer32):
    """Custom type mGuardDHCPIntRelayRemoteInfo based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("if-idx", 2),
          ("if-ip", 5),
          ("if-mac", 4),
          ("if-name", 3),
          ("if-prefixed-ip", 8),
          ("none", 1),
          ("rs2", 9),
          ("sysname", 6),
          ("text", 7))
    )


_MGuardDHCPIntRelayRemoteInfo_Type.__name__ = "Integer32"
_MGuardDHCPIntRelayRemoteInfo_Object = MibScalar
mGuardDHCPIntRelayRemoteInfo = _MGuardDHCPIntRelayRemoteInfo_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 56),
    _MGuardDHCPIntRelayRemoteInfo_Type()
)
mGuardDHCPIntRelayRemoteInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPIntRelayRemoteInfo.setStatus("mandatory")
_MGuardDHCPIntRelayRemoteText_Type = DisplayString
_MGuardDHCPIntRelayRemoteText_Object = MibScalar
mGuardDHCPIntRelayRemoteText = _MGuardDHCPIntRelayRemoteText_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 1, 57),
    _MGuardDHCPIntRelayRemoteText_Type()
)
mGuardDHCPIntRelayRemoteText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPIntRelayRemoteText.setStatus("mandatory")
_MGuardDHCPExt_ObjectIdentity = ObjectIdentity
mGuardDHCPExt = _MGuardDHCPExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2)
)


class _MGuardDHCPExtStart_Type(Integer32):
    """Custom type mGuardDHCPExtStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("enabled-relay", 3))
    )


_MGuardDHCPExtStart_Type.__name__ = "Integer32"
_MGuardDHCPExtStart_Object = MibScalar
mGuardDHCPExtStart = _MGuardDHCPExtStart_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 1),
    _MGuardDHCPExtStart_Type()
)
mGuardDHCPExtStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPExtStart.setStatus("mandatory")


class _MGuardDHCPExtPoolEnable_Type(Integer32):
    """Custom type mGuardDHCPExtPoolEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MGuardDHCPExtPoolEnable_Type.__name__ = "Integer32"
_MGuardDHCPExtPoolEnable_Object = MibScalar
mGuardDHCPExtPoolEnable = _MGuardDHCPExtPoolEnable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 2),
    _MGuardDHCPExtPoolEnable_Type()
)
mGuardDHCPExtPoolEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPExtPoolEnable.setStatus("mandatory")
_MGuardDHCPExtRangeStart_Type = IpAddress
_MGuardDHCPExtRangeStart_Object = MibScalar
mGuardDHCPExtRangeStart = _MGuardDHCPExtRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 3),
    _MGuardDHCPExtRangeStart_Type()
)
mGuardDHCPExtRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPExtRangeStart.setStatus("mandatory")
_MGuardDHCPExtRangeEnd_Type = IpAddress
_MGuardDHCPExtRangeEnd_Object = MibScalar
mGuardDHCPExtRangeEnd = _MGuardDHCPExtRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 4),
    _MGuardDHCPExtRangeEnd_Type()
)
mGuardDHCPExtRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPExtRangeEnd.setStatus("mandatory")
_MGuardDHCPExtNetmask_Type = IpAddress
_MGuardDHCPExtNetmask_Object = MibScalar
mGuardDHCPExtNetmask = _MGuardDHCPExtNetmask_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 5),
    _MGuardDHCPExtNetmask_Type()
)
mGuardDHCPExtNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPExtNetmask.setStatus("mandatory")
_MGuardDHCPExtGateway_Type = IpAddress
_MGuardDHCPExtGateway_Object = MibScalar
mGuardDHCPExtGateway = _MGuardDHCPExtGateway_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 6),
    _MGuardDHCPExtGateway_Type()
)
mGuardDHCPExtGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPExtGateway.setStatus("mandatory")
_MGuardDHCPExtDnsServer_Type = IpAddress
_MGuardDHCPExtDnsServer_Object = MibScalar
mGuardDHCPExtDnsServer = _MGuardDHCPExtDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 7),
    _MGuardDHCPExtDnsServer_Type()
)
mGuardDHCPExtDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPExtDnsServer.setStatus("mandatory")
_MGuardDHCPExtStaticTable_Object = MibTable
mGuardDHCPExtStaticTable = _MGuardDHCPExtStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 8)
)
if mibBuilder.loadTexts:
    mGuardDHCPExtStaticTable.setStatus("mandatory")
_MGuardDHCPExtStaticEntry_Object = MibTableRow
mGuardDHCPExtStaticEntry = _MGuardDHCPExtStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 8, 1)
)
mGuardDHCPExtStaticEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardDHCPExtStaticIndex"),
)
if mibBuilder.loadTexts:
    mGuardDHCPExtStaticEntry.setStatus("mandatory")


class _MGuardDHCPExtStaticIndex_Type(Integer32):
    """Custom type mGuardDHCPExtStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_MGuardDHCPExtStaticIndex_Type.__name__ = "Integer32"
_MGuardDHCPExtStaticIndex_Object = MibTableColumn
mGuardDHCPExtStaticIndex = _MGuardDHCPExtStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 8, 1, 1),
    _MGuardDHCPExtStaticIndex_Type()
)
mGuardDHCPExtStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardDHCPExtStaticIndex.setStatus("mandatory")
_MGuardDHCPExtStaticMAC_Type = MacAddress
_MGuardDHCPExtStaticMAC_Object = MibTableColumn
mGuardDHCPExtStaticMAC = _MGuardDHCPExtStaticMAC_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 8, 1, 2),
    _MGuardDHCPExtStaticMAC_Type()
)
mGuardDHCPExtStaticMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPExtStaticMAC.setStatus("mandatory")
_MGuardDHCPExtStaticIP_Type = IpAddress
_MGuardDHCPExtStaticIP_Object = MibTableColumn
mGuardDHCPExtStaticIP = _MGuardDHCPExtStaticIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 8, 1, 3),
    _MGuardDHCPExtStaticIP_Type()
)
mGuardDHCPExtStaticIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPExtStaticIP.setStatus("mandatory")
_MGuardDHCPExtStaticRowStatus_Type = RowStatus
_MGuardDHCPExtStaticRowStatus_Object = MibTableColumn
mGuardDHCPExtStaticRowStatus = _MGuardDHCPExtStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 8, 1, 4),
    _MGuardDHCPExtStaticRowStatus_Type()
)
mGuardDHCPExtStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPExtStaticRowStatus.setStatus("mandatory")
_MGuardDHCPExtBroadcast_Type = IpAddress
_MGuardDHCPExtBroadcast_Object = MibScalar
mGuardDHCPExtBroadcast = _MGuardDHCPExtBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 9),
    _MGuardDHCPExtBroadcast_Type()
)
mGuardDHCPExtBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPExtBroadcast.setStatus("mandatory")
_MGuardDHCPExtWINS_Type = IpAddress
_MGuardDHCPExtWINS_Object = MibScalar
mGuardDHCPExtWINS = _MGuardDHCPExtWINS_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 10),
    _MGuardDHCPExtWINS_Type()
)
mGuardDHCPExtWINS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPExtWINS.setStatus("mandatory")
_MGuardDHCPExtLeaseTime_Type = Integer32
_MGuardDHCPExtLeaseTime_Object = MibScalar
mGuardDHCPExtLeaseTime = _MGuardDHCPExtLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 11),
    _MGuardDHCPExtLeaseTime_Type()
)
mGuardDHCPExtLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPExtLeaseTime.setStatus("mandatory")
_MGuardDHCPExtRelayServerTable_Object = MibTable
mGuardDHCPExtRelayServerTable = _MGuardDHCPExtRelayServerTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 50)
)
if mibBuilder.loadTexts:
    mGuardDHCPExtRelayServerTable.setStatus("mandatory")
_MGuardDHCPExtRelayServerEntry_Object = MibTableRow
mGuardDHCPExtRelayServerEntry = _MGuardDHCPExtRelayServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 50, 1)
)
mGuardDHCPExtRelayServerEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardDHCPExtRelayServerIndex"),
)
if mibBuilder.loadTexts:
    mGuardDHCPExtRelayServerEntry.setStatus("mandatory")


class _MGuardDHCPExtRelayServerIndex_Type(Integer32):
    """Custom type mGuardDHCPExtRelayServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardDHCPExtRelayServerIndex_Type.__name__ = "Integer32"
_MGuardDHCPExtRelayServerIndex_Object = MibTableColumn
mGuardDHCPExtRelayServerIndex = _MGuardDHCPExtRelayServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 50, 1, 1),
    _MGuardDHCPExtRelayServerIndex_Type()
)
mGuardDHCPExtRelayServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardDHCPExtRelayServerIndex.setStatus("mandatory")
_MGuardDHCPExtRelayServerIP_Type = IpAddress
_MGuardDHCPExtRelayServerIP_Object = MibTableColumn
mGuardDHCPExtRelayServerIP = _MGuardDHCPExtRelayServerIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 50, 1, 2),
    _MGuardDHCPExtRelayServerIP_Type()
)
mGuardDHCPExtRelayServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPExtRelayServerIP.setStatus("mandatory")
_MGuardDHCPExtRelayRowStatus_Type = RowStatus
_MGuardDHCPExtRelayRowStatus_Object = MibTableColumn
mGuardDHCPExtRelayRowStatus = _MGuardDHCPExtRelayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 50, 1, 10),
    _MGuardDHCPExtRelayRowStatus_Type()
)
mGuardDHCPExtRelayRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPExtRelayRowStatus.setStatus("mandatory")
_MGuardDHCPExtRelayMaxHop_Type = Integer32
_MGuardDHCPExtRelayMaxHop_Object = MibScalar
mGuardDHCPExtRelayMaxHop = _MGuardDHCPExtRelayMaxHop_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 51),
    _MGuardDHCPExtRelayMaxHop_Type()
)
mGuardDHCPExtRelayMaxHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPExtRelayMaxHop.setStatus("mandatory")
_MGuardDHCPExtRelayAppend_Type = TruthValue
_MGuardDHCPExtRelayAppend_Object = MibScalar
mGuardDHCPExtRelayAppend = _MGuardDHCPExtRelayAppend_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 52),
    _MGuardDHCPExtRelayAppend_Type()
)
mGuardDHCPExtRelayAppend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPExtRelayAppend.setStatus("mandatory")
_MGuardDHCPExtRelayAppendLimit_Type = Integer32
_MGuardDHCPExtRelayAppendLimit_Object = MibScalar
mGuardDHCPExtRelayAppendLimit = _MGuardDHCPExtRelayAppendLimit_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 53),
    _MGuardDHCPExtRelayAppendLimit_Type()
)
mGuardDHCPExtRelayAppendLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPExtRelayAppendLimit.setStatus("mandatory")


class _MGuardDHCPExtRelayCircuitInfo_Type(Integer32):
    """Custom type mGuardDHCPExtRelayCircuitInfo based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("if-idx", 2),
          ("if-ip", 5),
          ("if-mac", 4),
          ("if-name", 3),
          ("if-prefixed-ip", 8),
          ("none", 1),
          ("rs2", 9),
          ("sysname", 6),
          ("text", 7))
    )


_MGuardDHCPExtRelayCircuitInfo_Type.__name__ = "Integer32"
_MGuardDHCPExtRelayCircuitInfo_Object = MibScalar
mGuardDHCPExtRelayCircuitInfo = _MGuardDHCPExtRelayCircuitInfo_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 54),
    _MGuardDHCPExtRelayCircuitInfo_Type()
)
mGuardDHCPExtRelayCircuitInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPExtRelayCircuitInfo.setStatus("mandatory")
_MGuardDHCPExtRelayCircuitText_Type = DisplayString
_MGuardDHCPExtRelayCircuitText_Object = MibScalar
mGuardDHCPExtRelayCircuitText = _MGuardDHCPExtRelayCircuitText_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 55),
    _MGuardDHCPExtRelayCircuitText_Type()
)
mGuardDHCPExtRelayCircuitText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPExtRelayCircuitText.setStatus("mandatory")


class _MGuardDHCPExtRelayRemoteInfo_Type(Integer32):
    """Custom type mGuardDHCPExtRelayRemoteInfo based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("if-idx", 2),
          ("if-ip", 5),
          ("if-mac", 4),
          ("if-name", 3),
          ("if-prefixed-ip", 8),
          ("none", 1),
          ("rs2", 9),
          ("sysname", 6),
          ("text", 7))
    )


_MGuardDHCPExtRelayRemoteInfo_Type.__name__ = "Integer32"
_MGuardDHCPExtRelayRemoteInfo_Object = MibScalar
mGuardDHCPExtRelayRemoteInfo = _MGuardDHCPExtRelayRemoteInfo_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 56),
    _MGuardDHCPExtRelayRemoteInfo_Type()
)
mGuardDHCPExtRelayRemoteInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPExtRelayRemoteInfo.setStatus("mandatory")
_MGuardDHCPExtRelayRemoteText_Type = DisplayString
_MGuardDHCPExtRelayRemoteText_Object = MibScalar
mGuardDHCPExtRelayRemoteText = _MGuardDHCPExtRelayRemoteText_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 5, 2, 57),
    _MGuardDHCPExtRelayRemoteText_Type()
)
mGuardDHCPExtRelayRemoteText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDHCPExtRelayRemoteText.setStatus("mandatory")
_MGuardDNS_ObjectIdentity = ObjectIdentity
mGuardDNS = _MGuardDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 6)
)
_MGuardDNSSearchPath_Type = DisplayString
_MGuardDNSSearchPath_Object = MibScalar
mGuardDNSSearchPath = _MGuardDNSSearchPath_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 6, 1),
    _MGuardDNSSearchPath_Type()
)
mGuardDNSSearchPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDNSSearchPath.setStatus("mandatory")


class _MGuardDNSServerType_Type(Integer32):
    """Custom type mGuardDNSServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("provider", 2),
          ("root", 1),
          ("user", 3))
    )


_MGuardDNSServerType_Type.__name__ = "Integer32"
_MGuardDNSServerType_Object = MibScalar
mGuardDNSServerType = _MGuardDNSServerType_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 6, 2),
    _MGuardDNSServerType_Type()
)
mGuardDNSServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDNSServerType.setStatus("mandatory")
_MGuardDNSUserDefinedServerTable_Object = MibTable
mGuardDNSUserDefinedServerTable = _MGuardDNSUserDefinedServerTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 6, 3)
)
if mibBuilder.loadTexts:
    mGuardDNSUserDefinedServerTable.setStatus("mandatory")
_MGuardDNSUserDefinedServerEntry_Object = MibTableRow
mGuardDNSUserDefinedServerEntry = _MGuardDNSUserDefinedServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 6, 3, 1)
)
mGuardDNSUserDefinedServerEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuarddnsServerIndex"),
)
if mibBuilder.loadTexts:
    mGuardDNSUserDefinedServerEntry.setStatus("mandatory")


class _MGuarddnsServerIndex_Type(Integer32):
    """Custom type mGuarddnsServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuarddnsServerIndex_Type.__name__ = "Integer32"
_MGuarddnsServerIndex_Object = MibTableColumn
mGuarddnsServerIndex = _MGuarddnsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 6, 3, 1, 1),
    _MGuarddnsServerIndex_Type()
)
mGuarddnsServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuarddnsServerIndex.setStatus("mandatory")
_MGuarddnsServerIP_Type = IpAddress
_MGuarddnsServerIP_Object = MibTableColumn
mGuarddnsServerIP = _MGuarddnsServerIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 6, 3, 1, 2),
    _MGuarddnsServerIP_Type()
)
mGuarddnsServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuarddnsServerIP.setStatus("mandatory")
_MGuarddnsServerRowStatus_Type = RowStatus
_MGuarddnsServerRowStatus_Object = MibTableColumn
mGuarddnsServerRowStatus = _MGuarddnsServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 6, 3, 1, 3),
    _MGuarddnsServerRowStatus_Type()
)
mGuarddnsServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuarddnsServerRowStatus.setStatus("mandatory")


class _MGuardDNSCacheEnabled_Type(Integer32):
    """Custom type mGuardDNSCacheEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MGuardDNSCacheEnabled_Type.__name__ = "Integer32"
_MGuardDNSCacheEnabled_Object = MibScalar
mGuardDNSCacheEnabled = _MGuardDNSCacheEnabled_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 6, 4),
    _MGuardDNSCacheEnabled_Type()
)
mGuardDNSCacheEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardDNSCacheEnabled.setStatus("mandatory")
_MGuardNetworkStatus_ObjectIdentity = ObjectIdentity
mGuardNetworkStatus = _MGuardNetworkStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 7)
)
_MGuardNetworkStatMode_Type = DisplayString
_MGuardNetworkStatMode_Object = MibScalar
mGuardNetworkStatMode = _MGuardNetworkStatMode_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 7, 1),
    _MGuardNetworkStatMode_Type()
)
mGuardNetworkStatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardNetworkStatMode.setStatus("mandatory")
_MGuardNetworkStatExtIP_Type = DisplayString
_MGuardNetworkStatExtIP_Object = MibScalar
mGuardNetworkStatExtIP = _MGuardNetworkStatExtIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 7, 2),
    _MGuardNetworkStatExtIP_Type()
)
mGuardNetworkStatExtIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardNetworkStatExtIP.setStatus("mandatory")
_MGuardNetworkStatGateway_Type = DisplayString
_MGuardNetworkStatGateway_Object = MibScalar
mGuardNetworkStatGateway = _MGuardNetworkStatGateway_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 7, 3),
    _MGuardNetworkStatGateway_Type()
)
mGuardNetworkStatGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardNetworkStatGateway.setStatus("mandatory")
_MGuardNetworkStatVPN_Type = DisplayString
_MGuardNetworkStatVPN_Object = MibScalar
mGuardNetworkStatVPN = _MGuardNetworkStatVPN_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 7, 4),
    _MGuardNetworkStatVPN_Type()
)
mGuardNetworkStatVPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardNetworkStatVPN.setStatus("mandatory")
_MGuardNetworkStatDynIPReg_Type = DisplayString
_MGuardNetworkStatDynIPReg_Object = MibScalar
mGuardNetworkStatDynIPReg = _MGuardNetworkStatDynIPReg_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 7, 5),
    _MGuardNetworkStatDynIPReg_Type()
)
mGuardNetworkStatDynIPReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardNetworkStatDynIPReg.setStatus("mandatory")
_MGuardNetworkStatHTTPSRemAccess_Type = DisplayString
_MGuardNetworkStatHTTPSRemAccess_Object = MibScalar
mGuardNetworkStatHTTPSRemAccess = _MGuardNetworkStatHTTPSRemAccess_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 7, 6),
    _MGuardNetworkStatHTTPSRemAccess_Type()
)
mGuardNetworkStatHTTPSRemAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardNetworkStatHTTPSRemAccess.setStatus("mandatory")
_MGuardNetworkStatSSHRemoteAccess_Type = DisplayString
_MGuardNetworkStatSSHRemoteAccess_Object = MibScalar
mGuardNetworkStatSSHRemoteAccess = _MGuardNetworkStatSSHRemoteAccess_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 7, 7),
    _MGuardNetworkStatSSHRemoteAccess_Type()
)
mGuardNetworkStatSSHRemoteAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardNetworkStatSSHRemoteAccess.setStatus("mandatory")
_MGuardNetworkSoftwareVersion_Type = DisplayString
_MGuardNetworkSoftwareVersion_Object = MibScalar
mGuardNetworkSoftwareVersion = _MGuardNetworkSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 7, 8),
    _MGuardNetworkSoftwareVersion_Type()
)
mGuardNetworkSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardNetworkSoftwareVersion.setStatus("mandatory")
_MGuardNetworkStatUptime_Type = DisplayString
_MGuardNetworkStatUptime_Object = MibScalar
mGuardNetworkStatUptime = _MGuardNetworkStatUptime_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 7, 9),
    _MGuardNetworkStatUptime_Type()
)
mGuardNetworkStatUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardNetworkStatUptime.setStatus("mandatory")
_MGuardNetworkStatLanguage_Type = DisplayString
_MGuardNetworkStatLanguage_Object = MibScalar
mGuardNetworkStatLanguage = _MGuardNetworkStatLanguage_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 7, 10),
    _MGuardNetworkStatLanguage_Type()
)
mGuardNetworkStatLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardNetworkStatLanguage.setStatus("mandatory")
_MGuardHostname_Type = DisplayString
_MGuardHostname_Object = MibScalar
mGuardHostname = _MGuardHostname_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 8),
    _MGuardHostname_Type()
)
mGuardHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardHostname.setStatus("mandatory")


class _MGuardHostnameMode_Type(Integer32):
    """Custom type mGuardHostnameMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("providerDefined", 2),
          ("userDefined", 1))
    )


_MGuardHostnameMode_Type.__name__ = "Integer32"
_MGuardHostnameMode_Object = MibScalar
mGuardHostnameMode = _MGuardHostnameMode_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 9),
    _MGuardHostnameMode_Type()
)
mGuardHostnameMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardHostnameMode.setStatus("mandatory")
_MGuardPPTP_ObjectIdentity = ObjectIdentity
mGuardPPTP = _MGuardPPTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 10)
)
_MGuardPPTPLogin_Type = DisplayString
_MGuardPPTPLogin_Object = MibScalar
mGuardPPTPLogin = _MGuardPPTPLogin_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 10, 1),
    _MGuardPPTPLogin_Type()
)
mGuardPPTPLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardPPTPLogin.setStatus("mandatory")
_MGuardPPTPassword_Type = DisplayString
_MGuardPPTPassword_Object = MibScalar
mGuardPPTPassword = _MGuardPPTPassword_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 10, 2),
    _MGuardPPTPassword_Type()
)
mGuardPPTPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardPPTPassword.setStatus("mandatory")


class _MGuardPPTPLocalIPMode_Type(Integer32):
    """Custom type mGuardPPTPLocalIPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 2),
          ("static", 1))
    )


_MGuardPPTPLocalIPMode_Type.__name__ = "Integer32"
_MGuardPPTPLocalIPMode_Object = MibScalar
mGuardPPTPLocalIPMode = _MGuardPPTPLocalIPMode_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 10, 3),
    _MGuardPPTPLocalIPMode_Type()
)
mGuardPPTPLocalIPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardPPTPLocalIPMode.setStatus("mandatory")
_MGuardPPTPLocalIP_Type = IpAddress
_MGuardPPTPLocalIP_Object = MibScalar
mGuardPPTPLocalIP = _MGuardPPTPLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 10, 4),
    _MGuardPPTPLocalIP_Type()
)
mGuardPPTPLocalIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardPPTPLocalIP.setStatus("mandatory")
_MGuardPPTPModemIP_Type = IpAddress
_MGuardPPTPModemIP_Object = MibScalar
mGuardPPTPModemIP = _MGuardPPTPModemIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 10, 5),
    _MGuardPPTPModemIP_Type()
)
mGuardPPTPModemIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardPPTPModemIP.setStatus("mandatory")
_MGuardPPTPpppdOptionsTable_Object = MibTable
mGuardPPTPpppdOptionsTable = _MGuardPPTPpppdOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 10, 6)
)
if mibBuilder.loadTexts:
    mGuardPPTPpppdOptionsTable.setStatus("mandatory")
_MGuardPPTPpppdOptionsEntry_Object = MibTableRow
mGuardPPTPpppdOptionsEntry = _MGuardPPTPpppdOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 10, 6, 1)
)
mGuardPPTPpppdOptionsEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardPPTPpppdOptionsIndex"),
)
if mibBuilder.loadTexts:
    mGuardPPTPpppdOptionsEntry.setStatus("mandatory")


class _MGuardPPTPpppdOptionsIndex_Type(Integer32):
    """Custom type mGuardPPTPpppdOptionsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardPPTPpppdOptionsIndex_Type.__name__ = "Integer32"
_MGuardPPTPpppdOptionsIndex_Object = MibTableColumn
mGuardPPTPpppdOptionsIndex = _MGuardPPTPpppdOptionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 10, 6, 1, 1),
    _MGuardPPTPpppdOptionsIndex_Type()
)
mGuardPPTPpppdOptionsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardPPTPpppdOptionsIndex.setStatus("mandatory")
_MGuardPPTPpppdOptionsValue_Type = DisplayString
_MGuardPPTPpppdOptionsValue_Object = MibTableColumn
mGuardPPTPpppdOptionsValue = _MGuardPPTPpppdOptionsValue_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 10, 6, 1, 2),
    _MGuardPPTPpppdOptionsValue_Type()
)
mGuardPPTPpppdOptionsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardPPTPpppdOptionsValue.setStatus("mandatory")
_MGuardPPTPpppdOptionsRowStatus_Type = RowStatus
_MGuardPPTPpppdOptionsRowStatus_Object = MibTableColumn
mGuardPPTPpppdOptionsRowStatus = _MGuardPPTPpppdOptionsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 10, 6, 1, 3),
    _MGuardPPTPpppdOptionsRowStatus_Type()
)
mGuardPPTPpppdOptionsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardPPTPpppdOptionsRowStatus.setStatus("mandatory")
_MGuardSerial_ObjectIdentity = ObjectIdentity
mGuardSerial = _MGuardSerial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11)
)
_MGuardSerialBaud_Type = Integer32
_MGuardSerialBaud_Object = MibScalar
mGuardSerialBaud = _MGuardSerialBaud_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 1),
    _MGuardSerialBaud_Type()
)
mGuardSerialBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialBaud.setStatus("mandatory")


class _MGuardSerialHWHandshakeEnable_Type(Integer32):
    """Custom type mGuardSerialHWHandshakeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MGuardSerialHWHandshakeEnable_Type.__name__ = "Integer32"
_MGuardSerialHWHandshakeEnable_Object = MibScalar
mGuardSerialHWHandshakeEnable = _MGuardSerialHWHandshakeEnable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 2),
    _MGuardSerialHWHandshakeEnable_Type()
)
mGuardSerialHWHandshakeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialHWHandshakeEnable.setStatus("mandatory")
_MGuardSerialPPP_ObjectIdentity = ObjectIdentity
mGuardSerialPPP = _MGuardSerialPPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3)
)


class _MGuardSerialPPPEnable_Type(Integer32):
    """Custom type mGuardSerialPPPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MGuardSerialPPPEnable_Type.__name__ = "Integer32"
_MGuardSerialPPPEnable_Object = MibScalar
mGuardSerialPPPEnable = _MGuardSerialPPPEnable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 1),
    _MGuardSerialPPPEnable_Type()
)
mGuardSerialPPPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialPPPEnable.setStatus("mandatory")
_MGuardSerialPPPLogin_Type = DisplayString
_MGuardSerialPPPLogin_Object = MibScalar
mGuardSerialPPPLogin = _MGuardSerialPPPLogin_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 2),
    _MGuardSerialPPPLogin_Type()
)
mGuardSerialPPPLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialPPPLogin.setStatus("mandatory")
_MGuardSerialPPPPasswd_Type = DisplayString
_MGuardSerialPPPPasswd_Object = MibScalar
mGuardSerialPPPPasswd = _MGuardSerialPPPPasswd_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 3),
    _MGuardSerialPPPPasswd_Type()
)
mGuardSerialPPPPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialPPPPasswd.setStatus("mandatory")
_MGuardSerialPPPLocalIP_Type = IpAddress
_MGuardSerialPPPLocalIP_Object = MibScalar
mGuardSerialPPPLocalIP = _MGuardSerialPPPLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 4),
    _MGuardSerialPPPLocalIP_Type()
)
mGuardSerialPPPLocalIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialPPPLocalIP.setStatus("mandatory")
_MGuardSerialPPPRemoteIP_Type = IpAddress
_MGuardSerialPPPRemoteIP_Object = MibScalar
mGuardSerialPPPRemoteIP = _MGuardSerialPPPRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 5),
    _MGuardSerialPPPRemoteIP_Type()
)
mGuardSerialPPPRemoteIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialPPPRemoteIP.setStatus("mandatory")
_MGuardSerialPPPFWIN_ObjectIdentity = ObjectIdentity
mGuardSerialPPPFWIN = _MGuardSerialPPPFWIN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 6)
)
_MGuardSerialPPPFWINTable_Object = MibTable
mGuardSerialPPPFWINTable = _MGuardSerialPPPFWINTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 6, 1)
)
if mibBuilder.loadTexts:
    mGuardSerialPPPFWINTable.setStatus("mandatory")
_MGuardSerialPPPFWINEntry_Object = MibTableRow
mGuardSerialPPPFWINEntry = _MGuardSerialPPPFWINEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 6, 1, 1)
)
mGuardSerialPPPFWINEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardFWINruleIndex"),
)
if mibBuilder.loadTexts:
    mGuardSerialPPPFWINEntry.setStatus("mandatory")


class _MGuardSerialPPPFWINruleIndex_Type(Integer32):
    """Custom type mGuardSerialPPPFWINruleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_MGuardSerialPPPFWINruleIndex_Type.__name__ = "Integer32"
_MGuardSerialPPPFWINruleIndex_Object = MibTableColumn
mGuardSerialPPPFWINruleIndex = _MGuardSerialPPPFWINruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 6, 1, 1, 1),
    _MGuardSerialPPPFWINruleIndex_Type()
)
mGuardSerialPPPFWINruleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardSerialPPPFWINruleIndex.setStatus("mandatory")
_MGuardSerialPPPFWINsourceIP_Type = DisplayString
_MGuardSerialPPPFWINsourceIP_Object = MibTableColumn
mGuardSerialPPPFWINsourceIP = _MGuardSerialPPPFWINsourceIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 6, 1, 1, 2),
    _MGuardSerialPPPFWINsourceIP_Type()
)
mGuardSerialPPPFWINsourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialPPPFWINsourceIP.setStatus("mandatory")
_MGuardSerialPPPFWINdestinationIP_Type = DisplayString
_MGuardSerialPPPFWINdestinationIP_Object = MibTableColumn
mGuardSerialPPPFWINdestinationIP = _MGuardSerialPPPFWINdestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 6, 1, 1, 3),
    _MGuardSerialPPPFWINdestinationIP_Type()
)
mGuardSerialPPPFWINdestinationIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialPPPFWINdestinationIP.setStatus("mandatory")
_MGuardSerialPPPFWINsport_Type = DisplayString
_MGuardSerialPPPFWINsport_Object = MibTableColumn
mGuardSerialPPPFWINsport = _MGuardSerialPPPFWINsport_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 6, 1, 1, 4),
    _MGuardSerialPPPFWINsport_Type()
)
mGuardSerialPPPFWINsport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialPPPFWINsport.setStatus("mandatory")
_MGuardSerialPPPFWINdport_Type = DisplayString
_MGuardSerialPPPFWINdport_Object = MibTableColumn
mGuardSerialPPPFWINdport = _MGuardSerialPPPFWINdport_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 6, 1, 1, 5),
    _MGuardSerialPPPFWINdport_Type()
)
mGuardSerialPPPFWINdport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialPPPFWINdport.setStatus("mandatory")


class _MGuardSerialPPPFWINtarget_Type(Integer32):
    """Custom type mGuardSerialPPPFWINtarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 3),
          ("reject", 2))
    )


_MGuardSerialPPPFWINtarget_Type.__name__ = "Integer32"
_MGuardSerialPPPFWINtarget_Object = MibTableColumn
mGuardSerialPPPFWINtarget = _MGuardSerialPPPFWINtarget_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 6, 1, 1, 6),
    _MGuardSerialPPPFWINtarget_Type()
)
mGuardSerialPPPFWINtarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialPPPFWINtarget.setStatus("mandatory")


class _MGuardSerialPPPFWINproto_Type(Integer32):
    """Custom type mGuardSerialPPPFWINproto based on Integer32"""
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
        *(("all", 4),
          ("icmp", 3),
          ("tcp", 1),
          ("udp", 2))
    )


_MGuardSerialPPPFWINproto_Type.__name__ = "Integer32"
_MGuardSerialPPPFWINproto_Object = MibTableColumn
mGuardSerialPPPFWINproto = _MGuardSerialPPPFWINproto_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 6, 1, 1, 7),
    _MGuardSerialPPPFWINproto_Type()
)
mGuardSerialPPPFWINproto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialPPPFWINproto.setStatus("mandatory")


class _MGuardSerialPPPFWINlog_Type(Integer32):
    """Custom type mGuardSerialPPPFWINlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardSerialPPPFWINlog_Type.__name__ = "Integer32"
_MGuardSerialPPPFWINlog_Object = MibTableColumn
mGuardSerialPPPFWINlog = _MGuardSerialPPPFWINlog_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 6, 1, 1, 8),
    _MGuardSerialPPPFWINlog_Type()
)
mGuardSerialPPPFWINlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialPPPFWINlog.setStatus("mandatory")
_MGuardSerialPPPFWINRowStatus_Type = RowStatus
_MGuardSerialPPPFWINRowStatus_Object = MibTableColumn
mGuardSerialPPPFWINRowStatus = _MGuardSerialPPPFWINRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 6, 1, 1, 9),
    _MGuardSerialPPPFWINRowStatus_Type()
)
mGuardSerialPPPFWINRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialPPPFWINRowStatus.setStatus("mandatory")
_MGuardSerialPPPFWINcomment_Type = DisplayString
_MGuardSerialPPPFWINcomment_Object = MibTableColumn
mGuardSerialPPPFWINcomment = _MGuardSerialPPPFWINcomment_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 6, 1, 1, 10),
    _MGuardSerialPPPFWINcomment_Type()
)
mGuardSerialPPPFWINcomment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialPPPFWINcomment.setStatus("mandatory")


class _MGuardSerialPPPFWINLogDefault_Type(Integer32):
    """Custom type mGuardSerialPPPFWINLogDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardSerialPPPFWINLogDefault_Type.__name__ = "Integer32"
_MGuardSerialPPPFWINLogDefault_Object = MibScalar
mGuardSerialPPPFWINLogDefault = _MGuardSerialPPPFWINLogDefault_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 6, 2),
    _MGuardSerialPPPFWINLogDefault_Type()
)
mGuardSerialPPPFWINLogDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialPPPFWINLogDefault.setStatus("mandatory")
_MGuardSerialPPPFWOUT_ObjectIdentity = ObjectIdentity
mGuardSerialPPPFWOUT = _MGuardSerialPPPFWOUT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 7)
)
_MGuardSerialPPPFWOUTTable_Object = MibTable
mGuardSerialPPPFWOUTTable = _MGuardSerialPPPFWOUTTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 7, 1)
)
if mibBuilder.loadTexts:
    mGuardSerialPPPFWOUTTable.setStatus("mandatory")
_MGuardSerialPPPFWOUTEntry_Object = MibTableRow
mGuardSerialPPPFWOUTEntry = _MGuardSerialPPPFWOUTEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 7, 1, 1)
)
mGuardSerialPPPFWOUTEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardSerialPPPFWOUTruleIndex"),
)
if mibBuilder.loadTexts:
    mGuardSerialPPPFWOUTEntry.setStatus("mandatory")


class _MGuardSerialPPPFWOUTruleIndex_Type(Integer32):
    """Custom type mGuardSerialPPPFWOUTruleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_MGuardSerialPPPFWOUTruleIndex_Type.__name__ = "Integer32"
_MGuardSerialPPPFWOUTruleIndex_Object = MibTableColumn
mGuardSerialPPPFWOUTruleIndex = _MGuardSerialPPPFWOUTruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 7, 1, 1, 1),
    _MGuardSerialPPPFWOUTruleIndex_Type()
)
mGuardSerialPPPFWOUTruleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardSerialPPPFWOUTruleIndex.setStatus("mandatory")
_MGuardSerialPPPFWOUTsourceIP_Type = DisplayString
_MGuardSerialPPPFWOUTsourceIP_Object = MibTableColumn
mGuardSerialPPPFWOUTsourceIP = _MGuardSerialPPPFWOUTsourceIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 7, 1, 1, 2),
    _MGuardSerialPPPFWOUTsourceIP_Type()
)
mGuardSerialPPPFWOUTsourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialPPPFWOUTsourceIP.setStatus("mandatory")
_MGuardSerialPPPFWOUTtargetIP_Type = DisplayString
_MGuardSerialPPPFWOUTtargetIP_Object = MibTableColumn
mGuardSerialPPPFWOUTtargetIP = _MGuardSerialPPPFWOUTtargetIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 7, 1, 1, 3),
    _MGuardSerialPPPFWOUTtargetIP_Type()
)
mGuardSerialPPPFWOUTtargetIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialPPPFWOUTtargetIP.setStatus("mandatory")
_MGuardSerialPPPFWOUTsport_Type = DisplayString
_MGuardSerialPPPFWOUTsport_Object = MibTableColumn
mGuardSerialPPPFWOUTsport = _MGuardSerialPPPFWOUTsport_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 7, 1, 1, 4),
    _MGuardSerialPPPFWOUTsport_Type()
)
mGuardSerialPPPFWOUTsport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialPPPFWOUTsport.setStatus("mandatory")
_MGuardSerialPPPFWOUTdport_Type = DisplayString
_MGuardSerialPPPFWOUTdport_Object = MibTableColumn
mGuardSerialPPPFWOUTdport = _MGuardSerialPPPFWOUTdport_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 7, 1, 1, 5),
    _MGuardSerialPPPFWOUTdport_Type()
)
mGuardSerialPPPFWOUTdport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialPPPFWOUTdport.setStatus("mandatory")


class _MGuardSerialPPPFWOUTtarget_Type(Integer32):
    """Custom type mGuardSerialPPPFWOUTtarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 3),
          ("reject", 2))
    )


_MGuardSerialPPPFWOUTtarget_Type.__name__ = "Integer32"
_MGuardSerialPPPFWOUTtarget_Object = MibTableColumn
mGuardSerialPPPFWOUTtarget = _MGuardSerialPPPFWOUTtarget_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 7, 1, 1, 6),
    _MGuardSerialPPPFWOUTtarget_Type()
)
mGuardSerialPPPFWOUTtarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialPPPFWOUTtarget.setStatus("mandatory")


class _MGuardSerialPPPFWOUTproto_Type(Integer32):
    """Custom type mGuardSerialPPPFWOUTproto based on Integer32"""
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
        *(("all", 4),
          ("icmp", 3),
          ("tcp", 1),
          ("udp", 2))
    )


_MGuardSerialPPPFWOUTproto_Type.__name__ = "Integer32"
_MGuardSerialPPPFWOUTproto_Object = MibTableColumn
mGuardSerialPPPFWOUTproto = _MGuardSerialPPPFWOUTproto_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 7, 1, 1, 7),
    _MGuardSerialPPPFWOUTproto_Type()
)
mGuardSerialPPPFWOUTproto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialPPPFWOUTproto.setStatus("mandatory")


class _MGuardSerialPPPFWOUTlog_Type(Integer32):
    """Custom type mGuardSerialPPPFWOUTlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardSerialPPPFWOUTlog_Type.__name__ = "Integer32"
_MGuardSerialPPPFWOUTlog_Object = MibTableColumn
mGuardSerialPPPFWOUTlog = _MGuardSerialPPPFWOUTlog_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 7, 1, 1, 8),
    _MGuardSerialPPPFWOUTlog_Type()
)
mGuardSerialPPPFWOUTlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialPPPFWOUTlog.setStatus("mandatory")
_MGuardSerialPPPFWOUTRowStatus_Type = RowStatus
_MGuardSerialPPPFWOUTRowStatus_Object = MibTableColumn
mGuardSerialPPPFWOUTRowStatus = _MGuardSerialPPPFWOUTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 7, 1, 1, 9),
    _MGuardSerialPPPFWOUTRowStatus_Type()
)
mGuardSerialPPPFWOUTRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialPPPFWOUTRowStatus.setStatus("mandatory")
_MGuardSerialPPPFWOUTcomment_Type = DisplayString
_MGuardSerialPPPFWOUTcomment_Object = MibTableColumn
mGuardSerialPPPFWOUTcomment = _MGuardSerialPPPFWOUTcomment_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 7, 1, 1, 10),
    _MGuardSerialPPPFWOUTcomment_Type()
)
mGuardSerialPPPFWOUTcomment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialPPPFWOUTcomment.setStatus("mandatory")


class _MGuardSerialPPPFWOUTLogDefault_Type(Integer32):
    """Custom type mGuardSerialPPPFWOUTLogDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardSerialPPPFWOUTLogDefault_Type.__name__ = "Integer32"
_MGuardSerialPPPFWOUTLogDefault_Object = MibScalar
mGuardSerialPPPFWOUTLogDefault = _MGuardSerialPPPFWOUTLogDefault_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 11, 3, 7, 2),
    _MGuardSerialPPPFWOUTLogDefault_Type()
)
mGuardSerialPPPFWOUTLogDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSerialPPPFWOUTLogDefault.setStatus("mandatory")
_MGuardArpTimeout_Type = Integer32
_MGuardArpTimeout_Object = MibScalar
mGuardArpTimeout = _MGuardArpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 3, 12),
    _MGuardArpTimeout_Type()
)
mGuardArpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardArpTimeout.setStatus("mandatory")
_MGuardSystem_ObjectIdentity = ObjectIdentity
mGuardSystem = _MGuardSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4)
)
_MGuardPasswords_ObjectIdentity = ObjectIdentity
mGuardPasswords = _MGuardPasswords_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 1)
)
_MGuardRootPassword_Type = DisplayString
_MGuardRootPassword_Object = MibScalar
mGuardRootPassword = _MGuardRootPassword_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 1, 1),
    _MGuardRootPassword_Type()
)
mGuardRootPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRootPassword.setStatus("mandatory")
_MGuardAdminPassword_Type = DisplayString
_MGuardAdminPassword_Object = MibScalar
mGuardAdminPassword = _MGuardAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 1, 2),
    _MGuardAdminPassword_Type()
)
mGuardAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardAdminPassword.setStatus("mandatory")
_MGuardUserPassword_Type = DisplayString
_MGuardUserPassword_Object = MibScalar
mGuardUserPassword = _MGuardUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 1, 3),
    _MGuardUserPassword_Type()
)
mGuardUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardUserPassword.setStatus("mandatory")
_MGuardUserPwdEnable_Type = TruthValue
_MGuardUserPwdEnable_Object = MibScalar
mGuardUserPwdEnable = _MGuardUserPwdEnable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 1, 4),
    _MGuardUserPwdEnable_Type()
)
mGuardUserPwdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardUserPwdEnable.setStatus("mandatory")
_MGuardHTTPSRemoteAccess_ObjectIdentity = ObjectIdentity
mGuardHTTPSRemoteAccess = _MGuardHTTPSRemoteAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 2)
)
_MGuardHTTPSRemoteEnable_Type = TruthValue
_MGuardHTTPSRemoteEnable_Object = MibScalar
mGuardHTTPSRemoteEnable = _MGuardHTTPSRemoteEnable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 2, 1),
    _MGuardHTTPSRemoteEnable_Type()
)
mGuardHTTPSRemoteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardHTTPSRemoteEnable.setStatus("mandatory")
_MGuardHTTPSRemotePort_Type = DisplayString
_MGuardHTTPSRemotePort_Object = MibScalar
mGuardHTTPSRemotePort = _MGuardHTTPSRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 2, 2),
    _MGuardHTTPSRemotePort_Type()
)
mGuardHTTPSRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardHTTPSRemotePort.setStatus("mandatory")
_MGuardHTTPSRemoteFWRuleTable_Object = MibTable
mGuardHTTPSRemoteFWRuleTable = _MGuardHTTPSRemoteFWRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 2, 3)
)
if mibBuilder.loadTexts:
    mGuardHTTPSRemoteFWRuleTable.setStatus("mandatory")
_MGuardHTTPSRemoteFWRuleEntry_Object = MibTableRow
mGuardHTTPSRemoteFWRuleEntry = _MGuardHTTPSRemoteFWRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 2, 3, 1)
)
mGuardHTTPSRemoteFWRuleEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardHTTPSFWruleIndex"),
)
if mibBuilder.loadTexts:
    mGuardHTTPSRemoteFWRuleEntry.setStatus("mandatory")


class _MGuardHTTPSFWruleIndex_Type(Integer32):
    """Custom type mGuardHTTPSFWruleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardHTTPSFWruleIndex_Type.__name__ = "Integer32"
_MGuardHTTPSFWruleIndex_Object = MibTableColumn
mGuardHTTPSFWruleIndex = _MGuardHTTPSFWruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 2, 3, 1, 1),
    _MGuardHTTPSFWruleIndex_Type()
)
mGuardHTTPSFWruleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardHTTPSFWruleIndex.setStatus("mandatory")
_MGuardHTTPSFWsourceIP_Type = DisplayString
_MGuardHTTPSFWsourceIP_Object = MibTableColumn
mGuardHTTPSFWsourceIP = _MGuardHTTPSFWsourceIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 2, 3, 1, 2),
    _MGuardHTTPSFWsourceIP_Type()
)
mGuardHTTPSFWsourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardHTTPSFWsourceIP.setStatus("mandatory")


class _MGuardHTTPSFWinterface_Type(Integer32):
    """Custom type mGuardHTTPSFWinterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extern", 1),
          ("intern", 2))
    )


_MGuardHTTPSFWinterface_Type.__name__ = "Integer32"
_MGuardHTTPSFWinterface_Object = MibTableColumn
mGuardHTTPSFWinterface = _MGuardHTTPSFWinterface_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 2, 3, 1, 3),
    _MGuardHTTPSFWinterface_Type()
)
mGuardHTTPSFWinterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardHTTPSFWinterface.setStatus("mandatory")


class _MGuardHTTPSFWtarget_Type(Integer32):
    """Custom type mGuardHTTPSFWtarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 3),
          ("reject", 2))
    )


_MGuardHTTPSFWtarget_Type.__name__ = "Integer32"
_MGuardHTTPSFWtarget_Object = MibTableColumn
mGuardHTTPSFWtarget = _MGuardHTTPSFWtarget_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 2, 3, 1, 4),
    _MGuardHTTPSFWtarget_Type()
)
mGuardHTTPSFWtarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardHTTPSFWtarget.setStatus("mandatory")


class _MGuardHTTPSFWlog_Type(Integer32):
    """Custom type mGuardHTTPSFWlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardHTTPSFWlog_Type.__name__ = "Integer32"
_MGuardHTTPSFWlog_Object = MibTableColumn
mGuardHTTPSFWlog = _MGuardHTTPSFWlog_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 2, 3, 1, 5),
    _MGuardHTTPSFWlog_Type()
)
mGuardHTTPSFWlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardHTTPSFWlog.setStatus("mandatory")
_MGuardHTTPSFWRowStatus_Type = RowStatus
_MGuardHTTPSFWRowStatus_Object = MibTableColumn
mGuardHTTPSFWRowStatus = _MGuardHTTPSFWRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 2, 3, 1, 6),
    _MGuardHTTPSFWRowStatus_Type()
)
mGuardHTTPSFWRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardHTTPSFWRowStatus.setStatus("mandatory")
_MGuardHTTPSFWcomment_Type = DisplayString
_MGuardHTTPSFWcomment_Object = MibTableColumn
mGuardHTTPSFWcomment = _MGuardHTTPSFWcomment_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 2, 3, 1, 7),
    _MGuardHTTPSFWcomment_Type()
)
mGuardHTTPSFWcomment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardHTTPSFWcomment.setStatus("mandatory")
_MGuardSSHRemoteAccess_ObjectIdentity = ObjectIdentity
mGuardSSHRemoteAccess = _MGuardSSHRemoteAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 3)
)
_MGuardSSHRemoteEnable_Type = TruthValue
_MGuardSSHRemoteEnable_Object = MibScalar
mGuardSSHRemoteEnable = _MGuardSSHRemoteEnable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 3, 1),
    _MGuardSSHRemoteEnable_Type()
)
mGuardSSHRemoteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSSHRemoteEnable.setStatus("mandatory")
_MGuardSSHRemotePort_Type = DisplayString
_MGuardSSHRemotePort_Object = MibScalar
mGuardSSHRemotePort = _MGuardSSHRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 3, 2),
    _MGuardSSHRemotePort_Type()
)
mGuardSSHRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSSHRemotePort.setStatus("mandatory")
_MGuardSSHRemoteFWRuleTable_Object = MibTable
mGuardSSHRemoteFWRuleTable = _MGuardSSHRemoteFWRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 3, 3)
)
if mibBuilder.loadTexts:
    mGuardSSHRemoteFWRuleTable.setStatus("mandatory")
_MGuardSSHRemoteFWRuleEntry_Object = MibTableRow
mGuardSSHRemoteFWRuleEntry = _MGuardSSHRemoteFWRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 3, 3, 1)
)
mGuardSSHRemoteFWRuleEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardSSHFWruleIndex"),
)
if mibBuilder.loadTexts:
    mGuardSSHRemoteFWRuleEntry.setStatus("mandatory")


class _MGuardSSHFWruleIndex_Type(Integer32):
    """Custom type mGuardSSHFWruleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardSSHFWruleIndex_Type.__name__ = "Integer32"
_MGuardSSHFWruleIndex_Object = MibTableColumn
mGuardSSHFWruleIndex = _MGuardSSHFWruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 3, 3, 1, 1),
    _MGuardSSHFWruleIndex_Type()
)
mGuardSSHFWruleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardSSHFWruleIndex.setStatus("mandatory")
_MGuardSSHFWsourceIP_Type = DisplayString
_MGuardSSHFWsourceIP_Object = MibTableColumn
mGuardSSHFWsourceIP = _MGuardSSHFWsourceIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 3, 3, 1, 2),
    _MGuardSSHFWsourceIP_Type()
)
mGuardSSHFWsourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSSHFWsourceIP.setStatus("mandatory")


class _MGuardSSHFWinterface_Type(Integer32):
    """Custom type mGuardSSHFWinterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extern", 1),
          ("intern", 2))
    )


_MGuardSSHFWinterface_Type.__name__ = "Integer32"
_MGuardSSHFWinterface_Object = MibTableColumn
mGuardSSHFWinterface = _MGuardSSHFWinterface_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 3, 3, 1, 3),
    _MGuardSSHFWinterface_Type()
)
mGuardSSHFWinterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSSHFWinterface.setStatus("mandatory")


class _MGuardSSHFWtarget_Type(Integer32):
    """Custom type mGuardSSHFWtarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 3),
          ("reject", 2))
    )


_MGuardSSHFWtarget_Type.__name__ = "Integer32"
_MGuardSSHFWtarget_Object = MibTableColumn
mGuardSSHFWtarget = _MGuardSSHFWtarget_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 3, 3, 1, 4),
    _MGuardSSHFWtarget_Type()
)
mGuardSSHFWtarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSSHFWtarget.setStatus("mandatory")


class _MGuardSSHFWlog_Type(Integer32):
    """Custom type mGuardSSHFWlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardSSHFWlog_Type.__name__ = "Integer32"
_MGuardSSHFWlog_Object = MibTableColumn
mGuardSSHFWlog = _MGuardSSHFWlog_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 3, 3, 1, 5),
    _MGuardSSHFWlog_Type()
)
mGuardSSHFWlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSSHFWlog.setStatus("mandatory")
_MGuardSSHFWRowStatus_Type = RowStatus
_MGuardSSHFWRowStatus_Object = MibTableColumn
mGuardSSHFWRowStatus = _MGuardSSHFWRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 3, 3, 1, 6),
    _MGuardSSHFWRowStatus_Type()
)
mGuardSSHFWRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSSHFWRowStatus.setStatus("mandatory")
_MGuardSSHFWcomment_Type = DisplayString
_MGuardSSHFWcomment_Object = MibTableColumn
mGuardSSHFWcomment = _MGuardSSHFWcomment_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 3, 3, 1, 7),
    _MGuardSSHFWcomment_Type()
)
mGuardSSHFWcomment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSSHFWcomment.setStatus("mandatory")
_MGuardWebInterface_ObjectIdentity = ObjectIdentity
mGuardWebInterface = _MGuardWebInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 4)
)


class _MGuardWebInterfaceLanguage_Type(Integer32):
    """Custom type mGuardWebInterfaceLanguage based on Integer32"""
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
        *(("automatic", 1),
          ("english", 2),
          ("german", 3),
          ("japanese", 4))
    )


_MGuardWebInterfaceLanguage_Type.__name__ = "Integer32"
_MGuardWebInterfaceLanguage_Object = MibScalar
mGuardWebInterfaceLanguage = _MGuardWebInterfaceLanguage_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 4, 1),
    _MGuardWebInterfaceLanguage_Type()
)
mGuardWebInterfaceLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardWebInterfaceLanguage.setStatus("mandatory")
_MGuardWebInterfaceSessionTimeout_Type = Integer32
_MGuardWebInterfaceSessionTimeout_Object = MibScalar
mGuardWebInterfaceSessionTimeout = _MGuardWebInterfaceSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 4, 2),
    _MGuardWebInterfaceSessionTimeout_Type()
)
mGuardWebInterfaceSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardWebInterfaceSessionTimeout.setStatus("mandatory")


class _MGuardWebInterfaceApplyButtonScope_Type(Integer32):
    """Custom type mGuardWebInterfaceApplyButtonScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("page", 1),
          ("session", 2))
    )


_MGuardWebInterfaceApplyButtonScope_Type.__name__ = "Integer32"
_MGuardWebInterfaceApplyButtonScope_Object = MibScalar
mGuardWebInterfaceApplyButtonScope = _MGuardWebInterfaceApplyButtonScope_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 4, 3),
    _MGuardWebInterfaceApplyButtonScope_Type()
)
mGuardWebInterfaceApplyButtonScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardWebInterfaceApplyButtonScope.setStatus("mandatory")
_MGuardHardwareInformation_ObjectIdentity = ObjectIdentity
mGuardHardwareInformation = _MGuardHardwareInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 5)
)
_MGuardHardware_Type = DisplayString
_MGuardHardware_Object = MibScalar
mGuardHardware = _MGuardHardware_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 5, 1),
    _MGuardHardware_Type()
)
mGuardHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardHardware.setStatus("mandatory")
_MGuardCPU_Type = DisplayString
_MGuardCPU_Object = MibScalar
mGuardCPU = _MGuardCPU_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 5, 2),
    _MGuardCPU_Type()
)
mGuardCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardCPU.setStatus("mandatory")
_MGuardCPUFamily_Type = DisplayString
_MGuardCPUFamily_Object = MibScalar
mGuardCPUFamily = _MGuardCPUFamily_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 5, 3),
    _MGuardCPUFamily_Type()
)
mGuardCPUFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardCPUFamily.setStatus("mandatory")
_MGuardCPUStepping_Type = DisplayString
_MGuardCPUStepping_Object = MibScalar
mGuardCPUStepping = _MGuardCPUStepping_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 5, 4),
    _MGuardCPUStepping_Type()
)
mGuardCPUStepping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardCPUStepping.setStatus("mandatory")
_MGuardCPUSpeed_Type = DisplayString
_MGuardCPUSpeed_Object = MibScalar
mGuardCPUSpeed = _MGuardCPUSpeed_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 5, 5),
    _MGuardCPUSpeed_Type()
)
mGuardCPUSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardCPUSpeed.setStatus("mandatory")
_MGuardSystemTemperature_Type = DisplayString
_MGuardSystemTemperature_Object = MibScalar
mGuardSystemTemperature = _MGuardSystemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 5, 6),
    _MGuardSystemTemperature_Type()
)
mGuardSystemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardSystemTemperature.setStatus("mandatory")
_MGuardUptime_Type = DisplayString
_MGuardUptime_Object = MibScalar
mGuardUptime = _MGuardUptime_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 5, 7),
    _MGuardUptime_Type()
)
mGuardUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardUptime.setStatus("mandatory")
_MGuardUSMem_Type = DisplayString
_MGuardUSMem_Object = MibScalar
mGuardUSMem = _MGuardUSMem_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 5, 8),
    _MGuardUSMem_Type()
)
mGuardUSMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardUSMem.setStatus("mandatory")
_MGuardMAC1_Type = DisplayString
_MGuardMAC1_Object = MibScalar
mGuardMAC1 = _MGuardMAC1_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 5, 9),
    _MGuardMAC1_Type()
)
mGuardMAC1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardMAC1.setStatus("mandatory")
_MGuardMAC2_Type = DisplayString
_MGuardMAC2_Object = MibScalar
mGuardMAC2 = _MGuardMAC2_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 5, 10),
    _MGuardMAC2_Type()
)
mGuardMAC2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardMAC2.setStatus("mandatory")
_MGuardMAC3_Type = DisplayString
_MGuardMAC3_Object = MibScalar
mGuardMAC3 = _MGuardMAC3_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 5, 11),
    _MGuardMAC3_Type()
)
mGuardMAC3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardMAC3.setStatus("mandatory")
_MGuardSerialNumber_Type = DisplayString
_MGuardSerialNumber_Object = MibScalar
mGuardSerialNumber = _MGuardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 5, 12),
    _MGuardSerialNumber_Type()
)
mGuardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardSerialNumber.setStatus("mandatory")
_MGuardVerParSet_Type = DisplayString
_MGuardVerParSet_Object = MibScalar
mGuardVerParSet = _MGuardVerParSet_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 5, 13),
    _MGuardVerParSet_Type()
)
mGuardVerParSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardVerParSet.setStatus("mandatory")
_MGuardProductName_Type = DisplayString
_MGuardProductName_Object = MibScalar
mGuardProductName = _MGuardProductName_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 5, 14),
    _MGuardProductName_Type()
)
mGuardProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardProductName.setStatus("mandatory")
_MGuardOEMName_Type = DisplayString
_MGuardOEMName_Object = MibScalar
mGuardOEMName = _MGuardOEMName_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 5, 15),
    _MGuardOEMName_Type()
)
mGuardOEMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardOEMName.setStatus("mandatory")
_MGuardOEMSerial_Type = DisplayString
_MGuardOEMSerial_Object = MibScalar
mGuardOEMSerial = _MGuardOEMSerial_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 5, 16),
    _MGuardOEMSerial_Type()
)
mGuardOEMSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardOEMSerial.setStatus("mandatory")
_MGuardManufacturer_Type = DisplayString
_MGuardManufacturer_Object = MibScalar
mGuardManufacturer = _MGuardManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 5, 17),
    _MGuardManufacturer_Type()
)
mGuardManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardManufacturer.setStatus("mandatory")
_MGuardManuDate_Type = DisplayString
_MGuardManuDate_Object = MibScalar
mGuardManuDate = _MGuardManuDate_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 5, 18),
    _MGuardManuDate_Type()
)
mGuardManuDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardManuDate.setStatus("mandatory")
_MGuardBootLoader_Type = DisplayString
_MGuardBootLoader_Object = MibScalar
mGuardBootLoader = _MGuardBootLoader_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 5, 19),
    _MGuardBootLoader_Type()
)
mGuardBootLoader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardBootLoader.setStatus("mandatory")
_MGuardHardwareVersion_Type = DisplayString
_MGuardHardwareVersion_Object = MibScalar
mGuardHardwareVersion = _MGuardHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 5, 20),
    _MGuardHardwareVersion_Type()
)
mGuardHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardHardwareVersion.setStatus("mandatory")
_MGuardRescueSystem_Type = DisplayString
_MGuardRescueSystem_Object = MibScalar
mGuardRescueSystem = _MGuardRescueSystem_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 5, 21),
    _MGuardRescueSystem_Type()
)
mGuardRescueSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardRescueSystem.setStatus("mandatory")
_MGuardProdSoft_Type = DisplayString
_MGuardProdSoft_Object = MibScalar
mGuardProdSoft = _MGuardProdSoft_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 5, 22),
    _MGuardProdSoft_Type()
)
mGuardProdSoft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardProdSoft.setStatus("mandatory")
_MGuardVersions_ObjectIdentity = ObjectIdentity
mGuardVersions = _MGuardVersions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 7)
)
_MGuardVersion_Type = DisplayString
_MGuardVersion_Object = MibScalar
mGuardVersion = _MGuardVersion_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 7, 1),
    _MGuardVersion_Type()
)
mGuardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardVersion.setStatus("mandatory")
_MGuardBaseVersion_Type = DisplayString
_MGuardBaseVersion_Object = MibScalar
mGuardBaseVersion = _MGuardBaseVersion_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 7, 2),
    _MGuardBaseVersion_Type()
)
mGuardBaseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardBaseVersion.setStatus("mandatory")
_MGuardUpdates_Type = DisplayString
_MGuardUpdates_Object = MibScalar
mGuardUpdates = _MGuardUpdates_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 7, 3),
    _MGuardUpdates_Type()
)
mGuardUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardUpdates.setStatus("mandatory")
_MGuardPackageVersionTable_Object = MibTable
mGuardPackageVersionTable = _MGuardPackageVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 7, 4)
)
if mibBuilder.loadTexts:
    mGuardPackageVersionTable.setStatus("mandatory")
_MGuardPackageVersionEntry_Object = MibTableRow
mGuardPackageVersionEntry = _MGuardPackageVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 7, 4, 1)
)
mGuardPackageVersionEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardPkgIndex"),
)
if mibBuilder.loadTexts:
    mGuardPackageVersionEntry.setStatus("mandatory")


class _MGuardPkgIndex_Type(Integer32):
    """Custom type mGuardPkgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_MGuardPkgIndex_Type.__name__ = "Integer32"
_MGuardPkgIndex_Object = MibTableColumn
mGuardPkgIndex = _MGuardPkgIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 7, 4, 1, 1),
    _MGuardPkgIndex_Type()
)
mGuardPkgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardPkgIndex.setStatus("mandatory")
_MGuardPkgName_Type = DisplayString
_MGuardPkgName_Object = MibTableColumn
mGuardPkgName = _MGuardPkgName_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 7, 4, 1, 2),
    _MGuardPkgName_Type()
)
mGuardPkgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardPkgName.setStatus("mandatory")
_MGuardPkgVerNum_Type = DisplayString
_MGuardPkgVerNum_Object = MibTableColumn
mGuardPkgVerNum = _MGuardPkgVerNum_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 7, 4, 1, 3),
    _MGuardPkgVerNum_Type()
)
mGuardPkgVerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardPkgVerNum.setStatus("mandatory")
_MGuardPkgVerVersion_Type = DisplayString
_MGuardPkgVerVersion_Object = MibTableColumn
mGuardPkgVerVersion = _MGuardPkgVerVersion_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 7, 4, 1, 4),
    _MGuardPkgVerVersion_Type()
)
mGuardPkgVerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardPkgVerVersion.setStatus("mandatory")
_MGuardPkgVerFlavour_Type = DisplayString
_MGuardPkgVerFlavour_Object = MibTableColumn
mGuardPkgVerFlavour = _MGuardPkgVerFlavour_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 7, 4, 1, 5),
    _MGuardPkgVerFlavour_Type()
)
mGuardPkgVerFlavour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardPkgVerFlavour.setStatus("mandatory")


class _MGuardAction_Type(Integer32):
    """Custom type mGuardAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reboot", 1)
    )


_MGuardAction_Type.__name__ = "Integer32"
_MGuardAction_Object = MibScalar
mGuardAction = _MGuardAction_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 8),
    _MGuardAction_Type()
)
mGuardAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardAction.setStatus("mandatory")


class _MGuardSysProduct_Type(Integer32):
    """Custom type mGuardSysProduct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              51001,
              51002,
              51003,
              51011,
              51012,
              51013,
              51020,
              51021,
              51030,
              51031,
              51032,
              51033,
              51040,
              51044,
              51052,
              51053,
              51060,
              51062,
              51063)
        )
    )
    namedValues = NamedValues(
        *(("mGuard-blade-en", 51052),
          ("mGuard-blade-enxl", 51053),
          ("mGuard-core-266", 51002),
          ("mGuard-core-533", 51012),
          ("mGuard-delta", 51060),
          ("mGuard-delta-en", 51062),
          ("mGuard-delta-enxl", 51063),
          ("mGuard-industrial-enfw", 51040),
          ("mGuard-industrial-enxl", 51044),
          ("mGuard-pci", 51030),
          ("mGuard-pci-en", 51032),
          ("mGuard-pci-enxl", 51033),
          ("mGuard-pci-pr", 51031),
          ("mGuard-smart", 51020),
          ("mGuard-smart-en", 51021),
          ("mGuard-smart-enxl", 51011),
          ("mGuard-smart-gw-266", 51003),
          ("mGuard-smart-gw-533", 51013),
          ("mGuard-smart-pr", 51001),
          ("unknown", 1))
    )


_MGuardSysProduct_Type.__name__ = "Integer32"
_MGuardSysProduct_Object = MibScalar
mGuardSysProduct = _MGuardSysProduct_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 4, 9),
    _MGuardSysProduct_Type()
)
mGuardSysProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardSysProduct.setStatus("mandatory")
_MGuardSNMP_ObjectIdentity = ObjectIdentity
mGuardSNMP = _MGuardSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5)
)


class _MGuardSNMPenableV3_Type(Integer32):
    """Custom type mGuardSNMPenableV3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardSNMPenableV3_Type.__name__ = "Integer32"
_MGuardSNMPenableV3_Object = MibScalar
mGuardSNMPenableV3 = _MGuardSNMPenableV3_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 1),
    _MGuardSNMPenableV3_Type()
)
mGuardSNMPenableV3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPenableV3.setStatus("mandatory")


class _MGuardSNMPenableV1_Type(Integer32):
    """Custom type mGuardSNMPenableV1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardSNMPenableV1_Type.__name__ = "Integer32"
_MGuardSNMPenableV1_Object = MibScalar
mGuardSNMPenableV1 = _MGuardSNMPenableV1_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 2),
    _MGuardSNMPenableV1_Type()
)
mGuardSNMPenableV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPenableV1.setStatus("mandatory")
_MGuardSNMPport_Type = DisplayString
_MGuardSNMPport_Object = MibScalar
mGuardSNMPport = _MGuardSNMPport_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 3),
    _MGuardSNMPport_Type()
)
mGuardSNMPport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPport.setStatus("mandatory")
_MGuardSNMPv1ROCommunity_Type = DisplayString
_MGuardSNMPv1ROCommunity_Object = MibScalar
mGuardSNMPv1ROCommunity = _MGuardSNMPv1ROCommunity_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 4),
    _MGuardSNMPv1ROCommunity_Type()
)
mGuardSNMPv1ROCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPv1ROCommunity.setStatus("mandatory")
_MGuardSNMPv1RWCommunity_Type = DisplayString
_MGuardSNMPv1RWCommunity_Object = MibScalar
mGuardSNMPv1RWCommunity = _MGuardSNMPv1RWCommunity_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 5),
    _MGuardSNMPv1RWCommunity_Type()
)
mGuardSNMPv1RWCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPv1RWCommunity.setStatus("mandatory")
_MGuardSNMPFWRuleTable_Object = MibTable
mGuardSNMPFWRuleTable = _MGuardSNMPFWRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 6)
)
if mibBuilder.loadTexts:
    mGuardSNMPFWRuleTable.setStatus("mandatory")
_MGuardSNMPFWRuleEntry_Object = MibTableRow
mGuardSNMPFWRuleEntry = _MGuardSNMPFWRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 6, 1)
)
mGuardSNMPFWRuleEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardSNMPFWruleIndex"),
)
if mibBuilder.loadTexts:
    mGuardSNMPFWRuleEntry.setStatus("mandatory")


class _MGuardSNMPFWruleIndex_Type(Integer32):
    """Custom type mGuardSNMPFWruleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardSNMPFWruleIndex_Type.__name__ = "Integer32"
_MGuardSNMPFWruleIndex_Object = MibTableColumn
mGuardSNMPFWruleIndex = _MGuardSNMPFWruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 6, 1, 1),
    _MGuardSNMPFWruleIndex_Type()
)
mGuardSNMPFWruleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardSNMPFWruleIndex.setStatus("mandatory")
_MGuardSNMPFWsourceIP_Type = DisplayString
_MGuardSNMPFWsourceIP_Object = MibTableColumn
mGuardSNMPFWsourceIP = _MGuardSNMPFWsourceIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 6, 1, 2),
    _MGuardSNMPFWsourceIP_Type()
)
mGuardSNMPFWsourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPFWsourceIP.setStatus("mandatory")


class _MGuardSNMPFWinterface_Type(Integer32):
    """Custom type mGuardSNMPFWinterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extern", 1),
          ("intern", 2))
    )


_MGuardSNMPFWinterface_Type.__name__ = "Integer32"
_MGuardSNMPFWinterface_Object = MibTableColumn
mGuardSNMPFWinterface = _MGuardSNMPFWinterface_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 6, 1, 3),
    _MGuardSNMPFWinterface_Type()
)
mGuardSNMPFWinterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPFWinterface.setStatus("mandatory")


class _MGuardSNMPFWtarget_Type(Integer32):
    """Custom type mGuardSNMPFWtarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 3),
          ("reject", 2))
    )


_MGuardSNMPFWtarget_Type.__name__ = "Integer32"
_MGuardSNMPFWtarget_Object = MibTableColumn
mGuardSNMPFWtarget = _MGuardSNMPFWtarget_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 6, 1, 4),
    _MGuardSNMPFWtarget_Type()
)
mGuardSNMPFWtarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPFWtarget.setStatus("mandatory")


class _MGuardSNMPFWlog_Type(Integer32):
    """Custom type mGuardSNMPFWlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardSNMPFWlog_Type.__name__ = "Integer32"
_MGuardSNMPFWlog_Object = MibTableColumn
mGuardSNMPFWlog = _MGuardSNMPFWlog_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 6, 1, 5),
    _MGuardSNMPFWlog_Type()
)
mGuardSNMPFWlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPFWlog.setStatus("mandatory")
_MGuardSNMPFWRowStatus_Type = RowStatus
_MGuardSNMPFWRowStatus_Object = MibTableColumn
mGuardSNMPFWRowStatus = _MGuardSNMPFWRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 6, 1, 6),
    _MGuardSNMPFWRowStatus_Type()
)
mGuardSNMPFWRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPFWRowStatus.setStatus("mandatory")
_MGuardSNMPFWcomment_Type = DisplayString
_MGuardSNMPFWcomment_Object = MibTableColumn
mGuardSNMPFWcomment = _MGuardSNMPFWcomment_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 6, 1, 7),
    _MGuardSNMPFWcomment_Type()
)
mGuardSNMPFWcomment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPFWcomment.setStatus("mandatory")
_MGuardSNMPTrapReceiverTable_Object = MibTable
mGuardSNMPTrapReceiverTable = _MGuardSNMPTrapReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 7)
)
if mibBuilder.loadTexts:
    mGuardSNMPTrapReceiverTable.setStatus("mandatory")
_MGuardSNMPTrapReceiverEntry_Object = MibTableRow
mGuardSNMPTrapReceiverEntry = _MGuardSNMPTrapReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 7, 1)
)
mGuardSNMPTrapReceiverEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardSNMPTrapReceiverIndex"),
)
if mibBuilder.loadTexts:
    mGuardSNMPTrapReceiverEntry.setStatus("mandatory")


class _MGuardSNMPTrapReceiverIndex_Type(Integer32):
    """Custom type mGuardSNMPTrapReceiverIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MGuardSNMPTrapReceiverIndex_Type.__name__ = "Integer32"
_MGuardSNMPTrapReceiverIndex_Object = MibTableColumn
mGuardSNMPTrapReceiverIndex = _MGuardSNMPTrapReceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 7, 1, 1),
    _MGuardSNMPTrapReceiverIndex_Type()
)
mGuardSNMPTrapReceiverIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardSNMPTrapReceiverIndex.setStatus("mandatory")
_MGuardSNMPTrapReceiverCommunity_Type = DisplayString
_MGuardSNMPTrapReceiverCommunity_Object = MibTableColumn
mGuardSNMPTrapReceiverCommunity = _MGuardSNMPTrapReceiverCommunity_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 7, 1, 2),
    _MGuardSNMPTrapReceiverCommunity_Type()
)
mGuardSNMPTrapReceiverCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPTrapReceiverCommunity.setStatus("mandatory")
_MGuardSNMPTrapReceiverIPAddress_Type = IpAddress
_MGuardSNMPTrapReceiverIPAddress_Object = MibTableColumn
mGuardSNMPTrapReceiverIPAddress = _MGuardSNMPTrapReceiverIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 7, 1, 3),
    _MGuardSNMPTrapReceiverIPAddress_Type()
)
mGuardSNMPTrapReceiverIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPTrapReceiverIPAddress.setStatus("mandatory")
_MGuardSNMPTrapReceiverName_Type = DisplayString
_MGuardSNMPTrapReceiverName_Object = MibTableColumn
mGuardSNMPTrapReceiverName = _MGuardSNMPTrapReceiverName_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 7, 1, 4),
    _MGuardSNMPTrapReceiverName_Type()
)
mGuardSNMPTrapReceiverName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPTrapReceiverName.setStatus("mandatory")
_MGuardSNMPTrapReceiverRowStatus_Type = RowStatus
_MGuardSNMPTrapReceiverRowStatus_Object = MibTableColumn
mGuardSNMPTrapReceiverRowStatus = _MGuardSNMPTrapReceiverRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 7, 1, 5),
    _MGuardSNMPTrapReceiverRowStatus_Type()
)
mGuardSNMPTrapReceiverRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPTrapReceiverRowStatus.setStatus("mandatory")
_MGuardSNMPTrapConfigGroup_ObjectIdentity = ObjectIdentity
mGuardSNMPTrapConfigGroup = _MGuardSNMPTrapConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 8)
)


class _MGuardSNMPAuthenticationTrapFlag_Type(Integer32):
    """Custom type mGuardSNMPAuthenticationTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MGuardSNMPAuthenticationTrapFlag_Type.__name__ = "Integer32"
_MGuardSNMPAuthenticationTrapFlag_Object = MibScalar
mGuardSNMPAuthenticationTrapFlag = _MGuardSNMPAuthenticationTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 8, 1),
    _MGuardSNMPAuthenticationTrapFlag_Type()
)
mGuardSNMPAuthenticationTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPAuthenticationTrapFlag.setStatus("mandatory")


class _MGuardSNMPLinkUpDownTrapFlag_Type(Integer32):
    """Custom type mGuardSNMPLinkUpDownTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MGuardSNMPLinkUpDownTrapFlag_Type.__name__ = "Integer32"
_MGuardSNMPLinkUpDownTrapFlag_Object = MibScalar
mGuardSNMPLinkUpDownTrapFlag = _MGuardSNMPLinkUpDownTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 8, 2),
    _MGuardSNMPLinkUpDownTrapFlag_Type()
)
mGuardSNMPLinkUpDownTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPLinkUpDownTrapFlag.setStatus("mandatory")


class _MGuardSNMPColdStartTrapFlag_Type(Integer32):
    """Custom type mGuardSNMPColdStartTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MGuardSNMPColdStartTrapFlag_Type.__name__ = "Integer32"
_MGuardSNMPColdStartTrapFlag_Object = MibScalar
mGuardSNMPColdStartTrapFlag = _MGuardSNMPColdStartTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 8, 3),
    _MGuardSNMPColdStartTrapFlag_Type()
)
mGuardSNMPColdStartTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPColdStartTrapFlag.setStatus("mandatory")


class _MGuardSNMPTrapFlag_Type(Integer32):
    """Custom type mGuardSNMPTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MGuardSNMPTrapFlag_Type.__name__ = "Integer32"
_MGuardSNMPTrapFlag_Object = MibScalar
mGuardSNMPTrapFlag = _MGuardSNMPTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 8, 4),
    _MGuardSNMPTrapFlag_Type()
)
mGuardSNMPTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPTrapFlag.setStatus("mandatory")


class _MGuardSNMPChassisTrapFlag_Type(Integer32):
    """Custom type mGuardSNMPChassisTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MGuardSNMPChassisTrapFlag_Type.__name__ = "Integer32"
_MGuardSNMPChassisTrapFlag_Object = MibScalar
mGuardSNMPChassisTrapFlag = _MGuardSNMPChassisTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 8, 5),
    _MGuardSNMPChassisTrapFlag_Type()
)
mGuardSNMPChassisTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPChassisTrapFlag.setStatus("mandatory")


class _MGuardSNMPAgentTrapFlag_Type(Integer32):
    """Custom type mGuardSNMPAgentTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MGuardSNMPAgentTrapFlag_Type.__name__ = "Integer32"
_MGuardSNMPAgentTrapFlag_Object = MibScalar
mGuardSNMPAgentTrapFlag = _MGuardSNMPAgentTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 8, 6),
    _MGuardSNMPAgentTrapFlag_Type()
)
mGuardSNMPAgentTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPAgentTrapFlag.setStatus("mandatory")


class _MGuardSNMPAvFailTrapFlag_Type(Integer32):
    """Custom type mGuardSNMPAvFailTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MGuardSNMPAvFailTrapFlag_Type.__name__ = "Integer32"
_MGuardSNMPAvFailTrapFlag_Object = MibScalar
mGuardSNMPAvFailTrapFlag = _MGuardSNMPAvFailTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 8, 7),
    _MGuardSNMPAvFailTrapFlag_Type()
)
mGuardSNMPAvFailTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPAvFailTrapFlag.setStatus("mandatory")


class _MGuardSNMPAvInfoTrapFlag_Type(Integer32):
    """Custom type mGuardSNMPAvInfoTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MGuardSNMPAvInfoTrapFlag_Type.__name__ = "Integer32"
_MGuardSNMPAvInfoTrapFlag_Object = MibScalar
mGuardSNMPAvInfoTrapFlag = _MGuardSNMPAvInfoTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 8, 8),
    _MGuardSNMPAvInfoTrapFlag_Type()
)
mGuardSNMPAvInfoTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPAvInfoTrapFlag.setStatus("mandatory")


class _MGuardSNMPBladeStateTrapFlag_Type(Integer32):
    """Custom type mGuardSNMPBladeStateTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MGuardSNMPBladeStateTrapFlag_Type.__name__ = "Integer32"
_MGuardSNMPBladeStateTrapFlag_Object = MibScalar
mGuardSNMPBladeStateTrapFlag = _MGuardSNMPBladeStateTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 8, 9),
    _MGuardSNMPBladeStateTrapFlag_Type()
)
mGuardSNMPBladeStateTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPBladeStateTrapFlag.setStatus("mandatory")


class _MGuardSNMPBladeConfigTrapFlag_Type(Integer32):
    """Custom type mGuardSNMPBladeConfigTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MGuardSNMPBladeConfigTrapFlag_Type.__name__ = "Integer32"
_MGuardSNMPBladeConfigTrapFlag_Object = MibScalar
mGuardSNMPBladeConfigTrapFlag = _MGuardSNMPBladeConfigTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 8, 10),
    _MGuardSNMPBladeConfigTrapFlag_Type()
)
mGuardSNMPBladeConfigTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPBladeConfigTrapFlag.setStatus("mandatory")


class _MGuardSNMPRouterRedundancyStatusFlag_Type(Integer32):
    """Custom type mGuardSNMPRouterRedundancyStatusFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MGuardSNMPRouterRedundancyStatusFlag_Type.__name__ = "Integer32"
_MGuardSNMPRouterRedundancyStatusFlag_Object = MibScalar
mGuardSNMPRouterRedundancyStatusFlag = _MGuardSNMPRouterRedundancyStatusFlag_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 5, 8, 11),
    _MGuardSNMPRouterRedundancyStatusFlag_Type()
)
mGuardSNMPRouterRedundancyStatusFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardSNMPRouterRedundancyStatusFlag.setStatus("mandatory")
_MGuardNTP_ObjectIdentity = ObjectIdentity
mGuardNTP = _MGuardNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 6)
)


class _MGuardNTPactivate_Type(Integer32):
    """Custom type mGuardNTPactivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardNTPactivate_Type.__name__ = "Integer32"
_MGuardNTPactivate_Object = MibScalar
mGuardNTPactivate = _MGuardNTPactivate_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 6, 1),
    _MGuardNTPactivate_Type()
)
mGuardNTPactivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardNTPactivate.setStatus("mandatory")


class _MGuardNTPtimestamp_Type(Integer32):
    """Custom type mGuardNTPtimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardNTPtimestamp_Type.__name__ = "Integer32"
_MGuardNTPtimestamp_Object = MibScalar
mGuardNTPtimestamp = _MGuardNTPtimestamp_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 6, 2),
    _MGuardNTPtimestamp_Type()
)
mGuardNTPtimestamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardNTPtimestamp.setStatus("mandatory")
_MGuardNTPServerTable_Object = MibTable
mGuardNTPServerTable = _MGuardNTPServerTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 6, 3)
)
if mibBuilder.loadTexts:
    mGuardNTPServerTable.setStatus("mandatory")
_MGuardNTPServerEntry_Object = MibTableRow
mGuardNTPServerEntry = _MGuardNTPServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 6, 3, 1)
)
mGuardNTPServerEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardNTPServerIndex"),
)
if mibBuilder.loadTexts:
    mGuardNTPServerEntry.setStatus("mandatory")


class _MGuardNTPServerIndex_Type(Integer32):
    """Custom type mGuardNTPServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MGuardNTPServerIndex_Type.__name__ = "Integer32"
_MGuardNTPServerIndex_Object = MibTableColumn
mGuardNTPServerIndex = _MGuardNTPServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 6, 3, 1, 1),
    _MGuardNTPServerIndex_Type()
)
mGuardNTPServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardNTPServerIndex.setStatus("mandatory")
_MGuardNTPServerHost_Type = DisplayString
_MGuardNTPServerHost_Object = MibTableColumn
mGuardNTPServerHost = _MGuardNTPServerHost_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 6, 3, 1, 2),
    _MGuardNTPServerHost_Type()
)
mGuardNTPServerHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardNTPServerHost.setStatus("mandatory")
_MGuardNTPServerRowStatus_Type = RowStatus
_MGuardNTPServerRowStatus_Object = MibTableColumn
mGuardNTPServerRowStatus = _MGuardNTPServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 6, 3, 1, 3),
    _MGuardNTPServerRowStatus_Type()
)
mGuardNTPServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardNTPServerRowStatus.setStatus("mandatory")
_MGuardNTPTimezone_Type = DisplayString
_MGuardNTPTimezone_Object = MibScalar
mGuardNTPTimezone = _MGuardNTPTimezone_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 6, 4),
    _MGuardNTPTimezone_Type()
)
mGuardNTPTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardNTPTimezone.setStatus("mandatory")
_MGuardNTPStatus_Type = DisplayString
_MGuardNTPStatus_Object = MibScalar
mGuardNTPStatus = _MGuardNTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 6, 5),
    _MGuardNTPStatus_Type()
)
mGuardNTPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardNTPStatus.setStatus("mandatory")
_MGuardUpdate_ObjectIdentity = ObjectIdentity
mGuardUpdate = _MGuardUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 7)
)
_MGuardUpdateServerTable_Object = MibTable
mGuardUpdateServerTable = _MGuardUpdateServerTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 7, 1)
)
if mibBuilder.loadTexts:
    mGuardUpdateServerTable.setStatus("mandatory")
_MGuardUpdateServerEntry_Object = MibTableRow
mGuardUpdateServerEntry = _MGuardUpdateServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 7, 1, 1)
)
mGuardUpdateServerEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardUpdateServerIndex"),
)
if mibBuilder.loadTexts:
    mGuardUpdateServerEntry.setStatus("mandatory")


class _MGuardUpdateServerIndex_Type(Integer32):
    """Custom type mGuardUpdateServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MGuardUpdateServerIndex_Type.__name__ = "Integer32"
_MGuardUpdateServerIndex_Object = MibTableColumn
mGuardUpdateServerIndex = _MGuardUpdateServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 7, 1, 1, 1),
    _MGuardUpdateServerIndex_Type()
)
mGuardUpdateServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardUpdateServerIndex.setStatus("mandatory")
_MGuardUpdateServer_Type = DisplayString
_MGuardUpdateServer_Object = MibTableColumn
mGuardUpdateServer = _MGuardUpdateServer_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 7, 1, 1, 2),
    _MGuardUpdateServer_Type()
)
mGuardUpdateServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardUpdateServer.setStatus("deprecated")
_MGuardUpdateServerRowStatus_Type = RowStatus
_MGuardUpdateServerRowStatus_Object = MibTableColumn
mGuardUpdateServerRowStatus = _MGuardUpdateServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 7, 1, 1, 3),
    _MGuardUpdateServerRowStatus_Type()
)
mGuardUpdateServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardUpdateServerRowStatus.setStatus("mandatory")
_MGuardUpdateServerProto_Type = DisplayString
_MGuardUpdateServerProto_Object = MibTableColumn
mGuardUpdateServerProto = _MGuardUpdateServerProto_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 7, 1, 1, 4),
    _MGuardUpdateServerProto_Type()
)
mGuardUpdateServerProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardUpdateServerProto.setStatus("mandatory")
_MGuardUpdateServerHost_Type = DisplayString
_MGuardUpdateServerHost_Object = MibTableColumn
mGuardUpdateServerHost = _MGuardUpdateServerHost_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 7, 1, 1, 5),
    _MGuardUpdateServerHost_Type()
)
mGuardUpdateServerHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardUpdateServerHost.setStatus("mandatory")
_MGuardUpdateServerLogin_Type = DisplayString
_MGuardUpdateServerLogin_Object = MibTableColumn
mGuardUpdateServerLogin = _MGuardUpdateServerLogin_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 7, 1, 1, 6),
    _MGuardUpdateServerLogin_Type()
)
mGuardUpdateServerLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardUpdateServerLogin.setStatus("mandatory")
_MGuardUpdateServerPassword_Type = DisplayString
_MGuardUpdateServerPassword_Object = MibTableColumn
mGuardUpdateServerPassword = _MGuardUpdateServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 7, 1, 1, 7),
    _MGuardUpdateServerPassword_Type()
)
mGuardUpdateServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardUpdateServerPassword.setStatus("mandatory")
_MGuardSNMPError_Type = DisplayString
_MGuardSNMPError_Object = MibScalar
mGuardSNMPError = _MGuardSNMPError_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 8),
    _MGuardSNMPError_Type()
)
mGuardSNMPError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardSNMPError.setStatus("mandatory")
_MGuardRedundancy_ObjectIdentity = ObjectIdentity
mGuardRedundancy = _MGuardRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 9)
)
_MGuardRouterRedundancy_ObjectIdentity = ObjectIdentity
mGuardRouterRedundancy = _MGuardRouterRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 9, 2)
)


class _MGuardRouterRedundancyEnable_Type(Integer32):
    """Custom type mGuardRouterRedundancyEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MGuardRouterRedundancyEnable_Type.__name__ = "Integer32"
_MGuardRouterRedundancyEnable_Object = MibScalar
mGuardRouterRedundancyEnable = _MGuardRouterRedundancyEnable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 9, 2, 1),
    _MGuardRouterRedundancyEnable_Type()
)
mGuardRouterRedundancyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterRedundancyEnable.setStatus("mandatory")


class _MGuardRouterRedundancyTrack_Type(Integer32):
    """Custom type mGuardRouterRedundancyTrack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MGuardRouterRedundancyTrack_Type.__name__ = "Integer32"
_MGuardRouterRedundancyTrack_Object = MibScalar
mGuardRouterRedundancyTrack = _MGuardRouterRedundancyTrack_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 9, 2, 2),
    _MGuardRouterRedundancyTrack_Type()
)
mGuardRouterRedundancyTrack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterRedundancyTrack.setStatus("mandatory")
_MGuardRouterRedundancyInternalID_Type = Integer32
_MGuardRouterRedundancyInternalID_Object = MibScalar
mGuardRouterRedundancyInternalID = _MGuardRouterRedundancyInternalID_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 9, 2, 3),
    _MGuardRouterRedundancyInternalID_Type()
)
mGuardRouterRedundancyInternalID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterRedundancyInternalID.setStatus("mandatory")
_MGuardRouterRedundancyExternalID_Type = Integer32
_MGuardRouterRedundancyExternalID_Object = MibScalar
mGuardRouterRedundancyExternalID = _MGuardRouterRedundancyExternalID_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 9, 2, 4),
    _MGuardRouterRedundancyExternalID_Type()
)
mGuardRouterRedundancyExternalID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterRedundancyExternalID.setStatus("mandatory")
_MGuardRouterRedundancyPassword_Type = DisplayString
_MGuardRouterRedundancyPassword_Object = MibScalar
mGuardRouterRedundancyPassword = _MGuardRouterRedundancyPassword_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 9, 2, 5),
    _MGuardRouterRedundancyPassword_Type()
)
mGuardRouterRedundancyPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterRedundancyPassword.setStatus("mandatory")
_MGuardRouterRedundancyPeerIntern_Type = IpAddress
_MGuardRouterRedundancyPeerIntern_Object = MibScalar
mGuardRouterRedundancyPeerIntern = _MGuardRouterRedundancyPeerIntern_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 9, 2, 6),
    _MGuardRouterRedundancyPeerIntern_Type()
)
mGuardRouterRedundancyPeerIntern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterRedundancyPeerIntern.setStatus("mandatory")
_MGuardRouterRedundancyPeerExtern_Type = IpAddress
_MGuardRouterRedundancyPeerExtern_Object = MibScalar
mGuardRouterRedundancyPeerExtern = _MGuardRouterRedundancyPeerExtern_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 9, 2, 7),
    _MGuardRouterRedundancyPeerExtern_Type()
)
mGuardRouterRedundancyPeerExtern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterRedundancyPeerExtern.setStatus("mandatory")
_MGuardRouterRedundancyPriority_Type = Integer32
_MGuardRouterRedundancyPriority_Object = MibScalar
mGuardRouterRedundancyPriority = _MGuardRouterRedundancyPriority_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 9, 2, 8),
    _MGuardRouterRedundancyPriority_Type()
)
mGuardRouterRedundancyPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterRedundancyPriority.setStatus("mandatory")
_MGuardRouterRedundancyVirtIpInt_Type = IpAddress
_MGuardRouterRedundancyVirtIpInt_Object = MibScalar
mGuardRouterRedundancyVirtIpInt = _MGuardRouterRedundancyVirtIpInt_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 9, 2, 9),
    _MGuardRouterRedundancyVirtIpInt_Type()
)
mGuardRouterRedundancyVirtIpInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterRedundancyVirtIpInt.setStatus("mandatory")
_MGuardRouterRedundancyVirtIpExt_Type = IpAddress
_MGuardRouterRedundancyVirtIpExt_Object = MibScalar
mGuardRouterRedundancyVirtIpExt = _MGuardRouterRedundancyVirtIpExt_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 9, 2, 10),
    _MGuardRouterRedundancyVirtIpExt_Type()
)
mGuardRouterRedundancyVirtIpExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterRedundancyVirtIpExt.setStatus("mandatory")


class _MGuardRouterRedundancyWantState_Type(Integer32):
    """Custom type mGuardRouterRedundancyWantState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("master", 1))
    )


_MGuardRouterRedundancyWantState_Type.__name__ = "Integer32"
_MGuardRouterRedundancyWantState_Object = MibScalar
mGuardRouterRedundancyWantState = _MGuardRouterRedundancyWantState_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 9, 2, 11),
    _MGuardRouterRedundancyWantState_Type()
)
mGuardRouterRedundancyWantState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterRedundancyWantState.setStatus("mandatory")
_MGuardRouterRedExtHostCheckTable_Object = MibTable
mGuardRouterRedExtHostCheckTable = _MGuardRouterRedExtHostCheckTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 9, 2, 12)
)
if mibBuilder.loadTexts:
    mGuardRouterRedExtHostCheckTable.setStatus("mandatory")
_MGuardRouterRedExtHostCheckEntry_Object = MibTableRow
mGuardRouterRedExtHostCheckEntry = _MGuardRouterRedExtHostCheckEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 9, 2, 12, 1)
)
mGuardRouterRedExtHostCheckEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardRouterRedExtHostCheckIndex"),
)
if mibBuilder.loadTexts:
    mGuardRouterRedExtHostCheckEntry.setStatus("mandatory")


class _MGuardRouterRedExtHostCheckIndex_Type(Integer32):
    """Custom type mGuardRouterRedExtHostCheckIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardRouterRedExtHostCheckIndex_Type.__name__ = "Integer32"
_MGuardRouterRedExtHostCheckIndex_Object = MibTableColumn
mGuardRouterRedExtHostCheckIndex = _MGuardRouterRedExtHostCheckIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 9, 2, 12, 1, 1),
    _MGuardRouterRedExtHostCheckIndex_Type()
)
mGuardRouterRedExtHostCheckIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardRouterRedExtHostCheckIndex.setStatus("mandatory")
_MGuardRouterRedExtHostCheckIP_Type = IpAddress
_MGuardRouterRedExtHostCheckIP_Object = MibTableColumn
mGuardRouterRedExtHostCheckIP = _MGuardRouterRedExtHostCheckIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 9, 2, 12, 1, 2),
    _MGuardRouterRedExtHostCheckIP_Type()
)
mGuardRouterRedExtHostCheckIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterRedExtHostCheckIP.setStatus("mandatory")
_MGuardRouterRedExtHostCheckRowSt_Type = RowStatus
_MGuardRouterRedExtHostCheckRowSt_Object = MibTableColumn
mGuardRouterRedExtHostCheckRowSt = _MGuardRouterRedExtHostCheckRowSt_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 9, 2, 12, 1, 3),
    _MGuardRouterRedExtHostCheckRowSt_Type()
)
mGuardRouterRedExtHostCheckRowSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterRedExtHostCheckRowSt.setStatus("mandatory")
_MGuardRouterRedIntHostCheckTable_Object = MibTable
mGuardRouterRedIntHostCheckTable = _MGuardRouterRedIntHostCheckTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 9, 2, 13)
)
if mibBuilder.loadTexts:
    mGuardRouterRedIntHostCheckTable.setStatus("mandatory")
_MGuardRouterRedIntHostCheckEntry_Object = MibTableRow
mGuardRouterRedIntHostCheckEntry = _MGuardRouterRedIntHostCheckEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 9, 2, 13, 1)
)
mGuardRouterRedIntHostCheckEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardRouterRedIntHostCheckIndex"),
)
if mibBuilder.loadTexts:
    mGuardRouterRedIntHostCheckEntry.setStatus("mandatory")


class _MGuardRouterRedIntHostCheckIndex_Type(Integer32):
    """Custom type mGuardRouterRedIntHostCheckIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardRouterRedIntHostCheckIndex_Type.__name__ = "Integer32"
_MGuardRouterRedIntHostCheckIndex_Object = MibTableColumn
mGuardRouterRedIntHostCheckIndex = _MGuardRouterRedIntHostCheckIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 9, 2, 13, 1, 1),
    _MGuardRouterRedIntHostCheckIndex_Type()
)
mGuardRouterRedIntHostCheckIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardRouterRedIntHostCheckIndex.setStatus("mandatory")
_MGuardRouterRedIntHostCheckIP_Type = IpAddress
_MGuardRouterRedIntHostCheckIP_Object = MibTableColumn
mGuardRouterRedIntHostCheckIP = _MGuardRouterRedIntHostCheckIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 9, 2, 13, 1, 2),
    _MGuardRouterRedIntHostCheckIP_Type()
)
mGuardRouterRedIntHostCheckIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterRedIntHostCheckIP.setStatus("mandatory")
_MGuardRouterRedIntHostCheckRowSt_Type = RowStatus
_MGuardRouterRedIntHostCheckRowSt_Object = MibTableColumn
mGuardRouterRedIntHostCheckRowSt = _MGuardRouterRedIntHostCheckRowSt_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 9, 2, 13, 1, 3),
    _MGuardRouterRedIntHostCheckRowSt_Type()
)
mGuardRouterRedIntHostCheckRowSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRouterRedIntHostCheckRowSt.setStatus("mandatory")


class _MGuardRouterRedundancyState_Type(Integer32):
    """Custom type mGuardRouterRedundancyState based on Integer32"""
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
        *(("backup", 1),
          ("disabled", 4),
          ("fault", 3),
          ("master", 2))
    )


_MGuardRouterRedundancyState_Type.__name__ = "Integer32"
_MGuardRouterRedundancyState_Object = MibScalar
mGuardRouterRedundancyState = _MGuardRouterRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 9, 2, 14),
    _MGuardRouterRedundancyState_Type()
)
mGuardRouterRedundancyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardRouterRedundancyState.setStatus("mandatory")
_MGuardInfo_ObjectIdentity = ObjectIdentity
mGuardInfo = _MGuardInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10)
)
_MGuardHTTPSLastAccessIP_Type = IpAddress
_MGuardHTTPSLastAccessIP_Object = MibScalar
mGuardHTTPSLastAccessIP = _MGuardHTTPSLastAccessIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 1),
    _MGuardHTTPSLastAccessIP_Type()
)
mGuardHTTPSLastAccessIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardHTTPSLastAccessIP.setStatus("mandatory")
_MGuardShellLastAccessIP_Type = IpAddress
_MGuardShellLastAccessIP_Object = MibScalar
mGuardShellLastAccessIP = _MGuardShellLastAccessIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 2),
    _MGuardShellLastAccessIP_Type()
)
mGuardShellLastAccessIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardShellLastAccessIP.setStatus("mandatory")
_MGuardDHCPLastAccessMAC_Type = MacAddress
_MGuardDHCPLastAccessMAC_Object = MibScalar
mGuardDHCPLastAccessMAC = _MGuardDHCPLastAccessMAC_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 3),
    _MGuardDHCPLastAccessMAC_Type()
)
mGuardDHCPLastAccessMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardDHCPLastAccessMAC.setStatus("mandatory")
_MGuardTrapResources_ObjectIdentity = ObjectIdentity
mGuardTrapResources = _MGuardTrapResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4)
)


class _MGuardTResDiscFull_Type(Integer32):
    """Custom type mGuardTResDiscFull based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("free", 1),
          ("full", 3),
          ("tight", 2))
    )


_MGuardTResDiscFull_Type.__name__ = "Integer32"
_MGuardTResDiscFull_Object = MibScalar
mGuardTResDiscFull = _MGuardTResDiscFull_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 1),
    _MGuardTResDiscFull_Type()
)
mGuardTResDiscFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardTResDiscFull.setStatus("mandatory")
_MGuardTResCpuLoadHigh_Type = Integer32
_MGuardTResCpuLoadHigh_Object = MibScalar
mGuardTResCpuLoadHigh = _MGuardTResCpuLoadHigh_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 2),
    _MGuardTResCpuLoadHigh_Type()
)
mGuardTResCpuLoadHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardTResCpuLoadHigh.setStatus("mandatory")
_MGuardTResMemoryFull_Type = Integer32
_MGuardTResMemoryFull_Object = MibScalar
mGuardTResMemoryFull = _MGuardTResMemoryFull_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 3),
    _MGuardTResMemoryFull_Type()
)
mGuardTResMemoryFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardTResMemoryFull.setStatus("mandatory")
_MGuardTResColdstart_Type = Integer32
_MGuardTResColdstart_Object = MibScalar
mGuardTResColdstart = _MGuardTResColdstart_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 4),
    _MGuardTResColdstart_Type()
)
mGuardTResColdstart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardTResColdstart.setStatus("mandatory")
_MGuardTResAV_ObjectIdentity = ObjectIdentity
mGuardTResAV = _MGuardTResAV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 6)
)
_MGuardTResAvUpdateDone_Type = DisplayString
_MGuardTResAvUpdateDone_Object = MibScalar
mGuardTResAvUpdateDone = _MGuardTResAvUpdateDone_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 6, 1),
    _MGuardTResAvUpdateDone_Type()
)
mGuardTResAvUpdateDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardTResAvUpdateDone.setStatus("mandatory")
_MGuardTResAvUpdateError_Type = DisplayString
_MGuardTResAvUpdateError_Object = MibScalar
mGuardTResAvUpdateError = _MGuardTResAvUpdateError_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 6, 2),
    _MGuardTResAvUpdateError_Type()
)
mGuardTResAvUpdateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardTResAvUpdateError.setStatus("mandatory")
_MGuardTResAvVirusDetected_Type = DisplayString
_MGuardTResAvVirusDetected_Object = MibScalar
mGuardTResAvVirusDetected = _MGuardTResAvVirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 6, 3),
    _MGuardTResAvVirusDetected_Type()
)
mGuardTResAvVirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardTResAvVirusDetected.setStatus("mandatory")
_MGuardTResAvFileNotScanned_Type = DisplayString
_MGuardTResAvFileNotScanned_Object = MibScalar
mGuardTResAvFileNotScanned = _MGuardTResAvFileNotScanned_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 6, 4),
    _MGuardTResAvFileNotScanned_Type()
)
mGuardTResAvFileNotScanned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardTResAvFileNotScanned.setStatus("mandatory")
_MGuardTResAvFailed_Type = DisplayString
_MGuardTResAvFailed_Object = MibScalar
mGuardTResAvFailed = _MGuardTResAvFailed_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 6, 5),
    _MGuardTResAvFailed_Type()
)
mGuardTResAvFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardTResAvFailed.setStatus("mandatory")
_MGuardTResPlatformSpecific_ObjectIdentity = ObjectIdentity
mGuardTResPlatformSpecific = _MGuardTResPlatformSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7)
)
_MGuardTResIndustrial_ObjectIdentity = ObjectIdentity
mGuardTResIndustrial = _MGuardTResIndustrial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 1)
)
_MGuardTResIndustrialPower_ObjectIdentity = ObjectIdentity
mGuardTResIndustrialPower = _MGuardTResIndustrialPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 1, 1)
)
_MGuardPSTable_Object = MibTable
mGuardPSTable = _MGuardPSTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mGuardPSTable.setStatus("mandatory")
_MGuardPSEntry_Object = MibTableRow
mGuardPSEntry = _MGuardPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 1, 1, 2, 1)
)
mGuardPSEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardPSSysID"),
    (0, "MGUARDB-MIB", "mGuardPSID"),
)
if mibBuilder.loadTexts:
    mGuardPSEntry.setStatus("mandatory")


class _MGuardPSSysID_Type(Integer32):
    """Custom type mGuardPSSysID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardPSSysID_Type.__name__ = "Integer32"
_MGuardPSSysID_Object = MibTableColumn
mGuardPSSysID = _MGuardPSSysID_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 1, 1, 2, 1, 1),
    _MGuardPSSysID_Type()
)
mGuardPSSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardPSSysID.setStatus("mandatory")


class _MGuardPSID_Type(Integer32):
    """Custom type mGuardPSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardPSID_Type.__name__ = "Integer32"
_MGuardPSID_Object = MibTableColumn
mGuardPSID = _MGuardPSID_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 1, 1, 2, 1, 2),
    _MGuardPSID_Type()
)
mGuardPSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardPSID.setStatus("mandatory")


class _MGuardPSState_Type(Integer32):
    """Custom type mGuardPSState based on Integer32"""
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
        *(("failed", 2),
          ("notInstalled", 3),
          ("ok", 1),
          ("unknown", 4))
    )


_MGuardPSState_Type.__name__ = "Integer32"
_MGuardPSState_Object = MibTableColumn
mGuardPSState = _MGuardPSState_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 1, 1, 2, 1, 3),
    _MGuardPSState_Type()
)
mGuardPSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardPSState.setStatus("mandatory")
_MGuardTResIndustrialTemperature_ObjectIdentity = ObjectIdentity
mGuardTResIndustrialTemperature = _MGuardTResIndustrialTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 1, 2)
)
_MGuardTResIndustrialTempHiLimit_Type = Integer32
_MGuardTResIndustrialTempHiLimit_Object = MibScalar
mGuardTResIndustrialTempHiLimit = _MGuardTResIndustrialTempHiLimit_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 1, 2, 2),
    _MGuardTResIndustrialTempHiLimit_Type()
)
mGuardTResIndustrialTempHiLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardTResIndustrialTempHiLimit.setStatus("mandatory")
_MGuardTResIndustrialTempLowLimit_Type = Integer32
_MGuardTResIndustrialTempLowLimit_Object = MibScalar
mGuardTResIndustrialTempLowLimit = _MGuardTResIndustrialTempLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 1, 2, 3),
    _MGuardTResIndustrialTempLowLimit_Type()
)
mGuardTResIndustrialTempLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardTResIndustrialTempLowLimit.setStatus("mandatory")
_MGuardTResSignalRelais_ObjectIdentity = ObjectIdentity
mGuardTResSignalRelais = _MGuardTResSignalRelais_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 1, 3)
)
_MGuardTResSignalRelaisState_Type = Integer32
_MGuardTResSignalRelaisState_Object = MibScalar
mGuardTResSignalRelaisState = _MGuardTResSignalRelaisState_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 1, 3, 1),
    _MGuardTResSignalRelaisState_Type()
)
mGuardTResSignalRelaisState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardTResSignalRelaisState.setStatus("mandatory")
_MGuardTResSignalRelaisReason_Type = ObjectIdentifier
_MGuardTResSignalRelaisReason_Object = MibScalar
mGuardTResSignalRelaisReason = _MGuardTResSignalRelaisReason_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 1, 3, 2),
    _MGuardTResSignalRelaisReason_Type()
)
mGuardTResSignalRelaisReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardTResSignalRelaisReason.setStatus("mandatory")
_MGuardTResSignalRelaisReasonIdx_Type = Integer32
_MGuardTResSignalRelaisReasonIdx_Object = MibScalar
mGuardTResSignalRelaisReasonIdx = _MGuardTResSignalRelaisReasonIdx_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 1, 3, 3),
    _MGuardTResSignalRelaisReasonIdx_Type()
)
mGuardTResSignalRelaisReasonIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardTResSignalRelaisReasonIdx.setStatus("mandatory")


class _MGuardTResSignalRelaisPowerAlarm_Type(Integer32):
    """Custom type mGuardTResSignalRelaisPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MGuardTResSignalRelaisPowerAlarm_Type.__name__ = "Integer32"
_MGuardTResSignalRelaisPowerAlarm_Object = MibScalar
mGuardTResSignalRelaisPowerAlarm = _MGuardTResSignalRelaisPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 1, 3, 4),
    _MGuardTResSignalRelaisPowerAlarm_Type()
)
mGuardTResSignalRelaisPowerAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardTResSignalRelaisPowerAlarm.setStatus("mandatory")


class _MGuardTResSignalRelaisMode_Type(Integer32):
    """Custom type mGuardTResSignalRelaisMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 2),
          ("standard", 1))
    )


_MGuardTResSignalRelaisMode_Type.__name__ = "Integer32"
_MGuardTResSignalRelaisMode_Object = MibScalar
mGuardTResSignalRelaisMode = _MGuardTResSignalRelaisMode_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 1, 3, 5),
    _MGuardTResSignalRelaisMode_Type()
)
mGuardTResSignalRelaisMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardTResSignalRelaisMode.setStatus("mandatory")


class _MGuardTResSignalRelaisManualStat_Type(Integer32):
    """Custom type mGuardTResSignalRelaisManualStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_MGuardTResSignalRelaisManualStat_Type.__name__ = "Integer32"
_MGuardTResSignalRelaisManualStat_Object = MibScalar
mGuardTResSignalRelaisManualStat = _MGuardTResSignalRelaisManualStat_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 1, 3, 6),
    _MGuardTResSignalRelaisManualStat_Type()
)
mGuardTResSignalRelaisManualStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardTResSignalRelaisManualStat.setStatus("mandatory")


class _MGuardTResAutoConfigAdapterState_Type(Integer32):
    """Custom type mGuardTResAutoConfigAdapterState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("checksumErr", 7),
          ("genericErr", 8),
          ("notInSync", 4),
          ("notPresent", 1),
          ("ok", 3),
          ("outOfMemory", 5),
          ("removed", 2),
          ("wrongMachine", 6))
    )


_MGuardTResAutoConfigAdapterState_Type.__name__ = "Integer32"
_MGuardTResAutoConfigAdapterState_Object = MibScalar
mGuardTResAutoConfigAdapterState = _MGuardTResAutoConfigAdapterState_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 1, 4),
    _MGuardTResAutoConfigAdapterState_Type()
)
mGuardTResAutoConfigAdapterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardTResAutoConfigAdapterState.setStatus("mandatory")
_MGuardTResSignalLinkTable_ObjectIdentity = ObjectIdentity
mGuardTResSignalLinkTable = _MGuardTResSignalLinkTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 1, 5)
)


class _MGuardTResSigLinkID_Type(Integer32):
    """Custom type mGuardTResSigLinkID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_MGuardTResSigLinkID_Type.__name__ = "Integer32"
_MGuardTResSigLinkID_Object = MibScalar
mGuardTResSigLinkID = _MGuardTResSigLinkID_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 1, 5, 1),
    _MGuardTResSigLinkID_Type()
)
mGuardTResSigLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardTResSigLinkID.setStatus("mandatory")


class _MGuardTResSigLinkAlarm_Type(Integer32):
    """Custom type mGuardTResSigLinkAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_MGuardTResSigLinkAlarm_Type.__name__ = "Integer32"
_MGuardTResSigLinkAlarm_Object = MibScalar
mGuardTResSigLinkAlarm = _MGuardTResSigLinkAlarm_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 1, 5, 2),
    _MGuardTResSigLinkAlarm_Type()
)
mGuardTResSigLinkAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardTResSigLinkAlarm.setStatus("mandatory")
_MGuardTResBladeCTRL_ObjectIdentity = ObjectIdentity
mGuardTResBladeCTRL = _MGuardTResBladeCTRL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 2)
)
_MGuardTResBladeInfo_ObjectIdentity = ObjectIdentity
mGuardTResBladeInfo = _MGuardTResBladeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 2, 1)
)
_MGuardTResBladeRackID_Type = DisplayString
_MGuardTResBladeRackID_Object = MibScalar
mGuardTResBladeRackID = _MGuardTResBladeRackID_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 2, 1, 1),
    _MGuardTResBladeRackID_Type()
)
mGuardTResBladeRackID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardTResBladeRackID.setStatus("mandatory")
_MGuardTResBladeSlotNr_Type = Integer32
_MGuardTResBladeSlotNr_Object = MibScalar
mGuardTResBladeSlotNr = _MGuardTResBladeSlotNr_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 2, 1, 2),
    _MGuardTResBladeSlotNr_Type()
)
mGuardTResBladeSlotNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardTResBladeSlotNr.setStatus("mandatory")


class _MGuardTResBladeCtrlPowerStatus_Type(Integer32):
    """Custom type mGuardTResBladeCtrlPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("online", 3),
          ("present", 2))
    )


_MGuardTResBladeCtrlPowerStatus_Type.__name__ = "Integer32"
_MGuardTResBladeCtrlPowerStatus_Object = MibScalar
mGuardTResBladeCtrlPowerStatus = _MGuardTResBladeCtrlPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 2, 2),
    _MGuardTResBladeCtrlPowerStatus_Type()
)
mGuardTResBladeCtrlPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardTResBladeCtrlPowerStatus.setStatus("mandatory")


class _MGuardTResBladeCtrlRunStatus_Type(Integer32):
    """Custom type mGuardTResBladeCtrlRunStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("online", 3),
          ("present", 2))
    )


_MGuardTResBladeCtrlRunStatus_Type.__name__ = "Integer32"
_MGuardTResBladeCtrlRunStatus_Object = MibScalar
mGuardTResBladeCtrlRunStatus = _MGuardTResBladeCtrlRunStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 2, 3),
    _MGuardTResBladeCtrlRunStatus_Type()
)
mGuardTResBladeCtrlRunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardTResBladeCtrlRunStatus.setStatus("mandatory")
_MGuardTResBladeCtrlCfg_ObjectIdentity = ObjectIdentity
mGuardTResBladeCtrlCfg = _MGuardTResBladeCtrlCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 2, 5)
)


class _MGuardTResBladeCtrlCfgBackup_Type(Integer32):
    """Custom type mGuardTResBladeCtrlCfgBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("downloaded", 3)
    )


_MGuardTResBladeCtrlCfgBackup_Type.__name__ = "Integer32"
_MGuardTResBladeCtrlCfgBackup_Object = MibScalar
mGuardTResBladeCtrlCfgBackup = _MGuardTResBladeCtrlCfgBackup_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 2, 5, 1),
    _MGuardTResBladeCtrlCfgBackup_Type()
)
mGuardTResBladeCtrlCfgBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardTResBladeCtrlCfgBackup.setStatus("mandatory")


class _MGuardTResBladeCtrlCfgRestored_Type(Integer32):
    """Custom type mGuardTResBladeCtrlCfgRestored based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_MGuardTResBladeCtrlCfgRestored_Type.__name__ = "Integer32"
_MGuardTResBladeCtrlCfgRestored_Object = MibScalar
mGuardTResBladeCtrlCfgRestored = _MGuardTResBladeCtrlCfgRestored_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 7, 2, 5, 2),
    _MGuardTResBladeCtrlCfgRestored_Type()
)
mGuardTResBladeCtrlCfgRestored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardTResBladeCtrlCfgRestored.setStatus("mandatory")
_MGuardTResRedundancy_ObjectIdentity = ObjectIdentity
mGuardTResRedundancy = _MGuardTResRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 8)
)
_MGuardTResRedundacyReason_Type = DisplayString
_MGuardTResRedundacyReason_Object = MibScalar
mGuardTResRedundacyReason = _MGuardTResRedundacyReason_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 8, 1),
    _MGuardTResRedundacyReason_Type()
)
mGuardTResRedundacyReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardTResRedundacyReason.setStatus("mandatory")
_MGuardTResRedundacyBackupDown_Type = DisplayString
_MGuardTResRedundacyBackupDown_Object = MibScalar
mGuardTResRedundacyBackupDown = _MGuardTResRedundacyBackupDown_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 4, 8, 2),
    _MGuardTResRedundacyBackupDown_Type()
)
mGuardTResRedundacyBackupDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardTResRedundacyBackupDown.setStatus("mandatory")
_MGuardTraps_ObjectIdentity = ObjectIdentity
mGuardTraps = _MGuardTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 5)
)
_MGuardTrapAV_ObjectIdentity = ObjectIdentity
mGuardTrapAV = _MGuardTrapAV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 6)
)
_MGuardTrapPlatformSpecific_ObjectIdentity = ObjectIdentity
mGuardTrapPlatformSpecific = _MGuardTrapPlatformSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 7)
)
_MGuardTrapIndustrial_ObjectIdentity = ObjectIdentity
mGuardTrapIndustrial = _MGuardTrapIndustrial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 7, 1)
)
_MGuardTrapBladeCTRL_ObjectIdentity = ObjectIdentity
mGuardTrapBladeCTRL = _MGuardTrapBladeCTRL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 7, 2)
)
_MGuardTrapBladeCtrlCfg_ObjectIdentity = ObjectIdentity
mGuardTrapBladeCtrlCfg = _MGuardTrapBladeCtrlCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 7, 2, 5)
)
_MGuardTrapRouterRedundancy_ObjectIdentity = ObjectIdentity
mGuardTrapRouterRedundancy = _MGuardTrapRouterRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 8)
)
_MGuardLogging_ObjectIdentity = ObjectIdentity
mGuardLogging = _MGuardLogging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 11)
)


class _MGuardLoggingRemoteActivate_Type(Integer32):
    """Custom type mGuardLoggingRemoteActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardLoggingRemoteActivate_Type.__name__ = "Integer32"
_MGuardLoggingRemoteActivate_Object = MibScalar
mGuardLoggingRemoteActivate = _MGuardLoggingRemoteActivate_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 11, 1),
    _MGuardLoggingRemoteActivate_Type()
)
mGuardLoggingRemoteActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardLoggingRemoteActivate.setStatus("mandatory")
_MGuardLoggingRemoteIP_Type = IpAddress
_MGuardLoggingRemoteIP_Object = MibScalar
mGuardLoggingRemoteIP = _MGuardLoggingRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 11, 2),
    _MGuardLoggingRemoteIP_Type()
)
mGuardLoggingRemoteIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardLoggingRemoteIP.setStatus("mandatory")
_MGuardLoggingRemotePort_Type = DisplayString
_MGuardLoggingRemotePort_Object = MibScalar
mGuardLoggingRemotePort = _MGuardLoggingRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 11, 3),
    _MGuardLoggingRemotePort_Type()
)
mGuardLoggingRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardLoggingRemotePort.setStatus("mandatory")
_MGuardContFilt_ObjectIdentity = ObjectIdentity
mGuardContFilt = _MGuardContFilt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12)
)
_MGuardContFiltAVP_ObjectIdentity = ObjectIdentity
mGuardContFiltAVP = _MGuardContFiltAVP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1)
)


class _MGuardContFiltAVPSchedule_Type(Integer32):
    """Custom type mGuardContFiltAVPSchedule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              15,
              30,
              60,
              120,
              360,
              720,
              1440)
        )
    )
    namedValues = NamedValues(
        *(("bihourly", 120),
          ("halfhourly", 30),
          ("hourly", 60),
          ("never", 1),
          ("onboot", 2),
          ("quarterhourly", 15),
          ("sixhourly", 720),
          ("triplehourly", 360),
          ("twicedayly", 1440))
    )


_MGuardContFiltAVPSchedule_Type.__name__ = "Integer32"
_MGuardContFiltAVPSchedule_Object = MibScalar
mGuardContFiltAVPSchedule = _MGuardContFiltAVPSchedule_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 1),
    _MGuardContFiltAVPSchedule_Type()
)
mGuardContFiltAVPSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltAVPSchedule.setStatus("mandatory")
_MGuardContFiltAVPServerTable_Object = MibTable
mGuardContFiltAVPServerTable = _MGuardContFiltAVPServerTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 2)
)
if mibBuilder.loadTexts:
    mGuardContFiltAVPServerTable.setStatus("mandatory")
_MGuardContFiltAVPServerEntry_Object = MibTableRow
mGuardContFiltAVPServerEntry = _MGuardContFiltAVPServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 2, 1)
)
mGuardContFiltAVPServerEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardContFiltAVPServerIndex"),
)
if mibBuilder.loadTexts:
    mGuardContFiltAVPServerEntry.setStatus("mandatory")


class _MGuardContFiltAVPServerIndex_Type(Integer32):
    """Custom type mGuardContFiltAVPServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardContFiltAVPServerIndex_Type.__name__ = "Integer32"
_MGuardContFiltAVPServerIndex_Object = MibTableColumn
mGuardContFiltAVPServerIndex = _MGuardContFiltAVPServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 2, 1, 1),
    _MGuardContFiltAVPServerIndex_Type()
)
mGuardContFiltAVPServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardContFiltAVPServerIndex.setStatus("mandatory")
_MGuardContFiltAVPServerURL_Type = DisplayString
_MGuardContFiltAVPServerURL_Object = MibTableColumn
mGuardContFiltAVPServerURL = _MGuardContFiltAVPServerURL_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 2, 1, 2),
    _MGuardContFiltAVPServerURL_Type()
)
mGuardContFiltAVPServerURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltAVPServerURL.setStatus("mandatory")
_MGuardContFiltAVPServerRowStatus_Type = RowStatus
_MGuardContFiltAVPServerRowStatus_Object = MibTableColumn
mGuardContFiltAVPServerRowStatus = _MGuardContFiltAVPServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 2, 1, 3),
    _MGuardContFiltAVPServerRowStatus_Type()
)
mGuardContFiltAVPServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltAVPServerRowStatus.setStatus("mandatory")
_MGuardContFiltAVPHTTPProxy_ObjectIdentity = ObjectIdentity
mGuardContFiltAVPHTTPProxy = _MGuardContFiltAVPHTTPProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 3)
)
_MGuardContFiltAVPHTTPProxyLogin_Type = DisplayString
_MGuardContFiltAVPHTTPProxyLogin_Object = MibScalar
mGuardContFiltAVPHTTPProxyLogin = _MGuardContFiltAVPHTTPProxyLogin_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 3, 1),
    _MGuardContFiltAVPHTTPProxyLogin_Type()
)
mGuardContFiltAVPHTTPProxyLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltAVPHTTPProxyLogin.setStatus("mandatory")
_MGuardContFiltAVPHTTPProxyPasswd_Type = DisplayString
_MGuardContFiltAVPHTTPProxyPasswd_Object = MibScalar
mGuardContFiltAVPHTTPProxyPasswd = _MGuardContFiltAVPHTTPProxyPasswd_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 3, 2),
    _MGuardContFiltAVPHTTPProxyPasswd_Type()
)
mGuardContFiltAVPHTTPProxyPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltAVPHTTPProxyPasswd.setStatus("mandatory")
_MGuardContFiltAVPHTTPProxyServer_Type = DisplayString
_MGuardContFiltAVPHTTPProxyServer_Object = MibScalar
mGuardContFiltAVPHTTPProxyServer = _MGuardContFiltAVPHTTPProxyServer_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 3, 3),
    _MGuardContFiltAVPHTTPProxyServer_Type()
)
mGuardContFiltAVPHTTPProxyServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltAVPHTTPProxyServer.setStatus("mandatory")
_MGuardContFiltAVPHTTPProxyPort_Type = DisplayString
_MGuardContFiltAVPHTTPProxyPort_Object = MibScalar
mGuardContFiltAVPHTTPProxyPort = _MGuardContFiltAVPHTTPProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 3, 4),
    _MGuardContFiltAVPHTTPProxyPort_Type()
)
mGuardContFiltAVPHTTPProxyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltAVPHTTPProxyPort.setStatus("mandatory")


class _MGuardContFiltAVPLogLevel_Type(Integer32):
    """Custom type mGuardContFiltAVPLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MGuardContFiltAVPLogLevel_Type.__name__ = "Integer32"
_MGuardContFiltAVPLogLevel_Object = MibScalar
mGuardContFiltAVPLogLevel = _MGuardContFiltAVPLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 5),
    _MGuardContFiltAVPLogLevel_Type()
)
mGuardContFiltAVPLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltAVPLogLevel.setStatus("mandatory")
_MGuardContFiltAVPMaxConnections_Type = Integer32
_MGuardContFiltAVPMaxConnections_Object = MibScalar
mGuardContFiltAVPMaxConnections = _MGuardContFiltAVPMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 6),
    _MGuardContFiltAVPMaxConnections_Type()
)
mGuardContFiltAVPMaxConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltAVPMaxConnections.setStatus("mandatory")
_MGuardContFiltAVPScanTimeout_Type = Integer32
_MGuardContFiltAVPScanTimeout_Object = MibScalar
mGuardContFiltAVPScanTimeout = _MGuardContFiltAVPScanTimeout_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 7),
    _MGuardContFiltAVPScanTimeout_Type()
)
mGuardContFiltAVPScanTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltAVPScanTimeout.setStatus("mandatory")
_MGuardContFiltAVPpass_ObjectIdentity = ObjectIdentity
mGuardContFiltAVPpass = _MGuardContFiltAVPpass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 8)
)


class _MGuardContFiltAVPpassCorrupt_Type(Integer32):
    """Custom type mGuardContFiltAVPpassCorrupt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardContFiltAVPpassCorrupt_Type.__name__ = "Integer32"
_MGuardContFiltAVPpassCorrupt_Object = MibScalar
mGuardContFiltAVPpassCorrupt = _MGuardContFiltAVPpassCorrupt_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 8, 1),
    _MGuardContFiltAVPpassCorrupt_Type()
)
mGuardContFiltAVPpassCorrupt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltAVPpassCorrupt.setStatus("mandatory")


class _MGuardContFiltAVPpassEncrypted_Type(Integer32):
    """Custom type mGuardContFiltAVPpassEncrypted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardContFiltAVPpassEncrypted_Type.__name__ = "Integer32"
_MGuardContFiltAVPpassEncrypted_Object = MibScalar
mGuardContFiltAVPpassEncrypted = _MGuardContFiltAVPpassEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 8, 2),
    _MGuardContFiltAVPpassEncrypted_Type()
)
mGuardContFiltAVPpassEncrypted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltAVPpassEncrypted.setStatus("mandatory")


class _MGuardContFiltAVPpassSuspicious_Type(Integer32):
    """Custom type mGuardContFiltAVPpassSuspicious based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardContFiltAVPpassSuspicious_Type.__name__ = "Integer32"
_MGuardContFiltAVPpassSuspicious_Object = MibScalar
mGuardContFiltAVPpassSuspicious = _MGuardContFiltAVPpassSuspicious_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 8, 3),
    _MGuardContFiltAVPpassSuspicious_Type()
)
mGuardContFiltAVPpassSuspicious.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltAVPpassSuspicious.setStatus("mandatory")


class _MGuardContFiltAVPpassWarnings_Type(Integer32):
    """Custom type mGuardContFiltAVPpassWarnings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardContFiltAVPpassWarnings_Type.__name__ = "Integer32"
_MGuardContFiltAVPpassWarnings_Object = MibScalar
mGuardContFiltAVPpassWarnings = _MGuardContFiltAVPpassWarnings_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 8, 4),
    _MGuardContFiltAVPpassWarnings_Type()
)
mGuardContFiltAVPpassWarnings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltAVPpassWarnings.setStatus("mandatory")
_MGuardContFiltQuarantine_ObjectIdentity = ObjectIdentity
mGuardContFiltQuarantine = _MGuardContFiltQuarantine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 9)
)


class _MGuardContFiltQuarantineClean_Type(Integer32):
    """Custom type mGuardContFiltQuarantineClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardContFiltQuarantineClean_Type.__name__ = "Integer32"
_MGuardContFiltQuarantineClean_Object = MibScalar
mGuardContFiltQuarantineClean = _MGuardContFiltQuarantineClean_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 9, 1),
    _MGuardContFiltQuarantineClean_Type()
)
mGuardContFiltQuarantineClean.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltQuarantineClean.setStatus("mandatory")


class _MGuardContFiltQuarantineError_Type(Integer32):
    """Custom type mGuardContFiltQuarantineError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardContFiltQuarantineError_Type.__name__ = "Integer32"
_MGuardContFiltQuarantineError_Object = MibScalar
mGuardContFiltQuarantineError = _MGuardContFiltQuarantineError_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 9, 2),
    _MGuardContFiltQuarantineError_Type()
)
mGuardContFiltQuarantineError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltQuarantineError.setStatus("mandatory")


class _MGuardContFiltQuarantineVirus_Type(Integer32):
    """Custom type mGuardContFiltQuarantineVirus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardContFiltQuarantineVirus_Type.__name__ = "Integer32"
_MGuardContFiltQuarantineVirus_Object = MibScalar
mGuardContFiltQuarantineVirus = _MGuardContFiltQuarantineVirus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 9, 3),
    _MGuardContFiltQuarantineVirus_Type()
)
mGuardContFiltQuarantineVirus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltQuarantineVirus.setStatus("mandatory")
_MGuardContFiltQuarantineSrvIP_Type = DisplayString
_MGuardContFiltQuarantineSrvIP_Object = MibScalar
mGuardContFiltQuarantineSrvIP = _MGuardContFiltQuarantineSrvIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 9, 4),
    _MGuardContFiltQuarantineSrvIP_Type()
)
mGuardContFiltQuarantineSrvIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltQuarantineSrvIP.setStatus("mandatory")
_MGuardContFiltQuarantineSrvPort_Type = DisplayString
_MGuardContFiltQuarantineSrvPort_Object = MibScalar
mGuardContFiltQuarantineSrvPort = _MGuardContFiltQuarantineSrvPort_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 9, 5),
    _MGuardContFiltQuarantineSrvPort_Type()
)
mGuardContFiltQuarantineSrvPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltQuarantineSrvPort.setStatus("mandatory")
_MGuardContFiltInfo_ObjectIdentity = ObjectIdentity
mGuardContFiltInfo = _MGuardContFiltInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 10)
)
_MGuardContFiltInfoFlashID_Type = DisplayString
_MGuardContFiltInfoFlashID_Object = MibScalar
mGuardContFiltInfoFlashID = _MGuardContFiltInfoFlashID_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 1, 10, 1),
    _MGuardContFiltInfoFlashID_Type()
)
mGuardContFiltInfoFlashID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardContFiltInfoFlashID.setStatus("mandatory")
_MGuardContFiltHTTP_ObjectIdentity = ObjectIdentity
mGuardContFiltHTTP = _MGuardContFiltHTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 2)
)


class _MGuardContFiltHTTPEnable_Type(Integer32):
    """Custom type mGuardContFiltHTTPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MGuardContFiltHTTPEnable_Type.__name__ = "Integer32"
_MGuardContFiltHTTPEnable_Object = MibScalar
mGuardContFiltHTTPEnable = _MGuardContFiltHTTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 2, 1),
    _MGuardContFiltHTTPEnable_Type()
)
mGuardContFiltHTTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltHTTPEnable.setStatus("mandatory")


class _MGuardContFiltHTTPVirusAction_Type(Integer32):
    """Custom type mGuardContFiltHTTPVirusAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("error", 1)
    )


_MGuardContFiltHTTPVirusAction_Type.__name__ = "Integer32"
_MGuardContFiltHTTPVirusAction_Object = MibScalar
mGuardContFiltHTTPVirusAction = _MGuardContFiltHTTPVirusAction_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 2, 2),
    _MGuardContFiltHTTPVirusAction_Type()
)
mGuardContFiltHTTPVirusAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltHTTPVirusAction.setStatus("mandatory")


class _MGuardContFiltHTTPMaxSize_Type(Integer32):
    """Custom type mGuardContFiltHTTPMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200000,
              500000,
              1000000,
              2000000,
              4000000,
              5000000,
              8000000,
              10000000)
        )
    )
    namedValues = NamedValues(
        *(("dotfivemeg", 500000),
          ("dottwomeg", 200000),
          ("eightmeg", 8000000),
          ("fivemeg", 5000000),
          ("fourmeg", 4000000),
          ("onemeg", 1000000),
          ("tenmeg", 10000000),
          ("twomeg", 2000000))
    )


_MGuardContFiltHTTPMaxSize_Type.__name__ = "Integer32"
_MGuardContFiltHTTPMaxSize_Object = MibScalar
mGuardContFiltHTTPMaxSize = _MGuardContFiltHTTPMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 2, 3),
    _MGuardContFiltHTTPMaxSize_Type()
)
mGuardContFiltHTTPMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltHTTPMaxSize.setStatus("mandatory")


class _MGuardContFiltHTTPExceedAction_Type(Integer32):
    """Custom type mGuardContFiltHTTPExceedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("pass", 2))
    )


_MGuardContFiltHTTPExceedAction_Type.__name__ = "Integer32"
_MGuardContFiltHTTPExceedAction_Object = MibScalar
mGuardContFiltHTTPExceedAction = _MGuardContFiltHTTPExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 2, 4),
    _MGuardContFiltHTTPExceedAction_Type()
)
mGuardContFiltHTTPExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltHTTPExceedAction.setStatus("mandatory")
_MGuardContFiltHTTPSrvrTable_Object = MibTable
mGuardContFiltHTTPSrvrTable = _MGuardContFiltHTTPSrvrTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 2, 5)
)
if mibBuilder.loadTexts:
    mGuardContFiltHTTPSrvrTable.setStatus("mandatory")
_MGuardContFiltHTTPSrvrEntry_Object = MibTableRow
mGuardContFiltHTTPSrvrEntry = _MGuardContFiltHTTPSrvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 2, 5, 1)
)
mGuardContFiltHTTPSrvrEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardContFiltHTTPSrvrIndex"),
)
if mibBuilder.loadTexts:
    mGuardContFiltHTTPSrvrEntry.setStatus("mandatory")


class _MGuardContFiltHTTPSrvrIndex_Type(Integer32):
    """Custom type mGuardContFiltHTTPSrvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardContFiltHTTPSrvrIndex_Type.__name__ = "Integer32"
_MGuardContFiltHTTPSrvrIndex_Object = MibTableColumn
mGuardContFiltHTTPSrvrIndex = _MGuardContFiltHTTPSrvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 2, 5, 1, 1),
    _MGuardContFiltHTTPSrvrIndex_Type()
)
mGuardContFiltHTTPSrvrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardContFiltHTTPSrvrIndex.setStatus("mandatory")
_MGuardContFiltHTTPSrvrIP_Type = DisplayString
_MGuardContFiltHTTPSrvrIP_Object = MibTableColumn
mGuardContFiltHTTPSrvrIP = _MGuardContFiltHTTPSrvrIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 2, 5, 1, 2),
    _MGuardContFiltHTTPSrvrIP_Type()
)
mGuardContFiltHTTPSrvrIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltHTTPSrvrIP.setStatus("mandatory")
_MGuardContFiltHTTPSrvrPort_Type = DisplayString
_MGuardContFiltHTTPSrvrPort_Object = MibTableColumn
mGuardContFiltHTTPSrvrPort = _MGuardContFiltHTTPSrvrPort_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 2, 5, 1, 3),
    _MGuardContFiltHTTPSrvrPort_Type()
)
mGuardContFiltHTTPSrvrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltHTTPSrvrPort.setStatus("mandatory")


class _MGuardContFiltHTTPSrvrScanAction_Type(Integer32):
    """Custom type mGuardContFiltHTTPSrvrScanAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noscan", 2),
          ("scan", 1))
    )


_MGuardContFiltHTTPSrvrScanAction_Type.__name__ = "Integer32"
_MGuardContFiltHTTPSrvrScanAction_Object = MibTableColumn
mGuardContFiltHTTPSrvrScanAction = _MGuardContFiltHTTPSrvrScanAction_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 2, 5, 1, 4),
    _MGuardContFiltHTTPSrvrScanAction_Type()
)
mGuardContFiltHTTPSrvrScanAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltHTTPSrvrScanAction.setStatus("mandatory")
_MGuardContFiltHTTPSrvrRowStatus_Type = RowStatus
_MGuardContFiltHTTPSrvrRowStatus_Object = MibTableColumn
mGuardContFiltHTTPSrvrRowStatus = _MGuardContFiltHTTPSrvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 2, 5, 1, 5),
    _MGuardContFiltHTTPSrvrRowStatus_Type()
)
mGuardContFiltHTTPSrvrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltHTTPSrvrRowStatus.setStatus("mandatory")
_MGuardContFiltHTTPSrvrComment_Type = DisplayString
_MGuardContFiltHTTPSrvrComment_Object = MibTableColumn
mGuardContFiltHTTPSrvrComment = _MGuardContFiltHTTPSrvrComment_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 2, 5, 1, 6),
    _MGuardContFiltHTTPSrvrComment_Type()
)
mGuardContFiltHTTPSrvrComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltHTTPSrvrComment.setStatus("mandatory")
_MGuardContFiltPOP3_ObjectIdentity = ObjectIdentity
mGuardContFiltPOP3 = _MGuardContFiltPOP3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 3)
)


class _MGuardContFiltPOP3Enable_Type(Integer32):
    """Custom type mGuardContFiltPOP3Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MGuardContFiltPOP3Enable_Type.__name__ = "Integer32"
_MGuardContFiltPOP3Enable_Object = MibScalar
mGuardContFiltPOP3Enable = _MGuardContFiltPOP3Enable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 3, 1),
    _MGuardContFiltPOP3Enable_Type()
)
mGuardContFiltPOP3Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltPOP3Enable.setStatus("mandatory")


class _MGuardContFiltPOP3VirusAction_Type(Integer32):
    """Custom type mGuardContFiltPOP3VirusAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("mail", 2))
    )


_MGuardContFiltPOP3VirusAction_Type.__name__ = "Integer32"
_MGuardContFiltPOP3VirusAction_Object = MibScalar
mGuardContFiltPOP3VirusAction = _MGuardContFiltPOP3VirusAction_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 3, 2),
    _MGuardContFiltPOP3VirusAction_Type()
)
mGuardContFiltPOP3VirusAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltPOP3VirusAction.setStatus("mandatory")


class _MGuardContFiltPOP3MaxSize_Type(Integer32):
    """Custom type mGuardContFiltPOP3MaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200000,
              500000,
              1000000,
              2000000,
              4000000,
              5000000,
              8000000,
              10000000)
        )
    )
    namedValues = NamedValues(
        *(("dotfivemeg", 500000),
          ("dottwomeg", 200000),
          ("eightmeg", 8000000),
          ("fivemeg", 5000000),
          ("fourmeg", 4000000),
          ("onemeg", 1000000),
          ("tenmeg", 10000000),
          ("twomeg", 2000000))
    )


_MGuardContFiltPOP3MaxSize_Type.__name__ = "Integer32"
_MGuardContFiltPOP3MaxSize_Object = MibScalar
mGuardContFiltPOP3MaxSize = _MGuardContFiltPOP3MaxSize_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 3, 3),
    _MGuardContFiltPOP3MaxSize_Type()
)
mGuardContFiltPOP3MaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltPOP3MaxSize.setStatus("mandatory")


class _MGuardContFiltPOP3ExceedAction_Type(Integer32):
    """Custom type mGuardContFiltPOP3ExceedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("pass", 2))
    )


_MGuardContFiltPOP3ExceedAction_Type.__name__ = "Integer32"
_MGuardContFiltPOP3ExceedAction_Object = MibScalar
mGuardContFiltPOP3ExceedAction = _MGuardContFiltPOP3ExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 3, 4),
    _MGuardContFiltPOP3ExceedAction_Type()
)
mGuardContFiltPOP3ExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltPOP3ExceedAction.setStatus("mandatory")
_MGuardContFiltPOP3SrvrTable_Object = MibTable
mGuardContFiltPOP3SrvrTable = _MGuardContFiltPOP3SrvrTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 3, 5)
)
if mibBuilder.loadTexts:
    mGuardContFiltPOP3SrvrTable.setStatus("mandatory")
_MGuardContFiltPOP3SrvrEntry_Object = MibTableRow
mGuardContFiltPOP3SrvrEntry = _MGuardContFiltPOP3SrvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 3, 5, 1)
)
mGuardContFiltPOP3SrvrEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardContFiltPOP3SrvrIndex"),
)
if mibBuilder.loadTexts:
    mGuardContFiltPOP3SrvrEntry.setStatus("mandatory")


class _MGuardContFiltPOP3SrvrIndex_Type(Integer32):
    """Custom type mGuardContFiltPOP3SrvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardContFiltPOP3SrvrIndex_Type.__name__ = "Integer32"
_MGuardContFiltPOP3SrvrIndex_Object = MibTableColumn
mGuardContFiltPOP3SrvrIndex = _MGuardContFiltPOP3SrvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 3, 5, 1, 1),
    _MGuardContFiltPOP3SrvrIndex_Type()
)
mGuardContFiltPOP3SrvrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardContFiltPOP3SrvrIndex.setStatus("mandatory")
_MGuardContFiltPOP3SrvrIP_Type = DisplayString
_MGuardContFiltPOP3SrvrIP_Object = MibTableColumn
mGuardContFiltPOP3SrvrIP = _MGuardContFiltPOP3SrvrIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 3, 5, 1, 2),
    _MGuardContFiltPOP3SrvrIP_Type()
)
mGuardContFiltPOP3SrvrIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltPOP3SrvrIP.setStatus("mandatory")
_MGuardContFiltPOP3SrvrPort_Type = DisplayString
_MGuardContFiltPOP3SrvrPort_Object = MibTableColumn
mGuardContFiltPOP3SrvrPort = _MGuardContFiltPOP3SrvrPort_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 3, 5, 1, 3),
    _MGuardContFiltPOP3SrvrPort_Type()
)
mGuardContFiltPOP3SrvrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltPOP3SrvrPort.setStatus("mandatory")


class _MGuardContFiltPOP3SrvrScanAction_Type(Integer32):
    """Custom type mGuardContFiltPOP3SrvrScanAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noscan", 2),
          ("scan", 1))
    )


_MGuardContFiltPOP3SrvrScanAction_Type.__name__ = "Integer32"
_MGuardContFiltPOP3SrvrScanAction_Object = MibTableColumn
mGuardContFiltPOP3SrvrScanAction = _MGuardContFiltPOP3SrvrScanAction_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 3, 5, 1, 4),
    _MGuardContFiltPOP3SrvrScanAction_Type()
)
mGuardContFiltPOP3SrvrScanAction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardContFiltPOP3SrvrScanAction.setStatus("mandatory")
_MGuardContFiltPOP3SrvrRowStatus_Type = RowStatus
_MGuardContFiltPOP3SrvrRowStatus_Object = MibTableColumn
mGuardContFiltPOP3SrvrRowStatus = _MGuardContFiltPOP3SrvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 3, 5, 1, 5),
    _MGuardContFiltPOP3SrvrRowStatus_Type()
)
mGuardContFiltPOP3SrvrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltPOP3SrvrRowStatus.setStatus("mandatory")
_MGuardContFiltPOP3SrvrComment_Type = DisplayString
_MGuardContFiltPOP3SrvrComment_Object = MibTableColumn
mGuardContFiltPOP3SrvrComment = _MGuardContFiltPOP3SrvrComment_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 3, 5, 1, 6),
    _MGuardContFiltPOP3SrvrComment_Type()
)
mGuardContFiltPOP3SrvrComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltPOP3SrvrComment.setStatus("mandatory")
_MGuardContFiltSMTP_ObjectIdentity = ObjectIdentity
mGuardContFiltSMTP = _MGuardContFiltSMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 4)
)


class _MGuardContFiltSMTPEnable_Type(Integer32):
    """Custom type mGuardContFiltSMTPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MGuardContFiltSMTPEnable_Type.__name__ = "Integer32"
_MGuardContFiltSMTPEnable_Object = MibScalar
mGuardContFiltSMTPEnable = _MGuardContFiltSMTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 4, 1),
    _MGuardContFiltSMTPEnable_Type()
)
mGuardContFiltSMTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltSMTPEnable.setStatus("mandatory")


class _MGuardContFiltSMTPVirusAction_Type(Integer32):
    """Custom type mGuardContFiltSMTPVirusAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("error", 1)
    )


_MGuardContFiltSMTPVirusAction_Type.__name__ = "Integer32"
_MGuardContFiltSMTPVirusAction_Object = MibScalar
mGuardContFiltSMTPVirusAction = _MGuardContFiltSMTPVirusAction_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 4, 2),
    _MGuardContFiltSMTPVirusAction_Type()
)
mGuardContFiltSMTPVirusAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltSMTPVirusAction.setStatus("mandatory")


class _MGuardContFiltSMTPMaxSize_Type(Integer32):
    """Custom type mGuardContFiltSMTPMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200000,
              500000,
              1000000,
              2000000,
              4000000,
              5000000,
              8000000,
              10000000)
        )
    )
    namedValues = NamedValues(
        *(("dotfivemeg", 500000),
          ("dottwomeg", 200000),
          ("eightmeg", 8000000),
          ("fivemeg", 5000000),
          ("fourmeg", 4000000),
          ("onemeg", 1000000),
          ("tenmeg", 10000000),
          ("twomeg", 2000000))
    )


_MGuardContFiltSMTPMaxSize_Type.__name__ = "Integer32"
_MGuardContFiltSMTPMaxSize_Object = MibScalar
mGuardContFiltSMTPMaxSize = _MGuardContFiltSMTPMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 4, 3),
    _MGuardContFiltSMTPMaxSize_Type()
)
mGuardContFiltSMTPMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltSMTPMaxSize.setStatus("mandatory")


class _MGuardContFiltSMTPExceedAction_Type(Integer32):
    """Custom type mGuardContFiltSMTPExceedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("pass", 2))
    )


_MGuardContFiltSMTPExceedAction_Type.__name__ = "Integer32"
_MGuardContFiltSMTPExceedAction_Object = MibScalar
mGuardContFiltSMTPExceedAction = _MGuardContFiltSMTPExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 4, 4),
    _MGuardContFiltSMTPExceedAction_Type()
)
mGuardContFiltSMTPExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltSMTPExceedAction.setStatus("mandatory")
_MGuardContFiltSMTPSrvrTable_Object = MibTable
mGuardContFiltSMTPSrvrTable = _MGuardContFiltSMTPSrvrTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 4, 5)
)
if mibBuilder.loadTexts:
    mGuardContFiltSMTPSrvrTable.setStatus("mandatory")
_MGuardContFiltSMTPSrvrEntry_Object = MibTableRow
mGuardContFiltSMTPSrvrEntry = _MGuardContFiltSMTPSrvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 4, 5, 1)
)
mGuardContFiltSMTPSrvrEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardContFiltSMTPSrvrIndex"),
)
if mibBuilder.loadTexts:
    mGuardContFiltSMTPSrvrEntry.setStatus("mandatory")


class _MGuardContFiltSMTPSrvrIndex_Type(Integer32):
    """Custom type mGuardContFiltSMTPSrvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardContFiltSMTPSrvrIndex_Type.__name__ = "Integer32"
_MGuardContFiltSMTPSrvrIndex_Object = MibTableColumn
mGuardContFiltSMTPSrvrIndex = _MGuardContFiltSMTPSrvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 4, 5, 1, 1),
    _MGuardContFiltSMTPSrvrIndex_Type()
)
mGuardContFiltSMTPSrvrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardContFiltSMTPSrvrIndex.setStatus("mandatory")
_MGuardContFiltSMTPSrvrIP_Type = DisplayString
_MGuardContFiltSMTPSrvrIP_Object = MibTableColumn
mGuardContFiltSMTPSrvrIP = _MGuardContFiltSMTPSrvrIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 4, 5, 1, 2),
    _MGuardContFiltSMTPSrvrIP_Type()
)
mGuardContFiltSMTPSrvrIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltSMTPSrvrIP.setStatus("mandatory")
_MGuardContFiltSMTPSrvrPort_Type = DisplayString
_MGuardContFiltSMTPSrvrPort_Object = MibTableColumn
mGuardContFiltSMTPSrvrPort = _MGuardContFiltSMTPSrvrPort_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 4, 5, 1, 3),
    _MGuardContFiltSMTPSrvrPort_Type()
)
mGuardContFiltSMTPSrvrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltSMTPSrvrPort.setStatus("mandatory")


class _MGuardContFiltSMTPSrvrScanAction_Type(Integer32):
    """Custom type mGuardContFiltSMTPSrvrScanAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noscan", 2),
          ("scan", 1))
    )


_MGuardContFiltSMTPSrvrScanAction_Type.__name__ = "Integer32"
_MGuardContFiltSMTPSrvrScanAction_Object = MibTableColumn
mGuardContFiltSMTPSrvrScanAction = _MGuardContFiltSMTPSrvrScanAction_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 4, 5, 1, 4),
    _MGuardContFiltSMTPSrvrScanAction_Type()
)
mGuardContFiltSMTPSrvrScanAction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardContFiltSMTPSrvrScanAction.setStatus("mandatory")
_MGuardContFiltSMTPSrvrRowStatus_Type = RowStatus
_MGuardContFiltSMTPSrvrRowStatus_Object = MibTableColumn
mGuardContFiltSMTPSrvrRowStatus = _MGuardContFiltSMTPSrvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 4, 5, 1, 5),
    _MGuardContFiltSMTPSrvrRowStatus_Type()
)
mGuardContFiltSMTPSrvrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltSMTPSrvrRowStatus.setStatus("mandatory")
_MGuardContFiltSMTPSrvrComment_Type = DisplayString
_MGuardContFiltSMTPSrvrComment_Object = MibTableColumn
mGuardContFiltSMTPSrvrComment = _MGuardContFiltSMTPSrvrComment_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 4, 5, 1, 6),
    _MGuardContFiltSMTPSrvrComment_Type()
)
mGuardContFiltSMTPSrvrComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltSMTPSrvrComment.setStatus("mandatory")
_MGuardContFiltFTP_ObjectIdentity = ObjectIdentity
mGuardContFiltFTP = _MGuardContFiltFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 5)
)


class _MGuardContFiltFTPEnable_Type(Integer32):
    """Custom type mGuardContFiltFTPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MGuardContFiltFTPEnable_Type.__name__ = "Integer32"
_MGuardContFiltFTPEnable_Object = MibScalar
mGuardContFiltFTPEnable = _MGuardContFiltFTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 5, 1),
    _MGuardContFiltFTPEnable_Type()
)
mGuardContFiltFTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltFTPEnable.setStatus("mandatory")


class _MGuardContFiltFTPVirusAction_Type(Integer32):
    """Custom type mGuardContFiltFTPVirusAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("error", 1)
    )


_MGuardContFiltFTPVirusAction_Type.__name__ = "Integer32"
_MGuardContFiltFTPVirusAction_Object = MibScalar
mGuardContFiltFTPVirusAction = _MGuardContFiltFTPVirusAction_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 5, 2),
    _MGuardContFiltFTPVirusAction_Type()
)
mGuardContFiltFTPVirusAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltFTPVirusAction.setStatus("mandatory")


class _MGuardContFiltFTPMaxSize_Type(Integer32):
    """Custom type mGuardContFiltFTPMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200000,
              500000,
              1000000,
              2000000,
              4000000,
              5000000,
              8000000,
              10000000)
        )
    )
    namedValues = NamedValues(
        *(("dotfivemeg", 500000),
          ("dottwomeg", 200000),
          ("eightmeg", 8000000),
          ("fivemeg", 5000000),
          ("fourmeg", 4000000),
          ("onemeg", 1000000),
          ("tenmeg", 10000000),
          ("twomeg", 2000000))
    )


_MGuardContFiltFTPMaxSize_Type.__name__ = "Integer32"
_MGuardContFiltFTPMaxSize_Object = MibScalar
mGuardContFiltFTPMaxSize = _MGuardContFiltFTPMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 5, 3),
    _MGuardContFiltFTPMaxSize_Type()
)
mGuardContFiltFTPMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltFTPMaxSize.setStatus("mandatory")


class _MGuardContFiltFTPExceedAction_Type(Integer32):
    """Custom type mGuardContFiltFTPExceedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("pass", 2))
    )


_MGuardContFiltFTPExceedAction_Type.__name__ = "Integer32"
_MGuardContFiltFTPExceedAction_Object = MibScalar
mGuardContFiltFTPExceedAction = _MGuardContFiltFTPExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 5, 4),
    _MGuardContFiltFTPExceedAction_Type()
)
mGuardContFiltFTPExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltFTPExceedAction.setStatus("mandatory")
_MGuardContFiltFTPSrvrTable_Object = MibTable
mGuardContFiltFTPSrvrTable = _MGuardContFiltFTPSrvrTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 5, 5)
)
if mibBuilder.loadTexts:
    mGuardContFiltFTPSrvrTable.setStatus("mandatory")
_MGuardContFiltFTPSrvrEntry_Object = MibTableRow
mGuardContFiltFTPSrvrEntry = _MGuardContFiltFTPSrvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 5, 5, 1)
)
mGuardContFiltFTPSrvrEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardContFiltFTPSrvrIndex"),
)
if mibBuilder.loadTexts:
    mGuardContFiltFTPSrvrEntry.setStatus("mandatory")


class _MGuardContFiltFTPSrvrIndex_Type(Integer32):
    """Custom type mGuardContFiltFTPSrvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardContFiltFTPSrvrIndex_Type.__name__ = "Integer32"
_MGuardContFiltFTPSrvrIndex_Object = MibTableColumn
mGuardContFiltFTPSrvrIndex = _MGuardContFiltFTPSrvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 5, 5, 1, 1),
    _MGuardContFiltFTPSrvrIndex_Type()
)
mGuardContFiltFTPSrvrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardContFiltFTPSrvrIndex.setStatus("mandatory")
_MGuardContFiltFTPSrvrIP_Type = DisplayString
_MGuardContFiltFTPSrvrIP_Object = MibTableColumn
mGuardContFiltFTPSrvrIP = _MGuardContFiltFTPSrvrIP_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 5, 5, 1, 2),
    _MGuardContFiltFTPSrvrIP_Type()
)
mGuardContFiltFTPSrvrIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltFTPSrvrIP.setStatus("mandatory")
_MGuardContFiltFTPSrvrPort_Type = DisplayString
_MGuardContFiltFTPSrvrPort_Object = MibTableColumn
mGuardContFiltFTPSrvrPort = _MGuardContFiltFTPSrvrPort_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 5, 5, 1, 3),
    _MGuardContFiltFTPSrvrPort_Type()
)
mGuardContFiltFTPSrvrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltFTPSrvrPort.setStatus("mandatory")


class _MGuardContFiltFTPSrvrScanAction_Type(Integer32):
    """Custom type mGuardContFiltFTPSrvrScanAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noscan", 2),
          ("scan", 1))
    )


_MGuardContFiltFTPSrvrScanAction_Type.__name__ = "Integer32"
_MGuardContFiltFTPSrvrScanAction_Object = MibTableColumn
mGuardContFiltFTPSrvrScanAction = _MGuardContFiltFTPSrvrScanAction_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 5, 5, 1, 4),
    _MGuardContFiltFTPSrvrScanAction_Type()
)
mGuardContFiltFTPSrvrScanAction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardContFiltFTPSrvrScanAction.setStatus("mandatory")
_MGuardContFiltFTPSrvrRowStatus_Type = RowStatus
_MGuardContFiltFTPSrvrRowStatus_Object = MibTableColumn
mGuardContFiltFTPSrvrRowStatus = _MGuardContFiltFTPSrvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 5, 5, 1, 5),
    _MGuardContFiltFTPSrvrRowStatus_Type()
)
mGuardContFiltFTPSrvrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltFTPSrvrRowStatus.setStatus("mandatory")
_MGuardContFiltFTPSrvrComment_Type = DisplayString
_MGuardContFiltFTPSrvrComment_Object = MibTableColumn
mGuardContFiltFTPSrvrComment = _MGuardContFiltFTPSrvrComment_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 12, 5, 5, 1, 6),
    _MGuardContFiltFTPSrvrComment_Type()
)
mGuardContFiltFTPSrvrComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardContFiltFTPSrvrComment.setStatus("mandatory")
_MGuardBlade_ObjectIdentity = ObjectIdentity
mGuardBlade = _MGuardBlade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 13)
)
_MGuardBladeRackID_Type = Integer32
_MGuardBladeRackID_Object = MibScalar
mGuardBladeRackID = _MGuardBladeRackID_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 13, 1),
    _MGuardBladeRackID_Type()
)
mGuardBladeRackID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardBladeRackID.setStatus("mandatory")
_MGuardBladeSlotID_Type = Integer32
_MGuardBladeSlotID_Object = MibScalar
mGuardBladeSlotID = _MGuardBladeSlotID_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 13, 2),
    _MGuardBladeSlotID_Type()
)
mGuardBladeSlotID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardBladeSlotID.setStatus("mandatory")
_MGuardBladeCtrlTable_Object = MibTable
mGuardBladeCtrlTable = _MGuardBladeCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 13, 3)
)
if mibBuilder.loadTexts:
    mGuardBladeCtrlTable.setStatus("mandatory")
_MGuardBladeCtrlEntry_Object = MibTableRow
mGuardBladeCtrlEntry = _MGuardBladeCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 13, 3, 1)
)
mGuardBladeCtrlEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardBladeCtrlIndex"),
)
if mibBuilder.loadTexts:
    mGuardBladeCtrlEntry.setStatus("mandatory")


class _MGuardBladeCtrlIndex_Type(Integer32):
    """Custom type mGuardBladeCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardBladeCtrlIndex_Type.__name__ = "Integer32"
_MGuardBladeCtrlIndex_Object = MibTableColumn
mGuardBladeCtrlIndex = _MGuardBladeCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 13, 3, 1, 1),
    _MGuardBladeCtrlIndex_Type()
)
mGuardBladeCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardBladeCtrlIndex.setStatus("mandatory")
_MGuardBladeCtrlDevice_Type = DisplayString
_MGuardBladeCtrlDevice_Object = MibTableColumn
mGuardBladeCtrlDevice = _MGuardBladeCtrlDevice_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 13, 3, 1, 2),
    _MGuardBladeCtrlDevice_Type()
)
mGuardBladeCtrlDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardBladeCtrlDevice.setStatus("mandatory")


class _MGuardBladeCtrlStatus_Type(Integer32):
    """Custom type mGuardBladeCtrlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("online", 3),
          ("present", 2))
    )


_MGuardBladeCtrlStatus_Type.__name__ = "Integer32"
_MGuardBladeCtrlStatus_Object = MibTableColumn
mGuardBladeCtrlStatus = _MGuardBladeCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 13, 3, 1, 3),
    _MGuardBladeCtrlStatus_Type()
)
mGuardBladeCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardBladeCtrlStatus.setStatus("mandatory")
_MGuardBladeCtrlAVRRevision_Type = DisplayString
_MGuardBladeCtrlAVRRevision_Object = MibTableColumn
mGuardBladeCtrlAVRRevision = _MGuardBladeCtrlAVRRevision_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 13, 3, 1, 4),
    _MGuardBladeCtrlAVRRevision_Type()
)
mGuardBladeCtrlAVRRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardBladeCtrlAVRRevision.setStatus("mandatory")
_MGuardBladeCtrlSlotID_Type = DisplayString
_MGuardBladeCtrlSlotID_Object = MibTableColumn
mGuardBladeCtrlSlotID = _MGuardBladeCtrlSlotID_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 13, 3, 1, 5),
    _MGuardBladeCtrlSlotID_Type()
)
mGuardBladeCtrlSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardBladeCtrlSlotID.setStatus("mandatory")
_MGuardBladeCtrlProductID_Type = DisplayString
_MGuardBladeCtrlProductID_Object = MibTableColumn
mGuardBladeCtrlProductID = _MGuardBladeCtrlProductID_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 13, 3, 1, 6),
    _MGuardBladeCtrlProductID_Type()
)
mGuardBladeCtrlProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardBladeCtrlProductID.setStatus("mandatory")
_MGuardBladeCtrlAssemblyID_Type = DisplayString
_MGuardBladeCtrlAssemblyID_Object = MibTableColumn
mGuardBladeCtrlAssemblyID = _MGuardBladeCtrlAssemblyID_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 13, 3, 1, 7),
    _MGuardBladeCtrlAssemblyID_Type()
)
mGuardBladeCtrlAssemblyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardBladeCtrlAssemblyID.setStatus("mandatory")
_MGuardBladeCtrlSerial_Type = DisplayString
_MGuardBladeCtrlSerial_Object = MibTableColumn
mGuardBladeCtrlSerial = _MGuardBladeCtrlSerial_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 13, 3, 1, 8),
    _MGuardBladeCtrlSerial_Type()
)
mGuardBladeCtrlSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardBladeCtrlSerial.setStatus("mandatory")
_MGuardBladeCtrlFlashID_Type = DisplayString
_MGuardBladeCtrlFlashID_Object = MibTableColumn
mGuardBladeCtrlFlashID = _MGuardBladeCtrlFlashID_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 13, 3, 1, 9),
    _MGuardBladeCtrlFlashID_Type()
)
mGuardBladeCtrlFlashID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardBladeCtrlFlashID.setStatus("mandatory")
_MGuardBladeCtrlVersion_Type = DisplayString
_MGuardBladeCtrlVersion_Object = MibTableColumn
mGuardBladeCtrlVersion = _MGuardBladeCtrlVersion_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 13, 3, 1, 10),
    _MGuardBladeCtrlVersion_Type()
)
mGuardBladeCtrlVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardBladeCtrlVersion.setStatus("mandatory")


class _MGuardBladeCtrlBackup_Type(Integer32):
    """Custom type mGuardBladeCtrlBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardBladeCtrlBackup_Type.__name__ = "Integer32"
_MGuardBladeCtrlBackup_Object = MibTableColumn
mGuardBladeCtrlBackup = _MGuardBladeCtrlBackup_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 13, 3, 1, 11),
    _MGuardBladeCtrlBackup_Type()
)
mGuardBladeCtrlBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardBladeCtrlBackup.setStatus("mandatory")


class _MGuardBladeCtrlRestore_Type(Integer32):
    """Custom type mGuardBladeCtrlRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MGuardBladeCtrlRestore_Type.__name__ = "Integer32"
_MGuardBladeCtrlRestore_Object = MibTableColumn
mGuardBladeCtrlRestore = _MGuardBladeCtrlRestore_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 13, 3, 1, 12),
    _MGuardBladeCtrlRestore_Type()
)
mGuardBladeCtrlRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardBladeCtrlRestore.setStatus("mandatory")
_MGuardBladePwrTable_Object = MibTable
mGuardBladePwrTable = _MGuardBladePwrTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 13, 4)
)
if mibBuilder.loadTexts:
    mGuardBladePwrTable.setStatus("mandatory")
_MGuardBladePwrEntry_Object = MibTableRow
mGuardBladePwrEntry = _MGuardBladePwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 13, 4, 1)
)
mGuardBladePwrEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardBladePwrIndex"),
)
if mibBuilder.loadTexts:
    mGuardBladePwrEntry.setStatus("mandatory")


class _MGuardBladePwrIndex_Type(Integer32):
    """Custom type mGuardBladePwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardBladePwrIndex_Type.__name__ = "Integer32"
_MGuardBladePwrIndex_Object = MibTableColumn
mGuardBladePwrIndex = _MGuardBladePwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 13, 4, 1, 1),
    _MGuardBladePwrIndex_Type()
)
mGuardBladePwrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardBladePwrIndex.setStatus("mandatory")


class _MGuardBladePwrStatus_Type(Integer32):
    """Custom type mGuardBladePwrStatus based on Integer32"""
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
        *(("absent", 1),
          ("defect", 3),
          ("fatal", 2),
          ("ok", 4))
    )


_MGuardBladePwrStatus_Type.__name__ = "Integer32"
_MGuardBladePwrStatus_Object = MibTableColumn
mGuardBladePwrStatus = _MGuardBladePwrStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 13, 4, 1, 2),
    _MGuardBladePwrStatus_Type()
)
mGuardBladePwrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGuardBladePwrStatus.setStatus("mandatory")
_MGuardProfile_ObjectIdentity = ObjectIdentity
mGuardProfile = _MGuardProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 14)
)
_MGuardProfilePush_ObjectIdentity = ObjectIdentity
mGuardProfilePush = _MGuardProfilePush_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 14, 1)
)
_MGuardProfilePull_ObjectIdentity = ObjectIdentity
mGuardProfilePull = _MGuardProfilePull_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 14, 2)
)


class _MGuardProfilePullSchedule_Type(Integer32):
    """Custom type mGuardProfilePullSchedule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              15,
              30,
              60,
              120,
              360,
              720,
              1440)
        )
    )
    namedValues = NamedValues(
        *(("bihourly", 120),
          ("halfhourly", 30),
          ("hourly", 60),
          ("never", 1),
          ("onboot", 2),
          ("quarterhourly", 15),
          ("sixhourly", 720),
          ("triplehourly", 360),
          ("twicedayly", 1440))
    )


_MGuardProfilePullSchedule_Type.__name__ = "Integer32"
_MGuardProfilePullSchedule_Object = MibScalar
mGuardProfilePullSchedule = _MGuardProfilePullSchedule_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 14, 2, 1),
    _MGuardProfilePullSchedule_Type()
)
mGuardProfilePullSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardProfilePullSchedule.setStatus("mandatory")
_MGuardProfilePullHTTPS_ObjectIdentity = ObjectIdentity
mGuardProfilePullHTTPS = _MGuardProfilePullHTTPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 14, 2, 2)
)
_MGuardProfilePullHTTPSCert_Type = DisplayString
_MGuardProfilePullHTTPSCert_Object = MibScalar
mGuardProfilePullHTTPSCert = _MGuardProfilePullHTTPSCert_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 14, 2, 2, 1),
    _MGuardProfilePullHTTPSCert_Type()
)
mGuardProfilePullHTTPSCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardProfilePullHTTPSCert.setStatus("mandatory")
_MGuardProfilePullHTTPSServer_Type = DisplayString
_MGuardProfilePullHTTPSServer_Object = MibScalar
mGuardProfilePullHTTPSServer = _MGuardProfilePullHTTPSServer_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 14, 2, 2, 2),
    _MGuardProfilePullHTTPSServer_Type()
)
mGuardProfilePullHTTPSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardProfilePullHTTPSServer.setStatus("mandatory")
_MGuardProfilePullHTTPSPort_Type = DisplayString
_MGuardProfilePullHTTPSPort_Object = MibScalar
mGuardProfilePullHTTPSPort = _MGuardProfilePullHTTPSPort_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 14, 2, 2, 3),
    _MGuardProfilePullHTTPSPort_Type()
)
mGuardProfilePullHTTPSPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardProfilePullHTTPSPort.setStatus("mandatory")
_MGuardProfilePullHTTPSFile_Type = DisplayString
_MGuardProfilePullHTTPSFile_Object = MibScalar
mGuardProfilePullHTTPSFile = _MGuardProfilePullHTTPSFile_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 14, 2, 2, 4),
    _MGuardProfilePullHTTPSFile_Type()
)
mGuardProfilePullHTTPSFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardProfilePullHTTPSFile.setStatus("mandatory")
_MGuardProfilePullHTTPSLogin_Type = DisplayString
_MGuardProfilePullHTTPSLogin_Object = MibScalar
mGuardProfilePullHTTPSLogin = _MGuardProfilePullHTTPSLogin_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 14, 2, 2, 5),
    _MGuardProfilePullHTTPSLogin_Type()
)
mGuardProfilePullHTTPSLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardProfilePullHTTPSLogin.setStatus("mandatory")
_MGuardProfilePullHTTPSPasswd_Type = DisplayString
_MGuardProfilePullHTTPSPasswd_Object = MibScalar
mGuardProfilePullHTTPSPasswd = _MGuardProfilePullHTTPSPasswd_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 14, 2, 2, 6),
    _MGuardProfilePullHTTPSPasswd_Type()
)
mGuardProfilePullHTTPSPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardProfilePullHTTPSPasswd.setStatus("mandatory")
_MGuardProfilePullHTTPSDirectory_Type = DisplayString
_MGuardProfilePullHTTPSDirectory_Object = MibScalar
mGuardProfilePullHTTPSDirectory = _MGuardProfilePullHTTPSDirectory_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 14, 2, 2, 7),
    _MGuardProfilePullHTTPSDirectory_Type()
)
mGuardProfilePullHTTPSDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardProfilePullHTTPSDirectory.setStatus("mandatory")
_MGuardUsers_ObjectIdentity = ObjectIdentity
mGuardUsers = _MGuardUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 15)
)
_MGuardRemoteUsers_ObjectIdentity = ObjectIdentity
mGuardRemoteUsers = _MGuardRemoteUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 15, 1)
)
_MGuardRADIUS_ObjectIdentity = ObjectIdentity
mGuardRADIUS = _MGuardRADIUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 15, 1, 1)
)


class _MGuardRADIUSTimeout_Type(Integer32):
    """Custom type mGuardRADIUSTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardRADIUSTimeout_Type.__name__ = "Integer32"
_MGuardRADIUSTimeout_Object = MibScalar
mGuardRADIUSTimeout = _MGuardRADIUSTimeout_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 15, 1, 1, 1),
    _MGuardRADIUSTimeout_Type()
)
mGuardRADIUSTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRADIUSTimeout.setStatus("mandatory")


class _MGuardRADIUSRetries_Type(Integer32):
    """Custom type mGuardRADIUSRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardRADIUSRetries_Type.__name__ = "Integer32"
_MGuardRADIUSRetries_Object = MibScalar
mGuardRADIUSRetries = _MGuardRADIUSRetries_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 15, 1, 1, 2),
    _MGuardRADIUSRetries_Type()
)
mGuardRADIUSRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRADIUSRetries.setStatus("mandatory")
_MGuardRADIUSServerTable_Object = MibTable
mGuardRADIUSServerTable = _MGuardRADIUSServerTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 15, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mGuardRADIUSServerTable.setStatus("mandatory")
_MGuardRADIUSServerEntry_Object = MibTableRow
mGuardRADIUSServerEntry = _MGuardRADIUSServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 15, 1, 1, 3, 1)
)
mGuardRADIUSServerEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardRADIUSServerIndex"),
)
if mibBuilder.loadTexts:
    mGuardRADIUSServerEntry.setStatus("mandatory")


class _MGuardRADIUSServerIndex_Type(Integer32):
    """Custom type mGuardRADIUSServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardRADIUSServerIndex_Type.__name__ = "Integer32"
_MGuardRADIUSServerIndex_Object = MibTableColumn
mGuardRADIUSServerIndex = _MGuardRADIUSServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 15, 1, 1, 3, 1, 1),
    _MGuardRADIUSServerIndex_Type()
)
mGuardRADIUSServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardRADIUSServerIndex.setStatus("mandatory")
_MGuardRADIUSServerHostname_Type = DisplayString
_MGuardRADIUSServerHostname_Object = MibTableColumn
mGuardRADIUSServerHostname = _MGuardRADIUSServerHostname_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 15, 1, 1, 3, 1, 2),
    _MGuardRADIUSServerHostname_Type()
)
mGuardRADIUSServerHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRADIUSServerHostname.setStatus("mandatory")


class _MGuardRADIUSServerPort_Type(Integer32):
    """Custom type mGuardRADIUSServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MGuardRADIUSServerPort_Type.__name__ = "Integer32"
_MGuardRADIUSServerPort_Object = MibTableColumn
mGuardRADIUSServerPort = _MGuardRADIUSServerPort_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 15, 1, 1, 3, 1, 3),
    _MGuardRADIUSServerPort_Type()
)
mGuardRADIUSServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRADIUSServerPort.setStatus("mandatory")
_MGuardRADIUSServerSecret_Type = DisplayString
_MGuardRADIUSServerSecret_Object = MibTableColumn
mGuardRADIUSServerSecret = _MGuardRADIUSServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 15, 1, 1, 3, 1, 4),
    _MGuardRADIUSServerSecret_Type()
)
mGuardRADIUSServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRADIUSServerSecret.setStatus("mandatory")
_MGuardRADIUSServerRowStatus_Type = RowStatus
_MGuardRADIUSServerRowStatus_Object = MibTableColumn
mGuardRADIUSServerRowStatus = _MGuardRADIUSServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 15, 1, 1, 3, 1, 5),
    _MGuardRADIUSServerRowStatus_Type()
)
mGuardRADIUSServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardRADIUSServerRowStatus.setStatus("mandatory")
_MGuardUserFWUsers_ObjectIdentity = ObjectIdentity
mGuardUserFWUsers = _MGuardUserFWUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 2, 15, 1, 2)
)
_MGuardUserFWUserTable_Object = MibTable
mGuardUserFWUserTable = _MGuardUserFWUserTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 15, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mGuardUserFWUserTable.setStatus("mandatory")
_MGuardUserFWUserEntry_Object = MibTableRow
mGuardUserFWUserEntry = _MGuardUserFWUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 15, 1, 2, 1, 1)
)
mGuardUserFWUserEntry.setIndexNames(
    (0, "MGUARDB-MIB", "mGuardUserFWUserIndex"),
)
if mibBuilder.loadTexts:
    mGuardUserFWUserEntry.setStatus("mandatory")


class _MGuardUserFWUserIndex_Type(Integer32):
    """Custom type mGuardUserFWUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MGuardUserFWUserIndex_Type.__name__ = "Integer32"
_MGuardUserFWUserIndex_Object = MibTableColumn
mGuardUserFWUserIndex = _MGuardUserFWUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 15, 1, 2, 1, 1, 1),
    _MGuardUserFWUserIndex_Type()
)
mGuardUserFWUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGuardUserFWUserIndex.setStatus("mandatory")
_MGuardUserFWUserName_Type = DisplayString
_MGuardUserFWUserName_Object = MibTableColumn
mGuardUserFWUserName = _MGuardUserFWUserName_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 15, 1, 2, 1, 1, 2),
    _MGuardUserFWUserName_Type()
)
mGuardUserFWUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardUserFWUserName.setStatus("mandatory")


class _MGuardUserFWUserAuthMethod_Type(Integer32):
    """Custom type mGuardUserFWUserAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("radius", 1))
    )


_MGuardUserFWUserAuthMethod_Type.__name__ = "Integer32"
_MGuardUserFWUserAuthMethod_Object = MibTableColumn
mGuardUserFWUserAuthMethod = _MGuardUserFWUserAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 15, 1, 2, 1, 1, 3),
    _MGuardUserFWUserAuthMethod_Type()
)
mGuardUserFWUserAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardUserFWUserAuthMethod.setStatus("mandatory")
_MGuardUserFWUserPassword_Type = DisplayString
_MGuardUserFWUserPassword_Object = MibTableColumn
mGuardUserFWUserPassword = _MGuardUserFWUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 15, 1, 2, 1, 1, 4),
    _MGuardUserFWUserPassword_Type()
)
mGuardUserFWUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardUserFWUserPassword.setStatus("mandatory")
_MGuardUserFWUserRowStatus_Type = RowStatus
_MGuardUserFWUserRowStatus_Object = MibTableColumn
mGuardUserFWUserRowStatus = _MGuardUserFWUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 2, 15, 1, 2, 1, 1, 5),
    _MGuardUserFWUserRowStatus_Type()
)
mGuardUserFWUserRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGuardUserFWUserRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mGuardHTTPSLoginTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 15450, 2, 0, 1)
)
mGuardHTTPSLoginTrap.setObjects(
    ("MGUARDB-MIB", "mGuardHTTPSLastAccessIP")
)
if mibBuilder.loadTexts:
    mGuardHTTPSLoginTrap.setStatus(
        ""
    )

mGuardShellLoginTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 15450, 2, 0, 2)
)
mGuardShellLoginTrap.setObjects(
    ("MGUARDB-MIB", "mGuardShellLastAccessIP")
)
if mibBuilder.loadTexts:
    mGuardShellLoginTrap.setStatus(
        ""
    )

mGuardDHCPNewClientTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 15450, 2, 0, 3)
)
mGuardDHCPNewClientTrap.setObjects(
    ("MGUARDB-MIB", "mGuardDHCPLastAccessMAC")
)
if mibBuilder.loadTexts:
    mGuardDHCPNewClientTrap.setStatus(
        ""
    )

mGuardTrapDiscFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 5, 0, 1)
)
mGuardTrapDiscFull.setObjects(
    ("MGUARDB-MIB", "mGuardTResDiscFull")
)
if mibBuilder.loadTexts:
    mGuardTrapDiscFull.setStatus(
        ""
    )

mGuardTrapCpuLoadHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 5, 0, 2)
)
mGuardTrapCpuLoadHigh.setObjects(
    ("MGUARDB-MIB", "mGuardTResCpuLoadHigh")
)
if mibBuilder.loadTexts:
    mGuardTrapCpuLoadHigh.setStatus(
        ""
    )

mGuardTrapMemoryFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 5, 0, 3)
)
mGuardTrapMemoryFull.setObjects(
    ("MGUARDB-MIB", "mGuardTResMemoryFull")
)
if mibBuilder.loadTexts:
    mGuardTrapMemoryFull.setStatus(
        ""
    )

mGuardTrapColdstart = NotificationType(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 5, 0, 4)
)
mGuardTrapColdstart.setObjects(
    ("MGUARDB-MIB", "mGuardTResColdstart")
)
if mibBuilder.loadTexts:
    mGuardTrapColdstart.setStatus(
        ""
    )

mGuardTrapAvUpdateDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 6, 0, 1)
)
mGuardTrapAvUpdateDone.setObjects(
    ("MGUARDB-MIB", "mGuardTResAvUpdateDone")
)
if mibBuilder.loadTexts:
    mGuardTrapAvUpdateDone.setStatus(
        ""
    )

mGuardTrapAvUpdateError = NotificationType(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 6, 0, 2)
)
mGuardTrapAvUpdateError.setObjects(
    ("MGUARDB-MIB", "mGuardTResAvUpdateError")
)
if mibBuilder.loadTexts:
    mGuardTrapAvUpdateError.setStatus(
        ""
    )

mGuardTrapAvVirusDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 6, 0, 3)
)
mGuardTrapAvVirusDetected.setObjects(
    ("MGUARDB-MIB", "mGuardTResAvVirusDetected")
)
if mibBuilder.loadTexts:
    mGuardTrapAvVirusDetected.setStatus(
        ""
    )

mGuardTrapAvFileNotScanned = NotificationType(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 6, 0, 4)
)
mGuardTrapAvFileNotScanned.setObjects(
    ("MGUARDB-MIB", "mGuardTResAvFileNotScanned")
)
if mibBuilder.loadTexts:
    mGuardTrapAvFileNotScanned.setStatus(
        ""
    )

mGuardTrapAvFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 6, 0, 5)
)
mGuardTrapAvFailed.setObjects(
    ("MGUARDB-MIB", "mGuardTResAvFailed")
)
if mibBuilder.loadTexts:
    mGuardTrapAvFailed.setStatus(
        ""
    )

mGuardTrapIndustrialTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 7, 1, 0, 1)
)
mGuardTrapIndustrialTemperature.setObjects(
      *(("MGUARDB-MIB", "mGuardSystemTemperature"),
        ("MGUARDB-MIB", "mGuardTResIndustrialTempHiLimit"),
        ("MGUARDB-MIB", "mGuardTResIndustrialTempLowLimit"))
)
if mibBuilder.loadTexts:
    mGuardTrapIndustrialTemperature.setStatus(
        ""
    )

mGuardTrapIndustrialPowerStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 7, 1, 0, 2)
)
mGuardTrapIndustrialPowerStatus.setObjects(
    ("MGUARDB-MIB", "mGuardPSState")
)
if mibBuilder.loadTexts:
    mGuardTrapIndustrialPowerStatus.setStatus(
        ""
    )

mGuardTrapSignalRelais = NotificationType(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 7, 1, 0, 3)
)
mGuardTrapSignalRelais.setObjects(
      *(("MGUARDB-MIB", "mGuardTResSignalRelaisState"),
        ("MGUARDB-MIB", "mGuardTResSignalRelaisReason"),
        ("MGUARDB-MIB", "mGuardTResSignalRelaisReasonIdx"))
)
if mibBuilder.loadTexts:
    mGuardTrapSignalRelais.setStatus(
        ""
    )

mGuardTrapAutoConfigAdapterState = NotificationType(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 7, 1, 0, 4)
)
mGuardTrapAutoConfigAdapterState.setObjects(
    ("MGUARDB-MIB", "mGuardTResAutoConfigAdapterState")
)
if mibBuilder.loadTexts:
    mGuardTrapAutoConfigAdapterState.setStatus(
        ""
    )

mGuardTrapBladeCtrlPowerStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 7, 2, 0, 2)
)
mGuardTrapBladeCtrlPowerStatus.setObjects(
      *(("MGUARDB-MIB", "mGuardTResBladeRackID"),
        ("MGUARDB-MIB", "mGuardTResBladeSlotNr"),
        ("MGUARDB-MIB", "mGuardTResBladeCtrlPowerStatus"))
)
if mibBuilder.loadTexts:
    mGuardTrapBladeCtrlPowerStatus.setStatus(
        ""
    )

mGuardTrapBladeCtrlRunStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 7, 2, 0, 3)
)
mGuardTrapBladeCtrlRunStatus.setObjects(
      *(("MGUARDB-MIB", "mGuardTResBladeRackID"),
        ("MGUARDB-MIB", "mGuardTResBladeSlotNr"),
        ("MGUARDB-MIB", "mGuardTResBladeCtrlRunStatus"))
)
if mibBuilder.loadTexts:
    mGuardTrapBladeCtrlRunStatus.setStatus(
        ""
    )

mGuardTrapBladeCtrlCfgBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 7, 2, 5, 0, 1)
)
mGuardTrapBladeCtrlCfgBackup.setObjects(
      *(("MGUARDB-MIB", "mGuardTResBladeRackID"),
        ("MGUARDB-MIB", "mGuardTResBladeSlotNr"),
        ("MGUARDB-MIB", "mGuardTResBladeCtrlCfgBackup"))
)
if mibBuilder.loadTexts:
    mGuardTrapBladeCtrlCfgBackup.setStatus(
        ""
    )

mGuardTrapBladeCtrlCfgRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 7, 2, 5, 0, 2)
)
mGuardTrapBladeCtrlCfgRestored.setObjects(
      *(("MGUARDB-MIB", "mGuardTResBladeRackID"),
        ("MGUARDB-MIB", "mGuardTResBladeSlotNr"),
        ("MGUARDB-MIB", "mGuardTResBladeCtrlCfgRestored"))
)
if mibBuilder.loadTexts:
    mGuardTrapBladeCtrlCfgRestored.setStatus(
        ""
    )

mGuardTrapRouterRedundancyStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 8, 0, 1)
)
mGuardTrapRouterRedundancyStatusChange.setObjects(
      *(("MGUARDB-MIB", "mGuardRouterRedundancyState"),
        ("MGUARDB-MIB", "mGuardTResRedundacyReason"))
)
if mibBuilder.loadTexts:
    mGuardTrapRouterRedundancyStatusChange.setStatus(
        ""
    )

mGuardTrapRouterRedundancyBackupDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 15450, 2, 10, 8, 0, 2)
)
mGuardTrapRouterRedundancyBackupDown.setObjects(
    ("MGUARDB-MIB", "mGuardTResRedundacyBackupDown")
)
if mibBuilder.loadTexts:
    mGuardTrapRouterRedundancyBackupDown.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MGUARDB-MIB",
    **{"innominate": innominate,
       "mGuardb": mGuardb,
       "mGuardHTTPSLoginTrap": mGuardHTTPSLoginTrap,
       "mGuardShellLoginTrap": mGuardShellLoginTrap,
       "mGuardDHCPNewClientTrap": mGuardDHCPNewClientTrap,
       "mGuardVPN": mGuardVPN,
       "mGuardVPNMachine": mGuardVPNMachine,
       "mGuardVPNMachineCert": mGuardVPNMachineCert,
       "mGuardVPNMachinePrivate": mGuardVPNMachinePrivate,
       "mGuardVPNConnectionTable": mGuardVPNConnectionTable,
       "mGuardVPNConnectionEntry": mGuardVPNConnectionEntry,
       "mGuardVPNconIndex": mGuardVPNconIndex,
       "mGuardVPNconName": mGuardVPNconName,
       "mGuardVPNconEnabled": mGuardVPNconEnabled,
       "mGuardVPNremGW": mGuardVPNremGW,
       "mGuardVPNconType": mGuardVPNconType,
       "mGuardVPNlocalNet": mGuardVPNlocalNet,
       "mGuardVPNlocalMask": mGuardVPNlocalMask,
       "mGuardVPNremoteNet": mGuardVPNremoteNet,
       "mGuardVPNremoteMask": mGuardVPNremoteMask,
       "mGuardVPNauthType": mGuardVPNauthType,
       "mGuardVPNpsk": mGuardVPNpsk,
       "mGuardVPNx509": mGuardVPNx509,
       "mGuardVPNikeDH": mGuardVPNikeDH,
       "mGuardVPNikeHash": mGuardVPNikeHash,
       "mGuardVPNipsecHash": mGuardVPNipsecHash,
       "mGuardVPNikeAlg": mGuardVPNikeAlg,
       "mGuardVPNipsecAlg": mGuardVPNipsecAlg,
       "mGuardVPNpfs": mGuardVPNpfs,
       "mGuardVPNconStartUp": mGuardVPNconStartUp,
       "mGuardVPNvirtIPMethod": mGuardVPNvirtIPMethod,
       "mGuardVPNvirtIP": mGuardVPNvirtIP,
       "mGuardVPNFWLogDefIn": mGuardVPNFWLogDefIn,
       "mGuardVPNFWLogDefOut": mGuardVPNFWLogDefOut,
       "mGuardVPNProtoAH": mGuardVPNProtoAH,
       "mGuardVPNProtoESP": mGuardVPNProtoESP,
       "mGuardVPNComp": mGuardVPNComp,
       "mGuardVPNLocalIDMode": mGuardVPNLocalIDMode,
       "mGuardVPNLocalID": mGuardVPNLocalID,
       "mGuardVPNRemoteIDMode": mGuardVPNRemoteIDMode,
       "mGuardVPNRemoteID": mGuardVPNRemoteID,
       "mGuardVPNIkeLifetime": mGuardVPNIkeLifetime,
       "mGuardVPNIpsecLifetime": mGuardVPNIpsecLifetime,
       "mGuardVPNRekeyMargin": mGuardVPNRekeyMargin,
       "mGuardVPNRekeyFuzz": mGuardVPNRekeyFuzz,
       "mGuardVPNKeyingTries": mGuardVPNKeyingTries,
       "mGuardVPNRekey": mGuardVPNRekey,
       "mGuardVPNDPDAction": mGuardVPNDPDAction,
       "mGuardVPNDPDDelay": mGuardVPNDPDDelay,
       "mGuardVPNDPDTimeout": mGuardVPNDPDTimeout,
       "mGuardVPNRowStatus": mGuardVPNRowStatus,
       "mGuardVPNAggressive": mGuardVPNAggressive,
       "mGuardVPNlocal": mGuardVPNlocal,
       "mGuardVPNremote": mGuardVPNremote,
       "mGuardVPNFW": mGuardVPNFW,
       "mGuardVPNFWINTable": mGuardVPNFWINTable,
       "mGuardVPNFWINEntry": mGuardVPNFWINEntry,
       "mGuardVPNFWINconIndex": mGuardVPNFWINconIndex,
       "mGuardVPNFWINruleIndex": mGuardVPNFWINruleIndex,
       "mGuardVPNFWINsourceIP": mGuardVPNFWINsourceIP,
       "mGuardVPNFWINdestinationIP": mGuardVPNFWINdestinationIP,
       "mGuardVPNFWINsport": mGuardVPNFWINsport,
       "mGuardVPNFWINdport": mGuardVPNFWINdport,
       "mGuardVPNFWINtarget": mGuardVPNFWINtarget,
       "mGuardVPNFWINproto": mGuardVPNFWINproto,
       "mGuardVPNFWINlog": mGuardVPNFWINlog,
       "mGuardVPNFWINRowStatus": mGuardVPNFWINRowStatus,
       "mGuardVPNFWINcomment": mGuardVPNFWINcomment,
       "mGuardVPNFWOUTTable": mGuardVPNFWOUTTable,
       "mGuardVPNFWOUTEntry": mGuardVPNFWOUTEntry,
       "mGuardVPNFWOUTconIndex": mGuardVPNFWOUTconIndex,
       "mGuardVPNFWOUTruleIndex": mGuardVPNFWOUTruleIndex,
       "mGuardVPNFWOUTsourceIP": mGuardVPNFWOUTsourceIP,
       "mGuardVPNFWOUTdestinationIP": mGuardVPNFWOUTdestinationIP,
       "mGuardVPNFWOUTsport": mGuardVPNFWOUTsport,
       "mGuardVPNFWOUTdport": mGuardVPNFWOUTdport,
       "mGuardVPNFWOUTtarget": mGuardVPNFWOUTtarget,
       "mGuardVPNFWOUTproto": mGuardVPNFWOUTproto,
       "mGuardVPNFWOUTlog": mGuardVPNFWOUTlog,
       "mGuardVPNFWOUTRowStatus": mGuardVPNFWOUTRowStatus,
       "mGuardVPNFWOUTcomment": mGuardVPNFWOUTcomment,
       "mGuardVPNDynDNS": mGuardVPNDynDNS,
       "mGuardVPNDynDNSRegister": mGuardVPNDynDNSRegister,
       "mGuardVPNDynDNSReg": mGuardVPNDynDNSReg,
       "mGuardVPNDynDNSRegInterval": mGuardVPNDynDNSRegInterval,
       "mGuardVPNDynDNSRegServer": mGuardVPNDynDNSRegServer,
       "mGuardVPNDynDNSRegLogin": mGuardVPNDynDNSRegLogin,
       "mGuardVPNDynDNSRegPasswd": mGuardVPNDynDNSRegPasswd,
       "mGuardVPNDynDNSRegProvider": mGuardVPNDynDNSRegProvider,
       "mGuardVPNDynDNSRegHostname": mGuardVPNDynDNSRegHostname,
       "mGuardVPNDynDNSCheck": mGuardVPNDynDNSCheck,
       "mGuardVPNDynDNSCheckDo": mGuardVPNDynDNSCheckDo,
       "mGuardVPNDynDNSCheckRefresh": mGuardVPNDynDNSCheckRefresh,
       "mGuardVPNL2TP": mGuardVPNL2TP,
       "mGuardVPNL2TPStart": mGuardVPNL2TPStart,
       "mGuardVPNL2TPLocalIP": mGuardVPNL2TPLocalIP,
       "mGuardVPNL2TPRemoteIPRangeStart": mGuardVPNL2TPRemoteIPRangeStart,
       "mGuardVPNL2TPRemoteIPRangeEnd": mGuardVPNL2TPRemoteIPRangeEnd,
       "mGuardVPNL2TPpppdOptTable": mGuardVPNL2TPpppdOptTable,
       "mGuardVPNL2TPpppdOptEntry": mGuardVPNL2TPpppdOptEntry,
       "mGuardVPNL2TPpppdOptIndex": mGuardVPNL2TPpppdOptIndex,
       "mGuardVPNL2TPpppdOptValue": mGuardVPNL2TPpppdOptValue,
       "mGuardVPNL2TPpppdOptRowStatus": mGuardVPNL2TPpppdOptRowStatus,
       "mGuardVPNSettings": mGuardVPNSettings,
       "mGuardVPNRequireUniqueIDs": mGuardVPNRequireUniqueIDs,
       "mGuardVPNNatTraversal": mGuardVPNNatTraversal,
       "mGuardVPNNatTPortfloating": mGuardVPNNatTPortfloating,
       "mGuardVPNNatTKeepAliveInterval": mGuardVPNNatTKeepAliveInterval,
       "mGuardVPNNatTKeepAliveForce": mGuardVPNNatTKeepAliveForce,
       "mGuardVPNIkeLog": mGuardVPNIkeLog,
       "mGuardVPNHideTos": mGuardVPNHideTos,
       "mGuardVPNmtu": mGuardVPNmtu,
       "mGuardVPNStrictCRLPolicy": mGuardVPNStrictCRLPolicy,
       "mGuardVPNNoCertReqSend": mGuardVPNNoCertReqSend,
       "mGuardFirewall": mGuardFirewall,
       "mGuardFirewallIncoming": mGuardFirewallIncoming,
       "mGuardFirewallIncomingTable": mGuardFirewallIncomingTable,
       "mGuardFirewallIncomingEntry": mGuardFirewallIncomingEntry,
       "mGuardFWINruleIndex": mGuardFWINruleIndex,
       "mGuardFWINsourceIP": mGuardFWINsourceIP,
       "mGuardFWINdestinationIP": mGuardFWINdestinationIP,
       "mGuardFWINsport": mGuardFWINsport,
       "mGuardFWINdport": mGuardFWINdport,
       "mGuardFWINtarget": mGuardFWINtarget,
       "mGuardFWINproto": mGuardFWINproto,
       "mGuardFWINlog": mGuardFWINlog,
       "mGuardFWINRowStatus": mGuardFWINRowStatus,
       "mGuardFWINcomment": mGuardFWINcomment,
       "mGuardFirewallINLogDefault": mGuardFirewallINLogDefault,
       "mGuardFirewallOutgoing": mGuardFirewallOutgoing,
       "mGuardFirewallOutgoingTable": mGuardFirewallOutgoingTable,
       "mGuardFirewallOutgoingEntry": mGuardFirewallOutgoingEntry,
       "mGuardFWOUTruleIndex": mGuardFWOUTruleIndex,
       "mGuardFWOUTsourceIP": mGuardFWOUTsourceIP,
       "mGuardFWOUTdestinationIP": mGuardFWOUTdestinationIP,
       "mGuardFWOUTsport": mGuardFWOUTsport,
       "mGuardFWOUTdport": mGuardFWOUTdport,
       "mGuardFWOUTtarget": mGuardFWOUTtarget,
       "mGuardFWOUTproto": mGuardFWOUTproto,
       "mGuardFWOUTlog": mGuardFWOUTlog,
       "mGuardFWOUTRowStatus": mGuardFWOUTRowStatus,
       "mGuardFWOUTcomment": mGuardFWOUTcomment,
       "mGuardFirewallOUTLogDefault": mGuardFirewallOUTLogDefault,
       "mGuardFirewallPortforwarding": mGuardFirewallPortforwarding,
       "mGuardFirewallPortforwardTable": mGuardFirewallPortforwardTable,
       "mGuardFirewallPortforwardEntry": mGuardFirewallPortforwardEntry,
       "mGuardFWPORTFORWruleIndex": mGuardFWPORTFORWruleIndex,
       "mGuardFWPORTFORWinIP": mGuardFWPORTFORWinIP,
       "mGuardFWPORTFORWoutIP": mGuardFWPORTFORWoutIP,
       "mGuardFWPORTFORWinport": mGuardFWPORTFORWinport,
       "mGuardFWPORTFORWoutport": mGuardFWPORTFORWoutport,
       "mGuardFWPORTFORWproto": mGuardFWPORTFORWproto,
       "mGuardFWPORTFORWlog": mGuardFWPORTFORWlog,
       "mGuardFWPORTFORWRowStatus": mGuardFWPORTFORWRowStatus,
       "mGuardFWPORTFORWsrcIP": mGuardFWPORTFORWsrcIP,
       "mGuardFWPORTFORWsrcport": mGuardFWPORTFORWsrcport,
       "mGuardFWPORTFORWcomment": mGuardFWPORTFORWcomment,
       "mGuardFirewallNAT": mGuardFirewallNAT,
       "mGuardFirewallNATRuleTable": mGuardFirewallNATRuleTable,
       "mGuardFirewallNATRuleEntry": mGuardFirewallNATRuleEntry,
       "mGuardFWNATruleIndex": mGuardFWNATruleIndex,
       "mGuardFWNATIP": mGuardFWNATIP,
       "mGuardFWNATRowStatus": mGuardFWNATRowStatus,
       "mGuardFWNATOutIP": mGuardFWNATOutIP,
       "mGuardFirewallExtended": mGuardFirewallExtended,
       "mGuardFirewallIPConntrackMax": mGuardFirewallIPConntrackMax,
       "mGuardFirewallIPSynfloodLimitInt": mGuardFirewallIPSynfloodLimitInt,
       "mGuardFirewallIPSynfloodLimitExt": mGuardFirewallIPSynfloodLimitExt,
       "mGuardFirewallICMPLimitInt": mGuardFirewallICMPLimitInt,
       "mGuardFirewallICMPLimitExt": mGuardFirewallICMPLimitExt,
       "mGuardFirewallEnableConntrackFTP": mGuardFirewallEnableConntrackFTP,
       "mGuardFirewallConntrackIRC": mGuardFirewallConntrackIRC,
       "mGuardFirewallConntrackPPTP": mGuardFirewallConntrackPPTP,
       "mGuardFirewallARPLimitInt": mGuardFirewallARPLimitInt,
       "mGuardFirewallARPLimitExt": mGuardFirewallARPLimitExt,
       "mGuardFirewallICMPPolicy": mGuardFirewallICMPPolicy,
       "mGuardFirewallConntrackH323": mGuardFirewallConntrackH323,
       "mGuardFirewallIpUncleanMatch": mGuardFirewallIpUncleanMatch,
       "mGuardFirewall11NAT": mGuardFirewall11NAT,
       "mGuardFirewall11NATRuleTable": mGuardFirewall11NATRuleTable,
       "mGuardFirewall11NATRuleEntry": mGuardFirewall11NATRuleEntry,
       "mGuardFW11NATruleIndex": mGuardFW11NATruleIndex,
       "mGuardFW11NATLocal": mGuardFW11NATLocal,
       "mGuardFW11NATRemote": mGuardFW11NATRemote,
       "mGuardFW11NATMask": mGuardFW11NATMask,
       "mGuardFW11NATLog": mGuardFW11NATLog,
       "mGuardFW11NATRowStatus": mGuardFW11NATRowStatus,
       "mGuardFirewallUserFW": mGuardFirewallUserFW,
       "mGuardFirewallUserFWEnabled": mGuardFirewallUserFWEnabled,
       "mGuardFirewallUserFWTemplateTable": mGuardFirewallUserFWTemplateTable,
       "mGuardFirewallUserFWTemplateEntry": mGuardFirewallUserFWTemplateEntry,
       "mGuardFirewallUserFWTemplateIndex": mGuardFirewallUserFWTemplateIndex,
       "mGuardFirewallUserFWTemplateEnabled": mGuardFirewallUserFWTemplateEnabled,
       "mGuardFirewallUserFWTemplateName": mGuardFirewallUserFWTemplateName,
       "mGuardFirewallUserFWTemplateComment": mGuardFirewallUserFWTemplateComment,
       "mGuardFirewallUserFWTemplateTimeout": mGuardFirewallUserFWTemplateTimeout,
       "mGuardFirewallUserFWTemplateSrcIP": mGuardFirewallUserFWTemplateSrcIP,
       "mGuardFirewallUserFWTemplateRowStatus": mGuardFirewallUserFWTemplateRowStatus,
       "mGuardFirewallUserFWTemplateUserTable": mGuardFirewallUserFWTemplateUserTable,
       "mGuardFirewallUserFWTemplateUserEntry": mGuardFirewallUserFWTemplateUserEntry,
       "mGuardFirewallUserFWTemplateUserTemplateIndex": mGuardFirewallUserFWTemplateUserTemplateIndex,
       "mGuardFirewallUserFWTemplateUserIndex": mGuardFirewallUserFWTemplateUserIndex,
       "mGuardFirewallUserFWTemplateUserName": mGuardFirewallUserFWTemplateUserName,
       "mGuardFirewallUserFWTemplateUserRowStatus": mGuardFirewallUserFWTemplateUserRowStatus,
       "mGuardFirewallUserFWTemplateRuleTable": mGuardFirewallUserFWTemplateRuleTable,
       "mGuardFirewallUserFWTemplateRuleEntry": mGuardFirewallUserFWTemplateRuleEntry,
       "mGuardFirewallUserFWTemplateRuleTemplateIndex": mGuardFirewallUserFWTemplateRuleTemplateIndex,
       "mGuardFirewallUserFWTemplateRuleIndex": mGuardFirewallUserFWTemplateRuleIndex,
       "mGuardFirewallUserFWTemplateRuleProto": mGuardFirewallUserFWTemplateRuleProto,
       "mGuardFirewallUserFWTemplateRuleSrcPort": mGuardFirewallUserFWTemplateRuleSrcPort,
       "mGuardFirewallUserFWTemplateRuleDstPort": mGuardFirewallUserFWTemplateRuleDstPort,
       "mGuardFirewallUserFWTemplateRuleDstIP": mGuardFirewallUserFWTemplateRuleDstIP,
       "mGuardFirewallUserFWTemplateRuleLog": mGuardFirewallUserFWTemplateRuleLog,
       "mGuardFirewallUserFWTemplateRuleComment": mGuardFirewallUserFWTemplateRuleComment,
       "mGuardFirewallUserFWTemplateRuleRowStatus": mGuardFirewallUserFWTemplateRuleRowStatus,
       "mGuardNetwork": mGuardNetwork,
       "mGuardNetworkMode": mGuardNetworkMode,
       "mGuardStealth": mGuardStealth,
       "mGuardStealthIPConfMode": mGuardStealthIPConfMode,
       "mGuardStealthIPConfStatic": mGuardStealthIPConfStatic,
       "mGuardStealthStaticIP": mGuardStealthStaticIP,
       "mGuardStealthStaticMAC": mGuardStealthStaticMAC,
       "mGuardStealthStaticActivate": mGuardStealthStaticActivate,
       "mGuardStealthManageIP": mGuardStealthManageIP,
       "mGuardStealthManageNetmask": mGuardStealthManageNetmask,
       "mGuardStealthManageGateway": mGuardStealthManageGateway,
       "mGuardStealthManageActivate": mGuardStealthManageActivate,
       "mGuardStealthHiDiscoveryRelay": mGuardStealthHiDiscoveryRelay,
       "mGuardStealthHiDiscoveryState": mGuardStealthHiDiscoveryState,
       "mGuardStealthL2Filter": mGuardStealthL2Filter,
       "mGuardL2FilterInternTable": mGuardL2FilterInternTable,
       "mGuardL2FilterInternEntry": mGuardL2FilterInternEntry,
       "mGuardL2FilterInternRuleIndex": mGuardL2FilterInternRuleIndex,
       "mGuardL2FilterInternRowStatus": mGuardL2FilterInternRowStatus,
       "mGuardL2FilterInternSrcMac": mGuardL2FilterInternSrcMac,
       "mGuardL2FilterInternDstMac": mGuardL2FilterInternDstMac,
       "mGuardL2FilterInternEthType": mGuardL2FilterInternEthType,
       "mGuardL2FilterInternTarget": mGuardL2FilterInternTarget,
       "mGuardL2FilterInternComment": mGuardL2FilterInternComment,
       "mGuardL2FilterExternTable": mGuardL2FilterExternTable,
       "mGuardL2FilterExternEntry": mGuardL2FilterExternEntry,
       "mGuardL2FilterExternRuleIndex": mGuardL2FilterExternRuleIndex,
       "mGuardL2FilterExternRowStatus": mGuardL2FilterExternRowStatus,
       "mGuardL2FilterExternSrcMac": mGuardL2FilterExternSrcMac,
       "mGuardL2FilterExternDstMac": mGuardL2FilterExternDstMac,
       "mGuardL2FilterExternEthType": mGuardL2FilterExternEthType,
       "mGuardL2FilterExternTarget": mGuardL2FilterExternTarget,
       "mGuardL2FilterExternComment": mGuardL2FilterExternComment,
       "mGuardStealthL2ForwardGVRP": mGuardStealthL2ForwardGVRP,
       "mGuardStealthL2ForwardSTP": mGuardStealthL2ForwardSTP,
       "mGuardStealthL2ForwardDHCP": mGuardStealthL2ForwardDHCP,
       "mGuardStealthInterface": mGuardStealthInterface,
       "mGuardStealthMTU": mGuardStealthMTU,
       "mGuardStealthVlanMTU": mGuardStealthVlanMTU,
       "mGuardStealthManageUseVLAN": mGuardStealthManageUseVLAN,
       "mGuardStealthManageVLanID": mGuardStealthManageVLanID,
       "mGuardRouter": mGuardRouter,
       "mGuardRouterLocal": mGuardRouterLocal,
       "mGuardRouterLocalIP": mGuardRouterLocalIP,
       "mGuardRouterLocalNetmask": mGuardRouterLocalNetmask,
       "mGuardRouterLocalActivate": mGuardRouterLocalActivate,
       "mGuardRouterLocalAliasesTable": mGuardRouterLocalAliasesTable,
       "mGuardRouterLocalAliasesEntry": mGuardRouterLocalAliasesEntry,
       "mGuardLocalAliasIndex": mGuardLocalAliasIndex,
       "mGuardLocalAliasIpAddress": mGuardLocalAliasIpAddress,
       "mGuardLocalAliasNetmask": mGuardLocalAliasNetmask,
       "mGuardLocalAliasRowStatus": mGuardLocalAliasRowStatus,
       "mGuardLocalAliasUseVLAN": mGuardLocalAliasUseVLAN,
       "mGuardLocalAliasVLANid": mGuardLocalAliasVLANid,
       "mGuardLocalRoutesTable": mGuardLocalRoutesTable,
       "mGuardLocalRoutesEntry": mGuardLocalRoutesEntry,
       "mGuardLocalRouteIndex": mGuardLocalRouteIndex,
       "mGuardLocalRouteNetwork": mGuardLocalRouteNetwork,
       "mGuardLocalRouteGateway": mGuardLocalRouteGateway,
       "mGuardLocalRouteRowStatus": mGuardLocalRouteRowStatus,
       "mGuardRouterLocalDevMTU": mGuardRouterLocalDevMTU,
       "mGuardRouterLocalUseVLAN": mGuardRouterLocalUseVLAN,
       "mGuardRouterLocalVlanId": mGuardRouterLocalVlanId,
       "mGuardRouterLocalDevVlanMTU": mGuardRouterLocalDevVlanMTU,
       "mGuardRouterExtern": mGuardRouterExtern,
       "mGuardRouterExternDHCP": mGuardRouterExternDHCP,
       "mGuardRouterExternStatic": mGuardRouterExternStatic,
       "mGuardRouterExternStaticIP": mGuardRouterExternStaticIP,
       "mGuardRouterExternStaticNetmask": mGuardRouterExternStaticNetmask,
       "mGuardRouterExternStaticGateway": mGuardRouterExternStaticGateway,
       "mGuardRouterExternActivate": mGuardRouterExternActivate,
       "mGuardRouterExternAliasesTable": mGuardRouterExternAliasesTable,
       "mGuardRouterExternAliasesEntry": mGuardRouterExternAliasesEntry,
       "mGuardExternAliasIndex": mGuardExternAliasIndex,
       "mGuardExternAliasIpAddress": mGuardExternAliasIpAddress,
       "mGuardExternAliasNetmask": mGuardExternAliasNetmask,
       "mGuardExternAliasRowStatus": mGuardExternAliasRowStatus,
       "mGuardExternAliasUseVLAN": mGuardExternAliasUseVLAN,
       "mGuardExternAliasVLANid": mGuardExternAliasVLANid,
       "mGuardExternRoutesTable": mGuardExternRoutesTable,
       "mGuardExternRoutesEntry": mGuardExternRoutesEntry,
       "mGuardExternRouteIndex": mGuardExternRouteIndex,
       "mGuardExternRouteNetwork": mGuardExternRouteNetwork,
       "mGuardExternRouteGateway": mGuardExternRouteGateway,
       "mGuardExternRouteRowStatus": mGuardExternRouteRowStatus,
       "mGuardRouterExternDevMTU": mGuardRouterExternDevMTU,
       "mGuardRouterExternUseVLAN": mGuardRouterExternUseVLAN,
       "mGuardRouterExternVlanId": mGuardRouterExternVlanId,
       "mGuardRouterExternDevVlanMTU": mGuardRouterExternDevVlanMTU,
       "mGuardRouterHiDiscovery": mGuardRouterHiDiscovery,
       "mGuardRouterHiDiscoveryIntern": mGuardRouterHiDiscoveryIntern,
       "mGuardRouterHiDiscoveryExtern": mGuardRouterHiDiscoveryExtern,
       "mGuardPPPOE": mGuardPPPOE,
       "mGuardPPPOELogin": mGuardPPPOELogin,
       "mGuardPPPOEPasswd": mGuardPPPOEPasswd,
       "mGuardPPPOEMSS": mGuardPPPOEMSS,
       "mGuardPPPOEServiceName": mGuardPPPOEServiceName,
       "mGuardPPPOEAccessConcentName": mGuardPPPOEAccessConcentName,
       "mGuardPPPOEHostUnique": mGuardPPPOEHostUnique,
       "mGuardPPPOEpppdOptionsTable": mGuardPPPOEpppdOptionsTable,
       "mGuardPPPOEpppdOptionsEntry": mGuardPPPOEpppdOptionsEntry,
       "mGuardPPPOEpppdOptionsIndex": mGuardPPPOEpppdOptionsIndex,
       "mGuardPPPOEpppdOptionsValue": mGuardPPPOEpppdOptionsValue,
       "mGuardPPPOEpppdOptionsRowStatus": mGuardPPPOEpppdOptionsRowStatus,
       "mGuardDHCP": mGuardDHCP,
       "mGuardDHCPInt": mGuardDHCPInt,
       "mGuardDHCPIntStart": mGuardDHCPIntStart,
       "mGuardDHCPIntPoolEnable": mGuardDHCPIntPoolEnable,
       "mGuardDHCPIntRangeStart": mGuardDHCPIntRangeStart,
       "mGuardDHCPIntRangeEnd": mGuardDHCPIntRangeEnd,
       "mGuardDHCPIntNetmask": mGuardDHCPIntNetmask,
       "mGuardDHCPIntGateway": mGuardDHCPIntGateway,
       "mGuardDHCPIntDnsServer": mGuardDHCPIntDnsServer,
       "mGuardDHCPIntStaticTable": mGuardDHCPIntStaticTable,
       "mGuardDHCPIntStaticEntry": mGuardDHCPIntStaticEntry,
       "mGuardDHCPIntStaticIndex": mGuardDHCPIntStaticIndex,
       "mGuardDHCPIntStaticMAC": mGuardDHCPIntStaticMAC,
       "mGuardDHCPIntStaticIP": mGuardDHCPIntStaticIP,
       "mGuardDHCPIntStaticRowStatus": mGuardDHCPIntStaticRowStatus,
       "mGuardDHCPIntBroadcast": mGuardDHCPIntBroadcast,
       "mGuardDHCPIntWINS": mGuardDHCPIntWINS,
       "mGuardDHCPIntLeaseTime": mGuardDHCPIntLeaseTime,
       "mGuardDHCPIntRelayServerTable": mGuardDHCPIntRelayServerTable,
       "mGuardDHCPIntRelayServerEntry": mGuardDHCPIntRelayServerEntry,
       "mGuardDHCPIntRelayServerIndex": mGuardDHCPIntRelayServerIndex,
       "mGuardDHCPIntRelayServerIP": mGuardDHCPIntRelayServerIP,
       "mGuardDHCPIntRelayRowStatus": mGuardDHCPIntRelayRowStatus,
       "mGuardDHCPIntRelayMaxHop": mGuardDHCPIntRelayMaxHop,
       "mGuardDHCPIntRelayAppend": mGuardDHCPIntRelayAppend,
       "mGuardDHCPIntRelayAppendLimit": mGuardDHCPIntRelayAppendLimit,
       "mGuardDHCPIntRelayCircuitInfo": mGuardDHCPIntRelayCircuitInfo,
       "mGuardDHCPIntRelayCircuitText": mGuardDHCPIntRelayCircuitText,
       "mGuardDHCPIntRelayRemoteInfo": mGuardDHCPIntRelayRemoteInfo,
       "mGuardDHCPIntRelayRemoteText": mGuardDHCPIntRelayRemoteText,
       "mGuardDHCPExt": mGuardDHCPExt,
       "mGuardDHCPExtStart": mGuardDHCPExtStart,
       "mGuardDHCPExtPoolEnable": mGuardDHCPExtPoolEnable,
       "mGuardDHCPExtRangeStart": mGuardDHCPExtRangeStart,
       "mGuardDHCPExtRangeEnd": mGuardDHCPExtRangeEnd,
       "mGuardDHCPExtNetmask": mGuardDHCPExtNetmask,
       "mGuardDHCPExtGateway": mGuardDHCPExtGateway,
       "mGuardDHCPExtDnsServer": mGuardDHCPExtDnsServer,
       "mGuardDHCPExtStaticTable": mGuardDHCPExtStaticTable,
       "mGuardDHCPExtStaticEntry": mGuardDHCPExtStaticEntry,
       "mGuardDHCPExtStaticIndex": mGuardDHCPExtStaticIndex,
       "mGuardDHCPExtStaticMAC": mGuardDHCPExtStaticMAC,
       "mGuardDHCPExtStaticIP": mGuardDHCPExtStaticIP,
       "mGuardDHCPExtStaticRowStatus": mGuardDHCPExtStaticRowStatus,
       "mGuardDHCPExtBroadcast": mGuardDHCPExtBroadcast,
       "mGuardDHCPExtWINS": mGuardDHCPExtWINS,
       "mGuardDHCPExtLeaseTime": mGuardDHCPExtLeaseTime,
       "mGuardDHCPExtRelayServerTable": mGuardDHCPExtRelayServerTable,
       "mGuardDHCPExtRelayServerEntry": mGuardDHCPExtRelayServerEntry,
       "mGuardDHCPExtRelayServerIndex": mGuardDHCPExtRelayServerIndex,
       "mGuardDHCPExtRelayServerIP": mGuardDHCPExtRelayServerIP,
       "mGuardDHCPExtRelayRowStatus": mGuardDHCPExtRelayRowStatus,
       "mGuardDHCPExtRelayMaxHop": mGuardDHCPExtRelayMaxHop,
       "mGuardDHCPExtRelayAppend": mGuardDHCPExtRelayAppend,
       "mGuardDHCPExtRelayAppendLimit": mGuardDHCPExtRelayAppendLimit,
       "mGuardDHCPExtRelayCircuitInfo": mGuardDHCPExtRelayCircuitInfo,
       "mGuardDHCPExtRelayCircuitText": mGuardDHCPExtRelayCircuitText,
       "mGuardDHCPExtRelayRemoteInfo": mGuardDHCPExtRelayRemoteInfo,
       "mGuardDHCPExtRelayRemoteText": mGuardDHCPExtRelayRemoteText,
       "mGuardDNS": mGuardDNS,
       "mGuardDNSSearchPath": mGuardDNSSearchPath,
       "mGuardDNSServerType": mGuardDNSServerType,
       "mGuardDNSUserDefinedServerTable": mGuardDNSUserDefinedServerTable,
       "mGuardDNSUserDefinedServerEntry": mGuardDNSUserDefinedServerEntry,
       "mGuarddnsServerIndex": mGuarddnsServerIndex,
       "mGuarddnsServerIP": mGuarddnsServerIP,
       "mGuarddnsServerRowStatus": mGuarddnsServerRowStatus,
       "mGuardDNSCacheEnabled": mGuardDNSCacheEnabled,
       "mGuardNetworkStatus": mGuardNetworkStatus,
       "mGuardNetworkStatMode": mGuardNetworkStatMode,
       "mGuardNetworkStatExtIP": mGuardNetworkStatExtIP,
       "mGuardNetworkStatGateway": mGuardNetworkStatGateway,
       "mGuardNetworkStatVPN": mGuardNetworkStatVPN,
       "mGuardNetworkStatDynIPReg": mGuardNetworkStatDynIPReg,
       "mGuardNetworkStatHTTPSRemAccess": mGuardNetworkStatHTTPSRemAccess,
       "mGuardNetworkStatSSHRemoteAccess": mGuardNetworkStatSSHRemoteAccess,
       "mGuardNetworkSoftwareVersion": mGuardNetworkSoftwareVersion,
       "mGuardNetworkStatUptime": mGuardNetworkStatUptime,
       "mGuardNetworkStatLanguage": mGuardNetworkStatLanguage,
       "mGuardHostname": mGuardHostname,
       "mGuardHostnameMode": mGuardHostnameMode,
       "mGuardPPTP": mGuardPPTP,
       "mGuardPPTPLogin": mGuardPPTPLogin,
       "mGuardPPTPassword": mGuardPPTPassword,
       "mGuardPPTPLocalIPMode": mGuardPPTPLocalIPMode,
       "mGuardPPTPLocalIP": mGuardPPTPLocalIP,
       "mGuardPPTPModemIP": mGuardPPTPModemIP,
       "mGuardPPTPpppdOptionsTable": mGuardPPTPpppdOptionsTable,
       "mGuardPPTPpppdOptionsEntry": mGuardPPTPpppdOptionsEntry,
       "mGuardPPTPpppdOptionsIndex": mGuardPPTPpppdOptionsIndex,
       "mGuardPPTPpppdOptionsValue": mGuardPPTPpppdOptionsValue,
       "mGuardPPTPpppdOptionsRowStatus": mGuardPPTPpppdOptionsRowStatus,
       "mGuardSerial": mGuardSerial,
       "mGuardSerialBaud": mGuardSerialBaud,
       "mGuardSerialHWHandshakeEnable": mGuardSerialHWHandshakeEnable,
       "mGuardSerialPPP": mGuardSerialPPP,
       "mGuardSerialPPPEnable": mGuardSerialPPPEnable,
       "mGuardSerialPPPLogin": mGuardSerialPPPLogin,
       "mGuardSerialPPPPasswd": mGuardSerialPPPPasswd,
       "mGuardSerialPPPLocalIP": mGuardSerialPPPLocalIP,
       "mGuardSerialPPPRemoteIP": mGuardSerialPPPRemoteIP,
       "mGuardSerialPPPFWIN": mGuardSerialPPPFWIN,
       "mGuardSerialPPPFWINTable": mGuardSerialPPPFWINTable,
       "mGuardSerialPPPFWINEntry": mGuardSerialPPPFWINEntry,
       "mGuardSerialPPPFWINruleIndex": mGuardSerialPPPFWINruleIndex,
       "mGuardSerialPPPFWINsourceIP": mGuardSerialPPPFWINsourceIP,
       "mGuardSerialPPPFWINdestinationIP": mGuardSerialPPPFWINdestinationIP,
       "mGuardSerialPPPFWINsport": mGuardSerialPPPFWINsport,
       "mGuardSerialPPPFWINdport": mGuardSerialPPPFWINdport,
       "mGuardSerialPPPFWINtarget": mGuardSerialPPPFWINtarget,
       "mGuardSerialPPPFWINproto": mGuardSerialPPPFWINproto,
       "mGuardSerialPPPFWINlog": mGuardSerialPPPFWINlog,
       "mGuardSerialPPPFWINRowStatus": mGuardSerialPPPFWINRowStatus,
       "mGuardSerialPPPFWINcomment": mGuardSerialPPPFWINcomment,
       "mGuardSerialPPPFWINLogDefault": mGuardSerialPPPFWINLogDefault,
       "mGuardSerialPPPFWOUT": mGuardSerialPPPFWOUT,
       "mGuardSerialPPPFWOUTTable": mGuardSerialPPPFWOUTTable,
       "mGuardSerialPPPFWOUTEntry": mGuardSerialPPPFWOUTEntry,
       "mGuardSerialPPPFWOUTruleIndex": mGuardSerialPPPFWOUTruleIndex,
       "mGuardSerialPPPFWOUTsourceIP": mGuardSerialPPPFWOUTsourceIP,
       "mGuardSerialPPPFWOUTtargetIP": mGuardSerialPPPFWOUTtargetIP,
       "mGuardSerialPPPFWOUTsport": mGuardSerialPPPFWOUTsport,
       "mGuardSerialPPPFWOUTdport": mGuardSerialPPPFWOUTdport,
       "mGuardSerialPPPFWOUTtarget": mGuardSerialPPPFWOUTtarget,
       "mGuardSerialPPPFWOUTproto": mGuardSerialPPPFWOUTproto,
       "mGuardSerialPPPFWOUTlog": mGuardSerialPPPFWOUTlog,
       "mGuardSerialPPPFWOUTRowStatus": mGuardSerialPPPFWOUTRowStatus,
       "mGuardSerialPPPFWOUTcomment": mGuardSerialPPPFWOUTcomment,
       "mGuardSerialPPPFWOUTLogDefault": mGuardSerialPPPFWOUTLogDefault,
       "mGuardArpTimeout": mGuardArpTimeout,
       "mGuardSystem": mGuardSystem,
       "mGuardPasswords": mGuardPasswords,
       "mGuardRootPassword": mGuardRootPassword,
       "mGuardAdminPassword": mGuardAdminPassword,
       "mGuardUserPassword": mGuardUserPassword,
       "mGuardUserPwdEnable": mGuardUserPwdEnable,
       "mGuardHTTPSRemoteAccess": mGuardHTTPSRemoteAccess,
       "mGuardHTTPSRemoteEnable": mGuardHTTPSRemoteEnable,
       "mGuardHTTPSRemotePort": mGuardHTTPSRemotePort,
       "mGuardHTTPSRemoteFWRuleTable": mGuardHTTPSRemoteFWRuleTable,
       "mGuardHTTPSRemoteFWRuleEntry": mGuardHTTPSRemoteFWRuleEntry,
       "mGuardHTTPSFWruleIndex": mGuardHTTPSFWruleIndex,
       "mGuardHTTPSFWsourceIP": mGuardHTTPSFWsourceIP,
       "mGuardHTTPSFWinterface": mGuardHTTPSFWinterface,
       "mGuardHTTPSFWtarget": mGuardHTTPSFWtarget,
       "mGuardHTTPSFWlog": mGuardHTTPSFWlog,
       "mGuardHTTPSFWRowStatus": mGuardHTTPSFWRowStatus,
       "mGuardHTTPSFWcomment": mGuardHTTPSFWcomment,
       "mGuardSSHRemoteAccess": mGuardSSHRemoteAccess,
       "mGuardSSHRemoteEnable": mGuardSSHRemoteEnable,
       "mGuardSSHRemotePort": mGuardSSHRemotePort,
       "mGuardSSHRemoteFWRuleTable": mGuardSSHRemoteFWRuleTable,
       "mGuardSSHRemoteFWRuleEntry": mGuardSSHRemoteFWRuleEntry,
       "mGuardSSHFWruleIndex": mGuardSSHFWruleIndex,
       "mGuardSSHFWsourceIP": mGuardSSHFWsourceIP,
       "mGuardSSHFWinterface": mGuardSSHFWinterface,
       "mGuardSSHFWtarget": mGuardSSHFWtarget,
       "mGuardSSHFWlog": mGuardSSHFWlog,
       "mGuardSSHFWRowStatus": mGuardSSHFWRowStatus,
       "mGuardSSHFWcomment": mGuardSSHFWcomment,
       "mGuardWebInterface": mGuardWebInterface,
       "mGuardWebInterfaceLanguage": mGuardWebInterfaceLanguage,
       "mGuardWebInterfaceSessionTimeout": mGuardWebInterfaceSessionTimeout,
       "mGuardWebInterfaceApplyButtonScope": mGuardWebInterfaceApplyButtonScope,
       "mGuardHardwareInformation": mGuardHardwareInformation,
       "mGuardHardware": mGuardHardware,
       "mGuardCPU": mGuardCPU,
       "mGuardCPUFamily": mGuardCPUFamily,
       "mGuardCPUStepping": mGuardCPUStepping,
       "mGuardCPUSpeed": mGuardCPUSpeed,
       "mGuardSystemTemperature": mGuardSystemTemperature,
       "mGuardUptime": mGuardUptime,
       "mGuardUSMem": mGuardUSMem,
       "mGuardMAC1": mGuardMAC1,
       "mGuardMAC2": mGuardMAC2,
       "mGuardMAC3": mGuardMAC3,
       "mGuardSerialNumber": mGuardSerialNumber,
       "mGuardVerParSet": mGuardVerParSet,
       "mGuardProductName": mGuardProductName,
       "mGuardOEMName": mGuardOEMName,
       "mGuardOEMSerial": mGuardOEMSerial,
       "mGuardManufacturer": mGuardManufacturer,
       "mGuardManuDate": mGuardManuDate,
       "mGuardBootLoader": mGuardBootLoader,
       "mGuardHardwareVersion": mGuardHardwareVersion,
       "mGuardRescueSystem": mGuardRescueSystem,
       "mGuardProdSoft": mGuardProdSoft,
       "mGuardVersions": mGuardVersions,
       "mGuardVersion": mGuardVersion,
       "mGuardBaseVersion": mGuardBaseVersion,
       "mGuardUpdates": mGuardUpdates,
       "mGuardPackageVersionTable": mGuardPackageVersionTable,
       "mGuardPackageVersionEntry": mGuardPackageVersionEntry,
       "mGuardPkgIndex": mGuardPkgIndex,
       "mGuardPkgName": mGuardPkgName,
       "mGuardPkgVerNum": mGuardPkgVerNum,
       "mGuardPkgVerVersion": mGuardPkgVerVersion,
       "mGuardPkgVerFlavour": mGuardPkgVerFlavour,
       "mGuardAction": mGuardAction,
       "mGuardSysProduct": mGuardSysProduct,
       "mGuardSNMP": mGuardSNMP,
       "mGuardSNMPenableV3": mGuardSNMPenableV3,
       "mGuardSNMPenableV1": mGuardSNMPenableV1,
       "mGuardSNMPport": mGuardSNMPport,
       "mGuardSNMPv1ROCommunity": mGuardSNMPv1ROCommunity,
       "mGuardSNMPv1RWCommunity": mGuardSNMPv1RWCommunity,
       "mGuardSNMPFWRuleTable": mGuardSNMPFWRuleTable,
       "mGuardSNMPFWRuleEntry": mGuardSNMPFWRuleEntry,
       "mGuardSNMPFWruleIndex": mGuardSNMPFWruleIndex,
       "mGuardSNMPFWsourceIP": mGuardSNMPFWsourceIP,
       "mGuardSNMPFWinterface": mGuardSNMPFWinterface,
       "mGuardSNMPFWtarget": mGuardSNMPFWtarget,
       "mGuardSNMPFWlog": mGuardSNMPFWlog,
       "mGuardSNMPFWRowStatus": mGuardSNMPFWRowStatus,
       "mGuardSNMPFWcomment": mGuardSNMPFWcomment,
       "mGuardSNMPTrapReceiverTable": mGuardSNMPTrapReceiverTable,
       "mGuardSNMPTrapReceiverEntry": mGuardSNMPTrapReceiverEntry,
       "mGuardSNMPTrapReceiverIndex": mGuardSNMPTrapReceiverIndex,
       "mGuardSNMPTrapReceiverCommunity": mGuardSNMPTrapReceiverCommunity,
       "mGuardSNMPTrapReceiverIPAddress": mGuardSNMPTrapReceiverIPAddress,
       "mGuardSNMPTrapReceiverName": mGuardSNMPTrapReceiverName,
       "mGuardSNMPTrapReceiverRowStatus": mGuardSNMPTrapReceiverRowStatus,
       "mGuardSNMPTrapConfigGroup": mGuardSNMPTrapConfigGroup,
       "mGuardSNMPAuthenticationTrapFlag": mGuardSNMPAuthenticationTrapFlag,
       "mGuardSNMPLinkUpDownTrapFlag": mGuardSNMPLinkUpDownTrapFlag,
       "mGuardSNMPColdStartTrapFlag": mGuardSNMPColdStartTrapFlag,
       "mGuardSNMPTrapFlag": mGuardSNMPTrapFlag,
       "mGuardSNMPChassisTrapFlag": mGuardSNMPChassisTrapFlag,
       "mGuardSNMPAgentTrapFlag": mGuardSNMPAgentTrapFlag,
       "mGuardSNMPAvFailTrapFlag": mGuardSNMPAvFailTrapFlag,
       "mGuardSNMPAvInfoTrapFlag": mGuardSNMPAvInfoTrapFlag,
       "mGuardSNMPBladeStateTrapFlag": mGuardSNMPBladeStateTrapFlag,
       "mGuardSNMPBladeConfigTrapFlag": mGuardSNMPBladeConfigTrapFlag,
       "mGuardSNMPRouterRedundancyStatusFlag": mGuardSNMPRouterRedundancyStatusFlag,
       "mGuardNTP": mGuardNTP,
       "mGuardNTPactivate": mGuardNTPactivate,
       "mGuardNTPtimestamp": mGuardNTPtimestamp,
       "mGuardNTPServerTable": mGuardNTPServerTable,
       "mGuardNTPServerEntry": mGuardNTPServerEntry,
       "mGuardNTPServerIndex": mGuardNTPServerIndex,
       "mGuardNTPServerHost": mGuardNTPServerHost,
       "mGuardNTPServerRowStatus": mGuardNTPServerRowStatus,
       "mGuardNTPTimezone": mGuardNTPTimezone,
       "mGuardNTPStatus": mGuardNTPStatus,
       "mGuardUpdate": mGuardUpdate,
       "mGuardUpdateServerTable": mGuardUpdateServerTable,
       "mGuardUpdateServerEntry": mGuardUpdateServerEntry,
       "mGuardUpdateServerIndex": mGuardUpdateServerIndex,
       "mGuardUpdateServer": mGuardUpdateServer,
       "mGuardUpdateServerRowStatus": mGuardUpdateServerRowStatus,
       "mGuardUpdateServerProto": mGuardUpdateServerProto,
       "mGuardUpdateServerHost": mGuardUpdateServerHost,
       "mGuardUpdateServerLogin": mGuardUpdateServerLogin,
       "mGuardUpdateServerPassword": mGuardUpdateServerPassword,
       "mGuardSNMPError": mGuardSNMPError,
       "mGuardRedundancy": mGuardRedundancy,
       "mGuardRouterRedundancy": mGuardRouterRedundancy,
       "mGuardRouterRedundancyEnable": mGuardRouterRedundancyEnable,
       "mGuardRouterRedundancyTrack": mGuardRouterRedundancyTrack,
       "mGuardRouterRedundancyInternalID": mGuardRouterRedundancyInternalID,
       "mGuardRouterRedundancyExternalID": mGuardRouterRedundancyExternalID,
       "mGuardRouterRedundancyPassword": mGuardRouterRedundancyPassword,
       "mGuardRouterRedundancyPeerIntern": mGuardRouterRedundancyPeerIntern,
       "mGuardRouterRedundancyPeerExtern": mGuardRouterRedundancyPeerExtern,
       "mGuardRouterRedundancyPriority": mGuardRouterRedundancyPriority,
       "mGuardRouterRedundancyVirtIpInt": mGuardRouterRedundancyVirtIpInt,
       "mGuardRouterRedundancyVirtIpExt": mGuardRouterRedundancyVirtIpExt,
       "mGuardRouterRedundancyWantState": mGuardRouterRedundancyWantState,
       "mGuardRouterRedExtHostCheckTable": mGuardRouterRedExtHostCheckTable,
       "mGuardRouterRedExtHostCheckEntry": mGuardRouterRedExtHostCheckEntry,
       "mGuardRouterRedExtHostCheckIndex": mGuardRouterRedExtHostCheckIndex,
       "mGuardRouterRedExtHostCheckIP": mGuardRouterRedExtHostCheckIP,
       "mGuardRouterRedExtHostCheckRowSt": mGuardRouterRedExtHostCheckRowSt,
       "mGuardRouterRedIntHostCheckTable": mGuardRouterRedIntHostCheckTable,
       "mGuardRouterRedIntHostCheckEntry": mGuardRouterRedIntHostCheckEntry,
       "mGuardRouterRedIntHostCheckIndex": mGuardRouterRedIntHostCheckIndex,
       "mGuardRouterRedIntHostCheckIP": mGuardRouterRedIntHostCheckIP,
       "mGuardRouterRedIntHostCheckRowSt": mGuardRouterRedIntHostCheckRowSt,
       "mGuardRouterRedundancyState": mGuardRouterRedundancyState,
       "mGuardInfo": mGuardInfo,
       "mGuardHTTPSLastAccessIP": mGuardHTTPSLastAccessIP,
       "mGuardShellLastAccessIP": mGuardShellLastAccessIP,
       "mGuardDHCPLastAccessMAC": mGuardDHCPLastAccessMAC,
       "mGuardTrapResources": mGuardTrapResources,
       "mGuardTResDiscFull": mGuardTResDiscFull,
       "mGuardTResCpuLoadHigh": mGuardTResCpuLoadHigh,
       "mGuardTResMemoryFull": mGuardTResMemoryFull,
       "mGuardTResColdstart": mGuardTResColdstart,
       "mGuardTResAV": mGuardTResAV,
       "mGuardTResAvUpdateDone": mGuardTResAvUpdateDone,
       "mGuardTResAvUpdateError": mGuardTResAvUpdateError,
       "mGuardTResAvVirusDetected": mGuardTResAvVirusDetected,
       "mGuardTResAvFileNotScanned": mGuardTResAvFileNotScanned,
       "mGuardTResAvFailed": mGuardTResAvFailed,
       "mGuardTResPlatformSpecific": mGuardTResPlatformSpecific,
       "mGuardTResIndustrial": mGuardTResIndustrial,
       "mGuardTResIndustrialPower": mGuardTResIndustrialPower,
       "mGuardPSTable": mGuardPSTable,
       "mGuardPSEntry": mGuardPSEntry,
       "mGuardPSSysID": mGuardPSSysID,
       "mGuardPSID": mGuardPSID,
       "mGuardPSState": mGuardPSState,
       "mGuardTResIndustrialTemperature": mGuardTResIndustrialTemperature,
       "mGuardTResIndustrialTempHiLimit": mGuardTResIndustrialTempHiLimit,
       "mGuardTResIndustrialTempLowLimit": mGuardTResIndustrialTempLowLimit,
       "mGuardTResSignalRelais": mGuardTResSignalRelais,
       "mGuardTResSignalRelaisState": mGuardTResSignalRelaisState,
       "mGuardTResSignalRelaisReason": mGuardTResSignalRelaisReason,
       "mGuardTResSignalRelaisReasonIdx": mGuardTResSignalRelaisReasonIdx,
       "mGuardTResSignalRelaisPowerAlarm": mGuardTResSignalRelaisPowerAlarm,
       "mGuardTResSignalRelaisMode": mGuardTResSignalRelaisMode,
       "mGuardTResSignalRelaisManualStat": mGuardTResSignalRelaisManualStat,
       "mGuardTResAutoConfigAdapterState": mGuardTResAutoConfigAdapterState,
       "mGuardTResSignalLinkTable": mGuardTResSignalLinkTable,
       "mGuardTResSigLinkID": mGuardTResSigLinkID,
       "mGuardTResSigLinkAlarm": mGuardTResSigLinkAlarm,
       "mGuardTResBladeCTRL": mGuardTResBladeCTRL,
       "mGuardTResBladeInfo": mGuardTResBladeInfo,
       "mGuardTResBladeRackID": mGuardTResBladeRackID,
       "mGuardTResBladeSlotNr": mGuardTResBladeSlotNr,
       "mGuardTResBladeCtrlPowerStatus": mGuardTResBladeCtrlPowerStatus,
       "mGuardTResBladeCtrlRunStatus": mGuardTResBladeCtrlRunStatus,
       "mGuardTResBladeCtrlCfg": mGuardTResBladeCtrlCfg,
       "mGuardTResBladeCtrlCfgBackup": mGuardTResBladeCtrlCfgBackup,
       "mGuardTResBladeCtrlCfgRestored": mGuardTResBladeCtrlCfgRestored,
       "mGuardTResRedundancy": mGuardTResRedundancy,
       "mGuardTResRedundacyReason": mGuardTResRedundacyReason,
       "mGuardTResRedundacyBackupDown": mGuardTResRedundacyBackupDown,
       "mGuardTraps": mGuardTraps,
       "mGuardTrapDiscFull": mGuardTrapDiscFull,
       "mGuardTrapCpuLoadHigh": mGuardTrapCpuLoadHigh,
       "mGuardTrapMemoryFull": mGuardTrapMemoryFull,
       "mGuardTrapColdstart": mGuardTrapColdstart,
       "mGuardTrapAV": mGuardTrapAV,
       "mGuardTrapAvUpdateDone": mGuardTrapAvUpdateDone,
       "mGuardTrapAvUpdateError": mGuardTrapAvUpdateError,
       "mGuardTrapAvVirusDetected": mGuardTrapAvVirusDetected,
       "mGuardTrapAvFileNotScanned": mGuardTrapAvFileNotScanned,
       "mGuardTrapAvFailed": mGuardTrapAvFailed,
       "mGuardTrapPlatformSpecific": mGuardTrapPlatformSpecific,
       "mGuardTrapIndustrial": mGuardTrapIndustrial,
       "mGuardTrapIndustrialTemperature": mGuardTrapIndustrialTemperature,
       "mGuardTrapIndustrialPowerStatus": mGuardTrapIndustrialPowerStatus,
       "mGuardTrapSignalRelais": mGuardTrapSignalRelais,
       "mGuardTrapAutoConfigAdapterState": mGuardTrapAutoConfigAdapterState,
       "mGuardTrapBladeCTRL": mGuardTrapBladeCTRL,
       "mGuardTrapBladeCtrlPowerStatus": mGuardTrapBladeCtrlPowerStatus,
       "mGuardTrapBladeCtrlRunStatus": mGuardTrapBladeCtrlRunStatus,
       "mGuardTrapBladeCtrlCfg": mGuardTrapBladeCtrlCfg,
       "mGuardTrapBladeCtrlCfgBackup": mGuardTrapBladeCtrlCfgBackup,
       "mGuardTrapBladeCtrlCfgRestored": mGuardTrapBladeCtrlCfgRestored,
       "mGuardTrapRouterRedundancy": mGuardTrapRouterRedundancy,
       "mGuardTrapRouterRedundancyStatusChange": mGuardTrapRouterRedundancyStatusChange,
       "mGuardTrapRouterRedundancyBackupDown": mGuardTrapRouterRedundancyBackupDown,
       "mGuardLogging": mGuardLogging,
       "mGuardLoggingRemoteActivate": mGuardLoggingRemoteActivate,
       "mGuardLoggingRemoteIP": mGuardLoggingRemoteIP,
       "mGuardLoggingRemotePort": mGuardLoggingRemotePort,
       "mGuardContFilt": mGuardContFilt,
       "mGuardContFiltAVP": mGuardContFiltAVP,
       "mGuardContFiltAVPSchedule": mGuardContFiltAVPSchedule,
       "mGuardContFiltAVPServerTable": mGuardContFiltAVPServerTable,
       "mGuardContFiltAVPServerEntry": mGuardContFiltAVPServerEntry,
       "mGuardContFiltAVPServerIndex": mGuardContFiltAVPServerIndex,
       "mGuardContFiltAVPServerURL": mGuardContFiltAVPServerURL,
       "mGuardContFiltAVPServerRowStatus": mGuardContFiltAVPServerRowStatus,
       "mGuardContFiltAVPHTTPProxy": mGuardContFiltAVPHTTPProxy,
       "mGuardContFiltAVPHTTPProxyLogin": mGuardContFiltAVPHTTPProxyLogin,
       "mGuardContFiltAVPHTTPProxyPasswd": mGuardContFiltAVPHTTPProxyPasswd,
       "mGuardContFiltAVPHTTPProxyServer": mGuardContFiltAVPHTTPProxyServer,
       "mGuardContFiltAVPHTTPProxyPort": mGuardContFiltAVPHTTPProxyPort,
       "mGuardContFiltAVPLogLevel": mGuardContFiltAVPLogLevel,
       "mGuardContFiltAVPMaxConnections": mGuardContFiltAVPMaxConnections,
       "mGuardContFiltAVPScanTimeout": mGuardContFiltAVPScanTimeout,
       "mGuardContFiltAVPpass": mGuardContFiltAVPpass,
       "mGuardContFiltAVPpassCorrupt": mGuardContFiltAVPpassCorrupt,
       "mGuardContFiltAVPpassEncrypted": mGuardContFiltAVPpassEncrypted,
       "mGuardContFiltAVPpassSuspicious": mGuardContFiltAVPpassSuspicious,
       "mGuardContFiltAVPpassWarnings": mGuardContFiltAVPpassWarnings,
       "mGuardContFiltQuarantine": mGuardContFiltQuarantine,
       "mGuardContFiltQuarantineClean": mGuardContFiltQuarantineClean,
       "mGuardContFiltQuarantineError": mGuardContFiltQuarantineError,
       "mGuardContFiltQuarantineVirus": mGuardContFiltQuarantineVirus,
       "mGuardContFiltQuarantineSrvIP": mGuardContFiltQuarantineSrvIP,
       "mGuardContFiltQuarantineSrvPort": mGuardContFiltQuarantineSrvPort,
       "mGuardContFiltInfo": mGuardContFiltInfo,
       "mGuardContFiltInfoFlashID": mGuardContFiltInfoFlashID,
       "mGuardContFiltHTTP": mGuardContFiltHTTP,
       "mGuardContFiltHTTPEnable": mGuardContFiltHTTPEnable,
       "mGuardContFiltHTTPVirusAction": mGuardContFiltHTTPVirusAction,
       "mGuardContFiltHTTPMaxSize": mGuardContFiltHTTPMaxSize,
       "mGuardContFiltHTTPExceedAction": mGuardContFiltHTTPExceedAction,
       "mGuardContFiltHTTPSrvrTable": mGuardContFiltHTTPSrvrTable,
       "mGuardContFiltHTTPSrvrEntry": mGuardContFiltHTTPSrvrEntry,
       "mGuardContFiltHTTPSrvrIndex": mGuardContFiltHTTPSrvrIndex,
       "mGuardContFiltHTTPSrvrIP": mGuardContFiltHTTPSrvrIP,
       "mGuardContFiltHTTPSrvrPort": mGuardContFiltHTTPSrvrPort,
       "mGuardContFiltHTTPSrvrScanAction": mGuardContFiltHTTPSrvrScanAction,
       "mGuardContFiltHTTPSrvrRowStatus": mGuardContFiltHTTPSrvrRowStatus,
       "mGuardContFiltHTTPSrvrComment": mGuardContFiltHTTPSrvrComment,
       "mGuardContFiltPOP3": mGuardContFiltPOP3,
       "mGuardContFiltPOP3Enable": mGuardContFiltPOP3Enable,
       "mGuardContFiltPOP3VirusAction": mGuardContFiltPOP3VirusAction,
       "mGuardContFiltPOP3MaxSize": mGuardContFiltPOP3MaxSize,
       "mGuardContFiltPOP3ExceedAction": mGuardContFiltPOP3ExceedAction,
       "mGuardContFiltPOP3SrvrTable": mGuardContFiltPOP3SrvrTable,
       "mGuardContFiltPOP3SrvrEntry": mGuardContFiltPOP3SrvrEntry,
       "mGuardContFiltPOP3SrvrIndex": mGuardContFiltPOP3SrvrIndex,
       "mGuardContFiltPOP3SrvrIP": mGuardContFiltPOP3SrvrIP,
       "mGuardContFiltPOP3SrvrPort": mGuardContFiltPOP3SrvrPort,
       "mGuardContFiltPOP3SrvrScanAction": mGuardContFiltPOP3SrvrScanAction,
       "mGuardContFiltPOP3SrvrRowStatus": mGuardContFiltPOP3SrvrRowStatus,
       "mGuardContFiltPOP3SrvrComment": mGuardContFiltPOP3SrvrComment,
       "mGuardContFiltSMTP": mGuardContFiltSMTP,
       "mGuardContFiltSMTPEnable": mGuardContFiltSMTPEnable,
       "mGuardContFiltSMTPVirusAction": mGuardContFiltSMTPVirusAction,
       "mGuardContFiltSMTPMaxSize": mGuardContFiltSMTPMaxSize,
       "mGuardContFiltSMTPExceedAction": mGuardContFiltSMTPExceedAction,
       "mGuardContFiltSMTPSrvrTable": mGuardContFiltSMTPSrvrTable,
       "mGuardContFiltSMTPSrvrEntry": mGuardContFiltSMTPSrvrEntry,
       "mGuardContFiltSMTPSrvrIndex": mGuardContFiltSMTPSrvrIndex,
       "mGuardContFiltSMTPSrvrIP": mGuardContFiltSMTPSrvrIP,
       "mGuardContFiltSMTPSrvrPort": mGuardContFiltSMTPSrvrPort,
       "mGuardContFiltSMTPSrvrScanAction": mGuardContFiltSMTPSrvrScanAction,
       "mGuardContFiltSMTPSrvrRowStatus": mGuardContFiltSMTPSrvrRowStatus,
       "mGuardContFiltSMTPSrvrComment": mGuardContFiltSMTPSrvrComment,
       "mGuardContFiltFTP": mGuardContFiltFTP,
       "mGuardContFiltFTPEnable": mGuardContFiltFTPEnable,
       "mGuardContFiltFTPVirusAction": mGuardContFiltFTPVirusAction,
       "mGuardContFiltFTPMaxSize": mGuardContFiltFTPMaxSize,
       "mGuardContFiltFTPExceedAction": mGuardContFiltFTPExceedAction,
       "mGuardContFiltFTPSrvrTable": mGuardContFiltFTPSrvrTable,
       "mGuardContFiltFTPSrvrEntry": mGuardContFiltFTPSrvrEntry,
       "mGuardContFiltFTPSrvrIndex": mGuardContFiltFTPSrvrIndex,
       "mGuardContFiltFTPSrvrIP": mGuardContFiltFTPSrvrIP,
       "mGuardContFiltFTPSrvrPort": mGuardContFiltFTPSrvrPort,
       "mGuardContFiltFTPSrvrScanAction": mGuardContFiltFTPSrvrScanAction,
       "mGuardContFiltFTPSrvrRowStatus": mGuardContFiltFTPSrvrRowStatus,
       "mGuardContFiltFTPSrvrComment": mGuardContFiltFTPSrvrComment,
       "mGuardBlade": mGuardBlade,
       "mGuardBladeRackID": mGuardBladeRackID,
       "mGuardBladeSlotID": mGuardBladeSlotID,
       "mGuardBladeCtrlTable": mGuardBladeCtrlTable,
       "mGuardBladeCtrlEntry": mGuardBladeCtrlEntry,
       "mGuardBladeCtrlIndex": mGuardBladeCtrlIndex,
       "mGuardBladeCtrlDevice": mGuardBladeCtrlDevice,
       "mGuardBladeCtrlStatus": mGuardBladeCtrlStatus,
       "mGuardBladeCtrlAVRRevision": mGuardBladeCtrlAVRRevision,
       "mGuardBladeCtrlSlotID": mGuardBladeCtrlSlotID,
       "mGuardBladeCtrlProductID": mGuardBladeCtrlProductID,
       "mGuardBladeCtrlAssemblyID": mGuardBladeCtrlAssemblyID,
       "mGuardBladeCtrlSerial": mGuardBladeCtrlSerial,
       "mGuardBladeCtrlFlashID": mGuardBladeCtrlFlashID,
       "mGuardBladeCtrlVersion": mGuardBladeCtrlVersion,
       "mGuardBladeCtrlBackup": mGuardBladeCtrlBackup,
       "mGuardBladeCtrlRestore": mGuardBladeCtrlRestore,
       "mGuardBladePwrTable": mGuardBladePwrTable,
       "mGuardBladePwrEntry": mGuardBladePwrEntry,
       "mGuardBladePwrIndex": mGuardBladePwrIndex,
       "mGuardBladePwrStatus": mGuardBladePwrStatus,
       "mGuardProfile": mGuardProfile,
       "mGuardProfilePush": mGuardProfilePush,
       "mGuardProfilePull": mGuardProfilePull,
       "mGuardProfilePullSchedule": mGuardProfilePullSchedule,
       "mGuardProfilePullHTTPS": mGuardProfilePullHTTPS,
       "mGuardProfilePullHTTPSCert": mGuardProfilePullHTTPSCert,
       "mGuardProfilePullHTTPSServer": mGuardProfilePullHTTPSServer,
       "mGuardProfilePullHTTPSPort": mGuardProfilePullHTTPSPort,
       "mGuardProfilePullHTTPSFile": mGuardProfilePullHTTPSFile,
       "mGuardProfilePullHTTPSLogin": mGuardProfilePullHTTPSLogin,
       "mGuardProfilePullHTTPSPasswd": mGuardProfilePullHTTPSPasswd,
       "mGuardProfilePullHTTPSDirectory": mGuardProfilePullHTTPSDirectory,
       "mGuardUsers": mGuardUsers,
       "mGuardRemoteUsers": mGuardRemoteUsers,
       "mGuardRADIUS": mGuardRADIUS,
       "mGuardRADIUSTimeout": mGuardRADIUSTimeout,
       "mGuardRADIUSRetries": mGuardRADIUSRetries,
       "mGuardRADIUSServerTable": mGuardRADIUSServerTable,
       "mGuardRADIUSServerEntry": mGuardRADIUSServerEntry,
       "mGuardRADIUSServerIndex": mGuardRADIUSServerIndex,
       "mGuardRADIUSServerHostname": mGuardRADIUSServerHostname,
       "mGuardRADIUSServerPort": mGuardRADIUSServerPort,
       "mGuardRADIUSServerSecret": mGuardRADIUSServerSecret,
       "mGuardRADIUSServerRowStatus": mGuardRADIUSServerRowStatus,
       "mGuardUserFWUsers": mGuardUserFWUsers,
       "mGuardUserFWUserTable": mGuardUserFWUserTable,
       "mGuardUserFWUserEntry": mGuardUserFWUserEntry,
       "mGuardUserFWUserIndex": mGuardUserFWUserIndex,
       "mGuardUserFWUserName": mGuardUserFWUserName,
       "mGuardUserFWUserAuthMethod": mGuardUserFWUserAuthMethod,
       "mGuardUserFWUserPassword": mGuardUserFWUserPassword,
       "mGuardUserFWUserRowStatus": mGuardUserFWUserRowStatus}
)
