# SNMP MIB module (ATT-CNM-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATT-CNM-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:20 2024
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

_Att_2_ObjectIdentity = ObjectIdentity
att_2 = _Att_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74)
)
_Att_products_ObjectIdentity = ObjectIdentity
att_products = _Att_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 1)
)
_Att_cnmAgent_ObjectIdentity = ObjectIdentity
att_cnmAgent = _Att_cnmAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 1, 9)
)
_Att_mgmt_ObjectIdentity = ObjectIdentity
att_mgmt = _Att_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2)
)
_Att_cnm_ObjectIdentity = ObjectIdentity
att_cnm = _Att_cnm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 15)
)
_Att_cnm_system_ObjectIdentity = ObjectIdentity
att_cnm_system = _Att_cnm_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 1)
)


class _AttCNMsysDescr_Type(DisplayString):
    """Custom type attCNMsysDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AttCNMsysDescr_Type.__name__ = "DisplayString"
_AttCNMsysDescr_Object = MibScalar
attCNMsysDescr = _AttCNMsysDescr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 1, 1),
    _AttCNMsysDescr_Type()
)
attCNMsysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsysDescr.setStatus("mandatory")
_AttCNMsysObjectID_Type = ObjectIdentifier
_AttCNMsysObjectID_Object = MibScalar
attCNMsysObjectID = _AttCNMsysObjectID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 1, 2),
    _AttCNMsysObjectID_Type()
)
attCNMsysObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsysObjectID.setStatus("mandatory")
_AttCNMsysUpTime_Type = TimeTicks
_AttCNMsysUpTime_Object = MibScalar
attCNMsysUpTime = _AttCNMsysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 1, 3),
    _AttCNMsysUpTime_Type()
)
attCNMsysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsysUpTime.setStatus("mandatory")


class _AttCNMsysContact_Type(DisplayString):
    """Custom type attCNMsysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AttCNMsysContact_Type.__name__ = "DisplayString"
_AttCNMsysContact_Object = MibScalar
attCNMsysContact = _AttCNMsysContact_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 1, 4),
    _AttCNMsysContact_Type()
)
attCNMsysContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsysContact.setStatus("mandatory")


class _AttCNMsysName_Type(DisplayString):
    """Custom type attCNMsysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AttCNMsysName_Type.__name__ = "DisplayString"
_AttCNMsysName_Object = MibScalar
attCNMsysName = _AttCNMsysName_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 1, 5),
    _AttCNMsysName_Type()
)
attCNMsysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsysName.setStatus("mandatory")


class _AttCNMsysLocation_Type(DisplayString):
    """Custom type attCNMsysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AttCNMsysLocation_Type.__name__ = "DisplayString"
_AttCNMsysLocation_Object = MibScalar
attCNMsysLocation = _AttCNMsysLocation_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 1, 6),
    _AttCNMsysLocation_Type()
)
attCNMsysLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsysLocation.setStatus("mandatory")


class _AttCNMsysServices_Type(Integer32):
    """Custom type attCNMsysServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AttCNMsysServices_Type.__name__ = "Integer32"
_AttCNMsysServices_Object = MibScalar
attCNMsysServices = _AttCNMsysServices_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 1, 7),
    _AttCNMsysServices_Type()
)
attCNMsysServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsysServices.setStatus("mandatory")
_Att_cnm_interfaces_ObjectIdentity = ObjectIdentity
att_cnm_interfaces = _Att_cnm_interfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 2)
)
_AttCNMifNumber_Type = Integer32
_AttCNMifNumber_Object = MibScalar
attCNMifNumber = _AttCNMifNumber_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 2, 1),
    _AttCNMifNumber_Type()
)
attCNMifNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMifNumber.setStatus("mandatory")
_AttCNMifConfigTable_Object = MibTable
attCNMifConfigTable = _AttCNMifConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 2, 2)
)
if mibBuilder.loadTexts:
    attCNMifConfigTable.setStatus("mandatory")
_AttCNMifConfigEntry_Object = MibTableRow
attCNMifConfigEntry = _AttCNMifConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 2, 2, 1)
)
attCNMifConfigEntry.setIndexNames(
    (0, "ATT-CNM-SYSTEM-MIB", "attCNMifConfigIndex"),
)
if mibBuilder.loadTexts:
    attCNMifConfigEntry.setStatus("mandatory")
_AttCNMifConfigIndex_Type = Integer32
_AttCNMifConfigIndex_Object = MibTableColumn
attCNMifConfigIndex = _AttCNMifConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 2, 2, 1, 1),
    _AttCNMifConfigIndex_Type()
)
attCNMifConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMifConfigIndex.setStatus("mandatory")


class _AttCNMifDescr_Type(DisplayString):
    """Custom type attCNMifDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AttCNMifDescr_Type.__name__ = "DisplayString"
_AttCNMifDescr_Object = MibTableColumn
attCNMifDescr = _AttCNMifDescr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 2, 2, 1, 2),
    _AttCNMifDescr_Type()
)
attCNMifDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMifDescr.setStatus("mandatory")


class _AttCNMifType_Type(Integer32):
    """Custom type attCNMifType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("frame-relay", 32),
          ("other", 1),
          ("sip", 31))
    )


_AttCNMifType_Type.__name__ = "Integer32"
_AttCNMifType_Object = MibTableColumn
attCNMifType = _AttCNMifType_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 2, 2, 1, 3),
    _AttCNMifType_Type()
)
attCNMifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMifType.setStatus("mandatory")
_AttCNMifMtu_Type = Integer32
_AttCNMifMtu_Object = MibTableColumn
attCNMifMtu = _AttCNMifMtu_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 2, 2, 1, 4),
    _AttCNMifMtu_Type()
)
attCNMifMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMifMtu.setStatus("mandatory")
_AttCNMifSpeed_Type = Gauge32
_AttCNMifSpeed_Object = MibTableColumn
attCNMifSpeed = _AttCNMifSpeed_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 2, 2, 1, 5),
    _AttCNMifSpeed_Type()
)
attCNMifSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMifSpeed.setStatus("mandatory")


class _AttCNMifContact_Type(DisplayString):
    """Custom type attCNMifContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AttCNMifContact_Type.__name__ = "DisplayString"
_AttCNMifContact_Object = MibTableColumn
attCNMifContact = _AttCNMifContact_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 2, 2, 1, 6),
    _AttCNMifContact_Type()
)
attCNMifContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMifContact.setStatus("mandatory")


class _AttCNMifLocation_Type(DisplayString):
    """Custom type attCNMifLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AttCNMifLocation_Type.__name__ = "DisplayString"
_AttCNMifLocation_Object = MibTableColumn
attCNMifLocation = _AttCNMifLocation_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 2, 2, 1, 7),
    _AttCNMifLocation_Type()
)
attCNMifLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMifLocation.setStatus("mandatory")


class _AttCNMifSubscriber_Type(DisplayString):
    """Custom type attCNMifSubscriber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AttCNMifSubscriber_Type.__name__ = "DisplayString"
_AttCNMifSubscriber_Object = MibTableColumn
attCNMifSubscriber = _AttCNMifSubscriber_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 2, 2, 1, 8),
    _AttCNMifSubscriber_Type()
)
attCNMifSubscriber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMifSubscriber.setStatus("mandatory")
_AttCNMifStatusTable_Object = MibTable
attCNMifStatusTable = _AttCNMifStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 2, 3)
)
if mibBuilder.loadTexts:
    attCNMifStatusTable.setStatus("mandatory")
_AttCNMifStatusEntry_Object = MibTableRow
attCNMifStatusEntry = _AttCNMifStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 2, 3, 1)
)
attCNMifStatusEntry.setIndexNames(
    (0, "ATT-CNM-SYSTEM-MIB", "attCNMifStatusIndex"),
)
if mibBuilder.loadTexts:
    attCNMifStatusEntry.setStatus("mandatory")
_AttCNMifStatusIndex_Type = Integer32
_AttCNMifStatusIndex_Object = MibTableColumn
attCNMifStatusIndex = _AttCNMifStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 2, 3, 1, 1),
    _AttCNMifStatusIndex_Type()
)
attCNMifStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMifStatusIndex.setStatus("mandatory")


class _AttCNMifAdminStatus_Type(Integer32):
    """Custom type attCNMifAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_AttCNMifAdminStatus_Type.__name__ = "Integer32"
_AttCNMifAdminStatus_Object = MibTableColumn
attCNMifAdminStatus = _AttCNMifAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 2, 3, 1, 2),
    _AttCNMifAdminStatus_Type()
)
attCNMifAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMifAdminStatus.setStatus("mandatory")


class _AttCNMifOperStatus_Type(Integer32):
    """Custom type attCNMifOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_AttCNMifOperStatus_Type.__name__ = "Integer32"
_AttCNMifOperStatus_Object = MibTableColumn
attCNMifOperStatus = _AttCNMifOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 2, 3, 1, 3),
    _AttCNMifOperStatus_Type()
)
attCNMifOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMifOperStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATT-CNM-SYSTEM-MIB",
    **{"att-2": att_2,
       "att-products": att_products,
       "att-cnmAgent": att_cnmAgent,
       "att-mgmt": att_mgmt,
       "att-cnm": att_cnm,
       "att-cnm-system": att_cnm_system,
       "attCNMsysDescr": attCNMsysDescr,
       "attCNMsysObjectID": attCNMsysObjectID,
       "attCNMsysUpTime": attCNMsysUpTime,
       "attCNMsysContact": attCNMsysContact,
       "attCNMsysName": attCNMsysName,
       "attCNMsysLocation": attCNMsysLocation,
       "attCNMsysServices": attCNMsysServices,
       "att-cnm-interfaces": att_cnm_interfaces,
       "attCNMifNumber": attCNMifNumber,
       "attCNMifConfigTable": attCNMifConfigTable,
       "attCNMifConfigEntry": attCNMifConfigEntry,
       "attCNMifConfigIndex": attCNMifConfigIndex,
       "attCNMifDescr": attCNMifDescr,
       "attCNMifType": attCNMifType,
       "attCNMifMtu": attCNMifMtu,
       "attCNMifSpeed": attCNMifSpeed,
       "attCNMifContact": attCNMifContact,
       "attCNMifLocation": attCNMifLocation,
       "attCNMifSubscriber": attCNMifSubscriber,
       "attCNMifStatusTable": attCNMifStatusTable,
       "attCNMifStatusEntry": attCNMifStatusEntry,
       "attCNMifStatusIndex": attCNMifStatusIndex,
       "attCNMifAdminStatus": attCNMifAdminStatus,
       "attCNMifOperStatus": attCNMifOperStatus}
)
