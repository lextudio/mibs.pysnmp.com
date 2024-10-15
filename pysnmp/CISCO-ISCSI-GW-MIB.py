# SNMP MIB module (CISCO-ISCSI-GW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ISCSI-GW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:07 2024
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

(cIscsiInstIndex,
 cIscsiInstanceAttributesEntry,
 cIscsiNodeAttributesEntry,
 cIscsiSessionAttributesEntry) = mibBuilder.importSymbols(
    "CISCO-ISCSI-MIB",
    "cIscsiInstIndex",
    "cIscsiInstanceAttributesEntry",
    "cIscsiNodeAttributesEntry",
    "cIscsiSessionAttributesEntry")

(ScsiLUNOrZero,
 ScsiName,
 ciscoScsiLuEntry) = mibBuilder.importSymbols(
    "CISCO-SCSI-MIB",
    "ScsiLUNOrZero",
    "ScsiName",
    "ciscoScsiLuEntry")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(FcNameId,
 FcNameIdOrZero,
 VsanIndex) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "FcNameId",
    "FcNameIdOrZero",
    "VsanIndex")

(CiscoPort,
 ListIndex,
 ListIndexOrZero) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoPort",
    "ListIndex",
    "ListIndexOrZero")

(FcList,) = mibBuilder.importSymbols(
    "CISCO-ZS-MIB",
    "FcList")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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

ciscoIscsiGwMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 317)
)
ciscoIscsiGwMIB.setRevisions(
        ("2005-04-29 00:00",
         "2004-11-16 00:00",
         "2003-12-08 00:00",
         "2003-11-14 00:00",
         "2003-08-18 00:00",
         "2003-05-22 00:00",
         "2003-04-10 00:00",
         "2003-02-11 00:00",
         "2002-10-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CIscsiTargetDomains(Bits, TextualConvention):
    status = "current"


class CIscsiNodeRoles(Bits, TextualConvention):
    status = "current"


class IscsiName(OctetString, TextualConvention):
    status = "current"
    displayHint = "223a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 223),
    )



class IscsiAuthMethod(Bits, TextualConvention):
    status = "current"


class CIscsiIntrIdentificationMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipaddress", 2),
          ("name", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoiScsiGwMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoiScsiGwMIBNotifications = _CiscoiScsiGwMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 0)
)
_CiscoiScsiGwMIBObjects_ObjectIdentity = ObjectIdentity
ciscoiScsiGwMIBObjects = _CiscoiScsiGwMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1)
)
_CiScsiConfig_ObjectIdentity = ObjectIdentity
ciScsiConfig = _CiScsiConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1)
)
_IscsiImprtExprtTgtsConfTable_Object = MibTable
iscsiImprtExprtTgtsConfTable = _IscsiImprtExprtTgtsConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 1)
)
if mibBuilder.loadTexts:
    iscsiImprtExprtTgtsConfTable.setStatus("current")
_IscsiImprtExprtTgtsConfEntry_Object = MibTableRow
iscsiImprtExprtTgtsConfEntry = _IscsiImprtExprtTgtsConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    iscsiImprtExprtTgtsConfEntry.setStatus("current")


class _IscsiImprtExprtTgtsConfImport_Type(CIscsiTargetDomains):
    """Custom type iscsiImprtExprtTgtsConfImport based on CIscsiTargetDomains"""
    defaultBinValue = "0"


_IscsiImprtExprtTgtsConfImport_Object = MibTableColumn
iscsiImprtExprtTgtsConfImport = _IscsiImprtExprtTgtsConfImport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 1, 1, 1),
    _IscsiImprtExprtTgtsConfImport_Type()
)
iscsiImprtExprtTgtsConfImport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiImprtExprtTgtsConfImport.setStatus("current")


class _IscsiImprtExprtTgtsConfExport_Type(CIscsiTargetDomains):
    """Custom type iscsiImprtExprtTgtsConfExport based on CIscsiTargetDomains"""
    defaultBinValue = "0"


_IscsiImprtExprtTgtsConfExport_Object = MibTableColumn
iscsiImprtExprtTgtsConfExport = _IscsiImprtExprtTgtsConfExport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 1, 1, 2),
    _IscsiImprtExprtTgtsConfExport_Type()
)
iscsiImprtExprtTgtsConfExport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiImprtExprtTgtsConfExport.setStatus("current")


class _IscsiAuthMethod_Type(IscsiAuthMethod):
    """Custom type iscsiAuthMethod based on IscsiAuthMethod"""
    defaultBinValue = "0"


_IscsiAuthMethod_Object = MibScalar
iscsiAuthMethod = _IscsiAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 2),
    _IscsiAuthMethod_Type()
)
iscsiAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiAuthMethod.setStatus("current")
_Iscsi2FcNodeTable_Object = MibTable
iscsi2FcNodeTable = _Iscsi2FcNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 3)
)
if mibBuilder.loadTexts:
    iscsi2FcNodeTable.setStatus("current")
_Iscsi2FcNodeEntry_Object = MibTableRow
iscsi2FcNodeEntry = _Iscsi2FcNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 3, 1)
)
iscsi2FcNodeEntry.setIndexNames(
    (0, "CISCO-ISCSI-MIB", "cIscsiInstIndex"),
    (0, "CISCO-ISCSI-GW-MIB", "iscsi2FcNodeIndex"),
)
if mibBuilder.loadTexts:
    iscsi2FcNodeEntry.setStatus("current")


class _Iscsi2FcNodeIndex_Type(Unsigned32):
    """Custom type iscsi2FcNodeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Iscsi2FcNodeIndex_Type.__name__ = "Unsigned32"
_Iscsi2FcNodeIndex_Object = MibTableColumn
iscsi2FcNodeIndex = _Iscsi2FcNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 3, 1, 1),
    _Iscsi2FcNodeIndex_Type()
)
iscsi2FcNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iscsi2FcNodeIndex.setStatus("current")
_Iscsi2FcNodeName_Type = IscsiName
_Iscsi2FcNodeName_Object = MibTableColumn
iscsi2FcNodeName = _Iscsi2FcNodeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 3, 1, 2),
    _Iscsi2FcNodeName_Type()
)
iscsi2FcNodeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsi2FcNodeName.setStatus("current")
_Iscsi2FcNodeRole_Type = CIscsiNodeRoles
_Iscsi2FcNodeRole_Object = MibTableColumn
iscsi2FcNodeRole = _Iscsi2FcNodeRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 3, 1, 3),
    _Iscsi2FcNodeRole_Type()
)
iscsi2FcNodeRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsi2FcNodeRole.setStatus("current")
_Iscsi2FcNodePersistentFCAddr_Type = TruthValue
_Iscsi2FcNodePersistentFCAddr_Object = MibTableColumn
iscsi2FcNodePersistentFCAddr = _Iscsi2FcNodePersistentFCAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 3, 1, 4),
    _Iscsi2FcNodePersistentFCAddr_Type()
)
iscsi2FcNodePersistentFCAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsi2FcNodePersistentFCAddr.setStatus("current")
_Iscsi2FcPortPersistentFCAddr_Type = TruthValue
_Iscsi2FcPortPersistentFCAddr_Object = MibTableColumn
iscsi2FcPortPersistentFCAddr = _Iscsi2FcPortPersistentFCAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 3, 1, 5),
    _Iscsi2FcPortPersistentFCAddr_Type()
)
iscsi2FcPortPersistentFCAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsi2FcPortPersistentFCAddr.setStatus("current")


class _Iscsi2FcPortNumFCAddr_Type(Unsigned32):
    """Custom type iscsi2FcPortNumFCAddr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Iscsi2FcPortNumFCAddr_Type.__name__ = "Unsigned32"
_Iscsi2FcPortNumFCAddr_Object = MibTableColumn
iscsi2FcPortNumFCAddr = _Iscsi2FcPortNumFCAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 3, 1, 6),
    _Iscsi2FcPortNumFCAddr_Type()
)
iscsi2FcPortNumFCAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsi2FcPortNumFCAddr.setStatus("current")
_Iscsi2FcNodeFCAddr_Type = FcNameIdOrZero
_Iscsi2FcNodeFCAddr_Object = MibTableColumn
iscsi2FcNodeFCAddr = _Iscsi2FcNodeFCAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 3, 1, 7),
    _Iscsi2FcNodeFCAddr_Type()
)
iscsi2FcNodeFCAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsi2FcNodeFCAddr.setStatus("current")
_Iscsi2FcPortFCAddrListIndex_Type = ListIndexOrZero
_Iscsi2FcPortFCAddrListIndex_Object = MibTableColumn
iscsi2FcPortFCAddrListIndex = _Iscsi2FcPortFCAddrListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 3, 1, 8),
    _Iscsi2FcPortFCAddrListIndex_Type()
)
iscsi2FcPortFCAddrListIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsi2FcPortFCAddrListIndex.setStatus("current")


class _Iscsi2FcNodeVsanList2k_Type(FcList):
    """Custom type iscsi2FcNodeVsanList2k based on FcList"""
    defaultHexValue = ""


_Iscsi2FcNodeVsanList2k_Object = MibTableColumn
iscsi2FcNodeVsanList2k = _Iscsi2FcNodeVsanList2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 3, 1, 9),
    _Iscsi2FcNodeVsanList2k_Type()
)
iscsi2FcNodeVsanList2k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsi2FcNodeVsanList2k.setStatus("current")


class _Iscsi2FcNodeVsanList4k_Type(FcList):
    """Custom type iscsi2FcNodeVsanList4k based on FcList"""
    defaultHexValue = ""


_Iscsi2FcNodeVsanList4k_Object = MibTableColumn
iscsi2FcNodeVsanList4k = _Iscsi2FcNodeVsanList4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 3, 1, 10),
    _Iscsi2FcNodeVsanList4k_Type()
)
iscsi2FcNodeVsanList4k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsi2FcNodeVsanList4k.setStatus("current")
_Iscsi2FcNodeDiscovered_Type = TruthValue
_Iscsi2FcNodeDiscovered_Object = MibTableColumn
iscsi2FcNodeDiscovered = _Iscsi2FcNodeDiscovered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 3, 1, 11),
    _Iscsi2FcNodeDiscovered_Type()
)
iscsi2FcNodeDiscovered.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsi2FcNodeDiscovered.setStatus("current")
_Iscsi2FcNodeRowStatus_Type = RowStatus
_Iscsi2FcNodeRowStatus_Object = MibTableColumn
iscsi2FcNodeRowStatus = _Iscsi2FcNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 3, 1, 12),
    _Iscsi2FcNodeRowStatus_Type()
)
iscsi2FcNodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsi2FcNodeRowStatus.setStatus("current")


class _Iscsi2FcNodeFcAddrAssignment_Type(Integer32):
    """Custom type iscsi2FcNodeFcAddrAssignment based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_Iscsi2FcNodeFcAddrAssignment_Type.__name__ = "Integer32"
_Iscsi2FcNodeFcAddrAssignment_Object = MibTableColumn
iscsi2FcNodeFcAddrAssignment = _Iscsi2FcNodeFcAddrAssignment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 3, 1, 13),
    _Iscsi2FcNodeFcAddrAssignment_Type()
)
iscsi2FcNodeFcAddrAssignment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsi2FcNodeFcAddrAssignment.setStatus("current")


class _Iscsi2FcNodeAuthUser_Type(SnmpAdminString):
    """Custom type iscsi2FcNodeAuthUser based on SnmpAdminString"""
    defaultHexValue = ""


_Iscsi2FcNodeAuthUser_Object = MibTableColumn
iscsi2FcNodeAuthUser = _Iscsi2FcNodeAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 3, 1, 14),
    _Iscsi2FcNodeAuthUser_Type()
)
iscsi2FcNodeAuthUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsi2FcNodeAuthUser.setStatus("current")


class _Iscsi2FcTargetUserName_Type(SnmpAdminString):
    """Custom type iscsi2FcTargetUserName based on SnmpAdminString"""
    defaultHexValue = ""


_Iscsi2FcTargetUserName_Object = MibTableColumn
iscsi2FcTargetUserName = _Iscsi2FcTargetUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 3, 1, 15),
    _Iscsi2FcTargetUserName_Type()
)
iscsi2FcTargetUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsi2FcTargetUserName.setStatus("current")


class _Iscsi2FcTargetPassword_Type(SnmpAdminString):
    """Custom type iscsi2FcTargetPassword based on SnmpAdminString"""
    defaultHexValue = ""


_Iscsi2FcTargetPassword_Object = MibTableColumn
iscsi2FcTargetPassword = _Iscsi2FcTargetPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 3, 1, 16),
    _Iscsi2FcTargetPassword_Type()
)
iscsi2FcTargetPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsi2FcTargetPassword.setStatus("current")
_Fc2IscsiNodeTable_Object = MibTable
fc2IscsiNodeTable = _Fc2IscsiNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 4)
)
if mibBuilder.loadTexts:
    fc2IscsiNodeTable.setStatus("current")
_Fc2IscsiNodeEntry_Object = MibTableRow
fc2IscsiNodeEntry = _Fc2IscsiNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    fc2IscsiNodeEntry.setStatus("current")
_Fc2IscsiNodeRole_Type = CIscsiNodeRoles
_Fc2IscsiNodeRole_Object = MibTableColumn
fc2IscsiNodeRole = _Fc2IscsiNodeRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 4, 1, 1),
    _Fc2IscsiNodeRole_Type()
)
fc2IscsiNodeRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fc2IscsiNodeRole.setStatus("current")
_Fc2IscsiNodeName_Type = IscsiName
_Fc2IscsiNodeName_Object = MibTableColumn
fc2IscsiNodeName = _Fc2IscsiNodeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 4, 1, 2),
    _Fc2IscsiNodeName_Type()
)
fc2IscsiNodeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fc2IscsiNodeName.setStatus("current")
_Fc2IscsiPortFCAddrListIndex_Type = ListIndexOrZero
_Fc2IscsiPortFCAddrListIndex_Object = MibTableColumn
fc2IscsiPortFCAddrListIndex = _Fc2IscsiPortFCAddrListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 4, 1, 3),
    _Fc2IscsiPortFCAddrListIndex_Type()
)
fc2IscsiPortFCAddrListIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fc2IscsiPortFCAddrListIndex.setStatus("current")
_Fc2IscsiNodePermitListIndex_Type = ListIndexOrZero
_Fc2IscsiNodePermitListIndex_Object = MibTableColumn
fc2IscsiNodePermitListIndex = _Fc2IscsiNodePermitListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 4, 1, 4),
    _Fc2IscsiNodePermitListIndex_Type()
)
fc2IscsiNodePermitListIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fc2IscsiNodePermitListIndex.setStatus("current")
_Fc2IscsiNodeAdvIntfListIndex_Type = ListIndexOrZero
_Fc2IscsiNodeAdvIntfListIndex_Object = MibTableColumn
fc2IscsiNodeAdvIntfListIndex = _Fc2IscsiNodeAdvIntfListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 4, 1, 5),
    _Fc2IscsiNodeAdvIntfListIndex_Type()
)
fc2IscsiNodeAdvIntfListIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fc2IscsiNodeAdvIntfListIndex.setStatus("current")


class _Fc2IscsiNodeAllIntrAccessAllowed_Type(TruthValue):
    """Custom type fc2IscsiNodeAllIntrAccessAllowed based on TruthValue"""


_Fc2IscsiNodeAllIntrAccessAllowed_Object = MibTableColumn
fc2IscsiNodeAllIntrAccessAllowed = _Fc2IscsiNodeAllIntrAccessAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 4, 1, 6),
    _Fc2IscsiNodeAllIntrAccessAllowed_Type()
)
fc2IscsiNodeAllIntrAccessAllowed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fc2IscsiNodeAllIntrAccessAllowed.setStatus("current")
_Fc2IscsiNodeDiscovered_Type = TruthValue
_Fc2IscsiNodeDiscovered_Object = MibTableColumn
fc2IscsiNodeDiscovered = _Fc2IscsiNodeDiscovered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 4, 1, 7),
    _Fc2IscsiNodeDiscovered_Type()
)
fc2IscsiNodeDiscovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc2IscsiNodeDiscovered.setStatus("current")
_Fc2IscsiNodeRowStatus_Type = RowStatus
_Fc2IscsiNodeRowStatus_Object = MibTableColumn
fc2IscsiNodeRowStatus = _Fc2IscsiNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 4, 1, 8),
    _Fc2IscsiNodeRowStatus_Type()
)
fc2IscsiNodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fc2IscsiNodeRowStatus.setStatus("current")


class _Fc2IscsiNodeTrespassMode_Type(TruthValue):
    """Custom type fc2IscsiNodeTrespassMode based on TruthValue"""


_Fc2IscsiNodeTrespassMode_Object = MibTableColumn
fc2IscsiNodeTrespassMode = _Fc2IscsiNodeTrespassMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 4, 1, 9),
    _Fc2IscsiNodeTrespassMode_Type()
)
fc2IscsiNodeTrespassMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fc2IscsiNodeTrespassMode.setStatus("current")


class _Fc2IscsiNodeRevertToPrimaryPort_Type(TruthValue):
    """Custom type fc2IscsiNodeRevertToPrimaryPort based on TruthValue"""


_Fc2IscsiNodeRevertToPrimaryPort_Object = MibTableColumn
fc2IscsiNodeRevertToPrimaryPort = _Fc2IscsiNodeRevertToPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 4, 1, 10),
    _Fc2IscsiNodeRevertToPrimaryPort_Type()
)
fc2IscsiNodeRevertToPrimaryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fc2IscsiNodeRevertToPrimaryPort.setStatus("current")
_FcAddressListTable_Object = MibTable
fcAddressListTable = _FcAddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 5)
)
if mibBuilder.loadTexts:
    fcAddressListTable.setStatus("current")
_FcAddressListEntry_Object = MibTableRow
fcAddressListEntry = _FcAddressListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 5, 1)
)
fcAddressListEntry.setIndexNames(
    (0, "CISCO-ISCSI-GW-MIB", "fcAddressListIndex"),
    (0, "CISCO-ISCSI-GW-MIB", "fcAddressIndex"),
)
if mibBuilder.loadTexts:
    fcAddressListEntry.setStatus("current")
_FcAddressListIndex_Type = ListIndex
_FcAddressListIndex_Object = MibTableColumn
fcAddressListIndex = _FcAddressListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 5, 1, 1),
    _FcAddressListIndex_Type()
)
fcAddressListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcAddressListIndex.setStatus("current")


class _FcAddressIndex_Type(Unsigned32):
    """Custom type fcAddressIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FcAddressIndex_Type.__name__ = "Unsigned32"
_FcAddressIndex_Object = MibTableColumn
fcAddressIndex = _FcAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 5, 1, 2),
    _FcAddressIndex_Type()
)
fcAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcAddressIndex.setStatus("current")
_FcAddress_Type = FcNameId
_FcAddress_Object = MibTableColumn
fcAddress = _FcAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 5, 1, 3),
    _FcAddress_Type()
)
fcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcAddress.setStatus("current")


class _FcSecondaryAddress_Type(FcNameIdOrZero):
    """Custom type fcSecondaryAddress based on FcNameIdOrZero"""
    defaultHexValue = ""


_FcSecondaryAddress_Object = MibTableColumn
fcSecondaryAddress = _FcSecondaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 5, 1, 4),
    _FcSecondaryAddress_Type()
)
fcSecondaryAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcSecondaryAddress.setStatus("current")
_FcAddressRowStatus_Type = RowStatus
_FcAddressRowStatus_Object = MibTableColumn
fcAddressRowStatus = _FcAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 5, 1, 5),
    _FcAddressRowStatus_Type()
)
fcAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcAddressRowStatus.setStatus("current")
_IscsiNodeNameListTable_Object = MibTable
iscsiNodeNameListTable = _IscsiNodeNameListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 6)
)
if mibBuilder.loadTexts:
    iscsiNodeNameListTable.setStatus("current")
_IscsiNodeNameListEntry_Object = MibTableRow
iscsiNodeNameListEntry = _IscsiNodeNameListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 6, 1)
)
iscsiNodeNameListEntry.setIndexNames(
    (0, "CISCO-ISCSI-GW-MIB", "iscsiNodeNameListIndex"),
    (0, "CISCO-ISCSI-GW-MIB", "iscsiNodeNameIndex"),
)
if mibBuilder.loadTexts:
    iscsiNodeNameListEntry.setStatus("current")
_IscsiNodeNameListIndex_Type = ListIndex
_IscsiNodeNameListIndex_Object = MibTableColumn
iscsiNodeNameListIndex = _IscsiNodeNameListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 6, 1, 1),
    _IscsiNodeNameListIndex_Type()
)
iscsiNodeNameListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iscsiNodeNameListIndex.setStatus("current")


class _IscsiNodeNameIndex_Type(Unsigned32):
    """Custom type iscsiNodeNameIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IscsiNodeNameIndex_Type.__name__ = "Unsigned32"
_IscsiNodeNameIndex_Object = MibTableColumn
iscsiNodeNameIndex = _IscsiNodeNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 6, 1, 2),
    _IscsiNodeNameIndex_Type()
)
iscsiNodeNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iscsiNodeNameIndex.setStatus("current")
_IscsiNodeName_Type = IscsiName
_IscsiNodeName_Object = MibTableColumn
iscsiNodeName = _IscsiNodeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 6, 1, 3),
    _IscsiNodeName_Type()
)
iscsiNodeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiNodeName.setStatus("current")
_IscsiNodeNameRowStatus_Type = RowStatus
_IscsiNodeNameRowStatus_Object = MibTableColumn
iscsiNodeNameRowStatus = _IscsiNodeNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 6, 1, 4),
    _IscsiNodeNameRowStatus_Type()
)
iscsiNodeNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiNodeNameRowStatus.setStatus("current")
_NodeAdvIntfListTable_Object = MibTable
nodeAdvIntfListTable = _NodeAdvIntfListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 7)
)
if mibBuilder.loadTexts:
    nodeAdvIntfListTable.setStatus("current")
_NodeAdvIntfListEntry_Object = MibTableRow
nodeAdvIntfListEntry = _NodeAdvIntfListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 7, 1)
)
nodeAdvIntfListEntry.setIndexNames(
    (0, "CISCO-ISCSI-GW-MIB", "nodeAdvIntfListIndex"),
    (0, "CISCO-ISCSI-GW-MIB", "nodeAdvIntfIndex"),
)
if mibBuilder.loadTexts:
    nodeAdvIntfListEntry.setStatus("current")


class _NodeAdvIntfListIndex_Type(Unsigned32):
    """Custom type nodeAdvIntfListIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NodeAdvIntfListIndex_Type.__name__ = "Unsigned32"
_NodeAdvIntfListIndex_Object = MibTableColumn
nodeAdvIntfListIndex = _NodeAdvIntfListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 7, 1, 1),
    _NodeAdvIntfListIndex_Type()
)
nodeAdvIntfListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nodeAdvIntfListIndex.setStatus("current")


class _NodeAdvIntfIndex_Type(Unsigned32):
    """Custom type nodeAdvIntfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NodeAdvIntfIndex_Type.__name__ = "Unsigned32"
_NodeAdvIntfIndex_Object = MibTableColumn
nodeAdvIntfIndex = _NodeAdvIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 7, 1, 2),
    _NodeAdvIntfIndex_Type()
)
nodeAdvIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nodeAdvIntfIndex.setStatus("current")
_NodeAdvIntfIfIndex_Type = InterfaceIndex
_NodeAdvIntfIfIndex_Object = MibTableColumn
nodeAdvIntfIfIndex = _NodeAdvIntfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 7, 1, 3),
    _NodeAdvIntfIfIndex_Type()
)
nodeAdvIntfIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nodeAdvIntfIfIndex.setStatus("current")
_NodeAdvIntfIfRowStatus_Type = RowStatus
_NodeAdvIntfIfRowStatus_Object = MibTableColumn
nodeAdvIntfIfRowStatus = _NodeAdvIntfIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 7, 1, 4),
    _NodeAdvIntfIfRowStatus_Type()
)
nodeAdvIntfIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nodeAdvIntfIfRowStatus.setStatus("current")
_ScsiLuExtTable_Object = MibTable
scsiLuExtTable = _ScsiLuExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 8)
)
if mibBuilder.loadTexts:
    scsiLuExtTable.setStatus("current")
_ScsiLuExtEntry_Object = MibTableRow
scsiLuExtEntry = _ScsiLuExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    scsiLuExtEntry.setStatus("current")
_ScsiLuExtRemotePortFcAddress_Type = FcNameId
_ScsiLuExtRemotePortFcAddress_Object = MibTableColumn
scsiLuExtRemotePortFcAddress = _ScsiLuExtRemotePortFcAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 8, 1, 1),
    _ScsiLuExtRemotePortFcAddress_Type()
)
scsiLuExtRemotePortFcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiLuExtRemotePortFcAddress.setStatus("current")


class _ScsiLuExtRemotePortSecFcAddress_Type(FcNameIdOrZero):
    """Custom type scsiLuExtRemotePortSecFcAddress based on FcNameIdOrZero"""
    defaultHexValue = ""


_ScsiLuExtRemotePortSecFcAddress_Object = MibTableColumn
scsiLuExtRemotePortSecFcAddress = _ScsiLuExtRemotePortSecFcAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 8, 1, 2),
    _ScsiLuExtRemotePortSecFcAddress_Type()
)
scsiLuExtRemotePortSecFcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiLuExtRemotePortSecFcAddress.setStatus("current")
_ScsiLuExtLocalTargetAddress_Type = ScsiName
_ScsiLuExtLocalTargetAddress_Object = MibTableColumn
scsiLuExtLocalTargetAddress = _ScsiLuExtLocalTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 8, 1, 3),
    _ScsiLuExtLocalTargetAddress_Type()
)
scsiLuExtLocalTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiLuExtLocalTargetAddress.setStatus("current")
_ScsiLuExtRemoteLun_Type = ScsiLUNOrZero
_ScsiLuExtRemoteLun_Object = MibTableColumn
scsiLuExtRemoteLun = _ScsiLuExtRemoteLun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 8, 1, 4),
    _ScsiLuExtRemoteLun_Type()
)
scsiLuExtRemoteLun.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiLuExtRemoteLun.setStatus("current")
_ScsiLuExtLocalLun_Type = ScsiLUNOrZero
_ScsiLuExtLocalLun_Object = MibTableColumn
scsiLuExtLocalLun = _ScsiLuExtLocalLun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 8, 1, 5),
    _ScsiLuExtLocalLun_Type()
)
scsiLuExtLocalLun.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiLuExtLocalLun.setStatus("current")
_ScsiLuExtRowStatus_Type = RowStatus
_ScsiLuExtRowStatus_Object = MibTableColumn
scsiLuExtRowStatus = _ScsiLuExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 8, 1, 6),
    _ScsiLuExtRowStatus_Type()
)
scsiLuExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiLuExtRowStatus.setStatus("current")
_ScsiLuExtRemoteSecLun_Type = ScsiLUNOrZero
_ScsiLuExtRemoteSecLun_Object = MibTableColumn
scsiLuExtRemoteSecLun = _ScsiLuExtRemoteSecLun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 8, 1, 7),
    _ScsiLuExtRemoteSecLun_Type()
)
scsiLuExtRemoteSecLun.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiLuExtRemoteSecLun.setStatus("current")
_IscsiIfTable_Object = MibTable
iscsiIfTable = _IscsiIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9)
)
if mibBuilder.loadTexts:
    iscsiIfTable.setStatus("current")
_IscsiIfEntry_Object = MibTableRow
iscsiIfEntry = _IscsiIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9, 1)
)
iscsiIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    iscsiIfEntry.setStatus("current")


class _IscsiIfTcpKeepAliveTimeout_Type(Unsigned32):
    """Custom type iscsiIfTcpKeepAliveTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7200),
    )


_IscsiIfTcpKeepAliveTimeout_Type.__name__ = "Unsigned32"
_IscsiIfTcpKeepAliveTimeout_Object = MibTableColumn
iscsiIfTcpKeepAliveTimeout = _IscsiIfTcpKeepAliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9, 1, 1),
    _IscsiIfTcpKeepAliveTimeout_Type()
)
iscsiIfTcpKeepAliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiIfTcpKeepAliveTimeout.setStatus("current")


class _IscsiIfTcpMaxBandwidth_Type(Unsigned32):
    """Custom type iscsiIfTcpMaxBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 1000000),
    )


_IscsiIfTcpMaxBandwidth_Type.__name__ = "Unsigned32"
_IscsiIfTcpMaxBandwidth_Object = MibTableColumn
iscsiIfTcpMaxBandwidth = _IscsiIfTcpMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9, 1, 2),
    _IscsiIfTcpMaxBandwidth_Type()
)
iscsiIfTcpMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiIfTcpMaxBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    iscsiIfTcpMaxBandwidth.setUnits("kbps")


class _IscsiIfTcpMaxRetransmissions_Type(Unsigned32):
    """Custom type iscsiIfTcpMaxRetransmissions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_IscsiIfTcpMaxRetransmissions_Type.__name__ = "Unsigned32"
_IscsiIfTcpMaxRetransmissions_Object = MibTableColumn
iscsiIfTcpMaxRetransmissions = _IscsiIfTcpMaxRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9, 1, 3),
    _IscsiIfTcpMaxRetransmissions_Type()
)
iscsiIfTcpMaxRetransmissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiIfTcpMaxRetransmissions.setStatus("current")


class _IscsiIfTcpMinRetransmitTime_Type(Unsigned32):
    """Custom type iscsiIfTcpMinRetransmitTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 5000),
    )


_IscsiIfTcpMinRetransmitTime_Type.__name__ = "Unsigned32"
_IscsiIfTcpMinRetransmitTime_Object = MibTableColumn
iscsiIfTcpMinRetransmitTime = _IscsiIfTcpMinRetransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9, 1, 4),
    _IscsiIfTcpMinRetransmitTime_Type()
)
iscsiIfTcpMinRetransmitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiIfTcpMinRetransmitTime.setStatus("current")
_IscsiIfTcpPMTUEnable_Type = TruthValue
_IscsiIfTcpPMTUEnable_Object = MibTableColumn
iscsiIfTcpPMTUEnable = _IscsiIfTcpPMTUEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9, 1, 5),
    _IscsiIfTcpPMTUEnable_Type()
)
iscsiIfTcpPMTUEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiIfTcpPMTUEnable.setStatus("current")


class _IscsiIfTcpQOS_Type(Unsigned32):
    """Custom type iscsiIfTcpQOS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_IscsiIfTcpQOS_Type.__name__ = "Unsigned32"
_IscsiIfTcpQOS_Object = MibTableColumn
iscsiIfTcpQOS = _IscsiIfTcpQOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9, 1, 6),
    _IscsiIfTcpQOS_Type()
)
iscsiIfTcpQOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiIfTcpQOS.setStatus("current")
_IscsiIfTcpSACKEnable_Type = TruthValue
_IscsiIfTcpSACKEnable_Object = MibTableColumn
iscsiIfTcpSACKEnable = _IscsiIfTcpSACKEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9, 1, 7),
    _IscsiIfTcpSACKEnable_Type()
)
iscsiIfTcpSACKEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiIfTcpSACKEnable.setStatus("current")


class _IscsiIfTcpSendBufferSize_Type(Unsigned32):
    """Custom type iscsiIfTcpSendBufferSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_IscsiIfTcpSendBufferSize_Type.__name__ = "Unsigned32"
_IscsiIfTcpSendBufferSize_Object = MibTableColumn
iscsiIfTcpSendBufferSize = _IscsiIfTcpSendBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9, 1, 8),
    _IscsiIfTcpSendBufferSize_Type()
)
iscsiIfTcpSendBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiIfTcpSendBufferSize.setStatus("current")


class _IscsiIfTcpMinBandwidth_Type(Unsigned32):
    """Custom type iscsiIfTcpMinBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 1000000),
    )


_IscsiIfTcpMinBandwidth_Type.__name__ = "Unsigned32"
_IscsiIfTcpMinBandwidth_Object = MibTableColumn
iscsiIfTcpMinBandwidth = _IscsiIfTcpMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9, 1, 9),
    _IscsiIfTcpMinBandwidth_Type()
)
iscsiIfTcpMinBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiIfTcpMinBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    iscsiIfTcpMinBandwidth.setUnits("kbps")


class _IscsiIfTcpPMTUResetTimeout_Type(Unsigned32):
    """Custom type iscsiIfTcpPMTUResetTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_IscsiIfTcpPMTUResetTimeout_Type.__name__ = "Unsigned32"
_IscsiIfTcpPMTUResetTimeout_Object = MibTableColumn
iscsiIfTcpPMTUResetTimeout = _IscsiIfTcpPMTUResetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9, 1, 10),
    _IscsiIfTcpPMTUResetTimeout_Type()
)
iscsiIfTcpPMTUResetTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiIfTcpPMTUResetTimeout.setStatus("current")
if mibBuilder.loadTexts:
    iscsiIfTcpPMTUResetTimeout.setUnits("seconds")
_IscsiIfTcpLocalPort_Type = CiscoPort
_IscsiIfTcpLocalPort_Object = MibTableColumn
iscsiIfTcpLocalPort = _IscsiIfTcpLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9, 1, 11),
    _IscsiIfTcpLocalPort_Type()
)
iscsiIfTcpLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIfTcpLocalPort.setStatus("deprecated")


class _IscsiIfForwardingMode_Type(Integer32):
    """Custom type iscsiIfForwardingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cutThrough", 4),
          ("passThrough", 1),
          ("storeAndForward", 2))
    )


_IscsiIfForwardingMode_Type.__name__ = "Integer32"
_IscsiIfForwardingMode_Object = MibTableColumn
iscsiIfForwardingMode = _IscsiIfForwardingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9, 1, 12),
    _IscsiIfForwardingMode_Type()
)
iscsiIfForwardingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiIfForwardingMode.setStatus("current")
_IscsiIfIntrProxyMode_Type = TruthValue
_IscsiIfIntrProxyMode_Object = MibTableColumn
iscsiIfIntrProxyMode = _IscsiIfIntrProxyMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9, 1, 13),
    _IscsiIfIntrProxyMode_Type()
)
iscsiIfIntrProxyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiIfIntrProxyMode.setStatus("current")
_IscsiIfIntrProxyModeNodeFcAddr_Type = FcNameIdOrZero
_IscsiIfIntrProxyModeNodeFcAddr_Object = MibTableColumn
iscsiIfIntrProxyModeNodeFcAddr = _IscsiIfIntrProxyModeNodeFcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9, 1, 14),
    _IscsiIfIntrProxyModeNodeFcAddr_Type()
)
iscsiIfIntrProxyModeNodeFcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiIfIntrProxyModeNodeFcAddr.setStatus("current")
_IscsiIfIntrProxyModePortFcAddr_Type = FcNameIdOrZero
_IscsiIfIntrProxyModePortFcAddr_Object = MibTableColumn
iscsiIfIntrProxyModePortFcAddr = _IscsiIfIntrProxyModePortFcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9, 1, 15),
    _IscsiIfIntrProxyModePortFcAddr_Type()
)
iscsiIfIntrProxyModePortFcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiIfIntrProxyModePortFcAddr.setStatus("current")


class _IscsiIfIntrProxyModeFcAddrAsgnmt_Type(Integer32):
    """Custom type iscsiIfIntrProxyModeFcAddrAsgnmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_IscsiIfIntrProxyModeFcAddrAsgnmt_Type.__name__ = "Integer32"
_IscsiIfIntrProxyModeFcAddrAsgnmt_Object = MibTableColumn
iscsiIfIntrProxyModeFcAddrAsgnmt = _IscsiIfIntrProxyModeFcAddrAsgnmt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9, 1, 16),
    _IscsiIfIntrProxyModeFcAddrAsgnmt_Type()
)
iscsiIfIntrProxyModeFcAddrAsgnmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiIfIntrProxyModeFcAddrAsgnmt.setStatus("current")
_IscsiIfIntrIdentificationMode_Type = CIscsiIntrIdentificationMode
_IscsiIfIntrIdentificationMode_Object = MibTableColumn
iscsiIfIntrIdentificationMode = _IscsiIfIntrIdentificationMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9, 1, 17),
    _IscsiIfIntrIdentificationMode_Type()
)
iscsiIfIntrIdentificationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiIfIntrIdentificationMode.setStatus("current")


class _IscsiIfTcpRndTrpTimeEst_Type(Unsigned32):
    """Custom type iscsiIfTcpRndTrpTimeEst based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300000),
    )


_IscsiIfTcpRndTrpTimeEst_Type.__name__ = "Unsigned32"
_IscsiIfTcpRndTrpTimeEst_Object = MibTableColumn
iscsiIfTcpRndTrpTimeEst = _IscsiIfTcpRndTrpTimeEst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9, 1, 18),
    _IscsiIfTcpRndTrpTimeEst_Type()
)
iscsiIfTcpRndTrpTimeEst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiIfTcpRndTrpTimeEst.setStatus("current")
if mibBuilder.loadTexts:
    iscsiIfTcpRndTrpTimeEst.setUnits("microseconds")
_IscsiIfTcpLocalTcpPort_Type = CiscoPort
_IscsiIfTcpLocalTcpPort_Object = MibTableColumn
iscsiIfTcpLocalTcpPort = _IscsiIfTcpLocalTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9, 1, 19),
    _IscsiIfTcpLocalTcpPort_Type()
)
iscsiIfTcpLocalTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiIfTcpLocalTcpPort.setStatus("current")
_IscsiIfNumNormalConnections_Type = Unsigned32
_IscsiIfNumNormalConnections_Object = MibTableColumn
iscsiIfNumNormalConnections = _IscsiIfNumNormalConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9, 1, 20),
    _IscsiIfNumNormalConnections_Type()
)
iscsiIfNumNormalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIfNumNormalConnections.setStatus("current")
_IscsiIfNumDiscovConnections_Type = Unsigned32
_IscsiIfNumDiscovConnections_Object = MibTableColumn
iscsiIfNumDiscovConnections = _IscsiIfNumDiscovConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9, 1, 21),
    _IscsiIfNumDiscovConnections_Type()
)
iscsiIfNumDiscovConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIfNumDiscovConnections.setStatus("current")


class _IscsiIfTcpCWMEnable_Type(TruthValue):
    """Custom type iscsiIfTcpCWMEnable based on TruthValue"""


_IscsiIfTcpCWMEnable_Object = MibTableColumn
iscsiIfTcpCWMEnable = _IscsiIfTcpCWMEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9, 1, 22),
    _IscsiIfTcpCWMEnable_Type()
)
iscsiIfTcpCWMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiIfTcpCWMEnable.setStatus("current")


class _IscsiIfTcpCWMBurstSize_Type(Unsigned32):
    """Custom type iscsiIfTcpCWMBurstSize based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_IscsiIfTcpCWMBurstSize_Type.__name__ = "Unsigned32"
_IscsiIfTcpCWMBurstSize_Object = MibTableColumn
iscsiIfTcpCWMBurstSize = _IscsiIfTcpCWMBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9, 1, 23),
    _IscsiIfTcpCWMBurstSize_Type()
)
iscsiIfTcpCWMBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiIfTcpCWMBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    iscsiIfTcpCWMBurstSize.setUnits("kilobytes")


class _IscsiIfTcpMaxJitter_Type(Unsigned32):
    """Custom type iscsiIfTcpMaxJitter based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_IscsiIfTcpMaxJitter_Type.__name__ = "Unsigned32"
_IscsiIfTcpMaxJitter_Object = MibTableColumn
iscsiIfTcpMaxJitter = _IscsiIfTcpMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 9, 1, 24),
    _IscsiIfTcpMaxJitter_Type()
)
iscsiIfTcpMaxJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiIfTcpMaxJitter.setStatus("current")
if mibBuilder.loadTexts:
    iscsiIfTcpMaxJitter.setUnits("microseconds")
_IscsiGigEIfTable_Object = MibTable
iscsiGigEIfTable = _IscsiGigEIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 10)
)
if mibBuilder.loadTexts:
    iscsiGigEIfTable.setStatus("current")
_IscsiGigEIfEntry_Object = MibTableRow
iscsiGigEIfEntry = _IscsiGigEIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 10, 1)
)
iscsiGigEIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    iscsiGigEIfEntry.setStatus("current")
_IscsiGigEIfAuthMethod_Type = IscsiAuthMethod
_IscsiGigEIfAuthMethod_Object = MibTableColumn
iscsiGigEIfAuthMethod = _IscsiGigEIfAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 10, 1, 1),
    _IscsiGigEIfAuthMethod_Type()
)
iscsiGigEIfAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiGigEIfAuthMethod.setStatus("current")
_IscsiGigEIfIsnsServerProfileName_Type = SnmpAdminString
_IscsiGigEIfIsnsServerProfileName_Object = MibTableColumn
iscsiGigEIfIsnsServerProfileName = _IscsiGigEIfIsnsServerProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 10, 1, 2),
    _IscsiGigEIfIsnsServerProfileName_Type()
)
iscsiGigEIfIsnsServerProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiGigEIfIsnsServerProfileName.setStatus("current")


class _IscsiGigEIfIscsiSessions_Type(Unsigned32):
    """Custom type iscsiGigEIfIscsiSessions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IscsiGigEIfIscsiSessions_Type.__name__ = "Unsigned32"
_IscsiGigEIfIscsiSessions_Object = MibTableColumn
iscsiGigEIfIscsiSessions = _IscsiGigEIfIscsiSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 10, 1, 3),
    _IscsiGigEIfIscsiSessions_Type()
)
iscsiGigEIfIscsiSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiGigEIfIscsiSessions.setStatus("current")


class _IscsiInitiatorIdleTimeout_Type(Unsigned32):
    """Custom type iscsiInitiatorIdleTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_IscsiInitiatorIdleTimeout_Type.__name__ = "Unsigned32"
_IscsiInitiatorIdleTimeout_Object = MibScalar
iscsiInitiatorIdleTimeout = _IscsiInitiatorIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 11),
    _IscsiInitiatorIdleTimeout_Type()
)
iscsiInitiatorIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiInitiatorIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    iscsiInitiatorIdleTimeout.setUnits("seconds")
_IscsiIntrIdentificationMode_Type = CIscsiIntrIdentificationMode
_IscsiIntrIdentificationMode_Object = MibScalar
iscsiIntrIdentificationMode = _IscsiIntrIdentificationMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 12),
    _IscsiIntrIdentificationMode_Type()
)
iscsiIntrIdentificationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiIntrIdentificationMode.setStatus("current")


class _IscsiTargetUserName_Type(SnmpAdminString):
    """Custom type iscsiTargetUserName based on SnmpAdminString"""
    defaultHexValue = ""


_IscsiTargetUserName_Object = MibScalar
iscsiTargetUserName = _IscsiTargetUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 13),
    _IscsiTargetUserName_Type()
)
iscsiTargetUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiTargetUserName.setStatus("current")


class _IscsiTargetPassword_Type(SnmpAdminString):
    """Custom type iscsiTargetPassword based on SnmpAdminString"""
    defaultHexValue = ""


_IscsiTargetPassword_Object = MibScalar
iscsiTargetPassword = _IscsiTargetPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 1, 14),
    _IscsiTargetPassword_Type()
)
iscsiTargetPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiTargetPassword.setStatus("current")
_CiScsiStatistics_ObjectIdentity = ObjectIdentity
ciScsiStatistics = _CiScsiStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 2)
)
_IscsiSessionAttributesExtTable_Object = MibTable
iscsiSessionAttributesExtTable = _IscsiSessionAttributesExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 2, 1)
)
if mibBuilder.loadTexts:
    iscsiSessionAttributesExtTable.setStatus("current")
_IscsiSessionAttributesExtEntry_Object = MibTableRow
iscsiSessionAttributesExtEntry = _IscsiSessionAttributesExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    iscsiSessionAttributesExtEntry.setStatus("current")
_IscsiSsnVsan_Type = VsanIndex
_IscsiSsnVsan_Object = MibTableColumn
iscsiSsnVsan = _IscsiSsnVsan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 2, 1, 1, 1),
    _IscsiSsnVsan_Type()
)
iscsiSsnVsan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnVsan.setStatus("current")
_CiscsiConnectionStatsTable_Object = MibTable
ciscsiConnectionStatsTable = _CiscsiConnectionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ciscsiConnectionStatsTable.setStatus("current")
_CiscsiConnectionStatsEntry_Object = MibTableRow
ciscsiConnectionStatsEntry = _CiscsiConnectionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 2, 2, 1)
)
ciscsiConnectionStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ISCSI-MIB", "cIscsiInstIndex"),
    (0, "CISCO-ISCSI-GW-MIB", "cIscsiStatsNodeIndex"),
    (0, "CISCO-ISCSI-GW-MIB", "cIscsiStatsSessionIndex"),
    (0, "CISCO-ISCSI-GW-MIB", "cIscsiStatsConnectionIndex"),
)
if mibBuilder.loadTexts:
    ciscsiConnectionStatsEntry.setStatus("current")


class _CIscsiStatsNodeIndex_Type(Unsigned32):
    """Custom type cIscsiStatsNodeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CIscsiStatsNodeIndex_Type.__name__ = "Unsigned32"
_CIscsiStatsNodeIndex_Object = MibTableColumn
cIscsiStatsNodeIndex = _CIscsiStatsNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 2, 2, 1, 1),
    _CIscsiStatsNodeIndex_Type()
)
cIscsiStatsNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIscsiStatsNodeIndex.setStatus("current")


class _CIscsiStatsSessionIndex_Type(Unsigned32):
    """Custom type cIscsiStatsSessionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CIscsiStatsSessionIndex_Type.__name__ = "Unsigned32"
_CIscsiStatsSessionIndex_Object = MibTableColumn
cIscsiStatsSessionIndex = _CIscsiStatsSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 2, 2, 1, 2),
    _CIscsiStatsSessionIndex_Type()
)
cIscsiStatsSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIscsiStatsSessionIndex.setStatus("current")


class _CIscsiStatsConnectionIndex_Type(Unsigned32):
    """Custom type cIscsiStatsConnectionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CIscsiStatsConnectionIndex_Type.__name__ = "Unsigned32"
_CIscsiStatsConnectionIndex_Object = MibTableColumn
cIscsiStatsConnectionIndex = _CIscsiStatsConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 2, 2, 1, 3),
    _CIscsiStatsConnectionIndex_Type()
)
cIscsiStatsConnectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIscsiStatsConnectionIndex.setStatus("current")
_CIscsiStatsConnectionRxBytes_Type = Counter64
_CIscsiStatsConnectionRxBytes_Object = MibTableColumn
cIscsiStatsConnectionRxBytes = _CIscsiStatsConnectionRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 2, 2, 1, 4),
    _CIscsiStatsConnectionRxBytes_Type()
)
cIscsiStatsConnectionRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiStatsConnectionRxBytes.setStatus("current")
_CIscsiStatsConnectionTxBytes_Type = Counter64
_CIscsiStatsConnectionTxBytes_Object = MibTableColumn
cIscsiStatsConnectionTxBytes = _CIscsiStatsConnectionTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 2, 2, 1, 5),
    _CIscsiStatsConnectionTxBytes_Type()
)
cIscsiStatsConnectionTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiStatsConnectionTxBytes.setStatus("current")
_CIscsiStatsIpSecInUse_Type = TruthValue
_CIscsiStatsIpSecInUse_Object = MibTableColumn
cIscsiStatsIpSecInUse = _CIscsiStatsIpSecInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 1, 2, 2, 1, 6),
    _CIscsiStatsIpSecInUse_Type()
)
cIscsiStatsIpSecInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiStatsIpSecInUse.setStatus("current")
_CiscoiScsiGwMIBConformance_ObjectIdentity = ObjectIdentity
ciscoiScsiGwMIBConformance = _CiscoiScsiGwMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2)
)
_CiscoiScsiGwMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoiScsiGwMIBCompliances = _CiscoiScsiGwMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 1)
)
_CiscoiScsiGwMIBGroups_ObjectIdentity = ObjectIdentity
ciscoiScsiGwMIBGroups = _CiscoiScsiGwMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 2)
)
cIscsiInstanceAttributesEntry.registerAugmentions(
    ("CISCO-ISCSI-GW-MIB",
     "iscsiImprtExprtTgtsConfEntry")
)
iscsiImprtExprtTgtsConfEntry.setIndexNames(*cIscsiInstanceAttributesEntry.getIndexNames())
cIscsiNodeAttributesEntry.registerAugmentions(
    ("CISCO-ISCSI-GW-MIB",
     "fc2IscsiNodeEntry")
)
fc2IscsiNodeEntry.setIndexNames(*cIscsiNodeAttributesEntry.getIndexNames())
ciscoScsiLuEntry.registerAugmentions(
    ("CISCO-ISCSI-GW-MIB",
     "scsiLuExtEntry")
)
scsiLuExtEntry.setIndexNames(*ciscoScsiLuEntry.getIndexNames())
cIscsiSessionAttributesEntry.registerAugmentions(
    ("CISCO-ISCSI-GW-MIB",
     "iscsiSessionAttributesExtEntry")
)
iscsiSessionAttributesExtEntry.setIndexNames(*cIscsiSessionAttributesEntry.getIndexNames())

# Managed Objects groups

cigConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 2, 1)
)
cigConfigurationGroup.setObjects(
      *(("CISCO-ISCSI-GW-MIB", "iscsiImprtExprtTgtsConfImport"),
        ("CISCO-ISCSI-GW-MIB", "iscsiImprtExprtTgtsConfExport"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeName"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeRole"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodePersistentFCAddr"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcPortPersistentFCAddr"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcPortNumFCAddr"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeFCAddr"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcPortFCAddrListIndex"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeVsanList2k"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeVsanList4k"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeDiscovered"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeRowStatus"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeRole"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeName"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiPortFCAddrListIndex"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodePermitListIndex"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeAdvIntfListIndex"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeAllIntrAccessAllowed"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeDiscovered"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeRowStatus"),
        ("CISCO-ISCSI-GW-MIB", "fcAddress"),
        ("CISCO-ISCSI-GW-MIB", "fcSecondaryAddress"),
        ("CISCO-ISCSI-GW-MIB", "fcAddressRowStatus"),
        ("CISCO-ISCSI-GW-MIB", "iscsiNodeName"),
        ("CISCO-ISCSI-GW-MIB", "iscsiNodeNameRowStatus"),
        ("CISCO-ISCSI-GW-MIB", "nodeAdvIntfIfIndex"),
        ("CISCO-ISCSI-GW-MIB", "nodeAdvIntfIfRowStatus"))
)
if mibBuilder.loadTexts:
    cigConfigurationGroup.setStatus("deprecated")

cigLuConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 2, 2)
)
cigLuConfigurationGroup.setObjects(
      *(("CISCO-ISCSI-GW-MIB", "scsiLuExtRemotePortFcAddress"),
        ("CISCO-ISCSI-GW-MIB", "scsiLuExtRemotePortSecFcAddress"),
        ("CISCO-ISCSI-GW-MIB", "scsiLuExtLocalTargetAddress"),
        ("CISCO-ISCSI-GW-MIB", "scsiLuExtRemoteLun"),
        ("CISCO-ISCSI-GW-MIB", "scsiLuExtLocalLun"),
        ("CISCO-ISCSI-GW-MIB", "scsiLuExtRowStatus"))
)
if mibBuilder.loadTexts:
    cigLuConfigurationGroup.setStatus("deprecated")

cigSessionStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 2, 3)
)
cigSessionStatsGroup.setObjects(
    ("CISCO-ISCSI-GW-MIB", "iscsiSsnVsan")
)
if mibBuilder.loadTexts:
    cigSessionStatsGroup.setStatus("current")

cigConfigurationGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 2, 4)
)
cigConfigurationGroupRev1.setObjects(
      *(("CISCO-ISCSI-GW-MIB", "iscsiImprtExprtTgtsConfImport"),
        ("CISCO-ISCSI-GW-MIB", "iscsiImprtExprtTgtsConfExport"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeName"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeRole"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodePersistentFCAddr"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcPortPersistentFCAddr"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcPortNumFCAddr"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeFCAddr"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcPortFCAddrListIndex"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeVsanList2k"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeVsanList4k"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeDiscovered"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeRowStatus"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeFcAddrAssignment"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeRole"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeName"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiPortFCAddrListIndex"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodePermitListIndex"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeAdvIntfListIndex"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeAllIntrAccessAllowed"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeDiscovered"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeRowStatus"),
        ("CISCO-ISCSI-GW-MIB", "fcAddress"),
        ("CISCO-ISCSI-GW-MIB", "fcSecondaryAddress"),
        ("CISCO-ISCSI-GW-MIB", "fcAddressRowStatus"),
        ("CISCO-ISCSI-GW-MIB", "iscsiNodeName"),
        ("CISCO-ISCSI-GW-MIB", "iscsiNodeNameRowStatus"),
        ("CISCO-ISCSI-GW-MIB", "nodeAdvIntfIfIndex"),
        ("CISCO-ISCSI-GW-MIB", "nodeAdvIntfIfRowStatus"))
)
if mibBuilder.loadTexts:
    cigConfigurationGroupRev1.setStatus("deprecated")

cigLuConfigurationGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 2, 5)
)
cigLuConfigurationGroupRev1.setObjects(
      *(("CISCO-ISCSI-GW-MIB", "scsiLuExtRemotePortFcAddress"),
        ("CISCO-ISCSI-GW-MIB", "scsiLuExtRemotePortSecFcAddress"),
        ("CISCO-ISCSI-GW-MIB", "scsiLuExtLocalTargetAddress"),
        ("CISCO-ISCSI-GW-MIB", "scsiLuExtRemoteLun"),
        ("CISCO-ISCSI-GW-MIB", "scsiLuExtLocalLun"),
        ("CISCO-ISCSI-GW-MIB", "scsiLuExtRowStatus"),
        ("CISCO-ISCSI-GW-MIB", "scsiLuExtRemoteSecLun"))
)
if mibBuilder.loadTexts:
    cigLuConfigurationGroupRev1.setStatus("current")

cigIscsiIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 2, 6)
)
cigIscsiIfGroup.setObjects(
      *(("CISCO-ISCSI-GW-MIB", "iscsiIfTcpKeepAliveTimeout"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpMaxBandwidth"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpMaxRetransmissions"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpMinRetransmitTime"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpPMTUEnable"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpQOS"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpSACKEnable"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpSendBufferSize"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpMinBandwidth"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpPMTUResetTimeout"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpLocalPort"))
)
if mibBuilder.loadTexts:
    cigIscsiIfGroup.setStatus("deprecated")

cigIscsiIfGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 2, 7)
)
cigIscsiIfGroupRev1.setObjects(
      *(("CISCO-ISCSI-GW-MIB", "iscsiIfTcpKeepAliveTimeout"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpMaxBandwidth"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpMaxRetransmissions"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpMinRetransmitTime"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpPMTUEnable"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpQOS"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpSACKEnable"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpSendBufferSize"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpMinBandwidth"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpPMTUResetTimeout"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpLocalPort"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfForwardingMode"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfIntrProxyMode"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfIntrProxyModeNodeFcAddr"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfIntrProxyModePortFcAddr"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfIntrProxyModeFcAddrAsgnmt"))
)
if mibBuilder.loadTexts:
    cigIscsiIfGroupRev1.setStatus("deprecated")

cigIscsiAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 2, 8)
)
cigIscsiAuthGroup.setObjects(
      *(("CISCO-ISCSI-GW-MIB", "iscsiAuthMethod"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeAuthUser"),
        ("CISCO-ISCSI-GW-MIB", "iscsiGigEIfAuthMethod"))
)
if mibBuilder.loadTexts:
    cigIscsiAuthGroup.setStatus("current")

cigConfigurationGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 2, 9)
)
cigConfigurationGroupRev2.setObjects(
      *(("CISCO-ISCSI-GW-MIB", "iscsiImprtExprtTgtsConfImport"),
        ("CISCO-ISCSI-GW-MIB", "iscsiImprtExprtTgtsConfExport"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeName"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeRole"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodePersistentFCAddr"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcPortPersistentFCAddr"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcPortNumFCAddr"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeFCAddr"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcPortFCAddrListIndex"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeVsanList2k"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeVsanList4k"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeDiscovered"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeRowStatus"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeFcAddrAssignment"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeRole"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeName"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiPortFCAddrListIndex"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodePermitListIndex"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeAdvIntfListIndex"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeAllIntrAccessAllowed"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeDiscovered"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeRowStatus"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeTrespassMode"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeRevertToPrimaryPort"),
        ("CISCO-ISCSI-GW-MIB", "fcAddress"),
        ("CISCO-ISCSI-GW-MIB", "fcSecondaryAddress"),
        ("CISCO-ISCSI-GW-MIB", "fcAddressRowStatus"),
        ("CISCO-ISCSI-GW-MIB", "iscsiNodeName"),
        ("CISCO-ISCSI-GW-MIB", "iscsiNodeNameRowStatus"),
        ("CISCO-ISCSI-GW-MIB", "nodeAdvIntfIfIndex"),
        ("CISCO-ISCSI-GW-MIB", "nodeAdvIntfIfRowStatus"))
)
if mibBuilder.loadTexts:
    cigConfigurationGroupRev2.setStatus("deprecated")

cigIscsiGigEIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 2, 10)
)
cigIscsiGigEIfGroup.setObjects(
      *(("CISCO-ISCSI-GW-MIB", "iscsiGigEIfIsnsServerProfileName"),
        ("CISCO-ISCSI-GW-MIB", "iscsiGigEIfIscsiSessions"))
)
if mibBuilder.loadTexts:
    cigIscsiGigEIfGroup.setStatus("current")

cigIscsiIfGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 2, 11)
)
cigIscsiIfGroupRev2.setObjects(
      *(("CISCO-ISCSI-GW-MIB", "iscsiIfTcpKeepAliveTimeout"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpMaxBandwidth"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpMaxRetransmissions"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpMinRetransmitTime"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpPMTUEnable"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpQOS"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpSACKEnable"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpSendBufferSize"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpMinBandwidth"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpPMTUResetTimeout"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpLocalPort"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfForwardingMode"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfIntrProxyMode"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfIntrProxyModeNodeFcAddr"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfIntrProxyModePortFcAddr"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfIntrProxyModeFcAddrAsgnmt"))
)
if mibBuilder.loadTexts:
    cigIscsiIfGroupRev2.setStatus("deprecated")

cigConfigurationGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 2, 12)
)
cigConfigurationGroupRev3.setObjects(
      *(("CISCO-ISCSI-GW-MIB", "iscsiImprtExprtTgtsConfImport"),
        ("CISCO-ISCSI-GW-MIB", "iscsiImprtExprtTgtsConfExport"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeName"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeRole"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodePersistentFCAddr"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcPortPersistentFCAddr"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcPortNumFCAddr"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeFCAddr"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcPortFCAddrListIndex"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeVsanList2k"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeVsanList4k"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeDiscovered"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeRowStatus"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcNodeFcAddrAssignment"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeRole"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeName"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiPortFCAddrListIndex"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodePermitListIndex"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeAdvIntfListIndex"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeAllIntrAccessAllowed"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeDiscovered"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeRowStatus"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeTrespassMode"),
        ("CISCO-ISCSI-GW-MIB", "fc2IscsiNodeRevertToPrimaryPort"),
        ("CISCO-ISCSI-GW-MIB", "fcAddress"),
        ("CISCO-ISCSI-GW-MIB", "fcSecondaryAddress"),
        ("CISCO-ISCSI-GW-MIB", "fcAddressRowStatus"),
        ("CISCO-ISCSI-GW-MIB", "iscsiNodeName"),
        ("CISCO-ISCSI-GW-MIB", "iscsiNodeNameRowStatus"),
        ("CISCO-ISCSI-GW-MIB", "nodeAdvIntfIfIndex"),
        ("CISCO-ISCSI-GW-MIB", "nodeAdvIntfIfRowStatus"),
        ("CISCO-ISCSI-GW-MIB", "iscsiInitiatorIdleTimeout"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIntrIdentificationMode"))
)
if mibBuilder.loadTexts:
    cigConfigurationGroupRev3.setStatus("current")

cigIscsiIfGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 2, 13)
)
cigIscsiIfGroupRev3.setObjects(
      *(("CISCO-ISCSI-GW-MIB", "iscsiIfTcpKeepAliveTimeout"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpMaxBandwidth"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpMaxRetransmissions"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpMinRetransmitTime"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpPMTUEnable"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpQOS"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpSACKEnable"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpSendBufferSize"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpMinBandwidth"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpPMTUResetTimeout"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpLocalPort"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfForwardingMode"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfIntrProxyMode"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfIntrProxyModeNodeFcAddr"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfIntrProxyModePortFcAddr"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfIntrProxyModeFcAddrAsgnmt"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfIntrIdentificationMode"))
)
if mibBuilder.loadTexts:
    cigIscsiIfGroupRev3.setStatus("deprecated")

cigIscsiIfGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 2, 14)
)
cigIscsiIfGroupRev4.setObjects(
      *(("CISCO-ISCSI-GW-MIB", "iscsiIfTcpKeepAliveTimeout"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpMaxBandwidth"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpMaxRetransmissions"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpMinRetransmitTime"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpPMTUEnable"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpQOS"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpSACKEnable"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpSendBufferSize"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpMinBandwidth"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpPMTUResetTimeout"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfForwardingMode"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfIntrProxyMode"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfIntrProxyModeNodeFcAddr"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfIntrProxyModePortFcAddr"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfIntrProxyModeFcAddrAsgnmt"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfIntrIdentificationMode"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpLocalTcpPort"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpRndTrpTimeEst"))
)
if mibBuilder.loadTexts:
    cigIscsiIfGroupRev4.setStatus("current")

cigIscsiIfGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 2, 15)
)
cigIscsiIfGroupSup1.setObjects(
      *(("CISCO-ISCSI-GW-MIB", "iscsiIfNumNormalConnections"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfNumDiscovConnections"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpCWMEnable"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpCWMBurstSize"),
        ("CISCO-ISCSI-GW-MIB", "iscsiIfTcpMaxJitter"))
)
if mibBuilder.loadTexts:
    cigIscsiIfGroupSup1.setStatus("current")

cigConnectionStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 2, 16)
)
cigConnectionStatsGroup.setObjects(
      *(("CISCO-ISCSI-GW-MIB", "cIscsiStatsConnectionTxBytes"),
        ("CISCO-ISCSI-GW-MIB", "cIscsiStatsConnectionRxBytes"),
        ("CISCO-ISCSI-GW-MIB", "cIscsiStatsIpSecInUse"))
)
if mibBuilder.loadTexts:
    cigConnectionStatsGroup.setStatus("current")

cigConfigurationGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 2, 17)
)
cigConfigurationGroupSup1.setObjects(
      *(("CISCO-ISCSI-GW-MIB", "iscsiTargetUserName"),
        ("CISCO-ISCSI-GW-MIB", "iscsiTargetPassword"))
)
if mibBuilder.loadTexts:
    cigConfigurationGroupSup1.setStatus("current")

cigIscsiAuthGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 2, 18)
)
cigIscsiAuthGroupSup1.setObjects(
      *(("CISCO-ISCSI-GW-MIB", "iscsi2FcTargetUserName"),
        ("CISCO-ISCSI-GW-MIB", "iscsi2FcTargetPassword"))
)
if mibBuilder.loadTexts:
    cigIscsiAuthGroupSup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoiScsiGwMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoiScsiGwMIBCompliance.setStatus(
        "deprecated"
    )

ciscoiScsiGwMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoiScsiGwMIBCompliance1.setStatus(
        "deprecated"
    )

ciscoiScsiGwMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoiScsiGwMIBCompliance2.setStatus(
        "deprecated"
    )

ciscoiScsiGwMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoiScsiGwMIBCompliance3.setStatus(
        "deprecated"
    )

ciscoiScsiGwMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoiScsiGwMIBCompliance4.setStatus(
        "deprecated"
    )

ciscoiScsiGwMIBCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 317, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoiScsiGwMIBCompliance5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ISCSI-GW-MIB",
    **{"CIscsiTargetDomains": CIscsiTargetDomains,
       "CIscsiNodeRoles": CIscsiNodeRoles,
       "IscsiName": IscsiName,
       "IscsiAuthMethod": IscsiAuthMethod,
       "CIscsiIntrIdentificationMode": CIscsiIntrIdentificationMode,
       "ciscoIscsiGwMIB": ciscoIscsiGwMIB,
       "ciscoiScsiGwMIBNotifications": ciscoiScsiGwMIBNotifications,
       "ciscoiScsiGwMIBObjects": ciscoiScsiGwMIBObjects,
       "ciScsiConfig": ciScsiConfig,
       "iscsiImprtExprtTgtsConfTable": iscsiImprtExprtTgtsConfTable,
       "iscsiImprtExprtTgtsConfEntry": iscsiImprtExprtTgtsConfEntry,
       "iscsiImprtExprtTgtsConfImport": iscsiImprtExprtTgtsConfImport,
       "iscsiImprtExprtTgtsConfExport": iscsiImprtExprtTgtsConfExport,
       "iscsiAuthMethod": iscsiAuthMethod,
       "iscsi2FcNodeTable": iscsi2FcNodeTable,
       "iscsi2FcNodeEntry": iscsi2FcNodeEntry,
       "iscsi2FcNodeIndex": iscsi2FcNodeIndex,
       "iscsi2FcNodeName": iscsi2FcNodeName,
       "iscsi2FcNodeRole": iscsi2FcNodeRole,
       "iscsi2FcNodePersistentFCAddr": iscsi2FcNodePersistentFCAddr,
       "iscsi2FcPortPersistentFCAddr": iscsi2FcPortPersistentFCAddr,
       "iscsi2FcPortNumFCAddr": iscsi2FcPortNumFCAddr,
       "iscsi2FcNodeFCAddr": iscsi2FcNodeFCAddr,
       "iscsi2FcPortFCAddrListIndex": iscsi2FcPortFCAddrListIndex,
       "iscsi2FcNodeVsanList2k": iscsi2FcNodeVsanList2k,
       "iscsi2FcNodeVsanList4k": iscsi2FcNodeVsanList4k,
       "iscsi2FcNodeDiscovered": iscsi2FcNodeDiscovered,
       "iscsi2FcNodeRowStatus": iscsi2FcNodeRowStatus,
       "iscsi2FcNodeFcAddrAssignment": iscsi2FcNodeFcAddrAssignment,
       "iscsi2FcNodeAuthUser": iscsi2FcNodeAuthUser,
       "iscsi2FcTargetUserName": iscsi2FcTargetUserName,
       "iscsi2FcTargetPassword": iscsi2FcTargetPassword,
       "fc2IscsiNodeTable": fc2IscsiNodeTable,
       "fc2IscsiNodeEntry": fc2IscsiNodeEntry,
       "fc2IscsiNodeRole": fc2IscsiNodeRole,
       "fc2IscsiNodeName": fc2IscsiNodeName,
       "fc2IscsiPortFCAddrListIndex": fc2IscsiPortFCAddrListIndex,
       "fc2IscsiNodePermitListIndex": fc2IscsiNodePermitListIndex,
       "fc2IscsiNodeAdvIntfListIndex": fc2IscsiNodeAdvIntfListIndex,
       "fc2IscsiNodeAllIntrAccessAllowed": fc2IscsiNodeAllIntrAccessAllowed,
       "fc2IscsiNodeDiscovered": fc2IscsiNodeDiscovered,
       "fc2IscsiNodeRowStatus": fc2IscsiNodeRowStatus,
       "fc2IscsiNodeTrespassMode": fc2IscsiNodeTrespassMode,
       "fc2IscsiNodeRevertToPrimaryPort": fc2IscsiNodeRevertToPrimaryPort,
       "fcAddressListTable": fcAddressListTable,
       "fcAddressListEntry": fcAddressListEntry,
       "fcAddressListIndex": fcAddressListIndex,
       "fcAddressIndex": fcAddressIndex,
       "fcAddress": fcAddress,
       "fcSecondaryAddress": fcSecondaryAddress,
       "fcAddressRowStatus": fcAddressRowStatus,
       "iscsiNodeNameListTable": iscsiNodeNameListTable,
       "iscsiNodeNameListEntry": iscsiNodeNameListEntry,
       "iscsiNodeNameListIndex": iscsiNodeNameListIndex,
       "iscsiNodeNameIndex": iscsiNodeNameIndex,
       "iscsiNodeName": iscsiNodeName,
       "iscsiNodeNameRowStatus": iscsiNodeNameRowStatus,
       "nodeAdvIntfListTable": nodeAdvIntfListTable,
       "nodeAdvIntfListEntry": nodeAdvIntfListEntry,
       "nodeAdvIntfListIndex": nodeAdvIntfListIndex,
       "nodeAdvIntfIndex": nodeAdvIntfIndex,
       "nodeAdvIntfIfIndex": nodeAdvIntfIfIndex,
       "nodeAdvIntfIfRowStatus": nodeAdvIntfIfRowStatus,
       "scsiLuExtTable": scsiLuExtTable,
       "scsiLuExtEntry": scsiLuExtEntry,
       "scsiLuExtRemotePortFcAddress": scsiLuExtRemotePortFcAddress,
       "scsiLuExtRemotePortSecFcAddress": scsiLuExtRemotePortSecFcAddress,
       "scsiLuExtLocalTargetAddress": scsiLuExtLocalTargetAddress,
       "scsiLuExtRemoteLun": scsiLuExtRemoteLun,
       "scsiLuExtLocalLun": scsiLuExtLocalLun,
       "scsiLuExtRowStatus": scsiLuExtRowStatus,
       "scsiLuExtRemoteSecLun": scsiLuExtRemoteSecLun,
       "iscsiIfTable": iscsiIfTable,
       "iscsiIfEntry": iscsiIfEntry,
       "iscsiIfTcpKeepAliveTimeout": iscsiIfTcpKeepAliveTimeout,
       "iscsiIfTcpMaxBandwidth": iscsiIfTcpMaxBandwidth,
       "iscsiIfTcpMaxRetransmissions": iscsiIfTcpMaxRetransmissions,
       "iscsiIfTcpMinRetransmitTime": iscsiIfTcpMinRetransmitTime,
       "iscsiIfTcpPMTUEnable": iscsiIfTcpPMTUEnable,
       "iscsiIfTcpQOS": iscsiIfTcpQOS,
       "iscsiIfTcpSACKEnable": iscsiIfTcpSACKEnable,
       "iscsiIfTcpSendBufferSize": iscsiIfTcpSendBufferSize,
       "iscsiIfTcpMinBandwidth": iscsiIfTcpMinBandwidth,
       "iscsiIfTcpPMTUResetTimeout": iscsiIfTcpPMTUResetTimeout,
       "iscsiIfTcpLocalPort": iscsiIfTcpLocalPort,
       "iscsiIfForwardingMode": iscsiIfForwardingMode,
       "iscsiIfIntrProxyMode": iscsiIfIntrProxyMode,
       "iscsiIfIntrProxyModeNodeFcAddr": iscsiIfIntrProxyModeNodeFcAddr,
       "iscsiIfIntrProxyModePortFcAddr": iscsiIfIntrProxyModePortFcAddr,
       "iscsiIfIntrProxyModeFcAddrAsgnmt": iscsiIfIntrProxyModeFcAddrAsgnmt,
       "iscsiIfIntrIdentificationMode": iscsiIfIntrIdentificationMode,
       "iscsiIfTcpRndTrpTimeEst": iscsiIfTcpRndTrpTimeEst,
       "iscsiIfTcpLocalTcpPort": iscsiIfTcpLocalTcpPort,
       "iscsiIfNumNormalConnections": iscsiIfNumNormalConnections,
       "iscsiIfNumDiscovConnections": iscsiIfNumDiscovConnections,
       "iscsiIfTcpCWMEnable": iscsiIfTcpCWMEnable,
       "iscsiIfTcpCWMBurstSize": iscsiIfTcpCWMBurstSize,
       "iscsiIfTcpMaxJitter": iscsiIfTcpMaxJitter,
       "iscsiGigEIfTable": iscsiGigEIfTable,
       "iscsiGigEIfEntry": iscsiGigEIfEntry,
       "iscsiGigEIfAuthMethod": iscsiGigEIfAuthMethod,
       "iscsiGigEIfIsnsServerProfileName": iscsiGigEIfIsnsServerProfileName,
       "iscsiGigEIfIscsiSessions": iscsiGigEIfIscsiSessions,
       "iscsiInitiatorIdleTimeout": iscsiInitiatorIdleTimeout,
       "iscsiIntrIdentificationMode": iscsiIntrIdentificationMode,
       "iscsiTargetUserName": iscsiTargetUserName,
       "iscsiTargetPassword": iscsiTargetPassword,
       "ciScsiStatistics": ciScsiStatistics,
       "iscsiSessionAttributesExtTable": iscsiSessionAttributesExtTable,
       "iscsiSessionAttributesExtEntry": iscsiSessionAttributesExtEntry,
       "iscsiSsnVsan": iscsiSsnVsan,
       "ciscsiConnectionStatsTable": ciscsiConnectionStatsTable,
       "ciscsiConnectionStatsEntry": ciscsiConnectionStatsEntry,
       "cIscsiStatsNodeIndex": cIscsiStatsNodeIndex,
       "cIscsiStatsSessionIndex": cIscsiStatsSessionIndex,
       "cIscsiStatsConnectionIndex": cIscsiStatsConnectionIndex,
       "cIscsiStatsConnectionRxBytes": cIscsiStatsConnectionRxBytes,
       "cIscsiStatsConnectionTxBytes": cIscsiStatsConnectionTxBytes,
       "cIscsiStatsIpSecInUse": cIscsiStatsIpSecInUse,
       "ciscoiScsiGwMIBConformance": ciscoiScsiGwMIBConformance,
       "ciscoiScsiGwMIBCompliances": ciscoiScsiGwMIBCompliances,
       "ciscoiScsiGwMIBCompliance": ciscoiScsiGwMIBCompliance,
       "ciscoiScsiGwMIBCompliance1": ciscoiScsiGwMIBCompliance1,
       "ciscoiScsiGwMIBCompliance2": ciscoiScsiGwMIBCompliance2,
       "ciscoiScsiGwMIBCompliance3": ciscoiScsiGwMIBCompliance3,
       "ciscoiScsiGwMIBCompliance4": ciscoiScsiGwMIBCompliance4,
       "ciscoiScsiGwMIBCompliance5": ciscoiScsiGwMIBCompliance5,
       "ciscoiScsiGwMIBGroups": ciscoiScsiGwMIBGroups,
       "cigConfigurationGroup": cigConfigurationGroup,
       "cigLuConfigurationGroup": cigLuConfigurationGroup,
       "cigSessionStatsGroup": cigSessionStatsGroup,
       "cigConfigurationGroupRev1": cigConfigurationGroupRev1,
       "cigLuConfigurationGroupRev1": cigLuConfigurationGroupRev1,
       "cigIscsiIfGroup": cigIscsiIfGroup,
       "cigIscsiIfGroupRev1": cigIscsiIfGroupRev1,
       "cigIscsiAuthGroup": cigIscsiAuthGroup,
       "cigConfigurationGroupRev2": cigConfigurationGroupRev2,
       "cigIscsiGigEIfGroup": cigIscsiGigEIfGroup,
       "cigIscsiIfGroupRev2": cigIscsiIfGroupRev2,
       "cigConfigurationGroupRev3": cigConfigurationGroupRev3,
       "cigIscsiIfGroupRev3": cigIscsiIfGroupRev3,
       "cigIscsiIfGroupRev4": cigIscsiIfGroupRev4,
       "cigIscsiIfGroupSup1": cigIscsiIfGroupSup1,
       "cigConnectionStatsGroup": cigConnectionStatsGroup,
       "cigConfigurationGroupSup1": cigConfigurationGroupSup1,
       "cigIscsiAuthGroupSup1": cigIscsiAuthGroupSup1}
)
