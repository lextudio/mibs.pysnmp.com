# SNMP MIB module (CABH-SEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CABH-SEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:11 2024
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

(clabProjCableHome,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjCableHome")

(X509Certificate,) = mibBuilder.importSymbols(
    "DOCS-BPI2-MIB",
    "X509Certificate")

(docsDevFilterIpEntry,) = mibBuilder.importSymbols(
    "DOCS-CABLE-DEVICE-MIB",
    "docsDevFilterIpEntry")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetPortNumber")

(ZeroBasedCounter32,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "ZeroBasedCounter32")

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
 iso,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "zeroDotZero")

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

cabhSecMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CabhSecFwObjects_ObjectIdentity = ObjectIdentity
cabhSecFwObjects = _CabhSecFwObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 1)
)
_CabhSecFwBase_ObjectIdentity = ObjectIdentity
cabhSecFwBase = _CabhSecFwBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 1, 1)
)


class _CabhSecFwPolicyFileEnable_Type(Integer32):
    """Custom type cabhSecFwPolicyFileEnable based on Integer32"""
    defaultValue = 1

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


_CabhSecFwPolicyFileEnable_Type.__name__ = "Integer32"
_CabhSecFwPolicyFileEnable_Object = MibScalar
cabhSecFwPolicyFileEnable = _CabhSecFwPolicyFileEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 1, 1, 1),
    _CabhSecFwPolicyFileEnable_Type()
)
cabhSecFwPolicyFileEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhSecFwPolicyFileEnable.setStatus("deprecated")
_CabhSecFwPolicyFileURL_Type = SnmpAdminString
_CabhSecFwPolicyFileURL_Object = MibScalar
cabhSecFwPolicyFileURL = _CabhSecFwPolicyFileURL_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 1, 1, 2),
    _CabhSecFwPolicyFileURL_Type()
)
cabhSecFwPolicyFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhSecFwPolicyFileURL.setStatus("deprecated")


class _CabhSecFwPolicyFileHash_Type(OctetString):
    """Custom type cabhSecFwPolicyFileHash based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(20, 20),
    )


_CabhSecFwPolicyFileHash_Type.__name__ = "OctetString"
_CabhSecFwPolicyFileHash_Object = MibScalar
cabhSecFwPolicyFileHash = _CabhSecFwPolicyFileHash_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 1, 1, 3),
    _CabhSecFwPolicyFileHash_Type()
)
cabhSecFwPolicyFileHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhSecFwPolicyFileHash.setStatus("deprecated")


class _CabhSecFwPolicyFileOperStatus_Type(Integer32):
    """Custom type cabhSecFwPolicyFileOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("complete", 2),
          ("failed", 4),
          ("inProgress", 1))
    )


_CabhSecFwPolicyFileOperStatus_Type.__name__ = "Integer32"
_CabhSecFwPolicyFileOperStatus_Object = MibScalar
cabhSecFwPolicyFileOperStatus = _CabhSecFwPolicyFileOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 1, 1, 4),
    _CabhSecFwPolicyFileOperStatus_Type()
)
cabhSecFwPolicyFileOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSecFwPolicyFileOperStatus.setStatus("deprecated")
_CabhSecFwPolicyFileCurrentVersion_Type = SnmpAdminString
_CabhSecFwPolicyFileCurrentVersion_Object = MibScalar
cabhSecFwPolicyFileCurrentVersion = _CabhSecFwPolicyFileCurrentVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 1, 1, 5),
    _CabhSecFwPolicyFileCurrentVersion_Type()
)
cabhSecFwPolicyFileCurrentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSecFwPolicyFileCurrentVersion.setStatus("deprecated")
_CabhSecFwPolicySuccessfulFileURL_Type = SnmpAdminString
_CabhSecFwPolicySuccessfulFileURL_Object = MibScalar
cabhSecFwPolicySuccessfulFileURL = _CabhSecFwPolicySuccessfulFileURL_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 1, 1, 6),
    _CabhSecFwPolicySuccessfulFileURL_Type()
)
cabhSecFwPolicySuccessfulFileURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSecFwPolicySuccessfulFileURL.setStatus("deprecated")
_CabhSecFwLogCtl_ObjectIdentity = ObjectIdentity
cabhSecFwLogCtl = _CabhSecFwLogCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 1, 2)
)


class _CabhSecFwEventType1Enable_Type(Integer32):
    """Custom type cabhSecFwEventType1Enable based on Integer32"""
    defaultValue = 2

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


_CabhSecFwEventType1Enable_Type.__name__ = "Integer32"
_CabhSecFwEventType1Enable_Object = MibScalar
cabhSecFwEventType1Enable = _CabhSecFwEventType1Enable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 1, 2, 1),
    _CabhSecFwEventType1Enable_Type()
)
cabhSecFwEventType1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhSecFwEventType1Enable.setStatus("deprecated")


class _CabhSecFwEventType2Enable_Type(Integer32):
    """Custom type cabhSecFwEventType2Enable based on Integer32"""
    defaultValue = 2

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


_CabhSecFwEventType2Enable_Type.__name__ = "Integer32"
_CabhSecFwEventType2Enable_Object = MibScalar
cabhSecFwEventType2Enable = _CabhSecFwEventType2Enable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 1, 2, 2),
    _CabhSecFwEventType2Enable_Type()
)
cabhSecFwEventType2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhSecFwEventType2Enable.setStatus("deprecated")


class _CabhSecFwEventType3Enable_Type(Integer32):
    """Custom type cabhSecFwEventType3Enable based on Integer32"""
    defaultValue = 2

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


_CabhSecFwEventType3Enable_Type.__name__ = "Integer32"
_CabhSecFwEventType3Enable_Object = MibScalar
cabhSecFwEventType3Enable = _CabhSecFwEventType3Enable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 1, 2, 3),
    _CabhSecFwEventType3Enable_Type()
)
cabhSecFwEventType3Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhSecFwEventType3Enable.setStatus("deprecated")


class _CabhSecFwEventAttackAlertThreshold_Type(Integer32):
    """Custom type cabhSecFwEventAttackAlertThreshold based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CabhSecFwEventAttackAlertThreshold_Type.__name__ = "Integer32"
_CabhSecFwEventAttackAlertThreshold_Object = MibScalar
cabhSecFwEventAttackAlertThreshold = _CabhSecFwEventAttackAlertThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 1, 2, 4),
    _CabhSecFwEventAttackAlertThreshold_Type()
)
cabhSecFwEventAttackAlertThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhSecFwEventAttackAlertThreshold.setStatus("deprecated")


class _CabhSecFwEventAttackAlertPeriod_Type(Integer32):
    """Custom type cabhSecFwEventAttackAlertPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CabhSecFwEventAttackAlertPeriod_Type.__name__ = "Integer32"
_CabhSecFwEventAttackAlertPeriod_Object = MibScalar
cabhSecFwEventAttackAlertPeriod = _CabhSecFwEventAttackAlertPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 1, 2, 5),
    _CabhSecFwEventAttackAlertPeriod_Type()
)
cabhSecFwEventAttackAlertPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhSecFwEventAttackAlertPeriod.setStatus("deprecated")
_CabhSecCertObjects_ObjectIdentity = ObjectIdentity
cabhSecCertObjects = _CabhSecCertObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 2)
)
_CabhSecCertPsCert_Type = X509Certificate
_CabhSecCertPsCert_Object = MibScalar
cabhSecCertPsCert = _CabhSecCertPsCert_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 2, 1),
    _CabhSecCertPsCert_Type()
)
cabhSecCertPsCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSecCertPsCert.setStatus("current")
_CabhSecNotification_ObjectIdentity = ObjectIdentity
cabhSecNotification = _CabhSecNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 3)
)
_CabhSecConformance_ObjectIdentity = ObjectIdentity
cabhSecConformance = _CabhSecConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 4)
)
_CabhSecCompliances_ObjectIdentity = ObjectIdentity
cabhSecCompliances = _CabhSecCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 4, 1)
)
_CabhSecGroups_ObjectIdentity = ObjectIdentity
cabhSecGroups = _CabhSecGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 4, 2)
)
_CabhSecMibObjects_ObjectIdentity = ObjectIdentity
cabhSecMibObjects = _CabhSecMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5)
)
_CabhSecKerbObjects_ObjectIdentity = ObjectIdentity
cabhSecKerbObjects = _CabhSecKerbObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 3)
)
_CabhSecKerbBase_ObjectIdentity = ObjectIdentity
cabhSecKerbBase = _CabhSecKerbBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 3, 1)
)


class _CabhSecKerbPKINITGracePeriod_Type(Unsigned32):
    """Custom type cabhSecKerbPKINITGracePeriod based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 600),
    )


_CabhSecKerbPKINITGracePeriod_Type.__name__ = "Unsigned32"
_CabhSecKerbPKINITGracePeriod_Object = MibScalar
cabhSecKerbPKINITGracePeriod = _CabhSecKerbPKINITGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 3, 1, 1),
    _CabhSecKerbPKINITGracePeriod_Type()
)
cabhSecKerbPKINITGracePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhSecKerbPKINITGracePeriod.setStatus("current")
if mibBuilder.loadTexts:
    cabhSecKerbPKINITGracePeriod.setUnits("minutes")


class _CabhSecKerbTGSGracePeriod_Type(Unsigned32):
    """Custom type cabhSecKerbTGSGracePeriod based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_CabhSecKerbTGSGracePeriod_Type.__name__ = "Unsigned32"
_CabhSecKerbTGSGracePeriod_Object = MibScalar
cabhSecKerbTGSGracePeriod = _CabhSecKerbTGSGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 3, 1, 2),
    _CabhSecKerbTGSGracePeriod_Type()
)
cabhSecKerbTGSGracePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhSecKerbTGSGracePeriod.setStatus("current")
if mibBuilder.loadTexts:
    cabhSecKerbTGSGracePeriod.setUnits("minutes")


class _CabhSecKerbUnsolicitedKeyMaxTimeout_Type(Unsigned32):
    """Custom type cabhSecKerbUnsolicitedKeyMaxTimeout based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 600),
    )


_CabhSecKerbUnsolicitedKeyMaxTimeout_Type.__name__ = "Unsigned32"
_CabhSecKerbUnsolicitedKeyMaxTimeout_Object = MibScalar
cabhSecKerbUnsolicitedKeyMaxTimeout = _CabhSecKerbUnsolicitedKeyMaxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 3, 1, 3),
    _CabhSecKerbUnsolicitedKeyMaxTimeout_Type()
)
cabhSecKerbUnsolicitedKeyMaxTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhSecKerbUnsolicitedKeyMaxTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cabhSecKerbUnsolicitedKeyMaxTimeout.setUnits("seconds")


class _CabhSecKerbUnsolicitedKeyMaxRetries_Type(Unsigned32):
    """Custom type cabhSecKerbUnsolicitedKeyMaxRetries based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CabhSecKerbUnsolicitedKeyMaxRetries_Type.__name__ = "Unsigned32"
_CabhSecKerbUnsolicitedKeyMaxRetries_Object = MibScalar
cabhSecKerbUnsolicitedKeyMaxRetries = _CabhSecKerbUnsolicitedKeyMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 3, 1, 4),
    _CabhSecKerbUnsolicitedKeyMaxRetries_Type()
)
cabhSecKerbUnsolicitedKeyMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhSecKerbUnsolicitedKeyMaxRetries.setStatus("current")
_CabhSec2FwObjects_ObjectIdentity = ObjectIdentity
cabhSec2FwObjects = _CabhSec2FwObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4)
)
_CabhSec2FwBase_ObjectIdentity = ObjectIdentity
cabhSec2FwBase = _CabhSec2FwBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 1)
)


class _CabhSec2FwEnable_Type(Integer32):
    """Custom type cabhSec2FwEnable based on Integer32"""
    defaultValue = 1

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


_CabhSec2FwEnable_Type.__name__ = "Integer32"
_CabhSec2FwEnable_Object = MibScalar
cabhSec2FwEnable = _CabhSec2FwEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 1, 1),
    _CabhSec2FwEnable_Type()
)
cabhSec2FwEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhSec2FwEnable.setStatus("current")
_CabhSec2FwPolicyFileURL_Type = SnmpAdminString
_CabhSec2FwPolicyFileURL_Object = MibScalar
cabhSec2FwPolicyFileURL = _CabhSec2FwPolicyFileURL_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 1, 2),
    _CabhSec2FwPolicyFileURL_Type()
)
cabhSec2FwPolicyFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhSec2FwPolicyFileURL.setStatus("current")


class _CabhSec2FwPolicyFileHash_Type(OctetString):
    """Custom type cabhSec2FwPolicyFileHash based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(20, 20),
    )


_CabhSec2FwPolicyFileHash_Type.__name__ = "OctetString"
_CabhSec2FwPolicyFileHash_Object = MibScalar
cabhSec2FwPolicyFileHash = _CabhSec2FwPolicyFileHash_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 1, 3),
    _CabhSec2FwPolicyFileHash_Type()
)
cabhSec2FwPolicyFileHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhSec2FwPolicyFileHash.setStatus("current")


class _CabhSec2FwPolicyFileOperStatus_Type(Integer32):
    """Custom type cabhSec2FwPolicyFileOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("complete", 2),
          ("failed", 3),
          ("inProgress", 1))
    )


_CabhSec2FwPolicyFileOperStatus_Type.__name__ = "Integer32"
_CabhSec2FwPolicyFileOperStatus_Object = MibScalar
cabhSec2FwPolicyFileOperStatus = _CabhSec2FwPolicyFileOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 1, 4),
    _CabhSec2FwPolicyFileOperStatus_Type()
)
cabhSec2FwPolicyFileOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwPolicyFileOperStatus.setStatus("current")
_CabhSec2FwPolicyFileCurrentVersion_Type = SnmpAdminString
_CabhSec2FwPolicyFileCurrentVersion_Object = MibScalar
cabhSec2FwPolicyFileCurrentVersion = _CabhSec2FwPolicyFileCurrentVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 1, 5),
    _CabhSec2FwPolicyFileCurrentVersion_Type()
)
cabhSec2FwPolicyFileCurrentVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhSec2FwPolicyFileCurrentVersion.setStatus("current")


class _CabhSec2FwClearPreviousRuleset_Type(TruthValue):
    """Custom type cabhSec2FwClearPreviousRuleset based on TruthValue"""


_CabhSec2FwClearPreviousRuleset_Object = MibScalar
cabhSec2FwClearPreviousRuleset = _CabhSec2FwClearPreviousRuleset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 1, 6),
    _CabhSec2FwClearPreviousRuleset_Type()
)
cabhSec2FwClearPreviousRuleset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhSec2FwClearPreviousRuleset.setStatus("current")


class _CabhSec2FwPolicySelection_Type(Integer32):
    """Custom type cabhSec2FwPolicySelection based on Integer32"""
    defaultValue = 1

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
        *(("configuredRulesetBoth", 2),
          ("configuredRulesetCabhSec2FwLocalFilterIpTable", 5),
          ("configuredRulesetDocsDevFilterIpTable", 4),
          ("factoryDefault", 1),
          ("factoryDefaultAndCabhSec2FwLocalFilterIpTable", 7),
          ("factoryDefaultAndConfiguredRulesetBoth", 3),
          ("factoryDefaultAndDocsDevFilterIpTable", 6))
    )


_CabhSec2FwPolicySelection_Type.__name__ = "Integer32"
_CabhSec2FwPolicySelection_Object = MibScalar
cabhSec2FwPolicySelection = _CabhSec2FwPolicySelection_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 1, 7),
    _CabhSec2FwPolicySelection_Type()
)
cabhSec2FwPolicySelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhSec2FwPolicySelection.setStatus("current")


class _CabhSec2FwEventSetToFactory_Type(TruthValue):
    """Custom type cabhSec2FwEventSetToFactory based on TruthValue"""


_CabhSec2FwEventSetToFactory_Object = MibScalar
cabhSec2FwEventSetToFactory = _CabhSec2FwEventSetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 1, 8),
    _CabhSec2FwEventSetToFactory_Type()
)
cabhSec2FwEventSetToFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhSec2FwEventSetToFactory.setStatus("current")
_CabhSec2FwEventLastSetToFactory_Type = TimeStamp
_CabhSec2FwEventLastSetToFactory_Object = MibScalar
cabhSec2FwEventLastSetToFactory = _CabhSec2FwEventLastSetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 1, 9),
    _CabhSec2FwEventLastSetToFactory_Type()
)
cabhSec2FwEventLastSetToFactory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwEventLastSetToFactory.setStatus("current")
_CabhSec2FwPolicySuccessfulFileURL_Type = SnmpAdminString
_CabhSec2FwPolicySuccessfulFileURL_Object = MibScalar
cabhSec2FwPolicySuccessfulFileURL = _CabhSec2FwPolicySuccessfulFileURL_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 1, 10),
    _CabhSec2FwPolicySuccessfulFileURL_Type()
)
cabhSec2FwPolicySuccessfulFileURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwPolicySuccessfulFileURL.setStatus("current")


class _CabhSec2FwConfiguredRulesetPriority_Type(Integer32):
    """Custom type cabhSec2FwConfiguredRulesetPriority based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cabhSec2FwLocalFilterIpTable", 2),
          ("docsDevFilterIpTable", 1))
    )


_CabhSec2FwConfiguredRulesetPriority_Type.__name__ = "Integer32"
_CabhSec2FwConfiguredRulesetPriority_Object = MibScalar
cabhSec2FwConfiguredRulesetPriority = _CabhSec2FwConfiguredRulesetPriority_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 1, 11),
    _CabhSec2FwConfiguredRulesetPriority_Type()
)
cabhSec2FwConfiguredRulesetPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhSec2FwConfiguredRulesetPriority.setStatus("current")


class _CabhSec2FwClearLocalRuleset_Type(TruthValue):
    """Custom type cabhSec2FwClearLocalRuleset based on TruthValue"""


_CabhSec2FwClearLocalRuleset_Object = MibScalar
cabhSec2FwClearLocalRuleset = _CabhSec2FwClearLocalRuleset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 1, 12),
    _CabhSec2FwClearLocalRuleset_Type()
)
cabhSec2FwClearLocalRuleset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhSec2FwClearLocalRuleset.setStatus("current")
_CabhSec2FwEvent_ObjectIdentity = ObjectIdentity
cabhSec2FwEvent = _CabhSec2FwEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 2)
)
_CabhSec2FwEventControlTable_Object = MibTable
cabhSec2FwEventControlTable = _CabhSec2FwEventControlTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 2, 1)
)
if mibBuilder.loadTexts:
    cabhSec2FwEventControlTable.setStatus("current")
_CabhSec2FwEventControlEntry_Object = MibTableRow
cabhSec2FwEventControlEntry = _CabhSec2FwEventControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 2, 1, 1)
)
cabhSec2FwEventControlEntry.setIndexNames(
    (0, "CABH-SEC-MIB", "cabhSec2FwEventType"),
)
if mibBuilder.loadTexts:
    cabhSec2FwEventControlEntry.setStatus("current")


class _CabhSec2FwEventType_Type(Integer32):
    """Custom type cabhSec2FwEventType based on Integer32"""
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
        *(("type1", 1),
          ("type2", 2),
          ("type3", 3),
          ("type4", 4),
          ("type5", 5),
          ("type6", 6))
    )


_CabhSec2FwEventType_Type.__name__ = "Integer32"
_CabhSec2FwEventType_Object = MibTableColumn
cabhSec2FwEventType = _CabhSec2FwEventType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 2, 1, 1, 1),
    _CabhSec2FwEventType_Type()
)
cabhSec2FwEventType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cabhSec2FwEventType.setStatus("current")


class _CabhSec2FwEventEnable_Type(Integer32):
    """Custom type cabhSec2FwEventEnable based on Integer32"""
    defaultValue = 2

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


_CabhSec2FwEventEnable_Type.__name__ = "Integer32"
_CabhSec2FwEventEnable_Object = MibTableColumn
cabhSec2FwEventEnable = _CabhSec2FwEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 2, 1, 1, 2),
    _CabhSec2FwEventEnable_Type()
)
cabhSec2FwEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhSec2FwEventEnable.setStatus("current")


class _CabhSec2FwEventThreshold_Type(Unsigned32):
    """Custom type cabhSec2FwEventThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CabhSec2FwEventThreshold_Type.__name__ = "Unsigned32"
_CabhSec2FwEventThreshold_Object = MibTableColumn
cabhSec2FwEventThreshold = _CabhSec2FwEventThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 2, 1, 1, 3),
    _CabhSec2FwEventThreshold_Type()
)
cabhSec2FwEventThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhSec2FwEventThreshold.setStatus("current")


class _CabhSec2FwEventInterval_Type(Unsigned32):
    """Custom type cabhSec2FwEventInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 744),
    )


_CabhSec2FwEventInterval_Type.__name__ = "Unsigned32"
_CabhSec2FwEventInterval_Object = MibTableColumn
cabhSec2FwEventInterval = _CabhSec2FwEventInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 2, 1, 1, 4),
    _CabhSec2FwEventInterval_Type()
)
cabhSec2FwEventInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhSec2FwEventInterval.setStatus("current")
if mibBuilder.loadTexts:
    cabhSec2FwEventInterval.setUnits("hours")
_CabhSec2FwEventCount_Type = ZeroBasedCounter32
_CabhSec2FwEventCount_Object = MibTableColumn
cabhSec2FwEventCount = _CabhSec2FwEventCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 2, 1, 1, 5),
    _CabhSec2FwEventCount_Type()
)
cabhSec2FwEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwEventCount.setStatus("current")


class _CabhSec2FwEventLogReset_Type(TruthValue):
    """Custom type cabhSec2FwEventLogReset based on TruthValue"""


_CabhSec2FwEventLogReset_Object = MibTableColumn
cabhSec2FwEventLogReset = _CabhSec2FwEventLogReset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 2, 1, 1, 6),
    _CabhSec2FwEventLogReset_Type()
)
cabhSec2FwEventLogReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhSec2FwEventLogReset.setStatus("current")
_CabhSec2FwEventLogLastReset_Type = TimeStamp
_CabhSec2FwEventLogLastReset_Object = MibTableColumn
cabhSec2FwEventLogLastReset = _CabhSec2FwEventLogLastReset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 2, 1, 1, 7),
    _CabhSec2FwEventLogLastReset_Type()
)
cabhSec2FwEventLogLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwEventLogLastReset.setStatus("current")
_CabhSec2FwLog_ObjectIdentity = ObjectIdentity
cabhSec2FwLog = _CabhSec2FwLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 3)
)
_CabhSec2FwLogTable_Object = MibTable
cabhSec2FwLogTable = _CabhSec2FwLogTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 3, 1)
)
if mibBuilder.loadTexts:
    cabhSec2FwLogTable.setStatus("current")
_CabhSec2FwLogEntry_Object = MibTableRow
cabhSec2FwLogEntry = _CabhSec2FwLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 3, 1, 1)
)
cabhSec2FwLogEntry.setIndexNames(
    (0, "CABH-SEC-MIB", "cabhSec2FwLogIndex"),
)
if mibBuilder.loadTexts:
    cabhSec2FwLogEntry.setStatus("current")


class _CabhSec2FwLogIndex_Type(Unsigned32):
    """Custom type cabhSec2FwLogIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CabhSec2FwLogIndex_Type.__name__ = "Unsigned32"
_CabhSec2FwLogIndex_Object = MibTableColumn
cabhSec2FwLogIndex = _CabhSec2FwLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 3, 1, 1, 1),
    _CabhSec2FwLogIndex_Type()
)
cabhSec2FwLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cabhSec2FwLogIndex.setStatus("current")


class _CabhSec2FwLogEventType_Type(Integer32):
    """Custom type cabhSec2FwLogEventType based on Integer32"""
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
        *(("type1", 1),
          ("type2", 2),
          ("type3", 3),
          ("type4", 4),
          ("type5", 5),
          ("type6", 6))
    )


_CabhSec2FwLogEventType_Type.__name__ = "Integer32"
_CabhSec2FwLogEventType_Object = MibTableColumn
cabhSec2FwLogEventType = _CabhSec2FwLogEventType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 3, 1, 1, 2),
    _CabhSec2FwLogEventType_Type()
)
cabhSec2FwLogEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwLogEventType.setStatus("current")


class _CabhSec2FwLogEventPriority_Type(Integer32):
    """Custom type cabhSec2FwLogEventPriority based on Integer32"""
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
        *(("alert", 2),
          ("critical", 3),
          ("debug", 8),
          ("emergency", 1),
          ("error", 4),
          ("information", 7),
          ("notice", 6),
          ("warning", 5))
    )


_CabhSec2FwLogEventPriority_Type.__name__ = "Integer32"
_CabhSec2FwLogEventPriority_Object = MibTableColumn
cabhSec2FwLogEventPriority = _CabhSec2FwLogEventPriority_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 3, 1, 1, 3),
    _CabhSec2FwLogEventPriority_Type()
)
cabhSec2FwLogEventPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwLogEventPriority.setStatus("current")
_CabhSec2FwLogEventId_Type = Unsigned32
_CabhSec2FwLogEventId_Object = MibTableColumn
cabhSec2FwLogEventId = _CabhSec2FwLogEventId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 3, 1, 1, 4),
    _CabhSec2FwLogEventId_Type()
)
cabhSec2FwLogEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwLogEventId.setStatus("current")
_CabhSec2FwLogTime_Type = DateAndTime
_CabhSec2FwLogTime_Object = MibTableColumn
cabhSec2FwLogTime = _CabhSec2FwLogTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 3, 1, 1, 5),
    _CabhSec2FwLogTime_Type()
)
cabhSec2FwLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwLogTime.setStatus("current")


class _CabhSec2FwLogIpProtocol_Type(Unsigned32):
    """Custom type cabhSec2FwLogIpProtocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_CabhSec2FwLogIpProtocol_Type.__name__ = "Unsigned32"
_CabhSec2FwLogIpProtocol_Object = MibTableColumn
cabhSec2FwLogIpProtocol = _CabhSec2FwLogIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 3, 1, 1, 6),
    _CabhSec2FwLogIpProtocol_Type()
)
cabhSec2FwLogIpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwLogIpProtocol.setStatus("current")
_CabhSec2FwLogIpSourceAddr_Type = InetAddress
_CabhSec2FwLogIpSourceAddr_Object = MibTableColumn
cabhSec2FwLogIpSourceAddr = _CabhSec2FwLogIpSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 3, 1, 1, 7),
    _CabhSec2FwLogIpSourceAddr_Type()
)
cabhSec2FwLogIpSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwLogIpSourceAddr.setStatus("current")
_CabhSec2FwLogIpDestAddr_Type = InetAddress
_CabhSec2FwLogIpDestAddr_Object = MibTableColumn
cabhSec2FwLogIpDestAddr = _CabhSec2FwLogIpDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 3, 1, 1, 8),
    _CabhSec2FwLogIpDestAddr_Type()
)
cabhSec2FwLogIpDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwLogIpDestAddr.setStatus("current")
_CabhSec2FwLogIpSourcePort_Type = InetPortNumber
_CabhSec2FwLogIpSourcePort_Object = MibTableColumn
cabhSec2FwLogIpSourcePort = _CabhSec2FwLogIpSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 3, 1, 1, 9),
    _CabhSec2FwLogIpSourcePort_Type()
)
cabhSec2FwLogIpSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwLogIpSourcePort.setStatus("current")
_CabhSec2FwLogIpDestPort_Type = InetPortNumber
_CabhSec2FwLogIpDestPort_Object = MibTableColumn
cabhSec2FwLogIpDestPort = _CabhSec2FwLogIpDestPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 3, 1, 1, 10),
    _CabhSec2FwLogIpDestPort_Type()
)
cabhSec2FwLogIpDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwLogIpDestPort.setStatus("current")
_CabhSec2FwLogMessageType_Type = Unsigned32
_CabhSec2FwLogMessageType_Object = MibTableColumn
cabhSec2FwLogMessageType = _CabhSec2FwLogMessageType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 3, 1, 1, 11),
    _CabhSec2FwLogMessageType_Type()
)
cabhSec2FwLogMessageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwLogMessageType.setStatus("current")


class _CabhSec2FwLogReplayCount_Type(Unsigned32):
    """Custom type cabhSec2FwLogReplayCount based on Unsigned32"""
    defaultValue = 0


_CabhSec2FwLogReplayCount_Object = MibTableColumn
cabhSec2FwLogReplayCount = _CabhSec2FwLogReplayCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 3, 1, 1, 12),
    _CabhSec2FwLogReplayCount_Type()
)
cabhSec2FwLogReplayCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwLogReplayCount.setStatus("current")


class _CabhSec2FwLogMIBPointer_Type(VariablePointer):
    """Custom type cabhSec2FwLogMIBPointer based on VariablePointer"""
    defaultValue = (0, 0)


_CabhSec2FwLogMIBPointer_Object = MibTableColumn
cabhSec2FwLogMIBPointer = _CabhSec2FwLogMIBPointer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 3, 1, 1, 13),
    _CabhSec2FwLogMIBPointer_Type()
)
cabhSec2FwLogMIBPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwLogMIBPointer.setStatus("current")


class _CabhSec2FwLogMatchingFilterTableName_Type(Integer32):
    """Custom type cabhSec2FwLogMatchingFilterTableName based on Integer32"""
    defaultValue = 4

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
        *(("cabhSec2FwFactoryDefaultFilterTable", 1),
          ("cabhSec2FwLocalFilterIpTable", 3),
          ("docsDevFilterIpTable", 2),
          ("none", 4))
    )


_CabhSec2FwLogMatchingFilterTableName_Type.__name__ = "Integer32"
_CabhSec2FwLogMatchingFilterTableName_Object = MibTableColumn
cabhSec2FwLogMatchingFilterTableName = _CabhSec2FwLogMatchingFilterTableName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 3, 1, 1, 14),
    _CabhSec2FwLogMatchingFilterTableName_Type()
)
cabhSec2FwLogMatchingFilterTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwLogMatchingFilterTableName.setStatus("current")


class _CabhSec2FwLogMatchingFilterTableIndex_Type(Unsigned32):
    """Custom type cabhSec2FwLogMatchingFilterTableIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CabhSec2FwLogMatchingFilterTableIndex_Type.__name__ = "Unsigned32"
_CabhSec2FwLogMatchingFilterTableIndex_Object = MibTableColumn
cabhSec2FwLogMatchingFilterTableIndex = _CabhSec2FwLogMatchingFilterTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 3, 1, 1, 15),
    _CabhSec2FwLogMatchingFilterTableIndex_Type()
)
cabhSec2FwLogMatchingFilterTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwLogMatchingFilterTableIndex.setStatus("current")


class _CabhSec2FwLogMatchingFilterDescr_Type(SnmpAdminString):
    """Custom type cabhSec2FwLogMatchingFilterDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhSec2FwLogMatchingFilterDescr_Type.__name__ = "SnmpAdminString"
_CabhSec2FwLogMatchingFilterDescr_Object = MibTableColumn
cabhSec2FwLogMatchingFilterDescr = _CabhSec2FwLogMatchingFilterDescr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 3, 1, 1, 16),
    _CabhSec2FwLogMatchingFilterDescr_Type()
)
cabhSec2FwLogMatchingFilterDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwLogMatchingFilterDescr.setStatus("current")
_CabhSec2FwFilter_ObjectIdentity = ObjectIdentity
cabhSec2FwFilter = _CabhSec2FwFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4)
)
_CabhSec2FwFilterScheduleTable_Object = MibTable
cabhSec2FwFilterScheduleTable = _CabhSec2FwFilterScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 1)
)
if mibBuilder.loadTexts:
    cabhSec2FwFilterScheduleTable.setStatus("current")
_CabhSec2FwFilterScheduleEntry_Object = MibTableRow
cabhSec2FwFilterScheduleEntry = _CabhSec2FwFilterScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cabhSec2FwFilterScheduleEntry.setStatus("current")


class _CabhSec2FwFilterScheduleStartTime_Type(Unsigned32):
    """Custom type cabhSec2FwFilterScheduleStartTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2359),
    )


_CabhSec2FwFilterScheduleStartTime_Type.__name__ = "Unsigned32"
_CabhSec2FwFilterScheduleStartTime_Object = MibTableColumn
cabhSec2FwFilterScheduleStartTime = _CabhSec2FwFilterScheduleStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 1, 1, 1),
    _CabhSec2FwFilterScheduleStartTime_Type()
)
cabhSec2FwFilterScheduleStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhSec2FwFilterScheduleStartTime.setStatus("current")


class _CabhSec2FwFilterScheduleEndTime_Type(Unsigned32):
    """Custom type cabhSec2FwFilterScheduleEndTime based on Unsigned32"""
    defaultValue = 2359

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2359),
    )


_CabhSec2FwFilterScheduleEndTime_Type.__name__ = "Unsigned32"
_CabhSec2FwFilterScheduleEndTime_Object = MibTableColumn
cabhSec2FwFilterScheduleEndTime = _CabhSec2FwFilterScheduleEndTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 1, 1, 2),
    _CabhSec2FwFilterScheduleEndTime_Type()
)
cabhSec2FwFilterScheduleEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhSec2FwFilterScheduleEndTime.setStatus("current")


class _CabhSec2FwFilterScheduleDOW_Type(Bits):
    """Custom type cabhSec2FwFilterScheduleDOW based on Bits"""
    defaultHexValue = "fe"

    namedValues = NamedValues(
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 0),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )

_CabhSec2FwFilterScheduleDOW_Type.__name__ = "Bits"
_CabhSec2FwFilterScheduleDOW_Object = MibTableColumn
cabhSec2FwFilterScheduleDOW = _CabhSec2FwFilterScheduleDOW_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 1, 1, 3),
    _CabhSec2FwFilterScheduleDOW_Type()
)
cabhSec2FwFilterScheduleDOW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhSec2FwFilterScheduleDOW.setStatus("current")


class _CabhSec2FwFilterScheduleDescr_Type(SnmpAdminString):
    """Custom type cabhSec2FwFilterScheduleDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhSec2FwFilterScheduleDescr_Type.__name__ = "SnmpAdminString"
_CabhSec2FwFilterScheduleDescr_Object = MibTableColumn
cabhSec2FwFilterScheduleDescr = _CabhSec2FwFilterScheduleDescr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 1, 1, 4),
    _CabhSec2FwFilterScheduleDescr_Type()
)
cabhSec2FwFilterScheduleDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhSec2FwFilterScheduleDescr.setStatus("current")
_CabhSec2FwFactoryDefaultFilterTable_Object = MibTable
cabhSec2FwFactoryDefaultFilterTable = _CabhSec2FwFactoryDefaultFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 2)
)
if mibBuilder.loadTexts:
    cabhSec2FwFactoryDefaultFilterTable.setStatus("current")
_CabhSec2FwFactoryDefaultFilterEntry_Object = MibTableRow
cabhSec2FwFactoryDefaultFilterEntry = _CabhSec2FwFactoryDefaultFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 2, 1)
)
cabhSec2FwFactoryDefaultFilterEntry.setIndexNames(
    (0, "CABH-SEC-MIB", "cabhSec2FwFactoryDefaultFilterIndex"),
)
if mibBuilder.loadTexts:
    cabhSec2FwFactoryDefaultFilterEntry.setStatus("current")


class _CabhSec2FwFactoryDefaultFilterIndex_Type(Unsigned32):
    """Custom type cabhSec2FwFactoryDefaultFilterIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CabhSec2FwFactoryDefaultFilterIndex_Type.__name__ = "Unsigned32"
_CabhSec2FwFactoryDefaultFilterIndex_Object = MibTableColumn
cabhSec2FwFactoryDefaultFilterIndex = _CabhSec2FwFactoryDefaultFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 2, 1, 1),
    _CabhSec2FwFactoryDefaultFilterIndex_Type()
)
cabhSec2FwFactoryDefaultFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cabhSec2FwFactoryDefaultFilterIndex.setStatus("current")


class _CabhSec2FwFactoryDefaultFilterControl_Type(Integer32):
    """Custom type cabhSec2FwFactoryDefaultFilterControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 2),
          ("deny", 1))
    )


_CabhSec2FwFactoryDefaultFilterControl_Type.__name__ = "Integer32"
_CabhSec2FwFactoryDefaultFilterControl_Object = MibTableColumn
cabhSec2FwFactoryDefaultFilterControl = _CabhSec2FwFactoryDefaultFilterControl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 2, 1, 2),
    _CabhSec2FwFactoryDefaultFilterControl_Type()
)
cabhSec2FwFactoryDefaultFilterControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwFactoryDefaultFilterControl.setStatus("current")
_CabhSec2FwFactoryDefaultFilterIfIndex_Type = InterfaceIndexOrZero
_CabhSec2FwFactoryDefaultFilterIfIndex_Object = MibTableColumn
cabhSec2FwFactoryDefaultFilterIfIndex = _CabhSec2FwFactoryDefaultFilterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 2, 1, 3),
    _CabhSec2FwFactoryDefaultFilterIfIndex_Type()
)
cabhSec2FwFactoryDefaultFilterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwFactoryDefaultFilterIfIndex.setStatus("current")


class _CabhSec2FwFactoryDefaultFilterDirection_Type(Integer32):
    """Custom type cabhSec2FwFactoryDefaultFilterDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("inbound", 1),
          ("outbound", 2))
    )


_CabhSec2FwFactoryDefaultFilterDirection_Type.__name__ = "Integer32"
_CabhSec2FwFactoryDefaultFilterDirection_Object = MibTableColumn
cabhSec2FwFactoryDefaultFilterDirection = _CabhSec2FwFactoryDefaultFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 2, 1, 4),
    _CabhSec2FwFactoryDefaultFilterDirection_Type()
)
cabhSec2FwFactoryDefaultFilterDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwFactoryDefaultFilterDirection.setStatus("current")


class _CabhSec2FwFactoryDefaultFilterSaddr_Type(InetAddress):
    """Custom type cabhSec2FwFactoryDefaultFilterSaddr based on InetAddress"""
    defaultHexValue = "00000000"


_CabhSec2FwFactoryDefaultFilterSaddr_Object = MibTableColumn
cabhSec2FwFactoryDefaultFilterSaddr = _CabhSec2FwFactoryDefaultFilterSaddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 2, 1, 5),
    _CabhSec2FwFactoryDefaultFilterSaddr_Type()
)
cabhSec2FwFactoryDefaultFilterSaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwFactoryDefaultFilterSaddr.setStatus("current")


class _CabhSec2FwFactoryDefaultFilterSmask_Type(InetAddress):
    """Custom type cabhSec2FwFactoryDefaultFilterSmask based on InetAddress"""
    defaultHexValue = "00000000"


_CabhSec2FwFactoryDefaultFilterSmask_Object = MibTableColumn
cabhSec2FwFactoryDefaultFilterSmask = _CabhSec2FwFactoryDefaultFilterSmask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 2, 1, 6),
    _CabhSec2FwFactoryDefaultFilterSmask_Type()
)
cabhSec2FwFactoryDefaultFilterSmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwFactoryDefaultFilterSmask.setStatus("current")


class _CabhSec2FwFactoryDefaultFilterDaddr_Type(InetAddress):
    """Custom type cabhSec2FwFactoryDefaultFilterDaddr based on InetAddress"""
    defaultHexValue = "00000000"


_CabhSec2FwFactoryDefaultFilterDaddr_Object = MibTableColumn
cabhSec2FwFactoryDefaultFilterDaddr = _CabhSec2FwFactoryDefaultFilterDaddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 2, 1, 7),
    _CabhSec2FwFactoryDefaultFilterDaddr_Type()
)
cabhSec2FwFactoryDefaultFilterDaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwFactoryDefaultFilterDaddr.setStatus("current")


class _CabhSec2FwFactoryDefaultFilterDmask_Type(InetAddress):
    """Custom type cabhSec2FwFactoryDefaultFilterDmask based on InetAddress"""
    defaultHexValue = "00000000"


_CabhSec2FwFactoryDefaultFilterDmask_Object = MibTableColumn
cabhSec2FwFactoryDefaultFilterDmask = _CabhSec2FwFactoryDefaultFilterDmask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 2, 1, 8),
    _CabhSec2FwFactoryDefaultFilterDmask_Type()
)
cabhSec2FwFactoryDefaultFilterDmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwFactoryDefaultFilterDmask.setStatus("current")


class _CabhSec2FwFactoryDefaultFilterProtocol_Type(Unsigned32):
    """Custom type cabhSec2FwFactoryDefaultFilterProtocol based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CabhSec2FwFactoryDefaultFilterProtocol_Type.__name__ = "Unsigned32"
_CabhSec2FwFactoryDefaultFilterProtocol_Object = MibTableColumn
cabhSec2FwFactoryDefaultFilterProtocol = _CabhSec2FwFactoryDefaultFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 2, 1, 9),
    _CabhSec2FwFactoryDefaultFilterProtocol_Type()
)
cabhSec2FwFactoryDefaultFilterProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwFactoryDefaultFilterProtocol.setStatus("current")


class _CabhSec2FwFactoryDefaultFilterSourcePortLow_Type(Unsigned32):
    """Custom type cabhSec2FwFactoryDefaultFilterSourcePortLow based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CabhSec2FwFactoryDefaultFilterSourcePortLow_Type.__name__ = "Unsigned32"
_CabhSec2FwFactoryDefaultFilterSourcePortLow_Object = MibTableColumn
cabhSec2FwFactoryDefaultFilterSourcePortLow = _CabhSec2FwFactoryDefaultFilterSourcePortLow_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 2, 1, 10),
    _CabhSec2FwFactoryDefaultFilterSourcePortLow_Type()
)
cabhSec2FwFactoryDefaultFilterSourcePortLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwFactoryDefaultFilterSourcePortLow.setStatus("current")


class _CabhSec2FwFactoryDefaultFilterSourcePortHigh_Type(Unsigned32):
    """Custom type cabhSec2FwFactoryDefaultFilterSourcePortHigh based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CabhSec2FwFactoryDefaultFilterSourcePortHigh_Type.__name__ = "Unsigned32"
_CabhSec2FwFactoryDefaultFilterSourcePortHigh_Object = MibTableColumn
cabhSec2FwFactoryDefaultFilterSourcePortHigh = _CabhSec2FwFactoryDefaultFilterSourcePortHigh_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 2, 1, 11),
    _CabhSec2FwFactoryDefaultFilterSourcePortHigh_Type()
)
cabhSec2FwFactoryDefaultFilterSourcePortHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwFactoryDefaultFilterSourcePortHigh.setStatus("current")


class _CabhSec2FwFactoryDefaultFilterDestPortLow_Type(Unsigned32):
    """Custom type cabhSec2FwFactoryDefaultFilterDestPortLow based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CabhSec2FwFactoryDefaultFilterDestPortLow_Type.__name__ = "Unsigned32"
_CabhSec2FwFactoryDefaultFilterDestPortLow_Object = MibTableColumn
cabhSec2FwFactoryDefaultFilterDestPortLow = _CabhSec2FwFactoryDefaultFilterDestPortLow_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 2, 1, 12),
    _CabhSec2FwFactoryDefaultFilterDestPortLow_Type()
)
cabhSec2FwFactoryDefaultFilterDestPortLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwFactoryDefaultFilterDestPortLow.setStatus("current")


class _CabhSec2FwFactoryDefaultFilterDestPortHigh_Type(Unsigned32):
    """Custom type cabhSec2FwFactoryDefaultFilterDestPortHigh based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CabhSec2FwFactoryDefaultFilterDestPortHigh_Type.__name__ = "Unsigned32"
_CabhSec2FwFactoryDefaultFilterDestPortHigh_Object = MibTableColumn
cabhSec2FwFactoryDefaultFilterDestPortHigh = _CabhSec2FwFactoryDefaultFilterDestPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 2, 1, 13),
    _CabhSec2FwFactoryDefaultFilterDestPortHigh_Type()
)
cabhSec2FwFactoryDefaultFilterDestPortHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwFactoryDefaultFilterDestPortHigh.setStatus("current")


class _CabhSec2FwFactoryDefaultFilterContinue_Type(TruthValue):
    """Custom type cabhSec2FwFactoryDefaultFilterContinue based on TruthValue"""


_CabhSec2FwFactoryDefaultFilterContinue_Object = MibTableColumn
cabhSec2FwFactoryDefaultFilterContinue = _CabhSec2FwFactoryDefaultFilterContinue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 2, 1, 14),
    _CabhSec2FwFactoryDefaultFilterContinue_Type()
)
cabhSec2FwFactoryDefaultFilterContinue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwFactoryDefaultFilterContinue.setStatus("current")
_CabhSec2FwLocalFilterIpTable_Object = MibTable
cabhSec2FwLocalFilterIpTable = _CabhSec2FwLocalFilterIpTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 3)
)
if mibBuilder.loadTexts:
    cabhSec2FwLocalFilterIpTable.setStatus("current")
_CabhSec2FwLocalFilterIpEntry_Object = MibTableRow
cabhSec2FwLocalFilterIpEntry = _CabhSec2FwLocalFilterIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 3, 1)
)
cabhSec2FwLocalFilterIpEntry.setIndexNames(
    (0, "CABH-SEC-MIB", "cabhSec2FwLocalFilterIpIndex"),
)
if mibBuilder.loadTexts:
    cabhSec2FwLocalFilterIpEntry.setStatus("current")


class _CabhSec2FwLocalFilterIpIndex_Type(Unsigned32):
    """Custom type cabhSec2FwLocalFilterIpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CabhSec2FwLocalFilterIpIndex_Type.__name__ = "Unsigned32"
_CabhSec2FwLocalFilterIpIndex_Object = MibTableColumn
cabhSec2FwLocalFilterIpIndex = _CabhSec2FwLocalFilterIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 3, 1, 1),
    _CabhSec2FwLocalFilterIpIndex_Type()
)
cabhSec2FwLocalFilterIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cabhSec2FwLocalFilterIpIndex.setStatus("current")
_CabhSec2FwLocalFilterIpStatus_Type = RowStatus
_CabhSec2FwLocalFilterIpStatus_Object = MibTableColumn
cabhSec2FwLocalFilterIpStatus = _CabhSec2FwLocalFilterIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 3, 1, 2),
    _CabhSec2FwLocalFilterIpStatus_Type()
)
cabhSec2FwLocalFilterIpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhSec2FwLocalFilterIpStatus.setStatus("current")


class _CabhSec2FwLocalFilterIpControl_Type(Integer32):
    """Custom type cabhSec2FwLocalFilterIpControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 2),
          ("deny", 1))
    )


_CabhSec2FwLocalFilterIpControl_Type.__name__ = "Integer32"
_CabhSec2FwLocalFilterIpControl_Object = MibTableColumn
cabhSec2FwLocalFilterIpControl = _CabhSec2FwLocalFilterIpControl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 3, 1, 3),
    _CabhSec2FwLocalFilterIpControl_Type()
)
cabhSec2FwLocalFilterIpControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhSec2FwLocalFilterIpControl.setStatus("current")


class _CabhSec2FwLocalFilterIpIfIndex_Type(InterfaceIndexOrZero):
    """Custom type cabhSec2FwLocalFilterIpIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 255


_CabhSec2FwLocalFilterIpIfIndex_Object = MibTableColumn
cabhSec2FwLocalFilterIpIfIndex = _CabhSec2FwLocalFilterIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 3, 1, 4),
    _CabhSec2FwLocalFilterIpIfIndex_Type()
)
cabhSec2FwLocalFilterIpIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhSec2FwLocalFilterIpIfIndex.setStatus("current")


class _CabhSec2FwLocalFilterIpDirection_Type(Integer32):
    """Custom type cabhSec2FwLocalFilterIpDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("inbound", 1),
          ("outbound", 2))
    )


_CabhSec2FwLocalFilterIpDirection_Type.__name__ = "Integer32"
_CabhSec2FwLocalFilterIpDirection_Object = MibTableColumn
cabhSec2FwLocalFilterIpDirection = _CabhSec2FwLocalFilterIpDirection_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 3, 1, 5),
    _CabhSec2FwLocalFilterIpDirection_Type()
)
cabhSec2FwLocalFilterIpDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhSec2FwLocalFilterIpDirection.setStatus("current")


class _CabhSec2FwLocalFilterIpSaddr_Type(InetAddress):
    """Custom type cabhSec2FwLocalFilterIpSaddr based on InetAddress"""
    defaultHexValue = "00000000"


_CabhSec2FwLocalFilterIpSaddr_Object = MibTableColumn
cabhSec2FwLocalFilterIpSaddr = _CabhSec2FwLocalFilterIpSaddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 3, 1, 6),
    _CabhSec2FwLocalFilterIpSaddr_Type()
)
cabhSec2FwLocalFilterIpSaddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhSec2FwLocalFilterIpSaddr.setStatus("current")


class _CabhSec2FwLocalFilterIpSmask_Type(InetAddress):
    """Custom type cabhSec2FwLocalFilterIpSmask based on InetAddress"""
    defaultHexValue = "00000000"


_CabhSec2FwLocalFilterIpSmask_Object = MibTableColumn
cabhSec2FwLocalFilterIpSmask = _CabhSec2FwLocalFilterIpSmask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 3, 1, 7),
    _CabhSec2FwLocalFilterIpSmask_Type()
)
cabhSec2FwLocalFilterIpSmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhSec2FwLocalFilterIpSmask.setStatus("current")


class _CabhSec2FwLocalFilterIpDaddr_Type(InetAddress):
    """Custom type cabhSec2FwLocalFilterIpDaddr based on InetAddress"""
    defaultHexValue = "00000000"


_CabhSec2FwLocalFilterIpDaddr_Object = MibTableColumn
cabhSec2FwLocalFilterIpDaddr = _CabhSec2FwLocalFilterIpDaddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 3, 1, 8),
    _CabhSec2FwLocalFilterIpDaddr_Type()
)
cabhSec2FwLocalFilterIpDaddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhSec2FwLocalFilterIpDaddr.setStatus("current")


class _CabhSec2FwLocalFilterIpDmask_Type(InetAddress):
    """Custom type cabhSec2FwLocalFilterIpDmask based on InetAddress"""
    defaultHexValue = "00000000"


_CabhSec2FwLocalFilterIpDmask_Object = MibTableColumn
cabhSec2FwLocalFilterIpDmask = _CabhSec2FwLocalFilterIpDmask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 3, 1, 9),
    _CabhSec2FwLocalFilterIpDmask_Type()
)
cabhSec2FwLocalFilterIpDmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhSec2FwLocalFilterIpDmask.setStatus("current")


class _CabhSec2FwLocalFilterIpProtocol_Type(Unsigned32):
    """Custom type cabhSec2FwLocalFilterIpProtocol based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CabhSec2FwLocalFilterIpProtocol_Type.__name__ = "Unsigned32"
_CabhSec2FwLocalFilterIpProtocol_Object = MibTableColumn
cabhSec2FwLocalFilterIpProtocol = _CabhSec2FwLocalFilterIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 3, 1, 10),
    _CabhSec2FwLocalFilterIpProtocol_Type()
)
cabhSec2FwLocalFilterIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhSec2FwLocalFilterIpProtocol.setStatus("current")


class _CabhSec2FwLocalFilterIpSourcePortLow_Type(Unsigned32):
    """Custom type cabhSec2FwLocalFilterIpSourcePortLow based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CabhSec2FwLocalFilterIpSourcePortLow_Type.__name__ = "Unsigned32"
_CabhSec2FwLocalFilterIpSourcePortLow_Object = MibTableColumn
cabhSec2FwLocalFilterIpSourcePortLow = _CabhSec2FwLocalFilterIpSourcePortLow_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 3, 1, 11),
    _CabhSec2FwLocalFilterIpSourcePortLow_Type()
)
cabhSec2FwLocalFilterIpSourcePortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhSec2FwLocalFilterIpSourcePortLow.setStatus("current")


class _CabhSec2FwLocalFilterIpSourcePortHigh_Type(Unsigned32):
    """Custom type cabhSec2FwLocalFilterIpSourcePortHigh based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CabhSec2FwLocalFilterIpSourcePortHigh_Type.__name__ = "Unsigned32"
_CabhSec2FwLocalFilterIpSourcePortHigh_Object = MibTableColumn
cabhSec2FwLocalFilterIpSourcePortHigh = _CabhSec2FwLocalFilterIpSourcePortHigh_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 3, 1, 12),
    _CabhSec2FwLocalFilterIpSourcePortHigh_Type()
)
cabhSec2FwLocalFilterIpSourcePortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhSec2FwLocalFilterIpSourcePortHigh.setStatus("current")


class _CabhSec2FwLocalFilterIpDestPortLow_Type(Unsigned32):
    """Custom type cabhSec2FwLocalFilterIpDestPortLow based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CabhSec2FwLocalFilterIpDestPortLow_Type.__name__ = "Unsigned32"
_CabhSec2FwLocalFilterIpDestPortLow_Object = MibTableColumn
cabhSec2FwLocalFilterIpDestPortLow = _CabhSec2FwLocalFilterIpDestPortLow_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 3, 1, 13),
    _CabhSec2FwLocalFilterIpDestPortLow_Type()
)
cabhSec2FwLocalFilterIpDestPortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhSec2FwLocalFilterIpDestPortLow.setStatus("current")


class _CabhSec2FwLocalFilterIpDestPortHigh_Type(Unsigned32):
    """Custom type cabhSec2FwLocalFilterIpDestPortHigh based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CabhSec2FwLocalFilterIpDestPortHigh_Type.__name__ = "Unsigned32"
_CabhSec2FwLocalFilterIpDestPortHigh_Object = MibTableColumn
cabhSec2FwLocalFilterIpDestPortHigh = _CabhSec2FwLocalFilterIpDestPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 3, 1, 14),
    _CabhSec2FwLocalFilterIpDestPortHigh_Type()
)
cabhSec2FwLocalFilterIpDestPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhSec2FwLocalFilterIpDestPortHigh.setStatus("current")
_CabhSec2FwLocalFilterIpMatches_Type = Counter32
_CabhSec2FwLocalFilterIpMatches_Object = MibTableColumn
cabhSec2FwLocalFilterIpMatches = _CabhSec2FwLocalFilterIpMatches_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 3, 1, 15),
    _CabhSec2FwLocalFilterIpMatches_Type()
)
cabhSec2FwLocalFilterIpMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwLocalFilterIpMatches.setStatus("current")


class _CabhSec2FwLocalFilterIpContinue_Type(TruthValue):
    """Custom type cabhSec2FwLocalFilterIpContinue based on TruthValue"""


_CabhSec2FwLocalFilterIpContinue_Object = MibTableColumn
cabhSec2FwLocalFilterIpContinue = _CabhSec2FwLocalFilterIpContinue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 3, 1, 16),
    _CabhSec2FwLocalFilterIpContinue_Type()
)
cabhSec2FwLocalFilterIpContinue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhSec2FwLocalFilterIpContinue.setStatus("current")


class _CabhSec2FwLocalFilterIpStartTime_Type(Unsigned32):
    """Custom type cabhSec2FwLocalFilterIpStartTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2359),
    )


_CabhSec2FwLocalFilterIpStartTime_Type.__name__ = "Unsigned32"
_CabhSec2FwLocalFilterIpStartTime_Object = MibTableColumn
cabhSec2FwLocalFilterIpStartTime = _CabhSec2FwLocalFilterIpStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 3, 1, 17),
    _CabhSec2FwLocalFilterIpStartTime_Type()
)
cabhSec2FwLocalFilterIpStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhSec2FwLocalFilterIpStartTime.setStatus("current")


class _CabhSec2FwLocalFilterIpEndTime_Type(Unsigned32):
    """Custom type cabhSec2FwLocalFilterIpEndTime based on Unsigned32"""
    defaultValue = 2359

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2359),
    )


_CabhSec2FwLocalFilterIpEndTime_Type.__name__ = "Unsigned32"
_CabhSec2FwLocalFilterIpEndTime_Object = MibTableColumn
cabhSec2FwLocalFilterIpEndTime = _CabhSec2FwLocalFilterIpEndTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 3, 1, 18),
    _CabhSec2FwLocalFilterIpEndTime_Type()
)
cabhSec2FwLocalFilterIpEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhSec2FwLocalFilterIpEndTime.setStatus("current")


class _CabhSec2FwLocalFilterIpDOW_Type(Bits):
    """Custom type cabhSec2FwLocalFilterIpDOW based on Bits"""
    defaultHexValue = "fe"

    namedValues = NamedValues(
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 0),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )

_CabhSec2FwLocalFilterIpDOW_Type.__name__ = "Bits"
_CabhSec2FwLocalFilterIpDOW_Object = MibTableColumn
cabhSec2FwLocalFilterIpDOW = _CabhSec2FwLocalFilterIpDOW_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 3, 1, 19),
    _CabhSec2FwLocalFilterIpDOW_Type()
)
cabhSec2FwLocalFilterIpDOW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhSec2FwLocalFilterIpDOW.setStatus("current")


class _CabhSec2FwLocalFilterIpDescr_Type(SnmpAdminString):
    """Custom type cabhSec2FwLocalFilterIpDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhSec2FwLocalFilterIpDescr_Type.__name__ = "SnmpAdminString"
_CabhSec2FwLocalFilterIpDescr_Object = MibTableColumn
cabhSec2FwLocalFilterIpDescr = _CabhSec2FwLocalFilterIpDescr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 5, 4, 4, 3, 1, 20),
    _CabhSec2FwLocalFilterIpDescr_Type()
)
cabhSec2FwLocalFilterIpDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhSec2FwLocalFilterIpDescr.setStatus("current")
docsDevFilterIpEntry.registerAugmentions(
    ("CABH-SEC-MIB",
     "cabhSec2FwFilterScheduleEntry")
)
cabhSec2FwFilterScheduleEntry.setIndexNames(*docsDevFilterIpEntry.getIndexNames())

# Managed Objects groups

cabhSecGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 4, 2, 1)
)
cabhSecGroup.setObjects(
      *(("CABH-SEC-MIB", "cabhSecFwPolicyFileEnable"),
        ("CABH-SEC-MIB", "cabhSecFwPolicyFileURL"),
        ("CABH-SEC-MIB", "cabhSecFwPolicyFileHash"),
        ("CABH-SEC-MIB", "cabhSecFwPolicyFileOperStatus"),
        ("CABH-SEC-MIB", "cabhSecFwPolicyFileCurrentVersion"),
        ("CABH-SEC-MIB", "cabhSecFwPolicySuccessfulFileURL"),
        ("CABH-SEC-MIB", "cabhSecFwEventType1Enable"),
        ("CABH-SEC-MIB", "cabhSecFwEventType2Enable"),
        ("CABH-SEC-MIB", "cabhSecFwEventType3Enable"),
        ("CABH-SEC-MIB", "cabhSecFwEventAttackAlertThreshold"),
        ("CABH-SEC-MIB", "cabhSecFwEventAttackAlertPeriod"))
)
if mibBuilder.loadTexts:
    cabhSecGroup.setStatus("deprecated")

cabhSecCertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 4, 2, 2)
)
cabhSecCertGroup.setObjects(
    ("CABH-SEC-MIB", "cabhSecCertPsCert")
)
if mibBuilder.loadTexts:
    cabhSecCertGroup.setStatus("current")

cabhSecKerbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 4, 2, 3)
)
cabhSecKerbGroup.setObjects(
      *(("CABH-SEC-MIB", "cabhSecKerbPKINITGracePeriod"),
        ("CABH-SEC-MIB", "cabhSecKerbTGSGracePeriod"),
        ("CABH-SEC-MIB", "cabhSecKerbUnsolicitedKeyMaxTimeout"),
        ("CABH-SEC-MIB", "cabhSecKerbUnsolicitedKeyMaxRetries"))
)
if mibBuilder.loadTexts:
    cabhSecKerbGroup.setStatus("current")

cabhSec2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 4, 2, 4)
)
cabhSec2Group.setObjects(
      *(("CABH-SEC-MIB", "cabhSec2FwEnable"),
        ("CABH-SEC-MIB", "cabhSec2FwPolicyFileURL"),
        ("CABH-SEC-MIB", "cabhSec2FwPolicyFileHash"),
        ("CABH-SEC-MIB", "cabhSec2FwPolicyFileOperStatus"),
        ("CABH-SEC-MIB", "cabhSec2FwPolicyFileCurrentVersion"),
        ("CABH-SEC-MIB", "cabhSec2FwClearPreviousRuleset"),
        ("CABH-SEC-MIB", "cabhSec2FwPolicySelection"),
        ("CABH-SEC-MIB", "cabhSec2FwEventSetToFactory"),
        ("CABH-SEC-MIB", "cabhSec2FwEventLastSetToFactory"),
        ("CABH-SEC-MIB", "cabhSec2FwPolicySuccessfulFileURL"),
        ("CABH-SEC-MIB", "cabhSec2FwEventEnable"),
        ("CABH-SEC-MIB", "cabhSec2FwEventThreshold"),
        ("CABH-SEC-MIB", "cabhSec2FwEventInterval"),
        ("CABH-SEC-MIB", "cabhSec2FwEventCount"),
        ("CABH-SEC-MIB", "cabhSec2FwEventLogReset"),
        ("CABH-SEC-MIB", "cabhSec2FwEventLogLastReset"),
        ("CABH-SEC-MIB", "cabhSec2FwLogEventType"),
        ("CABH-SEC-MIB", "cabhSec2FwLogEventPriority"),
        ("CABH-SEC-MIB", "cabhSec2FwLogEventId"),
        ("CABH-SEC-MIB", "cabhSec2FwLogTime"),
        ("CABH-SEC-MIB", "cabhSec2FwLogIpProtocol"),
        ("CABH-SEC-MIB", "cabhSec2FwLogIpSourceAddr"),
        ("CABH-SEC-MIB", "cabhSec2FwLogIpDestAddr"),
        ("CABH-SEC-MIB", "cabhSec2FwLogIpSourcePort"),
        ("CABH-SEC-MIB", "cabhSec2FwLogIpDestPort"),
        ("CABH-SEC-MIB", "cabhSec2FwLogMessageType"),
        ("CABH-SEC-MIB", "cabhSec2FwLogReplayCount"),
        ("CABH-SEC-MIB", "cabhSec2FwLogMIBPointer"),
        ("CABH-SEC-MIB", "cabhSec2FwFilterScheduleStartTime"),
        ("CABH-SEC-MIB", "cabhSec2FwFilterScheduleEndTime"),
        ("CABH-SEC-MIB", "cabhSec2FwFilterScheduleDOW"),
        ("CABH-SEC-MIB", "cabhSec2FwFactoryDefaultFilterControl"),
        ("CABH-SEC-MIB", "cabhSec2FwFactoryDefaultFilterIfIndex"),
        ("CABH-SEC-MIB", "cabhSec2FwFactoryDefaultFilterDirection"),
        ("CABH-SEC-MIB", "cabhSec2FwFactoryDefaultFilterSaddr"),
        ("CABH-SEC-MIB", "cabhSec2FwFactoryDefaultFilterSmask"),
        ("CABH-SEC-MIB", "cabhSec2FwFactoryDefaultFilterDaddr"),
        ("CABH-SEC-MIB", "cabhSec2FwFactoryDefaultFilterDmask"),
        ("CABH-SEC-MIB", "cabhSec2FwFactoryDefaultFilterProtocol"),
        ("CABH-SEC-MIB", "cabhSec2FwFactoryDefaultFilterSourcePortLow"),
        ("CABH-SEC-MIB", "cabhSec2FwFactoryDefaultFilterSourcePortHigh"),
        ("CABH-SEC-MIB", "cabhSec2FwFactoryDefaultFilterDestPortLow"),
        ("CABH-SEC-MIB", "cabhSec2FwFactoryDefaultFilterDestPortHigh"),
        ("CABH-SEC-MIB", "cabhSec2FwFactoryDefaultFilterContinue"))
)
if mibBuilder.loadTexts:
    cabhSec2Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cabhSecCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cabhSecCompliance.setStatus(
        "deprecated"
    )

cabhSec2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    cabhSec2Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CABH-SEC-MIB",
    **{"cabhSecMib": cabhSecMib,
       "cabhSecFwObjects": cabhSecFwObjects,
       "cabhSecFwBase": cabhSecFwBase,
       "cabhSecFwPolicyFileEnable": cabhSecFwPolicyFileEnable,
       "cabhSecFwPolicyFileURL": cabhSecFwPolicyFileURL,
       "cabhSecFwPolicyFileHash": cabhSecFwPolicyFileHash,
       "cabhSecFwPolicyFileOperStatus": cabhSecFwPolicyFileOperStatus,
       "cabhSecFwPolicyFileCurrentVersion": cabhSecFwPolicyFileCurrentVersion,
       "cabhSecFwPolicySuccessfulFileURL": cabhSecFwPolicySuccessfulFileURL,
       "cabhSecFwLogCtl": cabhSecFwLogCtl,
       "cabhSecFwEventType1Enable": cabhSecFwEventType1Enable,
       "cabhSecFwEventType2Enable": cabhSecFwEventType2Enable,
       "cabhSecFwEventType3Enable": cabhSecFwEventType3Enable,
       "cabhSecFwEventAttackAlertThreshold": cabhSecFwEventAttackAlertThreshold,
       "cabhSecFwEventAttackAlertPeriod": cabhSecFwEventAttackAlertPeriod,
       "cabhSecCertObjects": cabhSecCertObjects,
       "cabhSecCertPsCert": cabhSecCertPsCert,
       "cabhSecNotification": cabhSecNotification,
       "cabhSecConformance": cabhSecConformance,
       "cabhSecCompliances": cabhSecCompliances,
       "cabhSecCompliance": cabhSecCompliance,
       "cabhSec2Compliance": cabhSec2Compliance,
       "cabhSecGroups": cabhSecGroups,
       "cabhSecGroup": cabhSecGroup,
       "cabhSecCertGroup": cabhSecCertGroup,
       "cabhSecKerbGroup": cabhSecKerbGroup,
       "cabhSec2Group": cabhSec2Group,
       "cabhSecMibObjects": cabhSecMibObjects,
       "cabhSecKerbObjects": cabhSecKerbObjects,
       "cabhSecKerbBase": cabhSecKerbBase,
       "cabhSecKerbPKINITGracePeriod": cabhSecKerbPKINITGracePeriod,
       "cabhSecKerbTGSGracePeriod": cabhSecKerbTGSGracePeriod,
       "cabhSecKerbUnsolicitedKeyMaxTimeout": cabhSecKerbUnsolicitedKeyMaxTimeout,
       "cabhSecKerbUnsolicitedKeyMaxRetries": cabhSecKerbUnsolicitedKeyMaxRetries,
       "cabhSec2FwObjects": cabhSec2FwObjects,
       "cabhSec2FwBase": cabhSec2FwBase,
       "cabhSec2FwEnable": cabhSec2FwEnable,
       "cabhSec2FwPolicyFileURL": cabhSec2FwPolicyFileURL,
       "cabhSec2FwPolicyFileHash": cabhSec2FwPolicyFileHash,
       "cabhSec2FwPolicyFileOperStatus": cabhSec2FwPolicyFileOperStatus,
       "cabhSec2FwPolicyFileCurrentVersion": cabhSec2FwPolicyFileCurrentVersion,
       "cabhSec2FwClearPreviousRuleset": cabhSec2FwClearPreviousRuleset,
       "cabhSec2FwPolicySelection": cabhSec2FwPolicySelection,
       "cabhSec2FwEventSetToFactory": cabhSec2FwEventSetToFactory,
       "cabhSec2FwEventLastSetToFactory": cabhSec2FwEventLastSetToFactory,
       "cabhSec2FwPolicySuccessfulFileURL": cabhSec2FwPolicySuccessfulFileURL,
       "cabhSec2FwConfiguredRulesetPriority": cabhSec2FwConfiguredRulesetPriority,
       "cabhSec2FwClearLocalRuleset": cabhSec2FwClearLocalRuleset,
       "cabhSec2FwEvent": cabhSec2FwEvent,
       "cabhSec2FwEventControlTable": cabhSec2FwEventControlTable,
       "cabhSec2FwEventControlEntry": cabhSec2FwEventControlEntry,
       "cabhSec2FwEventType": cabhSec2FwEventType,
       "cabhSec2FwEventEnable": cabhSec2FwEventEnable,
       "cabhSec2FwEventThreshold": cabhSec2FwEventThreshold,
       "cabhSec2FwEventInterval": cabhSec2FwEventInterval,
       "cabhSec2FwEventCount": cabhSec2FwEventCount,
       "cabhSec2FwEventLogReset": cabhSec2FwEventLogReset,
       "cabhSec2FwEventLogLastReset": cabhSec2FwEventLogLastReset,
       "cabhSec2FwLog": cabhSec2FwLog,
       "cabhSec2FwLogTable": cabhSec2FwLogTable,
       "cabhSec2FwLogEntry": cabhSec2FwLogEntry,
       "cabhSec2FwLogIndex": cabhSec2FwLogIndex,
       "cabhSec2FwLogEventType": cabhSec2FwLogEventType,
       "cabhSec2FwLogEventPriority": cabhSec2FwLogEventPriority,
       "cabhSec2FwLogEventId": cabhSec2FwLogEventId,
       "cabhSec2FwLogTime": cabhSec2FwLogTime,
       "cabhSec2FwLogIpProtocol": cabhSec2FwLogIpProtocol,
       "cabhSec2FwLogIpSourceAddr": cabhSec2FwLogIpSourceAddr,
       "cabhSec2FwLogIpDestAddr": cabhSec2FwLogIpDestAddr,
       "cabhSec2FwLogIpSourcePort": cabhSec2FwLogIpSourcePort,
       "cabhSec2FwLogIpDestPort": cabhSec2FwLogIpDestPort,
       "cabhSec2FwLogMessageType": cabhSec2FwLogMessageType,
       "cabhSec2FwLogReplayCount": cabhSec2FwLogReplayCount,
       "cabhSec2FwLogMIBPointer": cabhSec2FwLogMIBPointer,
       "cabhSec2FwLogMatchingFilterTableName": cabhSec2FwLogMatchingFilterTableName,
       "cabhSec2FwLogMatchingFilterTableIndex": cabhSec2FwLogMatchingFilterTableIndex,
       "cabhSec2FwLogMatchingFilterDescr": cabhSec2FwLogMatchingFilterDescr,
       "cabhSec2FwFilter": cabhSec2FwFilter,
       "cabhSec2FwFilterScheduleTable": cabhSec2FwFilterScheduleTable,
       "cabhSec2FwFilterScheduleEntry": cabhSec2FwFilterScheduleEntry,
       "cabhSec2FwFilterScheduleStartTime": cabhSec2FwFilterScheduleStartTime,
       "cabhSec2FwFilterScheduleEndTime": cabhSec2FwFilterScheduleEndTime,
       "cabhSec2FwFilterScheduleDOW": cabhSec2FwFilterScheduleDOW,
       "cabhSec2FwFilterScheduleDescr": cabhSec2FwFilterScheduleDescr,
       "cabhSec2FwFactoryDefaultFilterTable": cabhSec2FwFactoryDefaultFilterTable,
       "cabhSec2FwFactoryDefaultFilterEntry": cabhSec2FwFactoryDefaultFilterEntry,
       "cabhSec2FwFactoryDefaultFilterIndex": cabhSec2FwFactoryDefaultFilterIndex,
       "cabhSec2FwFactoryDefaultFilterControl": cabhSec2FwFactoryDefaultFilterControl,
       "cabhSec2FwFactoryDefaultFilterIfIndex": cabhSec2FwFactoryDefaultFilterIfIndex,
       "cabhSec2FwFactoryDefaultFilterDirection": cabhSec2FwFactoryDefaultFilterDirection,
       "cabhSec2FwFactoryDefaultFilterSaddr": cabhSec2FwFactoryDefaultFilterSaddr,
       "cabhSec2FwFactoryDefaultFilterSmask": cabhSec2FwFactoryDefaultFilterSmask,
       "cabhSec2FwFactoryDefaultFilterDaddr": cabhSec2FwFactoryDefaultFilterDaddr,
       "cabhSec2FwFactoryDefaultFilterDmask": cabhSec2FwFactoryDefaultFilterDmask,
       "cabhSec2FwFactoryDefaultFilterProtocol": cabhSec2FwFactoryDefaultFilterProtocol,
       "cabhSec2FwFactoryDefaultFilterSourcePortLow": cabhSec2FwFactoryDefaultFilterSourcePortLow,
       "cabhSec2FwFactoryDefaultFilterSourcePortHigh": cabhSec2FwFactoryDefaultFilterSourcePortHigh,
       "cabhSec2FwFactoryDefaultFilterDestPortLow": cabhSec2FwFactoryDefaultFilterDestPortLow,
       "cabhSec2FwFactoryDefaultFilterDestPortHigh": cabhSec2FwFactoryDefaultFilterDestPortHigh,
       "cabhSec2FwFactoryDefaultFilterContinue": cabhSec2FwFactoryDefaultFilterContinue,
       "cabhSec2FwLocalFilterIpTable": cabhSec2FwLocalFilterIpTable,
       "cabhSec2FwLocalFilterIpEntry": cabhSec2FwLocalFilterIpEntry,
       "cabhSec2FwLocalFilterIpIndex": cabhSec2FwLocalFilterIpIndex,
       "cabhSec2FwLocalFilterIpStatus": cabhSec2FwLocalFilterIpStatus,
       "cabhSec2FwLocalFilterIpControl": cabhSec2FwLocalFilterIpControl,
       "cabhSec2FwLocalFilterIpIfIndex": cabhSec2FwLocalFilterIpIfIndex,
       "cabhSec2FwLocalFilterIpDirection": cabhSec2FwLocalFilterIpDirection,
       "cabhSec2FwLocalFilterIpSaddr": cabhSec2FwLocalFilterIpSaddr,
       "cabhSec2FwLocalFilterIpSmask": cabhSec2FwLocalFilterIpSmask,
       "cabhSec2FwLocalFilterIpDaddr": cabhSec2FwLocalFilterIpDaddr,
       "cabhSec2FwLocalFilterIpDmask": cabhSec2FwLocalFilterIpDmask,
       "cabhSec2FwLocalFilterIpProtocol": cabhSec2FwLocalFilterIpProtocol,
       "cabhSec2FwLocalFilterIpSourcePortLow": cabhSec2FwLocalFilterIpSourcePortLow,
       "cabhSec2FwLocalFilterIpSourcePortHigh": cabhSec2FwLocalFilterIpSourcePortHigh,
       "cabhSec2FwLocalFilterIpDestPortLow": cabhSec2FwLocalFilterIpDestPortLow,
       "cabhSec2FwLocalFilterIpDestPortHigh": cabhSec2FwLocalFilterIpDestPortHigh,
       "cabhSec2FwLocalFilterIpMatches": cabhSec2FwLocalFilterIpMatches,
       "cabhSec2FwLocalFilterIpContinue": cabhSec2FwLocalFilterIpContinue,
       "cabhSec2FwLocalFilterIpStartTime": cabhSec2FwLocalFilterIpStartTime,
       "cabhSec2FwLocalFilterIpEndTime": cabhSec2FwLocalFilterIpEndTime,
       "cabhSec2FwLocalFilterIpDOW": cabhSec2FwLocalFilterIpDOW,
       "cabhSec2FwLocalFilterIpDescr": cabhSec2FwLocalFilterIpDescr}
)
