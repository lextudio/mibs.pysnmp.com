# SNMP MIB module (DEPNODE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DEPNODE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:24:11 2024
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

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_IbmSP_ObjectIdentity = ObjectIdentity
ibmSP = _IbmSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 117)
)
_IbmSPDepNode_ObjectIdentity = ObjectIdentity
ibmSPDepNode = _IbmSPDepNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 117, 4)
)
_IbmSPDepNodeTable_Object = MibTable
ibmSPDepNodeTable = _IbmSPDepNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1)
)
if mibBuilder.loadTexts:
    ibmSPDepNodeTable.setStatus("mandatory")
_IbmSPDepNodeEntry_Object = MibTableRow
ibmSPDepNodeEntry = _IbmSPDepNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1)
)
ibmSPDepNodeEntry.setIndexNames(
    (0, "DEPNODE-MIB", "ibmSPDepNodeName"),
)
if mibBuilder.loadTexts:
    ibmSPDepNodeEntry.setStatus("mandatory")
_IbmSPDepNodeName_Type = DisplayString
_IbmSPDepNodeName_Object = MibTableColumn
ibmSPDepNodeName = _IbmSPDepNodeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 1),
    _IbmSPDepNodeName_Type()
)
ibmSPDepNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSPDepNodeName.setStatus("mandatory")
_IbmSPDepNodeNumber_Type = Integer32
_IbmSPDepNodeNumber_Object = MibTableColumn
ibmSPDepNodeNumber = _IbmSPDepNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 2),
    _IbmSPDepNodeNumber_Type()
)
ibmSPDepNodeNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSPDepNodeNumber.setStatus("mandatory")


class _IbmSPDepSwToken_Type(OctetString):
    """Custom type ibmSPDepSwToken based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_IbmSPDepSwToken_Type.__name__ = "OctetString"
_IbmSPDepSwToken_Object = MibTableColumn
ibmSPDepSwToken = _IbmSPDepSwToken_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 3),
    _IbmSPDepSwToken_Type()
)
ibmSPDepSwToken.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSPDepSwToken.setStatus("mandatory")


class _IbmSPDepSwARP_Type(Integer32):
    """Custom type ibmSPDepSwARP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IbmSPDepSwARP_Type.__name__ = "Integer32"
_IbmSPDepSwARP_Object = MibTableColumn
ibmSPDepSwARP = _IbmSPDepSwARP_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 4),
    _IbmSPDepSwARP_Type()
)
ibmSPDepSwARP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSPDepSwARP.setStatus("mandatory")


class _IbmSPDepSwNodeNumber_Type(Integer32):
    """Custom type ibmSPDepSwNodeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmSPDepSwNodeNumber_Type.__name__ = "Integer32"
_IbmSPDepSwNodeNumber_Object = MibTableColumn
ibmSPDepSwNodeNumber = _IbmSPDepSwNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 5),
    _IbmSPDepSwNodeNumber_Type()
)
ibmSPDepSwNodeNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSPDepSwNodeNumber.setStatus("mandatory")
_IbmSPDepIPaddr_Type = IpAddress
_IbmSPDepIPaddr_Object = MibTableColumn
ibmSPDepIPaddr = _IbmSPDepIPaddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 6),
    _IbmSPDepIPaddr_Type()
)
ibmSPDepIPaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSPDepIPaddr.setStatus("mandatory")
_IbmSPDepNetMask_Type = IpAddress
_IbmSPDepNetMask_Object = MibTableColumn
ibmSPDepNetMask = _IbmSPDepNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 7),
    _IbmSPDepNetMask_Type()
)
ibmSPDepNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSPDepNetMask.setStatus("mandatory")
_IbmSPDepIPMaxLinkPkt_Type = Integer32
_IbmSPDepIPMaxLinkPkt_Object = MibTableColumn
ibmSPDepIPMaxLinkPkt = _IbmSPDepIPMaxLinkPkt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 8),
    _IbmSPDepIPMaxLinkPkt_Type()
)
ibmSPDepIPMaxLinkPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSPDepIPMaxLinkPkt.setStatus("mandatory")
_IbmSPDepIPHostOffset_Type = Integer32
_IbmSPDepIPHostOffset_Object = MibTableColumn
ibmSPDepIPHostOffset = _IbmSPDepIPHostOffset_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 9),
    _IbmSPDepIPHostOffset_Type()
)
ibmSPDepIPHostOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSPDepIPHostOffset.setStatus("mandatory")


class _IbmSPDepConfigState_Type(Integer32):
    """Custom type ibmSPDepConfigState based on Integer32"""
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
        *(("diagnosticFailed", 4),
          ("driverLoadFailed", 3),
          ("firmwareLoadFailed", 2),
          ("fullyConfigured", 6),
          ("microcodeLoadFailed", 5),
          ("notConfigured", 1))
    )


_IbmSPDepConfigState_Type.__name__ = "Integer32"
_IbmSPDepConfigState_Object = MibTableColumn
ibmSPDepConfigState = _IbmSPDepConfigState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 10),
    _IbmSPDepConfigState_Type()
)
ibmSPDepConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSPDepConfigState.setStatus("mandatory")
_IbmSPDepSysName_Type = DisplayString
_IbmSPDepSysName_Object = MibTableColumn
ibmSPDepSysName = _IbmSPDepSysName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 11),
    _IbmSPDepSysName_Type()
)
ibmSPDepSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSPDepSysName.setStatus("mandatory")


class _IbmSPDepNodeState_Type(Integer32):
    """Custom type ibmSPDepNodeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodeDown", 2),
          ("nodeUp", 1))
    )


_IbmSPDepNodeState_Type.__name__ = "Integer32"
_IbmSPDepNodeState_Object = MibTableColumn
ibmSPDepNodeState = _IbmSPDepNodeState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 12),
    _IbmSPDepNodeState_Type()
)
ibmSPDepNodeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSPDepNodeState.setStatus("mandatory")
_IbmSPDepSwChipLink_Type = Integer32
_IbmSPDepSwChipLink_Object = MibTableColumn
ibmSPDepSwChipLink = _IbmSPDepSwChipLink_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 13),
    _IbmSPDepSwChipLink_Type()
)
ibmSPDepSwChipLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSPDepSwChipLink.setStatus("mandatory")
_IbmSPDepNodeDelay_Type = Integer32
_IbmSPDepNodeDelay_Object = MibTableColumn
ibmSPDepNodeDelay = _IbmSPDepNodeDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 14),
    _IbmSPDepNodeDelay_Type()
)
ibmSPDepNodeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSPDepNodeDelay.setStatus("mandatory")


class _IbmSPDepAdminStatus_Type(Integer32):
    """Custom type ibmSPDepAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("reconfigure", 3),
          ("up", 1))
    )


_IbmSPDepAdminStatus_Type.__name__ = "Integer32"
_IbmSPDepAdminStatus_Object = MibTableColumn
ibmSPDepAdminStatus = _IbmSPDepAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 1, 1, 15),
    _IbmSPDepAdminStatus_Type()
)
ibmSPDepAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSPDepAdminStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

switchInfoNeeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 0, 1)
)
switchInfoNeeded.setObjects(
    ("DEPNODE-MIB", "ibmSPDepNodeName")
)
if mibBuilder.loadTexts:
    switchInfoNeeded.setStatus(
        ""
    )

switchConfigState = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 0, 2)
)
switchConfigState.setObjects(
    ("DEPNODE-MIB", "ibmSPDepConfigState")
)
if mibBuilder.loadTexts:
    switchConfigState.setStatus(
        ""
    )

switchNodeUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 0, 3)
)
switchNodeUp.setObjects(
    ("DEPNODE-MIB", "ibmSPDepNodeName")
)
if mibBuilder.loadTexts:
    switchNodeUp.setStatus(
        ""
    )

switchNodeDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 117, 4, 0, 4)
)
switchNodeDown.setObjects(
    ("DEPNODE-MIB", "ibmSPDepNodeName")
)
if mibBuilder.loadTexts:
    switchNodeDown.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DEPNODE-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "ibmSP": ibmSP,
       "ibmSPDepNode": ibmSPDepNode,
       "switchInfoNeeded": switchInfoNeeded,
       "switchConfigState": switchConfigState,
       "switchNodeUp": switchNodeUp,
       "switchNodeDown": switchNodeDown,
       "ibmSPDepNodeTable": ibmSPDepNodeTable,
       "ibmSPDepNodeEntry": ibmSPDepNodeEntry,
       "ibmSPDepNodeName": ibmSPDepNodeName,
       "ibmSPDepNodeNumber": ibmSPDepNodeNumber,
       "ibmSPDepSwToken": ibmSPDepSwToken,
       "ibmSPDepSwARP": ibmSPDepSwARP,
       "ibmSPDepSwNodeNumber": ibmSPDepSwNodeNumber,
       "ibmSPDepIPaddr": ibmSPDepIPaddr,
       "ibmSPDepNetMask": ibmSPDepNetMask,
       "ibmSPDepIPMaxLinkPkt": ibmSPDepIPMaxLinkPkt,
       "ibmSPDepIPHostOffset": ibmSPDepIPHostOffset,
       "ibmSPDepConfigState": ibmSPDepConfigState,
       "ibmSPDepSysName": ibmSPDepSysName,
       "ibmSPDepNodeState": ibmSPDepNodeState,
       "ibmSPDepSwChipLink": ibmSPDepSwChipLink,
       "ibmSPDepNodeDelay": ibmSPDepNodeDelay,
       "ibmSPDepAdminStatus": ibmSPDepAdminStatus}
)
