# SNMP MIB module (TVD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TVD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:03 2024
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

(nai,
 naiTrapAgent,
 naiTrapAgentVersion,
 naiTrapDiagID,
 naiTrapLongDescription,
 naiTrapProblemResolution,
 naiTrapSeverity,
 naiTrapShortDescription,
 naiTrapSourceDNSName,
 naiTrapTargetDNSName,
 naiTrapURL) = mibBuilder.importSymbols(
    "NAI-MIB",
    "nai",
    "naiTrapAgent",
    "naiTrapAgentVersion",
    "naiTrapDiagID",
    "naiTrapLongDescription",
    "naiTrapProblemResolution",
    "naiTrapSeverity",
    "naiTrapShortDescription",
    "naiTrapSourceDNSName",
    "naiTrapTargetDNSName",
    "naiTrapURL")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mcafee_ObjectIdentity = ObjectIdentity
mcafee = _Mcafee_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3401, 12)
)
_McafeeTVDTrap_ObjectIdentity = ObjectIdentity
mcafeeTVDTrap = _McafeeTVDTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0)
)
_McafeeStandardTrapField_ObjectIdentity = ObjectIdentity
mcafeeStandardTrapField = _McafeeStandardTrapField_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1)
)
_Mcafee_TRAPID_Type = Integer32
_Mcafee_TRAPID_Object = MibScalar
mcafee_TRAPID = _Mcafee_TRAPID_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 1),
    _Mcafee_TRAPID_Type()
)
mcafee_TRAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_TRAPID.setStatus("mandatory")
_Mcafee_ENGINEVERSION_Type = DisplayString
_Mcafee_ENGINEVERSION_Object = MibScalar
mcafee_ENGINEVERSION = _Mcafee_ENGINEVERSION_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 2),
    _Mcafee_ENGINEVERSION_Type()
)
mcafee_ENGINEVERSION.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_ENGINEVERSION.setStatus("mandatory")
_Mcafee_DATVERSION_Type = DisplayString
_Mcafee_DATVERSION_Object = MibScalar
mcafee_DATVERSION = _Mcafee_DATVERSION_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 3),
    _Mcafee_DATVERSION_Type()
)
mcafee_DATVERSION.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_DATVERSION.setStatus("mandatory")
_Mcafee_ENGINESTATUS_Type = Integer32
_Mcafee_ENGINESTATUS_Object = MibScalar
mcafee_ENGINESTATUS = _Mcafee_ENGINESTATUS_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 4),
    _Mcafee_ENGINESTATUS_Type()
)
mcafee_ENGINESTATUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_ENGINESTATUS.setStatus("mandatory")
_Mcafee_VIRUSNAME_Type = DisplayString
_Mcafee_VIRUSNAME_Object = MibScalar
mcafee_VIRUSNAME = _Mcafee_VIRUSNAME_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 5),
    _Mcafee_VIRUSNAME_Type()
)
mcafee_VIRUSNAME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_VIRUSNAME.setStatus("mandatory")
_Mcafee_VIRUSTYPE_Type = DisplayString
_Mcafee_VIRUSTYPE_Object = MibScalar
mcafee_VIRUSTYPE = _Mcafee_VIRUSTYPE_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 6),
    _Mcafee_VIRUSTYPE_Type()
)
mcafee_VIRUSTYPE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_VIRUSTYPE.setStatus("mandatory")
_Mcafee_FILENAME_Type = DisplayString
_Mcafee_FILENAME_Object = MibScalar
mcafee_FILENAME = _Mcafee_FILENAME_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 7),
    _Mcafee_FILENAME_Type()
)
mcafee_FILENAME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_FILENAME.setStatus("mandatory")
_Mcafee_USERNAME_Type = DisplayString
_Mcafee_USERNAME_Object = MibScalar
mcafee_USERNAME = _Mcafee_USERNAME_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 8),
    _Mcafee_USERNAME_Type()
)
mcafee_USERNAME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_USERNAME.setStatus("mandatory")
_Mcafee_OS_Type = DisplayString
_Mcafee_OS_Object = MibScalar
mcafee_OS = _Mcafee_OS_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 9),
    _Mcafee_OS_Type()
)
mcafee_OS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_OS.setStatus("mandatory")
_Mcafee_PROCESSORSERIAL_Type = DisplayString
_Mcafee_PROCESSORSERIAL_Object = MibScalar
mcafee_PROCESSORSERIAL = _Mcafee_PROCESSORSERIAL_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 10),
    _Mcafee_PROCESSORSERIAL_Type()
)
mcafee_PROCESSORSERIAL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_PROCESSORSERIAL.setStatus("mandatory")
_Mcafee_TASKNAME_Type = DisplayString
_Mcafee_TASKNAME_Object = MibScalar
mcafee_TASKNAME = _Mcafee_TASKNAME_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 11),
    _Mcafee_TASKNAME_Type()
)
mcafee_TASKNAME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_TASKNAME.setStatus("mandatory")
_Mcafee_NUMVIRS_Type = Integer32
_Mcafee_NUMVIRS_Object = MibScalar
mcafee_NUMVIRS = _Mcafee_NUMVIRS_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 15),
    _Mcafee_NUMVIRS_Type()
)
mcafee_NUMVIRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_NUMVIRS.setStatus("mandatory")
_Mcafee_NUMCLEANED_Type = Integer32
_Mcafee_NUMCLEANED_Object = MibScalar
mcafee_NUMCLEANED = _Mcafee_NUMCLEANED_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 16),
    _Mcafee_NUMCLEANED_Type()
)
mcafee_NUMCLEANED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_NUMCLEANED.setStatus("mandatory")
_Mcafee_NUMDELETED_Type = Integer32
_Mcafee_NUMDELETED_Object = MibScalar
mcafee_NUMDELETED = _Mcafee_NUMDELETED_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 17),
    _Mcafee_NUMDELETED_Type()
)
mcafee_NUMDELETED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_NUMDELETED.setStatus("mandatory")
_Mcafee_NUMQUARANTINED_Type = Integer32
_Mcafee_NUMQUARANTINED_Object = MibScalar
mcafee_NUMQUARANTINED = _Mcafee_NUMQUARANTINED_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 18),
    _Mcafee_NUMQUARANTINED_Type()
)
mcafee_NUMQUARANTINED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_NUMQUARANTINED.setStatus("mandatory")
_Mcafee_SCANRETURNCODE_Type = Integer32
_Mcafee_SCANRETURNCODE_Object = MibScalar
mcafee_SCANRETURNCODE = _Mcafee_SCANRETURNCODE_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 19),
    _Mcafee_SCANRETURNCODE_Type()
)
mcafee_SCANRETURNCODE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_SCANRETURNCODE.setStatus("mandatory")
_Mcafee_MAILFROMNAME_Type = DisplayString
_Mcafee_MAILFROMNAME_Object = MibScalar
mcafee_MAILFROMNAME = _Mcafee_MAILFROMNAME_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 30),
    _Mcafee_MAILFROMNAME_Type()
)
mcafee_MAILFROMNAME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_MAILFROMNAME.setStatus("mandatory")
_Mcafee_MAILTONAME_Type = DisplayString
_Mcafee_MAILTONAME_Object = MibScalar
mcafee_MAILTONAME = _Mcafee_MAILTONAME_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 31),
    _Mcafee_MAILTONAME_Type()
)
mcafee_MAILTONAME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_MAILTONAME.setStatus("mandatory")
_Mcafee_MAILCCNAME_Type = DisplayString
_Mcafee_MAILCCNAME_Object = MibScalar
mcafee_MAILCCNAME = _Mcafee_MAILCCNAME_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 32),
    _Mcafee_MAILCCNAME_Type()
)
mcafee_MAILCCNAME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_MAILCCNAME.setStatus("mandatory")
_Mcafee_MAILSUBJECTLINE_Type = DisplayString
_Mcafee_MAILSUBJECTLINE_Object = MibScalar
mcafee_MAILSUBJECTLINE = _Mcafee_MAILSUBJECTLINE_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 33),
    _Mcafee_MAILSUBJECTLINE_Type()
)
mcafee_MAILSUBJECTLINE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_MAILSUBJECTLINE.setStatus("optional")
_Mcafee_MAILIDENTIFIERINFO_Type = DisplayString
_Mcafee_MAILIDENTIFIERINFO_Object = MibScalar
mcafee_MAILIDENTIFIERINFO = _Mcafee_MAILIDENTIFIERINFO_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 34),
    _Mcafee_MAILIDENTIFIERINFO_Type()
)
mcafee_MAILIDENTIFIERINFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_MAILIDENTIFIERINFO.setStatus("optional")
_Mcafee_NOTEID_Type = DisplayString
_Mcafee_NOTEID_Object = MibScalar
mcafee_NOTEID = _Mcafee_NOTEID_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 35),
    _Mcafee_NOTEID_Type()
)
mcafee_NOTEID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_NOTEID.setStatus("optional")
_Mcafee_NOTESSERVERNAME_Type = DisplayString
_Mcafee_NOTESSERVERNAME_Object = MibScalar
mcafee_NOTESSERVERNAME = _Mcafee_NOTESSERVERNAME_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 36),
    _Mcafee_NOTESSERVERNAME_Type()
)
mcafee_NOTESSERVERNAME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_NOTESSERVERNAME.setStatus("optional")
_Mcafee_NOTESDBNAME_Type = DisplayString
_Mcafee_NOTESDBNAME_Object = MibScalar
mcafee_NOTESDBNAME = _Mcafee_NOTESDBNAME_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 37),
    _Mcafee_NOTESDBNAME_Type()
)
mcafee_NOTESDBNAME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_NOTESDBNAME.setStatus("optional")
_Mcafee_DOMAIN_Type = DisplayString
_Mcafee_DOMAIN_Object = MibScalar
mcafee_DOMAIN = _Mcafee_DOMAIN_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 38),
    _Mcafee_DOMAIN_Type()
)
mcafee_DOMAIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_DOMAIN.setStatus("optional")
_Mcafee_OBRULE_Type = DisplayString
_Mcafee_OBRULE_Object = MibScalar
mcafee_OBRULE = _Mcafee_OBRULE_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 39),
    _Mcafee_OBRULE_Type()
)
mcafee_OBRULE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_OBRULE.setStatus("optional")
_Mcafee_LANGUAGECODE_Type = DisplayString
_Mcafee_LANGUAGECODE_Object = MibScalar
mcafee_LANGUAGECODE = _Mcafee_LANGUAGECODE_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 40),
    _Mcafee_LANGUAGECODE_Type()
)
mcafee_LANGUAGECODE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_LANGUAGECODE.setStatus("optional")
_Mcafee_CLIENTCOMPUTER_Type = DisplayString
_Mcafee_CLIENTCOMPUTER_Object = MibScalar
mcafee_CLIENTCOMPUTER = _Mcafee_CLIENTCOMPUTER_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 41),
    _Mcafee_CLIENTCOMPUTER_Type()
)
mcafee_CLIENTCOMPUTER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_CLIENTCOMPUTER.setStatus("optional")
_Mcafee_TSCLIENTID_Type = Integer32
_Mcafee_TSCLIENTID_Object = MibScalar
mcafee_TSCLIENTID = _Mcafee_TSCLIENTID_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 42),
    _Mcafee_TSCLIENTID_Type()
)
mcafee_TSCLIENTID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_TSCLIENTID.setStatus("optional")
_Mcafee_ACCESSPROCESSNAME_Type = DisplayString
_Mcafee_ACCESSPROCESSNAME_Object = MibScalar
mcafee_ACCESSPROCESSNAME = _Mcafee_ACCESSPROCESSNAME_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 43),
    _Mcafee_ACCESSPROCESSNAME_Type()
)
mcafee_ACCESSPROCESSNAME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_ACCESSPROCESSNAME.setStatus("optional")
_Mcafee_EVENTNAME_Type = DisplayString
_Mcafee_EVENTNAME_Object = MibScalar
mcafee_EVENTNAME = _Mcafee_EVENTNAME_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 44),
    _Mcafee_EVENTNAME_Type()
)
mcafee_EVENTNAME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_EVENTNAME.setStatus("optional")
_Mcafee_GMTTIME_Type = DisplayString
_Mcafee_GMTTIME_Object = MibScalar
mcafee_GMTTIME = _Mcafee_GMTTIME_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 45),
    _Mcafee_GMTTIME_Type()
)
mcafee_GMTTIME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_GMTTIME.setStatus("optional")
_Mcafee_TIME_Type = DisplayString
_Mcafee_TIME_Object = MibScalar
mcafee_TIME = _Mcafee_TIME_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 46),
    _Mcafee_TIME_Type()
)
mcafee_TIME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_TIME.setStatus("optional")
_Mcafee_SOURCEIP_Type = DisplayString
_Mcafee_SOURCEIP_Object = MibScalar
mcafee_SOURCEIP = _Mcafee_SOURCEIP_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 47),
    _Mcafee_SOURCEIP_Type()
)
mcafee_SOURCEIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_SOURCEIP.setStatus("optional")
_Mcafee_TARGETIP_Type = DisplayString
_Mcafee_TARGETIP_Object = MibScalar
mcafee_TARGETIP = _Mcafee_TARGETIP_Object(
    (1, 3, 6, 1, 4, 1, 3401, 12, 1, 48),
    _Mcafee_TARGETIP_Type()
)
mcafee_TARGETIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcafee_TARGETIP.setStatus("optional")

# Managed Objects groups


# Notification objects

mcafee_EVENT_VIRFOUND = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1024)
)
mcafee_EVENT_VIRFOUND.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_VIRFOUND.setStatus(
        ""
    )

mcafee_EVENT_FILECLEANED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1025)
)
mcafee_EVENT_FILECLEANED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_FILECLEANED.setStatus(
        ""
    )

mcafee_EVENT_FILECLEANERROR = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1026)
)
mcafee_EVENT_FILECLEANERROR.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_FILECLEANERROR.setStatus(
        ""
    )

mcafee_EVENT_FILEDELETED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1027)
)
mcafee_EVENT_FILEDELETED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_FILEDELETED.setStatus(
        ""
    )

mcafee_EVENT_FILEDELETEERROR = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1028)
)
mcafee_EVENT_FILEDELETEERROR.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_FILEDELETEERROR.setStatus(
        ""
    )

mcafee_EVENT_FILEEXCLUDING = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1029)
)
mcafee_EVENT_FILEEXCLUDING.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_FILEEXCLUDING.setStatus(
        ""
    )

mcafee_EVENT_EXCLUDEERR = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1030)
)
mcafee_EVENT_EXCLUDEERR.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_EXCLUDEERR.setStatus(
        ""
    )

mcafee_EVENT_INFECTION_ACESSDENIED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1031)
)
mcafee_EVENT_INFECTION_ACESSDENIED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_INFECTION_ACESSDENIED.setStatus(
        ""
    )

mcafee_EVENT_VIRUS_QUARANTINED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1032)
)
mcafee_EVENT_VIRUS_QUARANTINED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_VIRUS_QUARANTINED.setStatus(
        ""
    )

mcafee_EVENT_VIRUS_QUARANTINE_FAILURE = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1033)
)
mcafee_EVENT_VIRUS_QUARANTINE_FAILURE.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_VIRUS_QUARANTINE_FAILURE.setStatus(
        ""
    )

mcafee_EVENT_SCANEND_NO_VIRUSES = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1034)
)
mcafee_EVENT_SCANEND_NO_VIRUSES.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_SCANEND_NO_VIRUSES.setStatus(
        ""
    )

mcafee_EVENT_SCAN_CANCELED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1035)
)
mcafee_EVENT_SCAN_CANCELED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_SCAN_CANCELED.setStatus(
        ""
    )

mcafee_EVENT_VIRUS_FOUND_IN_MEMORY = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1036)
)
mcafee_EVENT_VIRUS_FOUND_IN_MEMORY.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_VIRUS_FOUND_IN_MEMORY.setStatus(
        ""
    )

mcafee_EVENT_VIRUS_IN_BOOT_RECORD = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1037)
)
mcafee_EVENT_VIRUS_IN_BOOT_RECORD.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_VIRUS_IN_BOOT_RECORD.setStatus(
        ""
    )

mcafee_EVENT_SCAN_FOUND_INFECTED_FILES = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1038)
)
mcafee_EVENT_SCAN_FOUND_INFECTED_FILES.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_SCAN_FOUND_INFECTED_FILES.setStatus(
        ""
    )

mcafee_EVENT_SCAN_FOUND_AND_CLEANED_INFECTIONS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1039)
)
mcafee_EVENT_SCAN_FOUND_AND_CLEANED_INFECTIONS.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_SCAN_FOUND_AND_CLEANED_INFECTIONS.setStatus(
        ""
    )

mcafee_EVENT_ALOG_ERROR = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1040)
)
mcafee_EVENT_ALOG_ERROR.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_ALOG_ERROR.setStatus(
        ""
    )

mcafee_EVENT_MEMALLOC_ERROR = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1041)
)
mcafee_EVENT_MEMALLOC_ERROR.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_MEMALLOC_ERROR.setStatus(
        ""
    )

mcafee_EVENT_DIR_ACCESS_ERROR = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1042)
)
mcafee_EVENT_DIR_ACCESS_ERROR.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_DIR_ACCESS_ERROR.setStatus(
        ""
    )

mcafee_EVENT_WRITE_PROTECT_ERR = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1043)
)
mcafee_EVENT_WRITE_PROTECT_ERR.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_WRITE_PROTECT_ERR.setStatus(
        ""
    )

mcafee_EVENT_MEDIA_NOT_FOUND_ERR = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1044)
)
mcafee_EVENT_MEDIA_NOT_FOUND_ERR.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_MEDIA_NOT_FOUND_ERR.setStatus(
        ""
    )

mcafee_EVENT_SCAN_ITEM_INVALID = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1045)
)
mcafee_EVENT_SCAN_ITEM_INVALID.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_SCAN_ITEM_INVALID.setStatus(
        ""
    )

mcafee_EVENT_FILE_IO_ERRORS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1046)
)
mcafee_EVENT_FILE_IO_ERRORS.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_FILE_IO_ERRORS.setStatus(
        ""
    )

mcafee_EVENT_DISK_IO_ERR = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1047)
)
mcafee_EVENT_DISK_IO_ERR.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_DISK_IO_ERR.setStatus(
        ""
    )

mcafee_EVENT_GEN_SYSTEM_ERROR = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1048)
)
mcafee_EVENT_GEN_SYSTEM_ERROR.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_GEN_SYSTEM_ERROR.setStatus(
        ""
    )

mcafee_EVENT_INTERNAL_APP_ERROR = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1049)
)
mcafee_EVENT_INTERNAL_APP_ERROR.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_INTERNAL_APP_ERROR.setStatus(
        ""
    )

mcafee_EVENT_INFECTION_PASSWORD_PROTECTED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1050)
)
mcafee_EVENT_INFECTION_PASSWORD_PROTECTED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_INFECTION_PASSWORD_PROTECTED.setStatus(
        ""
    )

mcafee_EVENT_NOT_SCANNED_PASSWORD = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1051)
)
mcafee_EVENT_NOT_SCANNED_PASSWORD.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_NOT_SCANNED_PASSWORD.setStatus(
        ""
    )

mcafee_EVENT_INFECTED_BINDARY = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1052)
)
mcafee_EVENT_INFECTED_BINDARY.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_INFECTED_BINDARY.setStatus(
        ""
    )

mcafee_EVENT_INFECTED_HEURISTICS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1053)
)
mcafee_EVENT_INFECTED_HEURISTICS.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_INFECTED_HEURISTICS.setStatus(
        ""
    )

mcafee_EVENT_DELETED_HEURISTICS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1054)
)
mcafee_EVENT_DELETED_HEURISTICS.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_DELETED_HEURISTICS.setStatus(
        ""
    )

mcafee_EVENT_DELETE_ERR_HEURISTICS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1055)
)
mcafee_EVENT_DELETE_ERR_HEURISTICS.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_DELETE_ERR_HEURISTICS.setStatus(
        ""
    )

mcafee_EVENT_QUARANTINED_HEURISTICS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1056)
)
mcafee_EVENT_QUARANTINED_HEURISTICS.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_QUARANTINED_HEURISTICS.setStatus(
        ""
    )

mcafee_EVENT_QUAR_ERROR_HEURISTICS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1057)
)
mcafee_EVENT_QUAR_ERROR_HEURISTICS.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_QUAR_ERROR_HEURISTICS.setStatus(
        ""
    )

mcafee_EVENT_SCAN_TIMEOUT = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1059)
)
mcafee_EVENT_SCAN_TIMEOUT.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_SCAN_TIMEOUT.setStatus(
        ""
    )

mcafee_EVENT_BOOT_SECTOR_CLEANED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1060)
)
mcafee_EVENT_BOOT_SECTOR_CLEANED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_BOOT_SECTOR_CLEANED.setStatus(
        ""
    )

mcafee_EVENT_CLEANERROR_BOOTSECTOR = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1061)
)
mcafee_EVENT_CLEANERROR_BOOTSECTOR.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_CLEANERROR_BOOTSECTOR.setStatus(
        ""
    )

mcafee_EVENT_ALERTERROR = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1062)
)
mcafee_EVENT_ALERTERROR.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_ALERTERROR.setStatus(
        ""
    )

mcafee_EVENT_OPTIONSERROR = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1063)
)
mcafee_EVENT_OPTIONSERROR.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_OPTIONSERROR.setStatus(
        ""
    )

mcafee_EVENT_SERVICE_STARTED_1064 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1064)
)
mcafee_EVENT_SERVICE_STARTED_1064.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_SERVICE_STARTED_1064.setStatus(
        ""
    )

mcafee_EVENT_SERVICE_ENDING_1065 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1065)
)
mcafee_EVENT_SERVICE_ENDING_1065.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_SERVICE_ENDING_1065.setStatus(
        ""
    )

mcafee_EVENT_SCED_START_TASK_OK = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1066)
)
mcafee_EVENT_SCED_START_TASK_OK.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_SCED_START_TASK_OK.setStatus(
        ""
    )

mcafee_EVENT_SCHED_START_TASK_ERROR = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1067)
)
mcafee_EVENT_SCHED_START_TASK_ERROR.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_SCHED_START_TASK_ERROR.setStatus(
        ""
    )

mcafee_EVENT_SCED_TASK_END_OK = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1068)
)
mcafee_EVENT_SCED_TASK_END_OK.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_SCED_TASK_END_OK.setStatus(
        ""
    )

mcafee_EVENT_SCHED_TASK_STOP_ERROR = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1069)
)
mcafee_EVENT_SCHED_TASK_STOP_ERROR.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_SCHED_TASK_STOP_ERROR.setStatus(
        ""
    )

mcafee_EVENT_SCHED_TASK_SUCCESS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1070)
)
mcafee_EVENT_SCHED_TASK_SUCCESS.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_SCHED_TASK_SUCCESS.setStatus(
        ""
    )

mcafee_EVENT_SCHED_TASK_CANCELED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1071)
)
mcafee_EVENT_SCHED_TASK_CANCELED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_SCHED_TASK_CANCELED.setStatus(
        ""
    )

mcafee_EVENT_TASKERR_LOGFILE = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1076)
)
mcafee_EVENT_TASKERR_LOGFILE.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_TASKERR_LOGFILE.setStatus(
        ""
    )

mcafee_EVENT_TASK_ERR_MEMALLOC = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1077)
)
mcafee_EVENT_TASK_ERR_MEMALLOC.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_TASK_ERR_MEMALLOC.setStatus(
        ""
    )

mcafee_EVENT_SCAN_PROC_ERR = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1086)
)
mcafee_EVENT_SCAN_PROC_ERR.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_SCAN_PROC_ERR.setStatus(
        ""
    )

mcafee_EVENT_OAS_START = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1087)
)
mcafee_EVENT_OAS_START.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_OAS_START.setStatus(
        ""
    )

mcafee_EVENT_OAS_STOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1088)
)
mcafee_EVENT_OAS_STOP.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_OAS_STOP.setStatus(
        ""
    )

mcafee_EVENT_SCAN_SETTINGS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1089)
)
mcafee_EVENT_SCAN_SETTINGS.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_SCAN_SETTINGS.setStatus(
        ""
    )

mcafee_EVENT_MACRO_VIRUS_DETECTED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1100)
)
mcafee_EVENT_MACRO_VIRUS_DETECTED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_MACRO_VIRUS_DETECTED.setStatus(
        ""
    )

mcafee_EVENT_MACRO_VIRUS_DELETED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1101)
)
mcafee_EVENT_MACRO_VIRUS_DELETED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_MACRO_VIRUS_DELETED.setStatus(
        ""
    )

mcafee_EVENT_UPDATEOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1118)
)
mcafee_EVENT_UPDATEOK.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_UPDATEOK.setStatus(
        ""
    )

mcafee_EVENT_UPDATEFAILED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1119)
)
mcafee_EVENT_UPDATEFAILED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_UPDATEFAILED.setStatus(
        ""
    )

mcafee_EVENT_UPDATE_RUNNING = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1120)
)
mcafee_EVENT_UPDATE_RUNNING.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_UPDATE_RUNNING.setStatus(
        ""
    )

mcafee_EVENT_UPDATECANCELED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1121)
)
mcafee_EVENT_UPDATECANCELED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_UPDATECANCELED.setStatus(
        ""
    )

mcafee_EVENT_UPGRADE_RUNNING = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1122)
)
mcafee_EVENT_UPGRADE_RUNNING.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_UPGRADE_RUNNING.setStatus(
        ""
    )

mcafee_EVENT_UPGRADE_FAILED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1123)
)
mcafee_EVENT_UPGRADE_FAILED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_UPGRADE_FAILED.setStatus(
        ""
    )

mcafee_EVENT_UPGRADE_CANCELED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1124)
)
mcafee_EVENT_UPGRADE_CANCELED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_UPGRADE_CANCELED.setStatus(
        ""
    )

mcafee_EVENT_UPDATE_VERSION_OLDER = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1125)
)
mcafee_EVENT_UPDATE_VERSION_OLDER.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_UPDATE_VERSION_OLDER.setStatus(
        ""
    )

mcafee_EVENT_SCAN_CANCELED_BY_UPD = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1126)
)
mcafee_EVENT_SCAN_CANCELED_BY_UPD.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_SCAN_CANCELED_BY_UPD.setStatus(
        ""
    )

mcafee_EVENT_SCANNER_DISABLED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1127)
)
mcafee_EVENT_SCANNER_DISABLED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_SCANNER_DISABLED.setStatus(
        ""
    )

mcafee_EVENT_START_PROCESS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1200)
)
mcafee_EVENT_START_PROCESS.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_START_PROCESS.setStatus(
        ""
    )

mcafee_EVENT_PROCESS_ENDED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1201)
)
mcafee_EVENT_PROCESS_ENDED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_PROCESS_ENDED.setStatus(
        ""
    )

mcafee_EVENT_ODS_SCAN_STARTED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1202)
)
mcafee_EVENT_ODS_SCAN_STARTED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_ODS_SCAN_STARTED.setStatus(
        ""
    )

mcafee_EVENT_ODS_SCAN_ENDED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1203)
)
mcafee_EVENT_ODS_SCAN_ENDED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_ODS_SCAN_ENDED.setStatus(
        ""
    )

mcafee_EVENT_SCAN_REPORT_OS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1204)
)
mcafee_EVENT_SCAN_REPORT_OS.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_SCAN_REPORT_OS.setStatus(
        ""
    )

mcafee_EVENT_MAIL_VIRUSCLEANED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1500)
)
mcafee_EVENT_MAIL_VIRUSCLEANED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_MAIL_VIRUSCLEANED.setStatus(
        ""
    )

mcafee_EVENT_MAIL_VIRUSQUARANTINED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1501)
)
mcafee_EVENT_MAIL_VIRUSQUARANTINED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_MAIL_VIRUSQUARANTINED.setStatus(
        ""
    )

mcafee_EVENT_MAIL_VIRUS_NOTCLEANED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1502)
)
mcafee_EVENT_MAIL_VIRUS_NOTCLEANED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_MAIL_VIRUS_NOTCLEANED.setStatus(
        ""
    )

mcafee_EVENT_MAIL_VIRUS_DETECTED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1503)
)
mcafee_EVENT_MAIL_VIRUS_DETECTED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_MAIL_VIRUS_DETECTED.setStatus(
        ""
    )

mcafee_EVENT_MAIL_VIRUS_DELETED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1504)
)
mcafee_EVENT_MAIL_VIRUS_DELETED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_MAIL_VIRUS_DELETED.setStatus(
        ""
    )

mcafee_EVENT_MAIL_VIRUS_FILTERED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1505)
)
mcafee_EVENT_MAIL_VIRUS_FILTERED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_MAIL_VIRUS_FILTERED.setStatus(
        ""
    )

mcafee_EVENT_MAIL_CONTENTBLOCK = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1506)
)
mcafee_EVENT_MAIL_CONTENTBLOCK.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_MAIL_CONTENTBLOCK.setStatus(
        ""
    )

mcafee_EVENT_MAIL_LOWDISKLIMIT = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1507)
)
mcafee_EVENT_MAIL_LOWDISKLIMIT.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_MAIL_LOWDISKLIMIT.setStatus(
        ""
    )

mcafee_EVENT_MAIL_UPPERDISKLIMIT = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1508)
)
mcafee_EVENT_MAIL_UPPERDISKLIMIT.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_MAIL_UPPERDISKLIMIT.setStatus(
        ""
    )

mcafee_EVENT_MAIL_SERVICE_START = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1509)
)
mcafee_EVENT_MAIL_SERVICE_START.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_MAIL_SERVICE_START.setStatus(
        ""
    )

mcafee_EVENT_MAIL_SERVICE_SHUTDOWN_OK = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1510)
)
mcafee_EVENT_MAIL_SERVICE_SHUTDOWN_OK.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_MAIL_SERVICE_SHUTDOWN_OK.setStatus(
        ""
    )

mcafee_EVENT_MAIL_SERVICE_ABEND = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1511)
)
mcafee_EVENT_MAIL_SERVICE_ABEND.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_MAIL_SERVICE_ABEND.setStatus(
        ""
    )

mcafee_EVENT_MAIL_SERVICE_MAX_LOAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1512)
)
mcafee_EVENT_MAIL_SERVICE_MAX_LOAD.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_MAIL_SERVICE_MAX_LOAD.setStatus(
        ""
    )

mcafee_EVENT_MAIL_VIRUS_QUARANTINEDCLEANED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1513)
)
mcafee_EVENT_MAIL_VIRUS_QUARANTINEDCLEANED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_MAIL_VIRUS_QUARANTINEDCLEANED.setStatus(
        ""
    )

mcafee_EVENT_MAIL_VIRUS_QUARANTINED = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1514)
)
mcafee_EVENT_MAIL_VIRUS_QUARANTINED.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_MAIL_VIRUS_QUARANTINED.setStatus(
        ""
    )

mcafee_EVENT_NEW_MIB = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 1900)
)
mcafee_EVENT_NEW_MIB.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_NEW_MIB.setStatus(
        ""
    )

mcafee_EVENT_EPO_FAILE_INSTPRODUCT = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 2201)
)
mcafee_EVENT_EPO_FAILE_INSTPRODUCT.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_EPO_FAILE_INSTPRODUCT.setStatus(
        ""
    )

mcafee_EVENT_EPO_AGENT_RETRYLIMIT = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 2202)
)
mcafee_EVENT_EPO_AGENT_RETRYLIMIT.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_EPO_AGENT_RETRYLIMIT.setStatus(
        ""
    )

mcafee_EVENT_EPO_AGENT_DISKSPACE = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 2204)
)
mcafee_EVENT_EPO_AGENT_DISKSPACE.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_EPO_AGENT_DISKSPACE.setStatus(
        ""
    )

mcafee_EVENT_EPO_SPIPE_DISKSPACE = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 2208)
)
mcafee_EVENT_EPO_SPIPE_DISKSPACE.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_EPO_SPIPE_DISKSPACE.setStatus(
        ""
    )

mcafee_EVENT_EPO_AGENT_WRONG_PLATFORM = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 2216)
)
mcafee_EVENT_EPO_AGENT_WRONG_PLATFORM.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_EPO_AGENT_WRONG_PLATFORM.setStatus(
        ""
    )

mcafee_EVENT_TEST_TRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 12, 0, 0, 9999)
)
mcafee_EVENT_TEST_TRAP.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapShortDescription"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("TVD-MIB", "mcafee_SOURCEIP"),
        ("TVD-MIB", "mcafee_GMTTIME"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapLongDescription"),
        ("NAI-MIB", "naiTrapProblemResolution"),
        ("NAI-MIB", "naiTrapDiagID"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapSourceDNSName"),
        ("TVD-MIB", "mcafee_TIME"),
        ("TVD-MIB", "mcafee_TARGETIP"),
        ("NAI-MIB", "naiTrapTargetDNSName"),
        ("TVD-MIB", "mcafee_TRAPID"),
        ("TVD-MIB", "mcafee_ENGINEVERSION"),
        ("TVD-MIB", "mcafee_DATVERSION"),
        ("TVD-MIB", "mcafee_ENGINESTATUS"),
        ("TVD-MIB", "mcafee_VIRUSNAME"),
        ("TVD-MIB", "mcafee_VIRUSTYPE"),
        ("TVD-MIB", "mcafee_FILENAME"),
        ("TVD-MIB", "mcafee_USERNAME"),
        ("TVD-MIB", "mcafee_OS"),
        ("TVD-MIB", "mcafee_PROCESSORSERIAL"),
        ("TVD-MIB", "mcafee_NUMVIRS"),
        ("TVD-MIB", "mcafee_NUMCLEANED"),
        ("TVD-MIB", "mcafee_NUMDELETED"),
        ("TVD-MIB", "mcafee_NUMQUARANTINED"),
        ("TVD-MIB", "mcafee_SCANRETURNCODE"),
        ("TVD-MIB", "mcafee_MAILFROMNAME"),
        ("TVD-MIB", "mcafee_MAILTONAME"),
        ("TVD-MIB", "mcafee_MAILCCNAME"),
        ("TVD-MIB", "mcafee_MAILSUBJECTLINE"),
        ("TVD-MIB", "mcafee_MAILIDENTIFIERINFO"),
        ("TVD-MIB", "mcafee_LANGUAGECODE"),
        ("TVD-MIB", "mcafee_CLIENTCOMPUTER"),
        ("TVD-MIB", "mcafee_TSCLIENTID"),
        ("TVD-MIB", "mcafee_ACCESSPROCESSNAME"),
        ("TVD-MIB", "mcafee_NOTEID"),
        ("TVD-MIB", "mcafee_NOTESSERVERNAME"),
        ("TVD-MIB", "mcafee_NOTESDBNAME"),
        ("TVD-MIB", "mcafee_DOMAIN"),
        ("TVD-MIB", "mcafee_OBRULE"),
        ("TVD-MIB", "mcafee_EVENTNAME"))
)
if mibBuilder.loadTexts:
    mcafee_EVENT_TEST_TRAP.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TVD-MIB",
    **{"mcafee": mcafee,
       "mcafeeTVDTrap": mcafeeTVDTrap,
       "mcafee_EVENT_VIRFOUND": mcafee_EVENT_VIRFOUND,
       "mcafee_EVENT_FILECLEANED": mcafee_EVENT_FILECLEANED,
       "mcafee_EVENT_FILECLEANERROR": mcafee_EVENT_FILECLEANERROR,
       "mcafee_EVENT_FILEDELETED": mcafee_EVENT_FILEDELETED,
       "mcafee_EVENT_FILEDELETEERROR": mcafee_EVENT_FILEDELETEERROR,
       "mcafee_EVENT_FILEEXCLUDING": mcafee_EVENT_FILEEXCLUDING,
       "mcafee_EVENT_EXCLUDEERR": mcafee_EVENT_EXCLUDEERR,
       "mcafee_EVENT_INFECTION_ACESSDENIED": mcafee_EVENT_INFECTION_ACESSDENIED,
       "mcafee_EVENT_VIRUS_QUARANTINED": mcafee_EVENT_VIRUS_QUARANTINED,
       "mcafee_EVENT_VIRUS_QUARANTINE_FAILURE": mcafee_EVENT_VIRUS_QUARANTINE_FAILURE,
       "mcafee_EVENT_SCANEND_NO_VIRUSES": mcafee_EVENT_SCANEND_NO_VIRUSES,
       "mcafee_EVENT_SCAN_CANCELED": mcafee_EVENT_SCAN_CANCELED,
       "mcafee_EVENT_VIRUS_FOUND_IN_MEMORY": mcafee_EVENT_VIRUS_FOUND_IN_MEMORY,
       "mcafee_EVENT_VIRUS_IN_BOOT_RECORD": mcafee_EVENT_VIRUS_IN_BOOT_RECORD,
       "mcafee_EVENT_SCAN_FOUND_INFECTED_FILES": mcafee_EVENT_SCAN_FOUND_INFECTED_FILES,
       "mcafee_EVENT_SCAN_FOUND_AND_CLEANED_INFECTIONS": mcafee_EVENT_SCAN_FOUND_AND_CLEANED_INFECTIONS,
       "mcafee_EVENT_ALOG_ERROR": mcafee_EVENT_ALOG_ERROR,
       "mcafee_EVENT_MEMALLOC_ERROR": mcafee_EVENT_MEMALLOC_ERROR,
       "mcafee_EVENT_DIR_ACCESS_ERROR": mcafee_EVENT_DIR_ACCESS_ERROR,
       "mcafee_EVENT_WRITE_PROTECT_ERR": mcafee_EVENT_WRITE_PROTECT_ERR,
       "mcafee_EVENT_MEDIA_NOT_FOUND_ERR": mcafee_EVENT_MEDIA_NOT_FOUND_ERR,
       "mcafee_EVENT_SCAN_ITEM_INVALID": mcafee_EVENT_SCAN_ITEM_INVALID,
       "mcafee_EVENT_FILE_IO_ERRORS": mcafee_EVENT_FILE_IO_ERRORS,
       "mcafee_EVENT_DISK_IO_ERR": mcafee_EVENT_DISK_IO_ERR,
       "mcafee_EVENT_GEN_SYSTEM_ERROR": mcafee_EVENT_GEN_SYSTEM_ERROR,
       "mcafee_EVENT_INTERNAL_APP_ERROR": mcafee_EVENT_INTERNAL_APP_ERROR,
       "mcafee_EVENT_INFECTION_PASSWORD_PROTECTED": mcafee_EVENT_INFECTION_PASSWORD_PROTECTED,
       "mcafee_EVENT_NOT_SCANNED_PASSWORD": mcafee_EVENT_NOT_SCANNED_PASSWORD,
       "mcafee_EVENT_INFECTED_BINDARY": mcafee_EVENT_INFECTED_BINDARY,
       "mcafee_EVENT_INFECTED_HEURISTICS": mcafee_EVENT_INFECTED_HEURISTICS,
       "mcafee_EVENT_DELETED_HEURISTICS": mcafee_EVENT_DELETED_HEURISTICS,
       "mcafee_EVENT_DELETE_ERR_HEURISTICS": mcafee_EVENT_DELETE_ERR_HEURISTICS,
       "mcafee_EVENT_QUARANTINED_HEURISTICS": mcafee_EVENT_QUARANTINED_HEURISTICS,
       "mcafee_EVENT_QUAR_ERROR_HEURISTICS": mcafee_EVENT_QUAR_ERROR_HEURISTICS,
       "mcafee_EVENT_SCAN_TIMEOUT": mcafee_EVENT_SCAN_TIMEOUT,
       "mcafee_EVENT_BOOT_SECTOR_CLEANED": mcafee_EVENT_BOOT_SECTOR_CLEANED,
       "mcafee_EVENT_CLEANERROR_BOOTSECTOR": mcafee_EVENT_CLEANERROR_BOOTSECTOR,
       "mcafee_EVENT_ALERTERROR": mcafee_EVENT_ALERTERROR,
       "mcafee_EVENT_OPTIONSERROR": mcafee_EVENT_OPTIONSERROR,
       "mcafee_EVENT_SERVICE_STARTED_1064": mcafee_EVENT_SERVICE_STARTED_1064,
       "mcafee_EVENT_SERVICE_ENDING_1065": mcafee_EVENT_SERVICE_ENDING_1065,
       "mcafee_EVENT_SCED_START_TASK_OK": mcafee_EVENT_SCED_START_TASK_OK,
       "mcafee_EVENT_SCHED_START_TASK_ERROR": mcafee_EVENT_SCHED_START_TASK_ERROR,
       "mcafee_EVENT_SCED_TASK_END_OK": mcafee_EVENT_SCED_TASK_END_OK,
       "mcafee_EVENT_SCHED_TASK_STOP_ERROR": mcafee_EVENT_SCHED_TASK_STOP_ERROR,
       "mcafee_EVENT_SCHED_TASK_SUCCESS": mcafee_EVENT_SCHED_TASK_SUCCESS,
       "mcafee_EVENT_SCHED_TASK_CANCELED": mcafee_EVENT_SCHED_TASK_CANCELED,
       "mcafee_EVENT_TASKERR_LOGFILE": mcafee_EVENT_TASKERR_LOGFILE,
       "mcafee_EVENT_TASK_ERR_MEMALLOC": mcafee_EVENT_TASK_ERR_MEMALLOC,
       "mcafee_EVENT_SCAN_PROC_ERR": mcafee_EVENT_SCAN_PROC_ERR,
       "mcafee_EVENT_OAS_START": mcafee_EVENT_OAS_START,
       "mcafee_EVENT_OAS_STOP": mcafee_EVENT_OAS_STOP,
       "mcafee_EVENT_SCAN_SETTINGS": mcafee_EVENT_SCAN_SETTINGS,
       "mcafee_EVENT_MACRO_VIRUS_DETECTED": mcafee_EVENT_MACRO_VIRUS_DETECTED,
       "mcafee_EVENT_MACRO_VIRUS_DELETED": mcafee_EVENT_MACRO_VIRUS_DELETED,
       "mcafee_EVENT_UPDATEOK": mcafee_EVENT_UPDATEOK,
       "mcafee_EVENT_UPDATEFAILED": mcafee_EVENT_UPDATEFAILED,
       "mcafee_EVENT_UPDATE_RUNNING": mcafee_EVENT_UPDATE_RUNNING,
       "mcafee_EVENT_UPDATECANCELED": mcafee_EVENT_UPDATECANCELED,
       "mcafee_EVENT_UPGRADE_RUNNING": mcafee_EVENT_UPGRADE_RUNNING,
       "mcafee_EVENT_UPGRADE_FAILED": mcafee_EVENT_UPGRADE_FAILED,
       "mcafee_EVENT_UPGRADE_CANCELED": mcafee_EVENT_UPGRADE_CANCELED,
       "mcafee_EVENT_UPDATE_VERSION_OLDER": mcafee_EVENT_UPDATE_VERSION_OLDER,
       "mcafee_EVENT_SCAN_CANCELED_BY_UPD": mcafee_EVENT_SCAN_CANCELED_BY_UPD,
       "mcafee_EVENT_SCANNER_DISABLED": mcafee_EVENT_SCANNER_DISABLED,
       "mcafee_EVENT_START_PROCESS": mcafee_EVENT_START_PROCESS,
       "mcafee_EVENT_PROCESS_ENDED": mcafee_EVENT_PROCESS_ENDED,
       "mcafee_EVENT_ODS_SCAN_STARTED": mcafee_EVENT_ODS_SCAN_STARTED,
       "mcafee_EVENT_ODS_SCAN_ENDED": mcafee_EVENT_ODS_SCAN_ENDED,
       "mcafee_EVENT_SCAN_REPORT_OS": mcafee_EVENT_SCAN_REPORT_OS,
       "mcafee_EVENT_MAIL_VIRUSCLEANED": mcafee_EVENT_MAIL_VIRUSCLEANED,
       "mcafee_EVENT_MAIL_VIRUSQUARANTINED": mcafee_EVENT_MAIL_VIRUSQUARANTINED,
       "mcafee_EVENT_MAIL_VIRUS_NOTCLEANED": mcafee_EVENT_MAIL_VIRUS_NOTCLEANED,
       "mcafee_EVENT_MAIL_VIRUS_DETECTED": mcafee_EVENT_MAIL_VIRUS_DETECTED,
       "mcafee_EVENT_MAIL_VIRUS_DELETED": mcafee_EVENT_MAIL_VIRUS_DELETED,
       "mcafee_EVENT_MAIL_VIRUS_FILTERED": mcafee_EVENT_MAIL_VIRUS_FILTERED,
       "mcafee_EVENT_MAIL_CONTENTBLOCK": mcafee_EVENT_MAIL_CONTENTBLOCK,
       "mcafee_EVENT_MAIL_LOWDISKLIMIT": mcafee_EVENT_MAIL_LOWDISKLIMIT,
       "mcafee_EVENT_MAIL_UPPERDISKLIMIT": mcafee_EVENT_MAIL_UPPERDISKLIMIT,
       "mcafee_EVENT_MAIL_SERVICE_START": mcafee_EVENT_MAIL_SERVICE_START,
       "mcafee_EVENT_MAIL_SERVICE_SHUTDOWN_OK": mcafee_EVENT_MAIL_SERVICE_SHUTDOWN_OK,
       "mcafee_EVENT_MAIL_SERVICE_ABEND": mcafee_EVENT_MAIL_SERVICE_ABEND,
       "mcafee_EVENT_MAIL_SERVICE_MAX_LOAD": mcafee_EVENT_MAIL_SERVICE_MAX_LOAD,
       "mcafee_EVENT_MAIL_VIRUS_QUARANTINEDCLEANED": mcafee_EVENT_MAIL_VIRUS_QUARANTINEDCLEANED,
       "mcafee_EVENT_MAIL_VIRUS_QUARANTINED": mcafee_EVENT_MAIL_VIRUS_QUARANTINED,
       "mcafee_EVENT_NEW_MIB": mcafee_EVENT_NEW_MIB,
       "mcafee_EVENT_EPO_FAILE_INSTPRODUCT": mcafee_EVENT_EPO_FAILE_INSTPRODUCT,
       "mcafee_EVENT_EPO_AGENT_RETRYLIMIT": mcafee_EVENT_EPO_AGENT_RETRYLIMIT,
       "mcafee_EVENT_EPO_AGENT_DISKSPACE": mcafee_EVENT_EPO_AGENT_DISKSPACE,
       "mcafee_EVENT_EPO_SPIPE_DISKSPACE": mcafee_EVENT_EPO_SPIPE_DISKSPACE,
       "mcafee_EVENT_EPO_AGENT_WRONG_PLATFORM": mcafee_EVENT_EPO_AGENT_WRONG_PLATFORM,
       "mcafee_EVENT_TEST_TRAP": mcafee_EVENT_TEST_TRAP,
       "mcafeeStandardTrapField": mcafeeStandardTrapField,
       "mcafee_TRAPID": mcafee_TRAPID,
       "mcafee_ENGINEVERSION": mcafee_ENGINEVERSION,
       "mcafee_DATVERSION": mcafee_DATVERSION,
       "mcafee_ENGINESTATUS": mcafee_ENGINESTATUS,
       "mcafee_VIRUSNAME": mcafee_VIRUSNAME,
       "mcafee_VIRUSTYPE": mcafee_VIRUSTYPE,
       "mcafee_FILENAME": mcafee_FILENAME,
       "mcafee_USERNAME": mcafee_USERNAME,
       "mcafee_OS": mcafee_OS,
       "mcafee_PROCESSORSERIAL": mcafee_PROCESSORSERIAL,
       "mcafee_TASKNAME": mcafee_TASKNAME,
       "mcafee_NUMVIRS": mcafee_NUMVIRS,
       "mcafee_NUMCLEANED": mcafee_NUMCLEANED,
       "mcafee_NUMDELETED": mcafee_NUMDELETED,
       "mcafee_NUMQUARANTINED": mcafee_NUMQUARANTINED,
       "mcafee_SCANRETURNCODE": mcafee_SCANRETURNCODE,
       "mcafee_MAILFROMNAME": mcafee_MAILFROMNAME,
       "mcafee_MAILTONAME": mcafee_MAILTONAME,
       "mcafee_MAILCCNAME": mcafee_MAILCCNAME,
       "mcafee_MAILSUBJECTLINE": mcafee_MAILSUBJECTLINE,
       "mcafee_MAILIDENTIFIERINFO": mcafee_MAILIDENTIFIERINFO,
       "mcafee_NOTEID": mcafee_NOTEID,
       "mcafee_NOTESSERVERNAME": mcafee_NOTESSERVERNAME,
       "mcafee_NOTESDBNAME": mcafee_NOTESDBNAME,
       "mcafee_DOMAIN": mcafee_DOMAIN,
       "mcafee_OBRULE": mcafee_OBRULE,
       "mcafee_LANGUAGECODE": mcafee_LANGUAGECODE,
       "mcafee_CLIENTCOMPUTER": mcafee_CLIENTCOMPUTER,
       "mcafee_TSCLIENTID": mcafee_TSCLIENTID,
       "mcafee_ACCESSPROCESSNAME": mcafee_ACCESSPROCESSNAME,
       "mcafee_EVENTNAME": mcafee_EVENTNAME,
       "mcafee_GMTTIME": mcafee_GMTTIME,
       "mcafee_TIME": mcafee_TIME,
       "mcafee_SOURCEIP": mcafee_SOURCEIP,
       "mcafee_TARGETIP": mcafee_TARGETIP}
)
