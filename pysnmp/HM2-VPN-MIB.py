# SNMP MIB module (HM2-VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-VPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:35 2024
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

(HmLargeDisplayString,
 HmTimeSeconds1970,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmLargeDisplayString",
    "HmTimeSeconds1970",
    "hm2ConfigurationMibs")

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

hm2VpnMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 120)
)
hm2VpnMib.setRevisions(
        ("2014-03-14 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2VpnMibNotifications_ObjectIdentity = ObjectIdentity
hm2VpnMibNotifications = _Hm2VpnMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 0)
)
_Hm2VpnMibObjects_ObjectIdentity = ObjectIdentity
hm2VpnMibObjects = _Hm2VpnMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1)
)
_Hm2VpnGeneralGroup_ObjectIdentity = ObjectIdentity
hm2VpnGeneralGroup = _Hm2VpnGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 1)
)
_Hm2VpnConnectionGroup_ObjectIdentity = ObjectIdentity
hm2VpnConnectionGroup = _Hm2VpnConnectionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2)
)


class _Hm2VpnConnMax_Type(Integer32):
    """Custom type hm2VpnConnMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Hm2VpnConnMax_Type.__name__ = "Integer32"
_Hm2VpnConnMax_Object = MibScalar
hm2VpnConnMax = _Hm2VpnConnMax_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 1),
    _Hm2VpnConnMax_Type()
)
hm2VpnConnMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnConnMax.setStatus("current")


class _Hm2VpnConnActiveMax_Type(Integer32):
    """Custom type hm2VpnConnActiveMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Hm2VpnConnActiveMax_Type.__name__ = "Integer32"
_Hm2VpnConnActiveMax_Object = MibScalar
hm2VpnConnActiveMax = _Hm2VpnConnActiveMax_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 2),
    _Hm2VpnConnActiveMax_Type()
)
hm2VpnConnActiveMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnConnActiveMax.setStatus("current")


class _Hm2VpnConnNext_Type(Integer32):
    """Custom type hm2VpnConnNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Hm2VpnConnNext_Type.__name__ = "Integer32"
_Hm2VpnConnNext_Object = MibScalar
hm2VpnConnNext = _Hm2VpnConnNext_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 3),
    _Hm2VpnConnNext_Type()
)
hm2VpnConnNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnConnNext.setStatus("current")
_Hm2VpnConnTable_Object = MibTable
hm2VpnConnTable = _Hm2VpnConnTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10)
)
if mibBuilder.loadTexts:
    hm2VpnConnTable.setStatus("current")
_Hm2VpnConnEntry_Object = MibTableRow
hm2VpnConnEntry = _Hm2VpnConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1)
)
hm2VpnConnEntry.setIndexNames(
    (0, "HM2-VPN-MIB", "hm2VpnConnIndex"),
)
if mibBuilder.loadTexts:
    hm2VpnConnEntry.setStatus("current")


class _Hm2VpnConnIndex_Type(Integer32):
    """Custom type hm2VpnConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Hm2VpnConnIndex_Type.__name__ = "Integer32"
_Hm2VpnConnIndex_Object = MibTableColumn
hm2VpnConnIndex = _Hm2VpnConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 1),
    _Hm2VpnConnIndex_Type()
)
hm2VpnConnIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2VpnConnIndex.setStatus("current")


class _Hm2VpnConnIkeVersion_Type(Integer32):
    """Custom type hm2VpnConnIkeVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ike", 1),
          ("ikev1", 2),
          ("ikev2", 3))
    )


_Hm2VpnConnIkeVersion_Type.__name__ = "Integer32"
_Hm2VpnConnIkeVersion_Object = MibTableColumn
hm2VpnConnIkeVersion = _Hm2VpnConnIkeVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 2),
    _Hm2VpnConnIkeVersion_Type()
)
hm2VpnConnIkeVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIkeVersion.setStatus("current")


class _Hm2VpnConnIkeStartup_Type(Integer32):
    """Custom type hm2VpnConnIkeStartup based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initiator", 1),
          ("responder", 2))
    )


_Hm2VpnConnIkeStartup_Type.__name__ = "Integer32"
_Hm2VpnConnIkeStartup_Object = MibTableColumn
hm2VpnConnIkeStartup = _Hm2VpnConnIkeStartup_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 3),
    _Hm2VpnConnIkeStartup_Type()
)
hm2VpnConnIkeStartup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIkeStartup.setStatus("current")


class _Hm2VpnConnIkeLifetime_Type(Integer32):
    """Custom type hm2VpnConnIkeLifetime based on Integer32"""
    defaultValue = 28800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 86400),
    )


_Hm2VpnConnIkeLifetime_Type.__name__ = "Integer32"
_Hm2VpnConnIkeLifetime_Object = MibTableColumn
hm2VpnConnIkeLifetime = _Hm2VpnConnIkeLifetime_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 4),
    _Hm2VpnConnIkeLifetime_Type()
)
hm2VpnConnIkeLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIkeLifetime.setStatus("current")


class _Hm2VpnConnIkeDpdTimeout_Type(Integer32):
    """Custom type hm2VpnConnIkeDpdTimeout based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Hm2VpnConnIkeDpdTimeout_Type.__name__ = "Integer32"
_Hm2VpnConnIkeDpdTimeout_Object = MibTableColumn
hm2VpnConnIkeDpdTimeout = _Hm2VpnConnIkeDpdTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 5),
    _Hm2VpnConnIkeDpdTimeout_Type()
)
hm2VpnConnIkeDpdTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIkeDpdTimeout.setStatus("current")


class _Hm2VpnConnIkeLocalAddr_Type(DisplayString):
    """Custom type hm2VpnConnIkeLocalAddr based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2VpnConnIkeLocalAddr_Type.__name__ = "DisplayString"
_Hm2VpnConnIkeLocalAddr_Object = MibTableColumn
hm2VpnConnIkeLocalAddr = _Hm2VpnConnIkeLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 6),
    _Hm2VpnConnIkeLocalAddr_Type()
)
hm2VpnConnIkeLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIkeLocalAddr.setStatus("current")


class _Hm2VpnConnIkeRemoteAddr_Type(DisplayString):
    """Custom type hm2VpnConnIkeRemoteAddr based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2VpnConnIkeRemoteAddr_Type.__name__ = "DisplayString"
_Hm2VpnConnIkeRemoteAddr_Object = MibTableColumn
hm2VpnConnIkeRemoteAddr = _Hm2VpnConnIkeRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 7),
    _Hm2VpnConnIkeRemoteAddr_Type()
)
hm2VpnConnIkeRemoteAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIkeRemoteAddr.setStatus("current")


class _Hm2VpnConnIkeAuthType_Type(Integer32):
    """Custom type hm2VpnConnIkeAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("individualx509", 2),
          ("pkcs12", 3),
          ("psk", 1))
    )


_Hm2VpnConnIkeAuthType_Type.__name__ = "Integer32"
_Hm2VpnConnIkeAuthType_Object = MibTableColumn
hm2VpnConnIkeAuthType = _Hm2VpnConnIkeAuthType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 8),
    _Hm2VpnConnIkeAuthType_Type()
)
hm2VpnConnIkeAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIkeAuthType.setStatus("current")


class _Hm2VpnConnIkeAuthMode_Type(Integer32):
    """Custom type hm2VpnConnIkeAuthMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 2),
          ("main", 1))
    )


_Hm2VpnConnIkeAuthMode_Type.__name__ = "Integer32"
_Hm2VpnConnIkeAuthMode_Object = MibTableColumn
hm2VpnConnIkeAuthMode = _Hm2VpnConnIkeAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 9),
    _Hm2VpnConnIkeAuthMode_Type()
)
hm2VpnConnIkeAuthMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIkeAuthMode.setStatus("current")


class _Hm2VpnConnIkeAuthCertCA_Type(DisplayString):
    """Custom type hm2VpnConnIkeAuthCertCA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2VpnConnIkeAuthCertCA_Type.__name__ = "DisplayString"
_Hm2VpnConnIkeAuthCertCA_Object = MibTableColumn
hm2VpnConnIkeAuthCertCA = _Hm2VpnConnIkeAuthCertCA_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 10),
    _Hm2VpnConnIkeAuthCertCA_Type()
)
hm2VpnConnIkeAuthCertCA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIkeAuthCertCA.setStatus("current")


class _Hm2VpnConnIkeAuthCertRemote_Type(DisplayString):
    """Custom type hm2VpnConnIkeAuthCertRemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2VpnConnIkeAuthCertRemote_Type.__name__ = "DisplayString"
_Hm2VpnConnIkeAuthCertRemote_Object = MibTableColumn
hm2VpnConnIkeAuthCertRemote = _Hm2VpnConnIkeAuthCertRemote_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 11),
    _Hm2VpnConnIkeAuthCertRemote_Type()
)
hm2VpnConnIkeAuthCertRemote.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIkeAuthCertRemote.setStatus("current")


class _Hm2VpnConnIkeAuthCertLocal_Type(DisplayString):
    """Custom type hm2VpnConnIkeAuthCertLocal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2VpnConnIkeAuthCertLocal_Type.__name__ = "DisplayString"
_Hm2VpnConnIkeAuthCertLocal_Object = MibTableColumn
hm2VpnConnIkeAuthCertLocal = _Hm2VpnConnIkeAuthCertLocal_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 12),
    _Hm2VpnConnIkeAuthCertLocal_Type()
)
hm2VpnConnIkeAuthCertLocal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIkeAuthCertLocal.setStatus("current")


class _Hm2VpnConnIkeAuthPrivKey_Type(DisplayString):
    """Custom type hm2VpnConnIkeAuthPrivKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2VpnConnIkeAuthPrivKey_Type.__name__ = "DisplayString"
_Hm2VpnConnIkeAuthPrivKey_Object = MibTableColumn
hm2VpnConnIkeAuthPrivKey = _Hm2VpnConnIkeAuthPrivKey_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 13),
    _Hm2VpnConnIkeAuthPrivKey_Type()
)
hm2VpnConnIkeAuthPrivKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIkeAuthPrivKey.setStatus("current")


class _Hm2VpnConnIkeAuthPasswd_Type(DisplayString):
    """Custom type hm2VpnConnIkeAuthPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2VpnConnIkeAuthPasswd_Type.__name__ = "DisplayString"
_Hm2VpnConnIkeAuthPasswd_Object = MibTableColumn
hm2VpnConnIkeAuthPasswd = _Hm2VpnConnIkeAuthPasswd_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 14),
    _Hm2VpnConnIkeAuthPasswd_Type()
)
hm2VpnConnIkeAuthPasswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIkeAuthPasswd.setStatus("current")


class _Hm2VpnConnIkeAuthPsk_Type(DisplayString):
    """Custom type hm2VpnConnIkeAuthPsk based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2VpnConnIkeAuthPsk_Type.__name__ = "DisplayString"
_Hm2VpnConnIkeAuthPsk_Object = MibTableColumn
hm2VpnConnIkeAuthPsk = _Hm2VpnConnIkeAuthPsk_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 15),
    _Hm2VpnConnIkeAuthPsk_Type()
)
hm2VpnConnIkeAuthPsk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIkeAuthPsk.setStatus("current")


class _Hm2VpnConnIkeAuthLocId_Type(DisplayString):
    """Custom type hm2VpnConnIkeAuthLocId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2VpnConnIkeAuthLocId_Type.__name__ = "DisplayString"
_Hm2VpnConnIkeAuthLocId_Object = MibTableColumn
hm2VpnConnIkeAuthLocId = _Hm2VpnConnIkeAuthLocId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 16),
    _Hm2VpnConnIkeAuthLocId_Type()
)
hm2VpnConnIkeAuthLocId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIkeAuthLocId.setStatus("current")


class _Hm2VpnConnIkeAuthLocType_Type(Integer32):
    """Custom type hm2VpnConnIkeAuthLocType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("address", 2),
          ("default", 1),
          ("id", 3))
    )


_Hm2VpnConnIkeAuthLocType_Type.__name__ = "Integer32"
_Hm2VpnConnIkeAuthLocType_Object = MibTableColumn
hm2VpnConnIkeAuthLocType = _Hm2VpnConnIkeAuthLocType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 17),
    _Hm2VpnConnIkeAuthLocType_Type()
)
hm2VpnConnIkeAuthLocType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIkeAuthLocType.setStatus("current")


class _Hm2VpnConnIkeAuthRemId_Type(DisplayString):
    """Custom type hm2VpnConnIkeAuthRemId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2VpnConnIkeAuthRemId_Type.__name__ = "DisplayString"
_Hm2VpnConnIkeAuthRemId_Object = MibTableColumn
hm2VpnConnIkeAuthRemId = _Hm2VpnConnIkeAuthRemId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 18),
    _Hm2VpnConnIkeAuthRemId_Type()
)
hm2VpnConnIkeAuthRemId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIkeAuthRemId.setStatus("current")


class _Hm2VpnConnIkeAuthRemType_Type(Integer32):
    """Custom type hm2VpnConnIkeAuthRemType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("address", 2),
          ("any", 1),
          ("id", 3))
    )


_Hm2VpnConnIkeAuthRemType_Type.__name__ = "Integer32"
_Hm2VpnConnIkeAuthRemType_Object = MibTableColumn
hm2VpnConnIkeAuthRemType = _Hm2VpnConnIkeAuthRemType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 19),
    _Hm2VpnConnIkeAuthRemType_Type()
)
hm2VpnConnIkeAuthRemType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIkeAuthRemType.setStatus("current")


class _Hm2VpnConnIkeAlgDh_Type(Integer32):
    """Custom type hm2VpnConnIkeAlgDh based on Integer32"""
    defaultValue = 2

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
        *(("any", 1),
          ("modp1024", 2),
          ("modp1536", 3),
          ("modp2048", 4),
          ("modp3072", 5),
          ("modp4096", 6))
    )


_Hm2VpnConnIkeAlgDh_Type.__name__ = "Integer32"
_Hm2VpnConnIkeAlgDh_Object = MibTableColumn
hm2VpnConnIkeAlgDh = _Hm2VpnConnIkeAlgDh_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 20),
    _Hm2VpnConnIkeAlgDh_Type()
)
hm2VpnConnIkeAlgDh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIkeAlgDh.setStatus("current")


class _Hm2VpnConnIkeAlgMac_Type(Integer32):
    """Custom type hm2VpnConnIkeAlgMac based on Integer32"""
    defaultValue = 3

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
        *(("any", 1),
          ("hmacmd5", 2),
          ("hmacsha1", 3),
          ("hmacsha256", 4),
          ("hmacsha384", 5),
          ("hmacsha512", 6))
    )


_Hm2VpnConnIkeAlgMac_Type.__name__ = "Integer32"
_Hm2VpnConnIkeAlgMac_Object = MibTableColumn
hm2VpnConnIkeAlgMac = _Hm2VpnConnIkeAlgMac_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 21),
    _Hm2VpnConnIkeAlgMac_Type()
)
hm2VpnConnIkeAlgMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIkeAlgMac.setStatus("current")


class _Hm2VpnConnIkeAlgEncr_Type(Integer32):
    """Custom type hm2VpnConnIkeAlgEncr based on Integer32"""
    defaultValue = 4

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
        *(("aes128", 4),
          ("aes192", 5),
          ("aes256", 6),
          ("any", 1),
          ("des", 2),
          ("des3", 3))
    )


_Hm2VpnConnIkeAlgEncr_Type.__name__ = "Integer32"
_Hm2VpnConnIkeAlgEncr_Object = MibTableColumn
hm2VpnConnIkeAlgEncr = _Hm2VpnConnIkeAlgEncr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 22),
    _Hm2VpnConnIkeAlgEncr_Type()
)
hm2VpnConnIkeAlgEncr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIkeAlgEncr.setStatus("current")


class _Hm2VpnConnIkeReAuth_Type(TruthValue):
    """Custom type hm2VpnConnIkeReAuth based on TruthValue"""


_Hm2VpnConnIkeReAuth_Object = MibTableColumn
hm2VpnConnIkeReAuth = _Hm2VpnConnIkeReAuth_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 23),
    _Hm2VpnConnIkeReAuth_Type()
)
hm2VpnConnIkeReAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIkeReAuth.setStatus("current")


class _Hm2VpnConnIpsecMode_Type(Integer32):
    """Custom type hm2VpnConnIpsecMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("tunnel", 1)
    )


_Hm2VpnConnIpsecMode_Type.__name__ = "Integer32"
_Hm2VpnConnIpsecMode_Object = MibTableColumn
hm2VpnConnIpsecMode = _Hm2VpnConnIpsecMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 24),
    _Hm2VpnConnIpsecMode_Type()
)
hm2VpnConnIpsecMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIpsecMode.setStatus("current")


class _Hm2VpnConnIpsecLifetime_Type(Integer32):
    """Custom type hm2VpnConnIpsecLifetime based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 28800),
    )


_Hm2VpnConnIpsecLifetime_Type.__name__ = "Integer32"
_Hm2VpnConnIpsecLifetime_Object = MibTableColumn
hm2VpnConnIpsecLifetime = _Hm2VpnConnIpsecLifetime_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 25),
    _Hm2VpnConnIpsecLifetime_Type()
)
hm2VpnConnIpsecLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIpsecLifetime.setStatus("current")


class _Hm2VpnConnMargintime_Type(Integer32):
    """Custom type hm2VpnConnMargintime based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_Hm2VpnConnMargintime_Type.__name__ = "Integer32"
_Hm2VpnConnMargintime_Object = MibTableColumn
hm2VpnConnMargintime = _Hm2VpnConnMargintime_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 26),
    _Hm2VpnConnMargintime_Type()
)
hm2VpnConnMargintime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnMargintime.setStatus("current")


class _Hm2VpnConnIpsecAlgDh_Type(Integer32):
    """Custom type hm2VpnConnIpsecAlgDh based on Integer32"""
    defaultValue = 2

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
        *(("any", 1),
          ("modp1024", 2),
          ("modp1536", 3),
          ("modp2048", 4),
          ("modp3072", 5),
          ("modp4096", 6),
          ("none", 7))
    )


_Hm2VpnConnIpsecAlgDh_Type.__name__ = "Integer32"
_Hm2VpnConnIpsecAlgDh_Object = MibTableColumn
hm2VpnConnIpsecAlgDh = _Hm2VpnConnIpsecAlgDh_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 27),
    _Hm2VpnConnIpsecAlgDh_Type()
)
hm2VpnConnIpsecAlgDh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIpsecAlgDh.setStatus("current")


class _Hm2VpnConnIpsecAlgMac_Type(Integer32):
    """Custom type hm2VpnConnIpsecAlgMac based on Integer32"""
    defaultValue = 3

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
        *(("any", 1),
          ("hmacmd5", 2),
          ("hmacsha1", 3),
          ("hmacsha256", 4),
          ("hmacsha384", 5),
          ("hmacsha512", 6))
    )


_Hm2VpnConnIpsecAlgMac_Type.__name__ = "Integer32"
_Hm2VpnConnIpsecAlgMac_Object = MibTableColumn
hm2VpnConnIpsecAlgMac = _Hm2VpnConnIpsecAlgMac_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 28),
    _Hm2VpnConnIpsecAlgMac_Type()
)
hm2VpnConnIpsecAlgMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIpsecAlgMac.setStatus("current")


class _Hm2VpnConnIpsecAlgEncr_Type(Integer32):
    """Custom type hm2VpnConnIpsecAlgEncr based on Integer32"""
    defaultValue = 4

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
              18)
        )
    )
    namedValues = NamedValues(
        *(("aes128", 4),
          ("aes128ctr", 7),
          ("aes128gcm128", 12),
          ("aes128gcm64", 10),
          ("aes128gcm96", 11),
          ("aes192", 5),
          ("aes192ctr", 8),
          ("aes192gcm128", 15),
          ("aes192gcm64", 13),
          ("aes192gcm96", 14),
          ("aes256", 6),
          ("aes256ctr", 9),
          ("aes256gcm128", 18),
          ("aes256gcm64", 16),
          ("aes256gcm96", 17),
          ("any", 1),
          ("des", 2),
          ("des3", 3))
    )


_Hm2VpnConnIpsecAlgEncr_Type.__name__ = "Integer32"
_Hm2VpnConnIpsecAlgEncr_Object = MibTableColumn
hm2VpnConnIpsecAlgEncr = _Hm2VpnConnIpsecAlgEncr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 29),
    _Hm2VpnConnIpsecAlgEncr_Type()
)
hm2VpnConnIpsecAlgEncr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnIpsecAlgEncr.setStatus("current")


class _Hm2VpnConnOperStatus_Type(Integer32):
    """Custom type hm2VpnConnOperStatus based on Integer32"""
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
        *(("constructing", 4),
          ("dormant", 5),
          ("down", 2),
          ("negotiation", 3),
          ("re-keying", 6),
          ("up", 1))
    )


_Hm2VpnConnOperStatus_Type.__name__ = "Integer32"
_Hm2VpnConnOperStatus_Object = MibTableColumn
hm2VpnConnOperStatus = _Hm2VpnConnOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 30),
    _Hm2VpnConnOperStatus_Type()
)
hm2VpnConnOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnConnOperStatus.setStatus("current")


class _Hm2VpnConnDesc_Type(DisplayString):
    """Custom type hm2VpnConnDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2VpnConnDesc_Type.__name__ = "DisplayString"
_Hm2VpnConnDesc_Object = MibTableColumn
hm2VpnConnDesc = _Hm2VpnConnDesc_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 31),
    _Hm2VpnConnDesc_Type()
)
hm2VpnConnDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnDesc.setStatus("current")


class _Hm2VpnConnLastError_Type(HmLargeDisplayString):
    """Custom type hm2VpnConnLastError based on HmLargeDisplayString"""
    subtypeSpec = HmLargeDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_Hm2VpnConnLastError_Type.__name__ = "HmLargeDisplayString"
_Hm2VpnConnLastError_Object = MibTableColumn
hm2VpnConnLastError = _Hm2VpnConnLastError_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 32),
    _Hm2VpnConnLastError_Type()
)
hm2VpnConnLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnConnLastError.setStatus("current")


class _Hm2VpnConnDebug_Type(Bits):
    """Custom type hm2VpnConnDebug based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("informational", 0),
          ("unhandled", 1))
    )

_Hm2VpnConnDebug_Type.__name__ = "Bits"
_Hm2VpnConnDebug_Object = MibTableColumn
hm2VpnConnDebug = _Hm2VpnConnDebug_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 33),
    _Hm2VpnConnDebug_Type()
)
hm2VpnConnDebug.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnDebug.setStatus("current")
_Hm2VpnConnRowStatus_Type = RowStatus
_Hm2VpnConnRowStatus_Object = MibTableColumn
hm2VpnConnRowStatus = _Hm2VpnConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 10, 1, 34),
    _Hm2VpnConnRowStatus_Type()
)
hm2VpnConnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnConnRowStatus.setStatus("current")
_Hm2VpnConnInfoTable_Object = MibTable
hm2VpnConnInfoTable = _Hm2VpnConnInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 15)
)
if mibBuilder.loadTexts:
    hm2VpnConnInfoTable.setStatus("current")
_Hm2VpnConnInfoEntry_Object = MibTableRow
hm2VpnConnInfoEntry = _Hm2VpnConnInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 15, 1)
)
hm2VpnConnInfoEntry.setIndexNames(
    (0, "HM2-VPN-MIB", "hm2VpnConnIndex"),
)
if mibBuilder.loadTexts:
    hm2VpnConnInfoEntry.setStatus("current")


class _Hm2VpnConnInfoIkeVersionUsed_Type(Integer32):
    """Custom type hm2VpnConnInfoIkeVersionUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ikev1", 1),
          ("ikev2", 2))
    )


_Hm2VpnConnInfoIkeVersionUsed_Type.__name__ = "Integer32"
_Hm2VpnConnInfoIkeVersionUsed_Object = MibTableColumn
hm2VpnConnInfoIkeVersionUsed = _Hm2VpnConnInfoIkeVersionUsed_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 15, 1, 1),
    _Hm2VpnConnInfoIkeVersionUsed_Type()
)
hm2VpnConnInfoIkeVersionUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnConnInfoIkeVersionUsed.setStatus("current")


class _Hm2VpnConnInfoIkeProposal_Type(DisplayString):
    """Custom type hm2VpnConnInfoIkeProposal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2VpnConnInfoIkeProposal_Type.__name__ = "DisplayString"
_Hm2VpnConnInfoIkeProposal_Object = MibTableColumn
hm2VpnConnInfoIkeProposal = _Hm2VpnConnInfoIkeProposal_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 15, 1, 2),
    _Hm2VpnConnInfoIkeProposal_Type()
)
hm2VpnConnInfoIkeProposal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnConnInfoIkeProposal.setStatus("current")


class _Hm2VpnConnInfoIpsecProposal_Type(DisplayString):
    """Custom type hm2VpnConnInfoIpsecProposal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2VpnConnInfoIpsecProposal_Type.__name__ = "DisplayString"
_Hm2VpnConnInfoIpsecProposal_Object = MibTableColumn
hm2VpnConnInfoIpsecProposal = _Hm2VpnConnInfoIpsecProposal_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 15, 1, 3),
    _Hm2VpnConnInfoIpsecProposal_Type()
)
hm2VpnConnInfoIpsecProposal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnConnInfoIpsecProposal.setStatus("current")


class _Hm2VpnConnInfoLocalHost_Type(DisplayString):
    """Custom type hm2VpnConnInfoLocalHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2VpnConnInfoLocalHost_Type.__name__ = "DisplayString"
_Hm2VpnConnInfoLocalHost_Object = MibTableColumn
hm2VpnConnInfoLocalHost = _Hm2VpnConnInfoLocalHost_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 15, 1, 4),
    _Hm2VpnConnInfoLocalHost_Type()
)
hm2VpnConnInfoLocalHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnConnInfoLocalHost.setStatus("current")


class _Hm2VpnConnInfoRemoteHost_Type(DisplayString):
    """Custom type hm2VpnConnInfoRemoteHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2VpnConnInfoRemoteHost_Type.__name__ = "DisplayString"
_Hm2VpnConnInfoRemoteHost_Object = MibTableColumn
hm2VpnConnInfoRemoteHost = _Hm2VpnConnInfoRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 15, 1, 5),
    _Hm2VpnConnInfoRemoteHost_Type()
)
hm2VpnConnInfoRemoteHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnConnInfoRemoteHost.setStatus("current")
_Hm2VpnConnInfoEstablished_Type = Unsigned32
_Hm2VpnConnInfoEstablished_Object = MibTableColumn
hm2VpnConnInfoEstablished = _Hm2VpnConnInfoEstablished_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 15, 1, 6),
    _Hm2VpnConnInfoEstablished_Type()
)
hm2VpnConnInfoEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnConnInfoEstablished.setStatus("current")
_Hm2VpnConnInfoIKEReauth_Type = Unsigned32
_Hm2VpnConnInfoIKEReauth_Object = MibTableColumn
hm2VpnConnInfoIKEReauth = _Hm2VpnConnInfoIKEReauth_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 15, 1, 7),
    _Hm2VpnConnInfoIKEReauth_Type()
)
hm2VpnConnInfoIKEReauth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnConnInfoIKEReauth.setStatus("current")
_Hm2VpnConnInfoIKERekeying_Type = Unsigned32
_Hm2VpnConnInfoIKERekeying_Object = MibTableColumn
hm2VpnConnInfoIKERekeying = _Hm2VpnConnInfoIKERekeying_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 15, 1, 8),
    _Hm2VpnConnInfoIKERekeying_Type()
)
hm2VpnConnInfoIKERekeying.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnConnInfoIKERekeying.setStatus("current")
_Hm2VpnConnInfoIpsecRekeying_Type = Unsigned32
_Hm2VpnConnInfoIpsecRekeying_Object = MibTableColumn
hm2VpnConnInfoIpsecRekeying = _Hm2VpnConnInfoIpsecRekeying_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 15, 1, 9),
    _Hm2VpnConnInfoIpsecRekeying_Type()
)
hm2VpnConnInfoIpsecRekeying.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnConnInfoIpsecRekeying.setStatus("current")
_Hm2VpnConnInfoIpsecInBytes_Type = Counter64
_Hm2VpnConnInfoIpsecInBytes_Object = MibTableColumn
hm2VpnConnInfoIpsecInBytes = _Hm2VpnConnInfoIpsecInBytes_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 15, 1, 10),
    _Hm2VpnConnInfoIpsecInBytes_Type()
)
hm2VpnConnInfoIpsecInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnConnInfoIpsecInBytes.setStatus("current")
_Hm2VpnConnInfoIpsecInPackets_Type = Counter64
_Hm2VpnConnInfoIpsecInPackets_Object = MibTableColumn
hm2VpnConnInfoIpsecInPackets = _Hm2VpnConnInfoIpsecInPackets_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 15, 1, 11),
    _Hm2VpnConnInfoIpsecInPackets_Type()
)
hm2VpnConnInfoIpsecInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnConnInfoIpsecInPackets.setStatus("current")
_Hm2VpnConnInfoIpsecInUse_Type = Unsigned32
_Hm2VpnConnInfoIpsecInUse_Object = MibTableColumn
hm2VpnConnInfoIpsecInUse = _Hm2VpnConnInfoIpsecInUse_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 15, 1, 12),
    _Hm2VpnConnInfoIpsecInUse_Type()
)
hm2VpnConnInfoIpsecInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnConnInfoIpsecInUse.setStatus("current")
_Hm2VpnConnInfoIpsecOutBytes_Type = Counter64
_Hm2VpnConnInfoIpsecOutBytes_Object = MibTableColumn
hm2VpnConnInfoIpsecOutBytes = _Hm2VpnConnInfoIpsecOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 15, 1, 13),
    _Hm2VpnConnInfoIpsecOutBytes_Type()
)
hm2VpnConnInfoIpsecOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnConnInfoIpsecOutBytes.setStatus("current")
_Hm2VpnConnInfoIpsecOutPackets_Type = Counter64
_Hm2VpnConnInfoIpsecOutPackets_Object = MibTableColumn
hm2VpnConnInfoIpsecOutPackets = _Hm2VpnConnInfoIpsecOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 15, 1, 14),
    _Hm2VpnConnInfoIpsecOutPackets_Type()
)
hm2VpnConnInfoIpsecOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnConnInfoIpsecOutPackets.setStatus("current")
_Hm2VpnConnInfoIpsecOutUse_Type = Unsigned32
_Hm2VpnConnInfoIpsecOutUse_Object = MibTableColumn
hm2VpnConnInfoIpsecOutUse = _Hm2VpnConnInfoIpsecOutUse_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 15, 1, 15),
    _Hm2VpnConnInfoIpsecOutUse_Type()
)
hm2VpnConnInfoIpsecOutUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnConnInfoIpsecOutUse.setStatus("current")


class _Hm2VpnConnInfoIKEInitiatorSPI_Type(DisplayString):
    """Custom type hm2VpnConnInfoIKEInitiatorSPI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2VpnConnInfoIKEInitiatorSPI_Type.__name__ = "DisplayString"
_Hm2VpnConnInfoIKEInitiatorSPI_Object = MibTableColumn
hm2VpnConnInfoIKEInitiatorSPI = _Hm2VpnConnInfoIKEInitiatorSPI_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 15, 1, 16),
    _Hm2VpnConnInfoIKEInitiatorSPI_Type()
)
hm2VpnConnInfoIKEInitiatorSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnConnInfoIKEInitiatorSPI.setStatus("current")


class _Hm2VpnConnInfoIKEResponderSPI_Type(DisplayString):
    """Custom type hm2VpnConnInfoIKEResponderSPI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2VpnConnInfoIKEResponderSPI_Type.__name__ = "DisplayString"
_Hm2VpnConnInfoIKEResponderSPI_Object = MibTableColumn
hm2VpnConnInfoIKEResponderSPI = _Hm2VpnConnInfoIKEResponderSPI_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 15, 1, 17),
    _Hm2VpnConnInfoIKEResponderSPI_Type()
)
hm2VpnConnInfoIKEResponderSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnConnInfoIKEResponderSPI.setStatus("current")


class _Hm2VpnConnInfoIpsecInSPI_Type(DisplayString):
    """Custom type hm2VpnConnInfoIpsecInSPI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Hm2VpnConnInfoIpsecInSPI_Type.__name__ = "DisplayString"
_Hm2VpnConnInfoIpsecInSPI_Object = MibTableColumn
hm2VpnConnInfoIpsecInSPI = _Hm2VpnConnInfoIpsecInSPI_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 15, 1, 18),
    _Hm2VpnConnInfoIpsecInSPI_Type()
)
hm2VpnConnInfoIpsecInSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnConnInfoIpsecInSPI.setStatus("current")


class _Hm2VpnConnInfoIpsecOutSPI_Type(DisplayString):
    """Custom type hm2VpnConnInfoIpsecOutSPI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Hm2VpnConnInfoIpsecOutSPI_Type.__name__ = "DisplayString"
_Hm2VpnConnInfoIpsecOutSPI_Object = MibTableColumn
hm2VpnConnInfoIpsecOutSPI = _Hm2VpnConnInfoIpsecOutSPI_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 2, 15, 1, 19),
    _Hm2VpnConnInfoIpsecOutSPI_Type()
)
hm2VpnConnInfoIpsecOutSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnConnInfoIpsecOutSPI.setStatus("current")
_Hm2VpnTrafficSelGroup_ObjectIdentity = ObjectIdentity
hm2VpnTrafficSelGroup = _Hm2VpnTrafficSelGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 3)
)
_Hm2VpnTrafficSelTable_Object = MibTable
hm2VpnTrafficSelTable = _Hm2VpnTrafficSelTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hm2VpnTrafficSelTable.setStatus("current")
_Hm2VpnTrafficSelEntry_Object = MibTableRow
hm2VpnTrafficSelEntry = _Hm2VpnTrafficSelEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 3, 1, 1)
)
hm2VpnTrafficSelEntry.setIndexNames(
    (0, "HM2-VPN-MIB", "hm2VpnConnIndex"),
    (0, "HM2-VPN-MIB", "hm2VpnTrafficSelIndex"),
)
if mibBuilder.loadTexts:
    hm2VpnTrafficSelEntry.setStatus("current")


class _Hm2VpnTrafficSelIndex_Type(Integer32):
    """Custom type hm2VpnTrafficSelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Hm2VpnTrafficSelIndex_Type.__name__ = "Integer32"
_Hm2VpnTrafficSelIndex_Object = MibTableColumn
hm2VpnTrafficSelIndex = _Hm2VpnTrafficSelIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 3, 1, 1, 1),
    _Hm2VpnTrafficSelIndex_Type()
)
hm2VpnTrafficSelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2VpnTrafficSelIndex.setStatus("current")


class _Hm2VpnTrafficSelSrcAddr_Type(DisplayString):
    """Custom type hm2VpnTrafficSelSrcAddr based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2VpnTrafficSelSrcAddr_Type.__name__ = "DisplayString"
_Hm2VpnTrafficSelSrcAddr_Object = MibTableColumn
hm2VpnTrafficSelSrcAddr = _Hm2VpnTrafficSelSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 3, 1, 1, 2),
    _Hm2VpnTrafficSelSrcAddr_Type()
)
hm2VpnTrafficSelSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnTrafficSelSrcAddr.setStatus("current")


class _Hm2VpnTrafficSelDstAddr_Type(DisplayString):
    """Custom type hm2VpnTrafficSelDstAddr based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2VpnTrafficSelDstAddr_Type.__name__ = "DisplayString"
_Hm2VpnTrafficSelDstAddr_Object = MibTableColumn
hm2VpnTrafficSelDstAddr = _Hm2VpnTrafficSelDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 3, 1, 1, 3),
    _Hm2VpnTrafficSelDstAddr_Type()
)
hm2VpnTrafficSelDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnTrafficSelDstAddr.setStatus("current")


class _Hm2VpnTrafficSelSrcRest_Type(DisplayString):
    """Custom type hm2VpnTrafficSelSrcRest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2VpnTrafficSelSrcRest_Type.__name__ = "DisplayString"
_Hm2VpnTrafficSelSrcRest_Object = MibTableColumn
hm2VpnTrafficSelSrcRest = _Hm2VpnTrafficSelSrcRest_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 3, 1, 1, 4),
    _Hm2VpnTrafficSelSrcRest_Type()
)
hm2VpnTrafficSelSrcRest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnTrafficSelSrcRest.setStatus("current")


class _Hm2VpnTrafficSelDstRest_Type(DisplayString):
    """Custom type hm2VpnTrafficSelDstRest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2VpnTrafficSelDstRest_Type.__name__ = "DisplayString"
_Hm2VpnTrafficSelDstRest_Object = MibTableColumn
hm2VpnTrafficSelDstRest = _Hm2VpnTrafficSelDstRest_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 3, 1, 1, 5),
    _Hm2VpnTrafficSelDstRest_Type()
)
hm2VpnTrafficSelDstRest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnTrafficSelDstRest.setStatus("current")


class _Hm2VpnTrafficSelDesc_Type(DisplayString):
    """Custom type hm2VpnTrafficSelDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2VpnTrafficSelDesc_Type.__name__ = "DisplayString"
_Hm2VpnTrafficSelDesc_Object = MibTableColumn
hm2VpnTrafficSelDesc = _Hm2VpnTrafficSelDesc_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 3, 1, 1, 6),
    _Hm2VpnTrafficSelDesc_Type()
)
hm2VpnTrafficSelDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnTrafficSelDesc.setStatus("current")
_Hm2VpnTrafficSelRowStatus_Type = RowStatus
_Hm2VpnTrafficSelRowStatus_Object = MibTableColumn
hm2VpnTrafficSelRowStatus = _Hm2VpnTrafficSelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 3, 1, 1, 7),
    _Hm2VpnTrafficSelRowStatus_Type()
)
hm2VpnTrafficSelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2VpnTrafficSelRowStatus.setStatus("current")
_Hm2VpnCertificateGroup_ObjectIdentity = ObjectIdentity
hm2VpnCertificateGroup = _Hm2VpnCertificateGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 4)
)


class _Hm2VpnCertificateUploadPassphrase_Type(DisplayString):
    """Custom type hm2VpnCertificateUploadPassphrase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2VpnCertificateUploadPassphrase_Type.__name__ = "DisplayString"
_Hm2VpnCertificateUploadPassphrase_Object = MibScalar
hm2VpnCertificateUploadPassphrase = _Hm2VpnCertificateUploadPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 4, 1),
    _Hm2VpnCertificateUploadPassphrase_Type()
)
hm2VpnCertificateUploadPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2VpnCertificateUploadPassphrase.setStatus("current")
_Hm2VpnCertificateTable_Object = MibTable
hm2VpnCertificateTable = _Hm2VpnCertificateTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 4, 10)
)
if mibBuilder.loadTexts:
    hm2VpnCertificateTable.setStatus("current")
_Hm2VpnCertificateEntry_Object = MibTableRow
hm2VpnCertificateEntry = _Hm2VpnCertificateEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 4, 10, 1)
)
hm2VpnCertificateEntry.setIndexNames(
    (0, "HM2-VPN-MIB", "hm2VpnCertificateIndex"),
)
if mibBuilder.loadTexts:
    hm2VpnCertificateEntry.setStatus("current")


class _Hm2VpnCertificateIndex_Type(Integer32):
    """Custom type hm2VpnCertificateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hm2VpnCertificateIndex_Type.__name__ = "Integer32"
_Hm2VpnCertificateIndex_Object = MibTableColumn
hm2VpnCertificateIndex = _Hm2VpnCertificateIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 4, 10, 1, 1),
    _Hm2VpnCertificateIndex_Type()
)
hm2VpnCertificateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2VpnCertificateIndex.setStatus("current")


class _Hm2VpnCertificateSubject_Type(DisplayString):
    """Custom type hm2VpnCertificateSubject based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2VpnCertificateSubject_Type.__name__ = "DisplayString"
_Hm2VpnCertificateSubject_Object = MibTableColumn
hm2VpnCertificateSubject = _Hm2VpnCertificateSubject_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 4, 10, 1, 2),
    _Hm2VpnCertificateSubject_Type()
)
hm2VpnCertificateSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnCertificateSubject.setStatus("current")


class _Hm2VpnCertificateIssuer_Type(DisplayString):
    """Custom type hm2VpnCertificateIssuer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2VpnCertificateIssuer_Type.__name__ = "DisplayString"
_Hm2VpnCertificateIssuer_Object = MibTableColumn
hm2VpnCertificateIssuer = _Hm2VpnCertificateIssuer_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 4, 10, 1, 3),
    _Hm2VpnCertificateIssuer_Type()
)
hm2VpnCertificateIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnCertificateIssuer.setStatus("current")
_Hm2VpnCertificateStartDate_Type = HmTimeSeconds1970
_Hm2VpnCertificateStartDate_Object = MibTableColumn
hm2VpnCertificateStartDate = _Hm2VpnCertificateStartDate_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 4, 10, 1, 4),
    _Hm2VpnCertificateStartDate_Type()
)
hm2VpnCertificateStartDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnCertificateStartDate.setStatus("current")
_Hm2VpnCertificateEndDate_Type = HmTimeSeconds1970
_Hm2VpnCertificateEndDate_Object = MibTableColumn
hm2VpnCertificateEndDate = _Hm2VpnCertificateEndDate_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 4, 10, 1, 5),
    _Hm2VpnCertificateEndDate_Type()
)
hm2VpnCertificateEndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnCertificateEndDate.setStatus("current")


class _Hm2VpnCertificateFileName_Type(DisplayString):
    """Custom type hm2VpnCertificateFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hm2VpnCertificateFileName_Type.__name__ = "DisplayString"
_Hm2VpnCertificateFileName_Object = MibTableColumn
hm2VpnCertificateFileName = _Hm2VpnCertificateFileName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 4, 10, 1, 6),
    _Hm2VpnCertificateFileName_Type()
)
hm2VpnCertificateFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnCertificateFileName.setStatus("current")


class _Hm2VpnCertificateType_Type(Integer32):
    """Custom type hm2VpnCertificateType based on Integer32"""
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
        *(("ca", 1),
          ("encryptedkey", 3),
          ("encryptedpkcs12", 5),
          ("peer", 2),
          ("pkcs12", 4))
    )


_Hm2VpnCertificateType_Type.__name__ = "Integer32"
_Hm2VpnCertificateType_Object = MibTableColumn
hm2VpnCertificateType = _Hm2VpnCertificateType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 4, 10, 1, 7),
    _Hm2VpnCertificateType_Type()
)
hm2VpnCertificateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnCertificateType.setStatus("current")
_Hm2VpnCertificateCertUploadDate_Type = HmTimeSeconds1970
_Hm2VpnCertificateCertUploadDate_Object = MibTableColumn
hm2VpnCertificateCertUploadDate = _Hm2VpnCertificateCertUploadDate_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 4, 10, 1, 8),
    _Hm2VpnCertificateCertUploadDate_Type()
)
hm2VpnCertificateCertUploadDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnCertificateCertUploadDate.setStatus("current")


class _Hm2VpnCertificatePrivateKeyStatus_Type(Integer32):
    """Custom type hm2VpnCertificatePrivateKeyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("notFound", 3),
          ("present", 2))
    )


_Hm2VpnCertificatePrivateKeyStatus_Type.__name__ = "Integer32"
_Hm2VpnCertificatePrivateKeyStatus_Object = MibTableColumn
hm2VpnCertificatePrivateKeyStatus = _Hm2VpnCertificatePrivateKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 4, 10, 1, 9),
    _Hm2VpnCertificatePrivateKeyStatus_Type()
)
hm2VpnCertificatePrivateKeyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnCertificatePrivateKeyStatus.setStatus("current")


class _Hm2VpnCertificatePrivateKeyFile_Type(DisplayString):
    """Custom type hm2VpnCertificatePrivateKeyFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hm2VpnCertificatePrivateKeyFile_Type.__name__ = "DisplayString"
_Hm2VpnCertificatePrivateKeyFile_Object = MibTableColumn
hm2VpnCertificatePrivateKeyFile = _Hm2VpnCertificatePrivateKeyFile_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 4, 10, 1, 10),
    _Hm2VpnCertificatePrivateKeyFile_Type()
)
hm2VpnCertificatePrivateKeyFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnCertificatePrivateKeyFile.setStatus("current")


class _Hm2VpnCertificateNoConnections_Type(Integer32):
    """Custom type hm2VpnCertificateNoConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Hm2VpnCertificateNoConnections_Type.__name__ = "Integer32"
_Hm2VpnCertificateNoConnections_Object = MibTableColumn
hm2VpnCertificateNoConnections = _Hm2VpnCertificateNoConnections_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 4, 10, 1, 11),
    _Hm2VpnCertificateNoConnections_Type()
)
hm2VpnCertificateNoConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2VpnCertificateNoConnections.setStatus("current")


class _Hm2VpnCertificateUserActions_Type(Integer32):
    """Custom type hm2VpnCertificateUserActions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_Hm2VpnCertificateUserActions_Type.__name__ = "Integer32"
_Hm2VpnCertificateUserActions_Object = MibTableColumn
hm2VpnCertificateUserActions = _Hm2VpnCertificateUserActions_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 1, 4, 10, 1, 12),
    _Hm2VpnCertificateUserActions_Type()
)
hm2VpnCertificateUserActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2VpnCertificateUserActions.setStatus("current")
_Hm2VpnMibSNMPExtensionGroup_ObjectIdentity = ObjectIdentity
hm2VpnMibSNMPExtensionGroup = _Hm2VpnMibSNMPExtensionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 3)
)
_Hm2VpnMibSNMPExtensionNoTrafficSelector_ObjectIdentity = ObjectIdentity
hm2VpnMibSNMPExtensionNoTrafficSelector = _Hm2VpnMibSNMPExtensionNoTrafficSelector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 3, 1)
)
if mibBuilder.loadTexts:
    hm2VpnMibSNMPExtensionNoTrafficSelector.setStatus("current")
_Hm2VpnMibSNMPExtensionTooManyActive_ObjectIdentity = ObjectIdentity
hm2VpnMibSNMPExtensionTooManyActive = _Hm2VpnMibSNMPExtensionTooManyActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 3, 2)
)
if mibBuilder.loadTexts:
    hm2VpnMibSNMPExtensionTooManyActive.setStatus("current")
_Hm2VpnMibSNMPExtensionTooManyConns_ObjectIdentity = ObjectIdentity
hm2VpnMibSNMPExtensionTooManyConns = _Hm2VpnMibSNMPExtensionTooManyConns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 3, 3)
)
if mibBuilder.loadTexts:
    hm2VpnMibSNMPExtensionTooManyConns.setStatus("current")
_Hm2VpnMibSNMPExtensionActiveRow_ObjectIdentity = ObjectIdentity
hm2VpnMibSNMPExtensionActiveRow = _Hm2VpnMibSNMPExtensionActiveRow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 3, 4)
)
if mibBuilder.loadTexts:
    hm2VpnMibSNMPExtensionActiveRow.setStatus("current")
_Hm2VpnMibSNMPExtensionInitiatorAny_ObjectIdentity = ObjectIdentity
hm2VpnMibSNMPExtensionInitiatorAny = _Hm2VpnMibSNMPExtensionInitiatorAny_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 3, 5)
)
if mibBuilder.loadTexts:
    hm2VpnMibSNMPExtensionInitiatorAny.setStatus("current")

# Managed Objects groups


# Notification objects

hm2VpnUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 0, 1)
)
hm2VpnUpTrap.setObjects(
      *(("HM2-VPN-MIB", "hm2VpnConnIndex"),
        ("HM2-VPN-MIB", "hm2VpnConnOperStatus"))
)
if mibBuilder.loadTexts:
    hm2VpnUpTrap.setStatus(
        "current"
    )

hm2VpnDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 120, 0, 2)
)
hm2VpnDownTrap.setObjects(
      *(("HM2-VPN-MIB", "hm2VpnConnIndex"),
        ("HM2-VPN-MIB", "hm2VpnConnOperStatus"))
)
if mibBuilder.loadTexts:
    hm2VpnDownTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-VPN-MIB",
    **{"hm2VpnMib": hm2VpnMib,
       "hm2VpnMibNotifications": hm2VpnMibNotifications,
       "hm2VpnUpTrap": hm2VpnUpTrap,
       "hm2VpnDownTrap": hm2VpnDownTrap,
       "hm2VpnMibObjects": hm2VpnMibObjects,
       "hm2VpnGeneralGroup": hm2VpnGeneralGroup,
       "hm2VpnConnectionGroup": hm2VpnConnectionGroup,
       "hm2VpnConnMax": hm2VpnConnMax,
       "hm2VpnConnActiveMax": hm2VpnConnActiveMax,
       "hm2VpnConnNext": hm2VpnConnNext,
       "hm2VpnConnTable": hm2VpnConnTable,
       "hm2VpnConnEntry": hm2VpnConnEntry,
       "hm2VpnConnIndex": hm2VpnConnIndex,
       "hm2VpnConnIkeVersion": hm2VpnConnIkeVersion,
       "hm2VpnConnIkeStartup": hm2VpnConnIkeStartup,
       "hm2VpnConnIkeLifetime": hm2VpnConnIkeLifetime,
       "hm2VpnConnIkeDpdTimeout": hm2VpnConnIkeDpdTimeout,
       "hm2VpnConnIkeLocalAddr": hm2VpnConnIkeLocalAddr,
       "hm2VpnConnIkeRemoteAddr": hm2VpnConnIkeRemoteAddr,
       "hm2VpnConnIkeAuthType": hm2VpnConnIkeAuthType,
       "hm2VpnConnIkeAuthMode": hm2VpnConnIkeAuthMode,
       "hm2VpnConnIkeAuthCertCA": hm2VpnConnIkeAuthCertCA,
       "hm2VpnConnIkeAuthCertRemote": hm2VpnConnIkeAuthCertRemote,
       "hm2VpnConnIkeAuthCertLocal": hm2VpnConnIkeAuthCertLocal,
       "hm2VpnConnIkeAuthPrivKey": hm2VpnConnIkeAuthPrivKey,
       "hm2VpnConnIkeAuthPasswd": hm2VpnConnIkeAuthPasswd,
       "hm2VpnConnIkeAuthPsk": hm2VpnConnIkeAuthPsk,
       "hm2VpnConnIkeAuthLocId": hm2VpnConnIkeAuthLocId,
       "hm2VpnConnIkeAuthLocType": hm2VpnConnIkeAuthLocType,
       "hm2VpnConnIkeAuthRemId": hm2VpnConnIkeAuthRemId,
       "hm2VpnConnIkeAuthRemType": hm2VpnConnIkeAuthRemType,
       "hm2VpnConnIkeAlgDh": hm2VpnConnIkeAlgDh,
       "hm2VpnConnIkeAlgMac": hm2VpnConnIkeAlgMac,
       "hm2VpnConnIkeAlgEncr": hm2VpnConnIkeAlgEncr,
       "hm2VpnConnIkeReAuth": hm2VpnConnIkeReAuth,
       "hm2VpnConnIpsecMode": hm2VpnConnIpsecMode,
       "hm2VpnConnIpsecLifetime": hm2VpnConnIpsecLifetime,
       "hm2VpnConnMargintime": hm2VpnConnMargintime,
       "hm2VpnConnIpsecAlgDh": hm2VpnConnIpsecAlgDh,
       "hm2VpnConnIpsecAlgMac": hm2VpnConnIpsecAlgMac,
       "hm2VpnConnIpsecAlgEncr": hm2VpnConnIpsecAlgEncr,
       "hm2VpnConnOperStatus": hm2VpnConnOperStatus,
       "hm2VpnConnDesc": hm2VpnConnDesc,
       "hm2VpnConnLastError": hm2VpnConnLastError,
       "hm2VpnConnDebug": hm2VpnConnDebug,
       "hm2VpnConnRowStatus": hm2VpnConnRowStatus,
       "hm2VpnConnInfoTable": hm2VpnConnInfoTable,
       "hm2VpnConnInfoEntry": hm2VpnConnInfoEntry,
       "hm2VpnConnInfoIkeVersionUsed": hm2VpnConnInfoIkeVersionUsed,
       "hm2VpnConnInfoIkeProposal": hm2VpnConnInfoIkeProposal,
       "hm2VpnConnInfoIpsecProposal": hm2VpnConnInfoIpsecProposal,
       "hm2VpnConnInfoLocalHost": hm2VpnConnInfoLocalHost,
       "hm2VpnConnInfoRemoteHost": hm2VpnConnInfoRemoteHost,
       "hm2VpnConnInfoEstablished": hm2VpnConnInfoEstablished,
       "hm2VpnConnInfoIKEReauth": hm2VpnConnInfoIKEReauth,
       "hm2VpnConnInfoIKERekeying": hm2VpnConnInfoIKERekeying,
       "hm2VpnConnInfoIpsecRekeying": hm2VpnConnInfoIpsecRekeying,
       "hm2VpnConnInfoIpsecInBytes": hm2VpnConnInfoIpsecInBytes,
       "hm2VpnConnInfoIpsecInPackets": hm2VpnConnInfoIpsecInPackets,
       "hm2VpnConnInfoIpsecInUse": hm2VpnConnInfoIpsecInUse,
       "hm2VpnConnInfoIpsecOutBytes": hm2VpnConnInfoIpsecOutBytes,
       "hm2VpnConnInfoIpsecOutPackets": hm2VpnConnInfoIpsecOutPackets,
       "hm2VpnConnInfoIpsecOutUse": hm2VpnConnInfoIpsecOutUse,
       "hm2VpnConnInfoIKEInitiatorSPI": hm2VpnConnInfoIKEInitiatorSPI,
       "hm2VpnConnInfoIKEResponderSPI": hm2VpnConnInfoIKEResponderSPI,
       "hm2VpnConnInfoIpsecInSPI": hm2VpnConnInfoIpsecInSPI,
       "hm2VpnConnInfoIpsecOutSPI": hm2VpnConnInfoIpsecOutSPI,
       "hm2VpnTrafficSelGroup": hm2VpnTrafficSelGroup,
       "hm2VpnTrafficSelTable": hm2VpnTrafficSelTable,
       "hm2VpnTrafficSelEntry": hm2VpnTrafficSelEntry,
       "hm2VpnTrafficSelIndex": hm2VpnTrafficSelIndex,
       "hm2VpnTrafficSelSrcAddr": hm2VpnTrafficSelSrcAddr,
       "hm2VpnTrafficSelDstAddr": hm2VpnTrafficSelDstAddr,
       "hm2VpnTrafficSelSrcRest": hm2VpnTrafficSelSrcRest,
       "hm2VpnTrafficSelDstRest": hm2VpnTrafficSelDstRest,
       "hm2VpnTrafficSelDesc": hm2VpnTrafficSelDesc,
       "hm2VpnTrafficSelRowStatus": hm2VpnTrafficSelRowStatus,
       "hm2VpnCertificateGroup": hm2VpnCertificateGroup,
       "hm2VpnCertificateUploadPassphrase": hm2VpnCertificateUploadPassphrase,
       "hm2VpnCertificateTable": hm2VpnCertificateTable,
       "hm2VpnCertificateEntry": hm2VpnCertificateEntry,
       "hm2VpnCertificateIndex": hm2VpnCertificateIndex,
       "hm2VpnCertificateSubject": hm2VpnCertificateSubject,
       "hm2VpnCertificateIssuer": hm2VpnCertificateIssuer,
       "hm2VpnCertificateStartDate": hm2VpnCertificateStartDate,
       "hm2VpnCertificateEndDate": hm2VpnCertificateEndDate,
       "hm2VpnCertificateFileName": hm2VpnCertificateFileName,
       "hm2VpnCertificateType": hm2VpnCertificateType,
       "hm2VpnCertificateCertUploadDate": hm2VpnCertificateCertUploadDate,
       "hm2VpnCertificatePrivateKeyStatus": hm2VpnCertificatePrivateKeyStatus,
       "hm2VpnCertificatePrivateKeyFile": hm2VpnCertificatePrivateKeyFile,
       "hm2VpnCertificateNoConnections": hm2VpnCertificateNoConnections,
       "hm2VpnCertificateUserActions": hm2VpnCertificateUserActions,
       "hm2VpnMibSNMPExtensionGroup": hm2VpnMibSNMPExtensionGroup,
       "hm2VpnMibSNMPExtensionNoTrafficSelector": hm2VpnMibSNMPExtensionNoTrafficSelector,
       "hm2VpnMibSNMPExtensionTooManyActive": hm2VpnMibSNMPExtensionTooManyActive,
       "hm2VpnMibSNMPExtensionTooManyConns": hm2VpnMibSNMPExtensionTooManyConns,
       "hm2VpnMibSNMPExtensionActiveRow": hm2VpnMibSNMPExtensionActiveRow,
       "hm2VpnMibSNMPExtensionInitiatorAny": hm2VpnMibSNMPExtensionInitiatorAny}
)
