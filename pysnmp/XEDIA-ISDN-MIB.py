# SNMP MIB module (XEDIA-ISDN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEDIA-ISDN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:56 2024
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

(dialCtlPeerCfgEntry,) = mibBuilder.importSymbols(
    "DIAL-CONTROL-MIB",
    "dialCtlPeerCfgEntry")

(isdnBasicRateEntry,
 isdnSignalingEntry) = mibBuilder.importSymbols(
    "ISDN-MIB",
    "isdnBasicRateEntry",
    "isdnSignalingEntry")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(xediaMibs,) = mibBuilder.importSymbols(
    "XEDIA-REG",
    "xediaMibs")


# MODULE-IDENTITY

xediaIsdnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 37)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XisdnObjects_ObjectIdentity = ObjectIdentity
xisdnObjects = _XisdnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 37, 1)
)
_XisdnTable_Object = MibTable
xisdnTable = _XisdnTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 1)
)
if mibBuilder.loadTexts:
    xisdnTable.setStatus("current")
_XisdnEntry_Object = MibTableRow
xisdnEntry = _XisdnEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 1, 1)
)
if mibBuilder.loadTexts:
    xisdnEntry.setStatus("current")


class _XisdnLoopbackState_Type(Integer32):
    """Custom type xisdnLoopbackState based on Integer32"""
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


_XisdnLoopbackState_Type.__name__ = "Integer32"
_XisdnLoopbackState_Object = MibTableColumn
xisdnLoopbackState = _XisdnLoopbackState_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 1, 1, 1),
    _XisdnLoopbackState_Type()
)
xisdnLoopbackState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xisdnLoopbackState.setStatus("current")
_XdialCtlPeerCfgTable_Object = MibTable
xdialCtlPeerCfgTable = _XdialCtlPeerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 2)
)
if mibBuilder.loadTexts:
    xdialCtlPeerCfgTable.setStatus("current")
_XdialCtlPeerCfgEntry_Object = MibTableRow
xdialCtlPeerCfgEntry = _XdialCtlPeerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 2, 1)
)
if mibBuilder.loadTexts:
    xdialCtlPeerCfgEntry.setStatus("current")


class _XcallControl_Type(Integer32):
    """Custom type xcallControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connect", 2),
          ("disconnect", 3),
          ("noOp", 1))
    )


_XcallControl_Type.__name__ = "Integer32"
_XcallControl_Object = MibTableColumn
xcallControl = _XcallControl_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 2, 1, 1),
    _XcallControl_Type()
)
xcallControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcallControl.setStatus("current")


class _XnailedUp_Type(Integer32):
    """Custom type xnailedUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("b1", 2),
          ("b2", 3),
          ("none", 1))
    )


_XnailedUp_Type.__name__ = "Integer32"
_XnailedUp_Object = MibTableColumn
xnailedUp = _XnailedUp_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 2, 1, 2),
    _XnailedUp_Type()
)
xnailedUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xnailedUp.setStatus("current")
_XisdnVersion_Type = DisplayString
_XisdnVersion_Object = MibScalar
xisdnVersion = _XisdnVersion_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 3),
    _XisdnVersion_Type()
)
xisdnVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xisdnVersion.setStatus("current")
_XisdnSignalingTable_Object = MibTable
xisdnSignalingTable = _XisdnSignalingTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 4)
)
if mibBuilder.loadTexts:
    xisdnSignalingTable.setStatus("current")
_XisdnSignalingEntry_Object = MibTableRow
xisdnSignalingEntry = _XisdnSignalingEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 4, 1)
)
if mibBuilder.loadTexts:
    xisdnSignalingEntry.setStatus("current")
_IsdnSignalingCallingAddress2_Type = DisplayString
_IsdnSignalingCallingAddress2_Object = MibTableColumn
isdnSignalingCallingAddress2 = _IsdnSignalingCallingAddress2_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 4, 1, 1),
    _IsdnSignalingCallingAddress2_Type()
)
isdnSignalingCallingAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnSignalingCallingAddress2.setStatus("current")
_IsdnEndpointSpid_Type = DisplayString
_IsdnEndpointSpid_Object = MibTableColumn
isdnEndpointSpid = _IsdnEndpointSpid_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 4, 1, 2),
    _IsdnEndpointSpid_Type()
)
isdnEndpointSpid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnEndpointSpid.setStatus("current")
_IsdnEndpointSpid2_Type = DisplayString
_IsdnEndpointSpid2_Object = MibTableColumn
isdnEndpointSpid2 = _IsdnEndpointSpid2_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 4, 1, 3),
    _IsdnEndpointSpid2_Type()
)
isdnEndpointSpid2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnEndpointSpid2.setStatus("current")
_XisdnConformance_ObjectIdentity = ObjectIdentity
xisdnConformance = _XisdnConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 37, 2)
)
_XisdnCompliances_ObjectIdentity = ObjectIdentity
xisdnCompliances = _XisdnCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 37, 2, 1)
)
_XisdnGroups_ObjectIdentity = ObjectIdentity
xisdnGroups = _XisdnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 37, 2, 2)
)
isdnBasicRateEntry.registerAugmentions(
    ("XEDIA-ISDN-MIB",
     "xisdnEntry")
)
xisdnEntry.setIndexNames(*isdnBasicRateEntry.getIndexNames())
dialCtlPeerCfgEntry.registerAugmentions(
    ("XEDIA-ISDN-MIB",
     "xdialCtlPeerCfgEntry")
)
xdialCtlPeerCfgEntry.setIndexNames(*dialCtlPeerCfgEntry.getIndexNames())
isdnSignalingEntry.registerAugmentions(
    ("XEDIA-ISDN-MIB",
     "xisdnSignalingEntry")
)
xisdnSignalingEntry.setIndexNames(*isdnSignalingEntry.getIndexNames())

# Managed Objects groups

xisdnAllGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 37, 2, 2, 1)
)
xisdnAllGroup.setObjects(
      *(("XEDIA-ISDN-MIB", "xisdnLoopbackState"),
        ("XEDIA-ISDN-MIB", "xcallControl"),
        ("XEDIA-ISDN-MIB", "xnailedUp"),
        ("XEDIA-ISDN-MIB", "xisdnVersion"),
        ("XEDIA-ISDN-MIB", "isdnSignalingCallingAddress2"),
        ("XEDIA-ISDN-MIB", "isdnEndpointSpid"),
        ("XEDIA-ISDN-MIB", "isdnEndpointSpid2"))
)
if mibBuilder.loadTexts:
    xisdnAllGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xisdnCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 838, 3, 37, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xisdnCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-ISDN-MIB",
    **{"xediaIsdnMIB": xediaIsdnMIB,
       "xisdnObjects": xisdnObjects,
       "xisdnTable": xisdnTable,
       "xisdnEntry": xisdnEntry,
       "xisdnLoopbackState": xisdnLoopbackState,
       "xdialCtlPeerCfgTable": xdialCtlPeerCfgTable,
       "xdialCtlPeerCfgEntry": xdialCtlPeerCfgEntry,
       "xcallControl": xcallControl,
       "xnailedUp": xnailedUp,
       "xisdnVersion": xisdnVersion,
       "xisdnSignalingTable": xisdnSignalingTable,
       "xisdnSignalingEntry": xisdnSignalingEntry,
       "isdnSignalingCallingAddress2": isdnSignalingCallingAddress2,
       "isdnEndpointSpid": isdnEndpointSpid,
       "isdnEndpointSpid2": isdnEndpointSpid2,
       "xisdnConformance": xisdnConformance,
       "xisdnCompliances": xisdnCompliances,
       "xisdnCompliance": xisdnCompliance,
       "xisdnGroups": xisdnGroups,
       "xisdnAllGroup": xisdnAllGroup}
)
