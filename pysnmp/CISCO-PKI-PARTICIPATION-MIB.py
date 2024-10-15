# SNMP MIB module (CISCO-PKI-PARTICIPATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PKI-PARTICIPATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:47 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cpkiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 505)
)
cpkiMIB.setRevisions(
        ("2005-10-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoPkiAction(Integer32, TextualConvention):
    status = "current"
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("caauth", 2),
          ("cadelete", 3),
          ("certconfirm", 9),
          ("certdelete", 6),
          ("certimport", 5),
          ("certnoconfirm", 10),
          ("certreq", 4),
          ("crldelete", 13),
          ("crlimport", 12),
          ("forcecertdelete", 11),
          ("noop", 1),
          ("pkcs12export", 8),
          ("pkcs12import", 7))
    )



class CiscoPkiActionResult(Integer32, TextualConvention):
    status = "current"
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
        *(("failed", 3),
          ("inProgress", 4),
          ("needConfirm", 5),
          ("none", 1),
          ("success", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CpkiMIBNotifs_ObjectIdentity = ObjectIdentity
cpkiMIBNotifs = _CpkiMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 0)
)
_CpkiMIBObjects_ObjectIdentity = ObjectIdentity
cpkiMIBObjects = _CpkiMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1)
)
_CpkiConfig_ObjectIdentity = ObjectIdentity
cpkiConfig = _CpkiConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1)
)
_CpkiRSAKeyPairTable_Object = MibTable
cpkiRSAKeyPairTable = _CpkiRSAKeyPairTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cpkiRSAKeyPairTable.setStatus("current")
_CpkiRSAKeyPairEntry_Object = MibTableRow
cpkiRSAKeyPairEntry = _CpkiRSAKeyPairEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 1, 1)
)
cpkiRSAKeyPairEntry.setIndexNames(
    (0, "CISCO-PKI-PARTICIPATION-MIB", "cpkiRSAKeyPairName"),
)
if mibBuilder.loadTexts:
    cpkiRSAKeyPairEntry.setStatus("current")


class _CpkiRSAKeyPairName_Type(SnmpAdminString):
    """Custom type cpkiRSAKeyPairName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CpkiRSAKeyPairName_Type.__name__ = "SnmpAdminString"
_CpkiRSAKeyPairName_Object = MibTableColumn
cpkiRSAKeyPairName = _CpkiRSAKeyPairName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 1, 1, 1),
    _CpkiRSAKeyPairName_Type()
)
cpkiRSAKeyPairName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpkiRSAKeyPairName.setStatus("current")
_CpkiRSAKeyPairId_Type = Unsigned32
_CpkiRSAKeyPairId_Object = MibTableColumn
cpkiRSAKeyPairId = _CpkiRSAKeyPairId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 1, 1, 2),
    _CpkiRSAKeyPairId_Type()
)
cpkiRSAKeyPairId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpkiRSAKeyPairId.setStatus("current")


class _CpkiRSAKeyPairSize_Type(Integer32):
    """Custom type cpkiRSAKeyPairSize based on Integer32"""
    defaultValue = 1

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
        *(("rsa1024", 3),
          ("rsa1536", 4),
          ("rsa2048", 5),
          ("rsa512", 1),
          ("rsa768", 2))
    )


_CpkiRSAKeyPairSize_Type.__name__ = "Integer32"
_CpkiRSAKeyPairSize_Object = MibTableColumn
cpkiRSAKeyPairSize = _CpkiRSAKeyPairSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 1, 1, 3),
    _CpkiRSAKeyPairSize_Type()
)
cpkiRSAKeyPairSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpkiRSAKeyPairSize.setStatus("current")


class _CpkiRSAPvtKeyFileName_Type(SnmpAdminString):
    """Custom type cpkiRSAPvtKeyFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpkiRSAPvtKeyFileName_Type.__name__ = "SnmpAdminString"
_CpkiRSAPvtKeyFileName_Object = MibTableColumn
cpkiRSAPvtKeyFileName = _CpkiRSAPvtKeyFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 1, 1, 4),
    _CpkiRSAPvtKeyFileName_Type()
)
cpkiRSAPvtKeyFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpkiRSAPvtKeyFileName.setStatus("current")


class _CpkiRSAKeyPairExportable_Type(TruthValue):
    """Custom type cpkiRSAKeyPairExportable based on TruthValue"""


_CpkiRSAKeyPairExportable_Object = MibTableColumn
cpkiRSAKeyPairExportable = _CpkiRSAKeyPairExportable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 1, 1, 5),
    _CpkiRSAKeyPairExportable_Type()
)
cpkiRSAKeyPairExportable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpkiRSAKeyPairExportable.setStatus("current")


class _CpkiRSAKeyPairStorageType_Type(StorageType):
    """Custom type cpkiRSAKeyPairStorageType based on StorageType"""


_CpkiRSAKeyPairStorageType_Object = MibTableColumn
cpkiRSAKeyPairStorageType = _CpkiRSAKeyPairStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 1, 1, 6),
    _CpkiRSAKeyPairStorageType_Type()
)
cpkiRSAKeyPairStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpkiRSAKeyPairStorageType.setStatus("current")
_CpkiRSAKeyPairConfigRowStatus_Type = RowStatus
_CpkiRSAKeyPairConfigRowStatus_Object = MibTableColumn
cpkiRSAKeyPairConfigRowStatus = _CpkiRSAKeyPairConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 1, 1, 7),
    _CpkiRSAKeyPairConfigRowStatus_Type()
)
cpkiRSAKeyPairConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpkiRSAKeyPairConfigRowStatus.setStatus("current")
_CpkiTrustPointTable_Object = MibTable
cpkiTrustPointTable = _CpkiTrustPointTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cpkiTrustPointTable.setStatus("current")
_CpkiTrustPointEntry_Object = MibTableRow
cpkiTrustPointEntry = _CpkiTrustPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1)
)
cpkiTrustPointEntry.setIndexNames(
    (0, "CISCO-PKI-PARTICIPATION-MIB", "cpkiTrustPointName"),
)
if mibBuilder.loadTexts:
    cpkiTrustPointEntry.setStatus("current")


class _CpkiTrustPointName_Type(SnmpAdminString):
    """Custom type cpkiTrustPointName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CpkiTrustPointName_Type.__name__ = "SnmpAdminString"
_CpkiTrustPointName_Object = MibTableColumn
cpkiTrustPointName = _CpkiTrustPointName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1, 1),
    _CpkiTrustPointName_Type()
)
cpkiTrustPointName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpkiTrustPointName.setStatus("current")
_CpkiTrustPointId_Type = Unsigned32
_CpkiTrustPointId_Object = MibTableColumn
cpkiTrustPointId = _CpkiTrustPointId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1, 2),
    _CpkiTrustPointId_Type()
)
cpkiTrustPointId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpkiTrustPointId.setStatus("current")


class _CpkiKeyPairName_Type(SnmpAdminString):
    """Custom type cpkiKeyPairName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpkiKeyPairName_Type.__name__ = "SnmpAdminString"
_CpkiKeyPairName_Object = MibTableColumn
cpkiKeyPairName = _CpkiKeyPairName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1, 3),
    _CpkiKeyPairName_Type()
)
cpkiKeyPairName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpkiKeyPairName.setStatus("current")


class _CpkiIdCertFileName_Type(SnmpAdminString):
    """Custom type cpkiIdCertFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpkiIdCertFileName_Type.__name__ = "SnmpAdminString"
_CpkiIdCertFileName_Object = MibTableColumn
cpkiIdCertFileName = _CpkiIdCertFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1, 4),
    _CpkiIdCertFileName_Type()
)
cpkiIdCertFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpkiIdCertFileName.setStatus("current")


class _CpkiIdCertSubjectName_Type(SnmpAdminString):
    """Custom type cpkiIdCertSubjectName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpkiIdCertSubjectName_Type.__name__ = "SnmpAdminString"
_CpkiIdCertSubjectName_Object = MibTableColumn
cpkiIdCertSubjectName = _CpkiIdCertSubjectName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1, 5),
    _CpkiIdCertSubjectName_Type()
)
cpkiIdCertSubjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpkiIdCertSubjectName.setStatus("current")


class _CpkiIdCertSerialNum_Type(SnmpAdminString):
    """Custom type cpkiIdCertSerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpkiIdCertSerialNum_Type.__name__ = "SnmpAdminString"
_CpkiIdCertSerialNum_Object = MibTableColumn
cpkiIdCertSerialNum = _CpkiIdCertSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1, 6),
    _CpkiIdCertSerialNum_Type()
)
cpkiIdCertSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpkiIdCertSerialNum.setStatus("current")
_CpkiIdCertStartDate_Type = DateAndTime
_CpkiIdCertStartDate_Object = MibTableColumn
cpkiIdCertStartDate = _CpkiIdCertStartDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1, 7),
    _CpkiIdCertStartDate_Type()
)
cpkiIdCertStartDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpkiIdCertStartDate.setStatus("current")
_CpkiIdCertEndDate_Type = DateAndTime
_CpkiIdCertEndDate_Object = MibTableColumn
cpkiIdCertEndDate = _CpkiIdCertEndDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1, 8),
    _CpkiIdCertEndDate_Type()
)
cpkiIdCertEndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpkiIdCertEndDate.setStatus("current")


class _CpkiIdCertFingerPrint_Type(SnmpAdminString):
    """Custom type cpkiIdCertFingerPrint based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpkiIdCertFingerPrint_Type.__name__ = "SnmpAdminString"
_CpkiIdCertFingerPrint_Object = MibTableColumn
cpkiIdCertFingerPrint = _CpkiIdCertFingerPrint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1, 9),
    _CpkiIdCertFingerPrint_Type()
)
cpkiIdCertFingerPrint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpkiIdCertFingerPrint.setStatus("current")


class _CpkiIssuerCertFileName_Type(SnmpAdminString):
    """Custom type cpkiIssuerCertFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpkiIssuerCertFileName_Type.__name__ = "SnmpAdminString"
_CpkiIssuerCertFileName_Object = MibTableColumn
cpkiIssuerCertFileName = _CpkiIssuerCertFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1, 10),
    _CpkiIssuerCertFileName_Type()
)
cpkiIssuerCertFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpkiIssuerCertFileName.setStatus("current")


class _CpkiIssuerCertSubjectName_Type(SnmpAdminString):
    """Custom type cpkiIssuerCertSubjectName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpkiIssuerCertSubjectName_Type.__name__ = "SnmpAdminString"
_CpkiIssuerCertSubjectName_Object = MibTableColumn
cpkiIssuerCertSubjectName = _CpkiIssuerCertSubjectName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1, 11),
    _CpkiIssuerCertSubjectName_Type()
)
cpkiIssuerCertSubjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpkiIssuerCertSubjectName.setStatus("current")


class _CpkiIssuerCertSerialNum_Type(SnmpAdminString):
    """Custom type cpkiIssuerCertSerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpkiIssuerCertSerialNum_Type.__name__ = "SnmpAdminString"
_CpkiIssuerCertSerialNum_Object = MibTableColumn
cpkiIssuerCertSerialNum = _CpkiIssuerCertSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1, 12),
    _CpkiIssuerCertSerialNum_Type()
)
cpkiIssuerCertSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpkiIssuerCertSerialNum.setStatus("current")
_CpkiIssuerCertStartDate_Type = DateAndTime
_CpkiIssuerCertStartDate_Object = MibTableColumn
cpkiIssuerCertStartDate = _CpkiIssuerCertStartDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1, 13),
    _CpkiIssuerCertStartDate_Type()
)
cpkiIssuerCertStartDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpkiIssuerCertStartDate.setStatus("current")
_CpkiIssuerCertEndDate_Type = DateAndTime
_CpkiIssuerCertEndDate_Object = MibTableColumn
cpkiIssuerCertEndDate = _CpkiIssuerCertEndDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1, 14),
    _CpkiIssuerCertEndDate_Type()
)
cpkiIssuerCertEndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpkiIssuerCertEndDate.setStatus("current")


class _CpkiIssuerCertFingerPrint_Type(SnmpAdminString):
    """Custom type cpkiIssuerCertFingerPrint based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpkiIssuerCertFingerPrint_Type.__name__ = "SnmpAdminString"
_CpkiIssuerCertFingerPrint_Object = MibTableColumn
cpkiIssuerCertFingerPrint = _CpkiIssuerCertFingerPrint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1, 15),
    _CpkiIssuerCertFingerPrint_Type()
)
cpkiIssuerCertFingerPrint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpkiIssuerCertFingerPrint.setStatus("current")


class _CpkiRevokeCheckMethods_Type(OctetString):
    """Custom type cpkiRevokeCheckMethods based on OctetString"""
    defaultHexValue = "02000000000000000000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_CpkiRevokeCheckMethods_Type.__name__ = "OctetString"
_CpkiRevokeCheckMethods_Object = MibTableColumn
cpkiRevokeCheckMethods = _CpkiRevokeCheckMethods_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1, 16),
    _CpkiRevokeCheckMethods_Type()
)
cpkiRevokeCheckMethods.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpkiRevokeCheckMethods.setStatus("current")


class _CpkiOCSPurl_Type(SnmpAdminString):
    """Custom type cpkiOCSPurl based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpkiOCSPurl_Type.__name__ = "SnmpAdminString"
_CpkiOCSPurl_Object = MibTableColumn
cpkiOCSPurl = _CpkiOCSPurl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1, 17),
    _CpkiOCSPurl_Type()
)
cpkiOCSPurl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpkiOCSPurl.setStatus("current")


class _CpkiAction_Type(CiscoPkiAction):
    """Custom type cpkiAction based on CiscoPkiAction"""


_CpkiAction_Object = MibTableColumn
cpkiAction = _CpkiAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1, 18),
    _CpkiAction_Type()
)
cpkiAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpkiAction.setStatus("current")
_CpkiActionUrl_Type = SnmpAdminString
_CpkiActionUrl_Object = MibTableColumn
cpkiActionUrl = _CpkiActionUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1, 19),
    _CpkiActionUrl_Type()
)
cpkiActionUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpkiActionUrl.setStatus("current")


class _CpkiActionPassword_Type(SnmpAdminString):
    """Custom type cpkiActionPassword based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpkiActionPassword_Type.__name__ = "SnmpAdminString"
_CpkiActionPassword_Object = MibTableColumn
cpkiActionPassword = _CpkiActionPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1, 20),
    _CpkiActionPassword_Type()
)
cpkiActionPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpkiActionPassword.setStatus("current")
_CpkiLastAction_Type = CiscoPkiAction
_CpkiLastAction_Object = MibTableColumn
cpkiLastAction = _CpkiLastAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1, 21),
    _CpkiLastAction_Type()
)
cpkiLastAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpkiLastAction.setStatus("current")
_CpkiLastActionResult_Type = CiscoPkiActionResult
_CpkiLastActionResult_Object = MibTableColumn
cpkiLastActionResult = _CpkiLastActionResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1, 22),
    _CpkiLastActionResult_Type()
)
cpkiLastActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpkiLastActionResult.setStatus("current")
_CpkiLastActionFailureReason_Type = SnmpAdminString
_CpkiLastActionFailureReason_Object = MibTableColumn
cpkiLastActionFailureReason = _CpkiLastActionFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1, 23),
    _CpkiLastActionFailureReason_Type()
)
cpkiLastActionFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpkiLastActionFailureReason.setStatus("current")


class _CpkiTrustPointStorageType_Type(StorageType):
    """Custom type cpkiTrustPointStorageType based on StorageType"""


_CpkiTrustPointStorageType_Object = MibTableColumn
cpkiTrustPointStorageType = _CpkiTrustPointStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1, 24),
    _CpkiTrustPointStorageType_Type()
)
cpkiTrustPointStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpkiTrustPointStorageType.setStatus("current")
_CpkiTrustPointConfigRowStatus_Type = RowStatus
_CpkiTrustPointConfigRowStatus_Object = MibTableColumn
cpkiTrustPointConfigRowStatus = _CpkiTrustPointConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 1, 1, 2, 1, 25),
    _CpkiTrustPointConfigRowStatus_Type()
)
cpkiTrustPointConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpkiTrustPointConfigRowStatus.setStatus("current")
_CpkiMIBConform_ObjectIdentity = ObjectIdentity
cpkiMIBConform = _CpkiMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 2)
)
_CpkiMIBCompliances_ObjectIdentity = ObjectIdentity
cpkiMIBCompliances = _CpkiMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 2, 1)
)
_CpkiMIBGroups_ObjectIdentity = ObjectIdentity
cpkiMIBGroups = _CpkiMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 2, 2)
)

# Managed Objects groups

cpkiConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 2, 2, 1)
)
cpkiConfigGroup.setObjects(
      *(("CISCO-PKI-PARTICIPATION-MIB", "cpkiRSAKeyPairId"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiRSAKeyPairSize"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiRSAPvtKeyFileName"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiRSAKeyPairExportable"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiRSAKeyPairStorageType"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiRSAKeyPairConfigRowStatus"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiTrustPointId"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiKeyPairName"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiIdCertFileName"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiIdCertSubjectName"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiIdCertSerialNum"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiIdCertStartDate"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiIdCertEndDate"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiIdCertFingerPrint"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiIssuerCertFileName"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiIssuerCertSubjectName"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiIssuerCertSerialNum"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiIssuerCertStartDate"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiIssuerCertEndDate"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiIssuerCertFingerPrint"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiRevokeCheckMethods"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiOCSPurl"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiAction"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiActionUrl"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiActionPassword"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiLastAction"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiLastActionResult"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiLastActionFailureReason"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiTrustPointStorageType"),
        ("CISCO-PKI-PARTICIPATION-MIB", "cpkiTrustPointConfigRowStatus"))
)
if mibBuilder.loadTexts:
    cpkiConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cpkiMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 505, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cpkiMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PKI-PARTICIPATION-MIB",
    **{"CiscoPkiAction": CiscoPkiAction,
       "CiscoPkiActionResult": CiscoPkiActionResult,
       "cpkiMIB": cpkiMIB,
       "cpkiMIBNotifs": cpkiMIBNotifs,
       "cpkiMIBObjects": cpkiMIBObjects,
       "cpkiConfig": cpkiConfig,
       "cpkiRSAKeyPairTable": cpkiRSAKeyPairTable,
       "cpkiRSAKeyPairEntry": cpkiRSAKeyPairEntry,
       "cpkiRSAKeyPairName": cpkiRSAKeyPairName,
       "cpkiRSAKeyPairId": cpkiRSAKeyPairId,
       "cpkiRSAKeyPairSize": cpkiRSAKeyPairSize,
       "cpkiRSAPvtKeyFileName": cpkiRSAPvtKeyFileName,
       "cpkiRSAKeyPairExportable": cpkiRSAKeyPairExportable,
       "cpkiRSAKeyPairStorageType": cpkiRSAKeyPairStorageType,
       "cpkiRSAKeyPairConfigRowStatus": cpkiRSAKeyPairConfigRowStatus,
       "cpkiTrustPointTable": cpkiTrustPointTable,
       "cpkiTrustPointEntry": cpkiTrustPointEntry,
       "cpkiTrustPointName": cpkiTrustPointName,
       "cpkiTrustPointId": cpkiTrustPointId,
       "cpkiKeyPairName": cpkiKeyPairName,
       "cpkiIdCertFileName": cpkiIdCertFileName,
       "cpkiIdCertSubjectName": cpkiIdCertSubjectName,
       "cpkiIdCertSerialNum": cpkiIdCertSerialNum,
       "cpkiIdCertStartDate": cpkiIdCertStartDate,
       "cpkiIdCertEndDate": cpkiIdCertEndDate,
       "cpkiIdCertFingerPrint": cpkiIdCertFingerPrint,
       "cpkiIssuerCertFileName": cpkiIssuerCertFileName,
       "cpkiIssuerCertSubjectName": cpkiIssuerCertSubjectName,
       "cpkiIssuerCertSerialNum": cpkiIssuerCertSerialNum,
       "cpkiIssuerCertStartDate": cpkiIssuerCertStartDate,
       "cpkiIssuerCertEndDate": cpkiIssuerCertEndDate,
       "cpkiIssuerCertFingerPrint": cpkiIssuerCertFingerPrint,
       "cpkiRevokeCheckMethods": cpkiRevokeCheckMethods,
       "cpkiOCSPurl": cpkiOCSPurl,
       "cpkiAction": cpkiAction,
       "cpkiActionUrl": cpkiActionUrl,
       "cpkiActionPassword": cpkiActionPassword,
       "cpkiLastAction": cpkiLastAction,
       "cpkiLastActionResult": cpkiLastActionResult,
       "cpkiLastActionFailureReason": cpkiLastActionFailureReason,
       "cpkiTrustPointStorageType": cpkiTrustPointStorageType,
       "cpkiTrustPointConfigRowStatus": cpkiTrustPointConfigRowStatus,
       "cpkiMIBConform": cpkiMIBConform,
       "cpkiMIBCompliances": cpkiMIBCompliances,
       "cpkiMIBCompliance": cpkiMIBCompliance,
       "cpkiMIBGroups": cpkiMIBGroups,
       "cpkiConfigGroup": cpkiConfigGroup}
)
