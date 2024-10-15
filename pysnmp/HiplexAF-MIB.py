# SNMP MIB module (HiplexAF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HiplexAF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:52 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sni_ObjectIdentity = ObjectIdentity
sni = _Sni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231)
)
_SniProductMibs_ObjectIdentity = ObjectIdentity
sniProductMibs = _SniProductMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2)
)
_SniHiplexAF_ObjectIdentity = ObjectIdentity
sniHiplexAF = _SniHiplexAF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 35)
)
_HiplexAFObjects_ObjectIdentity = ObjectIdentity
hiplexAFObjects = _HiplexAFObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1)
)
_HiplexAFGlobalData_ObjectIdentity = ObjectIdentity
hiplexAFGlobalData = _HiplexAFGlobalData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 1)
)
_HiplexAFVersion_Type = DisplayString
_HiplexAFVersion_Object = MibScalar
hiplexAFVersion = _HiplexAFVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 1, 1),
    _HiplexAFVersion_Type()
)
hiplexAFVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFVersion.setStatus("mandatory")
_HiplexAFSPVSUserid_Type = DisplayString
_HiplexAFSPVSUserid_Object = MibScalar
hiplexAFSPVSUserid = _HiplexAFSPVSUserid_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 1, 2),
    _HiplexAFSPVSUserid_Type()
)
hiplexAFSPVSUserid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFSPVSUserid.setStatus("mandatory")
_HiplexAFSPVSCatid_Type = DisplayString
_HiplexAFSPVSCatid_Object = MibScalar
hiplexAFSPVSCatid = _HiplexAFSPVSCatid_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 1, 3),
    _HiplexAFSPVSCatid_Type()
)
hiplexAFSPVSCatid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hiplexAFSPVSCatid.setStatus("mandatory")


class _HiplexAFState_Type(Integer32):
    """Custom type hiplexAFState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("started", 1),
          ("stopped", 2),
          ("undefined", 255))
    )


_HiplexAFState_Type.__name__ = "Integer32"
_HiplexAFState_Object = MibScalar
hiplexAFState = _HiplexAFState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 1, 4),
    _HiplexAFState_Type()
)
hiplexAFState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hiplexAFState.setStatus("mandatory")
_HiplexAFTermHost_Type = DisplayString
_HiplexAFTermHost_Object = MibScalar
hiplexAFTermHost = _HiplexAFTermHost_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 1, 5),
    _HiplexAFTermHost_Type()
)
hiplexAFTermHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFTermHost.setStatus("mandatory")
_HiplexAFHostInfo_ObjectIdentity = ObjectIdentity
hiplexAFHostInfo = _HiplexAFHostInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 2)
)
_HiplexAFHostTabNum_Type = Integer32
_HiplexAFHostTabNum_Object = MibScalar
hiplexAFHostTabNum = _HiplexAFHostTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 2, 1),
    _HiplexAFHostTabNum_Type()
)
hiplexAFHostTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFHostTabNum.setStatus("mandatory")
_HiplexAFHostTable_Object = MibTable
hiplexAFHostTable = _HiplexAFHostTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hiplexAFHostTable.setStatus("mandatory")
_HiplexAFHostEntry_Object = MibTableRow
hiplexAFHostEntry = _HiplexAFHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 2, 2, 1)
)
hiplexAFHostEntry.setIndexNames(
    (0, "HiplexAF-MIB", "hiplexAFHostName"),
)
if mibBuilder.loadTexts:
    hiplexAFHostEntry.setStatus("mandatory")
_HiplexAFHostName_Type = DisplayString
_HiplexAFHostName_Object = MibTableColumn
hiplexAFHostName = _HiplexAFHostName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 2, 2, 1, 1),
    _HiplexAFHostName_Type()
)
hiplexAFHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFHostName.setStatus("mandatory")


class _HiplexAFHostEventId_Type(Integer32):
    """Custom type hiplexAFHostEventId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no-event", 1),
          ("termination-requested", 2),
          ("undefined", 255))
    )


_HiplexAFHostEventId_Type.__name__ = "Integer32"
_HiplexAFHostEventId_Object = MibTableColumn
hiplexAFHostEventId = _HiplexAFHostEventId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 2, 2, 1, 2),
    _HiplexAFHostEventId_Type()
)
hiplexAFHostEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFHostEventId.setStatus("mandatory")


class _HiplexAFHostStateInd_Type(Integer32):
    """Custom type hiplexAFHostStateInd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("terminated", 2),
          ("undefined", 255),
          ("working", 1))
    )


_HiplexAFHostStateInd_Type.__name__ = "Integer32"
_HiplexAFHostStateInd_Object = MibTableColumn
hiplexAFHostStateInd = _HiplexAFHostStateInd_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 2, 2, 1, 3),
    _HiplexAFHostStateInd_Type()
)
hiplexAFHostStateInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hiplexAFHostStateInd.setStatus("mandatory")
_HiplexAFHostOperatorRole_Type = DisplayString
_HiplexAFHostOperatorRole_Object = MibTableColumn
hiplexAFHostOperatorRole = _HiplexAFHostOperatorRole_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 2, 2, 1, 4),
    _HiplexAFHostOperatorRole_Type()
)
hiplexAFHostOperatorRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hiplexAFHostOperatorRole.setStatus("mandatory")
_HiplexAFHostHomeCatid_Type = DisplayString
_HiplexAFHostHomeCatid_Object = MibTableColumn
hiplexAFHostHomeCatid = _HiplexAFHostHomeCatid_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 2, 2, 1, 5),
    _HiplexAFHostHomeCatid_Type()
)
hiplexAFHostHomeCatid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFHostHomeCatid.setStatus("mandatory")
_HiplexAFHostSystemId_Type = Integer32
_HiplexAFHostSystemId_Object = MibTableColumn
hiplexAFHostSystemId = _HiplexAFHostSystemId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 2, 2, 1, 6),
    _HiplexAFHostSystemId_Type()
)
hiplexAFHostSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFHostSystemId.setStatus("mandatory")
_HiplexAFHostBS2Version_Type = DisplayString
_HiplexAFHostBS2Version_Object = MibTableColumn
hiplexAFHostBS2Version = _HiplexAFHostBS2Version_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 2, 2, 1, 7),
    _HiplexAFHostBS2Version_Type()
)
hiplexAFHostBS2Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFHostBS2Version.setStatus("mandatory")


class _HiplexAFHostImcatInd_Type(Integer32):
    """Custom type hiplexAFHostImcatInd based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("check", 1),
          ("crash", 2),
          ("excat", 3),
          ("imcat", 4),
          ("mchange", 5),
          ("readerr", 6),
          ("shutdown", 7),
          ("undefined", 255),
          ("wrterr", 8))
    )


_HiplexAFHostImcatInd_Type.__name__ = "Integer32"
_HiplexAFHostImcatInd_Object = MibTableColumn
hiplexAFHostImcatInd = _HiplexAFHostImcatInd_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 2, 2, 1, 8),
    _HiplexAFHostImcatInd_Type()
)
hiplexAFHostImcatInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFHostImcatInd.setStatus("mandatory")


class _HiplexAFHostMasterSlaveInd_Type(Integer32):
    """Custom type hiplexAFHostMasterSlaveInd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("master", 1),
          ("slave", 3),
          ("undefined", 255))
    )


_HiplexAFHostMasterSlaveInd_Type.__name__ = "Integer32"
_HiplexAFHostMasterSlaveInd_Object = MibTableColumn
hiplexAFHostMasterSlaveInd = _HiplexAFHostMasterSlaveInd_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 2, 2, 1, 9),
    _HiplexAFHostMasterSlaveInd_Type()
)
hiplexAFHostMasterSlaveInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFHostMasterSlaveInd.setStatus("mandatory")


class _HiplexAFHostSnmpAgentStateInd_Type(Integer32):
    """Custom type hiplexAFHostSnmpAgentStateInd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("not-working", 2),
          ("undefined", 255),
          ("working", 1))
    )


_HiplexAFHostSnmpAgentStateInd_Type.__name__ = "Integer32"
_HiplexAFHostSnmpAgentStateInd_Object = MibTableColumn
hiplexAFHostSnmpAgentStateInd = _HiplexAFHostSnmpAgentStateInd_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 2, 2, 1, 10),
    _HiplexAFHostSnmpAgentStateInd_Type()
)
hiplexAFHostSnmpAgentStateInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hiplexAFHostSnmpAgentStateInd.setStatus("mandatory")
_HiplexAFSWUInfo_ObjectIdentity = ObjectIdentity
hiplexAFSWUInfo = _HiplexAFSWUInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 3)
)
_HiplexAFSWUTabNum_Type = Integer32
_HiplexAFSWUTabNum_Object = MibScalar
hiplexAFSWUTabNum = _HiplexAFSWUTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 3, 1),
    _HiplexAFSWUTabNum_Type()
)
hiplexAFSWUTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFSWUTabNum.setStatus("mandatory")
_HiplexAFSWUTable_Object = MibTable
hiplexAFSWUTable = _HiplexAFSWUTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hiplexAFSWUTable.setStatus("mandatory")
_HiplexAFSWUEntry_Object = MibTableRow
hiplexAFSWUEntry = _HiplexAFSWUEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 3, 2, 1)
)
hiplexAFSWUEntry.setIndexNames(
    (0, "HiplexAF-MIB", "hiplexAFSWUName"),
)
if mibBuilder.loadTexts:
    hiplexAFSWUEntry.setStatus("mandatory")
_HiplexAFSWUName_Type = DisplayString
_HiplexAFSWUName_Object = MibTableColumn
hiplexAFSWUName = _HiplexAFSWUName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 3, 2, 1, 1),
    _HiplexAFSWUName_Type()
)
hiplexAFSWUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFSWUName.setStatus("mandatory")
_HiplexAFSWUCreaTime_Type = DisplayString
_HiplexAFSWUCreaTime_Object = MibTableColumn
hiplexAFSWUCreaTime = _HiplexAFSWUCreaTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 3, 2, 1, 2),
    _HiplexAFSWUCreaTime_Type()
)
hiplexAFSWUCreaTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFSWUCreaTime.setStatus("mandatory")
_HiplexAFSWUWorkSystem_Type = DisplayString
_HiplexAFSWUWorkSystem_Object = MibTableColumn
hiplexAFSWUWorkSystem = _HiplexAFSWUWorkSystem_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 3, 2, 1, 3),
    _HiplexAFSWUWorkSystem_Type()
)
hiplexAFSWUWorkSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hiplexAFSWUWorkSystem.setStatus("mandatory")
_HiplexAFSWUVirtHost_Type = DisplayString
_HiplexAFSWUVirtHost_Object = MibTableColumn
hiplexAFSWUVirtHost = _HiplexAFSWUVirtHost_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 3, 2, 1, 4),
    _HiplexAFSWUVirtHost_Type()
)
hiplexAFSWUVirtHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFSWUVirtHost.setStatus("mandatory")
_HiplexAFSWUVirtHostAct_Type = DisplayString
_HiplexAFSWUVirtHostAct_Object = MibTableColumn
hiplexAFSWUVirtHostAct = _HiplexAFSWUVirtHostAct_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 3, 2, 1, 5),
    _HiplexAFSWUVirtHostAct_Type()
)
hiplexAFSWUVirtHostAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFSWUVirtHostAct.setStatus("mandatory")
_HiplexAFSWUVirtHostDeact_Type = DisplayString
_HiplexAFSWUVirtHostDeact_Object = MibTableColumn
hiplexAFSWUVirtHostDeact = _HiplexAFSWUVirtHostDeact_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 3, 2, 1, 6),
    _HiplexAFSWUVirtHostDeact_Type()
)
hiplexAFSWUVirtHostDeact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFSWUVirtHostDeact.setStatus("mandatory")
_HiplexAFSWUFEPNumber_Type = Integer32
_HiplexAFSWUFEPNumber_Object = MibTableColumn
hiplexAFSWUFEPNumber = _HiplexAFSWUFEPNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 3, 2, 1, 7),
    _HiplexAFSWUFEPNumber_Type()
)
hiplexAFSWUFEPNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFSWUFEPNumber.setStatus("mandatory")
_HiplexAFSWUPubsetNumber_Type = Integer32
_HiplexAFSWUPubsetNumber_Object = MibTableColumn
hiplexAFSWUPubsetNumber = _HiplexAFSWUPubsetNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 3, 2, 1, 8),
    _HiplexAFSWUPubsetNumber_Type()
)
hiplexAFSWUPubsetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFSWUPubsetNumber.setStatus("mandatory")
_HiplexAFSWUApplicationNumber_Type = Integer32
_HiplexAFSWUApplicationNumber_Object = MibTableColumn
hiplexAFSWUApplicationNumber = _HiplexAFSWUApplicationNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 3, 2, 1, 9),
    _HiplexAFSWUApplicationNumber_Type()
)
hiplexAFSWUApplicationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFSWUApplicationNumber.setStatus("mandatory")
_HiplexAFSWUHostParamInfo_ObjectIdentity = ObjectIdentity
hiplexAFSWUHostParamInfo = _HiplexAFSWUHostParamInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 4)
)
_HiplexAFSWUHostParamTable_Object = MibTable
hiplexAFSWUHostParamTable = _HiplexAFSWUHostParamTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hiplexAFSWUHostParamTable.setStatus("mandatory")
_HiplexAFSWUHostParamEntry_Object = MibTableRow
hiplexAFSWUHostParamEntry = _HiplexAFSWUHostParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 4, 1, 1)
)
hiplexAFSWUHostParamEntry.setIndexNames(
    (0, "HiplexAF-MIB", "hiplexAFSWUName"),
    (0, "HiplexAF-MIB", "hiplexAFHostName"),
)
if mibBuilder.loadTexts:
    hiplexAFSWUHostParamEntry.setStatus("mandatory")


class _HiplexAFSWUHostParamEventId_Type(Integer32):
    """Custom type hiplexAFSWUHostParamEventId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("pass-over", 2),
          ("take-over", 3),
          ("terminate", 4),
          ("undefined", 255))
    )


_HiplexAFSWUHostParamEventId_Type.__name__ = "Integer32"
_HiplexAFSWUHostParamEventId_Object = MibTableColumn
hiplexAFSWUHostParamEventId = _HiplexAFSWUHostParamEventId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 4, 1, 1, 1),
    _HiplexAFSWUHostParamEventId_Type()
)
hiplexAFSWUHostParamEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFSWUHostParamEventId.setStatus("mandatory")


class _HiplexAFSWUHostParamStateInd_Type(Integer32):
    """Custom type hiplexAFSWUHostParamStateInd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("crashed", 3),
          ("standby", 2),
          ("terminated", 4),
          ("undefined", 255),
          ("work", 1))
    )


_HiplexAFSWUHostParamStateInd_Type.__name__ = "Integer32"
_HiplexAFSWUHostParamStateInd_Object = MibTableColumn
hiplexAFSWUHostParamStateInd = _HiplexAFSWUHostParamStateInd_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 4, 1, 1, 2),
    _HiplexAFSWUHostParamStateInd_Type()
)
hiplexAFSWUHostParamStateInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hiplexAFSWUHostParamStateInd.setStatus("mandatory")


class _HiplexAFSWUHostParamPriority_Type(Integer32):
    """Custom type hiplexAFSWUHostParamPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HiplexAFSWUHostParamPriority_Type.__name__ = "Integer32"
_HiplexAFSWUHostParamPriority_Object = MibTableColumn
hiplexAFSWUHostParamPriority = _HiplexAFSWUHostParamPriority_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 4, 1, 1, 3),
    _HiplexAFSWUHostParamPriority_Type()
)
hiplexAFSWUHostParamPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hiplexAFSWUHostParamPriority.setStatus("mandatory")
_HiplexAFSWUHostParamOperatorRole_Type = DisplayString
_HiplexAFSWUHostParamOperatorRole_Object = MibTableColumn
hiplexAFSWUHostParamOperatorRole = _HiplexAFSWUHostParamOperatorRole_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 4, 1, 1, 4),
    _HiplexAFSWUHostParamOperatorRole_Type()
)
hiplexAFSWUHostParamOperatorRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hiplexAFSWUHostParamOperatorRole.setStatus("mandatory")
_HiplexAFSWUHostFEPInfo_ObjectIdentity = ObjectIdentity
hiplexAFSWUHostFEPInfo = _HiplexAFSWUHostFEPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 5)
)


class _HiplexAFSWUHostFEPTabNum_Type(Integer32):
    """Custom type hiplexAFSWUHostFEPTabNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_HiplexAFSWUHostFEPTabNum_Type.__name__ = "Integer32"
_HiplexAFSWUHostFEPTabNum_Object = MibScalar
hiplexAFSWUHostFEPTabNum = _HiplexAFSWUHostFEPTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 5, 1),
    _HiplexAFSWUHostFEPTabNum_Type()
)
hiplexAFSWUHostFEPTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFSWUHostFEPTabNum.setStatus("mandatory")
_HiplexAFSWUHostFEPTable_Object = MibTable
hiplexAFSWUHostFEPTable = _HiplexAFSWUHostFEPTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 5, 2)
)
if mibBuilder.loadTexts:
    hiplexAFSWUHostFEPTable.setStatus("mandatory")
_HiplexAFSWUHostFEPEntry_Object = MibTableRow
hiplexAFSWUHostFEPEntry = _HiplexAFSWUHostFEPEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 5, 2, 1)
)
hiplexAFSWUHostFEPEntry.setIndexNames(
    (0, "HiplexAF-MIB", "hiplexAFSWUName"),
    (0, "HiplexAF-MIB", "hiplexAFHostName"),
    (0, "HiplexAF-MIB", "hiplexAFSWUHostFEPIndex"),
)
if mibBuilder.loadTexts:
    hiplexAFSWUHostFEPEntry.setStatus("mandatory")


class _HiplexAFSWUHostFEPIndex_Type(Integer32):
    """Custom type hiplexAFSWUHostFEPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HiplexAFSWUHostFEPIndex_Type.__name__ = "Integer32"
_HiplexAFSWUHostFEPIndex_Object = MibTableColumn
hiplexAFSWUHostFEPIndex = _HiplexAFSWUHostFEPIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 5, 2, 1, 1),
    _HiplexAFSWUHostFEPIndex_Type()
)
hiplexAFSWUHostFEPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFSWUHostFEPIndex.setStatus("mandatory")
_HiplexAFSWUHostFEPName_Type = DisplayString
_HiplexAFSWUHostFEPName_Object = MibTableColumn
hiplexAFSWUHostFEPName = _HiplexAFSWUHostFEPName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 5, 2, 1, 2),
    _HiplexAFSWUHostFEPName_Type()
)
hiplexAFSWUHostFEPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hiplexAFSWUHostFEPName.setStatus("mandatory")
_HiplexAFSWUHostFEPPortnumber_Type = Integer32
_HiplexAFSWUHostFEPPortnumber_Object = MibTableColumn
hiplexAFSWUHostFEPPortnumber = _HiplexAFSWUHostFEPPortnumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 5, 2, 1, 3),
    _HiplexAFSWUHostFEPPortnumber_Type()
)
hiplexAFSWUHostFEPPortnumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hiplexAFSWUHostFEPPortnumber.setStatus("mandatory")
_HiplexAFSWUVolumeInfo_ObjectIdentity = ObjectIdentity
hiplexAFSWUVolumeInfo = _HiplexAFSWUVolumeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 6)
)
_HiplexAFSWUVolumeTabNum_Type = Integer32
_HiplexAFSWUVolumeTabNum_Object = MibScalar
hiplexAFSWUVolumeTabNum = _HiplexAFSWUVolumeTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 6, 1),
    _HiplexAFSWUVolumeTabNum_Type()
)
hiplexAFSWUVolumeTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFSWUVolumeTabNum.setStatus("mandatory")
_HiplexAFSWUVolumeTable_Object = MibTable
hiplexAFSWUVolumeTable = _HiplexAFSWUVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 6, 2)
)
if mibBuilder.loadTexts:
    hiplexAFSWUVolumeTable.setStatus("mandatory")
_HiplexAFSWUVolumeEntry_Object = MibTableRow
hiplexAFSWUVolumeEntry = _HiplexAFSWUVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 6, 2, 1)
)
hiplexAFSWUVolumeEntry.setIndexNames(
    (0, "HiplexAF-MIB", "hiplexAFSWUName"),
    (0, "HiplexAF-MIB", "hiplexAFSWUVolumeName"),
)
if mibBuilder.loadTexts:
    hiplexAFSWUVolumeEntry.setStatus("mandatory")
_HiplexAFSWUVolumeName_Type = DisplayString
_HiplexAFSWUVolumeName_Object = MibTableColumn
hiplexAFSWUVolumeName = _HiplexAFSWUVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 6, 2, 1, 1),
    _HiplexAFSWUVolumeName_Type()
)
hiplexAFSWUVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFSWUVolumeName.setStatus("mandatory")
_HiplexAFSWUVolumeTypeName_Type = DisplayString
_HiplexAFSWUVolumeTypeName_Object = MibTableColumn
hiplexAFSWUVolumeTypeName = _HiplexAFSWUVolumeTypeName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 6, 2, 1, 2),
    _HiplexAFSWUVolumeTypeName_Type()
)
hiplexAFSWUVolumeTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFSWUVolumeTypeName.setStatus("mandatory")


class _HiplexAFSWUVolumeType_Type(Integer32):
    """Custom type hiplexAFSWUVolumeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("by-user", 4),
          ("private-disk", 3),
          ("pubset", 2),
          ("shared-pubset", 1),
          ("undefined", 255))
    )


_HiplexAFSWUVolumeType_Type.__name__ = "Integer32"
_HiplexAFSWUVolumeType_Object = MibTableColumn
hiplexAFSWUVolumeType = _HiplexAFSWUVolumeType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 6, 2, 1, 3),
    _HiplexAFSWUVolumeType_Type()
)
hiplexAFSWUVolumeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFSWUVolumeType.setStatus("mandatory")
_HiplexAFSWUVolumeImportProc_Type = DisplayString
_HiplexAFSWUVolumeImportProc_Object = MibTableColumn
hiplexAFSWUVolumeImportProc = _HiplexAFSWUVolumeImportProc_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 6, 2, 1, 4),
    _HiplexAFSWUVolumeImportProc_Type()
)
hiplexAFSWUVolumeImportProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFSWUVolumeImportProc.setStatus("mandatory")
_HiplexAFSWUVolumeExportProc_Type = DisplayString
_HiplexAFSWUVolumeExportProc_Object = MibTableColumn
hiplexAFSWUVolumeExportProc = _HiplexAFSWUVolumeExportProc_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 6, 2, 1, 5),
    _HiplexAFSWUVolumeExportProc_Type()
)
hiplexAFSWUVolumeExportProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFSWUVolumeExportProc.setStatus("mandatory")
_HiplexAFSWUApplicationInfo_ObjectIdentity = ObjectIdentity
hiplexAFSWUApplicationInfo = _HiplexAFSWUApplicationInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 7)
)
_HiplexAFSWUApplicationTabNum_Type = Integer32
_HiplexAFSWUApplicationTabNum_Object = MibScalar
hiplexAFSWUApplicationTabNum = _HiplexAFSWUApplicationTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 7, 1),
    _HiplexAFSWUApplicationTabNum_Type()
)
hiplexAFSWUApplicationTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFSWUApplicationTabNum.setStatus("mandatory")
_HiplexAFSWUApplicationTable_Object = MibTable
hiplexAFSWUApplicationTable = _HiplexAFSWUApplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 7, 2)
)
if mibBuilder.loadTexts:
    hiplexAFSWUApplicationTable.setStatus("mandatory")
_HiplexAFSWUApplicationEntry_Object = MibTableRow
hiplexAFSWUApplicationEntry = _HiplexAFSWUApplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 7, 2, 1)
)
hiplexAFSWUApplicationEntry.setIndexNames(
    (0, "HiplexAF-MIB", "hiplexAFSWUName"),
    (0, "HiplexAF-MIB", "hiplexAFSWUApplicationMonJVName"),
)
if mibBuilder.loadTexts:
    hiplexAFSWUApplicationEntry.setStatus("mandatory")
_HiplexAFSWUApplicationMonJVName_Type = DisplayString
_HiplexAFSWUApplicationMonJVName_Object = MibTableColumn
hiplexAFSWUApplicationMonJVName = _HiplexAFSWUApplicationMonJVName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 7, 2, 1, 1),
    _HiplexAFSWUApplicationMonJVName_Type()
)
hiplexAFSWUApplicationMonJVName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFSWUApplicationMonJVName.setStatus("mandatory")


class _HiplexAFSWUApplicationType_Type(Integer32):
    """Custom type hiplexAFSWUApplicationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("bcam", 3),
          ("by-user", 4),
          ("job", 1),
          ("undefined", 255),
          ("utm", 2))
    )


_HiplexAFSWUApplicationType_Type.__name__ = "Integer32"
_HiplexAFSWUApplicationType_Object = MibTableColumn
hiplexAFSWUApplicationType = _HiplexAFSWUApplicationType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 7, 2, 1, 2),
    _HiplexAFSWUApplicationType_Type()
)
hiplexAFSWUApplicationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFSWUApplicationType.setStatus("mandatory")
_HiplexAFSWUApplicationStartProc_Type = DisplayString
_HiplexAFSWUApplicationStartProc_Object = MibTableColumn
hiplexAFSWUApplicationStartProc = _HiplexAFSWUApplicationStartProc_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 7, 2, 1, 3),
    _HiplexAFSWUApplicationStartProc_Type()
)
hiplexAFSWUApplicationStartProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFSWUApplicationStartProc.setStatus("mandatory")
_HiplexAFSWUApplicationStopProc_Type = DisplayString
_HiplexAFSWUApplicationStopProc_Object = MibTableColumn
hiplexAFSWUApplicationStopProc = _HiplexAFSWUApplicationStopProc_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 7, 2, 1, 4),
    _HiplexAFSWUApplicationStopProc_Type()
)
hiplexAFSWUApplicationStopProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFSWUApplicationStopProc.setStatus("mandatory")
_HiplexAFPubsetVolumeInfo_ObjectIdentity = ObjectIdentity
hiplexAFPubsetVolumeInfo = _HiplexAFPubsetVolumeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 8)
)
_HiplexAFTrapFilterTable_Object = MibTable
hiplexAFTrapFilterTable = _HiplexAFTrapFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 20)
)
if mibBuilder.loadTexts:
    hiplexAFTrapFilterTable.setStatus("mandatory")
_HiplexAFTrapFilterEntry_Object = MibTableRow
hiplexAFTrapFilterEntry = _HiplexAFTrapFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 20, 1)
)
hiplexAFTrapFilterEntry.setIndexNames(
    (0, "HiplexAF-MIB", "hiplexAFTrapFilterHost1Name"),
    (0, "HiplexAF-MIB", "hiplexAFTrapFilterHost2Name"),
)
if mibBuilder.loadTexts:
    hiplexAFTrapFilterEntry.setStatus("mandatory")
_HiplexAFTrapFilterHost1Name_Type = DisplayString
_HiplexAFTrapFilterHost1Name_Object = MibTableColumn
hiplexAFTrapFilterHost1Name = _HiplexAFTrapFilterHost1Name_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 20, 1, 1),
    _HiplexAFTrapFilterHost1Name_Type()
)
hiplexAFTrapFilterHost1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFTrapFilterHost1Name.setStatus("mandatory")
_HiplexAFTrapFilterHost2Name_Type = DisplayString
_HiplexAFTrapFilterHost2Name_Object = MibTableColumn
hiplexAFTrapFilterHost2Name = _HiplexAFTrapFilterHost2Name_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 20, 1, 2),
    _HiplexAFTrapFilterHost2Name_Type()
)
hiplexAFTrapFilterHost2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiplexAFTrapFilterHost2Name.setStatus("mandatory")


class _HiplexAFTrapFilterTrapSendInd_Type(Integer32):
    """Custom type hiplexAFTrapFilterTrapSendInd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("undefined", 255),
          ("yes", 1))
    )


_HiplexAFTrapFilterTrapSendInd_Type.__name__ = "Integer32"
_HiplexAFTrapFilterTrapSendInd_Object = MibTableColumn
hiplexAFTrapFilterTrapSendInd = _HiplexAFTrapFilterTrapSendInd_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 1, 20, 1, 3),
    _HiplexAFTrapFilterTrapSendInd_Type()
)
hiplexAFTrapFilterTrapSendInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hiplexAFTrapFilterTrapSendInd.setStatus("mandatory")
_HiplexAFTraps_ObjectIdentity = ObjectIdentity
hiplexAFTraps = _HiplexAFTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 2)
)

# Managed Objects groups


# Notification objects

hiplexAFStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 2, 0, 301)
)
hiplexAFStart.setObjects(
    ("HiplexAF-MIB", "hiplexAFHostName")
)
if mibBuilder.loadTexts:
    hiplexAFStart.setStatus(
        ""
    )

hiplexAFSWUStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 2, 0, 302)
)
hiplexAFSWUStart.setObjects(
      *(("HiplexAF-MIB", "hiplexAFSWUHostParamStateInd"),
        ("HiplexAF-MIB", "hiplexAFSWUName"),
        ("HiplexAF-MIB", "hiplexAFHostName"))
)
if mibBuilder.loadTexts:
    hiplexAFSWUStart.setStatus(
        ""
    )

hiplexAFStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 2, 0, 303)
)
hiplexAFStop.setObjects(
    ("HiplexAF-MIB", "hiplexAFTermHost")
)
if mibBuilder.loadTexts:
    hiplexAFStop.setStatus(
        ""
    )

hiplexAFCrash = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 2, 0, 304)
)
hiplexAFCrash.setObjects(
    ("HiplexAF-MIB", "hiplexAFHostName")
)
if mibBuilder.loadTexts:
    hiplexAFCrash.setStatus(
        ""
    )

hiplexAFSWUAppStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 2, 0, 305)
)
hiplexAFSWUAppStop.setObjects(
      *(("HiplexAF-MIB", "hiplexAFSWUHostParamStateInd"),
        ("HiplexAF-MIB", "hiplexAFSWUName"),
        ("HiplexAF-MIB", "hiplexAFHostName"))
)
if mibBuilder.loadTexts:
    hiplexAFSWUAppStop.setStatus(
        ""
    )

hiplexAFSWUAppStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 2, 0, 306)
)
hiplexAFSWUAppStart.setObjects(
      *(("HiplexAF-MIB", "hiplexAFSWUHostParamStateInd"),
        ("HiplexAF-MIB", "hiplexAFSWUName"),
        ("HiplexAF-MIB", "hiplexAFHostName"))
)
if mibBuilder.loadTexts:
    hiplexAFSWUAppStart.setStatus(
        ""
    )

hiplexAFSWUStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 35, 2, 0, 307)
)
hiplexAFSWUStop.setObjects(
      *(("HiplexAF-MIB", "hiplexAFSWUHostParamStateInd"),
        ("HiplexAF-MIB", "hiplexAFSWUName"),
        ("HiplexAF-MIB", "hiplexAFHostName"))
)
if mibBuilder.loadTexts:
    hiplexAFSWUStop.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HiplexAF-MIB",
    **{"sni": sni,
       "sniProductMibs": sniProductMibs,
       "sniHiplexAF": sniHiplexAF,
       "hiplexAFObjects": hiplexAFObjects,
       "hiplexAFGlobalData": hiplexAFGlobalData,
       "hiplexAFVersion": hiplexAFVersion,
       "hiplexAFSPVSUserid": hiplexAFSPVSUserid,
       "hiplexAFSPVSCatid": hiplexAFSPVSCatid,
       "hiplexAFState": hiplexAFState,
       "hiplexAFTermHost": hiplexAFTermHost,
       "hiplexAFHostInfo": hiplexAFHostInfo,
       "hiplexAFHostTabNum": hiplexAFHostTabNum,
       "hiplexAFHostTable": hiplexAFHostTable,
       "hiplexAFHostEntry": hiplexAFHostEntry,
       "hiplexAFHostName": hiplexAFHostName,
       "hiplexAFHostEventId": hiplexAFHostEventId,
       "hiplexAFHostStateInd": hiplexAFHostStateInd,
       "hiplexAFHostOperatorRole": hiplexAFHostOperatorRole,
       "hiplexAFHostHomeCatid": hiplexAFHostHomeCatid,
       "hiplexAFHostSystemId": hiplexAFHostSystemId,
       "hiplexAFHostBS2Version": hiplexAFHostBS2Version,
       "hiplexAFHostImcatInd": hiplexAFHostImcatInd,
       "hiplexAFHostMasterSlaveInd": hiplexAFHostMasterSlaveInd,
       "hiplexAFHostSnmpAgentStateInd": hiplexAFHostSnmpAgentStateInd,
       "hiplexAFSWUInfo": hiplexAFSWUInfo,
       "hiplexAFSWUTabNum": hiplexAFSWUTabNum,
       "hiplexAFSWUTable": hiplexAFSWUTable,
       "hiplexAFSWUEntry": hiplexAFSWUEntry,
       "hiplexAFSWUName": hiplexAFSWUName,
       "hiplexAFSWUCreaTime": hiplexAFSWUCreaTime,
       "hiplexAFSWUWorkSystem": hiplexAFSWUWorkSystem,
       "hiplexAFSWUVirtHost": hiplexAFSWUVirtHost,
       "hiplexAFSWUVirtHostAct": hiplexAFSWUVirtHostAct,
       "hiplexAFSWUVirtHostDeact": hiplexAFSWUVirtHostDeact,
       "hiplexAFSWUFEPNumber": hiplexAFSWUFEPNumber,
       "hiplexAFSWUPubsetNumber": hiplexAFSWUPubsetNumber,
       "hiplexAFSWUApplicationNumber": hiplexAFSWUApplicationNumber,
       "hiplexAFSWUHostParamInfo": hiplexAFSWUHostParamInfo,
       "hiplexAFSWUHostParamTable": hiplexAFSWUHostParamTable,
       "hiplexAFSWUHostParamEntry": hiplexAFSWUHostParamEntry,
       "hiplexAFSWUHostParamEventId": hiplexAFSWUHostParamEventId,
       "hiplexAFSWUHostParamStateInd": hiplexAFSWUHostParamStateInd,
       "hiplexAFSWUHostParamPriority": hiplexAFSWUHostParamPriority,
       "hiplexAFSWUHostParamOperatorRole": hiplexAFSWUHostParamOperatorRole,
       "hiplexAFSWUHostFEPInfo": hiplexAFSWUHostFEPInfo,
       "hiplexAFSWUHostFEPTabNum": hiplexAFSWUHostFEPTabNum,
       "hiplexAFSWUHostFEPTable": hiplexAFSWUHostFEPTable,
       "hiplexAFSWUHostFEPEntry": hiplexAFSWUHostFEPEntry,
       "hiplexAFSWUHostFEPIndex": hiplexAFSWUHostFEPIndex,
       "hiplexAFSWUHostFEPName": hiplexAFSWUHostFEPName,
       "hiplexAFSWUHostFEPPortnumber": hiplexAFSWUHostFEPPortnumber,
       "hiplexAFSWUVolumeInfo": hiplexAFSWUVolumeInfo,
       "hiplexAFSWUVolumeTabNum": hiplexAFSWUVolumeTabNum,
       "hiplexAFSWUVolumeTable": hiplexAFSWUVolumeTable,
       "hiplexAFSWUVolumeEntry": hiplexAFSWUVolumeEntry,
       "hiplexAFSWUVolumeName": hiplexAFSWUVolumeName,
       "hiplexAFSWUVolumeTypeName": hiplexAFSWUVolumeTypeName,
       "hiplexAFSWUVolumeType": hiplexAFSWUVolumeType,
       "hiplexAFSWUVolumeImportProc": hiplexAFSWUVolumeImportProc,
       "hiplexAFSWUVolumeExportProc": hiplexAFSWUVolumeExportProc,
       "hiplexAFSWUApplicationInfo": hiplexAFSWUApplicationInfo,
       "hiplexAFSWUApplicationTabNum": hiplexAFSWUApplicationTabNum,
       "hiplexAFSWUApplicationTable": hiplexAFSWUApplicationTable,
       "hiplexAFSWUApplicationEntry": hiplexAFSWUApplicationEntry,
       "hiplexAFSWUApplicationMonJVName": hiplexAFSWUApplicationMonJVName,
       "hiplexAFSWUApplicationType": hiplexAFSWUApplicationType,
       "hiplexAFSWUApplicationStartProc": hiplexAFSWUApplicationStartProc,
       "hiplexAFSWUApplicationStopProc": hiplexAFSWUApplicationStopProc,
       "hiplexAFPubsetVolumeInfo": hiplexAFPubsetVolumeInfo,
       "hiplexAFTrapFilterTable": hiplexAFTrapFilterTable,
       "hiplexAFTrapFilterEntry": hiplexAFTrapFilterEntry,
       "hiplexAFTrapFilterHost1Name": hiplexAFTrapFilterHost1Name,
       "hiplexAFTrapFilterHost2Name": hiplexAFTrapFilterHost2Name,
       "hiplexAFTrapFilterTrapSendInd": hiplexAFTrapFilterTrapSendInd,
       "hiplexAFTraps": hiplexAFTraps,
       "hiplexAFStart": hiplexAFStart,
       "hiplexAFSWUStart": hiplexAFSWUStart,
       "hiplexAFStop": hiplexAFStop,
       "hiplexAFCrash": hiplexAFCrash,
       "hiplexAFSWUAppStop": hiplexAFSWUAppStop,
       "hiplexAFSWUAppStart": hiplexAFSWUAppStart,
       "hiplexAFSWUStop": hiplexAFSWUStop}
)
