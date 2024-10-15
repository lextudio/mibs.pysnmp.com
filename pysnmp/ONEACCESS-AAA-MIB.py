# SNMP MIB module (ONEACCESS-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-AAA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:45 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(oacExpIMManagement,
 oacMIBModules) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMManagement",
    "oacMIBModules")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

oacAAAConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100, 690)
)
oacAAAConfigMIB.setRevisions(
        ("2011-07-26 00:00",
         "2011-06-15 00:00",
         "2010-12-17 00:01",
         "2010-07-08 00:01")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OacAAAConfig_ObjectIdentity = ObjectIdentity
oacAAAConfig = _OacAAAConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10)
)
_OacAAAConfigObjects_ObjectIdentity = ObjectIdentity
oacAAAConfigObjects = _OacAAAConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1)
)
_OacAAARadiusServerConfigTable_Object = MibTable
oacAAARadiusServerConfigTable = _OacAAARadiusServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 1)
)
if mibBuilder.loadTexts:
    oacAAARadiusServerConfigTable.setStatus("current")
_OacAAARadiusServerConfigEntry_Object = MibTableRow
oacAAARadiusServerConfigEntry = _OacAAARadiusServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 1, 1)
)
oacAAARadiusServerConfigEntry.setIndexNames(
    (0, "ONEACCESS-AAA-MIB", "oacAAARadiusServerInfo"),
    (0, "ONEACCESS-AAA-MIB", "oacAAARadiusServerPort"),
)
if mibBuilder.loadTexts:
    oacAAARadiusServerConfigEntry.setStatus("current")
_OacAAARadiusServerInfo_Type = DisplayString
_OacAAARadiusServerInfo_Object = MibTableColumn
oacAAARadiusServerInfo = _OacAAARadiusServerInfo_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 1, 1, 1),
    _OacAAARadiusServerInfo_Type()
)
oacAAARadiusServerInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAARadiusServerInfo.setStatus("current")


class _OacAAARadiusServerPort_Type(Integer32):
    """Custom type oacAAARadiusServerPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OacAAARadiusServerPort_Type.__name__ = "Integer32"
_OacAAARadiusServerPort_Object = MibTableColumn
oacAAARadiusServerPort = _OacAAARadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 1, 1, 2),
    _OacAAARadiusServerPort_Type()
)
oacAAARadiusServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAARadiusServerPort.setStatus("current")


class _OacAAARadiusServerSharedKey_Type(OctetString):
    """Custom type oacAAARadiusServerSharedKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 255),
    )


_OacAAARadiusServerSharedKey_Type.__name__ = "OctetString"
_OacAAARadiusServerSharedKey_Object = MibTableColumn
oacAAARadiusServerSharedKey = _OacAAARadiusServerSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 1, 1, 3),
    _OacAAARadiusServerSharedKey_Type()
)
oacAAARadiusServerSharedKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAARadiusServerSharedKey.setStatus("current")


class _OacAAARadiusServerRetries_Type(Integer32):
    """Custom type oacAAARadiusServerRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_OacAAARadiusServerRetries_Type.__name__ = "Integer32"
_OacAAARadiusServerRetries_Object = MibTableColumn
oacAAARadiusServerRetries = _OacAAARadiusServerRetries_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 1, 1, 4),
    _OacAAARadiusServerRetries_Type()
)
oacAAARadiusServerRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAARadiusServerRetries.setStatus("current")


class _OacAAARadiusServerTimeout_Type(Integer32):
    """Custom type oacAAARadiusServerTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_OacAAARadiusServerTimeout_Type.__name__ = "Integer32"
_OacAAARadiusServerTimeout_Object = MibTableColumn
oacAAARadiusServerTimeout = _OacAAARadiusServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 1, 1, 5),
    _OacAAARadiusServerTimeout_Type()
)
oacAAARadiusServerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAARadiusServerTimeout.setStatus("current")
_OacAAARadiusServerInterface_Type = InterfaceIndex
_OacAAARadiusServerInterface_Object = MibTableColumn
oacAAARadiusServerInterface = _OacAAARadiusServerInterface_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 1, 1, 6),
    _OacAAARadiusServerInterface_Type()
)
oacAAARadiusServerInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAARadiusServerInterface.setStatus("current")
_OacAAARadiusServerRowStatus_Type = RowStatus
_OacAAARadiusServerRowStatus_Object = MibTableColumn
oacAAARadiusServerRowStatus = _OacAAARadiusServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 1, 1, 7),
    _OacAAARadiusServerRowStatus_Type()
)
oacAAARadiusServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAARadiusServerRowStatus.setStatus("current")


class _OacAAARadiusConfigAccPort_Type(Integer32):
    """Custom type oacAAARadiusConfigAccPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OacAAARadiusConfigAccPort_Type.__name__ = "Integer32"
_OacAAARadiusConfigAccPort_Object = MibScalar
oacAAARadiusConfigAccPort = _OacAAARadiusConfigAccPort_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 2),
    _OacAAARadiusConfigAccPort_Type()
)
oacAAARadiusConfigAccPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacAAARadiusConfigAccPort.setStatus("current")
_OacAAATacacsServerConfigTable_Object = MibTable
oacAAATacacsServerConfigTable = _OacAAATacacsServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 3)
)
if mibBuilder.loadTexts:
    oacAAATacacsServerConfigTable.setStatus("current")
_OacAAATacacsServerConfigEntry_Object = MibTableRow
oacAAATacacsServerConfigEntry = _OacAAATacacsServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 3, 1)
)
oacAAATacacsServerConfigEntry.setIndexNames(
    (0, "ONEACCESS-AAA-MIB", "oacAAATacacsServerInfo"),
    (0, "ONEACCESS-AAA-MIB", "oacAAATacacsServerPort"),
)
if mibBuilder.loadTexts:
    oacAAATacacsServerConfigEntry.setStatus("current")
_OacAAATacacsServerInfo_Type = DisplayString
_OacAAATacacsServerInfo_Object = MibTableColumn
oacAAATacacsServerInfo = _OacAAATacacsServerInfo_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 3, 1, 1),
    _OacAAATacacsServerInfo_Type()
)
oacAAATacacsServerInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAATacacsServerInfo.setStatus("current")


class _OacAAATacacsServerPort_Type(Integer32):
    """Custom type oacAAATacacsServerPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OacAAATacacsServerPort_Type.__name__ = "Integer32"
_OacAAATacacsServerPort_Object = MibTableColumn
oacAAATacacsServerPort = _OacAAATacacsServerPort_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 3, 1, 2),
    _OacAAATacacsServerPort_Type()
)
oacAAATacacsServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAATacacsServerPort.setStatus("current")


class _OacAAATacacsServerSharedKey_Type(OctetString):
    """Custom type oacAAATacacsServerSharedKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 255),
    )


_OacAAATacacsServerSharedKey_Type.__name__ = "OctetString"
_OacAAATacacsServerSharedKey_Object = MibTableColumn
oacAAATacacsServerSharedKey = _OacAAATacacsServerSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 3, 1, 3),
    _OacAAATacacsServerSharedKey_Type()
)
oacAAATacacsServerSharedKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAATacacsServerSharedKey.setStatus("current")


class _OacAAATacacsServerTimeout_Type(Integer32):
    """Custom type oacAAATacacsServerTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_OacAAATacacsServerTimeout_Type.__name__ = "Integer32"
_OacAAATacacsServerTimeout_Object = MibTableColumn
oacAAATacacsServerTimeout = _OacAAATacacsServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 3, 1, 4),
    _OacAAATacacsServerTimeout_Type()
)
oacAAATacacsServerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAATacacsServerTimeout.setStatus("current")
_OacAAATacacsServerInterface_Type = InterfaceIndex
_OacAAATacacsServerInterface_Object = MibTableColumn
oacAAATacacsServerInterface = _OacAAATacacsServerInterface_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 3, 1, 5),
    _OacAAATacacsServerInterface_Type()
)
oacAAATacacsServerInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAATacacsServerInterface.setStatus("current")
_OacAAATacacsServerRowStatus_Type = RowStatus
_OacAAATacacsServerRowStatus_Object = MibTableColumn
oacAAATacacsServerRowStatus = _OacAAATacacsServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 3, 1, 6),
    _OacAAATacacsServerRowStatus_Type()
)
oacAAATacacsServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAATacacsServerRowStatus.setStatus("current")


class _OacAAATacacsConfigUseUsername_Type(TruthValue):
    """Custom type oacAAATacacsConfigUseUsername based on TruthValue"""


_OacAAATacacsConfigUseUsername_Object = MibScalar
oacAAATacacsConfigUseUsername = _OacAAATacacsConfigUseUsername_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 4),
    _OacAAATacacsConfigUseUsername_Type()
)
oacAAATacacsConfigUseUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacAAATacacsConfigUseUsername.setStatus("current")
_OacAAAAuthenticationServerConfigTable_Object = MibTable
oacAAAAuthenticationServerConfigTable = _OacAAAAuthenticationServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 5)
)
if mibBuilder.loadTexts:
    oacAAAAuthenticationServerConfigTable.setStatus("current")
_OacAAAAuthenticationServerConfigEntry_Object = MibTableRow
oacAAAAuthenticationServerConfigEntry = _OacAAAAuthenticationServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 5, 1)
)
oacAAAAuthenticationServerConfigEntry.setIndexNames(
    (0, "ONEACCESS-AAA-MIB", "oacAAAAuthenticationFeature"),
    (0, "ONEACCESS-AAA-MIB", "oacAAAAuthenticationReqSrc"),
)
if mibBuilder.loadTexts:
    oacAAAAuthenticationServerConfigEntry.setStatus("current")


class _OacAAAAuthenticationFeature_Type(Integer32):
    """Custom type oacAAAAuthenticationFeature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("login", 1))
    )


_OacAAAAuthenticationFeature_Type.__name__ = "Integer32"
_OacAAAAuthenticationFeature_Object = MibTableColumn
oacAAAAuthenticationFeature = _OacAAAAuthenticationFeature_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 5, 1, 1),
    _OacAAAAuthenticationFeature_Type()
)
oacAAAAuthenticationFeature.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAAAuthenticationFeature.setStatus("current")


class _OacAAAAuthenticationReqSrc_Type(Integer32):
    """Custom type oacAAAAuthenticationReqSrc based on Integer32"""
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
        *(("console", 2),
          ("default", 1),
          ("network", 3))
    )


_OacAAAAuthenticationReqSrc_Type.__name__ = "Integer32"
_OacAAAAuthenticationReqSrc_Object = MibTableColumn
oacAAAAuthenticationReqSrc = _OacAAAAuthenticationReqSrc_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 5, 1, 2),
    _OacAAAAuthenticationReqSrc_Type()
)
oacAAAAuthenticationReqSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAAAuthenticationReqSrc.setStatus("current")


class _OacAAAAuthenticationSvrType_Type(OctetString):
    """Custom type oacAAAAuthenticationSvrType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_OacAAAAuthenticationSvrType_Type.__name__ = "OctetString"
_OacAAAAuthenticationSvrType_Object = MibTableColumn
oacAAAAuthenticationSvrType = _OacAAAAuthenticationSvrType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 5, 1, 3),
    _OacAAAAuthenticationSvrType_Type()
)
oacAAAAuthenticationSvrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAAAuthenticationSvrType.setStatus("current")
_OacAAAAuthenticationServerRowStatus_Type = RowStatus
_OacAAAAuthenticationServerRowStatus_Object = MibTableColumn
oacAAAAuthenticationServerRowStatus = _OacAAAAuthenticationServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 5, 1, 4),
    _OacAAAAuthenticationServerRowStatus_Type()
)
oacAAAAuthenticationServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAAAuthenticationServerRowStatus.setStatus("current")
_OacAAAAuthenticationConfigBannerSeqTable_Object = MibTable
oacAAAAuthenticationConfigBannerSeqTable = _OacAAAAuthenticationConfigBannerSeqTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 6)
)
if mibBuilder.loadTexts:
    oacAAAAuthenticationConfigBannerSeqTable.setStatus("current")
_OacAAAAuthenticationConfigBannerSeqEntry_Object = MibTableRow
oacAAAAuthenticationConfigBannerSeqEntry = _OacAAAAuthenticationConfigBannerSeqEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 6, 1)
)
oacAAAAuthenticationConfigBannerSeqEntry.setIndexNames(
    (0, "ONEACCESS-AAA-MIB", "oacAAAAuthenticationBannerSequence"),
)
if mibBuilder.loadTexts:
    oacAAAAuthenticationConfigBannerSeqEntry.setStatus("current")


class _OacAAAAuthenticationBannerSequence_Type(Integer32):
    """Custom type oacAAAAuthenticationBannerSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_OacAAAAuthenticationBannerSequence_Type.__name__ = "Integer32"
_OacAAAAuthenticationBannerSequence_Object = MibTableColumn
oacAAAAuthenticationBannerSequence = _OacAAAAuthenticationBannerSequence_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 6, 1, 1),
    _OacAAAAuthenticationBannerSequence_Type()
)
oacAAAAuthenticationBannerSequence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAAAuthenticationBannerSequence.setStatus("current")


class _OacAAAAuthenticationBannerString_Type(OctetString):
    """Custom type oacAAAAuthenticationBannerString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_OacAAAAuthenticationBannerString_Type.__name__ = "OctetString"
_OacAAAAuthenticationBannerString_Object = MibTableColumn
oacAAAAuthenticationBannerString = _OacAAAAuthenticationBannerString_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 6, 1, 2),
    _OacAAAAuthenticationBannerString_Type()
)
oacAAAAuthenticationBannerString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAAAuthenticationBannerString.setStatus("current")
_OacAAAAuthenticationBannerSeqRowStatus_Type = RowStatus
_OacAAAAuthenticationBannerSeqRowStatus_Object = MibTableColumn
oacAAAAuthenticationBannerSeqRowStatus = _OacAAAAuthenticationBannerSeqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 6, 1, 3),
    _OacAAAAuthenticationBannerSeqRowStatus_Type()
)
oacAAAAuthenticationBannerSeqRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAAAuthenticationBannerSeqRowStatus.setStatus("current")
_OacAAAGroupServerConfigTable_Object = MibTable
oacAAAGroupServerConfigTable = _OacAAAGroupServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 7)
)
if mibBuilder.loadTexts:
    oacAAAGroupServerConfigTable.setStatus("current")
_OacAAAGroupServerConfigEntry_Object = MibTableRow
oacAAAGroupServerConfigEntry = _OacAAAGroupServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 7, 1)
)
oacAAAGroupServerConfigEntry.setIndexNames(
    (0, "ONEACCESS-AAA-MIB", "oacAAAServerGroupName"),
)
if mibBuilder.loadTexts:
    oacAAAGroupServerConfigEntry.setStatus("current")
_OacAAAServerGroupName_Type = DisplayString
_OacAAAServerGroupName_Object = MibTableColumn
oacAAAServerGroupName = _OacAAAServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 7, 1, 1),
    _OacAAAServerGroupName_Type()
)
oacAAAServerGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAAServerGroupName.setStatus("current")


class _OacAAAServerGroupType_Type(Integer32):
    """Custom type oacAAAServerGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radius", 1),
          ("tacacs", 2))
    )


_OacAAAServerGroupType_Type.__name__ = "Integer32"
_OacAAAServerGroupType_Object = MibTableColumn
oacAAAServerGroupType = _OacAAAServerGroupType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 7, 1, 2),
    _OacAAAServerGroupType_Type()
)
oacAAAServerGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAAServerGroupType.setStatus("current")
_OacAAAServerGroupServerInfo_Type = DisplayString
_OacAAAServerGroupServerInfo_Object = MibTableColumn
oacAAAServerGroupServerInfo = _OacAAAServerGroupServerInfo_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 7, 1, 3),
    _OacAAAServerGroupServerInfo_Type()
)
oacAAAServerGroupServerInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAAServerGroupServerInfo.setStatus("current")
_OacAAAServerGroupRowStatus_Type = RowStatus
_OacAAAServerGroupRowStatus_Object = MibTableColumn
oacAAAServerGroupRowStatus = _OacAAAServerGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 7, 1, 4),
    _OacAAAServerGroupRowStatus_Type()
)
oacAAAServerGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAAServerGroupRowStatus.setStatus("current")


class _OacAAAAuthorizationConfigCmdLevelDefTacacs_Type(Integer32):
    """Custom type oacAAAAuthorizationConfigCmdLevelDefTacacs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_OacAAAAuthorizationConfigCmdLevelDefTacacs_Type.__name__ = "Integer32"
_OacAAAAuthorizationConfigCmdLevelDefTacacs_Object = MibScalar
oacAAAAuthorizationConfigCmdLevelDefTacacs = _OacAAAAuthorizationConfigCmdLevelDefTacacs_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 8),
    _OacAAAAuthorizationConfigCmdLevelDefTacacs_Type()
)
oacAAAAuthorizationConfigCmdLevelDefTacacs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacAAAAuthorizationConfigCmdLevelDefTacacs.setStatus("current")
_OacAAAAccCmdsConfigTable_Object = MibTable
oacAAAAccCmdsConfigTable = _OacAAAAccCmdsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 9)
)
if mibBuilder.loadTexts:
    oacAAAAccCmdsConfigTable.setStatus("current")
_OacAAAAccCmdsConfigEntry_Object = MibTableRow
oacAAAAccCmdsConfigEntry = _OacAAAAccCmdsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 9, 1)
)
oacAAAAccCmdsConfigEntry.setIndexNames(
    (0, "ONEACCESS-AAA-MIB", "oacAAAAccCmdAccessLevel"),
)
if mibBuilder.loadTexts:
    oacAAAAccCmdsConfigEntry.setStatus("current")


class _OacAAAAccCmdAccessLevel_Type(Integer32):
    """Custom type oacAAAAccCmdAccessLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_OacAAAAccCmdAccessLevel_Type.__name__ = "Integer32"
_OacAAAAccCmdAccessLevel_Object = MibTableColumn
oacAAAAccCmdAccessLevel = _OacAAAAccCmdAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 9, 1, 1),
    _OacAAAAccCmdAccessLevel_Type()
)
oacAAAAccCmdAccessLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAAAccCmdAccessLevel.setStatus("current")
_OacAAAAccTacacsGroupName_Type = DisplayString
_OacAAAAccTacacsGroupName_Object = MibTableColumn
oacAAAAccTacacsGroupName = _OacAAAAccTacacsGroupName_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 9, 1, 2),
    _OacAAAAccTacacsGroupName_Type()
)
oacAAAAccTacacsGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAAAccTacacsGroupName.setStatus("current")
_OacAAAAccCmdsRowStatus_Type = RowStatus
_OacAAAAccCmdsRowStatus_Object = MibTableColumn
oacAAAAccCmdsRowStatus = _OacAAAAccCmdsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 9, 1, 3),
    _OacAAAAccCmdsRowStatus_Type()
)
oacAAAAccCmdsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacAAAAccCmdsRowStatus.setStatus("current")


class _OacAAAAccConfigExecStartStop_Type(OctetString):
    """Custom type oacAAAAccConfigExecStartStop based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OacAAAAccConfigExecStartStop_Type.__name__ = "OctetString"
_OacAAAAccConfigExecStartStop_Object = MibScalar
oacAAAAccConfigExecStartStop = _OacAAAAccConfigExecStartStop_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 10),
    _OacAAAAccConfigExecStartStop_Type()
)
oacAAAAccConfigExecStartStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacAAAAccConfigExecStartStop.setStatus("current")


class _OacAAAAccConfigSystemStartStop_Type(OctetString):
    """Custom type oacAAAAccConfigSystemStartStop based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OacAAAAccConfigSystemStartStop_Type.__name__ = "OctetString"
_OacAAAAccConfigSystemStartStop_Object = MibScalar
oacAAAAccConfigSystemStartStop = _OacAAAAccConfigSystemStartStop_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 11),
    _OacAAAAccConfigSystemStartStop_Type()
)
oacAAAAccConfigSystemStartStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacAAAAccConfigSystemStartStop.setStatus("current")
_OacAAAConfigConformance_ObjectIdentity = ObjectIdentity
oacAAAConfigConformance = _OacAAAConfigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 2)
)
_OacAAAConfigGroups_ObjectIdentity = ObjectIdentity
oacAAAConfigGroups = _OacAAAConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 2, 1)
)
_OacAAACompls_ObjectIdentity = ObjectIdentity
oacAAACompls = _OacAAACompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 2, 2)
)

# Managed Objects groups

oacAAAConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 2, 1, 1)
)
oacAAAConfigGroup.setObjects(
    ("ONEACCESS-AAA-MIB", "oacAAAAccConfigSystemStartStop")
)
if mibBuilder.loadTexts:
    oacAAAConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-AAA-MIB",
    **{"oacAAAConfigMIB": oacAAAConfigMIB,
       "oacAAAConfig": oacAAAConfig,
       "oacAAAConfigObjects": oacAAAConfigObjects,
       "oacAAARadiusServerConfigTable": oacAAARadiusServerConfigTable,
       "oacAAARadiusServerConfigEntry": oacAAARadiusServerConfigEntry,
       "oacAAARadiusServerInfo": oacAAARadiusServerInfo,
       "oacAAARadiusServerPort": oacAAARadiusServerPort,
       "oacAAARadiusServerSharedKey": oacAAARadiusServerSharedKey,
       "oacAAARadiusServerRetries": oacAAARadiusServerRetries,
       "oacAAARadiusServerTimeout": oacAAARadiusServerTimeout,
       "oacAAARadiusServerInterface": oacAAARadiusServerInterface,
       "oacAAARadiusServerRowStatus": oacAAARadiusServerRowStatus,
       "oacAAARadiusConfigAccPort": oacAAARadiusConfigAccPort,
       "oacAAATacacsServerConfigTable": oacAAATacacsServerConfigTable,
       "oacAAATacacsServerConfigEntry": oacAAATacacsServerConfigEntry,
       "oacAAATacacsServerInfo": oacAAATacacsServerInfo,
       "oacAAATacacsServerPort": oacAAATacacsServerPort,
       "oacAAATacacsServerSharedKey": oacAAATacacsServerSharedKey,
       "oacAAATacacsServerTimeout": oacAAATacacsServerTimeout,
       "oacAAATacacsServerInterface": oacAAATacacsServerInterface,
       "oacAAATacacsServerRowStatus": oacAAATacacsServerRowStatus,
       "oacAAATacacsConfigUseUsername": oacAAATacacsConfigUseUsername,
       "oacAAAAuthenticationServerConfigTable": oacAAAAuthenticationServerConfigTable,
       "oacAAAAuthenticationServerConfigEntry": oacAAAAuthenticationServerConfigEntry,
       "oacAAAAuthenticationFeature": oacAAAAuthenticationFeature,
       "oacAAAAuthenticationReqSrc": oacAAAAuthenticationReqSrc,
       "oacAAAAuthenticationSvrType": oacAAAAuthenticationSvrType,
       "oacAAAAuthenticationServerRowStatus": oacAAAAuthenticationServerRowStatus,
       "oacAAAAuthenticationConfigBannerSeqTable": oacAAAAuthenticationConfigBannerSeqTable,
       "oacAAAAuthenticationConfigBannerSeqEntry": oacAAAAuthenticationConfigBannerSeqEntry,
       "oacAAAAuthenticationBannerSequence": oacAAAAuthenticationBannerSequence,
       "oacAAAAuthenticationBannerString": oacAAAAuthenticationBannerString,
       "oacAAAAuthenticationBannerSeqRowStatus": oacAAAAuthenticationBannerSeqRowStatus,
       "oacAAAGroupServerConfigTable": oacAAAGroupServerConfigTable,
       "oacAAAGroupServerConfigEntry": oacAAAGroupServerConfigEntry,
       "oacAAAServerGroupName": oacAAAServerGroupName,
       "oacAAAServerGroupType": oacAAAServerGroupType,
       "oacAAAServerGroupServerInfo": oacAAAServerGroupServerInfo,
       "oacAAAServerGroupRowStatus": oacAAAServerGroupRowStatus,
       "oacAAAAuthorizationConfigCmdLevelDefTacacs": oacAAAAuthorizationConfigCmdLevelDefTacacs,
       "oacAAAAccCmdsConfigTable": oacAAAAccCmdsConfigTable,
       "oacAAAAccCmdsConfigEntry": oacAAAAccCmdsConfigEntry,
       "oacAAAAccCmdAccessLevel": oacAAAAccCmdAccessLevel,
       "oacAAAAccTacacsGroupName": oacAAAAccTacacsGroupName,
       "oacAAAAccCmdsRowStatus": oacAAAAccCmdsRowStatus,
       "oacAAAAccConfigExecStartStop": oacAAAAccConfigExecStartStop,
       "oacAAAAccConfigSystemStartStop": oacAAAAccConfigSystemStartStop,
       "oacAAAConfigConformance": oacAAAConfigConformance,
       "oacAAAConfigGroups": oacAAAConfigGroups,
       "oacAAAConfigGroup": oacAAAConfigGroup,
       "oacAAACompls": oacAAACompls}
)
