"""SNMP MIB module (QB-VLAN-MGMT-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QB-VLAN-MGMT-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 11:37:36 2024
On host MacBook-Pro.local platform Darwin version 23.4.0 by user lextm
Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]
"""
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(QbAtmAal5EncapsType,) = mibBuilder.importSymbols(
    "QB-DWS-MIB",
    "QbAtmAal5EncapsType")

(qbMibs,) = mibBuilder.importSymbols(
    "QUANTUMBRIDGE-REG",
    "qbMibs")

(ModuleCompliance,
 ObjectGroup,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "ObjectGroup",
    "NotificationGroup")

(Bits,
 Gauge32,
 NotificationType,
 Unsigned32,
 MibIdentifier,
 iso,
 ObjectIdentity,
 Integer32,
 ModuleIdentity,
 Counter64,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 IpAddress,
 Counter32) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Gauge32",
    "NotificationType",
    "Unsigned32",
    "MibIdentifier",
    "iso",
    "ObjectIdentity",
    "Integer32",
    "ModuleIdentity",
    "Counter64",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "IpAddress",
    "Counter32")

(TruthValue,
 RowStatus,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "TruthValue",
    "RowStatus",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

qbVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15)
)
qbVlanMIB.setLastUpdated("0107022155Z")
if mibBuilder.loadTexts:
    qbVlanMIB.setOrganization("""\
Quantum Bridge
""")
qbVlanMIB.setContactInfo("""\
mvaysman@quantumbridge.com
""")
if mibBuilder.loadTexts:
    qbVlanMIB.setDescription("""\
This module defines objects for the management of QB's proprietary VLAN
capability. This capability is based on Policing and Thresholding. The purpose
of the QBVLAN function is to provide provisioning and monitoring of VLANs set
up by the administrator.
""")


# Types definitions


# TEXTUAL-CONVENTIONS



class QbVlanPort(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )

    if mibBuilder.loadTexts:
        description = """\
VLAN port range
"""


class VlanIndex(TextualConvention, Unsigned32):
    status = "current"
    if mibBuilder.loadTexts:
        description = """\
A value used to index per-VLAN tables: values of 0 and 4095 are not permitted;
if the value is between 1 and 4094 inclusive, it represents an IEEE 802.1Q
VLAN-ID with global scope within a given bridged domain (see VlanId textual
convention). If the value is greater than 4095 then it represents a VLAN with
scope local to the particular agent, i.e. one without a global VLAN-ID assigned
to it. Such VLANs are outside the scope of IEEE 802.1Q but it is convenient to
be able to manage them in the same way using this MIB.
"""


# MIB Managed Objects in the order of their OIDs

_QbVlanObjects_ObjectIdentity = ObjectIdentity
qbVlanObjects = _QbVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1)
)
_QbVlanConfGroup_ObjectIdentity = ObjectIdentity
qbVlanConfGroup = _QbVlanConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 1)
)
_QbNextFreeVlanIndex_Type = VlanIndex
_QbNextFreeVlanIndex_Object = MibScalar
qbNextFreeVlanIndex = _QbNextFreeVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 1, 1),
    _QbNextFreeVlanIndex_Type()
)
qbNextFreeVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbNextFreeVlanIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbNextFreeVlanIndex.setDescription("""\
This is the lowest unused vlan index for the system. The next available value
for qbNextFreeVlanIndex of a local VLAN entry in qbVlanConfTableTable. This
will report values >=4096 if a new Local VLAN may be created or else the value
0 if this is not possible.
""")
_QbVlanNumVlans_Type = Integer32
_QbVlanNumVlans_Object = MibScalar
qbVlanNumVlans = _QbVlanNumVlans_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 1, 2),
    _QbVlanNumVlans_Type()
)
qbVlanNumVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVlanNumVlans.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanNumVlans.setDescription("""\
The total number of provisioned VLANs.
""")
_QbVlanConfTableLastUpdate_Type = TimeTicks
_QbVlanConfTableLastUpdate_Object = MibScalar
qbVlanConfTableLastUpdate = _QbVlanConfTableLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 1, 3),
    _QbVlanConfTableLastUpdate_Type()
)
qbVlanConfTableLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVlanConfTableLastUpdate.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanConfTableLastUpdate.setDescription("""\
The value of sysUpTime at the time of the last creation, deletion or
modification of an entry in the qbVlanConfTable. If the number of entries has
been unchanged since the last re-initialization of the agent, then this object
contains a zero value.
""")
_QbVlanConfTable_Object = MibTable
qbVlanConfTable = _QbVlanConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 1, 4)
)
if mibBuilder.loadTexts:
    qbVlanConfTable.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanConfTable.setDescription("""\
This table contains the data pertaining to Vlans. The table contains
configuration information for each VLAN configured into the device. All entries
are permanent and will be restored after the device is reset.
""")
_QbVlanConfEntry_Object = MibTableRow
qbVlanConfEntry = _QbVlanConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 1, 4, 1)
)
qbVlanConfEntry.setIndexNames(
    (0, "QB-VLAN-MGMT-MIB", "qbVlanConfIndex"),
)
if mibBuilder.loadTexts:
    qbVlanConfEntry.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanConfEntry.setDescription("""\
Each row provides data for a single vlan.
""")
_QbVlanConfIndex_Type = VlanIndex
_QbVlanConfIndex_Object = MibTableColumn
qbVlanConfIndex = _QbVlanConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 1, 4, 1, 1),
    _QbVlanConfIndex_Type()
)
qbVlanConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbVlanConfIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanConfIndex.setDescription("""\
This is the Vlan index for this VLAN. If the value is between 1 and 4094, it
represents an IEEE 802.1Q VLAN-ID with global scope within a given bridged
domain (see VlanId textual convention). If the value is greater than 4095 then
it represents a VLAN with scope local to the particular agent. Note that for
Release 3.0 the qbVlanConfIndex value ranges between 1 and 4095.
""")


class _QbVlanConfName_Type(DisplayString):
    """Custom type qbVlanConfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_QbVlanConfName_Type.__name__ = "DisplayString"
_QbVlanConfName_Object = MibTableColumn
qbVlanConfName = _QbVlanConfName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 1, 4, 1, 2),
    _QbVlanConfName_Type()
)
qbVlanConfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbVlanConfName.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanConfName.setDescription("""\
This is the unique user name assigned to this VLAN.
""")
_QbVlanConfSlot_Type = Integer32
_QbVlanConfSlot_Object = MibTableColumn
qbVlanConfSlot = _QbVlanConfSlot_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 1, 4, 1, 3),
    _QbVlanConfSlot_Type()
)
qbVlanConfSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbVlanConfSlot.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanConfSlot.setDescription("""\
This is the slot where this VLAN has been created.
""")
_QbVlanConfNextPort_Type = QbVlanPort
_QbVlanConfNextPort_Object = MibTableColumn
qbVlanConfNextPort = _QbVlanConfNextPort_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 1, 4, 1, 4),
    _QbVlanConfNextPort_Type()
)
qbVlanConfNextPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVlanConfNextPort.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanConfNextPort.setDescription("""\
This returns the lowest free VLAN port to be used.
""")
_QbVlanConfRowstatus_Type = RowStatus
_QbVlanConfRowstatus_Object = MibTableColumn
qbVlanConfRowstatus = _QbVlanConfRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 1, 4, 1, 5),
    _QbVlanConfRowstatus_Type()
)
qbVlanConfRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbVlanConfRowstatus.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanConfRowstatus.setDescription("""\
The row status column for this Vlan. This OBJECT can be set to: createAndGo(4)
destroy(6) The following values may be read: active(1) Setting this object to
createAndGo(4) causes the agent to attempt to create and commit the row based
on the contents of the objects in the row. If all necessary information is
present in the row and the values are acceptable to the agent, the agent will
change the status to active(1). If any of the necessary objects are not
available, the agent will reject the creation request. Setting this object to
destroy(6) will remove the corresponding entry in this table, and disable data
traffic.
""")
_QbVlanPortGroup_ObjectIdentity = ObjectIdentity
qbVlanPortGroup = _QbVlanPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 2)
)
_QbVlanPortConfTableLastUpdate_Type = TimeTicks
_QbVlanPortConfTableLastUpdate_Object = MibScalar
qbVlanPortConfTableLastUpdate = _QbVlanPortConfTableLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 2, 1),
    _QbVlanPortConfTableLastUpdate_Type()
)
qbVlanPortConfTableLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVlanPortConfTableLastUpdate.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanPortConfTableLastUpdate.setDescription("""\
The value of sysUpTime at the time of the last creation, deletion or
modification of an entry in the qbVlanConfTable. If the number of entries has
been unchanged since the last re-initialization of the agent, then this object
contains a zero value.
""")
_QbVlanPortConfTable_Object = MibTable
qbVlanPortConfTable = _QbVlanPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 2, 2)
)
if mibBuilder.loadTexts:
    qbVlanPortConfTable.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanPortConfTable.setDescription("""\
This table contains the data pertaining to Vlan ports and their connections.
The table contains per port control and status information for VLAN
configuration in the device.
""")
_QbVlanPortConfEntry_Object = MibTableRow
qbVlanPortConfEntry = _QbVlanPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 2, 2, 1)
)
qbVlanPortConfEntry.setIndexNames(
    (0, "QB-VLAN-MGMT-MIB", "qbVlanConfIndex"),
    (0, "QB-VLAN-MGMT-MIB", "qbVlanPortConfPort"),
)
if mibBuilder.loadTexts:
    qbVlanPortConfEntry.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanPortConfEntry.setDescription("""\
Each row provides data for a single vlan port.
""")
_QbVlanPortConfPort_Type = QbVlanPort
_QbVlanPortConfPort_Object = MibTableColumn
qbVlanPortConfPort = _QbVlanPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 2, 2, 1, 1),
    _QbVlanPortConfPort_Type()
)
qbVlanPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbVlanPortConfPort.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanPortConfPort.setDescription("""\
This is the Vlan port for this connection end-point.
""")


class _QbVlanPortConfPolicing_Type(Integer32):
    """Custom type qbVlanPortConfPolicing based on Integer32"""
    defaultValue = 2

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


_QbVlanPortConfPolicing_Type.__name__ = "Integer32"
_QbVlanPortConfPolicing_Object = MibTableColumn
qbVlanPortConfPolicing = _QbVlanPortConfPolicing_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 2, 2, 1, 2),
    _QbVlanPortConfPolicing_Type()
)
qbVlanPortConfPolicing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbVlanPortConfPolicing.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanPortConfPolicing.setDescription("""\
The object is used to enable or disable policing policy on a given port.
""")


class _QbVlanPortConfEncapsulation_Type(QbAtmAal5EncapsType):
    """Custom type qbVlanPortConfEncapsulation based on QbAtmAal5EncapsType"""


_QbVlanPortConfEncapsulation_Object = MibTableColumn
qbVlanPortConfEncapsulation = _QbVlanPortConfEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 2, 2, 1, 3),
    _QbVlanPortConfEncapsulation_Type()
)
qbVlanPortConfEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbVlanPortConfEncapsulation.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanPortConfEncapsulation.setDescription("""\
The type of data encapsulation used over the AAL5 SSCS layer. The definitions
reference RFC 1483 Multiprotocol Encapsulation over ATM AAL5 and to the ATM
Forum LAN Emulation specification.
""")


class _QbVlanPortConfAdmitFrameTypes_Type(Integer32):
    """Custom type qbVlanPortConfAdmitFrameTypes based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admitAll", 1),
          ("admitOnlyVlanTagged", 2))
    )


_QbVlanPortConfAdmitFrameTypes_Type.__name__ = "Integer32"
_QbVlanPortConfAdmitFrameTypes_Object = MibTableColumn
qbVlanPortConfAdmitFrameTypes = _QbVlanPortConfAdmitFrameTypes_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 2, 2, 1, 4),
    _QbVlanPortConfAdmitFrameTypes_Type()
)
qbVlanPortConfAdmitFrameTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbVlanPortConfAdmitFrameTypes.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanPortConfAdmitFrameTypes.setDescription("""\
When this is admitOnlyVlanTagged the device will discard any untagged frames or
priority-tagged frames received on this port. When admitAll, untagged frames or
priority-tagged frames received will be accepted and tagged with the VLAN id.
This applies to the traffic from the GigE card to the backplane only.
""")


class _QbVlanPortConfTagging_Type(Integer32):
    """Custom type qbVlanPortConfTagging based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dissable", 2),
          ("enable", 1))
    )


_QbVlanPortConfTagging_Type.__name__ = "Integer32"
_QbVlanPortConfTagging_Object = MibTableColumn
qbVlanPortConfTagging = _QbVlanPortConfTagging_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 2, 2, 1, 5),
    _QbVlanPortConfTagging_Type()
)
qbVlanPortConfTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbVlanPortConfTagging.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanPortConfTagging.setDescription("""\
When this value is set to disable, the VLAN tags will be removed from the
outgoing packets. This applies to the traffic from the GigE card to the
backplane only.
""")
_QbVlanPortStatsTable_Object = MibTable
qbVlanPortStatsTable = _QbVlanPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 2, 3)
)
if mibBuilder.loadTexts:
    qbVlanPortStatsTable.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanPortStatsTable.setDescription("""\
This table contains the statistics pertaining to connection end-points on a
VLAN port.
""")
_QbVlanPortStatsEntry_Object = MibTableRow
qbVlanPortStatsEntry = _QbVlanPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 2, 3, 1)
)
qbVlanPortConfEntry.registerAugmentions(
    ("QB-VLAN-MGMT-MIB",
     "qbVlanPortStatsEntry")
)
qbVlanPortStatsEntry.setIndexNames(*qbVlanPortConfEntry.getIndexNames())
if mibBuilder.loadTexts:
    qbVlanPortStatsEntry.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanPortStatsEntry.setDescription("""\
Each row provides stats data for a single VLAN port.
""")
_QbVlanPortStatsAal5CRCErrors_Type = Counter32
_QbVlanPortStatsAal5CRCErrors_Object = MibTableColumn
qbVlanPortStatsAal5CRCErrors = _QbVlanPortStatsAal5CRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 2, 3, 1, 1),
    _QbVlanPortStatsAal5CRCErrors_Type()
)
qbVlanPortStatsAal5CRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVlanPortStatsAal5CRCErrors.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanPortStatsAal5CRCErrors.setDescription("""\
A count of the number of AAL5 CRC errors.
""")
_QbVlanPortStatsAal5SarTimeouts_Type = Counter32
_QbVlanPortStatsAal5SarTimeouts_Object = MibTableColumn
qbVlanPortStatsAal5SarTimeouts = _QbVlanPortStatsAal5SarTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 2, 3, 1, 2),
    _QbVlanPortStatsAal5SarTimeouts_Type()
)
qbVlanPortStatsAal5SarTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVlanPortStatsAal5SarTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanPortStatsAal5SarTimeouts.setDescription("""\
A count of the number of AAL5 SAR timeouts.
""")
_QbVlanPortStatsAal5OversizeSDUs_Type = Counter32
_QbVlanPortStatsAal5OversizeSDUs_Object = MibTableColumn
qbVlanPortStatsAal5OversizeSDUs = _QbVlanPortStatsAal5OversizeSDUs_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 2, 3, 1, 3),
    _QbVlanPortStatsAal5OversizeSDUs_Type()
)
qbVlanPortStatsAal5OversizeSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVlanPortStatsAal5OversizeSDUs.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanPortStatsAal5OversizeSDUs.setDescription("""\
A count of the number of AAL5 oversized SDUs.
""")
_QbVlanPortStatsAal5UpstreamPkts_Type = Counter32
_QbVlanPortStatsAal5UpstreamPkts_Object = MibTableColumn
qbVlanPortStatsAal5UpstreamPkts = _QbVlanPortStatsAal5UpstreamPkts_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 2, 3, 1, 4),
    _QbVlanPortStatsAal5UpstreamPkts_Type()
)
qbVlanPortStatsAal5UpstreamPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVlanPortStatsAal5UpstreamPkts.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanPortStatsAal5UpstreamPkts.setDescription("""\
A count of the number of packets passed in the upstream direction. (i.e. from
GigE card to backplane)
""")
_QbVlanPortStatsAal5DownstreamPkts_Type = Counter32
_QbVlanPortStatsAal5DownstreamPkts_Object = MibTableColumn
qbVlanPortStatsAal5DownstreamPkts = _QbVlanPortStatsAal5DownstreamPkts_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 2, 3, 1, 5),
    _QbVlanPortStatsAal5DownstreamPkts_Type()
)
qbVlanPortStatsAal5DownstreamPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVlanPortStatsAal5DownstreamPkts.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanPortStatsAal5DownstreamPkts.setDescription("""\
A count of the number of packets passed in the downstream direction. (i.e. from
the backplane to GigE card on this port)
""")
_QbVlanPortStatsAal5UpstreamOctets_Type = Counter32
_QbVlanPortStatsAal5UpstreamOctets_Object = MibTableColumn
qbVlanPortStatsAal5UpstreamOctets = _QbVlanPortStatsAal5UpstreamOctets_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 2, 3, 1, 6),
    _QbVlanPortStatsAal5UpstreamOctets_Type()
)
qbVlanPortStatsAal5UpstreamOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVlanPortStatsAal5UpstreamOctets.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanPortStatsAal5UpstreamOctets.setDescription("""\
 A count of the number of octets passed in the upstream direction. (i.e. from
GigE card to backplane)
""")
_QbVlanPortStatsAal5DownStreamOctets_Type = Counter32
_QbVlanPortStatsAal5DownStreamOctets_Object = MibTableColumn
qbVlanPortStatsAal5DownStreamOctets = _QbVlanPortStatsAal5DownStreamOctets_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 2, 3, 1, 7),
    _QbVlanPortStatsAal5DownStreamOctets_Type()
)
qbVlanPortStatsAal5DownStreamOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVlanPortStatsAal5DownStreamOctets.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanPortStatsAal5DownStreamOctets.setDescription("""\
 A count of the number of octets passed in the downstream direction. (i.e. from
the backplane to GigE card on this port)
""")
_QbVlanPortStatsUpstreamPktDiscards_Type = Counter32
_QbVlanPortStatsUpstreamPktDiscards_Object = MibTableColumn
qbVlanPortStatsUpstreamPktDiscards = _QbVlanPortStatsUpstreamPktDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 2, 3, 1, 8),
    _QbVlanPortStatsUpstreamPktDiscards_Type()
)
qbVlanPortStatsUpstreamPktDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVlanPortStatsUpstreamPktDiscards.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanPortStatsUpstreamPktDiscards.setDescription("""\
 A count of the number of packets discarded in the upstream direction. (i.e.
from GigE card to backplane)
""")
_QbVlanPortStatsDownsteamPktDiscards_Type = Counter32
_QbVlanPortStatsDownsteamPktDiscards_Object = MibTableColumn
qbVlanPortStatsDownsteamPktDiscards = _QbVlanPortStatsDownsteamPktDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 1, 2, 3, 1, 9),
    _QbVlanPortStatsDownsteamPktDiscards_Type()
)
qbVlanPortStatsDownsteamPktDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVlanPortStatsDownsteamPktDiscards.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanPortStatsDownsteamPktDiscards.setDescription("""\
 A count of the number of packets discarded in the downstream direction. (i.e.
from the backplane to GigE card on this port)
""")
_QbVlanNotifications_ObjectIdentity = ObjectIdentity
qbVlanNotifications = _QbVlanNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 2)
)
_QbVlanNotificationPrefix_ObjectIdentity = ObjectIdentity
qbVlanNotificationPrefix = _QbVlanNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 2, 0)
)
_QbVlanConformance_ObjectIdentity = ObjectIdentity
qbVlanConformance = _QbVlanConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 3)
)
_QbVlanCompliances_ObjectIdentity = ObjectIdentity
qbVlanCompliances = _QbVlanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 3, 1)
)
_QbVlanGroups_ObjectIdentity = ObjectIdentity
qbVlanGroups = _QbVlanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 3, 2)
)

# Managed Objects groups

qbVlanGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 3, 2, 1)
)
qbVlanGroupInfo.setObjects(
      *(("QB-VLAN-MGMT-MIB", "qbVlanConfName"),
        ("QB-VLAN-MGMT-MIB", "qbVlanConfSlot"),
        ("QB-VLAN-MGMT-MIB", "qbVlanConfNextPort"),
        ("QB-VLAN-MGMT-MIB", "qbVlanConfRowstatus"),
        ("QB-VLAN-MGMT-MIB", "qbVlanPortConfPolicing"),
        ("QB-VLAN-MGMT-MIB", "qbVlanPortConfEncapsulation"),
        ("QB-VLAN-MGMT-MIB", "qbVlanPortConfAdmitFrameTypes"),
        ("QB-VLAN-MGMT-MIB", "qbVlanPortConfTagging"))
)
if mibBuilder.loadTexts:
    qbVlanGroupInfo.setStatus("current")
if mibBuilder.loadTexts:
    qbVlanGroupInfo.setDescription("""\
The set of all accessible objects in this MIB.
""")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qbVlanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4323, 2, 15, 3, 1, 1)
)
if mibBuilder.loadTexts:
    qbVlanCompliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    qbVlanCompliance.setDescription("""\
The compliance statement for all agents that support this MIB. A compliant
agent implements all objects defined in this MIB.
""")


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QB-VLAN-MGMT-MIB",
    **{"QbVlanPort": QbVlanPort,
       "VlanIndex": VlanIndex,
       "qbVlanMIB": qbVlanMIB,
       "qbVlanObjects": qbVlanObjects,
       "qbVlanConfGroup": qbVlanConfGroup,
       "qbNextFreeVlanIndex": qbNextFreeVlanIndex,
       "qbVlanNumVlans": qbVlanNumVlans,
       "qbVlanConfTableLastUpdate": qbVlanConfTableLastUpdate,
       "qbVlanConfTable": qbVlanConfTable,
       "qbVlanConfEntry": qbVlanConfEntry,
       "qbVlanConfIndex": qbVlanConfIndex,
       "qbVlanConfName": qbVlanConfName,
       "qbVlanConfSlot": qbVlanConfSlot,
       "qbVlanConfNextPort": qbVlanConfNextPort,
       "qbVlanConfRowstatus": qbVlanConfRowstatus,
       "qbVlanPortGroup": qbVlanPortGroup,
       "qbVlanPortConfTableLastUpdate": qbVlanPortConfTableLastUpdate,
       "qbVlanPortConfTable": qbVlanPortConfTable,
       "qbVlanPortConfEntry": qbVlanPortConfEntry,
       "qbVlanPortConfPort": qbVlanPortConfPort,
       "qbVlanPortConfPolicing": qbVlanPortConfPolicing,
       "qbVlanPortConfEncapsulation": qbVlanPortConfEncapsulation,
       "qbVlanPortConfAdmitFrameTypes": qbVlanPortConfAdmitFrameTypes,
       "qbVlanPortConfTagging": qbVlanPortConfTagging,
       "qbVlanPortStatsTable": qbVlanPortStatsTable,
       "qbVlanPortStatsEntry": qbVlanPortStatsEntry,
       "qbVlanPortStatsAal5CRCErrors": qbVlanPortStatsAal5CRCErrors,
       "qbVlanPortStatsAal5SarTimeouts": qbVlanPortStatsAal5SarTimeouts,
       "qbVlanPortStatsAal5OversizeSDUs": qbVlanPortStatsAal5OversizeSDUs,
       "qbVlanPortStatsAal5UpstreamPkts": qbVlanPortStatsAal5UpstreamPkts,
       "qbVlanPortStatsAal5DownstreamPkts": qbVlanPortStatsAal5DownstreamPkts,
       "qbVlanPortStatsAal5UpstreamOctets": qbVlanPortStatsAal5UpstreamOctets,
       "qbVlanPortStatsAal5DownStreamOctets": qbVlanPortStatsAal5DownStreamOctets,
       "qbVlanPortStatsUpstreamPktDiscards": qbVlanPortStatsUpstreamPktDiscards,
       "qbVlanPortStatsDownsteamPktDiscards": qbVlanPortStatsDownsteamPktDiscards,
       "qbVlanNotifications": qbVlanNotifications,
       "qbVlanNotificationPrefix": qbVlanNotificationPrefix,
       "qbVlanConformance": qbVlanConformance,
       "qbVlanCompliances": qbVlanCompliances,
       "qbVlanCompliance": qbVlanCompliance,
       "qbVlanGroups": qbVlanGroups,
       "qbVlanGroupInfo": qbVlanGroupInfo}
)
