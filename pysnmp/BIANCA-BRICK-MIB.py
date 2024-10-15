# SNMP MIB module (BIANCA-BRICK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:33 2024
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

(sysDescr,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr",
    "sysName")

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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""




class Date(Integer32):
    """Custom type Date based on Integer32"""




class HexValue(Integer32):
    """Custom type HexValue based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Admin_ObjectIdentity = ObjectIdentity
admin = _Admin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 1)
)


class _BiboAdmTrapCommunity_Type(DisplayString):
    """Custom type biboAdmTrapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BiboAdmTrapCommunity_Type.__name__ = "DisplayString"
_BiboAdmTrapCommunity_Object = MibScalar
biboAdmTrapCommunity = _BiboAdmTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 4),
    _BiboAdmTrapCommunity_Type()
)
biboAdmTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmTrapCommunity.setStatus("mandatory")


class _BiboAdmSnmpVersion_Type(Integer32):
    """Custom type biboAdmSnmpVersion based on Integer32"""
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
        *(("version1", 1),
          ("version1-compat", 2),
          ("version1p1", 3),
          ("version1p1-auto", 5),
          ("version1p1-compat", 4))
    )


_BiboAdmSnmpVersion_Type.__name__ = "Integer32"
_BiboAdmSnmpVersion_Object = MibScalar
biboAdmSnmpVersion = _BiboAdmSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 5),
    _BiboAdmSnmpVersion_Type()
)
biboAdmSnmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmSnmpVersion.setStatus("mandatory")
_BiboAdmSnmpPort_Type = Integer32
_BiboAdmSnmpPort_Object = MibScalar
biboAdmSnmpPort = _BiboAdmSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 6),
    _BiboAdmSnmpPort_Type()
)
biboAdmSnmpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmSnmpPort.setStatus("mandatory")
_BiboAdmSnmpTrapPort_Type = Integer32
_BiboAdmSnmpTrapPort_Object = MibScalar
biboAdmSnmpTrapPort = _BiboAdmSnmpTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 7),
    _BiboAdmSnmpTrapPort_Type()
)
biboAdmSnmpTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmSnmpTrapPort.setStatus("mandatory")
_BiboAdmIpAddr_Type = IpAddress
_BiboAdmIpAddr_Object = MibScalar
biboAdmIpAddr = _BiboAdmIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 8),
    _BiboAdmIpAddr_Type()
)
biboAdmIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmIpAddr.setStatus("mandatory")


class _BiboAdmTrapBrdCast_Type(Integer32):
    """Custom type biboAdmTrapBrdCast based on Integer32"""
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


_BiboAdmTrapBrdCast_Type.__name__ = "Integer32"
_BiboAdmTrapBrdCast_Object = MibScalar
biboAdmTrapBrdCast = _BiboAdmTrapBrdCast_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 9),
    _BiboAdmTrapBrdCast_Type()
)
biboAdmTrapBrdCast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmTrapBrdCast.setStatus("mandatory")
_BiboAdmTrapHostTable_Object = MibTable
biboAdmTrapHostTable = _BiboAdmTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 10)
)
if mibBuilder.loadTexts:
    biboAdmTrapHostTable.setStatus("mandatory")
_BiboAdmTrapHostEntry_Object = MibTableRow
biboAdmTrapHostEntry = _BiboAdmTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 10, 1)
)
biboAdmTrapHostEntry.setIndexNames(
    (0, "BIANCA-BRICK-MIB", "biboAdmTrapHostAddr"),
)
if mibBuilder.loadTexts:
    biboAdmTrapHostEntry.setStatus("mandatory")
_BiboAdmTrapHostAddr_Type = IpAddress
_BiboAdmTrapHostAddr_Object = MibTableColumn
biboAdmTrapHostAddr = _BiboAdmTrapHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 10, 1, 1),
    _BiboAdmTrapHostAddr_Type()
)
biboAdmTrapHostAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmTrapHostAddr.setStatus("mandatory")


class _BiboAdmTrapHostStatus_Type(Integer32):
    """Custom type biboAdmTrapHostStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("valid", 1))
    )


_BiboAdmTrapHostStatus_Type.__name__ = "Integer32"
_BiboAdmTrapHostStatus_Object = MibTableColumn
biboAdmTrapHostStatus = _BiboAdmTrapHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 10, 1, 2),
    _BiboAdmTrapHostStatus_Type()
)
biboAdmTrapHostStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmTrapHostStatus.setStatus("mandatory")
_BiboAdmSyslogMaxEntries_Type = Integer32
_BiboAdmSyslogMaxEntries_Object = MibScalar
biboAdmSyslogMaxEntries = _BiboAdmSyslogMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 11),
    _BiboAdmSyslogMaxEntries_Type()
)
biboAdmSyslogMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmSyslogMaxEntries.setStatus("mandatory")
_BiboAdmSyslogTable_Object = MibTable
biboAdmSyslogTable = _BiboAdmSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 12)
)
if mibBuilder.loadTexts:
    biboAdmSyslogTable.setStatus("mandatory")
_BiboAdmSyslogEntry_Object = MibTableRow
biboAdmSyslogEntry = _BiboAdmSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 12, 1)
)
biboAdmSyslogEntry.setIndexNames(
    (0, "BIANCA-BRICK-MIB", "biboAdmSyslogTimeStamp"),
    (0, "BIANCA-BRICK-MIB", "biboAdmSyslogLevel"),
)
if mibBuilder.loadTexts:
    biboAdmSyslogEntry.setStatus("mandatory")
_BiboAdmSyslogTimeStamp_Type = Date
_BiboAdmSyslogTimeStamp_Object = MibTableColumn
biboAdmSyslogTimeStamp = _BiboAdmSyslogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 12, 1, 1),
    _BiboAdmSyslogTimeStamp_Type()
)
biboAdmSyslogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmSyslogTimeStamp.setStatus("mandatory")


class _BiboAdmSyslogLevel_Type(Integer32):
    """Custom type biboAdmSyslogLevel based on Integer32"""
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
          ("crit", 3),
          ("debug", 8),
          ("emerg", 1),
          ("err", 4),
          ("info", 7),
          ("notice", 6),
          ("warning", 5))
    )


_BiboAdmSyslogLevel_Type.__name__ = "Integer32"
_BiboAdmSyslogLevel_Object = MibTableColumn
biboAdmSyslogLevel = _BiboAdmSyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 12, 1, 2),
    _BiboAdmSyslogLevel_Type()
)
biboAdmSyslogLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmSyslogLevel.setStatus("mandatory")
_BiboAdmSyslogMessage_Type = DisplayString
_BiboAdmSyslogMessage_Object = MibTableColumn
biboAdmSyslogMessage = _BiboAdmSyslogMessage_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 12, 1, 4),
    _BiboAdmSyslogMessage_Type()
)
biboAdmSyslogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmSyslogMessage.setStatus("mandatory")


class _BiboAdmSyslogSubject_Type(Integer32):
    """Custom type biboAdmSyslogSubject based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("acct", 1),
          ("atm", 20),
          ("bridge", 8),
          ("capi", 6),
          ("config", 9),
          ("ether", 13),
          ("fr", 17),
          ("inet", 3),
          ("ipsec", 22),
          ("ipx", 5),
          ("isdn", 2),
          ("modem", 18),
          ("ospf", 16),
          ("pabx", 21),
          ("ppp", 7),
          ("radius", 14),
          ("rip", 19),
          ("snmp", 10),
          ("tapi", 15),
          ("token", 12),
          ("x21", 11),
          ("x25", 4))
    )


_BiboAdmSyslogSubject_Type.__name__ = "Integer32"
_BiboAdmSyslogSubject_Object = MibTableColumn
biboAdmSyslogSubject = _BiboAdmSyslogSubject_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 12, 1, 5),
    _BiboAdmSyslogSubject_Type()
)
biboAdmSyslogSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmSyslogSubject.setStatus("mandatory")
_BiboAdmLogHostTable_Object = MibTable
biboAdmLogHostTable = _BiboAdmLogHostTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 13)
)
if mibBuilder.loadTexts:
    biboAdmLogHostTable.setStatus("mandatory")
_BiboAdmLogHostEntry_Object = MibTableRow
biboAdmLogHostEntry = _BiboAdmLogHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 13, 1)
)
biboAdmLogHostEntry.setIndexNames(
    (0, "BIANCA-BRICK-MIB", "biboAdmLogHostAddr"),
)
if mibBuilder.loadTexts:
    biboAdmLogHostEntry.setStatus("mandatory")
_BiboAdmLogHostAddr_Type = IpAddress
_BiboAdmLogHostAddr_Object = MibTableColumn
biboAdmLogHostAddr = _BiboAdmLogHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 13, 1, 1),
    _BiboAdmLogHostAddr_Type()
)
biboAdmLogHostAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmLogHostAddr.setStatus("mandatory")


class _BiboAdmLogHostLevel_Type(Integer32):
    """Custom type biboAdmLogHostLevel based on Integer32"""
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
        *(("alert", 2),
          ("crit", 3),
          ("debug", 8),
          ("delete", 9),
          ("emerg", 1),
          ("err", 4),
          ("info", 7),
          ("notice", 6),
          ("warning", 5))
    )


_BiboAdmLogHostLevel_Type.__name__ = "Integer32"
_BiboAdmLogHostLevel_Object = MibTableColumn
biboAdmLogHostLevel = _BiboAdmLogHostLevel_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 13, 1, 2),
    _BiboAdmLogHostLevel_Type()
)
biboAdmLogHostLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmLogHostLevel.setStatus("mandatory")


class _BiboAdmLogHostFacility_Type(Integer32):
    """Custom type biboAdmLogHostFacility based on Integer32"""
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
        *(("local0", 1),
          ("local1", 2),
          ("local2", 3),
          ("local3", 4),
          ("local4", 5),
          ("local5", 6),
          ("local6", 7),
          ("local7", 8))
    )


_BiboAdmLogHostFacility_Type.__name__ = "Integer32"
_BiboAdmLogHostFacility_Object = MibTableColumn
biboAdmLogHostFacility = _BiboAdmLogHostFacility_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 13, 1, 4),
    _BiboAdmLogHostFacility_Type()
)
biboAdmLogHostFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmLogHostFacility.setStatus("mandatory")


class _BiboAdmLogHostType_Type(Integer32):
    """Custom type biboAdmLogHostType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acct", 2),
          ("all", 3),
          ("system", 1))
    )


_BiboAdmLogHostType_Type.__name__ = "Integer32"
_BiboAdmLogHostType_Object = MibTableColumn
biboAdmLogHostType = _BiboAdmLogHostType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 13, 1, 5),
    _BiboAdmLogHostType_Type()
)
biboAdmLogHostType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmLogHostType.setStatus("mandatory")


class _BiboAdmLogHostTimestamp_Type(Integer32):
    """Custom type biboAdmLogHostTimestamp based on Integer32"""
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
          ("none", 1),
          ("time", 2))
    )


_BiboAdmLogHostTimestamp_Type.__name__ = "Integer32"
_BiboAdmLogHostTimestamp_Object = MibTableColumn
biboAdmLogHostTimestamp = _BiboAdmLogHostTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 13, 1, 6),
    _BiboAdmLogHostTimestamp_Type()
)
biboAdmLogHostTimestamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmLogHostTimestamp.setStatus("mandatory")
_BiboAdmConfigTable_Object = MibTable
biboAdmConfigTable = _BiboAdmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 14)
)
if mibBuilder.loadTexts:
    biboAdmConfigTable.setStatus("mandatory")
_BiboAdmConfigEntry_Object = MibTableRow
biboAdmConfigEntry = _BiboAdmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 14, 1)
)
biboAdmConfigEntry.setIndexNames(
    (0, "BIANCA-BRICK-MIB", "biboAdmConfigCmd"),
)
if mibBuilder.loadTexts:
    biboAdmConfigEntry.setStatus("mandatory")


class _BiboAdmConfigCmd_Type(Integer32):
    """Custom type biboAdmConfigCmd based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("copy", 8),
          ("delete", 6),
          ("get", 4),
          ("load", 2),
          ("move", 7),
          ("put", 3),
          ("reboot", 9),
          ("reorg", 10),
          ("save", 1),
          ("state", 5))
    )


_BiboAdmConfigCmd_Type.__name__ = "Integer32"
_BiboAdmConfigCmd_Object = MibTableColumn
biboAdmConfigCmd = _BiboAdmConfigCmd_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 14, 1, 1),
    _BiboAdmConfigCmd_Type()
)
biboAdmConfigCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmConfigCmd.setStatus("mandatory")
_BiboAdmConfigObject_Type = ObjectIdentifier
_BiboAdmConfigObject_Object = MibTableColumn
biboAdmConfigObject = _BiboAdmConfigObject_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 14, 1, 2),
    _BiboAdmConfigObject_Type()
)
biboAdmConfigObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmConfigObject.setStatus("mandatory")
_BiboAdmConfigPath_Type = DisplayString
_BiboAdmConfigPath_Object = MibTableColumn
biboAdmConfigPath = _BiboAdmConfigPath_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 14, 1, 3),
    _BiboAdmConfigPath_Type()
)
biboAdmConfigPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmConfigPath.setStatus("mandatory")
_BiboAdmConfigPathNew_Type = DisplayString
_BiboAdmConfigPathNew_Object = MibTableColumn
biboAdmConfigPathNew = _BiboAdmConfigPathNew_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 14, 1, 4),
    _BiboAdmConfigPathNew_Type()
)
biboAdmConfigPathNew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmConfigPathNew.setStatus("mandatory")
_BiboAdmConfigHost_Type = IpAddress
_BiboAdmConfigHost_Object = MibTableColumn
biboAdmConfigHost = _BiboAdmConfigHost_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 14, 1, 5),
    _BiboAdmConfigHost_Type()
)
biboAdmConfigHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmConfigHost.setStatus("mandatory")


class _BiboAdmConfigState_Type(Integer32):
    """Custom type biboAdmConfigState based on Integer32"""
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
        *(("done", 3),
          ("error", 4),
          ("running", 2),
          ("todo", 1))
    )


_BiboAdmConfigState_Type.__name__ = "Integer32"
_BiboAdmConfigState_Object = MibTableColumn
biboAdmConfigState = _BiboAdmConfigState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 14, 1, 6),
    _BiboAdmConfigState_Type()
)
biboAdmConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmConfigState.setStatus("mandatory")
_BiboAdmConfigFile_Type = DisplayString
_BiboAdmConfigFile_Object = MibTableColumn
biboAdmConfigFile = _BiboAdmConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 14, 1, 7),
    _BiboAdmConfigFile_Type()
)
biboAdmConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmConfigFile.setStatus("mandatory")
_BiboAdmConfigDirTable_Object = MibTable
biboAdmConfigDirTable = _BiboAdmConfigDirTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 15)
)
if mibBuilder.loadTexts:
    biboAdmConfigDirTable.setStatus("mandatory")
_BiboAdmConfigDirEntry_Object = MibTableRow
biboAdmConfigDirEntry = _BiboAdmConfigDirEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 15, 1)
)
biboAdmConfigDirEntry.setIndexNames(
    (0, "BIANCA-BRICK-MIB", "biboAdmConfigDirName"),
)
if mibBuilder.loadTexts:
    biboAdmConfigDirEntry.setStatus("mandatory")
_BiboAdmConfigDirName_Type = DisplayString
_BiboAdmConfigDirName_Object = MibTableColumn
biboAdmConfigDirName = _BiboAdmConfigDirName_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 15, 1, 1),
    _BiboAdmConfigDirName_Type()
)
biboAdmConfigDirName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmConfigDirName.setStatus("mandatory")
_BiboAdmConfigDirCount_Type = Integer32
_BiboAdmConfigDirCount_Object = MibTableColumn
biboAdmConfigDirCount = _BiboAdmConfigDirCount_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 15, 1, 2),
    _BiboAdmConfigDirCount_Type()
)
biboAdmConfigDirCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmConfigDirCount.setStatus("mandatory")
_BiboAdmConfigDirContent_Type = DisplayString
_BiboAdmConfigDirContent_Object = MibTableColumn
biboAdmConfigDirContent = _BiboAdmConfigDirContent_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 15, 1, 3),
    _BiboAdmConfigDirContent_Type()
)
biboAdmConfigDirContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmConfigDirContent.setStatus("mandatory")
_BiboAdmBoardTable_Object = MibTable
biboAdmBoardTable = _BiboAdmBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 17)
)
if mibBuilder.loadTexts:
    biboAdmBoardTable.setStatus("mandatory")
_BiboAdmBoardEntry_Object = MibTableRow
biboAdmBoardEntry = _BiboAdmBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 17, 1)
)
biboAdmBoardEntry.setIndexNames(
    (0, "BIANCA-BRICK-MIB", "biboABrdSlot"),
    (0, "BIANCA-BRICK-MIB", "biboABrdUnit"),
)
if mibBuilder.loadTexts:
    biboAdmBoardEntry.setStatus("mandatory")


class _BiboABrdSlot_Type(Integer32):
    """Custom type biboABrdSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_BiboABrdSlot_Type.__name__ = "Integer32"
_BiboABrdSlot_Object = MibTableColumn
biboABrdSlot = _BiboABrdSlot_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 17, 1, 1),
    _BiboABrdSlot_Type()
)
biboABrdSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboABrdSlot.setStatus("mandatory")
_BiboABrdType_Type = DisplayString
_BiboABrdType_Object = MibTableColumn
biboABrdType = _BiboABrdType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 17, 1, 2),
    _BiboABrdType_Type()
)
biboABrdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboABrdType.setStatus("mandatory")
_BiboABrdHWRelease_Type = DisplayString
_BiboABrdHWRelease_Object = MibTableColumn
biboABrdHWRelease = _BiboABrdHWRelease_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 17, 1, 3),
    _BiboABrdHWRelease_Type()
)
biboABrdHWRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboABrdHWRelease.setStatus("mandatory")
_BiboABrdFWRelease_Type = DisplayString
_BiboABrdFWRelease_Object = MibTableColumn
biboABrdFWRelease = _BiboABrdFWRelease_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 17, 1, 4),
    _BiboABrdFWRelease_Type()
)
biboABrdFWRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboABrdFWRelease.setStatus("mandatory")
_BiboABrdPartNo_Type = DisplayString
_BiboABrdPartNo_Object = MibTableColumn
biboABrdPartNo = _BiboABrdPartNo_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 17, 1, 5),
    _BiboABrdPartNo_Type()
)
biboABrdPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboABrdPartNo.setStatus("mandatory")


class _BiboABrdConnector_Type(Integer32):
    """Custom type biboABrdConnector based on Integer32"""
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
        *(("auto", 1),
          ("bnc", 3),
          ("rj45", 2),
          ("rj45-100mbit-fdup", 8),
          ("rj45-100mbit-hdup", 7),
          ("rj45-10mbit-fdup", 6),
          ("rj45-10mbit-hdup", 5),
          ("subd15", 4))
    )


_BiboABrdConnector_Type.__name__ = "Integer32"
_BiboABrdConnector_Object = MibTableColumn
biboABrdConnector = _BiboABrdConnector_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 17, 1, 6),
    _BiboABrdConnector_Type()
)
biboABrdConnector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboABrdConnector.setStatus("mandatory")


class _BiboABrdUnit_Type(Integer32):
    """Custom type biboABrdUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_BiboABrdUnit_Type.__name__ = "Integer32"
_BiboABrdUnit_Object = MibTableColumn
biboABrdUnit = _BiboABrdUnit_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 17, 1, 7),
    _BiboABrdUnit_Type()
)
biboABrdUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboABrdUnit.setStatus("mandatory")
_BiboABrdSerialNo_Type = DisplayString
_BiboABrdSerialNo_Object = MibTableColumn
biboABrdSerialNo = _BiboABrdSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 17, 1, 8),
    _BiboABrdSerialNo_Type()
)
biboABrdSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboABrdSerialNo.setStatus("mandatory")
_BiboAdmUsrTrapTable_Object = MibTable
biboAdmUsrTrapTable = _BiboAdmUsrTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 18)
)
if mibBuilder.loadTexts:
    biboAdmUsrTrapTable.setStatus("mandatory")
_BiboAdmUsrTrapEntry_Object = MibTableRow
biboAdmUsrTrapEntry = _BiboAdmUsrTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 18, 1)
)
biboAdmUsrTrapEntry.setIndexNames(
    (0, "BIANCA-BRICK-MIB", "biboATrpObj"),
)
if mibBuilder.loadTexts:
    biboAdmUsrTrapEntry.setStatus("mandatory")
_BiboATrpObj_Type = ObjectIdentifier
_BiboATrpObj_Object = MibTableColumn
biboATrpObj = _BiboATrpObj_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 18, 1, 1),
    _BiboATrpObj_Type()
)
biboATrpObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboATrpObj.setStatus("mandatory")


class _BiboATrpStatus_Type(Integer32):
    """Custom type biboATrpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("valid", 1))
    )


_BiboATrpStatus_Type.__name__ = "Integer32"
_BiboATrpStatus_Object = MibTableColumn
biboATrpStatus = _BiboATrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 18, 1, 2),
    _BiboATrpStatus_Type()
)
biboATrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboATrpStatus.setStatus("mandatory")
_BiboAdmDomainName_Type = DisplayString
_BiboAdmDomainName_Object = MibScalar
biboAdmDomainName = _BiboAdmDomainName_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 19),
    _BiboAdmDomainName_Type()
)
biboAdmDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmDomainName.setStatus("mandatory")
_BiboAdmNameServer_Type = IpAddress
_BiboAdmNameServer_Object = MibScalar
biboAdmNameServer = _BiboAdmNameServer_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 20),
    _BiboAdmNameServer_Type()
)
biboAdmNameServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmNameServer.setStatus("mandatory")
_BiboAdmNameServ2_Type = IpAddress
_BiboAdmNameServ2_Object = MibScalar
biboAdmNameServ2 = _BiboAdmNameServ2_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 21),
    _BiboAdmNameServ2_Type()
)
biboAdmNameServ2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmNameServ2.setStatus("mandatory")


class _BiboAdmBridgeEnable_Type(Integer32):
    """Custom type biboAdmBridgeEnable based on Integer32"""
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


_BiboAdmBridgeEnable_Type.__name__ = "Integer32"
_BiboAdmBridgeEnable_Object = MibScalar
biboAdmBridgeEnable = _BiboAdmBridgeEnable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 22),
    _BiboAdmBridgeEnable_Type()
)
biboAdmBridgeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmBridgeEnable.setStatus("mandatory")
_BiboAdmCapiTcpPort_Type = Integer32
_BiboAdmCapiTcpPort_Object = MibScalar
biboAdmCapiTcpPort = _BiboAdmCapiTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 23),
    _BiboAdmCapiTcpPort_Type()
)
biboAdmCapiTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmCapiTcpPort.setStatus("mandatory")
_BiboAdmTraceTcpPort_Type = Integer32
_BiboAdmTraceTcpPort_Object = MibScalar
biboAdmTraceTcpPort = _BiboAdmTraceTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 24),
    _BiboAdmTraceTcpPort_Type()
)
biboAdmTraceTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmTraceTcpPort.setStatus("mandatory")
_BiboAdmRipUdpPort_Type = Integer32
_BiboAdmRipUdpPort_Object = MibScalar
biboAdmRipUdpPort = _BiboAdmRipUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 25),
    _BiboAdmRipUdpPort_Type()
)
biboAdmRipUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmRipUdpPort.setStatus("mandatory")


class _BiboAdmSWVersion_Type(DisplayString):
    """Custom type biboAdmSWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BiboAdmSWVersion_Type.__name__ = "DisplayString"
_BiboAdmSWVersion_Object = MibScalar
biboAdmSWVersion = _BiboAdmSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 26),
    _BiboAdmSWVersion_Type()
)
biboAdmSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmSWVersion.setStatus("mandatory")
_BiboAdmTimeServer_Type = IpAddress
_BiboAdmTimeServer_Object = MibScalar
biboAdmTimeServer = _BiboAdmTimeServer_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 27),
    _BiboAdmTimeServer_Type()
)
biboAdmTimeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmTimeServer.setStatus("mandatory")
_BiboAdmTimeOffset_Type = Integer32
_BiboAdmTimeOffset_Object = MibScalar
biboAdmTimeOffset = _BiboAdmTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 28),
    _BiboAdmTimeOffset_Type()
)
biboAdmTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmTimeOffset.setStatus("mandatory")


class _BiboAdmConsoleSyslog_Type(Integer32):
    """Custom type biboAdmConsoleSyslog based on Integer32"""
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


_BiboAdmConsoleSyslog_Type.__name__ = "Integer32"
_BiboAdmConsoleSyslog_Object = MibScalar
biboAdmConsoleSyslog = _BiboAdmConsoleSyslog_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 29),
    _BiboAdmConsoleSyslog_Type()
)
biboAdmConsoleSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmConsoleSyslog.setStatus("mandatory")


class _BiboAdmSyslogTableLevel_Type(Integer32):
    """Custom type biboAdmSyslogTableLevel based on Integer32"""
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
          ("crit", 3),
          ("debug", 8),
          ("emerg", 1),
          ("err", 4),
          ("info", 7),
          ("notice", 6),
          ("warning", 5))
    )


_BiboAdmSyslogTableLevel_Type.__name__ = "Integer32"
_BiboAdmSyslogTableLevel_Object = MibScalar
biboAdmSyslogTableLevel = _BiboAdmSyslogTableLevel_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 30),
    _BiboAdmSyslogTableLevel_Type()
)
biboAdmSyslogTableLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmSyslogTableLevel.setStatus("mandatory")
_BiboAdmSystemId_Type = DisplayString
_BiboAdmSystemId_Object = MibScalar
biboAdmSystemId = _BiboAdmSystemId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 31),
    _BiboAdmSystemId_Type()
)
biboAdmSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmSystemId.setStatus("mandatory")
_BiboAdmLicInfoTable_Object = MibTable
biboAdmLicInfoTable = _BiboAdmLicInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 32)
)
if mibBuilder.loadTexts:
    biboAdmLicInfoTable.setStatus("mandatory")
_BiboAdmLicInfoEntry_Object = MibTableRow
biboAdmLicInfoEntry = _BiboAdmLicInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 32, 1)
)
biboAdmLicInfoEntry.setIndexNames(
    (0, "BIANCA-BRICK-MIB", "biboAdmLicInfoType"),
    (0, "BIANCA-BRICK-MIB", "biboAdmLicInfoStatus"),
)
if mibBuilder.loadTexts:
    biboAdmLicInfoEntry.setStatus("mandatory")


class _BiboAdmLicInfoType_Type(Integer32):
    """Custom type biboAdmLicInfoType based on Integer32"""
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
              33,
              128,
              129,
              130,
              131,
              132)
        )
    )
    namedValues = NamedValues(
        *(("bri", 129),
          ("bridge", 3),
          ("capi", 2),
          ("ethernet", 128),
          ("extended-lan", 10),
          ("extended-wan", 13),
          ("frame-relay", 7),
          ("g703", 130),
          ("ip", 1),
          ("ipsec", 33),
          ("ipx", 5),
          ("leased-line", 14),
          ("modem", 132),
          ("ospf", 9),
          ("pri", 131),
          ("stac", 6),
          ("taf", 12),
          ("tapi", 8),
          ("tunneling", 11),
          ("x25", 4))
    )


_BiboAdmLicInfoType_Type.__name__ = "Integer32"
_BiboAdmLicInfoType_Object = MibTableColumn
biboAdmLicInfoType = _BiboAdmLicInfoType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 32, 1, 1),
    _BiboAdmLicInfoType_Type()
)
biboAdmLicInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmLicInfoType.setStatus("mandatory")


class _BiboAdmLicInfoStatus_Type(Integer32):
    """Custom type biboAdmLicInfoStatus based on Integer32"""
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
        *(("builtin", 1),
          ("erase-internal", 5),
          ("invalid-license", 3),
          ("no-license", 4),
          ("valid-license", 2))
    )


_BiboAdmLicInfoStatus_Type.__name__ = "Integer32"
_BiboAdmLicInfoStatus_Object = MibTableColumn
biboAdmLicInfoStatus = _BiboAdmLicInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 32, 1, 2),
    _BiboAdmLicInfoStatus_Type()
)
biboAdmLicInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmLicInfoStatus.setStatus("mandatory")
_BiboAdmLicInfoId_Type = DisplayString
_BiboAdmLicInfoId_Object = MibTableColumn
biboAdmLicInfoId = _BiboAdmLicInfoId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 32, 1, 3),
    _BiboAdmLicInfoId_Type()
)
biboAdmLicInfoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmLicInfoId.setStatus("mandatory")


class _BiboAdmLicInfoSlot_Type(Integer32):
    """Custom type biboAdmLicInfoSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BiboAdmLicInfoSlot_Type.__name__ = "Integer32"
_BiboAdmLicInfoSlot_Object = MibTableColumn
biboAdmLicInfoSlot = _BiboAdmLicInfoSlot_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 32, 1, 4),
    _BiboAdmLicInfoSlot_Type()
)
biboAdmLicInfoSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmLicInfoSlot.setStatus("mandatory")
_BiboAdmLicInfoMaxLic_Type = Counter32
_BiboAdmLicInfoMaxLic_Object = MibTableColumn
biboAdmLicInfoMaxLic = _BiboAdmLicInfoMaxLic_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 32, 1, 5),
    _BiboAdmLicInfoMaxLic_Type()
)
biboAdmLicInfoMaxLic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmLicInfoMaxLic.setStatus("mandatory")
_BiboAdmLicInfoInUse_Type = Counter32
_BiboAdmLicInfoInUse_Object = MibTableColumn
biboAdmLicInfoInUse = _BiboAdmLicInfoInUse_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 32, 1, 6),
    _BiboAdmLicInfoInUse_Type()
)
biboAdmLicInfoInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmLicInfoInUse.setStatus("mandatory")
_BiboAdmLicInfoHwSerial_Type = DisplayString
_BiboAdmLicInfoHwSerial_Object = MibTableColumn
biboAdmLicInfoHwSerial = _BiboAdmLicInfoHwSerial_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 32, 1, 7),
    _BiboAdmLicInfoHwSerial_Type()
)
biboAdmLicInfoHwSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmLicInfoHwSerial.setStatus("mandatory")


class _BiboAdmLicInfoUnit_Type(Integer32):
    """Custom type biboAdmLicInfoUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BiboAdmLicInfoUnit_Type.__name__ = "Integer32"
_BiboAdmLicInfoUnit_Object = MibTableColumn
biboAdmLicInfoUnit = _BiboAdmLicInfoUnit_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 32, 1, 8),
    _BiboAdmLicInfoUnit_Type()
)
biboAdmLicInfoUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmLicInfoUnit.setStatus("mandatory")
_BiboAdmBootpRelayServer_Type = IpAddress
_BiboAdmBootpRelayServer_Object = MibScalar
biboAdmBootpRelayServer = _BiboAdmBootpRelayServer_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 33),
    _BiboAdmBootpRelayServer_Type()
)
biboAdmBootpRelayServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmBootpRelayServer.setStatus("mandatory")
_BiboAdmRadiusServer_Type = IpAddress
_BiboAdmRadiusServer_Object = MibScalar
biboAdmRadiusServer = _BiboAdmRadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 34),
    _BiboAdmRadiusServer_Type()
)
biboAdmRadiusServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmRadiusServer.setStatus("mandatory")
_BiboAdmLocalPPPIdent_Type = DisplayString
_BiboAdmLocalPPPIdent_Object = MibScalar
biboAdmLocalPPPIdent = _BiboAdmLocalPPPIdent_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 35),
    _BiboAdmLocalPPPIdent_Type()
)
biboAdmLocalPPPIdent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmLocalPPPIdent.setStatus("mandatory")
_BiboAdmHttpTcpPort_Type = Integer32
_BiboAdmHttpTcpPort_Object = MibScalar
biboAdmHttpTcpPort = _BiboAdmHttpTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 36),
    _BiboAdmHttpTcpPort_Type()
)
biboAdmHttpTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmHttpTcpPort.setStatus("mandatory")
_BiboAdmTapiTcpPort_Type = Integer32
_BiboAdmTapiTcpPort_Object = MibScalar
biboAdmTapiTcpPort = _BiboAdmTapiTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 37),
    _BiboAdmTapiTcpPort_Type()
)
biboAdmTapiTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmTapiTcpPort.setStatus("mandatory")


class _BiboAdmTimeProtocol_Type(Integer32):
    """Custom type biboAdmTimeProtocol based on Integer32"""
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
        *(("isdn", 5),
          ("none", 1),
          ("time-sntp", 4),
          ("time-tcp", 3),
          ("time-udp", 2))
    )


_BiboAdmTimeProtocol_Type.__name__ = "Integer32"
_BiboAdmTimeProtocol_Object = MibScalar
biboAdmTimeProtocol = _BiboAdmTimeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 38),
    _BiboAdmTimeProtocol_Type()
)
biboAdmTimeProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmTimeProtocol.setStatus("mandatory")
_BiboAdmTimeUpdate_Type = Integer32
_BiboAdmTimeUpdate_Object = MibScalar
biboAdmTimeUpdate = _BiboAdmTimeUpdate_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 39),
    _BiboAdmTimeUpdate_Type()
)
biboAdmTimeUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmTimeUpdate.setStatus("mandatory")
_BiboAdmWINS1_Type = IpAddress
_BiboAdmWINS1_Object = MibScalar
biboAdmWINS1 = _BiboAdmWINS1_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 40),
    _BiboAdmWINS1_Type()
)
biboAdmWINS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmWINS1.setStatus("mandatory")
_BiboAdmWINS2_Type = IpAddress
_BiboAdmWINS2_Object = MibScalar
biboAdmWINS2 = _BiboAdmWINS2_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 41),
    _BiboAdmWINS2_Type()
)
biboAdmWINS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmWINS2.setStatus("mandatory")
_BiboAdmCardTable_Object = MibTable
biboAdmCardTable = _BiboAdmCardTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 42)
)
if mibBuilder.loadTexts:
    biboAdmCardTable.setStatus("mandatory")
_BiboAdmCardEntry_Object = MibTableRow
biboAdmCardEntry = _BiboAdmCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 42, 1)
)
biboAdmCardEntry.setIndexNames(
    (0, "BIANCA-BRICK-MIB", "biboACrdSlot"),
)
if mibBuilder.loadTexts:
    biboAdmCardEntry.setStatus("mandatory")


class _BiboACrdSlot_Type(Integer32):
    """Custom type biboACrdSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_BiboACrdSlot_Type.__name__ = "Integer32"
_BiboACrdSlot_Object = MibTableColumn
biboACrdSlot = _BiboACrdSlot_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 42, 1, 1),
    _BiboACrdSlot_Type()
)
biboACrdSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboACrdSlot.setStatus("mandatory")
_BiboACrdType_Type = DisplayString
_BiboACrdType_Object = MibTableColumn
biboACrdType = _BiboACrdType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 42, 1, 2),
    _BiboACrdType_Type()
)
biboACrdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboACrdType.setStatus("mandatory")


class _BiboACrdState_Type(Integer32):
    """Custom type biboACrdState based on Integer32"""
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
        *(("down", 1),
          ("fail", 3),
          ("running", 2),
          ("stopped", 4))
    )


_BiboACrdState_Type.__name__ = "Integer32"
_BiboACrdState_Object = MibTableColumn
biboACrdState = _BiboACrdState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 42, 1, 3),
    _BiboACrdState_Type()
)
biboACrdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboACrdState.setStatus("mandatory")
_BiboACrdCpldVersion_Type = DisplayString
_BiboACrdCpldVersion_Object = MibTableColumn
biboACrdCpldVersion = _BiboACrdCpldVersion_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 42, 1, 4),
    _BiboACrdCpldVersion_Type()
)
biboACrdCpldVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboACrdCpldVersion.setStatus("mandatory")
_BiboACrdFpgaVersion_Type = DisplayString
_BiboACrdFpgaVersion_Object = MibTableColumn
biboACrdFpgaVersion = _BiboACrdFpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 42, 1, 5),
    _BiboACrdFpgaVersion_Type()
)
biboACrdFpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboACrdFpgaVersion.setStatus("mandatory")


class _BiboACrdTemp_Type(Integer32):
    """Custom type biboACrdTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_BiboACrdTemp_Type.__name__ = "Integer32"
_BiboACrdTemp_Object = MibTableColumn
biboACrdTemp = _BiboACrdTemp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 42, 1, 6),
    _BiboACrdTemp_Type()
)
biboACrdTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboACrdTemp.setStatus("mandatory")


class _BiboACrdTempAlarmThreshold_Type(Integer32):
    """Custom type biboACrdTempAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_BiboACrdTempAlarmThreshold_Type.__name__ = "Integer32"
_BiboACrdTempAlarmThreshold_Object = MibTableColumn
biboACrdTempAlarmThreshold = _BiboACrdTempAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 42, 1, 7),
    _BiboACrdTempAlarmThreshold_Type()
)
biboACrdTempAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboACrdTempAlarmThreshold.setStatus("mandatory")


class _BiboACrdTempAlarmTrap_Type(Integer32):
    """Custom type biboACrdTempAlarmTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("critical", 2),
          ("normal", 1))
    )


_BiboACrdTempAlarmTrap_Type.__name__ = "Integer32"
_BiboACrdTempAlarmTrap_Object = MibTableColumn
biboACrdTempAlarmTrap = _BiboACrdTempAlarmTrap_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 42, 1, 8),
    _BiboACrdTempAlarmTrap_Type()
)
biboACrdTempAlarmTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboACrdTempAlarmTrap.setStatus("mandatory")
_BiboAdmTraps_ObjectIdentity = ObjectIdentity
biboAdmTraps = _BiboAdmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 43)
)


class _BiboAdmSnmpLinkTrapEvent_Type(Integer32):
    """Custom type biboAdmSnmpLinkTrapEvent based on Integer32"""
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
        *(("any", 2),
          ("down", 4),
          ("none", 1),
          ("up", 3))
    )


_BiboAdmSnmpLinkTrapEvent_Type.__name__ = "Integer32"
_BiboAdmSnmpLinkTrapEvent_Object = MibScalar
biboAdmSnmpLinkTrapEvent = _BiboAdmSnmpLinkTrapEvent_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 44),
    _BiboAdmSnmpLinkTrapEvent_Type()
)
biboAdmSnmpLinkTrapEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmSnmpLinkTrapEvent.setStatus("mandatory")
_Admin_2_ObjectIdentity = ObjectIdentity
admin_2 = _Admin_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 22)
)
_Extadmin_ObjectIdentity = ObjectIdentity
extadmin = _Extadmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 22, 1)
)
_BiboExtAdmMonAddress_Type = IpAddress
_BiboExtAdmMonAddress_Object = MibScalar
biboExtAdmMonAddress = _BiboExtAdmMonAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 22, 1, 1),
    _BiboExtAdmMonAddress_Type()
)
biboExtAdmMonAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboExtAdmMonAddress.setStatus("mandatory")


class _BiboExtAdmMonPort_Type(Integer32):
    """Custom type biboExtAdmMonPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BiboExtAdmMonPort_Type.__name__ = "Integer32"
_BiboExtAdmMonPort_Object = MibScalar
biboExtAdmMonPort = _BiboExtAdmMonPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 22, 1, 2),
    _BiboExtAdmMonPort_Type()
)
biboExtAdmMonPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboExtAdmMonPort.setStatus("mandatory")


class _BiboExtAdmMonType_Type(Integer32):
    """Custom type biboExtAdmMonType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("physical", 2),
          ("physical-virt", 3))
    )


_BiboExtAdmMonType_Type.__name__ = "Integer32"
_BiboExtAdmMonType_Object = MibScalar
biboExtAdmMonType = _BiboExtAdmMonType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 22, 1, 3),
    _BiboExtAdmMonType_Type()
)
biboExtAdmMonType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboExtAdmMonType.setStatus("mandatory")


class _BiboExtAdmMonUpdate_Type(Integer32):
    """Custom type biboExtAdmMonUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_BiboExtAdmMonUpdate_Type.__name__ = "Integer32"
_BiboExtAdmMonUpdate_Object = MibScalar
biboExtAdmMonUpdate = _BiboExtAdmMonUpdate_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 22, 1, 4),
    _BiboExtAdmMonUpdate_Type()
)
biboExtAdmMonUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboExtAdmMonUpdate.setStatus("mandatory")

# Managed Objects groups


# Notification objects

biboAdmTrapACrdTempCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 43, 0, 1)
)
biboAdmTrapACrdTempCritical.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("BIANCA-BRICK-MIB", "biboACrdSlot"),
        ("BIANCA-BRICK-MIB", "biboACrdType"),
        ("BIANCA-BRICK-MIB", "biboACrdState"),
        ("BIANCA-BRICK-MIB", "biboACrdTemp"),
        ("BIANCA-BRICK-MIB", "biboACrdTempAlarmThreshold"))
)
if mibBuilder.loadTexts:
    biboAdmTrapACrdTempCritical.setStatus(
        ""
    )

biboAdmTrapACrdTempOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 43, 0, 2)
)
biboAdmTrapACrdTempOk.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("BIANCA-BRICK-MIB", "biboACrdSlot"),
        ("BIANCA-BRICK-MIB", "biboACrdType"),
        ("BIANCA-BRICK-MIB", "biboACrdState"),
        ("BIANCA-BRICK-MIB", "biboACrdTemp"),
        ("BIANCA-BRICK-MIB", "biboACrdTempAlarmThreshold"))
)
if mibBuilder.loadTexts:
    biboAdmTrapACrdTempOk.setStatus(
        ""
    )

biboAdmTrapACrdDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 43, 0, 3)
)
biboAdmTrapACrdDown.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("BIANCA-BRICK-MIB", "biboACrdSlot"),
        ("BIANCA-BRICK-MIB", "biboACrdType"),
        ("BIANCA-BRICK-MIB", "biboACrdState"),
        ("BIANCA-BRICK-MIB", "biboACrdTemp"))
)
if mibBuilder.loadTexts:
    biboAdmTrapACrdDown.setStatus(
        ""
    )

biboAdmTrapACrdRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 43, 0, 4)
)
biboAdmTrapACrdRunning.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("BIANCA-BRICK-MIB", "biboACrdSlot"),
        ("BIANCA-BRICK-MIB", "biboACrdType"),
        ("BIANCA-BRICK-MIB", "biboACrdState"),
        ("BIANCA-BRICK-MIB", "biboACrdTemp"))
)
if mibBuilder.loadTexts:
    biboAdmTrapACrdRunning.setStatus(
        ""
    )

biboAdmTrapACrdFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 43, 0, 5)
)
biboAdmTrapACrdFailed.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("BIANCA-BRICK-MIB", "biboACrdSlot"),
        ("BIANCA-BRICK-MIB", "biboACrdType"),
        ("BIANCA-BRICK-MIB", "biboACrdState"),
        ("BIANCA-BRICK-MIB", "biboACrdTemp"))
)
if mibBuilder.loadTexts:
    biboAdmTrapACrdFailed.setStatus(
        ""
    )

biboAdmTrapACrdStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 272, 4, 1, 43, 0, 6)
)
biboAdmTrapACrdStopped.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("BIANCA-BRICK-MIB", "biboACrdSlot"),
        ("BIANCA-BRICK-MIB", "biboACrdType"),
        ("BIANCA-BRICK-MIB", "biboACrdState"),
        ("BIANCA-BRICK-MIB", "biboACrdTemp"))
)
if mibBuilder.loadTexts:
    biboAdmTrapACrdStopped.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-MIB",
    **{"DisplayString": DisplayString,
       "PhysAddress": PhysAddress,
       "Date": Date,
       "HexValue": HexValue,
       "org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "admin": admin,
       "biboAdmTrapCommunity": biboAdmTrapCommunity,
       "biboAdmSnmpVersion": biboAdmSnmpVersion,
       "biboAdmSnmpPort": biboAdmSnmpPort,
       "biboAdmSnmpTrapPort": biboAdmSnmpTrapPort,
       "biboAdmIpAddr": biboAdmIpAddr,
       "biboAdmTrapBrdCast": biboAdmTrapBrdCast,
       "biboAdmTrapHostTable": biboAdmTrapHostTable,
       "biboAdmTrapHostEntry": biboAdmTrapHostEntry,
       "biboAdmTrapHostAddr": biboAdmTrapHostAddr,
       "biboAdmTrapHostStatus": biboAdmTrapHostStatus,
       "biboAdmSyslogMaxEntries": biboAdmSyslogMaxEntries,
       "biboAdmSyslogTable": biboAdmSyslogTable,
       "biboAdmSyslogEntry": biboAdmSyslogEntry,
       "biboAdmSyslogTimeStamp": biboAdmSyslogTimeStamp,
       "biboAdmSyslogLevel": biboAdmSyslogLevel,
       "biboAdmSyslogMessage": biboAdmSyslogMessage,
       "biboAdmSyslogSubject": biboAdmSyslogSubject,
       "biboAdmLogHostTable": biboAdmLogHostTable,
       "biboAdmLogHostEntry": biboAdmLogHostEntry,
       "biboAdmLogHostAddr": biboAdmLogHostAddr,
       "biboAdmLogHostLevel": biboAdmLogHostLevel,
       "biboAdmLogHostFacility": biboAdmLogHostFacility,
       "biboAdmLogHostType": biboAdmLogHostType,
       "biboAdmLogHostTimestamp": biboAdmLogHostTimestamp,
       "biboAdmConfigTable": biboAdmConfigTable,
       "biboAdmConfigEntry": biboAdmConfigEntry,
       "biboAdmConfigCmd": biboAdmConfigCmd,
       "biboAdmConfigObject": biboAdmConfigObject,
       "biboAdmConfigPath": biboAdmConfigPath,
       "biboAdmConfigPathNew": biboAdmConfigPathNew,
       "biboAdmConfigHost": biboAdmConfigHost,
       "biboAdmConfigState": biboAdmConfigState,
       "biboAdmConfigFile": biboAdmConfigFile,
       "biboAdmConfigDirTable": biboAdmConfigDirTable,
       "biboAdmConfigDirEntry": biboAdmConfigDirEntry,
       "biboAdmConfigDirName": biboAdmConfigDirName,
       "biboAdmConfigDirCount": biboAdmConfigDirCount,
       "biboAdmConfigDirContent": biboAdmConfigDirContent,
       "biboAdmBoardTable": biboAdmBoardTable,
       "biboAdmBoardEntry": biboAdmBoardEntry,
       "biboABrdSlot": biboABrdSlot,
       "biboABrdType": biboABrdType,
       "biboABrdHWRelease": biboABrdHWRelease,
       "biboABrdFWRelease": biboABrdFWRelease,
       "biboABrdPartNo": biboABrdPartNo,
       "biboABrdConnector": biboABrdConnector,
       "biboABrdUnit": biboABrdUnit,
       "biboABrdSerialNo": biboABrdSerialNo,
       "biboAdmUsrTrapTable": biboAdmUsrTrapTable,
       "biboAdmUsrTrapEntry": biboAdmUsrTrapEntry,
       "biboATrpObj": biboATrpObj,
       "biboATrpStatus": biboATrpStatus,
       "biboAdmDomainName": biboAdmDomainName,
       "biboAdmNameServer": biboAdmNameServer,
       "biboAdmNameServ2": biboAdmNameServ2,
       "biboAdmBridgeEnable": biboAdmBridgeEnable,
       "biboAdmCapiTcpPort": biboAdmCapiTcpPort,
       "biboAdmTraceTcpPort": biboAdmTraceTcpPort,
       "biboAdmRipUdpPort": biboAdmRipUdpPort,
       "biboAdmSWVersion": biboAdmSWVersion,
       "biboAdmTimeServer": biboAdmTimeServer,
       "biboAdmTimeOffset": biboAdmTimeOffset,
       "biboAdmConsoleSyslog": biboAdmConsoleSyslog,
       "biboAdmSyslogTableLevel": biboAdmSyslogTableLevel,
       "biboAdmSystemId": biboAdmSystemId,
       "biboAdmLicInfoTable": biboAdmLicInfoTable,
       "biboAdmLicInfoEntry": biboAdmLicInfoEntry,
       "biboAdmLicInfoType": biboAdmLicInfoType,
       "biboAdmLicInfoStatus": biboAdmLicInfoStatus,
       "biboAdmLicInfoId": biboAdmLicInfoId,
       "biboAdmLicInfoSlot": biboAdmLicInfoSlot,
       "biboAdmLicInfoMaxLic": biboAdmLicInfoMaxLic,
       "biboAdmLicInfoInUse": biboAdmLicInfoInUse,
       "biboAdmLicInfoHwSerial": biboAdmLicInfoHwSerial,
       "biboAdmLicInfoUnit": biboAdmLicInfoUnit,
       "biboAdmBootpRelayServer": biboAdmBootpRelayServer,
       "biboAdmRadiusServer": biboAdmRadiusServer,
       "biboAdmLocalPPPIdent": biboAdmLocalPPPIdent,
       "biboAdmHttpTcpPort": biboAdmHttpTcpPort,
       "biboAdmTapiTcpPort": biboAdmTapiTcpPort,
       "biboAdmTimeProtocol": biboAdmTimeProtocol,
       "biboAdmTimeUpdate": biboAdmTimeUpdate,
       "biboAdmWINS1": biboAdmWINS1,
       "biboAdmWINS2": biboAdmWINS2,
       "biboAdmCardTable": biboAdmCardTable,
       "biboAdmCardEntry": biboAdmCardEntry,
       "biboACrdSlot": biboACrdSlot,
       "biboACrdType": biboACrdType,
       "biboACrdState": biboACrdState,
       "biboACrdCpldVersion": biboACrdCpldVersion,
       "biboACrdFpgaVersion": biboACrdFpgaVersion,
       "biboACrdTemp": biboACrdTemp,
       "biboACrdTempAlarmThreshold": biboACrdTempAlarmThreshold,
       "biboACrdTempAlarmTrap": biboACrdTempAlarmTrap,
       "biboAdmTraps": biboAdmTraps,
       "biboAdmTrapACrdTempCritical": biboAdmTrapACrdTempCritical,
       "biboAdmTrapACrdTempOk": biboAdmTrapACrdTempOk,
       "biboAdmTrapACrdDown": biboAdmTrapACrdDown,
       "biboAdmTrapACrdRunning": biboAdmTrapACrdRunning,
       "biboAdmTrapACrdFailed": biboAdmTrapACrdFailed,
       "biboAdmTrapACrdStopped": biboAdmTrapACrdStopped,
       "biboAdmSnmpLinkTrapEvent": biboAdmSnmpLinkTrapEvent,
       "admin-2": admin_2,
       "extadmin": extadmin,
       "biboExtAdmMonAddress": biboExtAdmMonAddress,
       "biboExtAdmMonPort": biboExtAdmMonPort,
       "biboExtAdmMonType": biboExtAdmMonType,
       "biboExtAdmMonUpdate": biboExtAdmMonUpdate}
)
