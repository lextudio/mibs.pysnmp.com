# SNMP MIB module (HP-ICF-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-NTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:51 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

hpicfNtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121)
)
hpicfNtpMIB.setRevisions(
        ("2017-08-22 00:00",
         "2016-02-10 00:00",
         "2015-07-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfNtpConfig_ObjectIdentity = ObjectIdentity
hpicfNtpConfig = _HpicfNtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1)
)
_HpicfNtpConfigScalars_ObjectIdentity = ObjectIdentity
hpicfNtpConfigScalars = _HpicfNtpConfigScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 1)
)


class _HpicfNtpConfigMode_Type(Integer32):
    """Custom type hpicfNtpConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 3),
          ("disabled", 1),
          ("unicast", 2))
    )


_HpicfNtpConfigMode_Type.__name__ = "Integer32"
_HpicfNtpConfigMode_Object = MibScalar
hpicfNtpConfigMode = _HpicfNtpConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 1, 1),
    _HpicfNtpConfigMode_Type()
)
hpicfNtpConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfNtpConfigMode.setStatus("current")


class _HpicfNtpMaxAssociation_Type(Integer32):
    """Custom type hpicfNtpMaxAssociation based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HpicfNtpMaxAssociation_Type.__name__ = "Integer32"
_HpicfNtpMaxAssociation_Object = MibScalar
hpicfNtpMaxAssociation = _HpicfNtpMaxAssociation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 1, 2),
    _HpicfNtpMaxAssociation_Type()
)
hpicfNtpMaxAssociation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfNtpMaxAssociation.setStatus("current")
_HpicfNtpStatusReferenceTimeFrac_Type = Unsigned32
_HpicfNtpStatusReferenceTimeFrac_Object = MibScalar
hpicfNtpStatusReferenceTimeFrac = _HpicfNtpStatusReferenceTimeFrac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 1, 3),
    _HpicfNtpStatusReferenceTimeFrac_Type()
)
hpicfNtpStatusReferenceTimeFrac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpStatusReferenceTimeFrac.setStatus("current")
_HpicfNtpStatusReferenceTimeSec_Type = Unsigned32
_HpicfNtpStatusReferenceTimeSec_Object = MibScalar
hpicfNtpStatusReferenceTimeSec = _HpicfNtpStatusReferenceTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 1, 4),
    _HpicfNtpStatusReferenceTimeSec_Type()
)
hpicfNtpStatusReferenceTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpStatusReferenceTimeSec.setStatus("current")


class _HpicfNtpStatusClockOffset_Type(OctetString):
    """Custom type hpicfNtpStatusClockOffset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_HpicfNtpStatusClockOffset_Type.__name__ = "OctetString"
_HpicfNtpStatusClockOffset_Object = MibScalar
hpicfNtpStatusClockOffset = _HpicfNtpStatusClockOffset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 1, 5),
    _HpicfNtpStatusClockOffset_Type()
)
hpicfNtpStatusClockOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpStatusClockOffset.setStatus("current")


class _HpicfNtpStatusRootDelay_Type(OctetString):
    """Custom type hpicfNtpStatusRootDelay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_HpicfNtpStatusRootDelay_Type.__name__ = "OctetString"
_HpicfNtpStatusRootDelay_Object = MibScalar
hpicfNtpStatusRootDelay = _HpicfNtpStatusRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 1, 6),
    _HpicfNtpStatusRootDelay_Type()
)
hpicfNtpStatusRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpStatusRootDelay.setStatus("current")


class _HpicfNtpStatusRootDispersion_Type(OctetString):
    """Custom type hpicfNtpStatusRootDispersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_HpicfNtpStatusRootDispersion_Type.__name__ = "OctetString"
_HpicfNtpStatusRootDispersion_Object = MibScalar
hpicfNtpStatusRootDispersion = _HpicfNtpStatusRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 1, 7),
    _HpicfNtpStatusRootDispersion_Type()
)
hpicfNtpStatusRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpStatusRootDispersion.setStatus("current")


class _HpicfNtpAssoDrift_Type(OctetString):
    """Custom type hpicfNtpAssoDrift based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_HpicfNtpAssoDrift_Type.__name__ = "OctetString"
_HpicfNtpAssoDrift_Object = MibScalar
hpicfNtpAssoDrift = _HpicfNtpAssoDrift_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 1, 8),
    _HpicfNtpAssoDrift_Type()
)
hpicfNtpAssoDrift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpAssoDrift.setStatus("current")
_HpicfNtpInetConfigServerTable_Object = MibTable
hpicfNtpInetConfigServerTable = _HpicfNtpInetConfigServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfNtpInetConfigServerTable.setStatus("current")
_HpicfNtpInetConfigServerEntry_Object = MibTableRow
hpicfNtpInetConfigServerEntry = _HpicfNtpInetConfigServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 2, 1)
)
hpicfNtpInetConfigServerEntry.setIndexNames(
    (0, "HP-ICF-NTP-MIB", "hpicfNtpInetServerAddressType"),
    (0, "HP-ICF-NTP-MIB", "hpicfNtpInetServerAddress"),
)
if mibBuilder.loadTexts:
    hpicfNtpInetConfigServerEntry.setStatus("current")
_HpicfNtpInetServerAddressType_Type = InetAddressType
_HpicfNtpInetServerAddressType_Object = MibTableColumn
hpicfNtpInetServerAddressType = _HpicfNtpInetServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 2, 1, 1),
    _HpicfNtpInetServerAddressType_Type()
)
hpicfNtpInetServerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfNtpInetServerAddressType.setStatus("current")


class _HpicfNtpInetServerAddress_Type(InetAddress):
    """Custom type hpicfNtpInetServerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_HpicfNtpInetServerAddress_Type.__name__ = "InetAddress"
_HpicfNtpInetServerAddress_Object = MibTableColumn
hpicfNtpInetServerAddress = _HpicfNtpInetServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 2, 1, 2),
    _HpicfNtpInetServerAddress_Type()
)
hpicfNtpInetServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfNtpInetServerAddress.setStatus("current")
_HpicfNtpInetServerRowStatus_Type = RowStatus
_HpicfNtpInetServerRowStatus_Object = MibTableColumn
hpicfNtpInetServerRowStatus = _HpicfNtpInetServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 2, 1, 4),
    _HpicfNtpInetServerRowStatus_Type()
)
hpicfNtpInetServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfNtpInetServerRowStatus.setStatus("current")


class _HpicfNtpInetServerAuthKeyId_Type(Unsigned32):
    """Custom type hpicfNtpInetServerAuthKeyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpicfNtpInetServerAuthKeyId_Type.__name__ = "Unsigned32"
_HpicfNtpInetServerAuthKeyId_Object = MibTableColumn
hpicfNtpInetServerAuthKeyId = _HpicfNtpInetServerAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 2, 1, 5),
    _HpicfNtpInetServerAuthKeyId_Type()
)
hpicfNtpInetServerAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfNtpInetServerAuthKeyId.setStatus("current")


class _HpicfNtpConfigPollMinInterval_Type(Integer32):
    """Custom type hpicfNtpConfigPollMinInterval based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 17),
    )


_HpicfNtpConfigPollMinInterval_Type.__name__ = "Integer32"
_HpicfNtpConfigPollMinInterval_Object = MibTableColumn
hpicfNtpConfigPollMinInterval = _HpicfNtpConfigPollMinInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 2, 1, 6),
    _HpicfNtpConfigPollMinInterval_Type()
)
hpicfNtpConfigPollMinInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfNtpConfigPollMinInterval.setStatus("current")


class _HpicfNtpConfigPollMaxInterval_Type(Integer32):
    """Custom type hpicfNtpConfigPollMaxInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 17),
    )


_HpicfNtpConfigPollMaxInterval_Type.__name__ = "Integer32"
_HpicfNtpConfigPollMaxInterval_Object = MibTableColumn
hpicfNtpConfigPollMaxInterval = _HpicfNtpConfigPollMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 2, 1, 7),
    _HpicfNtpConfigPollMaxInterval_Type()
)
hpicfNtpConfigPollMaxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfNtpConfigPollMaxInterval.setStatus("current")


class _HpicfNtpAssoBurst_Type(Integer32):
    """Custom type hpicfNtpAssoBurst based on Integer32"""
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
        *(("burst", 2),
          ("iburst", 3),
          ("noburst", 1))
    )


_HpicfNtpAssoBurst_Type.__name__ = "Integer32"
_HpicfNtpAssoBurst_Object = MibTableColumn
hpicfNtpAssoBurst = _HpicfNtpAssoBurst_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 2, 1, 8),
    _HpicfNtpAssoBurst_Type()
)
hpicfNtpAssoBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfNtpAssoBurst.setStatus("current")


class _HpicfNtpAssoIsOobm_Type(TruthValue):
    """Custom type hpicfNtpAssoIsOobm based on TruthValue"""


_HpicfNtpAssoIsOobm_Object = MibTableColumn
hpicfNtpAssoIsOobm = _HpicfNtpAssoIsOobm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 2, 1, 9),
    _HpicfNtpAssoIsOobm_Type()
)
hpicfNtpAssoIsOobm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfNtpAssoIsOobm.setStatus("current")
_HpicfNtpInetServerInfoTable_Object = MibTable
hpicfNtpInetServerInfoTable = _HpicfNtpInetServerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfNtpInetServerInfoTable.setStatus("current")
_HpicfNtpInetServerInfoEntry_Object = MibTableRow
hpicfNtpInetServerInfoEntry = _HpicfNtpInetServerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1)
)
hpicfNtpInetServerInfoEntry.setIndexNames(
    (0, "HP-ICF-NTP-MIB", "hpicfNtpInetServerAddressType"),
    (0, "HP-ICF-NTP-MIB", "hpicfNtpInetServerAddress"),
)
if mibBuilder.loadTexts:
    hpicfNtpInetServerInfoEntry.setStatus("current")
_HpicfNtpAssoOurPollInterval_Type = Integer32
_HpicfNtpAssoOurPollInterval_Object = MibTableColumn
hpicfNtpAssoOurPollInterval = _HpicfNtpAssoOurPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 1),
    _HpicfNtpAssoOurPollInterval_Type()
)
hpicfNtpAssoOurPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpAssoOurPollInterval.setStatus("current")
_HpicfNtpAssoPeerPollInterval_Type = Integer32
_HpicfNtpAssoPeerPollInterval_Object = MibTableColumn
hpicfNtpAssoPeerPollInterval = _HpicfNtpAssoPeerPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 2),
    _HpicfNtpAssoPeerPollInterval_Type()
)
hpicfNtpAssoPeerPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpAssoPeerPollInterval.setStatus("current")


class _HpicfNtpAssoRootDelay_Type(OctetString):
    """Custom type hpicfNtpAssoRootDelay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_HpicfNtpAssoRootDelay_Type.__name__ = "OctetString"
_HpicfNtpAssoRootDelay_Object = MibTableColumn
hpicfNtpAssoRootDelay = _HpicfNtpAssoRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 3),
    _HpicfNtpAssoRootDelay_Type()
)
hpicfNtpAssoRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpAssoRootDelay.setStatus("current")


class _HpicfNtpAssoRootDispersion_Type(OctetString):
    """Custom type hpicfNtpAssoRootDispersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_HpicfNtpAssoRootDispersion_Type.__name__ = "OctetString"
_HpicfNtpAssoRootDispersion_Object = MibTableColumn
hpicfNtpAssoRootDispersion = _HpicfNtpAssoRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 4),
    _HpicfNtpAssoRootDispersion_Type()
)
hpicfNtpAssoRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpAssoRootDispersion.setStatus("current")


class _HpicfNtpAssoPeerReach_Type(OctetString):
    """Custom type hpicfNtpAssoPeerReach based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_HpicfNtpAssoPeerReach_Type.__name__ = "OctetString"
_HpicfNtpAssoPeerReach_Object = MibTableColumn
hpicfNtpAssoPeerReach = _HpicfNtpAssoPeerReach_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 6),
    _HpicfNtpAssoPeerReach_Type()
)
hpicfNtpAssoPeerReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpAssoPeerReach.setStatus("current")
_HpicfNtpAssoOriginTimeFrac_Type = Unsigned32
_HpicfNtpAssoOriginTimeFrac_Object = MibTableColumn
hpicfNtpAssoOriginTimeFrac = _HpicfNtpAssoOriginTimeFrac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 7),
    _HpicfNtpAssoOriginTimeFrac_Type()
)
hpicfNtpAssoOriginTimeFrac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpAssoOriginTimeFrac.setStatus("current")
_HpicfNtpAssoOriginTimeSec_Type = Unsigned32
_HpicfNtpAssoOriginTimeSec_Object = MibTableColumn
hpicfNtpAssoOriginTimeSec = _HpicfNtpAssoOriginTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 8),
    _HpicfNtpAssoOriginTimeSec_Type()
)
hpicfNtpAssoOriginTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpAssoOriginTimeSec.setStatus("current")
_HpicfNtpAssoRecvTimeFrac_Type = Unsigned32
_HpicfNtpAssoRecvTimeFrac_Object = MibTableColumn
hpicfNtpAssoRecvTimeFrac = _HpicfNtpAssoRecvTimeFrac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 9),
    _HpicfNtpAssoRecvTimeFrac_Type()
)
hpicfNtpAssoRecvTimeFrac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpAssoRecvTimeFrac.setStatus("current")
_HpicfNtpAssoRecvTimeSec_Type = Unsigned32
_HpicfNtpAssoRecvTimeSec_Object = MibTableColumn
hpicfNtpAssoRecvTimeSec = _HpicfNtpAssoRecvTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 10),
    _HpicfNtpAssoRecvTimeSec_Type()
)
hpicfNtpAssoRecvTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpAssoRecvTimeSec.setStatus("current")
_HpicfNtpAssoXmtTimeFrac_Type = Unsigned32
_HpicfNtpAssoXmtTimeFrac_Object = MibTableColumn
hpicfNtpAssoXmtTimeFrac = _HpicfNtpAssoXmtTimeFrac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 11),
    _HpicfNtpAssoXmtTimeFrac_Type()
)
hpicfNtpAssoXmtTimeFrac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpAssoXmtTimeFrac.setStatus("current")
_HpicfNtpAssoXmtTimeSec_Type = Unsigned32
_HpicfNtpAssoXmtTimeSec_Object = MibTableColumn
hpicfNtpAssoXmtTimeSec = _HpicfNtpAssoXmtTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 12),
    _HpicfNtpAssoXmtTimeSec_Type()
)
hpicfNtpAssoXmtTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpAssoXmtTimeSec.setStatus("current")
_HpicfNtpAssolastPollreq_Type = Integer32
_HpicfNtpAssolastPollreq_Object = MibTableColumn
hpicfNtpAssolastPollreq = _HpicfNtpAssolastPollreq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 13),
    _HpicfNtpAssolastPollreq_Type()
)
hpicfNtpAssolastPollreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpAssolastPollreq.setStatus("current")
_HpicfNtpAssoPrecision_Type = Integer32
_HpicfNtpAssoPrecision_Object = MibTableColumn
hpicfNtpAssoPrecision = _HpicfNtpAssoPrecision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 14),
    _HpicfNtpAssoPrecision_Type()
)
hpicfNtpAssoPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpAssoPrecision.setStatus("current")


class _HpicfNtpAssoCurrentMode_Type(Integer32):
    """Custom type hpicfNtpAssoCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("notsynchronized", 2),
          ("synchronized", 1),
          ("unknown", 99))
    )


_HpicfNtpAssoCurrentMode_Type.__name__ = "Integer32"
_HpicfNtpAssoCurrentMode_Object = MibTableColumn
hpicfNtpAssoCurrentMode = _HpicfNtpAssoCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 15),
    _HpicfNtpAssoCurrentMode_Type()
)
hpicfNtpAssoCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpAssoCurrentMode.setStatus("current")


class _HpicfNtpAssoPeerDispersion_Type(OctetString):
    """Custom type hpicfNtpAssoPeerDispersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_HpicfNtpAssoPeerDispersion_Type.__name__ = "OctetString"
_HpicfNtpAssoPeerDispersion_Object = MibTableColumn
hpicfNtpAssoPeerDispersion = _HpicfNtpAssoPeerDispersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 16),
    _HpicfNtpAssoPeerDispersion_Type()
)
hpicfNtpAssoPeerDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpAssoPeerDispersion.setStatus("current")
_HpicfNtpAuthenticationKeyTable_Object = MibTable
hpicfNtpAuthenticationKeyTable = _HpicfNtpAuthenticationKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfNtpAuthenticationKeyTable.setStatus("current")
_HpicfNtpAuthenticationKeyEntry_Object = MibTableRow
hpicfNtpAuthenticationKeyEntry = _HpicfNtpAuthenticationKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 4, 1)
)
hpicfNtpAuthenticationKeyEntry.setIndexNames(
    (0, "HP-ICF-NTP-MIB", "hpicfNtpAuthenticationKeyId"),
)
if mibBuilder.loadTexts:
    hpicfNtpAuthenticationKeyEntry.setStatus("current")


class _HpicfNtpAuthenticationKeyId_Type(Unsigned32):
    """Custom type hpicfNtpAuthenticationKeyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpicfNtpAuthenticationKeyId_Type.__name__ = "Unsigned32"
_HpicfNtpAuthenticationKeyId_Object = MibTableColumn
hpicfNtpAuthenticationKeyId = _HpicfNtpAuthenticationKeyId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 4, 1, 1),
    _HpicfNtpAuthenticationKeyId_Type()
)
hpicfNtpAuthenticationKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfNtpAuthenticationKeyId.setStatus("current")


class _HpicfNtpAuthenticationKeyAuthMode_Type(Integer32):
    """Custom type hpicfNtpAuthenticationKeyAuthMode based on Integer32"""
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
        *(("md5", 2),
          ("none", 1),
          ("sha1", 3))
    )


_HpicfNtpAuthenticationKeyAuthMode_Type.__name__ = "Integer32"
_HpicfNtpAuthenticationKeyAuthMode_Object = MibTableColumn
hpicfNtpAuthenticationKeyAuthMode = _HpicfNtpAuthenticationKeyAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 4, 1, 2),
    _HpicfNtpAuthenticationKeyAuthMode_Type()
)
hpicfNtpAuthenticationKeyAuthMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfNtpAuthenticationKeyAuthMode.setStatus("current")


class _HpicfNtpAuthenticationKeyValue_Type(OctetString):
    """Custom type hpicfNtpAuthenticationKeyValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpicfNtpAuthenticationKeyValue_Type.__name__ = "OctetString"
_HpicfNtpAuthenticationKeyValue_Object = MibTableColumn
hpicfNtpAuthenticationKeyValue = _HpicfNtpAuthenticationKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 4, 1, 3),
    _HpicfNtpAuthenticationKeyValue_Type()
)
hpicfNtpAuthenticationKeyValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfNtpAuthenticationKeyValue.setStatus("current")


class _HpicfNtpAuthenticationKeyTrusted_Type(TruthValue):
    """Custom type hpicfNtpAuthenticationKeyTrusted based on TruthValue"""
    defaultValue = 2


_HpicfNtpAuthenticationKeyTrusted_Object = MibTableColumn
hpicfNtpAuthenticationKeyTrusted = _HpicfNtpAuthenticationKeyTrusted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 4, 1, 4),
    _HpicfNtpAuthenticationKeyTrusted_Type()
)
hpicfNtpAuthenticationKeyTrusted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfNtpAuthenticationKeyTrusted.setStatus("current")
_HpicfNtpAuthenticationKeyRowStatus_Type = RowStatus
_HpicfNtpAuthenticationKeyRowStatus_Object = MibTableColumn
hpicfNtpAuthenticationKeyRowStatus = _HpicfNtpAuthenticationKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 4, 1, 5),
    _HpicfNtpAuthenticationKeyRowStatus_Type()
)
hpicfNtpAuthenticationKeyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfNtpAuthenticationKeyRowStatus.setStatus("current")


class _HpicfNtpAuthenticationKeyEncrypted_Type(OctetString):
    """Custom type hpicfNtpAuthenticationKeyEncrypted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpicfNtpAuthenticationKeyEncrypted_Type.__name__ = "OctetString"
_HpicfNtpAuthenticationKeyEncrypted_Object = MibTableColumn
hpicfNtpAuthenticationKeyEncrypted = _HpicfNtpAuthenticationKeyEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 4, 1, 6),
    _HpicfNtpAuthenticationKeyEncrypted_Type()
)
hpicfNtpAuthenticationKeyEncrypted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfNtpAuthenticationKeyEncrypted.setStatus("current")
_HpicfNtpIpv6MulticastTable_Object = MibTable
hpicfNtpIpv6MulticastTable = _HpicfNtpIpv6MulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfNtpIpv6MulticastTable.setStatus("current")
_HpicfNtpIpv6MulticastEntry_Object = MibTableRow
hpicfNtpIpv6MulticastEntry = _HpicfNtpIpv6MulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 5, 1)
)
hpicfNtpIpv6MulticastEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfNtpIpv6MulticastEntry.setStatus("current")


class _HpicfNtpIpv6Multicast_Type(TruthValue):
    """Custom type hpicfNtpIpv6Multicast based on TruthValue"""


_HpicfNtpIpv6Multicast_Object = MibTableColumn
hpicfNtpIpv6Multicast = _HpicfNtpIpv6Multicast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 5, 1, 1),
    _HpicfNtpIpv6Multicast_Type()
)
hpicfNtpIpv6Multicast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfNtpIpv6Multicast.setStatus("current")
_HpicfNtpIpv6MulticastStatus_Type = RowStatus
_HpicfNtpIpv6MulticastStatus_Object = MibTableColumn
hpicfNtpIpv6MulticastStatus = _HpicfNtpIpv6MulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 5, 1, 2),
    _HpicfNtpIpv6MulticastStatus_Type()
)
hpicfNtpIpv6MulticastStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfNtpIpv6MulticastStatus.setStatus("current")
_HpicfNtpAssoSampleTable_Object = MibTable
hpicfNtpAssoSampleTable = _HpicfNtpAssoSampleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 7)
)
if mibBuilder.loadTexts:
    hpicfNtpAssoSampleTable.setStatus("current")
_HpicfNtpAssoSampleEntry_Object = MibTableRow
hpicfNtpAssoSampleEntry = _HpicfNtpAssoSampleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 7, 1)
)
hpicfNtpAssoSampleEntry.setIndexNames(
    (0, "HP-ICF-NTP-MIB", "hpicfNtpInetServerAddressType"),
    (0, "HP-ICF-NTP-MIB", "hpicfNtpInetServerAddress"),
    (0, "HP-ICF-NTP-MIB", "hpicfNtpAssoSampleId"),
)
if mibBuilder.loadTexts:
    hpicfNtpAssoSampleEntry.setStatus("current")
_HpicfNtpAssoSampleId_Type = Unsigned32
_HpicfNtpAssoSampleId_Object = MibTableColumn
hpicfNtpAssoSampleId = _HpicfNtpAssoSampleId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 7, 1, 1),
    _HpicfNtpAssoSampleId_Type()
)
hpicfNtpAssoSampleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfNtpAssoSampleId.setStatus("current")


class _HpicfNtpfiltDelaySample_Type(OctetString):
    """Custom type hpicfNtpfiltDelaySample based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_HpicfNtpfiltDelaySample_Type.__name__ = "OctetString"
_HpicfNtpfiltDelaySample_Object = MibTableColumn
hpicfNtpfiltDelaySample = _HpicfNtpfiltDelaySample_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 7, 1, 2),
    _HpicfNtpfiltDelaySample_Type()
)
hpicfNtpfiltDelaySample.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpfiltDelaySample.setStatus("current")


class _HpicfNtpfiltOffsetSample_Type(OctetString):
    """Custom type hpicfNtpfiltOffsetSample based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_HpicfNtpfiltOffsetSample_Type.__name__ = "OctetString"
_HpicfNtpfiltOffsetSample_Object = MibTableColumn
hpicfNtpfiltOffsetSample = _HpicfNtpfiltOffsetSample_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 7, 1, 3),
    _HpicfNtpfiltOffsetSample_Type()
)
hpicfNtpfiltOffsetSample.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpfiltOffsetSample.setStatus("current")
_HpicfNtpInetServerNameTable_Object = MibTable
hpicfNtpInetServerNameTable = _HpicfNtpInetServerNameTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8)
)
if mibBuilder.loadTexts:
    hpicfNtpInetServerNameTable.setStatus("current")
_HpicfNtpInetServerNameEntry_Object = MibTableRow
hpicfNtpInetServerNameEntry = _HpicfNtpInetServerNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8, 1)
)
hpicfNtpInetServerNameEntry.setIndexNames(
    (0, "HP-ICF-NTP-MIB", "hpicfNtpServerNameIndex"),
)
if mibBuilder.loadTexts:
    hpicfNtpInetServerNameEntry.setStatus("current")


class _HpicfNtpServerNameIndex_Type(Unsigned32):
    """Custom type hpicfNtpServerNameIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HpicfNtpServerNameIndex_Type.__name__ = "Unsigned32"
_HpicfNtpServerNameIndex_Object = MibTableColumn
hpicfNtpServerNameIndex = _HpicfNtpServerNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8, 1, 1),
    _HpicfNtpServerNameIndex_Type()
)
hpicfNtpServerNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfNtpServerNameIndex.setStatus("current")


class _HpicfNtpInetServerName_Type(DisplayString):
    """Custom type hpicfNtpInetServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpicfNtpInetServerName_Type.__name__ = "DisplayString"
_HpicfNtpInetServerName_Object = MibTableColumn
hpicfNtpInetServerName = _HpicfNtpInetServerName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8, 1, 2),
    _HpicfNtpInetServerName_Type()
)
hpicfNtpInetServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfNtpInetServerName.setStatus("current")
_HpicfNtpInetServerNameRowStatus_Type = RowStatus
_HpicfNtpInetServerNameRowStatus_Object = MibTableColumn
hpicfNtpInetServerNameRowStatus = _HpicfNtpInetServerNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8, 1, 3),
    _HpicfNtpInetServerNameRowStatus_Type()
)
hpicfNtpInetServerNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfNtpInetServerNameRowStatus.setStatus("current")
_HpicfNtpServerNameResolvAddType_Type = InetAddressType
_HpicfNtpServerNameResolvAddType_Object = MibTableColumn
hpicfNtpServerNameResolvAddType = _HpicfNtpServerNameResolvAddType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8, 1, 4),
    _HpicfNtpServerNameResolvAddType_Type()
)
hpicfNtpServerNameResolvAddType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpServerNameResolvAddType.setStatus("current")


class _HpicfNtpServerNameResolvAddress_Type(InetAddress):
    """Custom type hpicfNtpServerNameResolvAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_HpicfNtpServerNameResolvAddress_Type.__name__ = "InetAddress"
_HpicfNtpServerNameResolvAddress_Object = MibTableColumn
hpicfNtpServerNameResolvAddress = _HpicfNtpServerNameResolvAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8, 1, 5),
    _HpicfNtpServerNameResolvAddress_Type()
)
hpicfNtpServerNameResolvAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpServerNameResolvAddress.setStatus("current")


class _HpicfNtpServerNameResolveStatus_Type(Integer32):
    """Custom type hpicfNtpServerNameResolveStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("dnsfailed", 4),
          ("dnsnotresponding", 3),
          ("dnsunknownhost", 2),
          ("notactive", 5),
          ("notattempted", 0))
    )


_HpicfNtpServerNameResolveStatus_Type.__name__ = "Integer32"
_HpicfNtpServerNameResolveStatus_Object = MibTableColumn
hpicfNtpServerNameResolveStatus = _HpicfNtpServerNameResolveStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8, 1, 6),
    _HpicfNtpServerNameResolveStatus_Type()
)
hpicfNtpServerNameResolveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfNtpServerNameResolveStatus.setStatus("current")


class _HpicfNtpInetServerNameAuthKeyId_Type(Unsigned32):
    """Custom type hpicfNtpInetServerNameAuthKeyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpicfNtpInetServerNameAuthKeyId_Type.__name__ = "Unsigned32"
_HpicfNtpInetServerNameAuthKeyId_Object = MibTableColumn
hpicfNtpInetServerNameAuthKeyId = _HpicfNtpInetServerNameAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8, 1, 7),
    _HpicfNtpInetServerNameAuthKeyId_Type()
)
hpicfNtpInetServerNameAuthKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfNtpInetServerNameAuthKeyId.setStatus("current")


class _HpicfNtpConfigServerNamePollMinInterval_Type(Integer32):
    """Custom type hpicfNtpConfigServerNamePollMinInterval based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 17),
    )


_HpicfNtpConfigServerNamePollMinInterval_Type.__name__ = "Integer32"
_HpicfNtpConfigServerNamePollMinInterval_Object = MibTableColumn
hpicfNtpConfigServerNamePollMinInterval = _HpicfNtpConfigServerNamePollMinInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8, 1, 8),
    _HpicfNtpConfigServerNamePollMinInterval_Type()
)
hpicfNtpConfigServerNamePollMinInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfNtpConfigServerNamePollMinInterval.setStatus("current")


class _HpicfNtpConfigServerNamePollMaxInterval_Type(Integer32):
    """Custom type hpicfNtpConfigServerNamePollMaxInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 17),
    )


_HpicfNtpConfigServerNamePollMaxInterval_Type.__name__ = "Integer32"
_HpicfNtpConfigServerNamePollMaxInterval_Object = MibTableColumn
hpicfNtpConfigServerNamePollMaxInterval = _HpicfNtpConfigServerNamePollMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8, 1, 9),
    _HpicfNtpConfigServerNamePollMaxInterval_Type()
)
hpicfNtpConfigServerNamePollMaxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfNtpConfigServerNamePollMaxInterval.setStatus("current")


class _HpicfNtpServerNameAssoBurst_Type(Integer32):
    """Custom type hpicfNtpServerNameAssoBurst based on Integer32"""
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
        *(("burst", 2),
          ("iburst", 3),
          ("noburst", 1))
    )


_HpicfNtpServerNameAssoBurst_Type.__name__ = "Integer32"
_HpicfNtpServerNameAssoBurst_Object = MibTableColumn
hpicfNtpServerNameAssoBurst = _HpicfNtpServerNameAssoBurst_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8, 1, 10),
    _HpicfNtpServerNameAssoBurst_Type()
)
hpicfNtpServerNameAssoBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfNtpServerNameAssoBurst.setStatus("current")


class _HpicfNtpServerNameAssoIsOobm_Type(TruthValue):
    """Custom type hpicfNtpServerNameAssoIsOobm based on TruthValue"""


_HpicfNtpServerNameAssoIsOobm_Object = MibTableColumn
hpicfNtpServerNameAssoIsOobm = _HpicfNtpServerNameAssoIsOobm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8, 1, 11),
    _HpicfNtpServerNameAssoIsOobm_Type()
)
hpicfNtpServerNameAssoIsOobm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfNtpServerNameAssoIsOobm.setStatus("current")
_HpicfNtpGlobal_ObjectIdentity = ObjectIdentity
hpicfNtpGlobal = _HpicfNtpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 2)
)


class _HpicfNtpAdminStatus_Type(TruthValue):
    """Custom type hpicfNtpAdminStatus based on TruthValue"""


_HpicfNtpAdminStatus_Object = MibScalar
hpicfNtpAdminStatus = _HpicfNtpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 2, 1),
    _HpicfNtpAdminStatus_Type()
)
hpicfNtpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfNtpAdminStatus.setStatus("current")
_HpicfNtpConfigConformance_ObjectIdentity = ObjectIdentity
hpicfNtpConfigConformance = _HpicfNtpConfigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3)
)
_HpicfNtpConfigCompliances_ObjectIdentity = ObjectIdentity
hpicfNtpConfigCompliances = _HpicfNtpConfigCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3, 1)
)
_HpicfNtpConfigGroups_ObjectIdentity = ObjectIdentity
hpicfNtpConfigGroups = _HpicfNtpConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3, 2)
)

# Managed Objects groups

hpicfNtpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3, 2, 1)
)
hpicfNtpConfigGroup.setObjects(
      *(("HP-ICF-NTP-MIB", "hpicfNtpConfigMode"),
        ("HP-ICF-NTP-MIB", "hpicfNtpMaxAssociation"),
        ("HP-ICF-NTP-MIB", "hpicfNtpAdminStatus"),
        ("HP-ICF-NTP-MIB", "hpicfNtpStatusReferenceTimeFrac"),
        ("HP-ICF-NTP-MIB", "hpicfNtpStatusReferenceTimeSec"),
        ("HP-ICF-NTP-MIB", "hpicfNtpStatusClockOffset"),
        ("HP-ICF-NTP-MIB", "hpicfNtpStatusRootDelay"),
        ("HP-ICF-NTP-MIB", "hpicfNtpStatusRootDispersion"),
        ("HP-ICF-NTP-MIB", "hpicfNtpAssoDrift"))
)
if mibBuilder.loadTexts:
    hpicfNtpConfigGroup.setStatus("current")

hpicfNtpInetServerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3, 2, 2)
)
hpicfNtpInetServerConfigGroup.setObjects(
      *(("HP-ICF-NTP-MIB", "hpicfNtpInetServerRowStatus"),
        ("HP-ICF-NTP-MIB", "hpicfNtpInetServerAuthKeyId"),
        ("HP-ICF-NTP-MIB", "hpicfNtpConfigPollMinInterval"),
        ("HP-ICF-NTP-MIB", "hpicfNtpConfigPollMaxInterval"),
        ("HP-ICF-NTP-MIB", "hpicfNtpAssoOurPollInterval"),
        ("HP-ICF-NTP-MIB", "hpicfNtpAssoPeerPollInterval"),
        ("HP-ICF-NTP-MIB", "hpicfNtpAssoRootDelay"),
        ("HP-ICF-NTP-MIB", "hpicfNtpAssoRootDispersion"),
        ("HP-ICF-NTP-MIB", "hpicfNtpAssoPeerReach"),
        ("HP-ICF-NTP-MIB", "hpicfNtpAssoOriginTimeFrac"),
        ("HP-ICF-NTP-MIB", "hpicfNtpAssoOriginTimeSec"),
        ("HP-ICF-NTP-MIB", "hpicfNtpAssoRecvTimeFrac"),
        ("HP-ICF-NTP-MIB", "hpicfNtpAssoRecvTimeSec"),
        ("HP-ICF-NTP-MIB", "hpicfNtpAssoXmtTimeFrac"),
        ("HP-ICF-NTP-MIB", "hpicfNtpAssoXmtTimeSec"),
        ("HP-ICF-NTP-MIB", "hpicfNtpAssolastPollreq"),
        ("HP-ICF-NTP-MIB", "hpicfNtpAssoPrecision"),
        ("HP-ICF-NTP-MIB", "hpicfNtpAssoCurrentMode"),
        ("HP-ICF-NTP-MIB", "hpicfNtpAssoPeerDispersion"),
        ("HP-ICF-NTP-MIB", "hpicfNtpAssoBurst"),
        ("HP-ICF-NTP-MIB", "hpicfNtpAssoIsOobm"))
)
if mibBuilder.loadTexts:
    hpicfNtpInetServerConfigGroup.setStatus("current")

hpicfNtpAuthenticationKeyIdConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3, 2, 3)
)
hpicfNtpAuthenticationKeyIdConfigGroup.setObjects(
      *(("HP-ICF-NTP-MIB", "hpicfNtpAuthenticationKeyAuthMode"),
        ("HP-ICF-NTP-MIB", "hpicfNtpAuthenticationKeyValue"),
        ("HP-ICF-NTP-MIB", "hpicfNtpAuthenticationKeyEncrypted"),
        ("HP-ICF-NTP-MIB", "hpicfNtpAuthenticationKeyTrusted"),
        ("HP-ICF-NTP-MIB", "hpicfNtpAuthenticationKeyRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfNtpAuthenticationKeyIdConfigGroup.setStatus("current")

hpicfNtpAssociationSampleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3, 2, 4)
)
hpicfNtpAssociationSampleGroup.setObjects(
      *(("HP-ICF-NTP-MIB", "hpicfNtpfiltDelaySample"),
        ("HP-ICF-NTP-MIB", "hpicfNtpfiltOffsetSample"),
        ("HP-ICF-NTP-MIB", "hpicfNtpIpv6Multicast"),
        ("HP-ICF-NTP-MIB", "hpicfNtpIpv6MulticastStatus"))
)
if mibBuilder.loadTexts:
    hpicfNtpAssociationSampleGroup.setStatus("current")

hpicfNtpInetServerNameCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3, 2, 5)
)
hpicfNtpInetServerNameCfgGroup.setObjects(
      *(("HP-ICF-NTP-MIB", "hpicfNtpInetServerName"),
        ("HP-ICF-NTP-MIB", "hpicfNtpInetServerNameRowStatus"),
        ("HP-ICF-NTP-MIB", "hpicfNtpServerNameResolvAddType"),
        ("HP-ICF-NTP-MIB", "hpicfNtpServerNameResolvAddress"),
        ("HP-ICF-NTP-MIB", "hpicfNtpServerNameResolveStatus"),
        ("HP-ICF-NTP-MIB", "hpicfNtpInetServerNameAuthKeyId"),
        ("HP-ICF-NTP-MIB", "hpicfNtpConfigServerNamePollMinInterval"),
        ("HP-ICF-NTP-MIB", "hpicfNtpConfigServerNamePollMaxInterval"),
        ("HP-ICF-NTP-MIB", "hpicfNtpServerNameAssoBurst"),
        ("HP-ICF-NTP-MIB", "hpicfNtpServerNameAssoIsOobm"))
)
if mibBuilder.loadTexts:
    hpicfNtpInetServerNameCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfNtpInetConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfNtpInetConfigCompliance.setStatus(
        "current"
    )

hpicfNtpAuthenticationConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfNtpAuthenticationConfigCompliance.setStatus(
        "current"
    )

hpicfNtpServerConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfNtpServerConfigCompliance.setStatus(
        "current"
    )

hpicfNtpAssoSampleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfNtpAssoSampleCompliance.setStatus(
        "current"
    )

hpicfNtpServerNameCfgCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfNtpServerNameCfgCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-NTP-MIB",
    **{"hpicfNtpMIB": hpicfNtpMIB,
       "hpicfNtpConfig": hpicfNtpConfig,
       "hpicfNtpConfigScalars": hpicfNtpConfigScalars,
       "hpicfNtpConfigMode": hpicfNtpConfigMode,
       "hpicfNtpMaxAssociation": hpicfNtpMaxAssociation,
       "hpicfNtpStatusReferenceTimeFrac": hpicfNtpStatusReferenceTimeFrac,
       "hpicfNtpStatusReferenceTimeSec": hpicfNtpStatusReferenceTimeSec,
       "hpicfNtpStatusClockOffset": hpicfNtpStatusClockOffset,
       "hpicfNtpStatusRootDelay": hpicfNtpStatusRootDelay,
       "hpicfNtpStatusRootDispersion": hpicfNtpStatusRootDispersion,
       "hpicfNtpAssoDrift": hpicfNtpAssoDrift,
       "hpicfNtpInetConfigServerTable": hpicfNtpInetConfigServerTable,
       "hpicfNtpInetConfigServerEntry": hpicfNtpInetConfigServerEntry,
       "hpicfNtpInetServerAddressType": hpicfNtpInetServerAddressType,
       "hpicfNtpInetServerAddress": hpicfNtpInetServerAddress,
       "hpicfNtpInetServerRowStatus": hpicfNtpInetServerRowStatus,
       "hpicfNtpInetServerAuthKeyId": hpicfNtpInetServerAuthKeyId,
       "hpicfNtpConfigPollMinInterval": hpicfNtpConfigPollMinInterval,
       "hpicfNtpConfigPollMaxInterval": hpicfNtpConfigPollMaxInterval,
       "hpicfNtpAssoBurst": hpicfNtpAssoBurst,
       "hpicfNtpAssoIsOobm": hpicfNtpAssoIsOobm,
       "hpicfNtpInetServerInfoTable": hpicfNtpInetServerInfoTable,
       "hpicfNtpInetServerInfoEntry": hpicfNtpInetServerInfoEntry,
       "hpicfNtpAssoOurPollInterval": hpicfNtpAssoOurPollInterval,
       "hpicfNtpAssoPeerPollInterval": hpicfNtpAssoPeerPollInterval,
       "hpicfNtpAssoRootDelay": hpicfNtpAssoRootDelay,
       "hpicfNtpAssoRootDispersion": hpicfNtpAssoRootDispersion,
       "hpicfNtpAssoPeerReach": hpicfNtpAssoPeerReach,
       "hpicfNtpAssoOriginTimeFrac": hpicfNtpAssoOriginTimeFrac,
       "hpicfNtpAssoOriginTimeSec": hpicfNtpAssoOriginTimeSec,
       "hpicfNtpAssoRecvTimeFrac": hpicfNtpAssoRecvTimeFrac,
       "hpicfNtpAssoRecvTimeSec": hpicfNtpAssoRecvTimeSec,
       "hpicfNtpAssoXmtTimeFrac": hpicfNtpAssoXmtTimeFrac,
       "hpicfNtpAssoXmtTimeSec": hpicfNtpAssoXmtTimeSec,
       "hpicfNtpAssolastPollreq": hpicfNtpAssolastPollreq,
       "hpicfNtpAssoPrecision": hpicfNtpAssoPrecision,
       "hpicfNtpAssoCurrentMode": hpicfNtpAssoCurrentMode,
       "hpicfNtpAssoPeerDispersion": hpicfNtpAssoPeerDispersion,
       "hpicfNtpAuthenticationKeyTable": hpicfNtpAuthenticationKeyTable,
       "hpicfNtpAuthenticationKeyEntry": hpicfNtpAuthenticationKeyEntry,
       "hpicfNtpAuthenticationKeyId": hpicfNtpAuthenticationKeyId,
       "hpicfNtpAuthenticationKeyAuthMode": hpicfNtpAuthenticationKeyAuthMode,
       "hpicfNtpAuthenticationKeyValue": hpicfNtpAuthenticationKeyValue,
       "hpicfNtpAuthenticationKeyTrusted": hpicfNtpAuthenticationKeyTrusted,
       "hpicfNtpAuthenticationKeyRowStatus": hpicfNtpAuthenticationKeyRowStatus,
       "hpicfNtpAuthenticationKeyEncrypted": hpicfNtpAuthenticationKeyEncrypted,
       "hpicfNtpIpv6MulticastTable": hpicfNtpIpv6MulticastTable,
       "hpicfNtpIpv6MulticastEntry": hpicfNtpIpv6MulticastEntry,
       "hpicfNtpIpv6Multicast": hpicfNtpIpv6Multicast,
       "hpicfNtpIpv6MulticastStatus": hpicfNtpIpv6MulticastStatus,
       "hpicfNtpAssoSampleTable": hpicfNtpAssoSampleTable,
       "hpicfNtpAssoSampleEntry": hpicfNtpAssoSampleEntry,
       "hpicfNtpAssoSampleId": hpicfNtpAssoSampleId,
       "hpicfNtpfiltDelaySample": hpicfNtpfiltDelaySample,
       "hpicfNtpfiltOffsetSample": hpicfNtpfiltOffsetSample,
       "hpicfNtpInetServerNameTable": hpicfNtpInetServerNameTable,
       "hpicfNtpInetServerNameEntry": hpicfNtpInetServerNameEntry,
       "hpicfNtpServerNameIndex": hpicfNtpServerNameIndex,
       "hpicfNtpInetServerName": hpicfNtpInetServerName,
       "hpicfNtpInetServerNameRowStatus": hpicfNtpInetServerNameRowStatus,
       "hpicfNtpServerNameResolvAddType": hpicfNtpServerNameResolvAddType,
       "hpicfNtpServerNameResolvAddress": hpicfNtpServerNameResolvAddress,
       "hpicfNtpServerNameResolveStatus": hpicfNtpServerNameResolveStatus,
       "hpicfNtpInetServerNameAuthKeyId": hpicfNtpInetServerNameAuthKeyId,
       "hpicfNtpConfigServerNamePollMinInterval": hpicfNtpConfigServerNamePollMinInterval,
       "hpicfNtpConfigServerNamePollMaxInterval": hpicfNtpConfigServerNamePollMaxInterval,
       "hpicfNtpServerNameAssoBurst": hpicfNtpServerNameAssoBurst,
       "hpicfNtpServerNameAssoIsOobm": hpicfNtpServerNameAssoIsOobm,
       "hpicfNtpGlobal": hpicfNtpGlobal,
       "hpicfNtpAdminStatus": hpicfNtpAdminStatus,
       "hpicfNtpConfigConformance": hpicfNtpConfigConformance,
       "hpicfNtpConfigCompliances": hpicfNtpConfigCompliances,
       "hpicfNtpInetConfigCompliance": hpicfNtpInetConfigCompliance,
       "hpicfNtpAuthenticationConfigCompliance": hpicfNtpAuthenticationConfigCompliance,
       "hpicfNtpServerConfigCompliance": hpicfNtpServerConfigCompliance,
       "hpicfNtpAssoSampleCompliance": hpicfNtpAssoSampleCompliance,
       "hpicfNtpServerNameCfgCompliance": hpicfNtpServerNameCfgCompliance,
       "hpicfNtpConfigGroups": hpicfNtpConfigGroups,
       "hpicfNtpConfigGroup": hpicfNtpConfigGroup,
       "hpicfNtpInetServerConfigGroup": hpicfNtpInetServerConfigGroup,
       "hpicfNtpAuthenticationKeyIdConfigGroup": hpicfNtpAuthenticationKeyIdConfigGroup,
       "hpicfNtpAssociationSampleGroup": hpicfNtpAssociationSampleGroup,
       "hpicfNtpInetServerNameCfgGroup": hpicfNtpInetServerNameCfgGroup}
)
