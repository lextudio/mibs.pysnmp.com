# SNMP MIB module (DOCS-BPI2EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-BPI2EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:30 2024
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

(clabProjDocsis,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjDocsis")

(DocsX509ASN1DEREncodedCertificate,) = mibBuilder.importSymbols(
    "DOCS-IETF-BPI2-MIB",
    "DocsX509ASN1DEREncodedCertificate")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

docsBpi2Ext31Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 29)
)
docsBpi2Ext31Mib.setRevisions(
        ("2017-04-13 00:00",
         "2016-10-20 00:00",
         "2016-05-05 00:00",
         "2016-01-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DocsCvcCaCertificateChain(OctetString, TextualConvention):
    status = "current"
    displayHint = "50x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8192),
    )



# MIB Managed Objects in the order of their OIDs

_DocsBpi2Ext31Notifications_ObjectIdentity = ObjectIdentity
docsBpi2Ext31Notifications = _DocsBpi2Ext31Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 0)
)
_DocsBpi2Ext31MibObjects_ObjectIdentity = ObjectIdentity
docsBpi2Ext31MibObjects = _DocsBpi2Ext31MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1)
)
_DocsBpi2Ext31CmObjects_ObjectIdentity = ObjectIdentity
docsBpi2Ext31CmObjects = _DocsBpi2Ext31CmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 1)
)
_DocsBpi2Ext31CmCertObjects_ObjectIdentity = ObjectIdentity
docsBpi2Ext31CmCertObjects = _DocsBpi2Ext31CmCertObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 1, 1)
)
_DocsBpi2Ext31CmDeviceCertTable_Object = MibTable
docsBpi2Ext31CmDeviceCertTable = _DocsBpi2Ext31CmDeviceCertTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    docsBpi2Ext31CmDeviceCertTable.setStatus("current")
_DocsBpi2Ext31CmDeviceCertEntry_Object = MibTableRow
docsBpi2Ext31CmDeviceCertEntry = _DocsBpi2Ext31CmDeviceCertEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 1, 1, 1, 1)
)
docsBpi2Ext31CmDeviceCertEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsBpi2Ext31CmDeviceCertEntry.setStatus("current")
_DocsBpi2Ext31CmDeviceCmCert_Type = DocsX509ASN1DEREncodedCertificate
_DocsBpi2Ext31CmDeviceCmCert_Object = MibTableColumn
docsBpi2Ext31CmDeviceCmCert = _DocsBpi2Ext31CmDeviceCmCert_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 1, 1, 1, 1, 1),
    _DocsBpi2Ext31CmDeviceCmCert_Type()
)
docsBpi2Ext31CmDeviceCmCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsBpi2Ext31CmDeviceCmCert.setStatus("current")
_DocsBpi2Ext31CmDeviceManufCert_Type = DocsX509ASN1DEREncodedCertificate
_DocsBpi2Ext31CmDeviceManufCert_Object = MibTableColumn
docsBpi2Ext31CmDeviceManufCert = _DocsBpi2Ext31CmDeviceManufCert_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 1, 1, 1, 1, 2),
    _DocsBpi2Ext31CmDeviceManufCert_Type()
)
docsBpi2Ext31CmDeviceManufCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2Ext31CmDeviceManufCert.setStatus("current")
_DocsBpi2Ext31CodeDownloadControl_ObjectIdentity = ObjectIdentity
docsBpi2Ext31CodeDownloadControl = _DocsBpi2Ext31CodeDownloadControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 2)
)
_DocsBpi2Ext31CodeUpdateCvcChain_Type = DocsCvcCaCertificateChain
_DocsBpi2Ext31CodeUpdateCvcChain_Object = MibScalar
docsBpi2Ext31CodeUpdateCvcChain = _DocsBpi2Ext31CodeUpdateCvcChain_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 2, 1),
    _DocsBpi2Ext31CodeUpdateCvcChain_Type()
)
docsBpi2Ext31CodeUpdateCvcChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsBpi2Ext31CodeUpdateCvcChain.setStatus("current")
_DocsBpi2Ext31CodeMfgOrgName_Type = SnmpAdminString
_DocsBpi2Ext31CodeMfgOrgName_Object = MibScalar
docsBpi2Ext31CodeMfgOrgName = _DocsBpi2Ext31CodeMfgOrgName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 2, 2),
    _DocsBpi2Ext31CodeMfgOrgName_Type()
)
docsBpi2Ext31CodeMfgOrgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2Ext31CodeMfgOrgName.setStatus("current")


class _DocsBpi2Ext31CodeMfgCodeAccessStart_Type(DateAndTime):
    """Custom type docsBpi2Ext31CodeMfgCodeAccessStart based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_DocsBpi2Ext31CodeMfgCodeAccessStart_Type.__name__ = "DateAndTime"
_DocsBpi2Ext31CodeMfgCodeAccessStart_Object = MibScalar
docsBpi2Ext31CodeMfgCodeAccessStart = _DocsBpi2Ext31CodeMfgCodeAccessStart_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 2, 3),
    _DocsBpi2Ext31CodeMfgCodeAccessStart_Type()
)
docsBpi2Ext31CodeMfgCodeAccessStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2Ext31CodeMfgCodeAccessStart.setStatus("current")


class _DocsBpi2Ext31CodeMfgCvcAccessStart_Type(DateAndTime):
    """Custom type docsBpi2Ext31CodeMfgCvcAccessStart based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_DocsBpi2Ext31CodeMfgCvcAccessStart_Type.__name__ = "DateAndTime"
_DocsBpi2Ext31CodeMfgCvcAccessStart_Object = MibScalar
docsBpi2Ext31CodeMfgCvcAccessStart = _DocsBpi2Ext31CodeMfgCvcAccessStart_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 2, 4),
    _DocsBpi2Ext31CodeMfgCvcAccessStart_Type()
)
docsBpi2Ext31CodeMfgCvcAccessStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2Ext31CodeMfgCvcAccessStart.setStatus("current")
_DocsBpi2Ext31CodeCoSignerOrgName_Type = SnmpAdminString
_DocsBpi2Ext31CodeCoSignerOrgName_Object = MibScalar
docsBpi2Ext31CodeCoSignerOrgName = _DocsBpi2Ext31CodeCoSignerOrgName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 2, 5),
    _DocsBpi2Ext31CodeCoSignerOrgName_Type()
)
docsBpi2Ext31CodeCoSignerOrgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2Ext31CodeCoSignerOrgName.setStatus("current")


class _DocsBpi2Ext31CodeCoSignerCodeAccessStart_Type(DateAndTime):
    """Custom type docsBpi2Ext31CodeCoSignerCodeAccessStart based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_DocsBpi2Ext31CodeCoSignerCodeAccessStart_Type.__name__ = "DateAndTime"
_DocsBpi2Ext31CodeCoSignerCodeAccessStart_Object = MibScalar
docsBpi2Ext31CodeCoSignerCodeAccessStart = _DocsBpi2Ext31CodeCoSignerCodeAccessStart_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 2, 6),
    _DocsBpi2Ext31CodeCoSignerCodeAccessStart_Type()
)
docsBpi2Ext31CodeCoSignerCodeAccessStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2Ext31CodeCoSignerCodeAccessStart.setStatus("current")


class _DocsBpi2Ext31CodeCoSignerCvcAccessStart_Type(DateAndTime):
    """Custom type docsBpi2Ext31CodeCoSignerCvcAccessStart based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_DocsBpi2Ext31CodeCoSignerCvcAccessStart_Type.__name__ = "DateAndTime"
_DocsBpi2Ext31CodeCoSignerCvcAccessStart_Object = MibScalar
docsBpi2Ext31CodeCoSignerCvcAccessStart = _DocsBpi2Ext31CodeCoSignerCvcAccessStart_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 2, 7),
    _DocsBpi2Ext31CodeCoSignerCvcAccessStart_Type()
)
docsBpi2Ext31CodeCoSignerCvcAccessStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2Ext31CodeCoSignerCvcAccessStart.setStatus("current")
_DocsBpi2Ext31Conformance_ObjectIdentity = ObjectIdentity
docsBpi2Ext31Conformance = _DocsBpi2Ext31Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 2)
)
_DocsBpi2Ext31Compliances_ObjectIdentity = ObjectIdentity
docsBpi2Ext31Compliances = _DocsBpi2Ext31Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 2, 1)
)
_DocsBpi2Ext31Groups_ObjectIdentity = ObjectIdentity
docsBpi2Ext31Groups = _DocsBpi2Ext31Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 2, 2)
)

# Managed Objects groups

docsBpi2Ext31CmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 2, 2, 1)
)
docsBpi2Ext31CmGroup.setObjects(
      *(("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CmDeviceCmCert"),
        ("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CmDeviceManufCert"))
)
if mibBuilder.loadTexts:
    docsBpi2Ext31CmGroup.setStatus("current")

docsBpi2Ext31BaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 2, 2, 2)
)
docsBpi2Ext31BaseGroup.setObjects(
      *(("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CodeUpdateCvcChain"),
        ("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CodeMfgOrgName"),
        ("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CodeMfgCodeAccessStart"),
        ("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CodeMfgCvcAccessStart"),
        ("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CodeCoSignerOrgName"),
        ("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CodeCoSignerCodeAccessStart"),
        ("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CodeCoSignerCvcAccessStart"))
)
if mibBuilder.loadTexts:
    docsBpi2Ext31BaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsBpi2Ext31MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 2, 1, 1)
)
if mibBuilder.loadTexts:
    docsBpi2Ext31MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-BPI2EXT-MIB",
    **{"DocsCvcCaCertificateChain": DocsCvcCaCertificateChain,
       "docsBpi2Ext31Mib": docsBpi2Ext31Mib,
       "docsBpi2Ext31Notifications": docsBpi2Ext31Notifications,
       "docsBpi2Ext31MibObjects": docsBpi2Ext31MibObjects,
       "docsBpi2Ext31CmObjects": docsBpi2Ext31CmObjects,
       "docsBpi2Ext31CmCertObjects": docsBpi2Ext31CmCertObjects,
       "docsBpi2Ext31CmDeviceCertTable": docsBpi2Ext31CmDeviceCertTable,
       "docsBpi2Ext31CmDeviceCertEntry": docsBpi2Ext31CmDeviceCertEntry,
       "docsBpi2Ext31CmDeviceCmCert": docsBpi2Ext31CmDeviceCmCert,
       "docsBpi2Ext31CmDeviceManufCert": docsBpi2Ext31CmDeviceManufCert,
       "docsBpi2Ext31CodeDownloadControl": docsBpi2Ext31CodeDownloadControl,
       "docsBpi2Ext31CodeUpdateCvcChain": docsBpi2Ext31CodeUpdateCvcChain,
       "docsBpi2Ext31CodeMfgOrgName": docsBpi2Ext31CodeMfgOrgName,
       "docsBpi2Ext31CodeMfgCodeAccessStart": docsBpi2Ext31CodeMfgCodeAccessStart,
       "docsBpi2Ext31CodeMfgCvcAccessStart": docsBpi2Ext31CodeMfgCvcAccessStart,
       "docsBpi2Ext31CodeCoSignerOrgName": docsBpi2Ext31CodeCoSignerOrgName,
       "docsBpi2Ext31CodeCoSignerCodeAccessStart": docsBpi2Ext31CodeCoSignerCodeAccessStart,
       "docsBpi2Ext31CodeCoSignerCvcAccessStart": docsBpi2Ext31CodeCoSignerCvcAccessStart,
       "docsBpi2Ext31Conformance": docsBpi2Ext31Conformance,
       "docsBpi2Ext31Compliances": docsBpi2Ext31Compliances,
       "docsBpi2Ext31MIBCompliance": docsBpi2Ext31MIBCompliance,
       "docsBpi2Ext31Groups": docsBpi2Ext31Groups,
       "docsBpi2Ext31CmGroup": docsBpi2Ext31CmGroup,
       "docsBpi2Ext31BaseGroup": docsBpi2Ext31BaseGroup}
)
